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

for z in [57.0, 57.2, 57.4, 57.5, 57.6, 57.7, 57.8, 57.9, 58.0]:
    plane = gp_Pln(gp_Pnt(0, 0, z), gp_Dir(0, 0, 1))
    section = BRepAlgoAPI_Section(shape, plane)
    section.Build()
    radii = []
    explorer = TopExp_Explorer(section.Shape(), TopAbs_EDGE)
    while explorer.More():
        edge = TopoDS.Edge_s(explorer.Current())
        curve = BRepAdaptor_Curve(edge)
        u1, u2 = curve.FirstParameter(), curve.LastParameter()
        for i in range(101):
            u = u1 + (u2 - u1) * i / 100
            pt = curve.Value(u)
            r = math.sqrt(pt.X()**2 + pt.Y()**2)
            radii.append(r)
        explorer.Next()
    sorted_r = sorted(set(round(r, 2) for r in radii))
    clusters = []
    cluster = [sorted_r[0]]
    for r in sorted_r[1:]:
        if r - cluster[-1] < 0.3:
            cluster.append(r)
        else:
            clusters.append((min(cluster), max(cluster)))
            cluster = [r]
    clusters.append((min(cluster), max(cluster)))
    print(f"Z={z:5.2f} rings={[(round(a,2),round(b,2)) for a,b in clusters]}")
