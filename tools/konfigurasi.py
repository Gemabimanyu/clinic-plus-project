"""Bandingkan konfigurasi bore/stroke pada kapasitas yang sama.

Menjawab: apa untung-ruginya square, overbore, dan overstroke — dalam angka,
bukan perasaan.
"""
import math

VD_TARGET = 150.0        # cc
KLEP_FRAC = 0.38         # diameter klep isap / bore, 4-klep
N_KLEP = 2
THROAT_FRAC = 0.90       # throat / diameter klep
MPS_LIMIT = 22.0         # m/s, batas praktis mesin balap kecil


def stroke_dari_bore(bore, vd_cc=VD_TARGET):
    return vd_cc * 1000.0 / (math.pi / 4 * bore ** 2)


def analisa(bore, vd_cc=VD_TARGET):
    stroke = stroke_dari_bore(bore, vd_cc)
    a_piston = math.pi / 4 * bore ** 2
    d_klep = KLEP_FRAC * bore
    d_throat = THROAT_FRAC * d_klep
    a_throat = N_KLEP * math.pi / 4 * d_throat ** 2
    rpm_maks = MPS_LIMIT * 60 / (2 * stroke / 1000.0)
    # potensi aliran ~ luas throat x rpm
    potensi = a_throat * rpm_maks
    # rasio permukaan/volume ruang bakar (indikator rugi panas & jalur api)
    return {
        "bore": bore, "stroke": stroke, "rasio_bs": bore / stroke,
        "a_piston": a_piston, "d_klep": d_klep, "d_throat": d_throat,
        "a_throat": a_throat, "throat_per_cc": a_throat / vd_cc,
        "rpm_maks": rpm_maks, "potensi": potensi,
    }


def _selfcheck():
    # kapasitas harus konsisten di semua konfigurasi
    for b in (48, 57.6, 65):
        s = stroke_dari_bore(b)
        vd = math.pi / 4 * b ** 2 * s / 1000.0
        assert abs(vd - VD_TARGET) < 1e-6, (b, vd)
    # bore lebih besar -> klep lebih besar, rpm lebih tinggi
    a, b = analisa(52), analisa(63)
    assert b["a_throat"] > a["a_throat"]
    assert b["rpm_maks"] > a["rpm_maks"]
    # square harus di antara keduanya
    sq = analisa(57.6)
    assert a["potensi"] < sq["potensi"] < b["potensi"]
    print("selfcheck OK\n")


if __name__ == "__main__":
    _selfcheck()
    print(f"  Kapasitas tetap {VD_TARGET:.0f} cc, 4-klep, batas MPS {MPS_LIMIT} m/s\n")
    hdr = (f"  {'konfigurasi':16s} {'bore':>6s} {'stroke':>7s} {'B/S':>5s} "
           f"{'klep':>6s} {'throat':>7s} {'mm2/cc':>7s} {'rpm maks':>9s} {'potensi':>9s}")
    print(hdr); print("  " + "-" * (len(hdr) - 2))
    dasar = analisa(57.6)["potensi"]
    for nm, b in (("overstroke", 52.0), ("square", 57.6),
                  ("overbore ringan", 60.0), ("overbore", 63.0)):
        r = analisa(b)
        print(f"  {nm:16s} {r['bore']:6.1f} {r['stroke']:7.1f} {r['rasio_bs']:5.2f} "
              f"{r['d_klep']:6.1f} {r['d_throat']:7.1f} {r['throat_per_cc']:7.2f} "
              f"{r['rpm_maks']:9.0f} {r['potensi']/dasar*100:8.0f}%")
    print("\n  potensi = luas throat x rpm maksimum, relatif terhadap square")

    print(f"\n  === KAPASITAS NAIK, HEAD TETAP ===")
    print(f"  (bore dinaikkan, head 150cc tidak diubah)")
    r0 = analisa(57.6)
    print(f"  {'kapasitas':>10s} {'bore':>6s} {'throat/cc':>10s} {'MGV @9000':>11s}")
    for vd in (150, 165, 180, 200):
        b = math.sqrt(vd * 1000.0 / (math.pi / 4 * stroke_dari_bore(57.6) / 1.0))
        # stroke tetap, bore naik
        s = stroke_dari_bore(57.6)
        b = math.sqrt(vd * 1000.0 / (math.pi / 4 * s))
        ap = math.pi / 4 * b ** 2
        mps = 2 * s / 1000.0 * 9000 / 60
        # head TETAP: pakai CSA port yg sama dgn versi 150cc
        csa = r0["a_throat"] * 1.03
        print(f"  {vd:9.0f}c {b:6.1f} {r0['a_throat']/vd:10.2f} {ap/csa*mps:11.0f}")
    print("  MGV naik terus karena luas piston naik tapi port tetap")
