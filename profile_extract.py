"""Extract cross-section profile from master STEP at multiple Z heights."""
import cadquery as cq
from OCP.GProp import GProp_GProps
from OCP.BRepGProp import BRepGProp
from OCP.BRepAlgoAPI import BRepAlgoAPI_Section
from OCP.gp import gp_Pln, gp_Pnt, gp_Dir
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_EDGE
from OCP.TopoDS import TopoDS
from OCP.BRep import BRep_Tool
from OCP.GCPnts import GCPnts_UniformAbscissa
from OCP.BRepAdaptor import BRepAdaptor_Curve
import math

result = cq.importers.importStep(
    r"C:\Users\Clinic plus\Desktop\CLAUDE PROJECT\c+ app v0.1\step example\velocity stack.step"
)
shape = result.val().wrapped

z_values = [0, 2, 4, 5, 6, 8, 10, 12, 14, 16, 17, 20, 25, 30, 35, 40, 45, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

for z in z_values:
    plane = gp_Pln(gp_Pnt(0, 0, z), gp_Dir(0, 0, 1))
    section = BRepAlgoAPI_Section(shape, plane)
    section.Build()
    if not section.IsDone():
        continue
    section_shape = section.Shape()

    radii = []
    explorer = TopExp_Explorer(section_shape, TopAbs_EDGE)
    while explorer.More():
        edge = TopoDS.Edge_s(explorer.Current())
        curve = BRepAdaptor_Curve(edge)
        u1 = curve.FirstParameter()
        u2 = curve.LastParameter()
        for u in [u1, (u1+u2)/2, u2]:
            pt = curve.Value(u)
            r = math.sqrt(pt.X()**2 + pt.Y()**2)
            radii.append(r)
        explorer.Next()

    if radii:
        print(f"Z={z:5.1f}  r_min={min(radii):7.3f}  r_max={max(radii):7.3f}")
