# Migration 17 — actual Phase32 Python caller on certified uint32 cells

Status: locally validated opt-in caller candidate; default/browser/CLI cutover not changed.
Baseline: `86111435b173464c91c000275077b74411fe93db` (M16).
Researcher: EM-DIRECT-4A5102 / TASK_RESEARCH.

## Actual caller change

The real `phase32_lab.py` keeps its historical float observer unchanged unless an
explicit exact pitch is supplied. `build(..., cell_pitch=(n,d))` now routes the
existing uint32 phase population into M16's exact `2**32` certified-cell carrier.
The legacy `config.pitch` remains display-only and is never reverse-inferred as
an exact source. Literal numerator/denominator pairs remain unreduced.

Phase32 declares nearest Euclidean A2 center followed by axial `(q,r)`
lexicographic ties. That is not the earlier q/r/s-error-priority rule of the base
certifier. M17 reuses the already tested M06 multiplicative lexicographic tie
adapter for true `CERTIFIED_TIE` records while retaining each complete base
certificate and its original tie rule. No tie mathematics is reimplemented.

Exact models persist `cell_pitch_source`, the original `cell_precision` budget
and the complete certified population. The certifier receives the reciprocal
layout scale required by the old pitch convention, so exact pitch `n/d` means
what legacy `quantize(..., pitch=n/d)` meant without deriving it from a float.

## Exact metrics, products and V2 export

`metrics()` branches only when the model carries the certified engine. Sector and
annulus bins use the existing BRC-backed integer floor transport. Approximate CV
roots are omitted; ordered counts feed the existing `AngularDispersion` CV²
integer ratio and residual readout. A custom exact readout scale is supported;
nondefault readout options on legacy models fail rather than silently doing
nothing.

Exact `multiplication()` retains integer product, uint32 phase defect and integer
Omega defect without calling `position`, `quantize`, complex arithmetic or display
pitch. Both approximate error fields are null, including zero multiplication;
omitted is not a measured zero. The spiral control remains nonclosed and retains
its nonzero phase defect.

Exact `hex_data()` uses certified integer cells, preserves every identity and
omits `ideal_x/ideal_y`. Its metadata stores an exact phase-source packet,
`cell_pitch_source`, precision budget and certificate summary, not the legacy
float camera/pitch configuration. If any cell is unresolved, complete V2 export
fails instead of guessing a coordinate. This is still a declared A2 observer,
not native X6/P000.

## Boundary witnesses

For `n=3`, quarter-turn phase and exact pitch 2, the old floating path selects
`(0,1)` while the declared lexicographic exact tie is `(-1,1)`. For `n=4` with a
quarter-turn source, the base certifier selects `(0,1)` under its own q/r/s rule;
M17 retains that base certificate but names `(-1,1)` for this caller's documented
lexicographic rule. These are equal-nearest boundary choices, not interior-distance
defects.

A deliberately low 8-bit budget leaves most nontrivial identities unresolved.
Exact metrics keep complete occupancy/collision/load totals null and retain the
unresolved identity list; `hex_data` refuses full-coordinate export. No float
fallback is used.

## Validation

M16's 154-test gate is retained. The original Phase32 suite contributes 17 tests;
15 numerical/API tests pass and two HTML/site tests are explicitly skipped only
because the M16 source-slice does not carry unchanged `phase32_lab.html`. Twelve
new exact-caller tests pass. Total recorded gate: 183 tests, zero failures/errors,
with exactly two source-slice package-data skips and no numerical skips.

The new tests poison Phase32 sqrt/sin/cos, `position` and `quantize` while exact
construction/readouts execute; check unreduced pitch provenance, CV² reconstruction,
spiral nonclosure, zero typing, pixel-free V2 data, low-budget unresolved behavior,
legacy full-object equality, float-boundary witnesses and base/local tie separation.

Finite actual Phase32 comparisons cover golden/hash/spiral at count 4096 and exact
pitches 1/2, 1 and 3/2. All nine populations are `CERTIFIED_ALL`; aggregate
occupancy/collision/max-load and every identity cell match the legacy floating
observer in those cases. A full 65536-identity golden/pitch-one case is also fully
certified at the initial 64-bit budget: occupied cells 47,497, collision excess
18,038, maximum multiplicity 9, zero unresolved and zero identity-cell differences.
These are finite regressions, not a universal termination theorem or performance
claim.

Clean replay applies only `migration17.patch` to the M16 source-slice plus the
byte-identical frozen Phase32 source/test blobs. The 183-test gate and both finite
population JSON files reproduce; deterministic evidence is byte-identical. Patch
SHA256: `87ff87b254349b973bf804c8a6579538a54a8cabd01e9d23a7af71037517e7c6`.

## Remaining work

The default Phase32 path, CLI, `phase32_lab.html` browser, report schema and site
remain legacy float. M18 should expose exact textual pitch/precision through the
real CLI and machine outputs without inferring from `config.pitch`, then a later
browser slice can migrate the actual page. The missing HTML package-data tests
must be recovered when that browser slice materializes the real template.

M15 production workbench/full-root-package admission also remains separately
unpassed; do not confuse M17 numerical progress with that packaging/browser gate.
Do not rebuild M01–M16 arithmetic or switch local tie semantics.
