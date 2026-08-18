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

for z in [50.0, 51.0, 52.0, 54.0, 56.0, 58.0, 59.0]:
    plane = gp_Pln(gp_Pnt(0, 0, z), gp_Dir(0, 0, 1))
    section = BRepAlgoAPI_Section(shape, plane)
    section.Build()
    radii = set()
    explorer = TopExp_Explorer(section.Shape(), TopAbs_EDGE)
    while explorer.More():
        edge = TopoDS.Edge_s(explorer.Current())
        curve = BRepAdaptor_Curve(edge)
        u1, u2 = curve.FirstParameter(), curve.LastParameter()
        for i in range(21):
            u = u1 + (u2 - u1) * i / 20
            pt = curve.Value(u)
            r = math.sqrt(pt.X()**2 + pt.Y()**2)
            radii.add(round(r, 2))
        explorer.Next()
    sorted_r = sorted(radii)
    print(f"Z={z:5.1f}  radii={sorted_r}")
