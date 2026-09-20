# Migration 06 — multiplicative.py certified cells with legacy tie semantics

Status: opt-in candidate; default/CLI/browser/main integration not changed.
Baseline: `68e828ef5131219eae72ee740827ead04f3c4250` (M05 report head).
Code: `26a8cb4c2fda7012268545222b11316354df34dc`.
Researcher: EM-DIRECT-4A5102 / TASK_RESEARCH.

## What moved

The older `multiplicative.py` already used exact integer phase residues, but its
cell identity still came from `sqrt/cos/sin -> lattice_point(float,float)`.  The
new opt-in `build_field(..., cell_scale=(n,d))` sends cell membership through the
existing certified integer/residual A2 engine.  The historical float `config.scale`
is *not* converted back into a rational; it remains display scale only.

When `cell_scale` is absent, the complete legacy `build_field`, `multiplication`,
`statistics`, and `hex_data` objects stay byte-semantically/structurally equal to
the frozen implementation in the tested cases.  Exact-mode rows retain approximate
`ideal` pixels for rendering, but those pixels do not choose cells.

## Important tie-policy correction

M03/M04's base certifier and this older module did not declare the same tie rule.
The base rule is `HALF_TOWARD_POSITIVE_INFINITY_THEN_MAX_ERROR_Q_R_S`; the older
`lattice_point` explicitly says nearest center and then axial `(q,r)` lexicographic.
A finite audit found 1,080 certified ties and 504 cases where those rules choose
different equal-nearest cells.  Therefore M06 does not silently reuse the base
selection.  It preserves the full base certificate and applies an exact adapter
only to certified ties, using integer rational distances or the existing exact
shared-radical sign comparator.  Example: `n=4`, quarter turn, scale 1/2 has base
cell `(0,1)` but this module's declared legacy tie cell `(-1,1)`.

A separate float-boundary witness remains: `n=3`, quarter turn, scale 1/2 is
`(0,1)` under the old double path and `(-1,1)` under exact legacy semantics.

## Validation

The source-slice runner passes 35 tests: 12 new migration/compatibility tests plus
23 historical tests, with zero failures/errors and one explicit source-slice skip.
That skip is only the historical deterministic-HTML test because the delivery
slice does not contain unchanged `multiplicative_lab.html`; the runner executes it
when that package-data file exists in a full checkout.

Twelve 4,096-identity cases (four schemes × scales 1/2, 1, 3/2) all certify every
identity and preserve all four aggregate collision statistics.  One individual
cell differs in that matrix: mixed scheme, scale 3/2, `n=2075`, a true certified
tie; aggregate counts remain equal.  A 65,536-identity valuation/scale-1 run also
certifies all identities and exactly preserves occupied=44,731, collisions=12,435,
excess=20,805, max-load=9, with zero individual differences in that case.

These are finite checks, not proof for all inputs.  Timings in evidence are
telemetry only.

## Exact vs approximate boundaries

Exact mode adds exact CV² records for integer angular/area-sector counts.  The old
CV square roots and iid sqrt reference remain compatibility/display quantities.
`ideal_x/y` remain approximate pixels.  Rounded-relative-error and maximum display
quantization error are omitted in exact-cell mode because the exact cell scale can
be different from the legacy display float scale; mixing the two observers would
be false precision.

Low precision may produce `UNRESOLVED_BOUNDARY`.  Such identities have null cells,
complete cell totals are null, and `hex_data` refuses to export guessed cells.
No float fallback is used.

This remains a declared A2 observer, not native X6/P000 geometry.  It is not a
general arbitrary-angle transcendental engine and says nothing about complex
amplitudes/QFT.

## Reproduce

```bash
python tools/run_migration06.py
python tools/benchmark_migration06.py
```

Patch SHA-256: `8afe743117c09a8a1756ee6df0b8fff46a901db6464d43402f0af15b8d75d39e`.
The clean replay materializes the two frozen upstream blobs that M05's source-slice bundle did not carry, then applies this patch.

See `evidence/migration06/` for frozen upstream sources, finite matrices, tie audit,
and witnesses.  The bundle is a source slice, not a full repository mirror.
