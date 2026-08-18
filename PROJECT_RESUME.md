# Clinic+ Modellers — Project Resume / Handoff

_Last updated: 2026-06-22. Single source of truth for picking this project up (e.g. in Claude Cowork)._

---

## 1. What this project is

An **offline Android app** (`com.velocitystack.modeller`) that wraps single-file HTML/WebGL
3D modelling tools. Built as a WebView app, sideloaded as a debug APK. Two threads of work:

1. **Velocity Stack modeller** (done, shipped) — axisymmetric trumpet/bellmouth, live 2D + 3D, STL export.
2. **Vario Bore tool** (in progress) — the real focus now: take the **Honda Vario 150 intake manifold** as a fixed base and let the user **modify the air-passage bores** (head port / output bore / input bore / TB port) live in 3D, then export a printable STL.

**End vision (user's words):** an app for 3D-print model generation from a base model, adjusting size live and fast.

---

## 2. Current status

| Item | State |
|---|---|
| Velocity Stack tool | ✅ working in app |
| Android build toolchain | ✅ working (`C:\vsbuild`) |
| APK builds & installs | ✅ `VarioBore-v0.3-debug.apk` on Desktop |
| WebViewAssetLoader (https origin for WASM/modules) | ✅ in MainActivity |
| Vario body = exact real STEP mesh | ✅ `vario_solid.stl` |
| Live bore editing (4 params) in 3D | ✅ |
| Printable boolean export (Manifold WASM, body − bore) | ✅ validated (watertight, ~43 cc, 15.6k tris) |
| **Bore centerline** | ❌ **WRONG — active bug.** Build used a straight vertical axis; the real bore is a strong curve. |

### 🔴 The active bug (next thing to fix)
The user gave a reference output STL:
`C:\Users\Clinic plus\Desktop\3dp file\mesh\intake\vario\intake vario 30-38 tb mx injector honda.stl`

The real air-passage **centerline is NOT straight** — it bows out to **x ≈ 20 mm at z ≈ 20** then returns
(peak ~42° off vertical). My bore stayed near x = 0 → **off by up to 20 mm** at the bend. User feedback:
_"ur build was off the centerline of the hole."_

So the earlier answer "straight vertical downdraft" was wrong in practice — **the bore must follow the real curved centerline.** Data extracted from the reference STL (smoothed, injector lobe eroded), embed these in the bore tool:

```js
// z (mm, head -7 → TB 54.5), bore-center x, bore-center y, original bore Ø
CL_Z=[-5.5,-4.0,-2.5,-1.0,0.5,2.0,3.5,5.0,6.5,8.0,9.5,11.0,12.5,14.0,15.5,17.0,18.5,20.0,21.5,23.0,24.5,26.0,27.5,29.0,30.5,32.0,33.5,35.0,36.5,38.0,39.5,41.0,42.5,44.0,45.5,47.0,48.5,50.0,51.5,53.0,54.5];
CL_X=[0.90,1.05,1.17,1.66,2.38,3.16,4.25,5.68,7.53,9.12,10.73,12.13,13.93,15.50,17.02,18.43,19.65,19.93,19.46,18.08,16.00,13.57,10.89,7.88,5.50,4.05,3.11,2.32,2.04,1.83,1.31,0.74,0.44,0.28,0.32,0.35,0.37,0.26,-0.08,-0.20,-0.40];
CL_Y=[-0.14,-0.14,-0.14,-0.16,-0.04,0.13,0.28,0.39,0.71,0.92,1.10,1.36,1.87,2.40,3.03,3.93,5.14,5.97,6.56,6.64,6.27,5.33,4.44,3.26,2.39,1.70,1.20,0.83,0.79,0.82,0.85,0.88,0.89,0.90,0.91,0.92,0.93,0.93,0.94,0.94,0.95];
ORIG_BORE_D=[30.0,29.9,29.8,29.7,29.7,29.6,29.6,29.6,29.5,29.4,29.4,29.4,29.4,29.5,29.6,29.7,29.8,30.0,30.2,30.3,30.6,30.8,31.0,31.3,31.6,31.9,32.2,32.6,33.0,33.4,33.8,34.2,34.7,35.1,35.6,36.1,36.7,37.2,37.8,38.4,39.0];
// path length ≈ 78.5 mm; x peak 19.9 @ z 20
```

### Next steps (in order)
1. **Replace the straight bore axis** in `intake-bore.html` / `intake-bore-dev.html` with the curved centerline above (`center(z)` → interpolate CL_X/CL_Y over CL_Z).
2. **Sweep the bore with parallel-transport frames** along the 3D polyline (a z-stacked-disk tube pinches on this ~42° curve). The 4 params (head/out/in/tb) set the bore Ø along arc-length.
3. **Curve-capable export:** build the export bore as a **union of `Manifold.hull(ring_i ∪ ring_{i+1})`** per segment (hull of two adjacent circle rings = a frustum, always manifold — avoids the winding failure a hand-built swept mesh hits with `Manifold.ofMesh`). `Manifold.hull` and batch `Manifold.union` are confirmed available in the loaded WASM. Then `body.subtract(bore)`, `decompose()`, keep largest.
4. Rebuild APK, user tests on S25.
5. Backlog: selectable **injector boss/joint** (user provides options); **cap bore to bolt-safe max** (bolt circle ~44 mm spacing, bore >~40 hits bolts); body/seam polish.

---

## 3. Files & layout

Project root: `C:\Users\Clinic plus\Desktop\CLAUDE PROJECT`

### App / assets (`android/app/src/main/assets/`)
- `menu.html` — landing menu (v0.3): Vario Bore, Velocity Stack, Intake Manifold (old).
- `intake-bore.html` — **APK Vario Bore tool** (full-screen portrait). ← edit this for the centerline fix.
- `intake-bore-dev.html` — same tool but framed as a Samsung S25 for desktop dev.
- `index.html` — Velocity Stack modeller (645 KB, inline Three.js).
- `intake-manifold-modeler.html` — OLD parametric manifold (superseded, kept in menu).
- `three.min.js` (603 KB) — extracted from the modeler's inline lib.
- `manifold.js` + `manifold.wasm` — `manifold-3d@3.5.1` (boolean engine for export).
- `vario_solid.stl` — **the body**: real Vario mesh with only the main bore filled → clean watertight solid (~92 cc, bbox ≈ real).
- `vario_flange.stl`, `vario_coupling.stl`, `reference_vario.stl` — earlier extractions (flange cap, coupling cap, full tessellated base). Not used by the current tool; safe to drop from APK to slim it.

### Self-contained / desktop copies (project root)
- `intake-bore-dev.html` — self-contained (inline three.js + base64 body STL) for double-click open; **export needs `manifold.js`+`manifold.wasm` next to it** (also copied to root).
- `vario_bore_GENERATED.stl` — a real generated output (proof the pipeline works).
- `reference_vario.stl` — full-res tessellated base.

### Source CAD
- `Component1.step` — earlier base.
- `STEP\VARIO 150\intake manifold honda vario 150 - injector honda joint yamaha - 30.2mm port - 38mm throttle body.step` — the Vario base STEP (tessellated to `reference_vario.stl`).
- **Reference OUTPUT** (what the user wants): `C:\Users\Clinic plus\Desktop\3dp file\mesh\intake\vario\intake vario 30-38 tb mx injector honda.stl`.

### Dev scripts (`dev/`)
- `regen_solid.py` — builds `vario_solid.stl` (radial fill, injector-junction band z∈[13,31] interpolated — don't remove that).
- `bore_proto.py` — offline boolean prototype (fill + cut along measured centerline).
- `render_assembly.py`, `assemble_bore_dev.py` (builds the self-contained html), `assemble_dev.py`.
- Renders: `assembly_preview.png`, `bore_in_body.png`, `printable_cutaway.png`, `generated_part.png`, `section_compare.png`.

---

## 4. Build the APK

Toolchain is in **`C:\vsbuild`** (NOT under the user profile — the space in `C:\Users\Clinic plus` breaks the Android SDK tools and Java's AF_UNIX socket pipe):
`android-sdk` (cmdline-tools + platform-tools + platforms;android-34 + build-tools;34.0.0), `gradle-8.7`, full Temurin **JDK 17** at `jdkdir\jdk-17.0.19+10`.

**Critical JVM workaround** (baked into `gradle.properties` and passed via `JDK_JAVA_OPTIONS`): `-Djdk.net.unixdomain.tmpdir=C:\t -Djava.io.tmpdir=C:\t`. Keep `C:\t` existing. The system Java is a JRE only (no `javac`) — must use the bundled JDK 17.

```bash
# from C:\vsbuild\android
export JAVA_HOME="C:\\vsbuild\\jdkdir\\jdk-17.0.19+10"
export ANDROID_HOME="C:\\vsbuild\\android-sdk"
export JDK_JAVA_OPTIONS="-Djdk.net.unixdomain.tmpdir=C:\\t -Djava.io.tmpdir=C:\\t"
export PATH="$JAVA_HOME/bin:$PATH"
./gradlew.bat assembleDebug --no-daemon
# APK → app/build/outputs/apk/debug/app-debug.apk
```
**Source of truth is the Desktop project**; copy changed files into `C:\vsbuild\android\...` before building (assets, MainActivity.java, build.gradle). `kotlin-stdlib` version clash from `androidx.webkit` is handled by the `resolutionStrategy { force ... }` block in `app/build.gradle`.

### Android specifics
- **MainActivity** serves assets over `https://appassets.androidplatform.net/assets/` via `androidx.webkit WebViewAssetLoader` (required — `file://` blocks the manifold ES module + WASM + fetch). Loads `menu.html` from there. Has display-cutout inset padding (S25 top-crop fix) and a `FileBridge` JS interface that saves exported STL/OBJ to **Downloads**.
- minSdk 24, targetSdk 34, compileSdk 34, versionName 0.3 / versionCode 3.

---

## 5. Dev preview (desktop)

Python 3.11 static server already configured in `.claude/launch.json` (serves the **assets dir** root on port 8765). Open short paths e.g. `/intake-bore.html`, `/intake-bore-dev.html`.
- WebGL pages: `preview_screenshot` times out — verify with `preview_eval` (read pixels / geometry) and render offline PNGs with matplotlib instead.

### Python geometry stack (Python 3.11 at `AppData\Local\Programs\Python\Python311`)
`pip install trimesh manifold3d rtree scipy shapely matplotlib gmsh`
- **gmsh** tessellates STEP → STL (has OpenCASCADE). **trimesh + manifold3d** do robust booleans. **shapely** for section polygons.

---

## 6. Vario 150 geometry reference (mm)

- Frame: head flange at **z = −7** (mounts to cylinder head), throttle-body face at **z = 54.5**. Downdraft (TB on top).
- Head flange (NON-NEGOTIABLE fit): two **Ø6.7 bolt holes** at (−2.6, 22.3) & (5.7, −22.3) + counterbores; bolt spacing ~45.4.
- Throttle-body end: **Ø47.9 ≈ 48 mm coupling OD (fixed, rubber coupling)**, ID ~37–38.
- Injector boss: tilted axis ≈ (0.56, 0, −0.83), **Ø9 injector hole**, **Ø6.2 joint bolt**. ("Honda joint / Yamaha injector" or "mx injector honda" variants.)
- Hole legend (user): 9 mm = injector; 6 mm ×3 = 2 flange bolts + 1 injector joint.
- Bore Ø tapers ~**30 @ head → 38.8 @ TB**; the **centerline curves** (see §2 data). Default params head 30 / out 31 / in 35 / tb 38.
- Base material volume ≈ 48 cc.
- Part is **3D printed** (made fresh) → bores can be larger OR smaller than original.

---

## 7. Design decisions (locked, with history)

- **Model = exact real Vario body (fixed) + parametric bore inside it.** Body is the real STEP shape so it bolts up; only the bore is editable. (User rejected: full parametric body; unmodified mesh; approximated tube body.)
- **Live editing is visual** (rebuild the bore mesh on each slider move — instant). The **boolean is only on Export** (~0.2–1 s). User wanted "fully live 3D" = the editing feedback is live.
- **Export = `body.subtract(bore)`** via Manifold WASM → `decompose()` → keep largest (drops a tiny coupling-groove artifact shell).
- Bezel note: `intake-bore-dev.html` has a desktop S25 phone-frame; `intake-bore.html` (APK) is full-screen — keep these in sync except the frame CSS.

---

## 8. Memory files (persisted)
`~/.claude/.../memory/`: `vario150-intake-geometry.md`, `android-build-toolchain.md`, `velocity-stack-design-system.md` (+ `MEMORY.md` index). These mirror §4 and §6 and are loaded automatically each session.
