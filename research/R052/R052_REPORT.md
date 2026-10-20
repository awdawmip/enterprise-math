# R052 Formal Plane Pi Typability, Multiplicity, and Coherence Report

**Researcher-ID:** `EM-R052-7C4A19`  
**Task:** `RS-R052-FORMAL-PLANE-PI-TYPABILITY-MULTIPLICITY-COHERENCE`  
**Taskbook source:** `a7d81f0572c3627a6cc5b1bbf9b8420fdff62263`  
**Foundation packet source:** `b6a34afb213558e974569ef63c19db606b882931`  
**Status:** `PURE_FORMAL_FOUNDATION_RESEARCH / NOT_CANONICAL`

## 1. Isolation and ordering

The required order was respected:

`TYPABILITY -> MULTIPLICITY -> COHERENCE -> IDENTIFICATION`.

No R046-R051 engineering/calibration/quantitative artifact was fetched or used. The host project context did expose prior-route references, so the run records `CONTEXT_CONTAMINATION_RISK` and quarantines that context rather than pretending it was absent. The only mathematical startup inputs used were the R052 foundation packet plus Foundational Logic / Gate V3 as semantic and typing discipline.

The classical Euclidean comparison model was not opened until the signature family, role registry, and theorem/counterexample ledger had all been frozen and hashed.

## 2. Stage A — formal-plane signature family

Seven signatures/families were frozen.

1. `S0_INC2` — rank-two incidence plane. No scalar sort, order, metric, orientation, or refinement is native. Finite projective-plane models are admitted.
2. `S1_OCELL2` — oriented finite-cell 2-plane family. Finite boundary cyclic structure and explicit subdivision are meaningful; no geometric scalar is native.
3. `S2_AFF2` — rank-two affine torsor over an unspecified field. A scalar sort exists, but order, norm, measure, and angle do not.
4. `S3_DIRACT2` — affine direction two-cover with an independent group action. It deliberately allows two separately canonical permutation roles without forcing them equal.
5. `S4_ORDAFF2` — ordered affine ray plane. Positive versus negative rays are definable; there is still no metric or angular scalar normalization.
6. `S5_NVAL2` — norm-and-valuation affine plane. Length and a separate polygon valuation are declared, but no normalization couples them.
7. `S6_TURNCOV2` — an unnormalized algebraic turn-cover extension. The kernel is infinite cyclic, but neither a generator orientation nor a scalar angular period is declared.

No signature assumes `plane = R^2`. Circle, center, radius, equidistance, Euclidean distance/area, radian, and a scalar full-turn normalization are not starting primitives.

**R052_SIGNATURE_FAMILY_SHA256**

`946eb08652b7c505adb9b2e8c1263a7260147962b1b7056d5a890d623fbcd0e2`

## 3. Stage B — typability before value

The first substantive result is negative and structural:

- On `S0_INC2`, a scalar-valued pi-role is not merely unknown; it is not well-typed because there is no scalar codomain.
- `S1_OCELL2` likewise has no native geometric scalar, although finite permutation-valued roles are well-typed.
- `S2_AFF2` has a field sort, but a scalar sort alone does not supply a role predicate selecting a distinguished pi-like scalar.
- `S3_DIRACT2` supports two well-typed, individually unique roles in the same codomain `Sym(ODir)`, yet their equality is not forced.
- `S4_ORDAFF2` canonically supplies the direction half-role as a group/permutation object, while still withholding a scalar angle.
- `S5_NVAL2` types a scalar optimization role in an order completion, but that role depends on valuation normalization and norm geometry.
- `S6_TURNCOV2` types a period-kernel generator predicate, but a raw generator is noncanonical; only the inversion quotient is invariant.

Thus the broad weak-plane class already supports `PI_NOT_WELL_TYPED_ON_WEAK_PLANES` and model-theoretic underdetermination before any attempt to identify a value.

## 4. Stage C — frozen role registry

Five independent constructions were frozen.

- `R1_CELL_HALF_CYCLE`: for an even finite boundary cycle of size `m`, the unique nonidentity involution `s^(m/2)` in the boundary successor group.
- `R2_DIRECTION_DECK`: the unique fixed-point-free deck involution of an exact two-sheet direction cover.
- `R3_GROUP_INVOLUTION_ACTION`: the action permutation of the unique nonidentity involution of the independently declared group `G`.
- `R4_RAW_ISOPERIMETRIC_CUT`: the **unnormalized** infimum of `Per_N(C)^2 / mu(C)` over nondegenerate convex polygons, valued in the order completion `Cut(K)`.
- `R5_TURN_KERNEL_GENERATOR_CLASS`: the inversion-orbit of the two generators of the infinite cyclic kernel of the unnormalized turn cover.

The registry deliberately does not insert a classical scalar normalization. In particular, `R4` freezes the raw isoperimetric invariant rather than a normalized target value, and `R5` refuses to promote either raw kernel generator to a canonical invariant.

**R052_PI_ROLE_REGISTRY_SHA256**

`33cabef583b3847eedae152181de002806b800bd8cdb01c07b595d5a695dfe66`

## 5. Stage D — multiplicity and the minimal coherence package

The crucial same-codomain attack is the pair

`R2_DIRECTION_DECK` versus `R3_GROUP_INVOLUTION_ACTION`.

In frozen `S3_DIRACT2`, both roles exist and are unique, but they can differ. The finite countermodel `M1_S3_ACTION_MOVES_BASE` uses a two-sheet direction cover whose deck map swaps the sheet bit while the unique group involution instead moves the underlying direction.

The minimal additional package relative to `S3` is

`A*_S3_DIRECTION_COHERENCE = {VERTICALITY, FIXED_POINT_FREE}`,

where:

- `VERTICALITY`: `q(rho(z)(d)) = q(d)` for every oriented direction `d`;
- `FIXED_POINT_FREE`: `rho(z)(d) != d` for every `d`.

These two axioms force exact equality pointwise. Every fiber contains exactly `{d, delta_q(d)}`; verticality puts `rho(z)(d)` in that fiber and fixed-point-freeness excludes `d`, leaving only `delta_q(d)`.

The package is irredundant relative to `S3`:

- deleting verticality while keeping fixed-point-freeness is refuted by `M1_S3_ACTION_MOVES_BASE`;
- deleting fixed-point-freeness while keeping verticality is refuted by `M2_S3_VERTICAL_WITH_FIXED_POINTS`.

`S4_ORDAFF2` realizes both conditions automatically: scalar negation keeps the underlying one-dimensional subspace and cannot fix a positive ray.

Other frozen roles are not silently equated. Several comparisons are ill-typed because their codomains differ, and no comparison map was inserted merely to obtain agreement.

## 6. Stage E — finite/refinement program

For any even base boundary size `m0 >= 4`, define a directed system indexed by positive integers `r`:

`B_r = Z/(m0 r)Z`.

When `r | s` and `s = k r`, uniform subdivision embeds old vertices by

`i_(r,s)(j) = k j`.

The internal half-role is

`h_r(j) = j + (m0 r)/2`.

It is exactly natural:

`h_s(i_(r,s)(j)) = i_(r,s)(h_r(j))`.

Therefore the compatible family induces a unique involution on the algebraic direct limit. This is exact stabilization of a group-valued role, **not numerical convergence**.

Unrestricted refinement fails: a four-edge boundary has the role, while subdividing exactly one edge produces a five-edge boundary where the role does not exist. This counterexample is preserved rather than repaired away.

The exact checker used only integer arithmetic and finite permutations. It verified:

- 25 uniform-refinement naturality cases;
- 27 refinement-composition cases;
- odd-cycle nonexistence cases;
- both `A*` deletion witnesses;
- exhaustive vertical-involution behavior for one through six two-element fibers.

The companion unittest suite ran **5 tests, all passing**.

## 7. Frozen theorem/counterexample ledger

The pre-comparison ledger includes, among other results:

- scalar typability obstruction on weak signatures;
- scalar-sort insufficiency on bare affine planes;
- exact even-cycle existence/uniqueness;
- exact two-sheet deck uniqueness;
- an explicit S3 role-separation countermodel;
- the `A*` coherence theorem and both deletion witnesses;
- valuation-scale ambiguity;
- raw turn-kernel generator noncanonicity and quotient uniqueness;
- uniform refinement naturality and direct-limit existence;
- unrestricted refinement failure;
- the global no-go theorem against a universal scalar role on the whole weak-plane family.

**R052_THEOREM_COUNTEREXAMPLE_LEDGER_SHA256**

`4a854ca114ab46e7b828f3eb991be745ac2342c034809566218442926b48ebac`

## 8. Stage F — sealed classical comparison

Only after the three freezes above was the classical Euclidean plane opened as a comparison model.

The frozen roles then admit the following symbolic identifications:

- `R2_DIRECTION_DECK` becomes the standard half-turn class `π mod 2π`.
- `R3_GROUP_INVOLUTION_ACTION`, already forced equal to `R2` under frozen `A*`, has the same symbolic identification.
- `R1_CELL_HALF_CYCLE` maps to a half-turn under the **extra comparison-only** regular equivariant realization of an even cyclic boundary; this realization is not backpropagated into `S1`.
- `R4_RAW_ISOPERIMETRIC_CUT` becomes `J = 4π` for standard Euclidean length and area; the comparison readout `J/4` is therefore `π`. The frozen role itself remains the raw `J`.
- `R5_TURN_KERNEL_GENERATOR_CLASS` maps to the orientation-free full-turn generator class `{+2π,-2π}`.

No decimal expansion of the classical constant was used. The Stage-A signature file, Stage-C role registry, and pre-F theorem ledger have identical SHA-256 values before and after this comparison.

## 9. Final research result

R052 supports the following combination, with no winner selected:

- `PI_NOT_WELL_TYPED_ON_WEAK_PLANES`
- `MULTIPLE_INEQUIVALENT_PI_ROLES_FROZEN`
- `COHERENCE_AXIOMS_FOUND`
- `COHERENCE_NOT_FORCED_UNDER_CURRENT_WEAK_SIGNATURE`
- `FINITE_REFINEMENT_ROLE_LIMIT_FOUND`
- `CLASSICAL_IDENTIFICATION_PROVED_AFTER_FREEZE`

The strongest conceptual conclusion is that “pi” is not one automatically available object of a weak formal plane. Typability comes first; once multiple role objects are well-typed they can remain inequivalent; exact coherence requires additional structure that can be audited by deletion witnesses. Classical symbolic identification is a later interpretation theorem, not a source of the formal definitions.

## 10. Nonclaims

This task does **not** claim:

- a universal scalar pi-role on all plane-like structures;
- that a scalar field alone selects such a role;
- that all five frozen roles are equal;
- that the finite refinement tower numerically converges to a classical decimal;
- that arbitrary refinement is path independent;
- that a raw turn-kernel generator is canonical;
- that the S5 scalar role is independent of norm/valuation normalization;
- that the R052 payload is canonical repository mathematics.

Any modification of the frozen signatures, role definitions, or pre-F theorem statements after the comparison is `NEW_GENERATION_FOR_LATER_TASK`.

## 11. Validation and repository status

Local exact checker:

`python tools/check_r052_finite_refinement.py --output research/R052/R052_EXACT_CHECK_RESULTS.json`

Local tests:

`PYTHONPATH=. python -m unittest tests.test_r052_finite_refinement -v`

Result: `PASS`.

Per repository liveness policy, this ordinary research checkpoint does not query workflow status:

`CI_NOT_REQUIRED_FOR_RESEARCH`.
