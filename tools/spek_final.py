"""Spek cam + kompresi final, terkalibrasi ke mesin acuan yang terbukti."""
import math

import cam_dari_acuan as cda
import cam_design as cd
import kompresi_terkalibrasi as kt

RPM = 12000

if __name__ == "__main__":
    b = cda.cam_baru(RPM)
    d_ref = kt.dcr_acuan()
    d14 = kt.dcr_dari_cr(14.0, b["ivc"], cd.BORE, cd.STROKE, cd.ROD)
    k, sudut = cd.kantong_klep(b["dur"], b["ivo"])
    a = cd.anggaran_ruang_bakar(k)

    print(f"  === SPEK CAM MESIN BARU @ {RPM} rpm ===")
    print(f"  durasi in / ex     {b['dur']:.0f} / {b['dur']:.0f} deg @1mm")
    print(f"  IN  buka / tutup   {b['ivo']:.0f} BTDC / {b['ivc']:.0f} ABDC")
    print(f"  EX  buka / tutup   {b['ivc']:.0f} BBDC / {b['ivo']:.0f} ATDC")
    print(f"  ICL / ECL          {b['icl']:.1f} ATDC / {b['icl']:.1f} BTDC")
    print(f"  LSA                {b['icl']:.1f} deg")
    print(f"  overlap            {b['overlap']:.0f} deg")
    print(f"  lift maks          {cd.LIFT:.1f} mm")
    print(f"  lift di TDC        {b['lift_tdc']:.2f} mm per klep in")

    print(f"\n  === KOMPRESI ===")
    print(f"  CR statis rencana  14.0:1")
    print(f"  DCR hasilnya       {d14:.2f}")
    print(f"  DCR terbukti kamu  {d_ref:.2f}  ({kt.REF_BBM})")
    print(f"  margin             {d_ref-d14:+.2f}   <- di bawah batas = aman")
    print(f"  CR utk paritas     {kt.cr_untuk_dcr(d_ref, b['ivc'], cd.BORE, cd.STROKE, cd.ROD):.1f}:1")

    print(f"\n  === KANTONG KLEP & ANGGARAN RUANG BAKAR ===")
    print(f"  kedalaman kantong  {k:.2f} mm  (paling kritis {sudut:+.0f} deg dari TDC)")
    for nm, key in (("pent-roof", "pentroof"), ("gasket 0.8mm", "gasket"),
                    ("deck 0.5mm", "deck"), ("4 kantong klep", "kantong")):
        print(f"  {nm:18s} {a[key]:6.2f} cc")
    print(f"  {'total':18s} {a['total_tanpa_dome']:6.2f} cc")
    print(f"  {'target 14:1':18s} {a['target_vc']:6.2f} cc")
    print(f"  -> CR tanpa dome   {a['cr_tanpa_dome']:.2f}:1")
    print(f"  -> dome mengusir   {a['dome_dibutuhkan']:.2f} cc "
          f"(tinggi rata2 {a['dome_dibutuhkan']*1000/(math.pi/4*cd.BORE**2):.2f} mm)")

    # rod pendek: percepatan piston dan gaya inersia di TDC
    w = 2 * math.pi * RPM / 60.0
    r_cr = cd.STROKE / 2000.0
    l_m = cd.ROD / 1000.0
    a_tdc = w ** 2 * r_cr * (1 + r_cr / l_m)
    print(f"\n  === BEBAN MEKANIS (rod {cd.ROD:.0f} mm, rod/stroke "
          f"{cd.ROD/cd.STROKE:.2f}) ===")
    print(f"  percepatan piston di TDC  {a_tdc:,.0f} m/s2  = {a_tdc/9.81:,.0f} g")
    for m_g in (80, 100, 120):
        print(f"  gaya inersia, piston {m_g} g   {m_g/1000*a_tdc:,.0f} N "
              f"= {m_g/1000*a_tdc/9.81:,.0f} kgf")

    def g_tdc(rpm, stroke_mm, rod_mm):
        w_ = 2 * math.pi * rpm / 60.0
        r_ = stroke_mm / 2000.0
        return w_ ** 2 * r_ * (1 + r_ / (rod_mm / 1000.0)) / 9.81

    print(f"\n  === BANDINGKAN DGN MESIN YANG SUDAH KAMU JALANKAN ===")
    print(f"  {'mesin':34s} {'rpm':>7s} {'g di TDC':>10s}")
    for rod_ref in (95.0, 105.0):
        for rpm_ref in (10000, 11250):
            print(f"  acuan 199cc stroke 64, rod {rod_ref:.0f}{'':6s} {rpm_ref:7d} "
                  f"{g_tdc(rpm_ref, 64.0, rod_ref):10,.0f}")
    for rpm_b in (12000, 12500, 13000):
        print(f"  {'BARU 150cc stroke 58, rod 95':34s} {rpm_b:7d} "
              f"{g_tdc(rpm_b, cd.STROKE, cd.ROD):10,.0f}")

    # apa untungnya naik ke 15:1?
    eff = lambda cr: 1 - 1 / cr ** 0.4
    print(f"\n  === UNTUNG-RUGI NAIK KE 15:1 ===")
    print(f"  efisiensi termal ideal 14:1 -> 15:1 : "
          f"{eff(14)*100:.1f}% -> {eff(15)*100:.1f}%  (+{(eff(15)/eff(14)-1)*100:.1f}%)")
    a15 = cd.anggaran_ruang_bakar(k)
    vc15 = cd.VD / 14.0
    print(f"  ruang bakar harus turun {a['target_vc']:.2f} -> {vc15:.2f} cc")
    print(f"  dome harus mengusir {a['total_tanpa_dome']-vc15:.2f} cc "
          f"(tinggi rata2 {(a['total_tanpa_dome']-vc15)*1000/(math.pi/4*cd.BORE**2):.2f} mm)")
