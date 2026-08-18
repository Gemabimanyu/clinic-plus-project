"""Sizing head 3-klep (2 in + 1 ex), khas Vespa/Piaggio 3V-iGet.

Dikalibrasi ke mesin drag Gema yang terbukti, sama seperti perhitungan 4-klep:
    kecepatan gas di port isap ~97 m/s, port ex ~101 m/s
    time-area cam disamakan, rasio port/throat disamakan

UBAH angka di blok MESIN sesuai hasil ukurmu. Nilai bawaan adalah perkiraan
untuk Piaggio 150 3V dan HARUS diverifikasi -- diameter klep tidak
dipublikasikan dan berbeda antar varian.
"""
import math

# ------------------------------------------------------------------ MESIN
BORE = 58.0
STROKE = 58.6
IN_D = 21.0            # PERKIRAAN - ukur sendiri
EX_D = 26.0            # PERKIRAAN - ukur sendiri
N_IN, N_EX = 2, 1
RPM = 10000

# ------------------------------------------- JANGKAR DARI MESIN TERBUKTI
V_PORT_IN = 97.0       # m/s, dari mesin acuan Gema
V_PORT_EX = 101.0
RASIO_PORT_THROAT_IN = 1.035
RASIO_PORT_THROAT_EX = 1.490
THROAT_RATIO_IN = 0.935    # rasio agresif yg sudah dia buktikan
THROAT_RATIO_EX = 0.88     # sisi buang lebih konservatif (panas)

# cam acuan: 281 deg @1mm, throat 661 mm2, 199.5 cc, 10.000 rpm
REF_DUR, REF_THROAT, REF_VD, REF_RPM = 281.0, 660.5, 199.5, 10000


def luas(n, d):
    return n * math.pi / 4 * d ** 2


def spek(bore=BORE, stroke=STROKE, in_d=IN_D, ex_d=EX_D,
         n_in=N_IN, n_ex=N_EX, rpm=RPM):
    a_piston = math.pi / 4 * bore ** 2
    vd = a_piston * stroke / 1000.0
    mps = 2 * (stroke / 1000.0) * rpm / 60.0

    thr_in_d = THROAT_RATIO_IN * in_d
    thr_ex_d = THROAT_RATIO_EX * ex_d
    a_thr_in = luas(n_in, thr_in_d)
    a_thr_ex = luas(n_ex, thr_ex_d)

    # port: dua jangkar seperti biasa
    csa_in_vel = a_piston * mps / V_PORT_IN
    csa_in_rat = RASIO_PORT_THROAT_IN * a_thr_in
    csa_ex_vel = a_piston * mps / V_PORT_EX
    csa_ex_rat = RASIO_PORT_THROAT_EX * a_thr_ex

    # durasi dari time-area
    k = REF_THROAT * REF_DUR / (REF_VD * REF_RPM)
    dur_in = k * vd * rpm / a_thr_in
    dur_ex = k * vd * rpm / a_thr_ex * (a_thr_ex / a_thr_in) ** 0  # lihat catatan
    return {
        "vd": vd, "mps": mps, "a_piston": a_piston,
        "a_klep_in": luas(n_in, in_d), "a_klep_ex": luas(n_ex, ex_d),
        "in_per_bore": luas(n_in, in_d) / a_piston,
        "ex_per_in_klep": luas(n_ex, ex_d) / luas(n_in, in_d),
        "thr_in_d": thr_in_d, "thr_ex_d": thr_ex_d,
        "a_thr_in": a_thr_in, "a_thr_ex": a_thr_ex,
        "ex_per_in_throat": a_thr_ex / a_thr_in,
        "csa_in": (csa_in_vel + csa_in_rat) / 2,
        "csa_ex": (csa_ex_vel + csa_ex_rat) / 2,
        "csa_in_rentang": (min(csa_in_vel, csa_in_rat), max(csa_in_vel, csa_in_rat)),
        "csa_ex_rentang": (min(csa_ex_vel, csa_ex_rat), max(csa_ex_vel, csa_ex_rat)),
        "dur_in": dur_in,
        "lift_kritis_in": a_thr_in / (n_in * math.pi * in_d),
        "lift_kritis_ex": a_thr_ex / (n_ex * math.pi * ex_d),
    }


def _selfcheck():
    s = spek()
    assert 150 < s["vd"] < 160, s["vd"]
    # 3-klep: satu klep ex butuh lift lebih tinggi utk mencapai batas throat-nya
    assert s["lift_kritis_ex"] > s["lift_kritis_in"], s
    # bandingkan dgn 4-klep Gema: luas klep in per bore harus LEBIH KECIL
    empat = spek(57.3, 58.0, 22.0, 19.0, 2, 2, 12000)
    assert s["in_per_bore"] < empat["in_per_bore"], (s["in_per_bore"],
                                                     empat["in_per_bore"])
    # klep in lebih besar -> durasi lebih pendek utk rpm yang sama
    a = spek(in_d=23.0)["dur_in"]
    b = spek(in_d=19.0)["dur_in"]
    assert a < b, (a, b)
    print("selfcheck OK\n")


if __name__ == "__main__":
    _selfcheck()
    s = spek()
    e = spek(57.3, 58.0, 22.0, 19.0, 2, 2, 12000)

    print(f"  === 3-KLEP {BORE}x{STROKE} ({s['vd']:.1f} cc) @ {RPM} rpm ===")
    print(f"  {'':26s} {'3-KLEP':>10s} {'4-KLEP Gema':>13s}")
    print(f"  {'klep in':26s} {f'{IN_D}x{N_IN}':>10s} {'22x2':>13s}")
    print(f"  {'klep ex':26s} {f'{EX_D}x{N_EX}':>10s} {'19x2':>13s}")
    print(f"  {'luas klep in / bore':26s} {s['in_per_bore']:10.3f} "
          f"{e['in_per_bore']:13.3f}   <-- kelemahan pokok")
    print(f"  {'luas klep ex / in':26s} {s['ex_per_in_klep']:10.3f} "
          f"{e['ex_per_in_klep']:13.3f}")
    print(f"  {'throat in':26s} {s['thr_in_d']:9.1f}mm {e['thr_in_d']:12.1f}mm")
    print(f"  {'throat ex':26s} {s['thr_ex_d']:9.1f}mm {e['thr_ex_d']:12.1f}mm")
    print(f"  {'rasio throat ex/in':26s} {s['ex_per_in_throat']:10.3f} "
          f"{e['ex_per_in_throat']:13.3f}")
    print(f"  {'lift kritis in':26s} {s['lift_kritis_in']:9.2f}mm "
          f"{e['lift_kritis_in']:12.2f}mm")
    print(f"  {'lift kritis ex':26s} {s['lift_kritis_ex']:9.2f}mm "
          f"{e['lift_kritis_ex']:12.2f}mm   <-- butuh lift lebih tinggi")

    print(f"\n  === PORT ===")
    lo, hi = s["csa_in_rentang"]
    print(f"  port isap (gabungan)  {lo:.0f} - {hi:.0f} mm2   "
          f"(oval {math.sqrt(s['csa_in']/(0.92*1.3)):.1f} W x "
          f"{math.sqrt(s['csa_in']/(0.92*1.3))*1.3:.1f} H mm)")
    lo, hi = s["csa_ex_rentang"]
    print(f"  port buang            {lo:.0f} - {hi:.0f} mm2   "
          f"(dia setara {math.sqrt(4*s['csa_ex']/math.pi):.1f} mm)")

    print(f"\n  === CAM ===")
    print(f"  durasi in (time-area) {s['dur_in']:.0f} deg @1mm")
    print(f"  durasi ex             {s['dur_in']:.0f} deg  "
          f"(rasio throat {s['ex_per_in_throat']:.3f} vs 0.671 acuan)")
    if s["ex_per_in_throat"] < 0.63:
        print(f"     -> sisi buang RELATIF SEMPIT, tambah 8-12 deg durasi ex")
    elif s["ex_per_in_throat"] > 0.72:
        print(f"     -> sisi buang relatif lega, cam simetris aman")
    else:
        print(f"     -> mirip acuan, cam simetris aman")

    print(f"\n  === RPM YANG MASUK AKAL ===")
    print(f"  {'rpm':>7s} {'v port in':>10s} {'durasi in':>10s}")
    for r in (9000, 10000, 11000, 12000):
        x = spek(rpm=r)
        v = x["a_piston"] * x["mps"] / x["csa_in"]
        print(f"  {r:7d} {v:10.0f} {x['dur_in']:10.0f}")
