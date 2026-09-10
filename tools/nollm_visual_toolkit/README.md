# Nollm Visual Toolkit 0.4.0

**Research workbench / important research infrastructure candidate.**  
[中文说明](README.zh-CN.md)

Offline, reproducible visualization for typed hex/X6 data plus a dedicated **Multiplicative Memory Field Lab**. The toolkit separates **arithmetic/native identity, observer coordinates, and rendering**. It is research infrastructure, not mathematical admission and not a production Nollm runtime change.

## Quick start

```sh
python -m pip install .

# Existing typed hex/X6 workbench
nollm-viz demo --out study.html --preview

# Complete static site: hex + X6 + multiplicative field observer
nollm-viz site --out preview-site --with-field --preview

# Standalone Multiplicative Memory Field Lab
nollm-viz field --out multiplicative.html --count 65536 --preview
```

The generated pages are self-contained and do not require a CDN, account, telemetry endpoint, or remote service. Local preview binds to `127.0.0.1` by default; non-loopback binding still requires explicit `--allow-remote`.

## 0.4.0: Multiplicative Memory Field Lab

The new field page implements a deliberately typed research observer for integers `0..N-1`.

### Arithmetic carrier retained before visualization

For every positive integer,

```text
n = product p^v_p(n)
A(n) = sum v_p(n) * h_seed(p)
```

where `h_seed(p)` is a deterministic unsigned 32-bit prime-phase code and `h_seed(2)=0`. `A(n)` is kept as an **unwrapped integer accumulator**, so serial multiplication satisfies the exact carrier law

```text
A(ab) = A(a) + A(b)
```

whenever the product is in the declared population. Zero remains a special absorbing state and is excluded from logarithmic identities. Prime valuations/identity are the carrier; the following polar coordinates are observers only.

### Multiplicative observer

For `n>0`, the page draws

```text
r(n) = n^alpha
theta(n) = frame_strength * (pi/4) * log2(n)
         + phase_strength * 2*pi*A(n)/2^32
```

The default `alpha=1/2` is the two-dimensional equal-area density candidate. The page also draws the 16 native-frame reference spokes at 22.5 degrees, preserving the distinction between the current Nollm frame schedule and the research prime-phase observer.

Interactive controls include:

- population size and deterministic prime-phase seed;
- radial exponent, frame strength, and prime-phase strength;
- `Frame only`, `Prime phase`, and `Hybrid` presets;
- prime/composite, residue class, `Omega(n)`, `v2(n)`, and prime-phase coloring;
- point lookup with exact factorization and integer phase accumulator;
- multiplication traces `n, mn, m^2 n, ...`;
- angular sector CV and equal-area radial CV diagnostics;
- angular CV normalized by the independent-uniform occupancy benchmark `sqrt((S-1)/B)`;
- PNG and configuration export.

A canvas point is only an observer location. Pixel overlap never merges arithmetic identities.

### Finite default diagnostic

For the verified 65,536-point default, with 64 angular sectors and blocks of 1024 consecutive positive integers:

- hybrid angular CV: `0.2344`;
- independent-uniform occupancy scale: `sqrt(63/1024)`;
- hybrid CV / iid scale: `0.945`;
- frame-only CV / iid scale: `27.696`;
- equal-area radial CV at `alpha=1/2`: `0.0001`.

These are finite observer diagnostics for the fixed implementation/seed, **not an asymptotic theorem or a proof of optimal uniformity**.

## Static research sites and preview

Existing 0.3.0 web generation remains available:

```sh
# Built-in hex + X6 pages
nollm-viz site --out preview-site

# Add the multiplicative observer
nollm-viz site --out preview-site --with-field

# Customize field population and seed
nollm-viz site --out preview-site --with-field --field-count 65536 --field-seed 814210

# Multiple user datasets plus the field observer
nollm-viz site run-a.json run-b.csv --out comparison-site --with-field --title "Experiment comparison"

# Preview any generated HTML/site
nollm-viz preview multiplicative.html
nollm-viz preview preview-site
```

The site landing page switches self-contained observer pages. It does not compose datasets or change identities. `manifest.json` remains `NOLLM_VISUAL_SITE_V1`; multiplicative pages are recorded as `kind="multiplicative-field-observer"` with a deterministic configuration fingerprint.

## Existing typed workbench

The existing observer contract is unchanged:

- native hex cells, rotatable A2 cube-plane observation, and explicit layer stacks;
- explicit six-component X6 input with six FCC carrier line families / twelve signed rays;
- slices, lookup, projection-collision audit, neighborhoods, integer-label multiplication trajectories;
- Q16 quotient/remainder, residue classes, prime/background and custom numeric layers;
- lossless documented JSON/CSV round trips, PNG/SVG observer exports, and dataset-bound view sessions.

Hex and X6 source coordinates are never inferred from one another. The A2 `(q,r,-q-r)` display plane is not six independent native dimensions. The X6-to-3D drawing convention remains an observer, not a completed global native/FCC bridge.

## CLI reference

```sh
nollm-viz validate data.json
nollm-viz render data.json --out study.html --preview
nollm-viz convert data.json --out data.csv
nollm-viz profile data.json --axis s --out slices.json
nollm-viz import-legacy interactive_65536.html --out recovered.json

nollm-viz field --out field.html --count 65536 --seed 814210 \
  --alpha 0.5 --frame-strength 1 --phase-strength 1 \
  --certificate carrier.json
```

The `--certificate` output is a bounded exact arithmetic-carrier check. It does not certify infinite-scale uniformity.

## Verification

0.4.0 local verification:

- 45 unit tests discovered: 44 passed; one optional Matplotlib test skipped because Matplotlib was unavailable;
- 7 multiplicative-field unit tests passed;
- 12 web/site tests passed, including multiplicative-page integration;
- 21 Chromium multiplicative-field acceptance checks passed on the full 65,536-point population with zero page errors and zero network requests;
- Python/browser prime-phase codes matched for selected primes;
- a 65,536-population finite exact carrier certificate checked 16,384 bounded products with zero accumulator-additivity failures;
- CLI `field` and `site --with-field` smoke passed;
- the 0.4.0 wheel built and contains `multiplicative.py`, `web.py`, and `workbench.html`.

The prior 0.2/0.3 typed workbench browser evidence is retained separately; it is not relabeled as a new full-front-end certification. Native iOS Safari, physical touchscreen behavior, repository-wide CI, live Nollm workloads, and production performance remain uncertified.

## BRC / claim boundary

BRC is **applied** to the multiplicative-field research surface:

- population: the declared finite integer interval;
- carrier: integer identity and sparse prime valuations, with exact integer prime-phase accumulator;
- serial composition: ordinary multiplication;
- observers: radius, angle, color, CV, pixel positions;
- information-loss guard: observer coordinates never replace the arithmetic carrier;
- status: finite executable research observer, not theorem promotion.

The deterministic phase hash is a research choice, not canonical number theory. Finite CV measurements are not asymptotic claims.

## Version boundary

- **0.2.0**: typed hex/X6 workbench and identity-preserving observer fixes.
- **0.3.0**: deterministic static-site generation and bounded localhost preview.
- **0.4.0**: exact arithmetic-carrier-backed Multiplicative Memory Field Lab, field/site CLI integration, and full-population browser acceptance for the new page.

License: MIT, inherited from Enterprise Math.
