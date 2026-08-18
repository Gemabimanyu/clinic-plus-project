"""Bandingkan luas patch di MESH dengan luas yang diharapkan dari geometri.

Kalau snappyHexMesh gagal menangkap sebagian patch, luasnya menyusut dan
aliran tersumbat -- padahal keseimbangan massa tetap sempurna dan checkMesh
tetap bilang OK. Ini cek yang tidak dilakukan keduanya.
"""
import sys

import numpy as np

import vtk_read as vr


def patch_area_and_flux(base, patch):
    d = vr.read(f"{base}/boundary/{patch}.vtp")
    conn, offs, pts = d["connectivity"], d["offsets"], d["points"]
    starts = np.concatenate([[0], offs[:-1]])
    ar = np.empty(len(offs))
    nrm = np.empty((len(offs), 3))
    for i, (a, b) in enumerate(zip(starts, offs)):
        q = pts[conn[a:b]]
        n = np.zeros(3)
        for k in range(len(q)):
            n = n + np.cross(q[k], q[(k + 1) % len(q)])
        n = n / 2
        ar[i] = np.linalg.norm(n)
        nrm[i] = n
    u = d["CellData:U"]
    q = float(np.abs((u * nrm).sum(axis=1)).sum())
    return ar.sum(), q, len(ar), np.linalg.norm(u, axis=1)


def main(case, tstep):
    base = f"//wsl.localhost/Ubuntu/root/cfd/{case}/VTK/{case}_{tstep}"
    print(f"  {'patch':8s} {'luas mm2':>12s} {'n face':>8s} {'|U| maks':>10s} {'|U| rata2':>10s}")
    for p in ("inlet", "outlet", "wall", "flange"):
        try:
            a, q, n, umag = patch_area_and_flux(base, p)
        except FileNotFoundError:
            print(f"  {p:8s} (tidak ada)")
            continue
        print(f"  {p:8s} {a*1e6:12.1f} {n:8d} {umag.max():10.1f} {umag.mean():10.2f}")

    print(f"\n  harapan: outlet = 320.5 mm2 (throat 20.2mm)")
    print(f"           inlet  = 40212  mm2 (setengah bola R80)")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "fl_bengkok",
         sys.argv[2] if len(sys.argv) > 2 else "3000")
