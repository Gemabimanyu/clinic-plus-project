# Intake Manifold Generator — Spec (Honda Vario 150 reference)

Single-runner intake manifold generator. Parametric, seeded from the user's
VARIO 150 STEP kit. **Live 2D cross-section**; **3D generated on demand** (not
live); watertight STL for 3D printing.

## Architecture (flow of air, head → throttle body)
`Port flange (head side)` → `tapered + bent runner` → `throttle-body coupling`
with a **selectable injector boss** mounted on the runner.

## Measured dimensions from the STEP kit (mm)
Source files in `STEP/VARIO 150/`.

### Port flange — "fixed flange (2 bolt) intake port bore (id)"
- Port bore Ø **30.2** (the head intake port)
- Spigot Ø **44** that enters the head
- **2 bolts**: Ø6.7 holes, Ø11 counterbore; centers (−77.6, 22.3) & (−69.3, −22.3)
  → **bolt center-spacing ≈ 45.4 mm**, line tilted ≈10.5° from vertical
- Flange plate ~7 mm thick (face plane at z = −7)

### Throttle-body end — "throttle body bore (id) rubber size (od)"
- Throttle body bore Ø **38**
- Rubber coupling OD ≈ Ø **47.9** (r 23.95), ID ≈ Ø43 (r 21.5)
- 45° lead-in chamfer; wavy rubber profile is a B-spline (cosmetic)

### Injector boss options (selectable dropdown)
- **Honda + Yamaha joint** ("injector honda + yamaha joint"): body Ø19.8 (r9.9),
  pintle Ø9 (r4.5), o-ring groove (torus 7.65×2.25), 45° seat, seat torus 21.17×16.5
- **Yamaha joint** ("yamaha joint"): spigot Ø31.4 (r15.7), step Ø26 (r13)/Ø21.8 (r10.9),
  bolt holes Ø7.2 (r3.6)

## Live 2D parameters (drag → instant 2D redraw)
- intake **port Ø** (default 30.2)
- **throttle-body Ø** (default 38)
- **runner taper** (port↔TB diameter blend) + runner **length** + **bend angle**
- wall thickness (default 3.0)

## 3D generate (button)
- Tapered, bent runner tube (constant wall) — watertight
- Port flange = extruded rounded-rect Shape with port bore + 2 bolt holes (watertight)
- Throttle-body collar = extruded annulus (watertight)
- Injector boss = extruded annulus stub at chosen angle/position (watertight)
- Export: **binary STL** (and OBJ). Overlapping watertight solids → slicer unions them.

## Known phasing / assumptions
- Phase 1: overlapping watertight primitives (no CSG). Injector bore meets the
  runner wall but is not yet booleaned through to the lumen — flag for Phase 2 CSG.
- Bend is planar (in the runner plane) → no twist artifacts.
- Runner length & bend angle defaults are estimates until confirmed against the
  full assembly STEP.

## Tech
- Reuse the embedded **three.js r128** UMD global from the velocity-stack HTML
  (keeps everything offline). New file: `intake-manifold-modeler.html`.
- Integrate as a 2nd mode in the Android WebView app; then fix S25 top-crop.
