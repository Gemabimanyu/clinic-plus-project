import cadquery as cq
from OCP.BRep import BRep_Tool
from OCP.Geom import Geom_CylindricalSurface

result = cq.importers.importStep(r"C:\Users\Clinic plus\Desktop\CLAUDE PROJECT\c+ app v0.1\step example\velocity stack.step")

for f in result.faces().vals():
    if f.geomType() == "CYLINDER":
        cylinder = BRep_Tool.Surface_s(f.wrapped)
        if isinstance(cylinder, Geom_CylindricalSurface):
            r = cylinder.Radius()
            if r < 5:
                ax = cylinder.Axis()
                loc = ax.Location()
                d = ax.Direction()
                print(f"r={r:.3f} center=({loc.X():.3f},{loc.Y():.3f},{loc.Z():.3f}) dir=({d.X():.3f},{d.Y():.3f},{d.Z():.3f})")

# Also get volume
from OCP.GProp import GProp_GProps
from OCP.BRepGProp import BRepGProp
props = GProp_GProps()
BRepGProp.VolumeProperties_s(result.val().wrapped, props)
print(f"Volume: {props.Mass():.1f} mm3")
