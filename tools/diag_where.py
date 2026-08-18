"""Cari DI MANA tekanan hilang sepanjang port. Diagnostik, bukan laporan."""
import sys

import numpy as np

import vtk_read as vr

DP = 2068.8   # tekanan total masuk, kinematik m2/s2


def main(case):
    base = f"//wsl.localhost/Ubuntu/root/cfd/{case}/VTK/{case}_1500"
    out = {}
    for patch in ("wall", "inlet", "outlet"):
        d = vr.read(f"{base}/boundary/{patch}.vtp")
        p, _ = vr.field(d, "p")
        u, _ = vr.field(d, "U")
        pts = d["points"]
        umag = np.linalg.norm(u, axis=1)
        out[patch] = (pts, p, umag)
        print(f"  {patch:7s} n={len(p):6d}  p [{p.min():8.1f} .. {p.max():8.1f}]"
              f"  |U| maks {umag.max():6.1f} m/s")

    pts, p, umag = out["wall"]
    # posisi sepanjang port: proyeksi ke sumbu mulut->throat
    mouth = pts[np.argmax(np.linalg.norm(pts, axis=1))]
    axis = -mouth / np.linalg.norm(mouth)
    s = (pts - mouth) @ axis

    print(f"\n  p minimum di s={s[np.argmin(p)]:.1f} mm dari mulut  (p={p.min():.0f})")
    print(f"  |U| maks di  s={s[np.argmax(umag)]:.1f} mm dari mulut  ({umag.max():.1f} m/s)")

    print("\n  profil tekanan dinding sepanjang port:")
    print(f"  {'s [mm]':>10s} {'p rata2':>10s} {'p min':>10s} {'|U| rata2':>10s}")
    tepi = np.linspace(s.min(), s.max(), 13)
    for a, b in zip(tepi[:-1], tepi[1:]):
        m = (s >= a) & (s < b)
        if m.sum() < 3:
            continue
        print(f"  {(a+b)/2:10.1f} {p[m].mean():10.1f} {p[m].min():10.1f} {umag[m].mean():10.1f}")

    # berapa banyak tekanan total yang sudah hilang di keluaran?
    pts_o, p_o, u_o = out["outlet"]
    ptot_out = p_o.mean() + 0.5 * (u_o ** 2).mean()
    print(f"\n  tekanan total di outlet {ptot_out:8.1f} / {DP:.1f} masuk "
          f"-> tersisa {ptot_out/DP*100:.1f}%")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "bell_bengkok")
