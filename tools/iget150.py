"""Vespa Sprint 150 i-Get: baseline standar vs potensi build drag.

CATATAN KEJUJURAN yang penting:
  - bore/stroke, kapasitas, dan tenaga standar = spesifikasi publik Piaggio
  - DIAMETER KLEP TIDAK dipublikasikan. Angka di bawah adalah rentang dari
    proporsi yang lazim di head 3-klep, BUKAN data pabrik. Ukur head-mu.
"""
import math

BORE, STROKE = 58.0, 58.6
VD = math.pi / 4 * BORE ** 2 * STROKE / 1000.0
CR_STD = 10.5
HP_STD = 12.7
RPM_STD = 7750

# proporsi lazim head 3-klep, sebagai fraksi bore
IN_FRAC = (0.33, 0.37)      # per klep isap
EX_FRAC = (0.41, 0.46)      # klep buang tunggal

THROAT_IN = 0.935           # rasio terbukti dari mesin drag Gema
THROAT_EX = 0.88
CF = 0.62                   # koefisien flow head 3-klep yg diporting baik
HP_PER_CFM = 0.45
RHO, DP28 = 1.204, 28 * 249.089


def potensi(in_d, ex_d):
    a_thr_in = 2 * math.pi / 4 * (THROAT_IN * in_d) ** 2
    v_teo = math.sqrt(2 * DP28 / RHO)
    cfm = a_thr_in * 1e-6 * v_teo * 2118.88 * CF
    return {"a_thr_in": a_thr_in, "cfm": cfm, "hp": cfm * HP_PER_CFM,
            "hp_per_l": cfm * HP_PER_CFM / (VD / 1000.0)}


def _selfcheck():
    assert 150 < VD < 160, VD
    a = potensi(19.0, 24.0)
    b = potensi(21.5, 26.7)
    assert b["hp"] > a["hp"], (a["hp"], b["hp"])
    # potensi harus jauh di atas tenaga standar (itu maksudnya build)
    assert a["hp"] > HP_STD * 1.5, a["hp"]
    # 4-klep Gema sebagai pembanding: throat 641 mm2
    empat = 641.0
    assert b["a_thr_in"] < empat, (b["a_thr_in"], empat)
    print("selfcheck OK\n")


if __name__ == "__main__":
    _selfcheck()
    print(f"  === STANDAR (spesifikasi publik Piaggio) ===")
    print(f"  {BORE} x {STROKE} mm = {VD:.1f} cc, 3-klep, pendingin UDARA")
    print(f"  CR {CR_STD}:1, {HP_STD} HP @ {RPM_STD} rpm "
          f"= {HP_STD/(VD/1000):.0f} HP/L")

    print(f"\n  === UKURAN KLEP YANG MUAT DI BORE {BORE:.0f} mm ===")
    print(f"  (proporsi lazim 3-klep, BUKAN data pabrik -- UKUR head-mu)")
    print(f"  {'':16s} {'minimum':>10s} {'maksimum':>10s}")
    print(f"  {'klep isap x2':16s} {IN_FRAC[0]*BORE:9.1f}mm {IN_FRAC[1]*BORE:9.1f}mm")
    print(f"  {'klep buang x1':16s} {EX_FRAC[0]*BORE:9.1f}mm {EX_FRAC[1]*BORE:9.1f}mm")

    print(f"\n  === POTENSI FLOW ===")
    print(f"  {'klep isap':>10s} {'throat':>8s} {'luas':>8s} {'CFM@28':>8s} "
          f"{'HP':>6s} {'HP/L':>7s}")
    for f in (0.33, 0.35, 0.37):
        d = f * BORE
        p = potensi(d, 0.44 * BORE)
        print(f"  {d:10.1f} {THROAT_IN*d:8.1f} {p['a_thr_in']:8.0f} "
              f"{p['cfm']:8.1f} {p['hp']:6.1f} {p['hp_per_l']:7.0f}")

    print(f"\n  === PEMBANDING ===")
    for nm, thr, vd_, hp in (
            ("iGet 3-klep, klep isap 21mm", 2*math.pi/4*(THROAT_IN*21)**2, VD, None),
            ("Gema 4-klep 150cc", 641.0, 149.6, 41.0),
            ("Gema 2-klep 199cc (terbukti)", 660.5, 199.5, 28.0)):
        p = thr / vd_
        print(f"  {nm:30s} throat {thr:5.0f} mm2 = {p:.2f} mm2/cc"
              + (f", {hp:.0f} HP" if hp else ""))
