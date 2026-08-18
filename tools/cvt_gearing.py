"""Rasio CVT, kecepatan, dan pemilihan final gear untuk lintasan tertentu.

Rasio final gear TIDAK ditebak dari katalog -- dikalibrasi dari satu titik data
yang sudah diketahui (kecepatan pada rpm tertentu). Ini cara yang sama seperti
seluruh buku: satu pengukuran mengalahkan banyak asumsi.
"""
import math


def keliling_roda(diameter_m):
    return math.pi * diameter_m


def kecepatan(rpm, i_total, d_roda):
    """km/h dari rpm mesin dan rasio reduksi total."""
    return 0.06 * math.pi * d_roda * rpm / i_total


def i_total_dari_data(rpm, v_kmh, d_roda):
    """Kalibrasi: hitung rasio total dari satu titik data terukur."""
    return 0.06 * math.pi * d_roda * rpm / v_kmh


def i_final_dari_data(rpm, v_kmh, d_roda, i_cvt_tinggi):
    return i_total_dari_data(rpm, v_kmh, d_roda) / i_cvt_tinggi


def waktu_dan_jarak(hp_roda, massa_kg, d_roda, i_total, rpm_maks,
                    cda=0.35, crr=0.02, jarak_m=500.0, dt=0.01):
    """Integrasi sederhana: percepatan dari tenaga, sampai jarak tertentu.

    Model kasar -- tanpa slip, tanpa wheelie, tanpa fase launch. Dipakai untuk
    MEMBANDINGKAN pilihan gear, bukan memprediksi waktu sebenarnya.
    """
    rho, g = 1.204, 9.81
    p = hp_roda * 745.7
    v, s, t = 0.5, 0.0, 0.0
    v_batas = kecepatan(rpm_maks, i_total, d_roda) / 3.6
    while s < jarak_m and t < 60:
        v_eff = min(v, v_batas)
        f_dorong = p / max(v_eff, 1.0) if v < v_batas else 0.0
        f_lawan = 0.5 * rho * cda * v * v + crr * massa_kg * g
        a = (f_dorong - f_lawan) / massa_kg
        v += a * dt
        v = min(v, v_batas)
        s += v * dt
        t += dt
    return {"waktu": t, "v_akhir_kmh": v * 3.6, "v_batas_kmh": v_batas * 3.6}


def _selfcheck():
    d = 0.56
    # bolak-balik kalibrasi harus konsisten
    i = i_total_dari_data(8500, 110.0, d)
    assert abs(kecepatan(8500, i, d) - 110.0) < 1e-9
    # rasio lebih besar -> lebih lambat
    assert kecepatan(10000, 10.0, d) < kecepatan(10000, 8.0, d)
    # HASIL PENTING: selama limiter tidak tersentuh, rasio gear TIDAK
    # mempengaruhi akselerasi -- CVT menahan mesin di tenaga puncak apa pun
    # rasionya. Ini berbeda total dari motor bergigi.
    a = waktu_dan_jarak(30, 150, d, 7.0, 12000)
    b = waktu_dan_jarak(30, 150, d, 6.0, 12000)
    assert abs(a["waktu"] - b["waktu"]) < 0.02, (a, b)
    # tapi gear terlalu PENDEK (mentok limiter sebelum garis) jelas merugikan
    c = waktu_dan_jarak(30, 150, d, 10.0, 12000)
    assert c["waktu"] > a["waktu"] + 0.3, (c, a)
    assert c["v_akhir_kmh"] < c["v_batas_kmh"] + 1
    print("selfcheck OK\n")


if __name__ == "__main__":
    _selfcheck()
    D_RODA = 0.56          # meter, ukur sendiri
    print(f"  Diameter roda (terpasang, dengan beban): {D_RODA} m")
    print(f"  Keliling: {keliling_roda(D_RODA):.3f} m\n")

    print("  === KALIBRASI RASIO TOTAL dari satu titik data ===")
    print(f"  {'rpm':>7s} {'v km/h':>8s} {'i_total':>9s}")
    for rpm, v in ((8500, 110), (9000, 120), (10000, 130)):
        print(f"  {rpm:7d} {v:8.0f} {i_total_dari_data(rpm, v, D_RODA):9.2f}")

    print("\n  === KECEPATAN pada berbagai rasio total ===")
    print(f"  {'i_total':>8s}" + "".join(f"{r:>9d}" for r in (10000, 11000, 12000, 13000)))
    for i in (6.0, 6.5, 7.0, 7.5, 8.0):
        baris = "".join(f"{kecepatan(r, i, D_RODA):9.0f}"
                        for r in (10000, 11000, 12000, 13000))
        print(f"  {i:8.1f}" + baris)
    print("  (km/h pada rpm mesin)")

    print("\n  === MEMILIH GEAR UNTUK 500 m (30 HP roda, 150 kg) ===")
    print(f"  {'i_total':>8s} {'v batas':>9s} {'waktu':>8s} {'v finish':>9s}")
    for i in (5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5):
        r = waktu_dan_jarak(30, 150, D_RODA, i, 12000)
        tanda = ""
        if r["v_akhir_kmh"] > r["v_batas_kmh"] - 2:
            tanda = "  <- mentok limiter"
        print(f"  {i:8.1f} {r['v_batas_kmh']:8.0f}k {r['waktu']:7.2f}s "
              f"{r['v_akhir_kmh']:8.0f}k{tanda}")
    print("\n  Gear terbaik = yang v finish-nya PAS mendekati v batas.")
    print("  Terlalu panjang: tidak sampai rpm puncak. Terlalu pendek: mentok limiter.")
