# R059D Stage X — Triaxial Unit-Step Staircase Classification

Task-ID: `RS-R059D-STAGE-X-TRIAXIAL-UNIT-STEP-STAIRCASE-CLASSIFICATION`
Generation: `R059D`
Status: `DRIVER_APPROVED_TASKBOOK`
Date: `2026-08-16`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Researcher-ID: `EM-R059D-9C6B2A`
Owner branch: `research/r059d-stage-x-triaxial-unit-step-staircase`
Frozen parent: `8313e75a356608f64795332a397d463631b9be18`

## 0. Frozen inputs and purpose

Stage W REISSUE2 is accepted as:

`VALID_NONHOMOGENEOUS_UNDERDETERMINATION`.

Its valid conclusions are immutable. In particular:

- cell coordinates are integers only;
- the A2/C6 cell-ID scaffold is independent of stored coordinates;
- first-round homogeneous coordinate increments are forbidden as a native premise;
- square root survives the nonhomogeneous minimal/cyclic atlas but is not unique;
- p=2..6 survive in the tested Q witness;
- collapse lower/upper remains multibranch through radius 4;
- `5 -> 4/9` remains unresolved.

Stage X does NOT enlarge the old completion CSP merely by brute-force radius. It inserts the missing elementary meaning of a number-axis unit step and classifies the resulting integer coordinate maps.

## 1. Core semantic distinction

Keep separate:

1. `CELL_ID` — combinatorial A2/C6 identity `(a,b)` and adjacency only.
2. `INTEGER_CELL_COORDINATE` — stored `(U,V,W) in Z^3`.
3. `PRECOLLAPSE_ALGEBRAIC_VALUE` — may be radical; never stored.
4. `UNIT_AXIS_STEP` — one real adjacency transition in a named positive/negative axis direction.
5. `COLLAPSE_STAIRCASE_EVENT` — whether a transverse stored integer coordinate stays on its current layer or crosses exactly one adjacent integer layer during one unit step.

Do not reintroduce the old zero-sum raw coordinate ontology or fixed full-vector increments.

## 2. Cell-ID scaffold

Use the frozen A2/C6 cell-ID moves:

- `+u : (a,b)->(a+1,b)`
- `-w : (a,b)->(a+1,b-1)`
- `+v : (a,b)->(a,b-1)`
- `-u : (a,b)->(a-1,b)`
- `+w : (a,b)->(a-1,b+1)`
- `-v : (a,b)->(a,b+1)`

This scaffold may be homogeneous as cell identity. Stored coordinates may not inherit additive homogeneity.

The exact cell relation `+u,+v,+w = identity` is a cell-ID relation only and must be respected by any path-independent stored coordinate map.

## 3. Hard observations

Freeze:

- `C(O)=(0,0,0)`;
- `C(+u)=(1,-1,-1)`.

Use the cyclic first-shell assignment only in a separately typed symmetric subcase:

- `C(+v)=(-1,1,-1)`;
- `C(+w)=(-1,-1,1)`.

Do NOT assume global sign inversion. Audit it later as an additional condition.

## 4. Unit-step staircase hypothesis to test

This task tests the user-intended number-axis semantics:

For every realized `+u` adjacency edge from any cell:

- the primary stored coordinate changes exactly `Delta U=+1`;
- each transverse stored coordinate changes by either `0` or `-1`;
- which of `0/-1` occurs may depend on the current cell/state.

Cyclically:

- `+v`: `Delta V=+1`, `Delta U,Delta W in {0,-1}`;
- `+w`: `Delta W=+1`, `Delta U,Delta V in {0,-1}`.

A negative edge is the exact inverse of the realized positive edge between the same two cell IDs. Do not replace this by global coordinate sign inversion.

This is `UNIT_STEP_STAIRCASE`, not translation homogeneity. The full coordinate increment is explicitly allowed to vary from cell to cell.

If this hypothesis is inconsistent with the A2 cell relations plus the hard first-step observation, reject it rather than repairing it post hoc.

## 5. Stage X0 — Solve the coordinate consistency equations

Let

`C(a,b)=(U(a,b),V(a,b),W(a,b))`.

Derive, symbolically and exactly, the most general path-independent integer solution of the unit-step staircase constraints on the infinite A2 scaffold or on a theoremically sufficient generic domain.

Do not start from a guessed root formula.

Required:

- solve the exact finite-difference equations imposed by primary `+1` changes;
- derive all remaining one-dimensional free functions/parameters, if any;
- impose transverse `0/-1` edge constraints exactly;
- impose cyclic covariance in the symmetric subcase;
- optionally impose reflection fixing the `u` ray and swapping the two transverse axes, because the user examples use equal transverse values; type this assumption explicitly;
- determine whether the whole 2D stored-coordinate atlas reduces to one scalar staircase sequence.

Preferred positive freeze if proved:

`TRIAXIAL_INTEGER_ATLAS_REDUCES_TO_ONE_BINARY_STAIRCASE_SEQUENCE`.

But do not assume this result.

## 6. Stage X1 — Pure-axis staircase

In the reflection-symmetric `+u` ray subcase define, if justified,

`C(nu)=(n,-a_n,-a_n)`

with integer `a_n>=0`.

Freeze only what the unit-step equations force, expected to include tests of:

- `a_0=0`;
- `a_1=1`;
- `a_{n+1}-a_n in {0,1}`.

Prove or refute that every admissible global atlas corresponds one-to-one with such a staircase sequence (plus explicitly listed symmetry/gauge data).

The central question is whether local cell-grid self-consistency forces the jump positions of `a_n`, or leaves them arbitrary.

## 7. Stage X2 — Global inversion audit

Audit, do not assume:

`C(-x)=-C(x)`.

Determine whether global coordinate inversion is compatible with:

- the hard first-step `C(+u)=(1,-1,-1)`;
- the A2 cell relation;
- cyclic symmetry;
- unit-step staircase semantics;
- transverse-ray reflection symmetry.

If incompatible, freeze the exact no-go and do NOT use global inversion to reject nontrivial root laws in later stages.

This audit is important because Stage W REISSUE2 showed that a particular Q witness failed global inversion; Stage X must decide whether the problem is Q-specific or structural under the new unit-step semantics.

## 8. Stage X3 — Root laws as staircase jump schedules

Only after the staircase classification, retype root candidates as candidate jump schedules for `a_n`.

For p=2..6 and each n:

- exact `n^(1/p)` is a PRECOLLAPSE value;
- legal stored magnitudes are the two adjacent integers when nonintegral;
- one global sequence `a_n` must be used consistently everywhere; do not choose lower/upper independently per cell.

Test at least:

- lower/floor root schedule;
- upper/ceiling root schedule;
- nearest-root schedule as a control only;
- power-midpoint schedule as a control only;
- arbitrary monotone 0/1 staircase subject to the root interval at every n, represented symbolically if possible rather than exhaustively.

Determine whether the Stage-X local coordinate equations distinguish p or distinguish lower/upper at all.

If every legal staircase extends, freeze:

`LOCAL_INTEGER_ATLAS_SELF_CONSISTENCY_ALONE_CANNOT_IDENTIFY_ROOT_ORDER_OR_COLLAPSE_JUMPS`.

That negative theorem would be a successful result.

## 9. Stage X4 — Count-only discriminator audit

The user hypothesis is that the missing jump law should be obtainable by elementary cell counting.

Do not formula-fit. Instead inventory a small predeclared set of canonical combinatorial counts already present in the A2 scaffold, for example:

- line/ray count;
- shell count;
- ball count;
- triangular sector count;
- rectangular/parallelogram block count generated by two named transverse directions.

For each count, state exactly what set of cell IDs is being counted and derive the elementary formula from finite sums/products.

Then ask a narrow question:

> Is there an independently justified equality/inequality connecting the direct primary ray count n to one of these transverse region counts such that the staircase jump positions become perfect-power or another elementary threshold sequence?

Do not simply declare `n=a_n^2` or `n=a_n^p`. Such a relation must correspond to an explicitly counted region or bijection.

If no such identity is forced by the current semantics, freeze:

`MISSING_COUNT_IDENTITY_NOT_YET_IDENTIFIED`.

This is preferable to inventing a root law.

## 10. Stage X5 — 5 -> 4 / 9 control

Only if a square-count identity is independently justified in X4, evaluate `n=5`.

If the derived staircase gives `a_5=2`, freeze `FIVE_TO_FOUR_FORCED_BY_COUNT_IDENTITY`.
If it gives `a_5=3`, freeze `FIVE_TO_NINE_FORCED_BY_COUNT_IDENTITY`.
If X4 does not identify the jump law, preserve `FIVE_TO_FOUR_OR_NINE_UNRESOLVED`.

No nearest rounding, midpoint convention, probability, stabilizer, reward, or Euclidean metric may decide this.

## 11. Mandatory anti-triviality controls

The checker must hard-reject accidental use of:

- fixed full-vector stored increments;
- `C(path)=sum(first-step coordinate triples)`;
- `C(nu)=n C(u)` as a premise;
- global sign inversion unless explicitly in the inversion-audit subcase;
- old zero-sum raw coordinates;
- old `e_i-e_j` raw cell coordinates;
- arbitrary preferred path;
- per-cell independent lower/upper completion when testing a global staircase law;
- nearest/floor/ceil as native premises;
- Euclidean angle/distance/norm;
- probability, ML, optimization, or fitted coefficients.

## 12. Required artifacts

At minimum:

1. `R059D_STAGE_X_UNIT_STEP_STAIRCASE_PROTOCOL.json`
2. `R059D_STAGE_X_GENERAL_COORDINATE_SOLUTION.json`
3. `R059D_STAGE_X_CYCLIC_SYMMETRY_REDUCTION.json`
4. `R059D_STAGE_X_PURE_AXIS_STAIRCASE_THEOREM.json`
5. `R059D_STAGE_X_GLOBAL_INVERSION_AUDIT.json`
6. `R059D_STAGE_X_ROOT_SCHEDULE_LEDGER.json`
7. `R059D_STAGE_X_COUNT_REGION_REGISTRY.json`
8. `R059D_STAGE_X_COUNT_IDENTITY_DISCRIMINATOR.json`
9. `R059D_STAGE_X_FIVE_TO_FOUR_OR_NINE_CONTROL.json`
10. `R059D_STAGE_X_TRIVIALITY_LEAKAGE_LEDGER.json`
11. deterministic checker source/output
12. report
13. manifest
14. frozen checkpoint.

## 13. Allowed outcomes

Positive and negative outcomes are both valid. Useful freezes include:

- `UNIT_STEP_STAIRCASE_SEMANTICS_SELF_CONSISTENT`
- `UNIT_STEP_STAIRCASE_SEMANTICS_INCONSISTENT`
- `TRIAXIAL_INTEGER_ATLAS_REDUCES_TO_ONE_BINARY_STAIRCASE_SEQUENCE`
- `PURE_AXIS_STAIRCASE_JUMPS_REMAIN_FREE`
- `GLOBAL_INVERSION_INCOMPATIBLE_WITH_HARD_FIRST_STEP_AND_UNIT_STEP_SEMANTICS`
- `ROOT_SCHEDULE_NOT_IDENTIFIED_BY_LOCAL_ATLAS`
- `COUNT_IDENTITY_FORCES_SQUARE_ROOT_THRESHOLDS`
- `COUNT_IDENTITY_FORCES_OTHER_THRESHOLDS`
- `MISSING_COUNT_IDENTITY_NOT_YET_IDENTIFIED`
- `FIVE_TO_FOUR_FORCED_BY_COUNT_IDENTITY`
- `FIVE_TO_NINE_FORCED_BY_COUNT_IDENTITY`
- `FIVE_TO_FOUR_OR_NINE_UNRESOLVED`
- `UNIVERSAL_BRC_LAW_NOT_ESTABLISHED`.

After all required artifacts and checks:

`STOP_FOR_DRIVER_REVIEW`.
