"""Bandingkan kecepatan gas di port antar mesin balap.

Definisi yang dipakai (sama untuk semua, kalau tidak apel vs jeruk):
    MGV = (luas piston / luas penampang) x mean piston speed
yaitu kecepatan rata-rata gas selama langkah isap.

CATATAN KEJUJURAN: bore/stroke/rpm di bawah dari spesifikasi publik. Diameter
klep dan CSA port TIDAK dipublikasikan pabrikan -- dipakai rasio yang lazim di
kelas masing-masing dan ditandai sebagai asumsi. Jadi angka mesin balap besar
di sini adalah PERKIRAAN BERALASAN, bukan data pabrik. Dua baris terakhir
(mesin Gema) memakai ukuran terukur sungguhan.
"""
import math

# nama, bore, stroke, n_cyl, rpm, n_klep_in, rasio klep/bore, rasio port/throat, terukur?
MESIN = [
    ("F1 V10 2005 (3.0L)",        98.0, 39.8, 10, 19000, 2, 0.385, 1.10, False),
    ("F1 V8 2008 (2.4L)",         98.0, 39.75, 8, 18000, 2, 0.385, 1.10, False),
    ("F1 V6 turbo (1.6L)",        80.0, 53.0,  6, 13000, 2, 0.380, 1.10, False),
    ("MotoGP 1000 I4",            81.0, 48.5,  4, 18000, 2, 0.385, 1.08, False),
    ("NHRA Pro Stock 500ci V8",  119.4, 91.5,  8, 10500, 1, 0.545, 1.25, False),
    ("Gema 199cc 2-klep drag",    63.0, 64.0,  1, 10000, 1, 0.492, 1.035, True),
    ("Gema 150cc 4-klep (baru)",  57.3, 58.0,  1, 12000, 2, 0.384, 1.038, True),
]

THROAT_PER_KLEP = 0.90     # rasio throat/diameter klep, lazim di mesin balap


def hitung(bore, stroke, rpm, n_klep, r_klep, r_port, throat_ratio=THROAT_PER_KLEP):
    a_piston = math.pi / 4 * bore ** 2
    d_klep = r_klep * bore
    d_throat = throat_ratio * d_klep
    a_throat = n_klep * math.pi / 4 * d_throat ** 2
    a_port = r_port * a_throat
    mps = 2 * (stroke / 1000.0) * rpm / 60.0
    return {
        "mps": mps,
        "d_klep": d_klep,
        "d_throat": d_throat,
        "a_throat": a_throat,
        "a_port": a_port,
        "klep_per_bore": n_klep * math.pi / 4 * d_klep ** 2 / a_piston,
        "v_throat": a_piston / a_throat * mps,
        "v_port": a_piston / a_port * mps,
    }


def _selfcheck():
    # mesin acuan Gema harus mereproduksi angka terukur: throat 29mm, port 683mm2
    r = hitung(63.0, 64.0, 10000, 1, 0.492, 1.035)
    assert abs(r["d_klep"] - 31.0) < 0.2, r["d_klep"]
    assert abs(r["d_throat"] - 27.9) < 0.5, r["d_throat"]
    # v_port acuan sekitar 97-101 m/s (terukur 97 dgn port 683mm2)
    assert 90 < r["v_port"] < 110, r["v_port"]
    # HASIL PENTING: bore hilang dari persamaan. Kalau semua proporsi diskalakan
    # ke bore, kecepatan port cuma bergantung mean piston speed + proporsi klep,
    # BUKAN ukuran mesin. Mesin 3 liter dan 150cc bisa persis sama.
    a = hitung(100.0, 60.0, 10000, 2, 0.385, 1.1)["v_port"]
    b = hitung(80.0, 60.0, 10000, 2, 0.385, 1.1)["v_port"]
    assert abs(a - b) < 1e-9, (a, b)
    # yang benar-benar menaikkan kecepatan: mean piston speed
    c = hitung(80.0, 60.0, 14000, 2, 0.385, 1.1)["v_port"]
    assert c > b, (c, b)
    # dan klep yang lebih kecil relatif thd bore
    d = hitung(80.0, 60.0, 10000, 2, 0.340, 1.1)["v_port"]
    assert d > b, (d, b)
    print("selfcheck OK\n")


if __name__ == "__main__":
    _selfcheck()
    hdr = (f"{'mesin':28s} {'MPS':>6s} {'klep':>6s} {'throat':>7s} "
           f"{'A/bore':>7s} {'v thrt':>7s} {'v port':>7s}")
    print(hdr); print("-" * len(hdr))
    for nm, b, s, nc, rpm, nk, rk, rp, ukur in MESIN:
        r = hitung(b, s, rpm, nk, rk, rp)
        tandai = "" if ukur else "  ~"
        print(f"{nm:28s} {r['mps']:6.1f} {r['d_klep']:6.1f} {r['d_throat']:7.1f} "
              f"{r['klep_per_bore']:7.3f} {r['v_throat']:7.0f} {r['v_port']:7.0f}{tandai}")
    print("\n  MPS = mean piston speed m/s | A/bore = luas klep in / luas bore")
    print("  v = m/s | ~ = ukuran klep & port ASUMSI, bukan data pabrik")
