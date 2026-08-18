# Intake Manifold & Velocity Stack Generator — Learning Resume

_Created 2026-08-01. **Read this first** in the new chat, before looking at anything else._

> **What this session is for:** Gema sends a batch of his own designs. I measure them,
> extract *his* design rules (not textbook rules), turn those into a parametric template +
> algorithm, and package it as a **skill** so every future generated part comes out looking
> and printing like something he made.
>
> **This is a learning session first, a coding session second.** Do not start writing the
> generator until §4's rule table has real numbers in it from real parts. Guessing geometry
> is exactly what got this parked twice before.

---

## 1. Why this is being redone

The parametric generator has been attempted before and **parked twice on purpose** — both
times because the output wasn't trustworthy enough to actually print. The reason was always
the same: the geometry was invented, then checked against one reference part after the fact.

This session inverts that. **Measure many real parts first → derive the rules → then build.**
Gema's designs are the ground truth. The generator's job is to reproduce his judgement, not
to be a generic CAD tool.

### The one hard rule

> A generated part is only acceptable if it would bolt onto the real engine and print on the
> real printer. **Fit surfaces are measured, never interpolated.** Bolt patterns, port bores,
> flange thicknesses and coupling ODs come from the source file — the generator may only
> parameterize the *air path between* those fixed surfaces.

This is already the locked design decision for the Vario 150 (see §3) — "fixed real ends +
parametric bore between them". Expect the same shape of answer for every new model, and
confirm it with Gema rather than assuming.

---

## 2. What to ask Gema at the start

Ask these before measuring anything — they change what's worth extracting:

1. **How many designs, and what are they?** (manifolds only? stacks too? which bikes?)
2. **Which ones are proven** — actually printed, fitted, and running — vs. drafts? Only
   proven parts should set the rules; drafts can be sanity checks.
3. **What varies between them on purpose** (a bigger TB, a different injector, a taller
   stack) vs. what he considers fixed shop practice (wall thickness, fillet style, bolt-boss
   size)?
4. **What has failed** — cracked, leaked, wouldn't fit, printed badly, needed rework. Failure
   cases pin down the *limits* of the rules better than the successes do.
5. **What printer/material/nozzle** these are made for, and which settings are non-negotiable.
6. **What should the generator ask the user for**, in his words? That list becomes the skill's
   input parameters; everything else the algorithm decides.

Do not skip #4. A rule with no known failure boundary is a guess with good manners.

---

## 3. What already exists (don't rebuild this)

### Reference geometry — Honda Vario 150
- `STEP/VARIO 150/` — five STEP files: the full manifold, the head flange (2-bolt), the
  throttle-body bore + rubber OD, and two injector joints (Honda+Yamaha, Yamaha).
- `docs/INTAKE-SPEC.md` — the measured dimension sheet from that kit. Accurate; reuse it.
- `reference_vario.stl`, `vario_bore_GENERATED.stl` — tessellated reference + a prior attempt.
- Memory file `[[vario150-intake-geometry]]` — **the single most valuable prior artifact.**
  Has the corrected feature extraction (holes are *not* all at Y≈0), the real 34° runner bend,
  the ~43 mm centerline length, the measured bore taper (30.1 mm @ head → 38.8 mm @ TB), the
  ~4 mm minimum wall, and the locked "fixed ends + parametric bore" decision. **Read it in
  full before measuring anything new** — several of its notes correct earlier wrong ones, so
  take the latest statement on each point.

### Working tools on this machine (all verified importable)
- **gmsh** — reads STEP via OpenCASCADE, writes STL. This is how STEP becomes measurable.
- **trimesh** — sectioning, centroid paths, volume, watertightness checks.
- **manifold3d** (Python) / **manifold.js + manifold.wasm** (browser) — real CSG booleans.
  The browser pair lives in `android/app/src/main/assets/` and is proven working there.
- Python 3.11 at `%LOCALAPPDATA%\Programs\Python\Python311`.
- Known trap, already solved: a hand-built tube mesh fails Manifold's `ofMesh` on winding —
  build bores from `Manifold.cylinder` primitives unioned per segment instead.

### Existing generators
- `c+ app v0.1/generate_vs.py` — old Python velocity-stack generator. Superseded by the HTML
  modeler for that part type; keep only as a reference for the revolve math.
- `cplus_mobile/assets/modeler/velocity-stack-modeler.html` — **the shipped, working velocity
  stack modeler.** Profile math, watertight revolve, STL/OBJ export, Clinic+ theme, presets,
  Revolve-segments slider. Any stack work should extend this, not restart it.
- `cplus_mobile/lib/stl_library.dart` — the same profile math in Dart (`_innerRadius`,
  `estimateFilament`, `generateStlAscii`) plus the filament/time estimator. **If the profile
  algorithm changes, these two must stay in sync** — the app estimates filament with the Dart
  copy and prints from the HTML copy.
- `intake-manifold-dev.html`, `intake-bore-dev.html`, `dev/` — prior intake experiments,
  including `dev/regen_solid.py` (radial bore fill with the injector-junction band
  interpolated — that interpolation is deliberate, don't "fix" it).
- `profile_extract*.py`, `vol_check*.py`, `vol_debug*.py` — throwaway measurement scripts from
  the earlier sessions. Mine them for technique, don't trust their numbers.

---

## 4. The extraction schema — fill this in for EVERY design

The whole point is comparability: the same measurements pulled from every part, so patterns
show up as ratios instead of anecdotes. Record into `designs/<part-name>.json` and keep a
combined table in `designs/MEASURED.md`.

### 4.1 Identity
| Field | Meaning |
|---|---|
| `name`, `bike`, `engine_cc` | what it's for |
| `part_type` | `manifold` \| `velocity_stack` \| `coupling` \| `other` |
| `status` | `proven` (printed + fitted + running) \| `printed` \| `draft` |
| `source_file` | STEP/STL path |
| `notes` | Gema's own words about the part — keep verbatim, don't paraphrase |

### 4.2 Fit surfaces (measured, never invented)
- **Head flange**: port bore Ø, spigot Ø, plate thickness, bolt count, bolt hole Ø,
  counterbore Ø + depth, bolt centers (x,y), plate outline extents.
- **Throttle-body end**: bore Ø, step Ø, coupling OD, chamfer angle, groove positions.
- **Injector boss** (if present): bore Ø, boss OD, axis vector, position along the runner,
  o-ring groove torus dims, joint bolt Ø + position.
- **Stack base** (velocity stacks): base bore Ø, base height, flange present y/n + its dims.

### 4.3 The air path (this is where his design language lives)
- **Centerline**: sampled points from flange face to TB face. Straight or curved? Total bend
  angle. Chord length vs. arc length. Which way it bows and by how much.
- **Bore taper**: equivalent diameter at ≥10 stations along the centerline. Linear? A
  smoothstep? Does it neck down before opening out?
- **Area ratio**: outlet area ÷ inlet area, and where along the length the area changes fastest.
- **Bellmouth** (stacks): radius, flare ratio, what fraction of total height the bell occupies,
  radiused vs. elliptical.
- **Wall thickness**: min, max, and where each occurs. Constant-wall or thickened at bends?

### 4.4 Printability
- Overall bbox, print orientation implied by the flat face, overhang angles over 45°, whether
  supports would be needed and where, part volume (cc) and mass in his usual material.

### 4.5 The comparison table (the actual deliverable of the measuring phase)
One row per part, columns as **ratios not absolutes** — ratios are what transfer to a new bike:

`port_Ø/TB_Ø` · `length/port_Ø` · `bend°` · `wall/port_Ø` · `outlet_area/inlet_area` ·
`bell_r/throat_Ø` · `bell_height/total_height` · `flange_thickness/port_Ø` · `bolt_spacing/port_Ø`

**Then look for what does NOT vary.** The constants across his parts *are* his design
method — those become the algorithm's hard-coded rules. The things that vary are the
generator's input parameters. That single distinction is the whole extraction.

---

## 5. From measurements to an algorithm

Only start this once §4.5 has ≥3 proven parts in it (fewer than 3 and a "rule" is just a
coincidence with confidence). Ask Gema before proceeding on fewer.

1. **Classify each dimension** as `fixed` (same across all parts), `derived` (a stable ratio
   of another dimension), or `input` (genuinely varies by application).
2. **Write each derived rule with its observed range and tolerance**, e.g.
   "wall = 0.13 × port_Ø, observed 3.0–4.2 mm, never below 3.0 (thinner cracked — see §2.4
   failure notes)". A rule without a floor/ceiling is not finished.
3. **Confirm every rule with Gema in plain language** before it goes in the code. He will know
   which are real intent and which are accidents of one particular part. Expect some of the
   tidiest-looking correlations to be coincidence — ask, don't assume.
4. **Validate**: regenerate an existing proven part from its inputs alone, and diff against the
   real mesh (Hausdorff distance / section overlay). If the generator can't reproduce a part
   he already made, the rules are wrong. This is the acceptance test, and it must pass before
   anything gets packaged.

---

## 6. The skill to produce

Package as `.claude/skills/intake-generator/` (name TBC with Gema):

```
SKILL.md               when to trigger, the input parameters, the workflow
references/
  design-rules.md      the §5 rule table — fixed / derived / input, with ranges
  measured-parts.md    the §4.5 comparison table, the evidence behind every rule
  fit-surfaces.md      per-bike measured flange/TB/injector data (the non-negotiables)
scripts/
  measure_step.py      STEP → measurements JSON (gmsh + trimesh)
  generate.py          parameters → watertight STL (manifold3d)
  validate.py          generated vs. reference diff — the §5.4 acceptance test
```

Skill triggers on: "generate an intake manifold for X", "make a velocity stack for Y",
"design a manifold for a <bike>" — including when the bike isn't one that's been measured.

**The skill must refuse to invent a fit surface.** For an unmeasured bike it asks for the
STEP/measurements of the head flange and TB end, or generates only the air path and says
plainly which surfaces are unverified. Silently guessing a bolt pattern produces a part that
looks right and doesn't fit — the worst possible failure for a shop that prints these to sell.

---

## 7. Session protocol

1. Read this file, then the `[[vario150-intake-geometry]]` memory, then `docs/INTAKE-SPEC.md`.
2. Ask §2's questions. Get the batch of designs.
3. Measure every part into `designs/<name>.json` — **one script, run per file, same schema.**
   Report each part's numbers back to Gema as you go; he'll catch a bad measurement instantly
   in a way no automated check will.
4. Build `designs/MEASURED.md` (§4.5). Show him the ratio table and the "what doesn't vary"
   finding. **This is the checkpoint** — the design language is either visible here or the
   sample isn't big enough yet.
5. Agree the rule table (§5). Write it down as prose he can correct, before any code.
6. Build `generate.py`, validate against a proven part (§5.4), iterate until the diff passes.
7. Package the skill (§6). Wire it into the Clinic+ app only after it stands alone.

Keep each phase's output on disk. If the session runs long, the next one resumes from the
files, not from chat history.

---

## 8. Context worth carrying in

- Clinic+ (the shop app) is complete and healthy — see `c+ app v0.1/resume.md`. It is **not**
  a dependency of this work; build the generator standalone and integrate later. The natural
  integration point is the existing STL Library module (a generated part becomes a record with
  its filament estimate already computed).
- The shop prints these for real customers at real prices (velocity stack Rp 100k, intake
  manifold Rp 300k), so generated output is production, not a demo.
- Two things Gema has explicitly parked, in his own decisions: **a customer-facing app**, and
  **guessing this generator's geometry without validating against the STEP master**. The second
  one is precisely what this session exists to do properly — with the measurements in hand,
  it's no longer parked.
- **iOS is a hard blocker** on this machine (no macOS/Xcode). Don't propose it.
- Screenshots of WebGL pages time out in the preview pane — verify geometry by evaluating JS
  and reading values back, and render checks offline with matplotlib.
