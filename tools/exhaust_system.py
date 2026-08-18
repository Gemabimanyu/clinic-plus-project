"""Sistem buang: CSA port, diameter header, dan panjang header.

Dikalibrasi dari mesin acuan Gema:
    port ex 29 mm, header dalam 30 mm, inlet muffler 50 mm
    (panjang header belum diukur -- itu satu-satunya yang belum terkunci)
"""
import math

# ----------------------------------------------------------------- ACUAN
R_EX_THROAT_D = 0.88 * 27.0      # 23.76 mm
R_PORT_D = 29.0
R_HEADER_D = 30.0
R_BORE, R_STROKE = 63.0, 64.0
R_RPM = 10000
R_EVO = 63.0                     # BBDC

# ------------------------------------------------------------------ BARU
EX_THROAT_D = 16.7
N_EX = 2
BORE, STROKE = 57.3, 58.0
RPM = 12000
EVO = 53.0                       # BBDC

C_GAS = 650.0                    # kecepatan suara gas buang m/s @ ~1100 K.
                                 # ASUMSI. Rentang wajar 550-700 tergantung
                                 # suhu dan kekayaan campuran.


def luas(n, d):
    return n * math.pi / 4 * d ** 2


def csa_port_buang():
    """Dua jangkar, sama seperti waktu menentukan port isap."""
    a_thr_ref = luas(1, R_EX_THROAT_D)
    a_port_ref = luas(1, R_PORT_D)
    rasio = a_port_ref / a_thr_ref

    a_thr_baru = luas(N_EX, EX_THROAT_D)
    # jangkar 1: samakan rasio port/throat
    csa_rasio = rasio * a_thr_baru
    # jangkar 2: samakan kecepatan gas di port
    mps_ref = 2 * (R_STROKE / 1000) * R_RPM / 60
    v_ref = (math.pi / 4 * R_BORE ** 2) / a_port_ref * mps_ref
    mps = 2 * (STROKE / 1000) * RPM / 60
    csa_vel = (math.pi / 4 * BORE ** 2) * mps / v_ref
    return {"rasio_acuan": rasio, "v_ref": v_ref,
            "csa_rasio": csa_rasio, "csa_vel": csa_vel,
            "a_thr_baru": a_thr_baru}


def header_dia(csa_port):
    """Header acuan 1.07x luas port. Pertahankan rasio itu."""
    r = luas(1, R_HEADER_D) / luas(1, R_PORT_D)
    a = r * csa_port
    return math.sqrt(4 * a / math.pi), r


def header_panjang(rpm, evo_bbdc, c=C_GAS, harmonik=(1, 2, 3, 4)):
    """Panjang header agar gelombang ekspansi pantulan tiba saat overlap.

    Gelombang lahir di EVO, lari ke ujung terbuka (sambungan ke muffler),
    memantul jadi gelombang negatif, lalu kembali ke klep. Jarak tempuh 2L.

    JUJUR: harmonik mana yang dipakai mesinmu TIDAK bisa ditentukan dari
    teori saja. Ukur panjang header mesin acuanmu -- itu langsung menunjukkan
    harmonik yang terbukti jalan, dan sisanya tinggal skala.
    """
    t = (180.0 + evo_bbdc) / (6.0 * rpm)     # detik, dari EVO ke TDC
    return {n: c * t / (2.0 * n) * 1000.0 for n in harmonik}


def _selfcheck():
    d = csa_port_buang()
    # port ex acuan memang jauh lebih besar dari throat-nya
    assert 1.3 < d["rasio_acuan"] < 1.7, d["rasio_acuan"]
    # dua jangkar harus se-orde
    assert 0.75 < d["csa_vel"] / d["csa_rasio"] < 1.25, d
    # header lebih besar dari port
    dh, r = header_dia(d["csa_rasio"])
    assert r > 1.0 and dh > math.sqrt(4 * d["csa_rasio"] / math.pi)
    # rpm naik -> header lebih pendek; harmonik tinggi -> lebih pendek
    a = header_panjang(12000, 53.0)
    b = header_panjang(10000, 53.0)
    assert a[1] < b[1] and a[2] < a[1]
    print("selfcheck OK\n")


if __name__ == "__main__":
    _selfcheck()
    d = csa_port_buang()
    print("  === CSA PORT BUANG ===")
    print(f"  acuan: port {R_PORT_D} mm ({luas(1,R_PORT_D):.0f} mm2) / "
          f"throat {R_EX_THROAT_D:.1f} mm ({luas(1,R_EX_THROAT_D):.0f} mm2)")
    print(f"  -> rasio port/throat {d['rasio_acuan']:.3f}  "
          f"(port ex hampir sebesar port isap 29.5mm)")
    print(f"  -> kecepatan gas di port ex acuan {d['v_ref']:.0f} m/s")
    print(f"\n  baru: throat ex {d['a_thr_baru']:.0f} mm2")
    for nm, v in (("jangkar rasio port/throat", d["csa_rasio"]),
                  ("jangkar kecepatan gas", d["csa_vel"])):
        print(f"  {nm:28s} {v:6.0f} mm2  (dia setara "
              f"{math.sqrt(4*v/math.pi):.1f} mm)")

    csa = (d["csa_rasio"] + d["csa_vel"]) / 2
    dh, r = header_dia(csa)
    print(f"\n  === HEADER ===")
    print(f"  acuan: header {R_HEADER_D} mm / port {R_PORT_D} mm "
          f"-> luas {r:.3f}x")
    print(f"  baru : port {csa:.0f} mm2 -> header dalam {dh:.1f} mm")
    print(f"  (acuanmu 30 mm -- praktis sama, tidak perlu diubah banyak)")

    print(f"\n  === PANJANG HEADER (dari klep ke step 50mm) ===")
    print(f"  kecepatan suara gas diasumsikan {C_GAS:.0f} m/s")
    pa = header_panjang(R_RPM, R_EVO)
    pb = header_panjang(RPM, EVO)
    print(f"  {'harmonik':>9s} {'ACUAN @10rb':>13s} {'BARU @12rb':>12s}")
    for n in (1, 2, 3, 4):
        print(f"  {n:9d} {pa[n]:11.0f} mm {pb[n]:10.0f} mm")
    print(f"\n  UKUR panjang header mesin acuanmu (klep -> step ke 50mm).")
    print(f"  Angka itu menunjuk harmonik yang TERBUKTI jalan, lalu tinggal")
    print(f"  pakai baris yang sama untuk mesin baru.")
