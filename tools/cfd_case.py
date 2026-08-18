"""Bangun case OpenFOAM flowbench dari STL port.

Flowbench: plenum bola pada tekanan total tetap -> port -> keluar throat pada
tekanan statik 0. Beda tekanan = depresi flowbench. Yang diukur: debit lewat
throat, dari situ CFM dan koefisien flow.

Solver: simpleFoam (steady, incompressible) + k-omega SST.
ponytail: incompressible. Di 28"H2O Mach ~0.31 jadi CFM absolut agak optimis,
tapi PERINGKAT antar varian tidak terpengaruh. Naikkan ke rhoSimpleFoam kalau
mau dibandingkan langsung dgn flowbench nyata.
"""
import math
import os
import re
import numpy as np

# --------------------------------------------------------------- KONSTAN
RHO = 1.204            # kg/m3
NU = 1.5e-5            # m2/s
PA_PER_INH2O = 249.089

# Solver dijalankan di depresi RENDAH, hasil dilaporkan di 28"H2O.
# Alasannya dua-duanya nyata:
#  1) di 28" kecepatan throat ~107 m/s (Mach 0.31) -- terlalu tinggi untuk
#     solver incompressible; di 10" jadi ~64 m/s (Mach 0.19), jauh lebih sah
#  2) start dingin dgn beda tekanan besar bikin simpleFoam diverge
# Konversi pakai akar rasio depresi -- ini praktik baku flowbench, bukan akal2an.
# Sah karena di Re > 1e5 koefisien flow praktis tidak tergantung Re.
RUN_INH2O = 10.0       # yang benar-benar disimulasikan
BENCH_INH2O = 28.0     # acuan pelaporan

HEAD = """/*--------------------------------*- C++ -*----------------------------------*\\
\\*---------------------------------------------------------------------------*/
FoamFile
{{
    version 2.0; format ascii; class {cls}; {loc}object {obj};
}}
"""


def _hdr(cls, obj, loc=None):
    return HEAD.format(cls=cls, obj=obj, loc=f'location "{loc}"; ' if loc else "")


def stl_bounds(path):
    """Baca vertex dari STL ascii, kembalikan bbox dalam mm."""
    pts = []
    with open(path) as f:
        for line in f:
            if line.lstrip().startswith("vertex"):
                pts.append([float(x) for x in line.split()[1:4]])
    p = np.array(pts)
    return p.min(axis=0), p.max(axis=0)


def split_axes(extent, n_proc):
    """Bagi n_proc jadi (nx,ny,nz) dgn membelah sumbu terpanjang berulang kali.
    Blok jadi mendekati kubus -> komunikasi antar-proses minimum."""
    n = [1, 1, 1]
    rem = int(n_proc)
    for f in _factors(rem):
        sizes = [extent[i] / n[i] for i in range(3)]
        n[sizes.index(max(sizes))] *= f
    assert n[0] * n[1] * n[2] == n_proc, (n, n_proc)
    return n


def _factors(n):
    """Faktor prima menurun, biar pembelahan besar didahulukan."""
    out, d = [], 2
    while d * d <= n:
        while n % d == 0:
            out.append(d); n //= d
        d += 1
    if n > 1:
        out.append(n)
    return sorted(out, reverse=True)


def build(stl_path, case_dir, depresi_inh2o=RUN_INH2O, bg_cell_mm=5.0,
          n_layers=6, iters=3000, n_proc=8):
    # iters 1500 terbukti kurang pada mesh halus: residual Ux masih 3.1e-3 dan
    # nyaris berhenti turun. residualControl tetap menghentikan lebih awal
    # kalau memang sudah konvergen, jadi batas tinggi tidak memboroskan apa-apa.
    import shutil
    os.makedirs(case_dir, exist_ok=True)
    # sisa "0" dari build lama bikin decomposePar mencari patch yg belum ada
    shutil.rmtree(os.path.join(case_dir, "0"), ignore_errors=True)
    # field ditaruh di 0.orig, BUKAN 0: decomposePar jalan sebelum snappyHexMesh,
    # saat itu mesh masih background dan patch inlet/outlet/wall belum ada.
    # 0.orig disalin ke tiap processor*/0 setelah meshing (alur baku OpenFOAM).
    for d in ("system", "constant/triSurface", "0.orig"):
        os.makedirs(os.path.join(case_dir, d), exist_ok=True)

    lo, hi = stl_bounds(stl_path)
    pad = bg_cell_mm * 2
    lo = (lo - pad) / 1000.0                      # mm -> m
    hi = (hi + pad) / 1000.0
    n = np.maximum(np.ceil((hi - lo) / (bg_cell_mm / 1000.0)), 4).astype(int)

    # tekanan kinematik (simpleFoam incompressible: p adalah p/rho)
    dp = depresi_inh2o * PA_PER_INH2O / RHO

    # titik di dalam fluida: sedikit masuk dari bidang keluar throat,
    # sepanjang sumbu klep. Throat dikunci 20.2mm jadi titik ini selalu aman.
    tilt = math.radians(13.0)
    loc = (0.005 * math.sin(tilt), 0.0, 0.005 * math.cos(tilt))

    shutil.copy(stl_path, os.path.join(case_dir, "constant/triSurface/port.stl"))
    core_src = stl_path.replace(".stl", "_core.stl")
    if not os.path.exists(core_src):
        raise FileNotFoundError(
            f"{core_src} tidak ada -- port_geom.generate() harus menulisnya. "
            "Tanpa refinementRegion inti port, aliran utama dihitung di sel kasar.")
    shutil.copy(core_src, os.path.join(case_dir, "constant/triSurface/port_core.stl"))

    w = lambda rel, txt: open(os.path.join(case_dir, rel), "w").write(txt)

    # ---------------------------------------------------------- blockMesh
    v = [(lo[0], lo[1], lo[2]), (hi[0], lo[1], lo[2]), (hi[0], hi[1], lo[2]),
         (lo[0], hi[1], lo[2]), (lo[0], lo[1], hi[2]), (hi[0], lo[1], hi[2]),
         (hi[0], hi[1], hi[2]), (lo[0], hi[1], hi[2])]
    verts = "\n".join(f"    ({a:.6f} {b:.6f} {c:.6f})" for a, b, c in v)
    w("system/blockMeshDict", _hdr("dictionary", "blockMeshDict", "system") + f"""
scale 1;
vertices
(
{verts}
);
blocks ( hex (0 1 2 3 4 5 6 7) ({n[0]} {n[1]} {n[2]}) simpleGrading (1 1 1) );
edges ();
boundary
(
    bg {{ type patch; faces ( (0 3 2 1) (4 5 6 7) (0 1 5 4) (2 3 7 6) (0 4 7 3) (1 2 6 5) ); }}
);
mergePatchPairs ();
""")

    # ------------------------------------------------------ snappyHexMesh
    w("system/snappyHexMeshDict", _hdr("dictionary", "snappyHexMeshDict", "system") + f"""
castellatedMesh true; snap true; addLayers true;

geometry
{{
    port.stl
    {{
        type triSurfaceMesh; name port; scale 0.001;
        regions {{ inlet {{ name inlet; }} outlet {{ name outlet; }}
                   wall {{ name wall; }} flange {{ name flange; }} }}
    }}
    // hanya untuk refinement volume, bukan permukaan mesh
    port_core.stl {{ type triSurfaceMesh; name portcore; scale 0.001; }}
}}

castellatedMeshControls
{{
    maxLocalCells 4000000; maxGlobalCells 12000000;
    minRefinementCells 10; maxLoadUnbalance 0.10; nCellsBetweenLevels 3;
    features ( {{ file "port.eMesh"; level 3; }} );
    refinementSurfaces
    {{
        port
        {{
            level (2 2);
            regions
            {{
                wall   {{ level (3 4); patchInfo {{ type wall; }} }}
                inlet  {{ level (0 1); patchInfo {{ type patch; }} }}
                outlet {{ level (4 4); patchInfo {{ type patch; }} }}
                // pelat flange: kasar. Kalau ikut level wall, mesh meledak 5x.
                flange {{ level (0 1); patchInfo {{ type wall; }} }}
            }}
        }}
    }}
    resolveFeatureAngle 30;
    // INTI port dihaluskan sampai level 3 (~0.6mm) -> ~30 sel melintang.
    // Tanpa ini intinya cuma ~4 sel dan hasilnya tidak berarti.
    refinementRegions {{ portcore {{ mode inside; levels ((1e15 3)); }} }}
    locationInMesh ({loc[0]:.6f} {loc[1]:.6f} {loc[2]:.6f});
    allowFreeStandingZoneFaces false;
}}

snapControls
{{
    nSmoothPatch 3; tolerance 2.0; nSolveIter 50; nRelaxIter 6;
    nFeatureSnapIter 12; implicitFeatureSnap false; explicitFeatureSnap true;
    multiRegionFeatureSnap false;
}}

addLayersControls
{{
    relativeSizes true;
    layers {{ wall {{ nSurfaceLayers {n_layers}; }} }}
    expansionRatio 1.20; finalLayerThickness 0.45; minThickness 0.08;
    nGrow 0; featureAngle 130; slipFeatureAngle 30;
    nRelaxIter 5; nSmoothSurfaceNormals 1; nSmoothNormals 3; nSmoothThickness 10;
    maxFaceThicknessRatio 0.5; maxThicknessToMedialRatio 0.3;
    minMedialAxisAngle 90; nBufferCellsNoExtrude 0; nLayerIter 50;
}}

meshQualityControls
{{
    maxNonOrtho 65; maxBoundarySkewness 20; maxInternalSkewness 4;
    maxConcave 80; minVol 1e-13; minTetQuality 1e-15; minArea -1;
    minTwist 0.02; minDeterminant 0.001; minFaceWeight 0.02; minVolRatio 0.01;
    minTriangleTwist -1; nSmoothScale 4; errorReduction 0.75;
}}
mergeTolerance 1e-6;
""")

    w("system/surfaceFeatureExtractDict", _hdr("dictionary", "surfaceFeatureExtractDict", "system") + """
port.stl { extractionMethod extractFromSurface; includedAngle 150; subsetFeatures { nonManifoldEdges no; openEdges yes; } writeObj no; }
""")

    # ------------------------------------------------------------- fields
    w("0.orig/p", _hdr("volScalarField", "p", "0") + f"""
dimensions [0 2 -2 0 0 0 0];
internalField uniform 0;
boundaryField
{{
    #includeEtc "caseDicts/setConstraintTypes"
    inlet  {{ type totalPressure; p0 uniform {dp:.1f}; value uniform {dp:.1f}; }}
    outlet {{ type fixedValue; value uniform 0; }}
    "(wall|flange)" {{ type zeroGradient; }}
}}
""")
    w("0.orig/U", _hdr("volVectorField", "U", "0") + """
dimensions [0 1 -1 0 0 0 0];
internalField uniform (0 0 0);
boundaryField
{
    #includeEtc "caseDicts/setConstraintTypes"
    inlet  { type pressureInletOutletVelocity; value uniform (0 0 0); }
    outlet { type zeroGradient; }
    "(wall|flange)" { type noSlip; }
}
""")
    w("0.orig/k", _hdr("volScalarField", "k", "0") + """
dimensions [0 2 -2 0 0 0 0];
internalField uniform 1.0;
boundaryField
{
    #includeEtc "caseDicts/setConstraintTypes"
    inlet  { type inletOutlet; inletValue uniform 1.0; value uniform 1.0; }
    outlet { type zeroGradient; }
    "(wall|flange)" { type kqRWallFunction; value uniform 1.0; }
}
""")
    w("0.orig/omega", _hdr("volScalarField", "omega", "0") + """
dimensions [0 0 -1 0 0 0 0];
internalField uniform 500;
boundaryField
{
    #includeEtc "caseDicts/setConstraintTypes"
    inlet  { type inletOutlet; inletValue uniform 500; value uniform 500; }
    outlet { type zeroGradient; }
    "(wall|flange)" { type omegaWallFunction; value uniform 500; }
}
""")
    w("0.orig/nut", _hdr("volScalarField", "nut", "0") + """
dimensions [0 2 -1 0 0 0 0];
internalField uniform 0;
boundaryField
{
    #includeEtc "caseDicts/setConstraintTypes"
    inlet  { type calculated; value uniform 0; }
    outlet { type calculated; value uniform 0; }
    "(wall|flange)" { type nutkWallFunction; value uniform 0; }
}
""")

    w("constant/transportProperties", _hdr("dictionary", "transportProperties", "constant") + f"""
transportModel Newtonian;
nu [0 2 -1 0 0 0 0] {NU};
""")
    w("constant/turbulenceProperties", _hdr("dictionary", "turbulenceProperties", "constant") + """
simulationType RAS;
RAS { RASModel kOmegaSST; turbulence on; printCoeffs on; }
""")

    # ------------------------------------------------------------ control
    # TANPA functionObject. Build v1912 paket Debian crash dgn
    # "error in IOstream sha1" pada functionObject APA PUN, bukan cuma yg
    # berbasis dynamic code. Debit diukur belakangan dari file phi lewat
    # read_patch_flux(). Jangan tambahkan blok functions di sini.
    w("system/controlDict", _hdr("dictionary", "controlDict", "system") + f"""
application simpleFoam;
startFrom latestTime; startTime 0; stopAt endTime; endTime {iters};
deltaT 1; writeControl timeStep; writeInterval {iters};
purgeWrite 2; writeFormat ascii; writePrecision 8; writeCompression off;
timeFormat general; timePrecision 6; runTimeModifiable false;

functions {{}}
""")
    w("system/fvSchemes", _hdr("dictionary", "fvSchemes", "system") + """
ddtSchemes { default steadyState; }
gradSchemes { default cellLimited Gauss linear 1; }
divSchemes
{
    default none;
    div(phi,U) bounded Gauss linearUpwind grad(U);
    div(phi,k) bounded Gauss limitedLinear 1;
    div(phi,omega) bounded Gauss limitedLinear 1;
    div((nuEff*dev2(T(grad(U))))) Gauss linear;
}
laplacianSchemes { default Gauss linear limited corrected 0.33; }
interpolationSchemes { default linear; }
snGradSchemes { default limited corrected 0.33; }
wallDist { method meshWave; }
""")
    w("system/fvSolution", _hdr("dictionary", "fvSolution", "system") + """
solvers
{
    p { solver GAMG; tolerance 1e-7; relTol 0.01; smoother GaussSeidel; }
    "(U|k|omega)" { solver smoothSolver; smoother symGaussSeidel; tolerance 1e-8; relTol 0.05; }
}
SIMPLE
{
    nNonOrthogonalCorrectors 2;
    consistent no;
    residualControl { p 1e-4; U 1e-5; "(k|omega)" 1e-5; }
}
// SIMPLE baku + under-relaxation konservatif. SIMPLEC (consistent yes) dgn
// relaksasi 0.9 diverge di iterasi ~69 dari start dingin -- residual Ux naik
// 0.28 -> 0.81 lalu floating point exception. Jangan dinaikkan tanpa alasan.
relaxationFactors
{
    fields { p 0.3; }
    equations { U 0.7; "(k|omega)" 0.7; }
}
""")
    # scotch di paket Debian cuma stub kosong -> pakai hierarchical (built-in).
    # Pecah greedy sepanjang sumbu terpanjang yang tersisa.
    nx, ny, nz = split_axes(hi - lo, n_proc)
    w("system/decomposeParDict", _hdr("dictionary", "decomposeParDict", "system") + f"""
numberOfSubdomains {n_proc};
method hierarchical;
coeffs {{ n ({nx} {ny} {nz}); order xyz; }}
""")

    return {"case": case_dir, "bbox_lo_m": lo.tolist(), "bbox_hi_m": hi.tolist(),
            "bg_cells": n.tolist(), "dp_kinematic": dp,
            "locationInMesh": loc}


def _patch_block(text, patch):
    """Ambil isi blok satu patch dari boundaryField, hitung kurung kurawal."""
    i = text.find("boundaryField")
    if i < 0:
        raise ValueError("boundaryField tidak ada")
    j = text.find(patch, i)
    while j > 0:
        # pastikan ini nama patch (diikuti '{' setelah whitespace), bukan substring
        k = j + len(patch)
        while k < len(text) and text[k] in " \t\r\n":
            k += 1
        if k < len(text) and text[k] == "{":
            break
        j = text.find(patch, j + 1)
    if j < 0:
        raise ValueError(f"patch {patch} tidak ada")
    depth, start = 0, k
    for m in range(k, len(text)):
        if text[m] == "{":
            depth += 1
        elif text[m] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:m]
    raise ValueError("kurung tidak seimbang")


def _sum_patch_in_file(path, patch):
    blk = _patch_block(open(path).read(), patch)
    # patch tanpa face di processor ini: "value nonuniform 0();"
    if re.search(r"value\s+nonuniform\s+0\s*\(\s*\)\s*;", blk):
        return 0.0, 0
    m = re.search(r"value\s+nonuniform\s+List<scalar>\s*\d*\s*\((.*?)\)\s*;", blk, re.S)
    if m:
        vals = np.fromstring(m.group(1), sep=" ")
        return float(vals.sum()), len(vals)
    m = re.search(r"value\s+uniform\s+([-\d.eE+]+)\s*;", blk)
    if m:
        return float(m.group(1)), 1
    return 0.0, 0


def read_patch_flux(case_dir, patch, time_dir=None):
    """Jumlahkan phi (fluks volumetrik per face, m3/s) di satu patch.

    Dibaca langsung dari file hasil, TIDAK pakai functionObject -- build v1912
    paket Debian crash ("error in IOstream sha1") pada functionObject apa pun.
    Kalau case masih terdekomposisi, dijumlahkan lintas processor* -- itu jalur
    normal di sini karena snappyHexMesh -overwrite paralel menghapus
    *ProcAddressing sehingga reconstructPar tidak bisa jalan.

    Konvensi OpenFOAM: phi positif KELUAR domain -> inlet negatif, outlet positif.
    """
    procs = sorted(d for d in os.listdir(case_dir) if d.startswith("processor"))

    def times_in(root):
        return [d for d in os.listdir(root)
                if d.replace(".", "").isdigit()
                and os.path.exists(os.path.join(root, d, "phi"))]

    if procs:
        if time_dir is None:
            ts = times_in(os.path.join(case_dir, procs[0]))
            if not ts:
                raise FileNotFoundError(f"tidak ada phi di {procs[0]}")
            time_dir = max(ts, key=float)
        total, nf = 0.0, 0
        for p in procs:
            q, n = _sum_patch_in_file(os.path.join(case_dir, p, time_dir, "phi"), patch)
            total += q; nf += n
        return total, time_dir, nf

    if time_dir is None:
        ts = times_in(case_dir)
        if not ts:
            raise FileNotFoundError(f"tidak ada time dir berisi phi di {case_dir}")
        time_dir = max(ts, key=float)
    q, n = _sum_patch_in_file(os.path.join(case_dir, time_dir, "phi"), patch)
    return q, time_dir, n


def cfm_from_flux(q_m3s, dari_inh2o=RUN_INH2O, ke_inh2o=BENCH_INH2O):
    """phi incompressible = debit volumetrik m3/s. Dikonversi ke depresi acuan
    dengan akar rasio tekanan (konversi baku flowbench)."""
    return abs(q_m3s) * 2118.88 * math.sqrt(ke_inh2o / dari_inh2o)


def flow_coefficient(q_m3s, throat_dia_mm, depresi_inh2o=RUN_INH2O):
    """Cf = debit nyata / debit teoretis lewat luas throat. Tak berdimensi, jadi
    dihitung pada depresi yang BENAR-BENAR disimulasikan."""
    dp = depresi_inh2o * PA_PER_INH2O
    v_theo = math.sqrt(2 * dp / RHO)
    a = math.pi / 4 * (throat_dia_mm / 1000.0) ** 2
    return abs(q_m3s) / (a * v_theo)


def _selfcheck():
    # 28"H2O -> ~107 m/s teoretis, 10"H2O -> ~64 m/s
    assert 105 < math.sqrt(2 * BENCH_INH2O * PA_PER_INH2O / RHO) < 110
    v10 = math.sqrt(2 * RUN_INH2O * PA_PER_INH2O / RHO)
    assert 62 < v10 < 66, v10
    # Cf=1 harus keluar kalau debitnya persis debit teoretis di depresi run
    a = math.pi / 4 * (20.2 / 1000.0) ** 2
    assert abs(flow_coefficient(a * v10, 20.2) - 1.0) < 1e-9
    # konversi depresi: CFM naik dgn akar rasio tekanan
    assert abs(cfm_from_flux(1.0, 10.0, 10.0) - 2118.88) < 1e-6
    assert abs(cfm_from_flux(1.0, 10.0, 28.0) / cfm_from_flux(1.0, 10.0, 10.0)
               - math.sqrt(2.8)) < 1e-9
    # parser patch: blok bersarang & nama patch yg jadi substring nama lain
    dummy = '''boundaryField
{
    outletExtra { type calculated; value uniform 9; }
    outlet { type calculated; value nonuniform List<scalar> 3 ( 1.5 2.5 -0.5 ) ; }
}'''
    import tempfile, shutil
    d = tempfile.mkdtemp(); os.makedirs(os.path.join(d, "100"))
    open(os.path.join(d, "100", "phi"), "w").write(dummy)
    q, t, nf = read_patch_flux(d, "outlet")
    assert abs(q - 3.5) < 1e-9 and t == "100" and nf == 3, (q, t, nf)
    shutil.rmtree(d)

    # case terdekomposisi: dijumlahkan lintas processor, patch kosong = 0
    d = tempfile.mkdtemp()
    kosong = 'boundaryField\n{\n    outlet { type calculated; value nonuniform 0(); }\n}'
    for i, isi in enumerate((dummy, kosong)):
        os.makedirs(os.path.join(d, f"processor{i}", "50"))
        open(os.path.join(d, f"processor{i}", "50", "phi"), "w").write(isi)
    q, t, nf = read_patch_flux(d, "outlet")
    assert abs(q - 3.5) < 1e-9 and t == "50" and nf == 3, (q, t, nf)
    shutil.rmtree(d)
    # pembagian domain harus mengalikan balik jadi n_proc
    for np_ in (2, 4, 8, 12, 16, 20):
        nx, ny, nz = split_axes(np.array([0.20, 0.18, 0.21]), np_)
        assert nx * ny * nz == np_, (np_, nx, ny, nz)
    # sumbu terpanjang harus dibelah lebih banyak
    a, b, c = split_axes(np.array([1.0, 0.1, 0.1]), 4)
    assert a == 4 and b == 1 and c == 1, (a, b, c)
    print("selfcheck OK")


if __name__ == "__main__":
    import sys
    _selfcheck()
    stl = sys.argv[1] if len(sys.argv) > 1 else "../cfd/stl/csa615_asp130_str40.stl"
    out = sys.argv[2] if len(sys.argv) > 2 else "../cfd/run/validasi"
    info = build(stl, out)
    for k, v in info.items():
        print(f"  {k}: {v}")
    print(f"  total sel background: {np.prod(info['bg_cells']):,}")


