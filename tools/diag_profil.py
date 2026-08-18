"""Profil kecepatan melintang di dalam saluran, dari data mentah.

Plot bisa menipu (mask, interpolasi tepi). Ini membaca titik langsung:
di satu ketinggian z, urutkan menurut x dan cetak |U|. Aliran saluran normal
harus berbentuk kubah: nol di dinding, maksimum di tengah.
"""
import sys

import numpy as np

import slice_fig as sf


AX = np.array([-np.sin(np.radians(13.0)), 0.0, -np.cos(np.radians(13.0))])


def main(case, tstep, z_list=(10.0, 25.0, 40.0)):
    pts, p, u = sf.load_slice(case, tstep, tol_mm=1.2)
    umag = np.linalg.norm(u, axis=1)
    u_ax = u @ AX                     # + = mengalir keluar lewat throat
    print(f"  komponen aksial: min {u_ax.min():.1f}  maks {u_ax.max():.1f} m/s")
    print(f"  titik dgn aliran BALIK (u_ax<0): {(u_ax<0).sum()} dari {len(u_ax)}"
          f"  ({(u_ax<0).mean()*100:.1f}%)")
    print(f"  komponen y (swirl): maks |Uy| {np.abs(u[:,1]).max():.1f} m/s")
    for z0 in z_list:
        m = np.abs(pts[:, 2] - z0) < 1.0
        if m.sum() < 5:
            print(f"  z={z0}: cuma {m.sum()} titik")
            continue
        x = pts[m, 0]
        v = u[m] @ AX                 # aksial bertanda, bukan |U|
        o = np.argsort(x)
        x, v = x[o], v[o]
        print(f"\n  z = {z0:.0f} mm   lebar fluida {x.min():.1f} .. {x.max():.1f} mm "
              f"({x.max()-x.min():.1f} mm), {m.sum()} titik")
        # rangkum jadi 14 bin supaya terbaca
        tepi = np.linspace(x.min(), x.max(), 15)
        baris = []
        for a, b in zip(tepi[:-1], tepi[1:]):
            k = (x >= a) & (x < b)
            baris.append(f"{v[k].mean():5.1f}" if k.sum() else "    -")
        print("   x :", "".join(f"{(a+b)/2:6.1f}" for a, b in zip(tepi[:-1], tepi[1:])))
        print("   |U|:", "".join(f"{s:>6s}" for s in baris))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "pipa",
         sys.argv[2] if len(sys.argv) > 2 else "3000")
