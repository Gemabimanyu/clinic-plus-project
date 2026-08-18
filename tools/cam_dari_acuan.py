"""Rancang cam mesin baru dgn menskalakan dari timing cam acuan yang TERBUKTI.

Timing acuan (2-klep, 199cc, 500m 15.4 detik):
    EX buka 63 BBDC, EX tutup 38 ATDC
    IN buka 38 BTDC, IN tutup 63 ABDC

Sudut jauh lebih bisa dipercaya daripada angka lift, karena tidak tergantung
tafsir "lift di TDC itu satu klep atau gabungan".
"""
import math

import cam_design as cd

# ---------------------------------------------------- CAM ACUAN (TERBUKTI)
R_IVO, R_IVC = 38.0, 63.0      # BTDC, ABDC
R_EVO, R_EVC = 63.0, 38.0      # BBDC, ATDC
R_LIFT = 10.8
R_KLEP_IN = 31.0
R_N_IN = 1
R_VD = 199.5
R_RPM = 10000
R_THROAT_A = math.pi / 4 * 29.0 ** 2
R_BORE, R_STROKE = 63.0, 64.0
R_ROD = 105.0                  # ASUMSI


def urai(ivo, ivc, evo, evc):
    dur_in = ivo + 180 + ivc
    dur_ex = evo + 180 + evc
    icl = dur_in / 2 - ivo            # ATDC
    ecl = dur_ex / 2 - evc            # BTDC
    return {
        "dur_in": dur_in, "dur_ex": dur_ex,
        "overlap": ivo + evc,
        "icl": icl, "ecl": ecl,
        "lsa": (icl + ecl) / 2,
    }


def lift_di_tdc(ivo, dur, lift_max):
    return cd.lift_pada(ivo, dur, lift_max)


def dcr_acuan(cr_statis, ivc=R_IVC, bore=R_BORE, stroke=R_STROKE, rod=R_ROD):
    s = cd.piston_dari_tdc(180 + ivc, stroke, rod)
    vd = math.pi / 4 * bore ** 2 * stroke / 1000.0
    vc = vd / (cr_statis - 1.0)
    return (vc + math.pi / 4 * bore ** 2 * s / 1000.0) / vc


def cam_baru(rpm=12000):
    """Skalakan dua besaran sekaligus:
       - time-area  (luas throat x durasi / kapasitas / rpm)  -> durasi
       - luas tirai overlap per cc                            -> lift di TDC
    """
    a = urai(R_IVO, R_IVC, R_EVO, R_EVC)
    dur = (R_THROAT_A * a["dur_in"] / (R_VD * R_RPM)) * cd.VD * rpm / cd.THROAT_A

    # luas tirai overlap per cc yang harus ditiru
    lift_tdc_ref = lift_di_tdc(R_IVO, a["dur_in"], R_LIFT)
    luas_per_cc = R_N_IN * math.pi * R_KLEP_IN * lift_tdc_ref / R_VD
    lift_tdc = luas_per_cc * cd.VD / (cd.N_KLEP_IN * math.pi * cd.KLEP_IN_DIA)

    ivo, ivc = cd.bagi_timing(dur, lift_tdc)
    return {
        "dur": dur, "ivo": ivo, "ivc": ivc,
        "icl": dur / 2 - ivo,
        "lift_tdc_ref": lift_tdc_ref, "lift_tdc": lift_tdc,
        "overlap": 2 * ivo,
        "dcr": cd.dcr(ivc),
    }


def _selfcheck():
    a = urai(R_IVO, R_IVC, R_EVO, R_EVC)
    assert abs(a["dur_in"] - 281.0) < 1e-9, a["dur_in"]
    assert abs(a["overlap"] - 76.0) < 1e-9
    assert abs(a["lsa"] - 102.5) < 1e-9, a["lsa"]
    # cam simetris: ICL dan ECL harus sama
    assert abs(a["icl"] - a["ecl"]) < 1e-9
    # DCR acuan turun kalau CR statis turun
    assert dcr_acuan(12.0) < dcr_acuan(14.0)
    # cam baru: rpm lebih tinggi -> durasi lebih panjang
    assert cam_baru(13000)["dur"] > cam_baru(11000)["dur"]
    # lift di TDC mesin baru harus LEBIH KECIL dari acuan (dua klep, bore kecil)
    b = cam_baru(12000)
    assert b["lift_tdc"] < b["lift_tdc_ref"], b
    print("selfcheck OK\n")


if __name__ == "__main__":
    _selfcheck()
    a = urai(R_IVO, R_IVC, R_EVO, R_EVC)
    print("  === CAM ACUANMU, DIURAI ===")
    print(f"  durasi in / ex     {a['dur_in']:.0f} / {a['dur_ex']:.0f} deg")
    print(f"  overlap            {a['overlap']:.0f} deg")
    print(f"  ICL / ECL          {a['icl']:.1f} ATDC / {a['ecl']:.1f} BTDC")
    print(f"  LSA                {a['lsa']:.1f} deg   (simetris, tanpa maju/mundur)")
    lt = lift_di_tdc(R_IVO, a["dur_in"], R_LIFT)
    print(f"  lift di TDC        {lt:.2f} mm per klep  "
          f"-> {2*lt:.2f} mm gabungan in+ex")
    print(f"  (angka '3.6 mm' yg kamu sebut = GABUNGAN in+ex, bukan per klep)")

    print("\n  === KOMPRESI DINAMIS MESIN ACUANMU (IVC 63 ABDC) ===")
    print(f"  {'CR statis':>10s} {'DCR':>7s}   bahan bakar")
    for cr in (11.5, 12.0, 12.5, 13.0, 13.5, 14.0):
        d = dcr_acuan(cr)
        print(f"  {cr:10.1f} {d:7.2f}   {cd.bbm_dari_dcr(d)}")

    print("\n  === CAM MESIN BARU, DISKALAKAN DARI ACUAN ===")
    print(f"  {'rpm':>6s} {'durasi':>7s} {'IVO':>6s} {'IVC':>6s} {'ICL':>6s} "
          f"{'overlap':>8s} {'lift TDC':>9s} {'DCR':>6s}")
    for rpm in (11000, 11500, 12000, 12500, 13000):
        b = cam_baru(rpm)
        print(f"  {rpm:6d} {b['dur']:7.0f} {b['ivo']:6.1f} {b['ivc']:6.1f} "
              f"{b['icl']:6.1f} {b['overlap']:8.0f} {b['lift_tdc']:9.2f} "
              f"{b['dcr']:6.2f}")
    b = cam_baru(12000)
    print(f"\n  ICL cam baru {b['icl']:.1f} vs acuan {a['icl']:.1f} "
          f"-> praktis sama, tanda penskalaannya konsisten")
