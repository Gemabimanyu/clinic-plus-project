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

for z in [50, 50.5, 51, 51.5, 52, 53, 54, 55, 56, 56.5, 57, 57.5, 58, 58.5, 59, 59.5, 59.8, 59.9]:
    plane = gp_Pln(gp_Pnt(0, 0, z), gp_Dir(0, 0, 1))
    section = BRepAlgoAPI_Section(shape, plane)
    section.Build()
    radii = []
    explorer = TopExp_Explorer(section.Shape(), TopAbs_EDGE)
    while explorer.More():
        edge = TopoDS.Edge_s(explorer.Current())
        curve = BRepAdaptor_Curve(edge)
        u1, u2 = curve.FirstParameter(), curve.LastParameter()
        for i in range(51):
            u = u1 + (u2 - u1) * i / 50
            pt = curve.Value(u)
            r = math.sqrt(pt.X()**2 + pt.Y()**2)
            radii.append(round(r, 3))
        explorer.Next()
    unique_r = sorted(set(radii))
    # Group into clusters
    clusters = []
    if unique_r:
        cluster = [unique_r[0]]
        for r in unique_r[1:]:
            if r - cluster[-1] < 0.5:
                cluster.append(r)
            else:
                clusters.append((min(cluster), max(cluster)))
                cluster = [r]
        clusters.append((min(cluster), max(cluster)))
    print(f"Z={z:5.1f}  rings={clusters}")
