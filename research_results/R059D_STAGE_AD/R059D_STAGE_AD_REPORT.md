# R059D Stage AD — Triangular Coverage BRC Circle Resolve

Researcher-ID: `EM-R059D-3F7C42`
Task-ID: `RS-R059D-STAGE-AD-TRIANGULAR-COVERAGE-BRC-CIRCLE-RESOLVE`
Taskbook source: `0bae4ac7ab7d8c6073c901598a009ac598826f07`
Frozen base: `71a40c12b5804fd76e10a91df431c1d5f80304f0`

## Primary disposition

`COVERAGE_BRIDGE_ESTABLISHED__RESOLVE_RULE_UNDERDETERMINED`

## Construction

The source teacher is the orthogonal-system fixed-length disk/orbit. In the triangular compatibility chart the source classifier uses
`Q(a,b)=a^2+ab+b^2` only as a source-side teacher identity.

Each Enterprise implementation triangle is subdivided into `s^2` equal-area microtriangles. The centroid of every microtriangle is classified with an exact scaled-integer comparison, so every coverage value is stored as an integer fraction `covered/s^2`. Primary registry:
- radii `r=1..24`;
- sampling `s=4,8,16,32`;
- 96 primary cases;
- secondary `s=64` controls and `r=24,s=128`.

The soft frontier is exact but not uniformly cell-adjacency connected inside one 60-degree sector: 43/96 primary cases have more than one frontier-cell component under strict edge adjacency. This failure is retained. It does not prevent the independently resolved binary N/C disks from having a single closed interface.

## Resolver N

`NEAREST_CELL_BASELINE` classifies the deterministic triangle centroid by the source teacher.

Across all 96 primary cases:
- full closure: PASS;
- one occupied component: PASS;
- one interface-boundary cycle: PASS;
- six-sector rotation: PASS;
- reflection: PASS;
- source provenance: PASS.

Sampling precision is exactly irrelevant to N by definition.

## Resolver C

`COVERAGE_THRESHOLD` uses one globally frozen threshold `theta=1/2`.

Across all 96 primary cases it passes the same primary closure, topology, D6 and provenance gates as N.

However N and C produce different binary boundaries in **25/96** cases. At `s=32` the differing radii are:
`10,11,15,17,21,22,24`.

Therefore the successful coverage bridge does not uniquely determine a binary resolve rule.

Coverage-sampling changes are bounded but not uniformly absent. Secondary controls show most difficult radii stabilize by `s=64`; radius 24 changes from `s=32` to `s=64` and then is stable at the `s=128` control.

## Resolver R

The predeclared residual recurrence is

`e_(k+1)=e_k+c_k-b_k`

with `b_k=1` iff `e_k+c_k >= 1/2`, separately initialized with `e_0=0` in each open 60-degree sector.

Exact theorem:

`-1/2 <= e_k < 1/2`

for every prefix. Hence each sector has exact coverage discrepancy at most `1/2`, and the six-sector full-circle discrepancy satisfies

`|E_total| <= 3`

on the audited construction.

This is the strongest new exact structural result of AD.

But R is not currently a valid unique circle resolver:
- forward/reverse occupancy differs in **82/96** primary cases;
- mirror(forward) equals reverse in 96/96, showing the dependence is a genuine orientation/order effect;
- exact reflection symmetry passes only **14/96**;
- the full primary circle gate vector passes only **12/96**;
- multiple occupied components occur in 43/96 cases;
- a canonical single interface cycle exists in only 48/96 cases.

Therefore:

`ORDER_DEPENDENT_RESOLVE`

and the residual rule is not promoted as the native BRC circle law.

## Cross precision

Coverage sampling and native spatial refinement remain typed separately.

Native spatial refinement controls use radii `1,2,3,5,8`, refinement factors `h=2,3,4`, fine coverage sampling `s=8`, and deterministic majority coarse-graining of the `h^2` child triangles.

Observed maximum coarse/base symmetric difference:
- N: 12 cells;
- C: 12 cells;
- R: 36 cells.

Statuses:
- N: `BOUNDED_CROSS_PRECISION_DIFFERENCE`;
- C: `BOUNDED_CROSS_PRECISION_DIFFERENCE`;
- R: `CROSS_PRECISION_INCONSISTENT`.

No universal exact refinement theorem is claimed.

## Circle/orbit candidate

For N and C every primary case has one closed interface-edge cycle. For discriminator radii
`1,2,3,4,5,8,13,21` at `s=32`, exact ordered boundary edge states with coverage provenance are frozen as
`ENTERPRISE_CIRCLE_ORBIT_CANDIDATE`.

These are typed only as `SOURCE_LENGTH_COMPATIBLE(r,s)`. No target-side Enterprise metric or equal-length theorem is imported.

## Historical R059D bridge

After AD data were generated independently, the N/C one-sector boundary arcs were compared with historical staircase work.

Their local interface steps are drawn from
`(-1,1)`, `(-1,0)`, `(0,1)`,
so both coordinate components evolve by binary increments `(0, 1)` after the natural monotone reparameterization. This is a genuine raster/staircase compatibility observation.

However it is **not** an exact identification with the old pure-ray staircase theorem. The residual state supplies an explicit jump discriminator, but it is not canonical because of the 82/96 order-dependence result.

Therefore:

`HISTORICAL_BRC_BRIDGE_STATUS = QUALITATIVE_RASTER_STAIRCASE_BRIDGE__EXACT_HISTORICAL_BRC_SELECTION_BRIDGE_OPEN`.

## Status vector

- `COVERAGE_FIELD_STATUS = EXACT_INTEGER_RATIONAL_COVERAGE_FIELD_ESTABLISHED`
- `FRONTIER_STATUS = EXACT_SOFT_FRONTIER_ESTABLISHED__SECTOR_CONNECTIVITY_NOT_UNIVERSAL`
- `NEAREST_CELL_STATUS = PASSES_PRIMARY_CIRCLE_GATES_96_OF_96__BASELINE_ONLY`
- `COVERAGE_THRESHOLD_STATUS = PASSES_PRIMARY_CIRCLE_GATES_96_OF_96__NOT_UNIQUELY_SELECTED`
- `ACCUMULATED_RESIDUAL_STATUS = EXACT_ERROR_BOUND_PROVED__ORDER_DEPENDENT__PRIMARY_GATES_12_OF_96`
- `FULL_CIRCLE_CLOSURE_STATUS = N_AND_C_PASS_ALL_PRIMARY_CASES__R_MIXED`
- `D6_SYMMETRY_STATUS = N_AND_C_EXACT__R_ROTATION_EXACT_REFLECTION_NOT_GENERAL`
- `ORDER_DEPENDENCE_STATUS = ORDER_DEPENDENT_RESOLVE`
- `CROSS_PRECISION_STATUS = MIXED__N_C_BOUNDED_DIAGNOSTIC__R_INCONSISTENT`
- `HISTORICAL_BRC_BRIDGE_STATUS = QUALITATIVE_RASTER_STAIRCASE_BRIDGE__EXACT_HISTORICAL_BRC_SELECTION_BRIDGE_OPEN`

## Checker

Deterministic checker passes `2643/2643`, digest
`2627ce754fed59485f97c6c861f707f0d1e29b852d514b42272829fc81f7cde7`
before the external Git-history immutability gate.

No AE or later stage is consumed.
