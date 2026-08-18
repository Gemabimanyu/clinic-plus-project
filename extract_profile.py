"""Cut master STEP with XZ plane to get the 2D revolution profile."""
import cadquery as cq
from OCP.BRepAlgoAPI import BRepAlgoAPI_Section
from OCP.gp import gp_Pln, gp_Pnt, gp_Dir
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_EDGE
from OCP.TopoDS import TopoDS
from OCP.BRepAdaptor import BRepAdaptor_Curve

result = cq.importers.importStep(
    r"C:\Users\Clinic plus\Desktop\CLAUDE PROJECT\c+ app v0.1\step example\velocity stack.step"
)
shape = result.val().wrapped

# Cut with XZ plane (Y=0)
plane = gp_Pln(gp_Pnt(0, 0, 0), gp_Dir(0, 1, 0))
section = BRepAlgoAPI_Section(shape, plane)
section.Build()

# Extract all edge points
edges = []
explorer = TopExp_Explorer(section.Shape(), TopAbs_EDGE)
while explorer.More():
    edge = TopoDS.Edge_s(explorer.Current())
    curve = BRepAdaptor_Curve(edge)
    u1, u2 = curve.FirstParameter(), curve.LastParameter()
    pts = []
    for i in range(101):
        u = u1 + (u2 - u1) * i / 100
        pt = curve.Value(u)
        pts.append((pt.X(), pt.Z()))
    edges.append(pts)
    explorer.Next()

print(f"Found {len(edges)} edges in XZ cross-section")
# Print each edge's start/end and a few sample points
for i, pts in enumerate(edges):
    # Only positive X (right half = outer profile for revolve)
    pos_pts = [(x, z) for x, z in pts if x >= -0.1]
    if pos_pts:
        print(f"\nEdge {i}: {len(pos_pts)} pts, X=[{min(p[0] for p in pos_pts):.2f}..{max(p[0] for p in pos_pts):.2f}], Z=[{min(p[1] for p in pos_pts):.2f}..{max(p[1] for p in pos_pts):.2f}]")
        # Print every 10th point
        for j in range(0, len(pos_pts), 10):
            print(f"  ({pos_pts[j][0]:7.3f}, {pos_pts[j][1]:7.3f})")
        if len(pos_pts) % 10 != 1:
            print(f"  ({pos_pts[-1][0]:7.3f}, {pos_pts[-1][1]:7.3f})")
