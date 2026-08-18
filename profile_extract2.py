import cadquery as cq
from OCP.BRepAlgoAPI import BRepAlgoAPI_Section
from OCP.gp import gp_Pln, gp_Pnt, gp_Dir
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_EDGE
from OCP.TopoDS import TopoDS
from OCP.BRepAdaptor import BRepAdaptor_Curve
import math

result = cq.importers.importStep(
    r"C:\Users\Clinic plus\Desktop\CLAUDE PROJECT\c+ app v0.1\step example\velocity stack.step"
)
shape = result.val().wrapped

for z in [50.0, 50.5, 50.8, 50.9, 51.0, 51.5, 52.0, 55.0, 58.0, 59.0, 59.5, 59.8, 59.9, 60.0]:
    plane = gp_Pln(gp_Pnt(0, 0, z), gp_Dir(0, 0, 1))
    section = BRepAlgoAPI_Section(shape, plane)
    section.Build()
    if not section.IsDone():
        print(f"Z={z:6.1f}  FAILED")
        continue
    radii = []
    explorer = TopExp_Explorer(section.Shape(), TopAbs_EDGE)
    while explorer.More():
        edge = TopoDS.Edge_s(explorer.Current())
        curve = BRepAdaptor_Curve(edge)
        for u in [curve.FirstParameter(), (curve.FirstParameter()+curve.LastParameter())/2, curve.LastParameter()]:
            pt = curve.Value(u)
            r = math.sqrt(pt.X()**2 + pt.Y()**2)
            radii.append(r)
        explorer.Next()
    if radii:
        print(f"Z={z:6.1f}  r_min={min(radii):7.3f}  r_max={max(radii):7.3f}")
    else:
        print(f"Z={z:6.1f}  NO EDGES")
