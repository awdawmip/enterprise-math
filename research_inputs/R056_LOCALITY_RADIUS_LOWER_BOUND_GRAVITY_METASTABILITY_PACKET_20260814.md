# R056 Problem Packet — Locality-Radius Lower Bounds for Fixed-N Gravity Metastability

Status: `FROZEN PROBLEM PACKET / NEW GENERATION AFTER R055 / NOT CANONICAL`

## 0. Why R056 exists

R055 established a sharp separation between the global gravity objective and the original strictly local monotone dynamics.

Frozen R055 anchors:

- `R055_RELAXATION_PROTOCOL_SHA256 = aa69f2bc31cb9b5ec574a85de2879b9f8f765cfdfdb6dd0cbfc625cf8feed683`
- `R055_MOVE_ENERGY_REGISTRY_SHA256 = 83d546105a3fa721ba5cadea9a1bbf217a1661fdf0d1560fcdccc6d4c9d29ceb`
- `R055_INITIAL_STATE_REGISTRY_SHA256 = 5de0e7ae6ff89cf81342f6c18125eb1eebd78c4725c0324acee2893552acd7f2`
- `R055_THEOREM_COUNTEREXAMPLE_LEDGER_SHA256 = 159ba8ed8e664522fec5fa9771b8efc7630d0b0c78ca5a2f67e7c33c724ac660`
- `R055_ARTIFACT_MANIFEST_SHA256 = 84d41e0d7c392576cfef8717eaa8fcdd6a5e780c02915b125e60043938dffdc7`

R055 full-workspace evidence source:

- exact source head: `ea0781f564b8c4016d592521a50c02888e2f371d`
- staging archive SHA-256: `d7686f5b71d5df95e910ec41d081c06afb75e483263f3ae2ea5631b7009c3736`
- full-sync source files: `381`
- full-sync source bytes: `184183474`

R055 proved in its frozen ledger that the centered hex shell

`H_r = {(a,b) in Z^2 : max(|a|,|b|,|a+b|) <= r}`

with

`N_r = 1 + 3 r(r+1)`

is a strict D1 local minimum of the exact gravity energy for every `r>=1`, while for every `r>=6` it admits a strictly improving D2 nonlocal relocation. Hence the original nearest-neighbor one-cell strict-descent law has an infinite metastable family.

The post-freeze R055 addendum also gives a disk-limit theorem for global `G` minimizers. R056 does **not** need to use the disk theorem as an optimization target. The present question is earlier and purely dynamical:

> Is R055's metastability merely a defect of the one-cell D1 rule, or is it an unavoidable consequence of every fixed bounded-support strict-descent local rearrangement?

R056 must not mutate any R055 bytes or reinterpret D2 as a local physical law.

## 1. Fixed substrate and energy

Use exactly the R055 triangular lattice and equal-mass fixed-N state space.

Axial coordinates:

- `e1=(1,0)`;
- `e2=(1/2,sqrt(3)/2)`;
- exact squared norm `Q(a,b)=a^2+a*b+b^2`;
- nearest-neighbor graph distance

`d_L((a,b),(c,d)) = max(|a-c|, |b-d|, |(a+b)-(c+d)|)`.

A state `C` must remain:

- finite;
- `|C|=N`;
- nearest-neighbor connected;
- hole-free under the frozen R055 topology convention.

For equal masses let

`S(C)=sum_{x in C} x`,

`g(C)=S(C)/N`,

`G(C)=N*sum_{x in C} Q(x)-Q(S(C))`.

This equals the frozen R055 exact pairwise gravity-compaction energy.

After every accepted move, recompute the full centroid and exact `G` as a checker invariant even if an incremental formula is used for candidate scoring.

## 2. General bounded-support cooperative move class

R056 introduces one generous comparison family between R055 D1 and D2.

For integers `m>=1`, `rho>=1`, define `D(m,rho)` as follows.

Choose finite sets

- `U subset C` of removed occupied cells;
- `V subset Lambda\C` of added empty cells;
- `1 <= |U| = |V| <= m`.

Set

`C'=(C\U) union V`.

The move is admissible only if:

1. `C'` has exactly `N` cells;
2. `C'` is connected;
3. `C'` is hole-free;
4. every changed cell lies within bounded lattice support:

`diam_L(U union V) := max_{x,y in U union V} d_L(x,y) <= rho`;

5. `G(C') < G(C)` strictly.

No plateau or uphill move is permitted in the primary R056 class.

Interpretation discipline:

- `D(1,1)` contains the original R055 D1 nearest-neighbor single-cell slide subject to the same topology conditions;
- `D(m,rho)` for `m>1` is a **cooperative bounded-support rearrangement reference**, not automatically a physical sliding law;
- R055 D2 is not any fixed `D(m,rho)` family as `r -> infinity`, because its relocation span may grow with the cluster diameter.

The class is intentionally generous. A no-go theorem for this class automatically applies to stricter local rearrangement laws with the same support bounds.

## 3. Exact multi-replacement energy identity

Let

`DeltaS = sum_{v in V} v - sum_{u in U} u`

and let `L(x,y)` be the polar bilinear form associated with `Q`, so

`Q(x+y)=Q(x)+Q(y)+L(x,y)`.

R056 must prove/check before heavy search:

`DeltaG = G(C')-G(C)`

`= N * (sum_{v in V}Q(v)-sum_{u in U}Q(u)) - L(S(C),DeltaS) - Q(DeltaS)`.

For centered shells `H_r`, `S(H_r)=0`, hence

`DeltaG = N_r * DeltaQsum - Q(DeltaS)`.

This identity is the preferred exact pruning/scoring formula.

## 4. Central locality quantities

For fixed `m`, define the shell escape locality radius

`rho_m(r) = min diam_L(U union V)`

over all admissible strictly `G`-decreasing replacements from `H_r` with `1<=|U|=|V|<=m`.

If no such move exists, set `rho_m(r)=infinity`.

Also define for a fixed locality cap `rho`

`m_rho(r) = min |U|`

over strictly decreasing admissible moves from `H_r` with support diameter at most `rho`, or `infinity` if none exists.

These are structural quantities. Do not choose `m` or `rho` after seeing holdout behavior without declaring a new generation.

## 5. Main theorem fork

The highest-value target is the following bounded-locality obstruction.

### Target A — bounded-support strict-descent obstruction

Prove, or find an exact counterexample to:

> For every fixed finite pair `(m,rho)`, there exists `r0(m,rho)` such that for every `r>=r0`, the centered shell `H_r` has no admissible `D(m,rho)` move with strictly smaller `G`.

Equivalent useful forms include:

- for every fixed `m`, `rho_m(r) -> infinity` as `r -> infinity`;
- stronger: for each fixed `m`, `rho_m(r) >= c_m r - O_m(1)` with some explicit `c_m>0`;
- strongest reasonable form: a lower bound uniform over every fixed `m` in a declared range or asymptotic family.

If proved, return

`BOUNDED_SUPPORT_STRICT_DESCENT_OBSTRUCTION`.

This would show that adding finitely many cooperative cells with a fixed local support cannot repair R055 D1 at all scales.

### Target B — finite-locality escape

If Target A is false, find the smallest exact counterexample and classify the minimal pair(s) `(m,rho)` that escape `H_r` for an unbounded family of `r`.

Do not claim an all-r local repair from finitely many examples.

## 6. Geometry/pruning theorem before brute force

Do not begin with a combinatorial all-subset search over large shells.

First derive exact inequalities using:

- the six supporting coordinates of `H_r`;
- convexity of `Q`;
- locality bound `diam_L <= rho`;
- the centered-shell identity `S=0`;
- integrality of `DeltaQsum`;
- the bound on `Q(DeltaS)` implied by `m` and `rho`.

A particularly useful route is to show that within any fixed-width boundary patch of a sufficiently large `H_r`, every legal replacement has positive `DeltaQsum`, while the centroid correction `Q(DeltaS)` is only bounded in terms of `(m,rho)`. Since `N_r=Theta(r^2)`, a positive integer `DeltaQsum` then dominates the centroid correction.

But this is a suggested proof strategy, not a permitted assumption. Exact equality cases `DeltaQsum=0` must be audited separately because then `-Q(DeltaS)` could create a strict decrease.

## 7. Frozen computation registry

Computation is for counterexample search, exact small cases and theorem stress-testing, not for replacing proof.

Before any shell search freeze the exact computation registry.

Primary exact construction radii:

`r = [2,3,4,5,6,8,10,12,16]`.

Strict holdout radii:

`r = [7,9,11,13,17,24]`.

Primary cooperative caps:

- `m in {1,2,3}` for exhaustive/strong search where feasible;
- `m=4` only for bounded radii where exact enumeration is demonstrably tractable;
- no silent expansion to large `m` after seeing results.

For `m=1`, compute exact `rho_1(r)` for substantially larger radii if cheap, preferably through at least `r=64`, because single-cell relocation can be searched directly without subset explosion.

For `m>=2`, use geometry-derived pruning and canonicalization before enumeration.

A computation that threatens the execution budget must checkpoint current exact results rather than silently extending the search domain.

## 8. Small exact comparisons

For each construction radius and each declared `m` where exact search is feasible, record:

- whether any strict descent exists;
- exact minimum support diameter `rho_m(r)`;
- number of minimizing move classes modulo the stabilizer of `H_r`;
- `|U|`, `DeltaQsum`, `Q(DeltaS)`, exact `DeltaG`;
- connectivity/hole-free certificate;
- whether the move is equivalent to an R055 D2-style far relocation or genuinely bounded-local.

For selected `rho`, also compute `m_rho(r)` where tractable.

Do not call a failed bounded search an infinity result unless the declared search space is exhaustive.

## 9. Holdout discipline

Before opening the strict holdout radii, freeze:

- the locality model;
- the shell-escape search protocol;
- the computation registry;
- the theorem/counterexample ledger status based on construction and proof work.

Holdout may test already-frozen conjectured formulas, lower bounds and exact search algorithms.

No theorem may be repaired by changing the move class after holdout.

## 10. What R056 must not do

R056 must not:

- use a Euclidean circle, radius, circumference, classical pi or tangent as a move target;
- mutate R055 frozen artifacts;
- relabel R055 D2 as local motion;
- introduce plateau or uphill moves into the primary class;
- jump directly to stochastic/thermal dynamics before resolving the strict bounded-support question;
- claim that `rho_m(r)` grows from a regression alone;
- infer an all-scale theorem from construction/holdout radii;
- hide `DeltaQsum=0` cases;
- treat a cooperative patch replacement as physically realizable without a separate kinematic argument.

If bounded-support strict descent is obstructed, the natural later generation is an energy-barrier/nonmonotone-local-path task. Do not open that generation inside R056.

## 11. Mandatory adversarial attacks

At minimum record:

- `R055_FROZEN_BYTES_MUTATED`;
- `R055_D2_RELABELED_LOCAL`;
- `CIRCLE_OR_PI_USED_IN_LOCALITY_SELECTION`;
- `MOVE_SUPPORT_DIAMETER_MISCOMPUTED`;
- `CELL_COUNT_CHANGED`;
- `CONNECTIVITY_OR_HOLE_FREE_VIOLATION`;
- `CENTROID_NOT_RECOMPUTED_AFTER_ACCEPTED_MOVE`;
- `MULTI_REPLACEMENT_DELTA_G_FORMULA_WRONG`;
- `DELTA_Q_ZERO_CASE_IGNORED`;
- `FINITE_SEARCH_CALLED_INFINITY`;
- `FINITE_RADII_REGRESSION_CALLED_THEOREM`;
- `M_OR_RHO_EXPANDED_POSTHOC`;
- `HOLDOUT_USED_TO_REPAIR_LOCALITY_MODEL`;
- `COOPERATIVE_REFERENCE_CALLED_PHYSICAL_SLIDE`;
- `BOUND_DEPENDS_ON_R_WHILE_CALLED_FIXED_LOCALITY`;
- `ONE_FIXED_M_RESULT_GENERALIZED_TO_ALL_FIXED_M`.

## 12. Required artifacts

Return at least:

- `R056_REPORT.md`
- `R056_LOCALITY_MODEL.json`
- `R056_SHELL_ESCAPE_PROTOCOL.json`
- `R056_COMPUTATION_REGISTRY.json`
- `R056_MULTI_REPLACEMENT_IDENTITY.json`
- `R056_SHELL_ESCAPE_ATLAS.json`
- `R056_LOCALITY_SCALING_ATLAS.json`
- `R056_THEOREM_COUNTEREXAMPLE_LEDGER.json`
- `R056_HOLDOUT_RESULTS.json`
- `R056_ADVERSARIAL_TEST_RESULTS.json`
- `R056_EXACT_CHECK_RESULTS.json`
- `R056_ARTIFACT_MANIFEST.json`
- exact checker/tests and the minimal executable search implementation.

Freeze and return, before heavy computation:

- `R056_LOCALITY_MODEL_SHA256`
- `R056_SHELL_ESCAPE_PROTOCOL_SHA256`
- `R056_COMPUTATION_REGISTRY_SHA256`

Freeze before strict holdout:

- `R056_THEOREM_COUNTEREXAMPLE_LEDGER_SHA256`

Freeze at final checkpoint:

- `R056_ARTIFACT_MANIFEST_SHA256`

## 13. Interpretation boundary

A positive obstruction theorem means only:

> Under the declared fixed-N triangular-lattice quadratic gravity energy, any strict-descent rearrangement with fixed bounded moved-cell count and fixed bounded support eventually fails to escape the centered-shell family.

It does not prove that real gravity is quadratic, that the triangular lattice is physical, or that nature requires nonlocal motion.

A counterexample means only that a declared bounded cooperative local class can escape the R055 shell trap. It does not establish global convergence or a unique terminal shape.

The purpose of R056 is to identify the exact locality barrier before the project spends another generation engineering local rules.
