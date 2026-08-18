"""Periksa patch inlet: apakah benar-benar permukaan bola plenum, atau ada
bagian sempit berkecepatan tinggi yang salah tertandai."""
import sys

import numpy as np

import vtk_read as vr

BALL_R = 0.080   # meter. foamToVTK menulis dalam satuan solver (m), bukan mm.


def poly_areas(d):
    conn, offs, pts = d["connectivity"], d["offsets"], d["points"]
    starts = np.concatenate([[0], offs[:-1]])
    ar, cen = [], []
    for a, b in zip(starts, offs):
        q = pts[conn[a:b]]
        n = np.zeros(3)
        for i in range(len(q)):
            n = n + np.cross(q[i], q[(i + 1) % len(q)])
        ar.append(np.linalg.norm(n) / 2)
        cen.append(q.mean(axis=0))
    return np.array(ar), np.array(cen)


def main(case):
    base = f"//wsl.localhost/Ubuntu/root/cfd/{case}/VTK/{case}_1500"
    d = vr.read(f"{base}/boundary/inlet.vtp")
    u = d["CellData:U"]
    umag = np.linalg.norm(u, axis=1)
    ar, cen = poly_areas(d)

    print(f"  jumlah face      {len(ar)}")
    print(f"  luas total       {ar.sum()*1e6:10.1f} mm2")
    print(f"  luas bola penuh  {4*np.pi*BALL_R**2*1e6:10.1f} mm2")

    c0 = (cen * ar[:, None]).sum(axis=0) / ar.sum()
    r = np.linalg.norm(cen - c0, axis=1) * 1000.0        # -> mm
    print(f"  jari-jari face   [{r.min():7.2f} .. {r.max():7.2f}] mm")

    cepat = umag > 5.0
    print(f"\n  face dgn |U| > 5 m/s : {cepat.sum()} dari {len(ar)}")
    print(f"  luasnya              : {ar[cepat].sum()*1e6:.1f} mm2 "
          f"({ar[cepat].sum()/ar.sum()*100:.2f}% dari patch)")
    if cepat.any():
        print(f"  jari-jari face cepat : [{r[cepat].min():.2f} .. {r[cepat].max():.2f}] mm")
        print(f"  |U| di situ          : [{umag[cepat].min():.1f} .. {umag[cepat].max():.1f}] m/s")
        q_cepat = (umag[cepat] * ar[cepat]).sum()
        q_tot = (umag * ar).sum()
        print(f"  perkiraan debit lewat face cepat: {q_cepat/q_tot*100:.1f}% dari total")
        print(f"  sebaran posisi face cepat (mm): "
              f"x[{cen[cepat,0].min()*1e3:.0f}..{cen[cepat,0].max()*1e3:.0f}] "
              f"y[{cen[cepat,1].min()*1e3:.0f}..{cen[cepat,1].max()*1e3:.0f}] "
              f"z[{cen[cepat,2].min()*1e3:.0f}..{cen[cepat,2].max()*1e3:.0f}]")
        print(f"  luas rata2 face cepat : {ar[cepat].mean()*1e6:.3f} mm2"
              f"   vs lambat {ar[~cepat].mean()*1e6:.3f} mm2")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "bell_bengkok")
