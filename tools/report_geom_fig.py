"""Gambar bentuk port: centerline, penampang, dan distribusi luas sepanjang port.

Dipakai sebagai halaman geometri di laporan PDF.
"""
import math

import matplotlib.pyplot as plt
import numpy as np

import port_geom as pg


def port_profile(csa_total, aspect, str_ratio, throat_dia,
                 downdraft=40.0, port_len=70.0):
    """Hitung ulang jalur & penampang persis seperti yang dipakai generator STL."""
    csa = csa_total / 2.0
    a_throat = math.pi / 4 * throat_dia ** 2
    port_h = math.sqrt(csa / (0.92 * aspect)) * aspect
    str_radius = str_ratio * port_h
    cl, tang = pg.centerline(port_len, downdraft, str_radius, port_h)
    n = len(cl)

    s = np.concatenate([[0], np.cumsum(np.linalg.norm(np.diff(cl, axis=0), axis=1))])
    area = np.empty(n); asp = np.empty(n)
    for i in range(n):
        f = i / (n - 1.0)
        w = 0.5 - 0.5 * math.cos(math.pi * f)
        area[i] = csa + (a_throat - csa) * w
        asp[i] = aspect + (1.0 - aspect) * w
    return {"cl": cl, "tang": tang, "s": s, "area": area, "aspect": asp,
            "port_h": port_h, "str_radius": str_radius, "csa_branch": csa,
            "a_throat": a_throat}


def outline_xz(p):
    """Dinding atas & bawah port di bidang simetri (x-z), untuk gambar potongan."""
    cl, tang, area, asp = p["cl"], p["tang"], p["area"], p["aspect"]
    top, bot = [], []
    for i in range(len(cl)):
        d = tang[i] / np.linalg.norm(tang[i])
        up = np.cross(d, np.array([0.0, 1.0, 0.0]))
        up /= np.linalg.norm(up)
        h = math.sqrt(area[i] / (0.92 * asp[i])) * asp[i]     # tinggi penampang
        top.append(cl[i] + up * h / 2)
        bot.append(cl[i] - up * h / 2)
    return np.array(top), np.array(bot)


def figure(csa_total, aspect, str_ratio, throat_dia, judul=""):
    p = port_profile(csa_total, aspect, str_ratio, throat_dia)
    top, bot = outline_xz(p)

    fig = plt.figure(figsize=(11.7, 8.3))
    fig.suptitle(judul or f"Geometri port  CSA {csa_total:.0f} mm2 (total), "
                          f"aspect {aspect:.2f}, short-turn {str_ratio:.2f}, "
                          f"throat {throat_dia:.1f} mm", fontsize=12)

    # --- potongan memanjang ---
    ax = fig.add_subplot(2, 2, (1, 2))
    ax.plot(top[:, 0], top[:, 2], "k-", lw=1.6, label="dinding luar (langit port)")
    ax.plot(bot[:, 0], bot[:, 2], "-", color="crimson", lw=1.6,
            label="dinding dalam (lantai / short turn)")
    ax.plot(p["cl"][:, 0], p["cl"][:, 2], "--", color="0.5", lw=0.9, label="centerline")
    ax.fill(np.concatenate([top[:, 0], bot[::-1, 0]]),
            np.concatenate([top[:, 2], bot[::-1, 2]]), color="steelblue", alpha=0.18)
    ax.set_aspect("equal"); ax.grid(alpha=0.3)
    ax.set_xlabel("x [mm]"); ax.set_ylabel("z [mm]")
    ax.set_title("Potongan memanjang di bidang simetri (satu cabang)", fontsize=10)
    ax.legend(fontsize=8, loc="best")

    # --- penampang di beberapa posisi ---
    ax = fig.add_subplot(2, 2, 3)
    n = len(p["s"])
    for frac, warna in ((0.0, "steelblue"), (0.5, "seagreen"), (1.0, "crimson")):
        i = min(int(frac * (n - 1)), n - 1)
        u, v = pg.superellipse(240, p["aspect"][i], p["area"][i])
        ax.plot(np.append(u, u[0]), np.append(v, v[0]), color=warna, lw=1.6,
                label=f"s={p['s'][i]:.0f} mm  A={p['area'][i]:.0f} mm2")
    ax.set_aspect("equal"); ax.grid(alpha=0.3)
    ax.set_xlabel("lebar [mm]"); ax.set_ylabel("tinggi [mm]")
    ax.set_title("Penampang: mulut - tengah - throat", fontsize=10)
    ax.legend(fontsize=8)

    # --- distribusi luas ---
    ax = fig.add_subplot(2, 2, 4)
    ax.plot(p["s"], p["area"], "k-", lw=1.8)
    ax.axhline(p["a_throat"], ls="--", color="crimson", lw=1.0,
               label=f"luas throat {p['a_throat']:.0f} mm2")
    ax.axhline(p["csa_branch"], ls="--", color="steelblue", lw=1.0,
               label=f"CSA cabang {p['csa_branch']:.0f} mm2")
    ax.grid(alpha=0.3)
    ax.set_xlabel("jarak sepanjang port [mm]"); ax.set_ylabel("luas penampang [mm2]")
    ax.set_title("Distribusi luas (menyempit halus, tanpa lonjakan)", fontsize=10)
    ax.legend(fontsize=8)

    fig.tight_layout(rect=(0, 0, 1, 0.96))
    return fig, p


def _selfcheck():
    p = port_profile(615.0, 1.30, 0.40, 20.2)
    # luas harus mulai di CSA cabang dan berakhir persis di luas throat
    assert abs(p["area"][0] - 615.0 / 2) < 1e-6, p["area"][0]
    assert abs(p["area"][-1] - p["a_throat"]) < 1e-6, p["area"][-1]
    # monoton (arah mana pun): tidak boleh ada tonjolan/cekungan lokal.
    # Arahnya sendiri tergantung rasio CSA cabang thd luas throat -- pada
    # CSA 615 mm2 cabang (307.5) LEBIH KECIL dari satu throat (320.5), jadi
    # port justru melebar sedikit ke throat. Itu geometri yang benar, bukan bug.
    d = np.diff(p["area"])
    assert np.all(d <= 1e-9) or np.all(d >= -1e-9), "luas port tidak monoton"
    # dan besarnya perubahan harus wajar, bukan lompatan
    assert abs(p["area"][-1] / p["area"][0] - 1) < 0.35, p["area"][-1] / p["area"][0]
    # aspect harus berakhir bundar di throat
    assert abs(p["aspect"][-1] - 1.0) < 1e-9
    # dinding dalam & luar tidak boleh saling menembus (short turn terlalu tajam)
    top, bot = outline_xz(p)
    assert np.all(np.linalg.norm(top - bot, axis=1) > 0.5), "dinding port berpotongan"
    print("selfcheck OK")


if __name__ == "__main__":
    _selfcheck()
    fig, p = figure(615.0, 1.30, 0.40, 20.2)
    fig.savefig("../cfd/geom_615_130_040.png", dpi=130)
    print(f"  tinggi cabang   {p['port_h']:.2f} mm")
    print(f"  short-turn R    {p['str_radius']:.2f} mm")
    print(f"  panjang jalur   {p['s'][-1]:.1f} mm")
    print("  gambar -> ../cfd/geom_615_130_040.png")

    print("\n  rasio CSA port terhadap luas throat gabungan (2 x 20.2 mm):")
    a_thr_total = 2 * math.pi / 4 * 20.2 ** 2
    for csa in (560.0, 615.0, 665.0):
        r = csa / a_thr_total
        arah = "menyempit ke throat" if r > 1 else "MELEBAR ke throat"
        print(f"    CSA {csa:.0f} mm2 -> rasio {r:.3f}  ({arah})")
    print(f"    acuan mesin terbukti: 1.035")
