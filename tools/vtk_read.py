"""Parser VTP/VTU ascii seadanya -- cukup untuk ambil titik + medan dari foamToVTK.

ponytail: bukan pustaka VTK. foamToVTK di sini menulis XML ascii, dan yang
dibutuhkan cuma <Points> plus beberapa DataArray. Pasang pustaka VTK untuk itu
berlebihan.
"""
import re
import xml.etree.ElementTree as ET

import numpy as np


def _array(da):
    """Isi satu DataArray ascii -> ndarray (n, ncomp)."""
    if da.get("format") != "ascii":
        raise ValueError(f"DataArray '{da.get('Name')}' bukan ascii "
                         f"(format={da.get('format')}) -- jalankan foamToVTK -ascii")
    vals = np.fromstring(da.text, sep=" ")
    nc = int(da.get("NumberOfComponents", 1))
    return vals.reshape(-1, nc) if nc > 1 else vals


def read(path, fields=None):
    """Kembalikan dict: points (n,3), lalu tiap medan point-data & cell-data."""
    root = ET.parse(path).getroot()
    piece = root.find(".//Piece")
    out = {}

    pts = piece.find("Points/DataArray")
    out["points"] = _array(pts).reshape(-1, 3)

    for tag in ("PointData", "CellData"):
        blok = piece.find(tag)
        if blok is None:
            continue
        for da in blok.findall("DataArray"):
            nm = da.get("Name")
            if fields is None or nm in fields:
                out[f"{tag}:{nm}"] = _array(da)

    conn = piece.find("Polys/DataArray[@Name='connectivity']")
    offs = piece.find("Polys/DataArray[@Name='offsets']")
    if conn is not None and offs is not None:
        out["connectivity"] = _array(conn).astype(np.int64)
        out["offsets"] = _array(offs).astype(np.int64)
    return out


def poly_centroids(d):
    """Titik tengah tiap poligon, untuk memasangkan CellData dengan posisi."""
    conn, offs = d["connectivity"], d["offsets"]
    pts = d["points"]
    starts = np.concatenate([[0], offs[:-1]])
    return np.array([pts[conn[a:b]].mean(axis=0) for a, b in zip(starts, offs)])


def field(d, name):
    """Ambil medan tanpa peduli dia PointData atau CellData."""
    for k in (f"PointData:{name}", f"CellData:{name}"):
        if k in d:
            return d[k], k.split(":")[0]
    raise KeyError(f"{name} tidak ada. Tersedia: {[k for k in d if ':' in k]}")


def _selfcheck():
    import tempfile, os
    xml = """<VTKFile type='PolyData'><PolyData><Piece NumberOfPoints='3' NumberOfPolys='1'>
    <Points><DataArray type='Float32' NumberOfComponents='3' format='ascii'>
    0 0 0  1 0 0  0 1 0</DataArray></Points>
    <PointData><DataArray Name='p' format='ascii'>1 2 3</DataArray>
    <DataArray Name='U' NumberOfComponents='3' format='ascii'>1 0 0  0 1 0  0 0 1</DataArray></PointData>
    <Polys><DataArray Name='connectivity' format='ascii'>0 1 2</DataArray>
    <DataArray Name='offsets' format='ascii'>3</DataArray></Polys>
    </Piece></PolyData></VTKFile>"""
    p = os.path.join(tempfile.gettempdir(), "t.vtp")
    open(p, "w").write(xml)
    d = read(p)
    assert d["points"].shape == (3, 3), d["points"].shape
    pv, loc = field(d, "p")
    assert loc == "PointData" and np.allclose(pv, [1, 2, 3])
    uv, _ = field(d, "U")
    assert uv.shape == (3, 3)
    c = poly_centroids(d)
    assert np.allclose(c[0], [1 / 3, 1 / 3, 0]), c
    os.remove(p)
    print("selfcheck OK")


if __name__ == "__main__":
    _selfcheck()
