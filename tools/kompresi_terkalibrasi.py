"""Batas kompresi dinamis yang TERBUKTI, dikalibrasi dari mesin acuan Gema.

Mesin acuan: 199cc 2-klep, CR statis 16:1, IVC 63 ABDC, bahan bakar bensol /
avgas 100LL, terbukti 500m 15.4 detik tanpa masalah.

Tabel oktan umum bilang DCR di atas ~12.5 harus metanol. Mesin ini
membuktikan sebaliknya untuk bensol/avgas. Jadi tabel umum DIBUANG dan
diganti angka terukur dari mesin yang benar-benar jalan.
"""
import math

import cam_dari_acuan as cda
import cam_design as cd

REF_CR = 16.0
REF_BBM = "bensol / avgas 100LL"


def dcr_dari_cr(cr, ivc, bore, stroke, rod):
    """DCR linear terhadap (CR-1) untuk IVC yang sama."""
    s = cd.piston_dari_tdc(180 + ivc, stroke, rod)
    vd = math.pi / 4 * bore ** 2 * stroke / 1000.0
    v_sapu = math.pi / 4 * bore ** 2 * s / 1000.0
    return 1.0 + v_sapu * (cr - 1.0) / vd


def cr_untuk_dcr(dcr_target, ivc, bore, stroke, rod):
    """Balik: CR statis yang dibutuhkan untuk mencapai DCR tertentu."""
    s = cd.piston_dari_tdc(180 + ivc, stroke, rod)
    vd = math.pi / 4 * bore ** 2 * stroke / 1000.0
    v_sapu = math.pi / 4 * bore ** 2 * s / 1000.0
    return 1.0 + (dcr_target - 1.0) * vd / v_sapu


def dcr_acuan(rod=cda.R_ROD):
    return dcr_dari_cr(REF_CR, cda.R_IVC, cda.R_BORE, cda.R_STROKE, rod)


def _selfcheck():
    d = dcr_acuan()
    assert 12.0 < d < 13.5, d
    # bolak-balik harus konsisten
    cr = cr_untuk_dcr(d, cda.R_IVC, cda.R_BORE, cda.R_STROKE, cda.R_ROD)
    assert abs(cr - REF_CR) < 1e-9, cr
    # IVC lebih telat -> butuh CR statis lebih tinggi utk DCR yang sama
    a = cr_untuk_dcr(12.0, 70, cd.BORE, cd.STROKE, cd.ROD)
    b = cr_untuk_dcr(12.0, 50, cd.BORE, cd.STROKE, cd.ROD)
    assert a > b, (a, b)
    # rod lebih panjang sedikit menurunkan DCR (piston lebih dekat TDC saat IVC)
    assert dcr_acuan(115.0) < dcr_acuan(100.0)
    print("selfcheck OK\n")


if __name__ == "__main__":
    _selfcheck()
    print(f"  === BATAS TERBUKTI DARI MESIN ACUANMU ===")
    print(f"  CR statis {REF_CR}:1, IVC {cda.R_IVC:.0f} ABDC, {REF_BBM}")
    print(f"  {'rod (asumsi)':>14s} {'DCR':>7s}")
    for rod in (98, 102, 105, 108, 112):
        print(f"  {rod:14.0f} {dcr_acuan(rod):7.2f}")
    d_ref = dcr_acuan()
    print(f"\n  -> DCR TERBUKTI ~{d_ref:.2f} pada {REF_BBM}")
    print(f"     (tabel oktan umum bilang >12.5 harus metanol -- SALAH untuk bbm ini)")

    print(f"\n  === MESIN BARU: DCR pada rencana 14:1 ===")
    print(f"  {'rpm':>6s} {'durasi':>7s} {'IVC':>6s} {'DCR @14:1':>10s} "
          f"{'margin':>8s} {'CR utk DCR terbukti':>20s}")
    for rpm in (11000, 11500, 12000, 12500, 13000):
        b = cda.cam_baru(rpm)
        d14 = dcr_dari_cr(14.0, b["ivc"], cd.BORE, cd.STROKE, cd.ROD)
        cr_par = cr_untuk_dcr(d_ref, b["ivc"], cd.BORE, cd.STROKE, cd.ROD)
        print(f"  {rpm:6d} {b['dur']:7.0f} {b['ivc']:6.1f} {d14:10.2f} "
              f"{d_ref-d14:+8.2f} {cr_par:20.1f}")
    print("\n  margin = seberapa jauh DI BAWAH batas terbuktimu (positif = lebih aman)")
