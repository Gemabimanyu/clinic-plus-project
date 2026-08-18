"""Ukur penampang solid port LANGSUNG dari STL, sepanjang jalurnya.

Cek terakhir yang belum pernah dilakukan: apakah solid hasil sapuan benar-benar
punya luas penampang yang diniatkan di setiap posisi, atau ada penyempitan /
saling-tembus yang tidak terlihat dari volume total.

Metode: potong segitiga STL dengan bidang tegak lurus sumbu, kumpulkan ruas
garis perpotongan, lalu luas dihitung dgn shoelace setelah diurutkan sudut.
"""
import math
import sys

import numpy as np


def read_stl(path):
    v = []
    with open(path) as f:
        for line in f:
            s = line.lstrip()
            if s.startswith("vertex"):
                v.append([float(x) for x in s.split()[1:4]])
    return np.asarray(v).reshape(-1, 3, 3)


def plane_section_area(tris, origin, normal):
    """Luas penampang solid pada bidang (origin, normal)."""
    n = normal / np.linalg.norm(normal)
    d = (tris - origin) @ n                       # (ntri, 3) jarak bertanda
    sisi = d > 0
    n_pos = sisi.sum(axis=1)
    kena = (n_pos == 1) | (n_pos == 2)
    if not kena.any():
        return 0.0, 0
    segs = []
    for tri, dd, sp in zip(tris[kena], d[kena], sisi[kena]):
        pts = []
        for i in range(3):
            j = (i + 1) % 3
            if sp[i] != sp[j]:
                t = dd[i] / (dd[i] - dd[j])
                pts.append(tri[i] + t * (tri[j] - tri[i]))
        if len(pts) == 2:
            segs.append(pts)
    if len(segs) < 3:
        return 0.0, len(segs)
    P = np.array([s[0] for s in segs])
    # basis dalam bidang
    a = np.array([1.0, 0, 0])
    if abs(a @ n) > 0.9:
        a = np.array([0, 1.0, 0])
    e1 = np.cross(n, a); e1 /= np.linalg.norm(e1)
    e2 = np.cross(n, e1)
    q = np.stack([(P - origin) @ e1, (P - origin) @ e2], axis=1)
    c = q.mean(axis=0)
    ang = np.arctan2(q[:, 1] - c[1], q[:, 0] - c[0])
    q = q[np.argsort(ang)]
    area = 0.5 * abs(np.sum(q[:, 0] * np.roll(q[:, 1], -1)
                            - np.roll(q[:, 0], -1) * q[:, 1]))
    return area, len(segs)


def main(stl, downdraft, harapan):
    tris = read_stl(stl)
    th = math.radians(downdraft)
    tilt = math.radians(13.0)
    d_in = np.array([-math.cos(th), 0.0, -math.sin(th)])
    d_out = np.array([-math.sin(tilt), 0.0, -math.cos(tilt)])
    print(f"  {stl}   {len(tris)} segitiga")
    print(f"  {'posisi':>10s} {'luas mm2':>10s} {'ruas':>6s}   harapan {harapan:.1f}")
    # potong tegak lurus sumbu keluar, dari throat (origin) mundur ke hulu
    for s in (2, 6, 12, 20, 30, 40, 50, 60):
        o = -d_out * s          # mundur dari throat sepanjang sumbu klep
        a, ns = plane_section_area(tris, o, d_out)
        tanda = "" if abs(a / harapan - 1) < 0.25 else "   <-- MELESET"
        print(f"  {s:10.0f} {a:10.1f} {ns:6d}{tanda}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "../cfd/stl/_pipa_core.stl",
         float(sys.argv[2]) if len(sys.argv) > 2 else 70.0,
         float(sys.argv[3]) if len(sys.argv) > 3 else math.pi / 4 * 20.2 ** 2)
