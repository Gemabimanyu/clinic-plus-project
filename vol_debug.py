"""Compare volume per section between master STEP and our profile model."""
import math
import cadquery as cq
from OCP.BRepAlgoAPI import BRepAlgoAPI_Section
from OCP.gp import gp_Pln, gp_Pnt, gp_Dir
from OCP.TopExp import TopExp_Explorer
from OCP.TopAbs import TopAbs_EDGE
from OCP.TopoDS import TopoDS
from OCP.BRepAdaptor import BRepAdaptor_Curve
from OCP.GProp import GProp_GProps
from OCP.BRepGProp import BRepGProp

result = cq.importers.importStep(
    r"C:\Users\Clinic plus\Desktop\CLAUDE PROJECT\c+ app v0.1\step example\velocity stack.step"
)
shape = result.val().wrapped

# For each thin slice, compute actual solid area using BRepGProp on the slice
# Alternative: use known volume = 35814 and just figure out what area I need

# Get actual area at each Z by slicing and measuring edge-bounded area
# Actually simplest: use half-space to cut the solid and measure partial volumes

zs = list(range(0, 61, 1))
prev_vol = 0
print(f"{'Z':>4} {'slice_vol':>10} {'cum_vol':>10}")
for z in zs:
    from OCP.BRepAlgoAPI import BRepAlgoAPI_Cut
    from OCP.BRepPrimAPI import BRepPrimAPI_MakeHalfSpace, BRepPrimAPI_MakeBox

    # Create a box from Z=-1 to Z=z, large enough in X/Y
    box = cq.Workplane("XY").box(200, 200, z + 1, centered=(True, True, False)).translate((0, 0, -0.5))

    from OCP.BRepAlgoAPI import BRepAlgoAPI_Common
    common = BRepAlgoAPI_Common(shape, box.val().wrapped)
    common.Build()
    if common.IsDone():
        props = GProp_GProps()
        BRepGProp.VolumeProperties_s(common.Shape(), props)
        cum_vol = props.Mass()
        slice_vol = cum_vol - prev_vol
        print(f"Z={z:3d}  slice={slice_vol:8.1f}  cum={cum_vol:8.1f}")
        prev_vol = cum_vol
