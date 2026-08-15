# R059D Stage N REISSUE — BRC Pure-Algebra Coupled Complementary Collapse / Three-Axis Transfer / Post-Credit Foundations

Task-ID: `RS-R059D-STAGE-N-BRC-PURE-ALGEBRA-COUPLED-COMPLEMENTARY-COLLAPSE`
Generation: `R059D`
Status: `DRIVER_APPROVED_REISSUE_TASKBOOK`
Date: `2026-08-16`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Researcher-ID: `EM-R059D-9C6B2A`
Owner branch: `research/r059d-stage-n-brc-pure-algebra-complementary-collapse`
Frozen parent: `d6cfcb3435deac50901581cd4fa82e6b3cf588d3`

## 0. Supersede disposition

The earlier Stage-N task:

`research_tasks/R059D_STAGE_N_BRC6_PATH_LANGUAGE_WELL_POSEDNESS_GENERATING_CARRIER_20260815.md`

is `SUPERSEDED_BEFORE_EXECUTION`.

Its branch

`research/r059d-stage-n-brc6-path-language-generating-carrier`

remained exactly at the Stage-M frozen head and produced no Stage-N result. Do not execute, consume, extend, or reinterpret that path-language task as the current route.

Current Stage N starts again from the same frozen Stage-M head:

`d6cfcb3435deac50901581cd4fa82e6b3cf588d3`.

All Stage J/K/L/M artifacts remain immutable.

## 1. Governing project semantics

Read and obey:

- `PROJECT_DEFINITION.md`
- `PROJECT_DEFINITION.zh-CN.md`
- `project_definition.json`
- `FOUNDATIONAL_LOGIC.md`
- `foundational_logic.json`
- `native_semantics_admissibility.json`
- `GEOMETRIC_TOOL_REFOUNDATION_POLICY.md`
- `research_notes/BRC_PURE_ALGEBRA_COLLAPSE_CREDIT_COORDINATE_TRANSFER_ANCHOR_20260816.md`

Project mode remains:

`REFOUND, NOT REJECT`.

The present task is foundation-facing. Classical geometry may later be used as calibration/evidence, but current positive claims must be derived from the declared algebraic substrate rather than copied from Euclidean coordinates, metric, angle, trigonometry, or nearest-rounding intuition.

## 2. Scientific correction and core question

BRC collapse is to be treated first as a **pure algebraic up/down collapse**, not as path merging or endpoint-count argmax.

Canonical scalar example:

`5 -> 4` versus `5 -> 9`.

For a scalar state `n` between two adjacent completed states `L < n < U`, write:

`G = U-L`

and an upper-collapse bit

`b in {0,1}`, `b^2=b`.

Freeze the generic binary representation:

`C(n;b) = L + G b`.

Thus:

- `b=0` gives lower/down collapse `L`;
- `b=1` gives upper/up collapse `U`.

For perfect-power specialization:

if `k^p < n < (k+1)^p`, then

`L=k^p`, `U=(k+1)^p`.

For `p=2,n=5`:

`C_2(5;b)=4+5b`.

The present task does **not** assume a local rule for `b`. Its purpose is to identify what exact algebraic constraints can couple multiple collapse bits and whether the current six local transfer vectors arise from such coupled complementary collapse.

## 3. Signed collapse residue

For `n=L+d`, define the exact signed collapse residue:

`rho(n,b)=n-C(n;b)=d-Gb`.

Do not rank collapse choices by `|rho|` unless a later task independently establishes that as a law. In particular, nearest rounding is forbidden as an implicit selector premise.

Stage N must preserve the signed residue because later post-credit may depend on cancellation, reinforcement, or higher-order coupling among multiple residues.

Freeze and test:

`SCALAR_COLLAPSE_BIT_ALGEBRA`

with at least:

- arbitrary adjacent integer endpoints `L<U`;
- perfect-power examples including `5 between 4 and 9`;
- non-midpoint states;
- exact midpoint states when the precision carrier admits them;
- negative intervals and sign symmetry controls;
- translated intervals `L+c,U+c`;
- scaled integer-gap controls where meaningful.

## 4. Current two-dimensional three-axis carrier

Consume from Stage M only the already-frozen algebraic carrier:

`Lambda = {(a,b,c) in Z^3 : a+b+c=0}`

with

`u=(1,-1,0)`

`v=(0,1,-1)`

`w=(-1,0,1)`

and

`u+v+w=0`.

For positions, use the affine sheet:

`Pi_K = {(x,y,z) : x+y+z=K}`.

Treat `K` as an affine gauge/constant-sheet label. A transition displacement belongs to `Lambda`.

Do not interpret the three coordinates as three independent spatial dimensions. The carrier has two degrees of freedom.

## 5. The `(100,0,0) -> y+` test is mandatory

Start from:

`X=(100,0,0)` in `Pi_100`.

Declare a target-coordinate unit increment:

`Delta y = +1`.

Exact sheet preservation requires:

`Delta x + Delta z = -1`.

Stage N must distinguish three logically different constructions.

### N5-A Direct integer endpoint construction

Without using a fractional midpoint, define the candidate integer compensation set under explicitly declared local endpoint assumptions.

If the transverse completed-state choices are `{0,-1}`, solve exactly:

`Delta x in {0,-1}`

`Delta z in {0,-1}`

`Delta x + Delta z = -1`.

The expected solution set is:

`(-1,+1,0)`

and

`(0,+1,-1)`.

But do not simply assert this. Store the exact assumption set that makes `{0,-1}` the relevant adjacent completed states.

### N5-B Symmetric unresolved pre-collapse construction

Introduce transverse exchange symmetry only as an explicit hypothesis:

`x <-> z` before collapse.

Let the unresolved compensation be `(a,+1,a)`.

From sheet preservation derive:

`2a+1=0`.

Hence:

`a=-1/2`.

Freeze this only with its semantic status:

`SYMMETRIC_PRECOLLAPSE_HALF_STATE_DERIVED_UNDER_EXCHANGE_SYMMETRY`.

Do **not** promote `-1/2` to an unconditional native packet quantity. It is a pre-collapse precision/algebra carrier value under the declared symmetry hypothesis.

### N5-C Equivalence bridge

At integer endpoint precision, the adjacent completed states around `-1/2` are `-1` and `0`.

Introduce separate upper-collapse bits:

`b_x,b_z in {0,1}`

with

`Delta x = -1 + b_x`

`Delta z = -1 + b_z`.

Sheet preservation requires:

`(-1+b_x)+1+(-1+b_z)=0`

therefore:

`b_x+b_z=1`.

Prove exact equivalence between:

1. the direct integer solution set;
2. the symmetric half-state plus two scalar up/down collapses constrained by `b_x+b_z=1`.

If they are not exactly equivalent under the frozen assumptions, report the mismatch.

## 6. Complementary-collapse bit parameterization

From

`b_x+b_z=1`

reduce the two bits to one free bit without losing the meaning of the original scalar upper-collapse bits.

One admissible parameterization is:

`b_z=b`

`b_x=1-b`.

Then:

`Delta_y^+(b)=(-b,+1,-(1-b))`.

Verify:

- `b=1 -> (-1,+1,0)`;
- `b=0 -> (0,+1,-1)`;
- coordinate sum is exactly zero for both;
- the two branches are exchanged by `x<->z`.

Do not confuse this reduced `b` with a generic scalar lower-indicator; retain explicit provenance showing which coordinate's upper-collapse bit it represents.

Freeze a positive theorem only if proved:

`COUPLED_COMPLEMENTARY_COLLAPSE_BIT_REDUCTION_ESTABLISHED`.

## 7. General three-axis unit-transfer derivation

Generalize without importing Euclidean angle/distance.

Let `e_x,e_y,e_z` denote coordinate basis labels in the ambient serialization carrier.

An elementary unit transfer from donor coordinate `j` to recipient coordinate `i`, `i!=j`, has displacement:

`e_i-e_j`.

Stage N must determine whether, under the frozen assumptions, the union of all complementary-collapse branches is exactly:

`D_transfer = {e_i-e_j : i != j}`.

This set has six elements.

Then prove or reject exact equivalence with the Stage-M vector set:

`D6={+u,-u,+v,-v,+w,-w}`.

Do not count duplicated descriptions twice. Audit the redundancy between:

- choosing a recipient axis and donor axis;
- choosing a signed increment on a named axis;
- additive inversion.

Required exact classification:

`THREE_AXIS_TRANSFER_SIX_STATE_EMERGENCE`

must be one of:

- `ESTABLISHED_FROM_FROZEN_ASSUMPTIONS`;
- `ESTABLISHED_ONLY_WITH_ADDITIONAL_MINIMALITY_ASSUMPTION`;
- `NONUNIQUE_MORE_BRANCHES_EXIST`;
- `NOT_ESTABLISHED`.

## 8. Assumption necessity audit — mandatory

This is one of the most important parts of Stage N.

Do not hide which assumptions are doing the work.

Audit at least the following independently:

A1. rank-two affine conservation:

`x+y+z=K`.

A2. unit recipient increment:

`Delta_i=+1` for an elementary positive transfer event.

A3. integer completed-state endpoints.

A4. transverse exchange symmetry before collapse.

A5. adjacent endpoint pair around the symmetric unresolved value.

A6. no extra simultaneous multi-unit compensation in a single elementary event.

A7. collapse endpoints are completed states, not arbitrary fractional outputs.

For each assumption:

- remove or weaken it;
- compute the exact enlarged solution family;
- give a tiny counterexample if the two-branch result fails;
- state whether the assumption is logically necessary, only sufficient, or redundant given the others.

The task must explicitly answer:

`WHY_TWO_BRANCHES_NOT_THREE_OR_INFINITE?`

and

`WHY_SIX_TRANSFER_STATES_NOT_MORE?`

No positive native claim is accepted without this audit.

## 9. General coupled-collapse algebra

Abstract beyond the three-axis example.

For `m` local algebraic states, write:

`C_i = L_i + G_i b_i`

with

`b_i^2-b_i=0`.

Let exact higher-level algebraic constraints be:

`F_r(C_1,...,C_m)=0`, `r=1,...,R`.

Substitute collapse forms to obtain Boolean-polynomial constraints:

`P_r(b_1,...,b_m)=0`.

Define the admissible BRC bit set:

`B(F) = {b in {0,1}^m : P_r(b)=0 for all r}`.

This is a set-valued algebraic object. Do not force a unique bit assignment when the exact constraints leave multiple assignments.

Classify:

- `UNIQUE_COLLAPSE_ASSIGNMENT` if `|B(F)|=1`;
- `MULTIBRANCH_ADMISSIBLE` if `|B(F)|>1`;
- `INCONSISTENT_CONSTRAINT_SET` if `B(F)=empty`.

The three-axis complementary pair should appear as the first nontrivial exact example.

## 10. Post-credit algebra — prototype only, no reward weights

Stage N must connect the above to the current BRC post-credit hypothesis without pretending the full BRC law is solved.

For a known higher-level relation represented by exact residual polynomial:

`R(b_1,...,b_m)`

define exact discrete difference operators:

`Delta_i R = R(...,b_i=1,...) - R(...,b_i=0,...)`.

Also define higher-order interactions:

`Delta_i Delta_j R`, etc.

Reduce Boolean powers using:

`b_i^2=b_i`.

Store the multilinear/Mobius-form coefficient structure exactly.

The purpose is to distinguish:

- single-bit credit;
- pairwise complementary credit;
- higher-order cooperative credit;
- constraints that leave a symmetry-related branch pair unresolved.

Do not introduce arbitrary scalar reward weights.

Do not use machine-learning fitting as the positive proof method.

Do not enumerate `2^m` states for large `m` as the intended mechanism. Tiny enumeration is allowed only as an oracle/checker for symbolic algebra.

Priority symbolic methods:

- Boolean polynomial reduction;
- exact substitution;
- elimination;
- Gröbner-style or equivalent exact finite algebra where useful;
- symmetry quotienting;
- sparse interaction factorization.

## 11. The `5 -> 4 or 9` bridge is mandatory

The task must explicitly connect the scalar collapse bit and the three-axis coupled branch bit.

For `5` between `4` and `9`:

`C_2(5;b)=4+5b`.

For transverse half-state `-1/2` between `-1` and `0`:

`C_half(b)=-1+b`.

Explain exactly what is structurally common:

- two adjacent completed states;
- one binary up/down bit;
- signed residue;
- downstream exact constraints can couple multiple bits.

Also explain what is different:

- the square-collapse gap is 5;
- the transverse compensation gap is 1;
- the three-axis conservation law couples two local bits;
- no claim is yet made that the same local selector function chooses both cases.

The task must not collapse these distinctions.

## 12. Straightness enters only as downstream credit calibration

Consume the current proposed straightness definition only as a downstream certificate candidate:

A set of positions is straight if their displacement vectors generate a rank-one integer submodule.

Do not use straightness to derive the two-branch complementary formula itself.

Only after Sections 5-11 pass may Stage N run a tiny post-credit test asking whether repeated complementary transfer choices can generate rank-one macro position sets and what exact bit constraints straightness adds.

Do not define geometric length or angle here.

Do not use Euclidean distance, norm, dot product, sine, cosine, or nearest-line error as selector premises.

If straightness provides no additional bit identification beyond symmetry/conservation, record that negative result.

## 13. Robustness / covariance tests

All positive formulas must be tested under:

- translation of the affine sheet `K -> K+c`;
- permutation of coordinate names x,y,z;
- global sign/inversion of displacement;
- change of recipient/donor coordinate;
- arbitrary large coordinate backgrounds such as `10^36` with exact arithmetic;
- equivalent serialization of the same Lambda vector.

The complementary-collapse law must not depend on absolute coordinate origin or privileged axis naming.

## 14. Prohibited shortcuts

Hard reject any implementation that:

- chooses the nearer endpoint and calls that BRC;
- imports Euclidean angle/distance to choose a branch;
- treats `(100,1,0)` as a same-sheet point under `x+y+z=100`;
- assumes the half-state is native without stating the exchange-symmetry bridge;
- assumes the six D6 vectors before deriving the transfer branch set in the positive proof path;
- uses Stage-M endpoint-count microgrammar as the current BRC law;
- uses old Stage-N path-language results;
- assigns arbitrary reward weights to known macro laws;
- hides unresolved multiple bit assignments;
- interprets algebraic branch multiplicity as physical probability;
- promotes a calibration success to physical ontology.

## 15. Required tiny deterministic cases

At minimum include exact tables for:

1. `(100,0,0)` with `y+1`;
2. all cyclic coordinate permutations of case 1;
3. all inverse moves;
4. translated backgrounds `(K,0,0)` for several K including very large integer K;
5. scalar `5 -> 4/9`;
6. at least one non-midpoint scalar collapse;
7. a pair of coupled scalar collapse bits with a linear conservation constraint;
8. a coupled system whose exact constraint leaves two solutions;
9. a coupled system with a unique solution;
10. an inconsistent coupled system;
11. removal of each assumption A1-A7;
12. a straightness downstream-credit toy case after the pure algebra gate passes.

All tiny cases must be reproducible with exact arithmetic.

## 16. Theorem / result targets

Seek, but do not force, the following.

### N-T1 Scalar binary collapse normal form

`C=L+Gb`, `b^2=b`, with signed residue `rho=n-C`.

### N-T2 Symmetric transverse half-state

Under sheet conservation and exchange symmetry, `(+1)` recipient change induces equal transverse unresolved compensation `-1/2,-1/2`.

### N-T3 Coupled complementary collapse

Integer endpoint collapse of the two transverse half-states plus sheet conservation yields complementary upper bits:

`b_x+b_z=1`.

### N-T4 Six-state unit-transfer emergence

The union of exact coupled branches across three axes equals `{e_i-e_j:i!=j}` and matches D6.

### N-T5 Assumption-minimality theorem

Identify the weakest frozen assumption set under which N-T3/N-T4 remain true.

### N-T6 Constraint-induced BRC set

`B(F)` is the exact set of collapse-bit assignments compatible with a declared family of higher-level algebraic constraints.

### N-T7 Post-credit finite-difference decomposition

Exact macro residuals admit discrete single-bit and higher-order interaction credit terms without arbitrary reward weighting.

If any target fails, preserve the failure and weakest surviving statement.

## 17. Required artifacts

At minimum freeze:

1. `R059D_STAGE_N_SCALAR_UP_DOWN_COLLAPSE_PROTOCOL.json`
2. `R059D_STAGE_N_SIGNED_COLLAPSE_RESIDUE_PROTOCOL.json`
3. `R059D_STAGE_N_AFFINE_THREE_AXIS_SHEET_PROTOCOL.json`
4. `R059D_STAGE_N_SYMMETRIC_PRECOLLAPSE_HALF_STATE_DERIVATION.json`
5. `R059D_STAGE_N_COMPLEMENTARY_COLLAPSE_BIT_PROTOCOL.json`
6. `R059D_STAGE_N_DIRECT_INTEGER_VS_HALF_STATE_EQUIVALENCE.json`
7. `R059D_STAGE_N_D6_TRANSFER_EMERGENCE_AUDIT.json`
8. `R059D_STAGE_N_ASSUMPTION_NECESSITY_LEDGER.json`
9. `R059D_STAGE_N_GENERAL_COUPLED_BOOLEAN_COLLAPSE_ALGEBRA.json`
10. `R059D_STAGE_N_POST_CREDIT_FINITE_DIFFERENCE_ALGEBRA.json`
11. `R059D_STAGE_N_SCALAR_TO_VECTOR_COLLAPSE_BRIDGE.json`
12. `R059D_STAGE_N_STRAIGHTNESS_DOWNSTREAM_CREDIT_TOY.json`
13. `R059D_STAGE_N_LARGE_BACKGROUND_COVARIANCE_REGISTRY.json`
14. `R059D_STAGE_N_TRIVIALITY_TARGET_LEAKAGE_LEDGER.json`
15. deterministic checker source + output
16. report
17. artifact manifest
18. frozen checkpoint

## 18. Checker gates

The deterministic checker must hard-reject:

- non-Boolean collapse bits;
- failure of `b^2=b` in symbolic reductions;
- branch endpoint outside declared completed states;
- violation of affine sheet conservation;
- failure of complementary relation where claimed;
- D6 result hard-coded rather than derived in test path;
- axis-name dependence;
- absolute-coordinate dependence;
- nearest-rounding selector used as premise;
- Euclidean metric/angle/trig leakage;
- path-language Stage-N consumption;
- arbitrary reward weights;
- floating-point equality in exact theorem checks;
- physical-probability language from algebraic branch count.

## 19. Interpretation firewall

May freeze only if proved:

- `PURE_ALGEBRA_BINARY_COLLAPSE_NORMAL_FORM_ESTABLISHED`
- `SYMMETRIC_PRECOLLAPSE_HALF_STATE_DERIVED_UNDER_EXCHANGE_SYMMETRY`
- `COUPLED_COMPLEMENTARY_COLLAPSE_BIT_REDUCTION_ESTABLISHED`
- `THREE_AXIS_TRANSFER_SIX_STATE_EMERGENCE_ESTABLISHED`
- `BRC_CONSTRAINT_SOLUTION_SET_ALGEBRA_ESTABLISHED`
- `POST_CREDIT_DISCRETE_DIFFERENCE_ALGEBRA_ESTABLISHED`

Continue unless separately proved:

- `BRC_UNIQUE_INTERNAL_SELECTOR = NOT_ESTABLISHED`
- `BRC_PHYSICAL_DIRECTION_LAW = NOT_ESTABLISHED`
- `PHYSICAL_PROBABILITY_FROM_BRC = NOT_ESTABLISHED`
- `PHYSICAL_LENGTH_FROM_THREE_AXIS_TRANSFER = NOT_ESTABLISHED`
- `PHYSICAL_ANGLE_FROM_THREE_AXIS_TRANSFER = NOT_ESTABLISHED`
- `QUANTUM_BRIDGE = NOT_ESTABLISHED`

## 20. Scientific success criterion

Stage N is a PASS if it does at least one of the following with exact proof/checker support:

1. derives the complementary two-branch collapse structure from an explicit weak assumption set and shows that the six D6 transfer states emerge rather than being assumed;
2. proves that additional hidden assumptions are required and identifies them exactly;
3. proves a structural obstruction showing the proposed half-state/complementary-bit route cannot uniquely account for D6.

The preferred positive outcome is not merely reproducing six vectors. It is exposing the internal algebraic mechanism by which a pair of scalar up/down collapses becomes one constrained complementary branch bit.

## 21. Stop condition

After all artifacts, checker, report, manifest and frozen checkpoint are complete:

`STOP_FOR_DRIVER_REVIEW`.

Do not open a subsequent stage automatically.
