"""Beban valvetrain: percepatan klep, gaya inersia, dan kebutuhan per klep.

Menjawab: berapa kekuatan per klep yang dibutuhkan supaya klep tidak floating
di rpm sasaran, dan berapa banyak yang dihemat kalau memakai klep titanium.
"""
import math

G = 9.81


def percepatan_nose(lift_mm, durasi_crank, rpm_crank):
    """Percepatan klep di puncak lobe [m/s2], profil harmonik.

    Cam berputar setengah kecepatan crank, jadi durasi dalam derajat cam
    adalah setengah durasi dalam derajat crank.
    """
    dur_cam_rad = math.radians(durasi_crank / 2.0)
    w_cam = 2 * math.pi * (rpm_crank / 2.0) / 60.0
    L = lift_mm / 1000.0
    return L / 2.0 * (2 * math.pi / dur_cam_rad) ** 2 * w_cam ** 2


def gaya_inersia(massa_g, a):
    return massa_g / 1000.0 * a          # Newton


def per_dibutuhkan(massa_g, a, faktor_aman=1.4):
    """Gaya per klep pada lift maksimum yang dibutuhkan, dalam kgf."""
    return gaya_inersia(massa_g, a) * faktor_aman / G


def rpm_floating(massa_g, gaya_per_kgf, lift_mm, durasi_crank):
    """RPM di mana per klep tidak lagi mampu menahan — perkiraan."""
    # gaya = massa x a, dan a ~ rpm^2, jadi rpm ~ sqrt(gaya/massa)
    a_maks = gaya_per_kgf * G / (massa_g / 1000.0)
    dur_cam_rad = math.radians(durasi_crank / 2.0)
    L = lift_mm / 1000.0
    w_cam2 = a_maks / (L / 2.0 * (2 * math.pi / dur_cam_rad) ** 2)
    return math.sqrt(w_cam2) * 60.0 / (2 * math.pi) * 2.0


def _selfcheck():
    a = percepatan_nose(9.0, 261.0, 12000)
    assert 10000 < a < 20000, a                       # ~1400 g, wajar
    # klep lebih berat butuh per lebih kuat
    assert per_dibutuhkan(35, a) > per_dibutuhkan(22, a)
    # rpm floating harus konsisten bolak-balik
    p = per_dibutuhkan(35, a, faktor_aman=1.0)
    r = rpm_floating(35, p, 9.0, 261.0)
    assert abs(r - 12000) < 50, r
    # lift lebih tinggi -> percepatan lebih besar
    assert percepatan_nose(11.0, 261.0, 12000) > a
    # durasi lebih panjang -> percepatan lebih kecil (ramp lebih landai)
    assert percepatan_nose(9.0, 290.0, 12000) < a
    print("selfcheck OK\n")


if __name__ == "__main__":
    _selfcheck()
    LIFT, DUR, RPM = 9.0, 261.0, 12000
    a = percepatan_nose(LIFT, DUR, RPM)
    print(f"  Lift {LIFT} mm, durasi {DUR:.0f} deg, {RPM} rpm")
    print(f"  percepatan klep di puncak lobe: {a:,.0f} m/s2 = {a/G:,.0f} g\n")

    print(f"  {'rakitan klep':28s} {'massa':>7s} {'gaya':>8s} {'per perlu':>10s}")
    print("  " + "-" * 56)
    for nm, m in (("stainless + retainer baja", 38),
                  ("stainless + retainer titanium", 32),
                  ("titanium + retainer titanium", 22)):
        print(f"  {nm:28s} {m:6.0f}g {gaya_inersia(m,a):7.0f}N "
              f"{per_dibutuhkan(m,a):9.0f} kgf")

    print(f"\n  === RPM FLOATING dengan per 65 kgf ===")
    for nm, m in (("stainless 38 g", 38), ("titanium 22 g", 22)):
        print(f"  {nm:16s} floating di ~{rpm_floating(m,65,LIFT,DUR):,.0f} rpm")

    print(f"\n  === PENGARUH LIFT dan DURASI (klep 38 g) ===")
    print(f"  {'lift':>6s} {'durasi':>7s} {'percepatan g':>13s} {'per perlu':>10s}")
    for lift in (8.0, 9.0, 10.0, 11.0):
        aa = percepatan_nose(lift, DUR, RPM)
        print(f"  {lift:5.1f}mm {DUR:6.0f}d {aa/G:12,.0f} {per_dibutuhkan(38,aa):9.0f} kgf")
    for dur in (240.0, 261.0, 290.0):
        aa = percepatan_nose(LIFT, dur, RPM)
        print(f"  {LIFT:5.1f}mm {dur:6.0f}d {aa/G:12,.0f} {per_dibutuhkan(38,aa):9.0f} kgf")
