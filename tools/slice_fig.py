"""Irisan medan CFD di bidang simetri (y=0): kecepatan & tekanan.

Dipakai untuk diagnosa DAN sebagai halaman visualisasi di laporan PDF.
Membaca internal.vtu ascii dari foamToVTK -- titik + PointData saja, tanpa
merekonstruksi sel (untuk gambar irisan itu sudah cukup).
"""
import sys

import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import numpy as np

import vtk_read as vr

DP = 2068.8      # tekanan total masuk, kinematik m2/s2
V_TEO = float(np.sqrt(2 * DP))


def load_slice(case, tstep, tol_mm=1.2):
    base = f"//wsl.localhost/Ubuntu/root/cfd/{case}/VTK/{case}_{tstep}"
    d = vr.read(f"{base}/internal.vtu")
    pts = d["points"] * 1000.0                    # m -> mm
    p, _ = vr.field(d, "p")
    u, _ = vr.field(d, "U")
    m = np.abs(pts[:, 1]) < tol_mm
    return pts[m], p[m], u[m]


def figure(case, tstep, judul="", mask_mm=9.0, zoom=None):
    """mask_mm: sisi segitiga maksimum. HATI-HATI -- nilai terlalu kecil
    membuang sel kasar di inti domain dan bikin 'lubang' palsu yang gampang
    disalahartikan sebagai cacat mesh. Sel background 5mm punya diagonal 8.7mm,
    jadi ambangnya harus di atas itu."""
    pts, p, u = load_slice(case, tstep)
    x, z = pts[:, 0], pts[:, 2]
    umag = np.linalg.norm(u, axis=1)
    tri = mtri.Triangulation(x, z)

    xt, zt = x[tri.triangles], z[tri.triangles]
    sisi = np.max(np.hypot(xt - np.roll(xt, 1, axis=1),
                           zt - np.roll(zt, 1, axis=1)), axis=1)
    tri.set_mask(sisi > mask_mm)

    fig, axes = plt.subplots(1, 2, figsize=(13.5, 6.2))
    fig.suptitle(judul or f"Medan CFD di bidang simetri - {case}", fontsize=12)

    c0 = axes[0].tricontourf(tri, umag, levels=40, cmap="turbo")
    fig.colorbar(c0, ax=axes[0], label="|U| [m/s]")
    axes[0].set_title(f"Kecepatan (teoretis maks {V_TEO:.0f} m/s)", fontsize=10)

    c1 = axes[1].tricontourf(tri, p, levels=40, cmap="coolwarm")
    fig.colorbar(c1, ax=axes[1], label="p kinematik [m2/s2]")
    axes[1].set_title(f"Tekanan statik (masuk {DP:.0f}, keluar 0)", fontsize=10)

    for ax in axes:
        ax.set_aspect("equal"); ax.set_xlabel("x [mm]"); ax.set_ylabel("z [mm]")
        ax.grid(alpha=0.25)
        if zoom:
            ax.set_xlim(zoom[0], zoom[1]); ax.set_ylim(zoom[2], zoom[3])
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return fig, (pts, p, u)


def ringkas(case, tstep):
    pts, p, u = load_slice(case, tstep)
    umag = np.linalg.norm(u, axis=1)
    print(f"  titik di irisan   {len(pts)}")
    print(f"  |U|  [{umag.min():6.2f} .. {umag.max():6.2f}] m/s   (teoretis {V_TEO:.1f})")
    print(f"  p    [{p.min():8.1f} .. {p.max():8.1f}]   (masuk {DP:.1f})")
    ptot = p + 0.5 * umag ** 2
    print(f"  p total [{ptot.min():8.1f} .. {ptot.max():8.1f}]")
    # di mana tekanan total sudah anjlok?
    for frac in (0.9, 0.7, 0.5, 0.3):
        m = ptot < DP * frac
        if m.any():
            print(f"    p_total < {frac*100:3.0f}% : {m.sum():6d} titik, "
                  f"x[{pts[m,0].min():6.1f}..{pts[m,0].max():6.1f}] "
                  f"z[{pts[m,2].min():6.1f}..{pts[m,2].max():6.1f}]")


if __name__ == "__main__":
    case = sys.argv[1] if len(sys.argv) > 1 else "fl_bengkok"
    tstep = sys.argv[2] if len(sys.argv) > 2 else "3000"
    ringkas(case, tstep)
    fig, _ = figure(case, tstep)
    out = f"../cfd/slice_{case}.png"
    fig.savefig(out, dpi=130)
    print(f"  gambar -> {out}")
