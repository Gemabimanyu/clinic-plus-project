# Intake/Velocity-Stack Generator → Clinic+ App — Build Resume

_Created 2026-08-01. **Read this first** in the new chat._

> **What this session is for:** turn the measured, confirmed design rules from the learning
> session into (1) a `.claude/skills/` skill, and (2) a real generator feature wired into the
> Clinic+ Flutter app (`c+ app v0.1/cplus_mobile/`), alongside the existing velocity-stack
> modeler and STL Library.

---

## 1. What's already done — don't re-measure

A full learning pass ran across **52 proven, printed, fitted, running parts** (no failures,
no drafts — see `designs/design-rules.md` §status). The rule table is **locked and confirmed
with Gema in plain language**, part by part, as each number came out of the geometry. Do not
re-derive these; read them.

**Read in this order:**
1. `designs/design-rules.md` — the final fixed/input/derived rule table. This is the thing
   the skill and the generator both consume.
2. `designs/FIT-SURFACES.md` — per-bike flange bolt pattern detail (count, diameter, bolt-circle
   radius) behind the rule table.
3. `designs/MEASURED.md` — the full 52-part comparison table (filename-sourced dimensions +
   geometry fallback).
4. `GENERATOR-RESUME.md` — the original learning-session brief (§4 extraction schema, §6 skill
   layout target, §7 protocol). Rule table is done; pick up from its §5.4/§6.

## 2. The locked rules (summary — full detail in design-rules.md)

**Intake manifold, fixed per bike:**
| bike | bolts | bolt Ø | bolt-circle r | sample size |
|---|---|---|---|---|
| Aerox | 2 | 6.60mm | 27.09mm | 9 parts |
| Vario | 2 | 6.55mm | 23.77mm | 14 parts |
| Vespa | 3 | 6.50mm | 29.14mm | 3 parts — **below the ≥3 comfort margin, treat as provisional** |
| Xmax | 2 | 6.99mm | 34.08mm | 3 parts — **provisional**, + confirmed alignment-pin relief hole |

- Flange plate thickness: 10 or 12mm (Gema's call per job).
- Intake tube wall: **6.7mm** (median, confirmed by Gema).
- Velocity stack tube wall: **3.0mm** (median, confirmed by Gema).
- **Every velocity stack base gets an M5 threaded clamp-bolt mount — always**, not derived,
  not optional. This is the one rule most likely to get silently dropped if someone re-derives
  from geometry instead of reading this doc — it doesn't show up in any measurement, it's a
  direct standing instruction from Gema.
- Velocity stacks have **no fixed flange** — most fit a custom TB, not OEM. Unlike intake
  manifolds, there's no "must match motorcycle X" rule for this part type.
- Bore taper: intake mostly-linear (median R²=0.79), velocity-stack bells more curved (median
  R²=0.52) — curve family (smoothstep/elliptical/tangent-arc) still unconfirmed, flag as
  unverified wherever the generator uses it.

**The one hard rule (from GENERATOR-RESUME.md, still binding):** fit surfaces are measured,
never interpolated. A bike not in the table above (only Aerox/Vario/Vespa/Xmax have bolt-pattern
data right now) needs new STEP/STL input before a flange can be generated for it — the skill
must refuse to invent one.

## 3. Status — build done, app wiring is not

**Done, this session (2026-08-01f):**

1. **`designs/generate.py`** — built. `manifold3d`-based, both part types
   (`build_manifold`, `build_stack`). Applies the fixed rules from
   `design-rules.md`.
2. **Real bug found and fixed along the way**: `FIT-SURFACES.md`/`bolt_patterns.json` only
   ever recorded bolt-hole *radius* from the bore centre, not position — not enough to build
   a flange (two bolts at the same radius could be anywhere around the circle). Re-extracted
   as `designs/bolt_positions.json` via a new `bolt_positions.py`, which found **bolt-pair
   spacing measures near-exact per bike** (sd 0.00–0.82mm) while radius varies, because
   several Vario "raised port" parts deliberately offset the bore off the bolt axis by
   8–11mm. The generator builds the flange around the **bolt pair as the datum**, not the
   bore — this also matches how the part actually bolts on. Full writeup in
   `design-rules.md`'s new "Build-session correction" section.
3. **Validated** against `v150 28x34 barrel jaski.stl` (a clean, boss-free proven Vario
   part): watertight ✓, bolt spacing reproduced off the generated mesh to 0.00mm ✓, volume
   within 10.9% (tolerance 20% — the flange plate is a hull approximation of the real
   irregular outline, expected), surface-distance median 1.5mm. **Gate passed** —
   `designs/validate.py` is the reusable check. Velocity-stack profile math was cross-checked
   bit-identical (max diff 0.0mm) against the shipped Dart/HTML formula instead of a raw mesh
   diff, since the M5 clamp tab breaks naive axisymmetric section-scanning on real stack
   scans — documented in `design-rules.md`.
4. **Real length-semantics bug found and fixed**: first pass fed `--length` as
   centerline-only and then added the flange+collar on top of it, roughly doubling generated
   volume. `MEASURED.md`'s `length_mm(geo)` is actually the **total** part bbox length. Fixed
   in `generate.py` and documented loudly in both the script's docstring and
   `design-rules.md`, since it's the trap most likely to bite a future re-read of this code.
5. **Packaged as a skill**: `~/.claude/skills/clinic-plus-generator/` (user-level, not
   project-level — matches where `velocity-stack-ios-design` already lives).
   `SKILL.md` + `references/{design-rules,fit-surfaces}.md` +
   `references/bolt-positions.json` + `scripts/{generate,validate}.py`. Registered and
   showing up in the skill list already. Refuses unmeasured bikes (tested in `--demo`).

**Done, follow-up session (2026-08-01g) — app wiring, backend-endpoint approach chosen by
the user:**

6. **Backend**: `c+ app v0.1/c+ app v0.1/manifold_generator.py` — third synced copy of
   `generate.py` (see its own header; must move with `designs/generate.py` and the skill's
   copy). `sync_api.py` gained five endpoints under `/sync/generate/*`:
   `GET bikes` (the measured fit-surface table, so Dart never hardcodes bike data),
   `POST manifold`, `POST stack` (both return `{id, meta, stats}`, reject with 400 for a bad
   parameter / unmeasured bike, 422 if somehow not watertight), `GET <id>/stl` (downloads the
   file — same two-step shape as the existing invoice-PDF endpoint). Generated files land in
   a new `generated/` folder, pruned on each request past 24h old — no queue, no schedule.
   **Real trap found while wiring this**: watertight checks on a *re-opened* .stl file can
   read `False` even for a genuinely watertight part — STL as a format has no shared
   vertices, so a naive exact-match merge fails after float32 export rounding. The
   authoritative check is the in-memory one `save_stl()` already does before export; noted
   in `generate.py`'s docstring so it isn't mistaken for a bug later.
7. **Mobile**: `lib/generator_service.dart` (calls the backend, reusing `SyncService`'s
   `serverIp`/`apiKey`/`port`), `lib/pages/generator_page.dart` (bike/type picker, params
   form, generate → result card with watertight/volume/warnings/unverified → "Save to STL
   Library"). Entry points added to `stl_library_page.dart` (desktop header button + mobile
   list button) alongside the existing "New STL record" flow.
8. **Schema change (v12 → v13)**: `parts.stl_path TEXT DEFAULT ''`. Necessary because a
   manifold's real geometry (bent tube + flange + bolt pattern) has no revolve-formula
   equivalent in Dart the way a velocity stack's does — `stl_library.dart`'s
   `generateStlAscii` can only ever regenerate a stack. A generated record's actual STL is
   copied out of the temp download into `ApplicationSupportDirectory/generated_parts/` and
   the row points at it; `_exportStl`/`_export` in `stl_library_page.dart` now check
   `stl_path` first and only fall back to `generateStlAscii` when it's empty (hand-entered
   stack records, unchanged). The preview sheet shows a plain marker instead of the
   revolve-profile wireframe for a stored-mesh record, since drawing that wireframe from a
   manifold's dimensions would be actively misleading, not just absent.
9. **Filament estimate refactor, no behavior change**: `StlLibrary.estimateFilament` now
   integrates a volume and calls a new `StlLibrary.filamentFromVolume(volumeCc, material)`
   for the grams/support/hours conversion, instead of having that math inline. The generator
   page uses `filamentFromVolume` directly with the backend's own reported `volume_cc` —
   this keeps the grams=volume×density / support=16% / hours=grams÷26 convention in exactly
   one place rather than adding a second copy for the new caller.
10. **Explicit tradeoff, stated once here**: the generator is the one Clinic+ feature that
    needs the desktop backend reachable over WiFi. Every other feature (Orders, Finance, the
    velocity-stack modeler) was deliberately built to work fully offline — this is a real,
    known departure from that principle, made because the user chose the backend-endpoint
    approach explicitly. `GeneratorPage` shows a clear "could not reach the desktop backend"
    banner rather than failing silently or pretending to work offline.

**Verified**: backend endpoints tested live via curl — bikes list, manifold generation
(round and oval TB), stack generation, unmeasured-bike rejection (400), missing-API-key
rejection (401), full download round-trip. `flutter analyze` 0 errors/0 warnings (11
pre-existing lint infos). `flutter test` **53/53** (added `filamentFromVolume` tests and a
`parts.stl_path` round-trip test). `flutter build windows --debug` launches and survives the
v12→v13 migration on the real database.

**Not done / explicitly out of scope this session:**
- No GUI click-through of the actual Generate-part flow inside the running app (backend
  behavior, schema migration, and Dart logic are all independently verified; wiring them
  together in a live UI session wasn't done — worth a manual pass before relying on it for a
  real job).
- The desktop backend is not auto-started by the app; the shop still runs
  `python sync_api.py` manually as before. No change to that.
- CPU/time cost of a manifold generation over WiFi on a slow network isn't measured — the
  backend call has a 30s timeout on both the generate and the download leg; if that's too
  tight for a phone on a weak signal, raise it in `generator_service.dart`.

## 4. Existing app code this plugs into — read before touching

- `c+ app v0.1/cplus_mobile/` — the Flutter app root. This is the real one; ignore the stray
  top-level `cplus_mobile_v1.apk` next to it (build artifact, not source).
- `c+ app v0.1/cplus_mobile/assets/modeler/velocity-stack-modeler.html` — the shipped, working
  velocity-stack modeler (profile math, watertight revolve, STL/OBJ export, Clinic+ theme,
  presets). **The velocity-stack rules from §2 (3.0mm wall, M5 mount) should extend this
  modeler, not replace it** — check whether it already exposes a wall-thickness parameter and
  an M5-boss toggle before assuming either needs adding.
- `c+ app v0.1/cplus_mobile/lib/stl_library.dart` — Dart port of the same profile math
  (`_innerRadius`, `estimateFilament`, `generateStlAscii`) plus the filament/time estimator.
  **If the profile algorithm changes, this and the HTML modeler must stay in sync** — the app
  estimates filament with the Dart copy, prints from the HTML copy. Don't edit one without the
  other.
- `c+ app v0.1/resume.md` — Clinic+ app status doc. App is complete and healthy; this generator
  work is additive, not a rewrite.
- Ignore `build/` subfolders under `cplus_mobile/` — those are compiled output copies of the
  same modeler HTML, not sources.

## 5. Session protocol

1. Read this file, then `designs/design-rules.md`, then `c+ app v0.1/resume.md` for current
   app state.
2. Write `designs/generate.py`, validate against a proven Vario part (§3.2) — this gate must
   pass before moving on.
3. Package the skill (§3.3).
4. Wire into `stl_library.dart` / the modeler HTML per §4, keeping both profile-math copies in
   sync.
5. Test in the actual app (build + run), not just script output — a part that validates in
   isolation but doesn't show up right in the STL Library isn't done.
