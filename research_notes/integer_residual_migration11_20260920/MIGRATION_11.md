# Migration 11 — exact Python statistics and product readouts

Status: locally validated candidate; no production-default or main-code cutover.
Baseline: `f7f2ecbf2d61e96ef7835c495ab4c9736f52286d` (M10).
Researcher: EM-DIRECT-4A5102 / TASK_RESEARCH.

## Actual consumer change

Only `multiplicative.py::statistics` and `multiplication` change their Python
function ASTs relative to M10. Cell construction, exact lexicographic tie
selection, CLI/main/render, startup and BRC arithmetic remain unchanged.

Exact statistics omit approximate CV, area-sector CV, iid square-root reference
and geometric-error metrics with null values and
`approximate_metrics_role=OMITTED_FROM_EXACT_OBSERVER`. Exact multiplication
returns integer product, modular phase defect and integer omega defect without
reading pixel positions or display scale. Both approximate errors are null even
for multiplication by zero: an omitted measurement is not a measured zero.
Zero has undefined phase; the spiral counterexample's nonzero defect survives.

CV squared retains the ordered histogram and unreduced integers
`N=B*sum(c_i*c_i)-T*T`, `D=T*T`. The existing BRC readout computes
`S*N=D*q+r`, `0<=r<D`, so `CV2=q/S+r/(D*S)`. The default readout scale is
1,000,000, matching the browser. Python callers may specify another positive
integer or `readout_scale=None` for source-only output. This scale does not
change cell layout, precision budgets, source counts or their order.

Custom positive integer rings/sectors remain supported, including one sector.
The existing Python/BigInt AngularDispersion family now accepts a one-bin
histogram with positive population: its CV2 is exactly zero, with its original
T*T denominator. It is not padded into a different histogram. Empty/zero
populations and inexact/invalid counts remain rejected. The separate browser
phaseBin domain is unchanged. Tested legacy-mode V1 objects and JSON stay
unchanged; four old test expectations are deliberately advanced for the new
single-bin domain and exact omission roles.

## Validation

121 tests passed: 20 new readout tests and 101 retained tests; zero failures,
errors or skips. Checks include 5 complete Python/Node statistic records,
1,028 sampled product records, 40 custom histogram/readout-scale cases and
60 complete legacy statistic objects. Tests poison floating sqrt/trigonometry,
remove pixel fields, preserve unresolved totals, execute the real machine-only
CLI, and check the unchanged BRC blob and unchanged M10 function ASTs.

Thirteen finite population readout comparisons passed: twelve 4,096-identity
cases across four schemes and three scales, plus valuation/scale-one at
65,536. Every default statistic record matches the frozen M10 browser functions
and every prior integer count is unchanged. The 65,536 case occupies 44,731
cells. These are finite checks, not a universal theorem or speed claim.

Node executes verbatim M10 stats/multiply function excerpts in a test host
that supplies the fixed modulus and rejects legacy dispatch. It does NOT
execute a browser build, DOM, navigation or WebCrypto. M10's prior browser
checks are not claimed as M11 reruns. The exact-policy checker passes only
angular_dispersion.py and certified_hex.py, not the mixed legacy module.

Clean pinned source-slice replay passed the same 121 tests and 13 population
comparisons; all 11 source/fixture files and both deterministic reports match.
A later one-bin docstring clarification changes no arithmetic. Final delivery
verification is recorded separately. Raw reports/logs are in the bundle;
source_manifest.json and validation.json bind their hashes.

## Reproduce and boundaries

```bash
python tools/run_migration11.py
python tools/benchmark_migration11.py
```

Python API: `statistics(field, rings=3, sectors=7, readout_scale=10**12)` for
an explicit exact field. `None` requests source-only CV2; nondefault readout
options on a legacy field fail rather than silently do nothing.

Patch SHA256: `2b13f2bd69153cd87331d139d9a6ef01e61a3ab4a94a1195be04facdf9291919`.
Apply migration11.patch to the selected pinned M10 source. The delivery is a
focused readout source slice over the earlier M04 regression scaffold, NOT a
full M10 checkout or complete HTML application. Its inherited isolated
src/enterprise_math/__init__.py must NEVER overwrite production. Missing full
M10 browser/package files are not emulated or passed as full integration.

Exact field construction still computes approximate ideal display pixels;
config/hex export can still carry display floats. This slice only removes
them from exact statistics and multiplication readouts. Full package/startup
regression, native-browser acceptance, independent review, defaults and main
code integration remain pending. Geometry stays a declared A2 observer, not
native X6/P000; no general transcendental or complex-amplitude closure claim.

Next independent numerical unit: separate machine-only exact field creation
from optional approximate display construction, while preserving legacy
objects, CLI/startup source provenance and local tie semantics. Do not rebuild
BRC, repeat M01-M10, or bypass the known managed navigation restrictions.
