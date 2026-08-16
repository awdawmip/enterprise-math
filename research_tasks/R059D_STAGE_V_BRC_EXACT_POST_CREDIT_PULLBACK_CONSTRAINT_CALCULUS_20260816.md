# R059D Stage V — Exact Post-Credit Pullback Constraint Calculus

Task-ID: `RS-R059D-STAGE-V-BRC-EXACT-POST-CREDIT-PULLBACK-CONSTRAINT-CALCULUS`
Generation: `R059D`
Status: `DRIVER_APPROVED_TASKBOOK`
Date: `2026-08-16`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Researcher-ID: `EM-R059D-9C6B2A`
Owner branch: `research/r059d-stage-v-brc-exact-post-credit-pullback`
Frozen parent: `a9929a5bd666e621cb1bd77adb464df0d35db399`

## 0. Frozen inputs

Stage U is immutable.

Read and obey the current project-level semantics, including:

- `PROJECT_DEFINITION.md`
- `FOUNDATIONAL_LOGIC.md`
- `GEOMETRIC_TOOL_REFOUNDATION_POLICY.md`
- `RELATIONAL_AXIS_CONVENTION.md`
- `THREE_DIMENSIONAL_RELATIONAL_AXIS_CONVENTION.md`

Project mode remains `REFOUND, NOT REJECT`.

Canonical Stage-U selector calculus:

`E(x)=A(x) ∩ Fix_Y(Stab_G(x))`.

Stage V does **not** replace this formula. It investigates the missing internal mechanism: how exact downstream/macroscopic knowledge constructs the feasible set `A(x)` without exhaustive branch scoring.

## 1. Scientific target

Freeze the interpretation:

`POST_CREDIT = EXACT CONSTRAINT PULLBACK / FEASIBILITY REDUCTION`

not scalar reward, probability, branch-count argmax, ML score, Euclidean distance, or nearest rounding.

Given:

- local collapse variables / branch outputs `y`;
- a declared exact forward algebra map `F` from local collapse state to downstream algebraic state;
- independently known exact downstream certificate(s) `Phi(F(y),h)=0`;

post-credit must pull the certificate backward to the local branch fiber:

`A_post(x,h) = { y in A_pre(x,h) : Phi(F(y),h)=0 }`.

For binary completion variables:

`C_i=L_i+G_i b_i`, `b_i^2=b_i`,

substitute into downstream exact relations and reduce them as exact Boolean/multilinear constraints.

The primary positive theorem sought is a typed pullback theorem, not a fitted selector.

## 2. Stage V0 — Formal pullback protocol

Define and freeze:

- branch/collapse fiber `Y_x`;
- pre-credit legality `A_pre(x) subseteq Y_x`;
- exact forward map `F_x:Y_x -> Z` or a declared relational correspondence if nonfunctional;
- downstream exact certificate set `C subseteq Z`;
- post-credit feasible set `A_post=F_x^{-1}(C) ∩ A_pre`.

Prove covariance under declared finite-group actions when `F` and `C` are equivariant/invariant in the typed sense.

Must distinguish:

- certificate known before branch realization;
- candidate-conditioned readout computed only after substituting the branch;
- circular self-certification.

## 3. Stage V1 — Boolean/polynomial exact reduction

For finite binary collapse networks, construct exact symbolic reduction modulo:

`b_i^2-b_i=0`.

Do not enumerate `2^m` assignments as the theorem mechanism.

Allowed exact methods include:

- symbolic substitution;
- multilinear Boolean reduction;
- elimination / exact constraint propagation;
- exact finite differences / Möbius coefficients as diagnostics;
- Gröbner/elimination over an explicitly declared exact ring if useful.

Tiny enumeration may be used only as oracle/regression.

Required classifications:

- `NO_REDUCTION`
- `RELATIVE_CONSTRAINT_ONLY`
- `PARTIAL_FEASIBILITY_REDUCTION`
- `SINGLETON_FEASIBILITY`
- `INCONSISTENT_CERTIFICATE`
- `CIRCULAR_CERTIFICATE_REJECTED`.

## 4. Stage V2 — Replay established controls

At minimum replay:

### A. 2D complementary branch

Recover a case where symmetric supervision leaves `{0,1}` unchanged and a genuinely independent tau-odd exact certificate can reduce to singleton.

### B. 3D three-donor branch

Recover an `S3` case where an independently declared donor relation or upstream exact algebraic equation pulls back to one donor; symmetric `S3` certificate must leave all three or none.

### C. Full D12 straightness

Use the already-frozen rank-one definition only as a downstream exact certificate.

Prove the pullback from rank-one straightness to the next-step fiber is exactly the previous **unoriented axis**:

`A_axis={previous axis}`

while the orientation fiber remains `{+,-}`.

This must reproduce Stage T through the Stage-U filter:

`E_axis=A_axis ∩ Fix(...)`.

### D. Scalar midpoint control

For `L<q<U`, bare completion gives `{L,U}`.

Show explicitly that a one-state local pullback without the Stage-R cross-state axioms does not force the off-midpoint selector.

Then represent the Stage-R midpoint-core package (`reflection equivariance + non-midpoint single-valuedness + order monotonicity`, with legality) as a **family-level exact constraint system** over multiple `q` states and demonstrate how it eliminates non-midpoint counterselectors.

The purpose is to retype Stage-R axioms as cross-state post-credit constraints, not to assume nearest rounding.

## 5. Stage V3 — Local versus family-level credit

This distinction is mandatory.

Prove or refute:

- some BRC choices are identifiable from local exact certificates at one state;
- others, such as scalar midpoint monotonicity, are identifiable only from a family of states / cross-state consistency relations.

Define separate types:

`LOCAL_POST_CREDIT`

and

`FAMILY_POST_CREDIT`.

Do not collapse them into one score.

## 6. Stage V4 — Upward/downward algebraic propagation

Construct at least one finite multi-level example with fine/mid/coarse collapse variables.

Forward/upward algebra maps local collapse values to a macro certificate.

Backward/downward pullback must recover the exact compatible local set.

Prioritize symbolic exact propagation rather than exhaustive global assignment search.

Audit:

- tree/DAG exactness;
- cycle correlation/holonomy if cycles are included;
- information that must be retained so local projections do not create false feasible states.

Do not reintroduce the superseded path-language Stage N.

## 7. Stage V5 — Interaction with stabilizer filtering

For every positive witness calculate separately:

`A_post(x)`

`H_x=Stab_G(x)`

`Fix_Y(H_x)`

`E(x)=A_post(x) ∩ Fix_Y(H_x)`.

Required counterexamples:

1. `A_post` singleton but symmetry-incompatible -> `E=empty`.
2. symmetry fixed set singleton but certificate excludes it -> `E=empty`.
3. symmetry breaking yields multiple fixed outputs and `A_post` full -> `|E|>1`.
4. `A_post` nonsingleton but stabilizer filter makes `E` singleton.
5. `A_post` singleton and stabilizer-compatible -> unique output.

This is required to keep feasibility and equivariance logically distinct.

## 8. Stage V6 — No exhaustive discovery

The task must not claim BRC has been discovered merely because a finite registry was enumerated.

The intended mechanism is structural:

`known exact macro relation`
`-> exact pullback constraint`
`-> feasible-set reduction A`
`-> stabilizer filter`
`-> singleton / multibranch / impossible`.

If the mechanism still requires an arbitrary choice of macro certificate, say so explicitly.

## 9. Required artifacts

At minimum:

- `R059D_STAGE_V_POST_CREDIT_PULLBACK_PROTOCOL.json`
- `R059D_STAGE_V_BOOLEAN_EXACT_REDUCTION_PROTOCOL.json`
- `R059D_STAGE_V_LOCAL_VS_FAMILY_CREDIT_LEDGER.json`
- `R059D_STAGE_V_Z2_REPLAY.json`
- `R059D_STAGE_V_S3_REPLAY.json`
- `R059D_STAGE_V_D12_STRAIGHTNESS_PULLBACK.json`
- `R059D_STAGE_V_SCALAR_MIDPOINT_FAMILY_PULLBACK.json`
- `R059D_STAGE_V_MULTI_LEVEL_UP_DOWN_PULLBACK.json`
- `R059D_STAGE_V_STABILIZER_INTERSECTION_COUNTEREXAMPLES.json`
- `R059D_STAGE_V_TRIVIALITY_LEAKAGE_LEDGER.json`
- deterministic checker source/output
- report
- manifest
- frozen checkpoint.

## 10. Firewalls

Do not use as positive proof:

- arbitrary reward weights;
- probability or physical probability;
- endpoint-count argmax;
- nearest rounding / Euclidean distance;
- hidden coordinate/axis ordering;
- ML fitting;
- random tie-break;
- branch-conditioned readout as its own independent certificate;
- exhaustive assignment search as the theorem mechanism.

## 11. Allowed outcomes

Positive or negative outcomes are both valid. In particular preserve if established:

- `EXACT_POST_CREDIT_PULLBACK_CALCULUS_ESTABLISHED`
- `POST_CREDIT_IS_FEASIBILITY_REDUCTION_NOT_SCALAR_REWARD`
- `LOCAL_AND_FAMILY_POST_CREDIT_ARE_DISTINCT`
- `STRAIGHTNESS_PULLBACK_FORCES_AXIS_NOT_ORIENTATION`
- `MIDPOINT_SELECTOR_REQUIRES_FAMILY_LEVEL_ORDER_CONSTRAINTS`
- `STABILIZER_FILTER_AND_POST_CREDIT_PULLBACK_ARE_COMPLEMENTARY_NOT_REDUNDANT`
- `MACRO_CERTIFICATE_SOURCE_STILL_NOT_IDENTIFIED`
- `UNIVERSAL_BRC_LAW_NOT_ESTABLISHED`.

After all required artifacts and checks:

`STOP_FOR_DRIVER_REVIEW`.
