# Native Enterprise CRT tower: downward-projected prime-fiber equidistribution candidate

Status: `FREE_RESEARCH_EXACT_FINITE_CENSUS / EQUIDISTRIBUTION_CANDIDATE / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_C3_CRT_COLLAPSE_TOWER_2D_19D_20260823.md`

## 1. Exact test shell

Use the exact d=8 primorial shell

`r=P_8=9699690=2*3*5*7*11*13*17*19`.

The largest C3 fiber labels on this shell are below `2^64`, so the finite primality census can use a deterministic Miller-Rabin base set valid on the full tested range.

The primitive basin has

`phi(P_8)=1658880`

fibers.

Exact enumeration finds

`T(P_8)=9330`

fully-prime C3 fibers.

Each is represented by its shell residue

`rho in U(P_8)`.

## 2. Downward projection

For each `j=2,...,8`, reduce the 9330 bright residues modulo

`P_j`.

This is exactly the canonical tower map

`U(P_8) -> U(P_j)`.

The observed occupied classes are:

- j=2: `2/2`;
- j=3: `8/8`;
- j=4: `48/48`;
- j=5: `480/480`;
- j=6: `4592/5760`;
- j=7: `8938/92160`;
- j=8: `9330/1658880`.

For sparse high layers, occupancy is sample-limited. The observed occupied counts are close to the occupancy expected from uniform random samples of size 9330 on the corresponding unit basin.

## 3. Lower-dimensional uniformity metrics

For dimensions where the expected count per unit class remains meaningful, compare the empirical projection with uniform measure on `U(P_j)`.

Total-variation distance:

- j=2: `0.00096463`;
- j=3: `0.00640407`;
- j=4: `0.02704984`;
- j=5: `0.09067524`;
- j=6: `0.32341461`.

Reduced chi-square (`chi^2/(|U|-1)`):

- j=2: `0.03473`;
- j=3: `0.43209`;
- j=4: `0.81803`;
- j=5: `1.01413`;
- j=6: `1.01768`.

The normalized empirical entropy is:

- j=2: `0.9999973`;
- j=3: `0.9999214`;
- j=4: `0.9994707`;
- j=5: `0.9957077`;
- j=6: `0.9580790`.

At j=5 and j=6 the reduced chi-square is essentially 1, consistent with ordinary finite multinomial fluctuation around the uniform unit-basin distribution.

## 4. Occupancy sanity check

For N=9330 independent uniform draws from U states, the expected occupied class count is

`U*(1-(1-1/U)^N)`.

Observed versus this uniform-sampling baseline:

- j=5, U=480: observed 480, expected approximately 480.0000;
- j=6, U=5760: observed 4592, expected approximately 4620.03;
- j=7, U=92160: observed 8938, expected approximately 8873.32;
- j=8, U=1658880: observed 9330, expected approximately 9303.81.

No dramatic clustering survives this coarse downward projection in the finite d=8 census.

## 5. Interpretation

The finite experiment suggests the native pattern

`HIGH-DIMENSIONAL BRIGHT FIBERS ARE SPARSE`

`-> DOWNWARD CRT COLLAPSE`

`-> NEAR-UNIFORM COVERAGE OF LOWER UNIT BASINS`.

This is qualitatively different from searching for Euclidean bright lines. The visually/simple object is the lower-dimensional shadow: a high-dimensional sparse set becomes almost homogeneous after enough independent collapse channels are forgotten.

## 6. Falsification boundary

This is not yet evidence of a new prime distribution theorem.

Classical Hardy-Littlewood prime-tuple heuristics and singular-series models already predict that local residue obstructions govern prime constellations, and equidistribution across admissible reduced residue classes is compatible with that framework.

Therefore the current status is:

`PROJECTED_UNIT_EQUIDISTRIBUTION = FINITE_NATIVE_PATTERN_CANDIDATE`.

A genuinely Enterprise-specific survivor would have to show a projection statistic not explained by the classical local singular series.

## 7. Next discriminating test

1. repeat on multiple shells carrying the same d-dimensional channel set rather than only the exact primorial shell;
2. compare observed projection measures to a matched singular-series null, not merely uniform measure;
3. inspect whether collapse-to-collapse correlations between adjacent levels retain information after local-factor normalization;
4. only promote a new invariant if a stable residual survives these controls.
