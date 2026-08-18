"""Tenaga spesifik (HP/liter) antar mesin, plus perkiraan tenaga mesin Gema
dari hasil Racebox 500m.

Metode untuk mesin Gema: neraca energi sepanjang lintasan, bukan rumus jempol.
Energi total = energi kinetik di garis + rugi aero + rugi gelinding.
Semua asumsi (berat, CdA, Crr) dibuat eksplisit dan bisa diubah.
"""
import math

RHO = 1.204
G = 9.81

# nama, kapasitas L, HP, NA?, catatan
MESIN = [
    ("F1 V10 2005",        3.0,  950, True,  "19.000 rpm"),
    ("F1 V8 2008",         2.4,  750, True,  "18.000 rpm"),
    ("MotoGP 1000 I4",     1.0,  290, True,  "18.000 rpm"),
    ("F1 V6 turbo (ICE)",  1.6,  900, False, "turbo, tidak sebanding"),
    ("NHRA Pro Stock",     8.19, 1350, True, "10.500 rpm, 2 klep pushrod"),
]


def tenaga_dari_lintasan(jarak_m=500.0, waktu_s=15.4, trap_kmh=158.0,
                         massa_kg=150.0, cda=0.35, crr=0.02, eff_puncak=0.80):
    """Perkiraan tenaga di roda dari satu lintasan drag.

    eff_puncak = rasio daya rata-rata terhadap daya puncak. CVT menahan mesin
    dekat puncak hampir sepanjang lintasan, tapi fase launch dibatasi traksi,
    jadi 0.75-0.85 wajar.
    """
    v = trap_kmh / 3.6
    e_kinetik = 0.5 * massa_kg * v ** 2
    # kecepatan naik ~linear thd waktu -> rata-rata v^3 = v_maks^3 / 4
    e_aero = 0.5 * RHO * cda * (v ** 3 / 4) * waktu_s
    e_gelinding = crr * massa_kg * G * jarak_m
    e_total = e_kinetik + e_aero + e_gelinding
    p_rata = e_total / waktu_s
    p_puncak = p_rata / eff_puncak
    return {
        "v_trap_ms": v,
        "e_kinetik": e_kinetik, "e_aero": e_aero, "e_gelinding": e_gelinding,
        "hp_rata_roda": p_rata / 745.7,
        "hp_puncak_roda": p_puncak / 745.7,
        "hp_puncak_crank": p_puncak / 745.7 / 0.88,   # rugi CVT+transmisi ~12%
    }


def _selfcheck():
    r = tenaga_dari_lintasan()
    # energi kinetik harus komponen terbesar
    assert r["e_kinetik"] > r["e_aero"] > r["e_gelinding"], r
    # motor lebih berat butuh tenaga lebih besar utk trap yang sama
    a = tenaga_dari_lintasan(massa_kg=180)["hp_puncak_roda"]
    b = tenaga_dari_lintasan(massa_kg=150)["hp_puncak_roda"]
    assert a > b, (a, b)
    # trap lebih tinggi -> tenaga lebih besar, dan naiknya tajam (v^2 dan v^3)
    c = tenaga_dari_lintasan(trap_kmh=170)["hp_puncak_roda"]
    assert c > b * 1.1, (c, b)
    # cek kewarasan besaran: matic drag 200cc harus di 20-60 HP
    assert 20 < r["hp_puncak_crank"] < 60, r["hp_puncak_crank"]
    print("selfcheck OK\n")


if __name__ == "__main__":
    _selfcheck()

    print("  === TENAGA SPESIFIK MESIN BALAP ===")
    print(f"  {'mesin':22s} {'liter':>6s} {'HP':>6s} {'HP/L':>7s}   catatan")
    for nm, L, hp, na, cat in MESIN:
        tag = "" if na else "  (turbo)"
        print(f"  {nm:22s} {L:6.2f} {hp:6.0f} {hp/L:7.0f}{tag}   {cat}")

    print("\n  === MESIN ACUANMU, dari Racebox 500m 15.4s @ 158 km/h ===")
    for m in (140, 150, 165):
        r = tenaga_dari_lintasan(massa_kg=m)
        print(f"  massa {m} kg -> puncak roda {r['hp_puncak_roda']:5.1f} HP, "
              f"crank {r['hp_puncak_crank']:5.1f} HP, "
              f"HP/L {r['hp_puncak_crank']/0.1995:5.0f}")
    r = tenaga_dari_lintasan()
    print(f"\n  rincian energi (massa 150 kg): kinetik {r['e_kinetik']/1000:.0f} kJ, "
          f"aero {r['e_aero']/1000:.0f} kJ, gelinding {r['e_gelinding']/1000:.0f} kJ")

    print("\n  === MESIN BARUMU (potensi dari flow head) ===")
    for hp in (35, 40, 41):
        print(f"  {hp} HP dari 149.6 cc -> {hp/0.1496:5.0f} HP/L")
