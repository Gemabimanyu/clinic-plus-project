"""Diagnostik: pisahkan rugi TIKUNGAN dari rugi MULUT port.

Bikin port yang nyaris lurus (downdraft 70 deg -> tikungan cuma ~7 deg) dengan
mulut dan throat identik. Kalau Cf-nya melonjak, rugi didominasi tikungan dan
Cf 0.56 di port bengkok itu fisika sungguhan. Kalau Cf tetap rendah, ruginya
ada di mulut port -- artefak cara plenum ditempel, harus diperbaiki sebelum
36 case dijalankan.
"""
import cfd_case
import port_geom as pg

STL = "../cfd/stl/_diag_lurus.stl"
CASE = "../cfd/run/diag_lurus"

if __name__ == "__main__":
    r = pg.generate(STL, 615.0, 1.30, 0.40, 20.2, downdraft=70.0)
    print(f"  tinggi cabang    {r['port_h_mm']:.2f} mm")
    print(f"  rasio outlet/throat {r['rasio_outlet_throat']:.4f}")
    print(f"  volume port      {r['port_volume_mm3']:.0f} mm3")
    info = cfd_case.build(STL, CASE, n_proc=8)
    print(f"  case -> {CASE}, background {info['bg_cells']}")
