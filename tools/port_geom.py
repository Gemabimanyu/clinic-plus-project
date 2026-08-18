"""Generator volume fluida port 4-klep untuk CFD.

Bikin VOLUME FLUIDA langsung sebagai solid (bukan bikin head lalu boolean
subtract) -- jauh lebih sederhana dan watertight by construction.

Model: SATU cabang port (dari flange manifold sampai keluar throat), bukan
kedua-duanya. Port 4-klep siamese simetris terhadap sekat pemisah, jadi satu
cabang membawa separuh aliran dan separuh CSA. Yang hilang dari model ini cuma
rugi di ujung sekat -- dan itu sama untuk semua varian, jadi tidak mengubah
peringkat. ponytail: sekat tidak dimodelkan, tambahkan kalau butuh CFM absolut.

Output: STL ascii multi-solid dengan region inlet/wall/outlet supaya
snappyHexMesh bisa kasih nama patch langsung.
"""
import math
import numpy as np
import manifold3d

SEC = 80          # jumlah penampang sepanjang centerline
RING = 56         # titik per penampang
SE_EXP = 2.5      # eksponen superelips (2=elips, besar=makin kotak)
VALVE_TILT = 13.0 # sudut sumbu klep dari vertikal (pent-roof 4-klep)


def superellipse(n_pts, aspect, area, exp=SE_EXP):
    """Titik-titik penampang dengan luas persis `area` dan rasio tinggi/lebar
    `aspect`. Luas dihitung numerik lalu diskalakan -- tidak perlu fungsi gamma."""
    t = np.linspace(0, 2 * np.pi, n_pts, endpoint=False)
    c, s = np.cos(t), np.sin(t)
    u = np.sign(c) * np.abs(c) ** (2.0 / exp)
    v = np.sign(s) * np.abs(s) ** (2.0 / exp) * aspect
    a_unit = 0.5 * np.abs(np.sum(u * np.roll(v, -1) - np.roll(u, -1) * v))
    k = math.sqrt(area / a_unit)
    return u * k, v * k


def centerline(port_len, downdraft_deg, str_radius, port_h):
    """Lurus -> busur -> lurus. Radius busur diatur supaya LANTAI port (sisi
    dalam tikungan) punya radius = str_radius. Itu yang menentukan aliran lepas
    atau tidak, bukan radius centerline."""
    th = math.radians(downdraft_deg)
    tilt = math.radians(VALVE_TILT)
    d_in = np.array([-math.cos(th), 0.0, -math.sin(th)])       # arah masuk port
    d_out = np.array([-math.sin(tilt), 0.0, -math.cos(tilt)])  # arah lewat throat
    turn = math.acos(np.clip(np.dot(d_in, d_out), -1, 1))
    r_c = str_radius + port_h / 2.0                            # radius centerline
    arc_len = r_c * turn

    straight = max(port_len - arc_len, port_len * 0.15)
    l_in = straight * 0.55
    l_out = straight * 0.45

    # bangun dgn integrasi arah: lurus, lalu belok bertahap, lalu lurus
    n_in = max(int(SEC * l_in / port_len), 4)
    n_arc = max(int(SEC * arc_len / port_len), 8)
    n_out = SEC - n_in - n_arc
    if n_out < 4:
        n_arc += n_out - 4
        n_out = 4

    # sumbu rotasi busur (bidang x-z)
    axis = np.array([0.0, 1.0, 0.0])
    dirs, steps = [], []
    dirs += [d_in] * n_in
    steps += [l_in / n_in] * n_in
    for i in range(n_arc):
        ang = turn * (i + 0.5) / n_arc
        ca, sa = math.cos(ang), math.sin(ang)
        # rotasi d_in mengelilingi y menuju d_out
        d = np.array([d_in[0] * ca + d_in[2] * sa, 0.0, -d_in[0] * sa + d_in[2] * ca])
        # pastikan arah putar benar (mendekati d_out)
        d2 = np.array([d_in[0] * ca - d_in[2] * sa, 0.0, d_in[0] * sa + d_in[2] * ca])
        dirs.append(d if np.dot(d, d_out) > np.dot(d2, d_out) else d2)
        steps.append(arc_len / n_arc)
    dirs += [d_out] * n_out
    steps += [l_out / n_out] * n_out

    pts = [np.zeros(3)]
    for d, h in zip(dirs, steps):
        pts.append(pts[-1] + d * h)
    pts = np.array(pts)
    pts -= pts[-1]                      # ujung throat di origin
    return pts, np.array(dirs + [dirs[-1]])


N_BELL = 14        # penampang di sepanjang bellmouth
BELL_RATIO = 0.25  # radius bellmouth / tinggi port


def build_port(csa_total, aspect, str_ratio, throat_dia,
               downdraft=40.0, port_len=70.0, bell_ratio=BELL_RATIO):
    """csa_total = CSA port gabungan (mm2). Model pakai separuhnya (1 cabang).

    Mulut port diberi BELLMOUTH seperempat lingkaran. Tanpa itu mulutnya jadi
    pipa bertepi tajam yang menonjol ke plenum, dan rugi masuknya (K~1.7)
    menenggelamkan rugi tikungan (K~0.4) yang justru jadi objek studi.
    Terukur: port lurus tanpa bellmouth cuma Cf 0.602 -- hampir semuanya rugi
    mulut, bukan gesekan (gesekan saluran 70mm cuma K~0.07).
    """
    csa = csa_total / 2.0
    a_throat = math.pi / 4 * throat_dia ** 2
    port_h = math.sqrt(csa / (0.92 * aspect)) * aspect
    str_radius = str_ratio * port_h
    bell_r = bell_ratio * port_h

    cl, tang = centerline(port_len, downdraft, str_radius, port_h)
    side = np.array([0.0, 1.0, 0.0])              # lebar port selalu arah y

    def frame(d):
        d = d / np.linalg.norm(d)
        up = np.cross(d, side)
        return d, up / np.linalg.norm(up)

    # penampang: (titik pusat, arah, u, v)
    sections = []

    # --- bellmouth: melebar keluar mengikuti busur seperempat lingkaran ---
    u0, v0 = superellipse(RING, aspect, csa)
    w0, h0 = np.abs(u0).max(), np.abs(v0).max()
    d0, _ = frame(tang[0])
    for k in range(N_BELL):
        th = math.radians(90.0 * (1.0 - k / N_BELL))
        off = bell_r * (1.0 - math.cos(th))       # melebar keluar
        back = bell_r * math.sin(th)              # mundur dari bidang mulut
        sections.append((cl[0] - d0 * back, d0,
                         u0 * (w0 + off) / w0, v0 * (h0 + off) / h0))

    # --- badan port: mulut -> throat ---
    n_main = len(cl)
    for i in range(n_main):
        f = i / (n_main - 1.0)
        # luas berubah halus (cosine, bukan linear -- perubahan mendadak di
        # dekat throat bikin aliran lepas)
        w = 0.5 - 0.5 * math.cos(math.pi * f)
        area = csa + (a_throat - csa) * w
        asp = aspect + (1.0 - aspect) * w        # berubah jadi bundar di throat
        u, v = superellipse(RING, asp, area)
        sections.append((cl[i], tang[i], u, v))

    n = len(sections)
    verts = []
    for cen, d, u, v in sections:
        d, up = frame(d)
        for j in range(RING):
            verts.append(cen + side * u[j] + up * v[j])
    mouth_pt, mouth_dir = sections[0][0], d0

    # Pusat tutup HARUS sebidang dgn cincin yang ditutupnya. Dulu ini cl[0],
    # dan setelah bellmouth ditambahkan cincin pertama pindah ke hulu sejauh
    # bell_r -- tutupnya jadi KERUCUT menjorok ke dalam port, bukan cakram.
    # Akibatnya aliran masuk sebagai cincin di dinding dgn aliran balik
    # -15 m/s di tengah, dan Cf anjlok ke 0.2. Jangan pakai cl[0] di sini.
    c0 = len(verts); verts.append(sections[0][0].copy())
    c1 = len(verts); verts.append(sections[-1][0].copy())
    verts = np.array(verts, dtype=np.float32)

    tris = []
    for i in range(n - 1):
        for j in range(RING):
            a = i * RING + j
            b = i * RING + (j + 1) % RING
            c = (i + 1) * RING + j
            d = (i + 1) * RING + (j + 1) % RING
            tris += [[a, c, b], [b, c, d]]
    # arah putar tutup HARUS berlawanan dgn rim tabung, kalau tidak halfedge
    # kembar searah -> NotManifold. Cek edge tak-berarah tidak menangkap ini.
    for j in range(RING):                       # tutup mulut port
        tris.append([c0, j, (j + 1) % RING])
    base = (n - 1) * RING
    for j in range(RING):                       # tutup keluaran throat
        tris.append([c1, base + (j + 1) % RING, base + j])

    # balik semua supaya normal menghadap KELUAR (volume positif)
    tris = np.array(tris, dtype=np.uint32)[:, [0, 2, 1]]
    return verts, tris, mouth_pt, mouth_dir, port_h


def add_plenum(verts, tris, mouth_pt, radius=80.0, mouth_dir=None, overlap=2.0):
    """Union port dengan plenum SETENGAH BOLA berpusat di mulut port, dipotong
    tepat di bidang mulut -- jadi mulut port terbuka di tengah bidang datar
    (muka flange) dan batas masuk berjarak `radius` ke segala arah.

    JANGAN kembali ke bola utuh yang digeser ke depan mulut. Terukur: dgn bola
    radius 80 berpusat 75mm di depan mulut, permukaannya cuma 5mm dari mulut,
    dan 62% aliran masuk lewat 0.42% luas patch pada 72 m/s. Itu bukan plenum,
    itu jet -- dan menyumbang K~1.5 rugi palsu yang menenggelamkan rugi bentuk
    port (K~0.5) yang justru jadi objek studi.
    """
    port = manifold3d.Manifold(manifold3d.Mesh(
        vert_properties=verts.astype(np.float32),
        tri_verts=tris.astype(np.uint32)))
    d = mouth_dir / np.linalg.norm(mouth_dir)      # arah masuk port (ke hilir)
    ball = manifold3d.Manifold.sphere(radius, 96).translate(tuple(mouth_pt))

    # Sisakan hanya sisi HULU, plus sedikit overlap supaya union bersih.
    # Konvensi arah trim_by_plane tidak dipercaya: pilih separuh yang TIDAK
    # menelan port. Membedakan lewat volume tidak bisa -- kedua separuh
    # volumenya nyaris sama (1.03e6 vs 1.11e6) dan yang salah justru lebih kecil.
    off = float(np.dot(mouth_pt, d) + overlap)
    kandidat = [ball.trim_by_plane(tuple(d), off),
                ball.trim_by_plane(tuple(-d), -off)]
    plen = None
    for p in kandidat:
        if (port + p).volume() > p.volume() + 0.5 * port.volume():
            plen = p                                # port menonjol keluar -> hulu
            break
    if plen is None:
        raise ValueError("tidak ada separuh plenum yang menyisakan port di luarnya")
    return port + plen, mouth_pt


def _write_stl(man, path, solid_name):
    """Tulis satu manifold sebagai STL ascii solid tunggal."""
    mesh = man.to_mesh()
    v = np.asarray(mesh.vert_properties)[:, :3]
    t = np.asarray(mesh.tri_verts)
    with open(path, "w") as f:
        f.write(f"solid {solid_name}\n")
        for tri in t:
            p = v[tri]
            n = np.cross(p[1] - p[0], p[2] - p[0])
            ln = np.linalg.norm(n)
            n = n / ln if ln > 0 else np.array([0.0, 0.0, 1.0])
            f.write(f"  facet normal {n[0]:.6e} {n[1]:.6e} {n[2]:.6e}\n    outer loop\n")
            for q in p:
                f.write(f"      vertex {q[0]:.6e} {q[1]:.6e} {q[2]:.6e}\n")
            f.write("    endloop\n  endfacet\n")
        f.write(f"endsolid {solid_name}\n")
    return len(t)


def classify_write(man, path, ball_center, ball_r, throat_dia,
                   mouth_pt=None, mouth_dir=None):
    """Tulis STL multi-solid. Region dari geometri: segitiga di permukaan bola
    = inlet, di cakram keluar throat = outlet, sisanya wall.

    Cakram keluar TEGAK LURUS SUMBU KLEP yang miring 13 deg, jadi harus diuji
    terhadap bidang bersumbu itu -- bukan terhadap z. Memakai |z|<tol cuma
    menangkap pita tipis di tengah cakram, sisa cakram jadi dinding yang
    menyumbat throat: Cf anjlok ke 0.25 padahal mesh & massa terlihat sehat.
    """
    mesh = man.to_mesh()
    v = np.asarray(mesh.vert_properties)[:, :3]
    t = np.asarray(mesh.tri_verts)
    cen = v[t].mean(axis=1)

    # inlet = permukaan LENGKUNG setengah bola saja. Bidang datar di mulut
    # (muka flange) harus jadi wall, bukan inlet.
    d_ball = np.linalg.norm(cen - ball_center, axis=1)
    is_inlet = np.abs(d_ball - ball_r) < ball_r * 0.02

    tilt = math.radians(VALVE_TILT)
    axis = np.array([math.sin(tilt), 0.0, math.cos(tilt)])   # sumbu klep
    s = cen @ axis                                            # jarak sepanjang sumbu
    radial = np.linalg.norm(cen - np.outer(s, axis), axis=1)  # jarak dari sumbu

    # normal tiap segitiga: cakram keluar sejajar sumbu, dinding tegak lurus.
    # Uji jarak saja tidak cukup -- dinding di bibir throat ikut tertangkap.
    p3 = v[t]
    nrm = np.cross(p3[:, 1] - p3[:, 0], p3[:, 2] - p3[:, 0])
    nrm /= np.maximum(np.linalg.norm(nrm, axis=1, keepdims=True), 1e-30)
    sejajar_sumbu = np.abs(nrm @ axis) > 0.9

    is_outlet = ((np.abs(s) < 1.0) & (radial < throat_dia / 2 * 1.05)
                 & sejajar_sumbu & ~is_inlet)

    # Bidang datar flange di sekitar mulut: pelat besar, jauh dari aliran yang
    # menarik. Dipisah supaya bisa di-mesh kasar. Kalau ikut jadi "wall" dia
    # kena refinement level 3-4 + lapis prisma: mesh meledak 123k -> 615k sel
    # dan satu case makan 82 menit, bukan 6.
    md = mouth_dir / np.linalg.norm(mouth_dir)
    jarak_bidang = (cen - mouth_pt) @ md
    is_flange = (np.abs(jarak_bidang) < 2.5) & (np.abs(nrm @ md) > 0.9) & ~is_inlet

    region = np.where(is_inlet, 0, np.where(is_outlet, 1,
                      np.where(is_flange, 3, 2)))

    names = ["inlet", "outlet", "wall", "flange"]
    # luas tiap region, dipakai untuk memverifikasi klasifikasi
    p3 = v[t]
    tri_area = np.linalg.norm(np.cross(p3[:, 1] - p3[:, 0], p3[:, 2] - p3[:, 0]), axis=1) / 2
    areas = {nm: float(tri_area[region == i].sum()) for i, nm in enumerate(names)}

    with open(path, "w") as f:
        for rid, nm in enumerate(names):
            f.write(f"solid {nm}\n")
            for tri in t[region == rid]:
                p = v[tri]
                nrm = np.cross(p[1] - p[0], p[2] - p[0])
                ln = np.linalg.norm(nrm)
                nrm = nrm / ln if ln > 0 else np.array([0.0, 0.0, 1.0])
                f.write(f"  facet normal {nrm[0]:.6e} {nrm[1]:.6e} {nrm[2]:.6e}\n    outer loop\n")
                for q in p:
                    f.write(f"      vertex {q[0]:.6e} {q[1]:.6e} {q[2]:.6e}\n")
                f.write("    endloop\n  endfacet\n")
            f.write(f"endsolid {nm}\n")
    return ({nm: int((region == i).sum()) for i, nm in enumerate(names)}, areas)


def generate(path, csa_total, aspect, str_ratio, throat_dia,
             downdraft=40.0, port_len=70.0, ball_r=80.0):
    verts, tris, mouth, mouth_dir, port_h = build_port(
        csa_total, aspect, str_ratio, throat_dia, downdraft, port_len)
    port_only = manifold3d.Manifold(manifold3d.Mesh(
        vert_properties=verts.astype(np.float32), tri_verts=tris.astype(np.uint32)))
    man, center = add_plenum(verts, tris, mouth, ball_r, mouth_dir)
    counts, areas = classify_write(man, path, center, ball_r, throat_dia,
                                   mouth, mouth_dir)

    # STL kedua: HANYA volume port, tanpa plenum. Dipakai snappyHexMesh sebagai
    # refinementRegion supaya INTI port ikut halus. Tanpa ini refinement cuma
    # kena permukaan: dinding dapat sel 0.3mm + lapis prisma, tapi inti port
    # cuma ~4 sel melintang dan aliran utamanya dihitung di mesh kasar.
    core_path = path.replace(".stl", "_core.stl")
    _write_stl(port_only, core_path, "portcore")

    # PENJAGA: luas patch outlet harus mendekati luas throat. Kalau meleset,
    # sebagian cakram keluar salah ditandai jadi dinding -> throat tersumbat dan
    # Cf keluar rendah palsu, padahal mesh & keseimbangan massa tampak sehat.
    a_throat = math.pi / 4 * throat_dia ** 2
    rasio = areas["outlet"] / a_throat
    if not 0.90 < rasio < 1.15:
        raise ValueError(
            f"luas patch outlet {areas['outlet']:.1f} mm2 vs luas throat "
            f"{a_throat:.1f} mm2 (rasio {rasio:.3f}) -- klasifikasi patch salah")

    # PENJAGA: inlet harus mendekati luas setengah bola. Kalau jauh lebih kecil,
    # plenumnya salah bentuk/posisi dan aliran masuk lewat celah sempit.
    a_hemi = 2 * math.pi * ball_r ** 2
    r_in = areas["inlet"] / a_hemi
    if not 0.80 < r_in < 1.20:
        raise ValueError(
            f"luas patch inlet {areas['inlet']:.0f} mm2 vs setengah bola "
            f"{a_hemi:.0f} mm2 (rasio {r_in:.3f}) -- plenum salah")

    return {"volume_mm3": man.volume(), "port_volume_mm3": port_only.volume(),
            "port_h_mm": port_h, "port_w_mm": port_h / aspect,
            "str_radius_mm": str_ratio * port_h, "facets": counts,
            "area_outlet_mm2": areas["outlet"], "area_throat_mm2": a_throat,
            "rasio_outlet_throat": rasio,
            "area_inlet_mm2": areas["inlet"], "rasio_inlet_hemi": r_in}


def _halfedge_ok(tris):
    """Tiap halfedge berarah harus muncul PERSIS sekali. Cek edge tak-berarah
    saja tidak cukup -- tutup dgn arah putar terbalik tetap lolos cek itu."""
    seen = set()
    for a, b, c in tris:
        for e in ((a, b), (b, c), (c, a)):
            if e in seen:
                return False
            seen.add(e)
    return all((b, a) in seen for a, b in seen)


def _selfcheck():
    import tempfile, os
    # penampang harus mereproduksi luas & aspect
    u, v = superellipse(200, 1.3, 500.0)
    a = 0.5 * abs(np.sum(u * np.roll(v, -1) - np.roll(u, -1) * v))
    assert abs(a - 500.0) < 0.5, a
    assert abs((v.max() - v.min()) / (u.max() - u.min()) - 1.3) < 0.01

    # bulat = aspect 1.0 harus benar-benar lingkaran
    u, v = superellipse(400, 1.0, 320.0, exp=2.0)
    r = np.hypot(u, v)
    assert r.std() / r.mean() < 1e-6, r.std()

    _v, _t, _m, _md, _h = build_port(615.0, 1.30, 0.40, 20.2)
    assert _halfedge_ok(_t), "halfedge tidak konsisten -> Manifold akan gagal"

    # tutup harus DATAR: pusat tutup sebidang dgn cincin yg ditutupnya.
    # Kalau tidak, tutupnya kerucut yang menyumbat mulut/throat.
    for nama, ring0, pusat in (("mulut", _v[:RING], _v[-2]),
                               ("throat", _v[-2 - RING:-2], _v[-1])):
        nrm = np.cross(ring0[1] - ring0[0], ring0[RING // 3] - ring0[0])
        nrm /= np.linalg.norm(nrm)
        simpang = abs((pusat - ring0[0]) @ nrm)
        assert simpang < 1e-3, f"tutup {nama} tidak datar: simpang {simpang:.3f} mm"
    # bellmouth harus benar-benar melebar: mulut lebih lebar dari badan port
    r_mulut = np.linalg.norm(_v[:RING] - _v[:RING].mean(axis=0), axis=1).mean()
    r_badan = np.linalg.norm(_v[N_BELL * RING:(N_BELL + 1) * RING]
                             - _v[N_BELL * RING:(N_BELL + 1) * RING].mean(axis=0),
                             axis=1).mean()
    assert r_mulut > r_badan * 1.15, (r_mulut, r_badan)

    p = os.path.join(tempfile.gettempdir(), "pc.stl")
    r1 = generate(p, 615.0, 1.30, 0.40, 20.2)
    assert r1["volume_mm3"] > 0 and r1["port_volume_mm3"] > 0, r1
    for k in ("inlet", "outlet", "wall"):
        assert r1["facets"][k] > 0, (k, r1["facets"])
    # short turn lebih besar -> volume port berubah, tapi tetap solid valid
    r2 = generate(p, 615.0, 1.30, 0.55, 20.2)
    assert r2["volume_mm3"] > 0 and r2["str_radius_mm"] > r1["str_radius_mm"]
    # CSA lebih besar -> volume PORT lebih besar (volume total didominasi bola)
    r3 = generate(p, 665.0, 1.30, 0.40, 20.2)
    assert r3["port_volume_mm3"] > r1["port_volume_mm3"], (
        r1["port_volume_mm3"], r3["port_volume_mm3"])
    # volume port harus se-orde dgn CSA x panjang (cek unit/skala)
    kasar = (615.0 / 2) * 70.0
    assert 0.5 * kasar < r1["port_volume_mm3"] < 1.5 * kasar, (r1["port_volume_mm3"], kasar)
    os.remove(p)
    print("selfcheck OK")


CSA_SET = [560.0, 615.0, 665.0]      # CSA port gabungan (mm2)
ASPECT_SET = [1.00, 1.15, 1.30, 1.45]  # 1.00 = bulat, kontrol thd port acuan
STR_SET = [0.30, 0.40, 0.55]         # short-turn radius / tinggi cabang
THROAT = 20.2                        # dikunci: seat dibesarkan dari 19.5


def sweep(outdir):
    import os, csv
    os.makedirs(outdir, exist_ok=True)
    rows = []
    for csa in CSA_SET:
        for asp in ASPECT_SET:
            for st in STR_SET:
                name = f"csa{int(csa)}_asp{int(asp*100)}_str{int(st*100)}"
                r = generate(os.path.join(outdir, name + ".stl"),
                             csa, asp, st, THROAT)
                rows.append({"case": name, "csa_total": csa, "aspect": asp,
                             "str_ratio": st, "throat": THROAT,
                             "cabang_w_mm": round(r["port_w_mm"], 2),
                             "cabang_h_mm": round(r["port_h_mm"], 2),
                             "str_radius_mm": round(r["str_radius_mm"], 2),
                             "port_vol_mm3": round(r["port_volume_mm3"], 1)})
    with open(os.path.join(outdir, "cases.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    return rows


if __name__ == "__main__":
    _selfcheck()
    rows = sweep("../cfd/stl")
    print(f"{len(rows)} STL dibuat di ../cfd/stl")
    for r in rows[:3]:
        print(" ", r)
