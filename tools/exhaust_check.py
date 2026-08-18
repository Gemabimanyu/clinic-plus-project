"""Periksa sisi buang: proporsi ex/in, throat, lift, dan apakah cam simetris
masih tepat.

Cara memutuskan durasi ex: JANGAN pakai aturan umum. Bandingkan proporsi ex/in
mesin baru dengan mesin acuan yang sudah terbukti jalan pakai cam simetris
281/281. Kalau proporsinya sama, cam simetris tetap benar.
"""
import math

# ------------------------------------------------------------------ BARU
IN_D, EX_D = 22.0, 19.0
N_IN, N_EX = 2, 2
IN_THROAT = 20.2                 # sudah ditetapkan
EX_THROAT_RATIO = 0.88           # throat/klep sisi buang (seat lebih lebar utk panas)

# ----------------------------------------------------------------- ACUAN
R_IN_D, R_EX_D = 31.0, 27.0
R_N_IN, R_N_EX = 1, 1
R_IN_THROAT = 29.0               # DIUKUR
R_EX_THROAT_RATIO = 0.88


def luas(n, d):
    return n * math.pi / 4 * d ** 2


def analisa(in_d, ex_d, n_in, n_ex, in_throat, ex_ratio):
    ex_throat = ex_ratio * ex_d
    a_in_klep, a_ex_klep = luas(n_in, in_d), luas(n_ex, ex_d)
    a_in_thr, a_ex_thr = luas(n_in, in_throat), luas(n_ex, ex_throat)
    return {
        "ex_throat_d": ex_throat,
        "rasio_dia": ex_d / in_d,
        "rasio_luas_klep": a_ex_klep / a_in_klep,
        "rasio_luas_throat": a_ex_thr / a_in_thr,
        "a_in_thr": a_in_thr, "a_ex_thr": a_ex_thr,
        # lift saat tirai = throat: di atas ini throat jadi pembatas
        "lift_kritis_in": a_in_thr / (n_in * math.pi * in_d),
        "lift_kritis_ex": a_ex_thr / (n_ex * math.pi * ex_d),
    }


def _selfcheck():
    b = analisa(IN_D, EX_D, N_IN, N_EX, IN_THROAT, EX_THROAT_RATIO)
    a = analisa(R_IN_D, R_EX_D, R_N_IN, R_N_EX, R_IN_THROAT, R_EX_THROAT_RATIO)
    # rasio luas harus kuadrat dari rasio diameter
    assert abs(b["rasio_luas_klep"] - b["rasio_dia"] ** 2) < 1e-9
    # sisi buang selalu lebih kecil dari sisi isap
    assert b["rasio_luas_throat"] < 1.0 and a["rasio_luas_throat"] < 1.0
    # klep lebih besar -> lift kritis lebih tinggi
    assert a["lift_kritis_in"] > b["lift_kritis_in"]
    print("selfcheck OK\n")


if __name__ == "__main__":
    _selfcheck()
    b = analisa(IN_D, EX_D, N_IN, N_EX, IN_THROAT, EX_THROAT_RATIO)
    a = analisa(R_IN_D, R_EX_D, R_N_IN, R_N_EX, R_IN_THROAT, R_EX_THROAT_RATIO)

    print(f"  {'':26s} {'ACUAN (terbukti)':>18s} {'BARU':>12s}")
    print(f"  {'klep in / ex':26s} {f'{R_IN_D:.0f} / {R_EX_D:.0f} mm x1':>18s} "
          f"{f'{IN_D:.0f} / {EX_D:.0f} x2':>12s}")
    print(f"  {'rasio diameter ex/in':26s} {a['rasio_dia']:18.3f} {b['rasio_dia']:12.3f}")
    print(f"  {'rasio luas klep ex/in':26s} {a['rasio_luas_klep']:18.3f} "
          f"{b['rasio_luas_klep']:12.3f}")
    print(f"  {'throat ex':26s} {a['ex_throat_d']:15.1f} mm {b['ex_throat_d']:9.1f} mm")
    print(f"  {'luas throat in':26s} {a['a_in_thr']:15.0f} mm2 {b['a_in_thr']:8.0f} mm2")
    print(f"  {'luas throat ex':26s} {a['a_ex_thr']:15.0f} mm2 {b['a_ex_thr']:8.0f} mm2")
    print(f"  {'RASIO THROAT ex/in':26s} {a['rasio_luas_throat']:18.3f} "
          f"{b['rasio_luas_throat']:12.3f}   <-- penentu")

    selisih = abs(b["rasio_luas_throat"] - a["rasio_luas_throat"])
    print(f"\n  selisih rasio throat: {selisih:.3f} "
          f"({selisih/a['rasio_luas_throat']*100:.1f}%)")
    if selisih / a["rasio_luas_throat"] < 0.06:
        print("  -> proporsi ex/in praktis SAMA dgn mesin terbuktimu.")
        print("     Cam simetris 261/261 tetap benar, sama seperti 281/281 di acuan.")
    else:
        print("  -> proporsi berbeda, durasi ex perlu disesuaikan.")

    print(f"\n  === LIFT KRITIS (di atas ini throat jadi pembatas) ===")
    print(f"  {'':10s} {'ACUAN':>10s} {'BARU':>10s}")
    print(f"  {'in':10s} {a['lift_kritis_in']:10.2f} {b['lift_kritis_in']:10.2f} mm")
    print(f"  {'ex':10s} {a['lift_kritis_ex']:10.2f} {b['lift_kritis_ex']:10.2f} mm")
    print(f"\n  lift dipakai: acuan 10.8 mm, baru 9.0 mm")
    print(f"  kelipatan thd lift kritis:")
    print(f"    acuan  in {10.8/a['lift_kritis_in']:.2f}x   ex {10.8/a['lift_kritis_ex']:.2f}x")
    print(f"    baru   in {9.0/b['lift_kritis_in']:.2f}x   ex {9.0/b['lift_kritis_ex']:.2f}x")

    print(f"\n  === CSA PORT BUANG ===")
    for r in (0.95, 1.05, 1.15):
        csa = r * b["a_ex_thr"]
        print(f"  {r:.2f} x luas throat ex = {csa:5.0f} mm2  "
              f"(dia setara {math.sqrt(4*csa/math.pi):.1f} mm)")
