# Migration 12 — machine-only field construction without display floats

Status: locally validated candidate; no display default or main-code cutover.
Baseline remote: `3f6946239e28009bd915075afc201faa508468e8` (M11).
Researcher: EM-DIRECT-4A5102 / TASK_RESEARCH.

## Actual change

The real `multiplicative.py::build_field` now accepts `include_display=False`.
It takes a typed `machine_config` containing only count, scheme and exact prime
phase overrides, and requires an explicit positive integer-ratio `cell_scale`.
The existing phase generator, BRC arithmetic, certified cells, full base
certificates and legacy axial lexicographic tie selection are executed unchanged.
This is a caller separation, not a new number class or BRC family.

Machine construction never parses a display scale or calls sqrt/sin/cos, the
legacy quantizer or the optional pixel helper. `ideal` fields are absent rather
than false zeros. The complete machine field, statistics and machine JSON/CSV
exports contain no float objects. Source denominators and lexical CLI inputs
remain unreduced; nonzero phase defects and unresolved identities are retained.

The old default `build_field` path and the optional displayed exact path keep
M11 objects and JSON ordering. Shared integer input validation is extracted
without changing legacy valid outputs or tested error ordering. Existing
mathematical functions other than config/build_field/hex_data/main keep their
M11 ASTs; the original BRC source blob is unchanged.

## Actual CLI and versioned data

`--machine-only` now uses the float-free constructor. Its report schema is
`NOLLM_MULTIPLICATIVE_MACHINE_REPORT_V1`, whose `config` has schema
`NOLLM_MULTIPLICATIVE_MACHINE_CONFIG_V1`. This is intentionally NOT a display
V1/V2 configuration with its float scale silently deleted. Explicit `--scale`
is rejected in machine-only mode, before float conversion or any writes.
Ordinary HTML/display calls retain their V1/V2 reports and startup contract.

The machine field/report/hex metadata retain `cell_precision.initial_bits` and
`max_bits`. Without these parameters, replaying a low-budget unresolved report
at the default precision would change the observation. Tests reconstruct the
same unresolved summary from the persisted phase inputs, original scale text
and original precision budget.

Machine hex export uses the existing visual-data V2 carrier without ideal_x/y.
Every identity is retained even at shared centers. It includes the exact cell
summary and provenance, and is detached from the live field. Unresolved cells
or coordinates outside that carrier's integer range are rejected before any
requested outputs are written. A broader positive scale is still valid for an
exact machine report; rejection by the visual carrier does not reject the
mathematical source. No multi-file I/O rollback/transaction guarantee is made.

## Reproduce

```bash
python tools/run_migration12.py
python tools/benchmark_migration12.py
python tools/benchmark_migration12.py --count 65536 --schemes valuation --scales 1
PYTHONPATH=src:tools/nollm_visual_toolkit python -m nollm_visual_toolkit.multiplicative --count 4096 --machine-only --cell-scale 0.50 --report exact.json --hex-data cells.json
```

```python
from nollm_visual_toolkit import multiplicative as m
field = m.build_field(m.machine_config(256, 'valuation'),
                      cell_scale=(50, 100), include_display=False)
stats = m.statistics(field, rings=3, sectors=7, readout_scale=10**12)
```

Python, mpmath and Node must be available for the full retained tests. Production
machine arithmetic does not use mpmath. There is no dependency installation,
remote computation or background executor.

## Verified scope

148 tests passed: 27 new machine-path tests and 121 retained tests, zero
failures/errors/skips. Two M11 test expectations were explicitly advanced:
allowed caller AST changes and the dedicated machine report schema. The initial
run surfaced exactly those two expected differences; both are retained in logs.
Tests disable floating conversion, complex construction, display math and the
old quantizer during full machine construction, readouts and real CLI exports.
JSON/CSV roundtrips, strict config typing, replay budgets, detached exports,
source order, legacy objects, zero phase and spiral nonclosure are covered.

Thirteen finite comparisons passed: four schemes x three scales at 4096,
plus valuation/scale-one at 65536. Full certificate and pixel-free identity
hashes and all default exact statistics equal the frozen M11 displayed
reference. All these cases certify every identity; the 65536 case occupies
44731 cells. Finite tests are not a universal theorem or complexity guarantee.

A fresh M11 bundle plus migration12.patch replayed all 148 tests and 13
population comparisons. All six source files and all three deterministic
reports matched byte-for-byte. The combined benchmark exceeded one tool-call
budget; only the incomplete 65536 unit was restarted and completed separately.
No background benchmark is implied.

Patch SHA256: `503a68a1011356ad69352e5440bbe4c4a07a0d5f3d5c2a2e735743c4f8e6f8f3`.
The exact-policy checker passes its unchanged declared arithmetic files, not
the whole mixed legacy/display module. Node comparisons are retained M10
readout functions, not a new DOM/browser/WebCrypto run.

## Remaining work and delivery boundary

This is a focused source slice over the M11 package, not a full application or
repository mirror. NEVER overwrite production with its inherited isolated
`src/enterprise_math/__init__.py`. Apply only migration12.patch to pinned M11
source. The normal display path still intentionally uses approximate pixels.
Full-package/startup/browser regression, native navigation, Safari/iOS,
independent review, default activation and main integration are not completed.

Next: integrate the machine report schema into actual downstream report readers
and explicit display adapters, then validate the complete package before a
separate default/main decision. Do not infer missing display scales or pixels
from an already-rounded float. Broader production consumers, historical
experiments, general transcendental/complex-amplitude closure and native X6
path integration remain separate. Geometry here remains a declared A2 observer.
