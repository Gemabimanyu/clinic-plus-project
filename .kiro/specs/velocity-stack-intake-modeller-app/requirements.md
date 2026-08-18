# Requirements Document

## Introduction

A polished Android mobile app (Samsung Galaxy S25 primary target) serving as a combined
Velocity Stack and Intake Manifold 3D modeller. The app wraps two standalone HTML/WebGL
tools in an Android WebView. The Velocity Stack modeller is retained with light UX polish.
The Intake Manifold modeller is a full rebuild: the geometry is locked to the Honda Vario 150
STEP reference (runner shape, flange, injector boss, throttle-body coupling) but the user
may freely change the intake-port bore diameter and the throttle-body bore diameter, which
drives a live parametric model. Both tools export watertight binary STL files to the device
Downloads folder. A single standalone HTML file is also delivered for fast desktop/browser
testing before an APK is built.

## Glossary

- **App**: The Android application (`com.velocitystack.modeller`) containing the two modeller tools.
- **Menu**: The landing screen (`menu.html`) that presents navigation cards for each tool.
- **Velocity_Stack_Modeller**: The axisymmetric trumpet/bellmouth tool (`index.html`).
- **Intake_Manifold_Modeller**: The Honda Vario 150 single-runner intake manifold tool (`intake-manifold-modeler.html`).
- **WebView**: The Android `WebView` component that hosts the HTML modellers offline.
- **Three_JS**: The embedded Three.js r128 UMD library used for 3D rendering and geometry generation.
- **STL_Exporter**: The in-page JavaScript module that serialises Three.js geometry to binary STL format.
- **AndroidFile_Bridge**: The `@JavascriptInterface`-annotated Java class that receives base64 STL data from the WebView and writes it to device storage.
- **Reference_STEP**: The STEP file `intake manifold honda vario 150 - injector honda joint yamaha - 30.2mm port - 38mm throttle body.step` used as the dimensional ground truth for the manifold geometry.
- **Port_Bore**: The circular cross-section diameter (mm) at the engine head intake port; default 30.2 mm per the Reference_STEP.
- **TB_Bore**: The throttle-body bore diameter (mm) at the air-intake end; default 38 mm per the Reference_STEP.
- **Runner**: The tapered and bent tube connecting the port flange to the throttle-body coupling.
- **Port_Flange**: The bolt-on plate that mates the Runner to the engine head; geometry locked to the Vario 150 2-bolt pattern (Ø6.7 holes, 45.4 mm centre spacing).
- **TB_Coupling**: The throttle-body sleeve at the air-intake end of the Runner; outer diameter locked to Ø47.9 mm per the Reference_STEP.
- **Injector_Boss**: The fuel injector mounting stub on the Runner; geometry locked to the Honda + Yamaha joint profile (Ø19.8 body).
- **Ghost_Reference**: The semi-transparent STL mesh of the real Vario 150 manifold displayed alongside the parametric model for visual alignment.
- **Safe_Area**: The region of the phone screen not obscured by the status bar, navigation bar, or camera punch-hole cutout.
- **Dev_HTML**: A single standalone HTML file (`intake-manifold-v2.html`) that runs in a desktop browser and in the Android WebView for pre-APK testing.
- **CSG**: Constructive Solid Geometry — boolean subtraction of the injector bore through the runner lumen wall.
- **Panel**: The scrollable control area containing parameter sliders, dropdowns, and action buttons.
- **Stage**: The canvas area displaying 2D cross-section and 3D viewport.

---

## Requirements

### Requirement 1: App Navigation and Safe-Area Layout

**User Story:** As a user on a Samsung Galaxy S25, I want to open the app and navigate to either tool without any UI element being hidden behind the camera punch-hole or status bar, so that all controls and labels are fully visible and tappable.

#### Acceptance Criteria

1. WHEN the App launches, THE Menu SHALL display a navigation card for the Velocity_Stack_Modeller and a navigation card for the Intake_Manifold_Modeller within the Safe_Area.
2. WHEN the user taps a navigation card, THE WebView SHALL load the corresponding modeller HTML page.
3. WHEN the user presses the Android back button from any modeller page, THE WebView SHALL navigate back to the Menu.
4. THE App SHALL apply `env(safe-area-inset-top)` padding so that no header, label, or interactive control is obscured by the camera punch-hole or status bar on any device with API ≥ 28.
5. WHEN the device reports a display cutout via `WindowInsets.getDisplayCutout()`, THE MainActivity SHALL set the WebView top padding to the maximum of the system window inset top and the display-cutout safe inset top.
6. THE App SHALL set `layoutInDisplayCutoutMode` to `LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES` on API ≥ 28 so that full-screen hardware-accelerated rendering is available.

---

### Requirement 2: Offline Operation and WebGL Rendering

**User Story:** As a user without a network connection, I want both modeller tools to load and run fully offline, so that I can use the app in the workshop without Wi-Fi.

#### Acceptance Criteria

1. THE App SHALL embed all HTML, CSS, JavaScript (including Three_JS), and asset files inside the APK `assets/` directory.
2. WHEN the WebView loads a modeller page, THE WebView SHALL load it from `file:///android_asset/` with no network requests.
3. THE WebView SHALL enable hardware acceleration (`LAYER_TYPE_HARDWARE`) so that WebGL rendering via Three_JS operates at 60 fps on the Galaxy S25.
4. THE WebView SHALL enable JavaScript, DOM storage, and file access required for Three_JS geometry generation and STL export.
5. IF the WebGL context fails to initialise, THEN THE Intake_Manifold_Modeller SHALL display a plain-text error message within the Stage area stating that WebGL is unavailable.

---

### Requirement 3: STL Export to Device Storage

**User Story:** As a user, I want to export the generated 3D model as a binary STL file saved directly to my Downloads folder, so that I can open it in a slicer or send it to a 3D printer.

#### Acceptance Criteria

1. WHEN the user taps the Export STL button, THE STL_Exporter SHALL serialise the current Three_JS scene geometry to binary STL format.
2. WHEN the STL_Exporter has produced a binary STL byte array, THE Intake_Manifold_Modeller SHALL call `AndroidFile.save(filename, base64Data)` via the AndroidFile_Bridge.
3. WHEN running on Android API ≥ 29, THE AndroidFile_Bridge SHALL write the STL file to the MediaStore Downloads collection and clear the `IS_PENDING` flag upon completion.
4. WHEN running on Android API < 29, THE AndroidFile_Bridge SHALL write the STL file to the app-specific external downloads directory.
5. THE AndroidFile_Bridge SHALL return a string path or `"error: <message>"` to the caller; WHEN an error string is returned, THE Intake_Manifold_Modeller SHALL display the error text in the status note area.
6. THE STL_Exporter SHALL name the output file `intake-vario150-portXX.X-tbYY.Y.stl` where `XX.X` is the Port_Bore value and `YY.Y` is the TB_Bore value, each formatted to one decimal place.

---

### Requirement 4: Intake Manifold — Parametric Air Passage (Full Rebuild)

**User Story:** As a motorcycle engine builder, I want to modify the intake port bore and throttle-body bore diameters while all other manifold geometry stays locked to the Vario 150 reference, so that I can produce a custom air-passage manifold that fits the real engine without redesigning the mounting hardware.

#### Acceptance Criteria

1. THE Intake_Manifold_Modeller SHALL seed its default parameter values from the Reference_STEP: Port_Bore = 30.2 mm, TB_Bore = 38.0 mm.
2. WHEN the user adjusts the Port_Bore slider (range 16 mm – 46 mm, step 0.1 mm), THE Intake_Manifold_Modeller SHALL update the 2D cross-section canvas within 50 ms.
3. WHEN the user adjusts the TB_Bore slider (range 18 mm – 50 mm, step 0.1 mm), THE Intake_Manifold_Modeller SHALL update the 2D cross-section canvas within 50 ms.
4. THE Intake_Manifold_Modeller SHALL lock the following geometry to the Reference_STEP values and SHALL NOT expose them as user-adjustable sliders:
   - Runner length: 43 mm
   - Runner bend angle: 34°
   - Port_Flange bolt pattern: 2 × Ø6.7 holes at 45.4 mm centre spacing
   - Port_Flange spigot: Ø44 mm
   - TB_Coupling outer diameter: Ø47.9 mm
   - Injector_Boss profile: Honda + Yamaha joint body Ø19.8 mm
5. THE 2D cross-section canvas SHALL display: the runner air-passage outline using the current Port_Bore and TB_Bore values, the Port_Flange profile, the TB_Coupling profile, and the Injector_Boss stub outline — all to scale and labelled with current diameter values.
6. WHEN the user taps the Reset button, THE Intake_Manifold_Modeller SHALL restore Port_Bore to 30.2 mm and TB_Bore to 38.0 mm and SHALL redraw the 2D canvas.

---

### Requirement 5: Intake Manifold — 3D Generation and Ghost Reference

**User Story:** As a user, I want to generate a 3D model of the manifold and compare it against the real part reference mesh, so that I can visually verify the modified air passage fits within the correct outer envelope.

#### Acceptance Criteria

1. WHEN the user taps the Generate 3D button, THE Intake_Manifold_Modeller SHALL generate a Three_JS scene containing:
   - A tapered and bent Runner tube with constant wall thickness of 3.0 mm
   - A Port_Flange extruded shape with port bore and two bolt holes
   - A TB_Coupling extruded annulus
   - An Injector_Boss extruded annulus stub at the reference angle and position
2. WHEN the user taps the Generate 3D button, THE Intake_Manifold_Modeller SHALL complete geometry generation and first render within 3 seconds on the Galaxy S25.
3. THE Intake_Manifold_Modeller SHALL render a Ghost_Reference mesh loaded from `reference_vario.stl` at a default opacity of 28%.
4. WHEN the user adjusts the Ghost opacity slider (range 0% – 85%, step 1%), THE Intake_Manifold_Modeller SHALL update the Ghost_Reference mesh material opacity within one animation frame.
5. THE Intake_Manifold_Modeller SHALL provide rotation (X, Y, Z) and translation (X, Y, Z) sliders for the Ghost_Reference mesh so the user can manually align the reference to the generated model.
6. THE 3D canvas SHALL support single-finger drag to orbit the scene and two-finger pinch to zoom, using Three_JS OrbitControls touch events.
7. WHEN geometry has been generated, THE Intake_Manifold_Modeller SHALL display the approximate volume of the Runner lumen (cm³) in the status note area.

---

### Requirement 6: Intake Manifold — Phase 2 CSG (Boolean Injector Bore)

**User Story:** As a user preparing a manifold for 3D printing, I want the injector boss bore to be properly subtracted through the runner wall so the resulting STL has a true open lumen, making the printed part functional rather than having a blind stub.

#### Acceptance Criteria

1. WHEN the user taps Generate 3D, THE Intake_Manifold_Modeller SHALL perform a CSG boolean subtraction of the Injector_Boss bore (Ø9 mm pintle channel) through the Runner wall so that the injector lumen is fully open to the air passage.
2. WHEN CSG is complete, THE Intake_Manifold_Modeller SHALL produce a manifold mesh that is watertight (no open edges, no non-manifold faces) and suitable for direct slicing.
3. IF the CSG operation produces a non-watertight result, THEN THE Intake_Manifold_Modeller SHALL fall back to Phase 1 overlapping primitives and SHALL display a warning stating "CSG fallback: overlapping primitives used".
4. THE Intake_Manifold_Modeller SHALL compute CSG on the main thread using the embedded Three_JS geometry operations and SHALL NOT require a network connection or native plugin.

---

### Requirement 7: Mobile UI — Clean Functional Layout (Samsung Galaxy S25)

**User Story:** As a user on a Samsung Galaxy S25 in portrait orientation, I want a clean, functional UI that gives maximum space to the 3D/2D viewport while keeping all controls reachable with one hand, so that the app feels polished and efficient.

#### Acceptance Criteria

1. THE Intake_Manifold_Modeller SHALL use a two-region portrait layout: the Stage occupying the upper 54% of the Safe_Area height and the Panel occupying the lower 46%, matching the existing dev layout.
2. THE Panel SHALL be vertically scrollable when its content exceeds the allocated height, with `overflow-y: auto` and `-webkit-overflow-scrolling: touch`.
3. THE App SHALL use the dark colour scheme (`--bg: #0b0f14`, `--panel: #121922`, `--accent: #22d3ee`) with no light-theme toggle.
4. ALL interactive controls (sliders, buttons, select dropdowns) SHALL have a minimum touch target height of 44 px to comply with touch accessibility guidelines.
5. THE Panel action buttons (Generate 3D, Export STL, Reset) SHALL be visually distinct: Generate 3D uses the accent gradient fill, Export STL uses a bordered secondary style, and Reset uses a tertiary flat style.
6. THE Intake_Manifold_Modeller SHALL use the system sans-serif font stack (`-apple-system, Segoe UI, Roboto, system-ui, sans-serif`) at a base size of 14 px for labels and 16 px for section headings.
7. THE App SHALL suppress the browser zoom gesture (`user-scalable=no, maximum-scale=1`) in the viewport meta tag so pinch events are exclusively consumed by Three_JS OrbitControls.
8. WHEN the Panel is scrolled to the bottom, THE action buttons SHALL remain visible via a sticky container with a gradient fade above them so the buttons are always reachable without scrolling.

---

### Requirement 8: Velocity Stack Modeller — Light UX Polish

**User Story:** As a user, I want the Velocity Stack modeller to have the same clean look and feel as the rebuilt Intake Manifold modeller so the app feels consistent, without changing any of the existing modelling or export functionality.

#### Acceptance Criteria

1. THE Velocity_Stack_Modeller SHALL retain all existing live 2D preview, live 3D preview, and binary STL export functionality without modification to the geometry or export logic.
2. THE Velocity_Stack_Modeller SHALL apply the same dark colour scheme (`--bg: #0b0f14`, `--accent: #22d3ee`) and font stack as the Intake_Manifold_Modeller.
3. THE Velocity_Stack_Modeller SHALL use the same minimum 44 px touch target height for all sliders and buttons.
4. THE Velocity_Stack_Modeller SHALL apply `env(safe-area-inset-top)` padding in its header so no content is hidden behind the camera punch-hole on the S25.
5. WHEN the user taps Export STL in the Velocity_Stack_Modeller, THE AndroidFile_Bridge SHALL save the file to the device Downloads folder using the same mechanism as the Intake_Manifold_Modeller.

---

### Requirement 9: Standalone Dev HTML for Pre-APK Testing

**User Story:** As a developer, I want a single standalone HTML file that I can open in a desktop browser (Chrome/Edge) to test the full Intake Manifold modeller UI and geometry before building the APK, so that the iteration cycle is fast.

#### Acceptance Criteria

1. THE Dev_HTML SHALL be a single self-contained HTML file with all CSS, JavaScript, and Three_JS r128 inline — no external network dependencies.
2. WHEN opened in a desktop Chromium browser, THE Dev_HTML SHALL render the full Intake_Manifold_Modeller UI including 2D canvas, 3D canvas, all sliders, Ghost_Reference controls, and action buttons.
3. THE Dev_HTML SHALL detect the absence of the `AndroidFile` global and, WHEN Export STL is triggered in that environment, SHALL trigger a browser `<a download>` link instead of calling the AndroidFile_Bridge.
4. THE Dev_HTML SHALL visually simulate the Samsung Galaxy S25 portrait viewport (360 × 780 px content area) when displayed on a desktop screen wider than 760 px, by centering a phone-frame `<div>` of those dimensions with rounded corners and a camera punch-hole.
5. WHEN the Dev_HTML is loaded inside the Android WebView, THE Dev_HTML SHALL behave identically to the production `intake-manifold-modeler.html` with no desktop-simulation styles applied.
6. THE Dev_HTML SHALL be the primary deliverable for the initial development phase; the production APK asset SHALL be created from this HTML once testing is complete.
