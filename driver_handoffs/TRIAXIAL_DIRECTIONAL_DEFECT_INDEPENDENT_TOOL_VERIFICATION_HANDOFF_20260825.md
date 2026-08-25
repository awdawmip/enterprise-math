# Driver Handoff — Independent Verification of Triaxial Directional Defect Calculus

Status: `DRIVER-READY / NOT_DISPATCHABLE_UNTIL DRIVER TASKBOOK REVIEW`
Date: `2026-08-25`
Prepared by: `EM-FREE-C19420 / FREE_AXIOM_DISCOVERY`
User direction: `出任务`

> This file is a Driver-ready handoff, not a dispatchable `research_tasks/*.md` taskbook. Current taskbook governance requires a `RESEARCH_DRIVER` to generate/review/approve the actual taskbook and allocate the runtime Researcher-ID outside the taskbook.

## 1. Recommended task identity

Recommended Task-ID:

`RS-TRIAXIAL-DIRECTIONAL-DEFECT-INDEPENDENT-TOOL-VERIFICATION`

Recommended title:

`Triaxial Directional Defect Calculus — Independent Tool Reconstruction and Cross-Domain Verification`

Recommended kind / priority / leverage:

- kind: `RESEARCH`
- priority: `P1`
- leverage: `HIGH`
- origin_kind: `DIRECT_USER_DIRECTION`
- task_lineage: `NEW_DIRECTION`
- identity_lane: `TDDEF`

Recommended owner branch:

`research/triaxial-directional-defect-independent-tool-verification`

Hard target:

`TRIAXIAL_DIRECTIONAL_DEFECT_CALCULUS_T1_SUBTOOL_INDEPENDENTLY_RECONSTRUCTED_AND_CROSS_DOMAIN_VERIFIED_OR_NARROWED_OR_REJECTED`

## 2. Mother question

Does the proposed `TRIAXIAL_DIRECTIONAL_DEFECT_CALCULUS` constitute a genuine reusable `GLOBAL_SUBTOOL` extension of Enterprise toolbox family `T1_SCALE_ENUMERATION_VALUATION`, rather than merely a tomography-specific theorem package or a renamed instance of existing finite-difference machinery?

The decision must be based on an independent proof/checker reconstruction and successful reuse of the same typed operator interface in at least two mathematically distinct domains.

## 3. Independence boundary

This task is an independent implementation / proof replication, not an independent candidate-discovery task.

Before mathematical work, create and push an execution stamp on the owner branch:

`evidence/triaxial_directional_defect_execution_stamp.json`

The stamp must record at minimum:

- resolved runtime `researcher_id`;
- `task_id`;
- `phase = "STARTED_BEFORE_WITHHELD_DERIVATIONS"`;
- `verification_verdict = null`;
- owner branch;
- start timestamp.

Only after the remote stamp commit is confirmed may Phase A mathematics begin.

### Phase A allowed inputs

Use only:

1. the approved taskbook generated from this handoff;
2. `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`;
3. `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md` only where arbitrary-point min-zero decode / translation semantics are required;
4. standard mathematics / standard library code written independently by the researcher.

The taskbook itself may state the claims/API targets below, but must not include source proofs or source checker code.

### Withheld until the independent return is frozen

Do not read or use:

- GLOBAL_KNOWLEDGE journals authored by `EM-FREE-C19420` concerning triaxial tomography, ghost kernels, chirality augmentation, or tool-upgrade validation;
- this originating conversation transcript;
- any implementation/checker produced by `EM-FREE-C19420` for this direction;
- downstream Driver/tool-steward comparison or integration material;
- any future source module implementing the candidate tool;
- source proof derivations for the candidate claims.

After the independent mathematical return and checker are frozen, Phase B may read current toolbox/method inventories for dedup/integration classification.

## 4. Frozen candidate interface to reconstruct

Fix a declared 120-degree frame

`F=(S, rho S, rho^2 S)`

with commuting endpoint translation operators `tau_1,tau_2,tau_3` on the declared finite carrier/domain.

Independently reconstruct and type-check the operator ladder:

`Delta_i = tau_i - I`

`H_ij = Delta_i Delta_j`

`G = Delta_1 Delta_2 Delta_3`

The implementation may choose names, but the return must expose equivalents of the following semantic APIs:

- `DECLARE_FRAME`
- `DIFF1`
- `RHOMBUS2`
- `TRIPLE_DEFECT`
- `XRAY_KERNEL_CERT`
- `FRAME_WIDTH`
- `MULTIFRAME_UNIQUENESS`
- `EXPOSED_AUGMENT`
- `CHIRALITY_AUGMENT`
- `GRAM_FACTOR`

No API may silently identify carrier endpoint equality with native trace identity.

## 5. Required independent mathematical results

### A. Frame covariance and orientation

Prove or refute, under exact stated hypotheses:

1. cyclic covariance/invariance of the triple defect under the declared `rho` action;
2. simultaneous frame reversal changes the triple defect sign;
3. the result is well typed as a triaxial orientation/chirality object rather than a generic coordinate-free scalar.

Any sign convention difference is acceptable if stated consistently and transported through all tests.

### B. Second-to-third defect bridge

For the three cyclic rhombus/mixed-second-difference operators, prove or refute the common complementary-direction identity

`Delta_1 H_23 = Delta_2 H_31 = Delta_3 H_12 = G`

up to the implementation's fixed translation/sign convention.

This result must be reused in the Hive/rhombus test below, not proved and then left application-local.

### C. Endpoint six-point collapse versus trace cube

Expand the abstract product `(tau_1-I)(tau_2-I)(tau_3-I)` as an eight-state signed cube.

Under the declared endpoint carrier closure of the three frame directions, classify exactly which endpoint terms coalesce/cancel and derive or refute the six-point switching stencil.

The return must explicitly preserve the semantic distinction:

`ENDPOINT_COALESCENCE != TRACE_IDENTITY_COALESCENCE`.

### D. Native hex-box tomography kernel

For

`B_R = {(A,B,C) in N_0^3 : min(A,B,C)=0, max(A,B,C)<=R}`,

construct the three-direction X-ray/line-sum operator for one primitive frame and for finite sets of pairwise distinct frame orbits.

Independently prove or refute an exact kernel certificate of the form

`ker X_F(B_R) = P_F K^{B_{R-W}}`

with

`W = sum_{S in F} w(S)`

and the appropriate independently derived definition of `w(S)`.

Do not assume in advance that `w(S)=max(A,B,C)`; derive the support erosion / frame-width quantity from the independent proof and then compare.

The return must determine whether the consequences

`dim ker X_F(B_R)=|B_{R-W}|`

and

`W>R iff X_F is injective`

are true, false, or require narrowing.

A finite-rank table alone is not a proof.

### E. Primitive frame census

Determine independently the number of primitive frame orbits at exact width `w`.

Test the proposed Euler-phi law rather than assuming it. If the law holds, give an explicit orbit parameterization and proof; if not, provide the first counterexample.

### F. Minimal ambiguity-killing augmentation

Independently analyze two augmentation modes.

1. Adjoint/chirality mode: `Omega = G^* f`.
   - determine the coefficient domains/characteristics on which it is injective on the ghost space;
   - prove/refute the factorization of `G^*G` into the three directional Laplacians;
   - identify small-characteristic failures exactly.

2. Exposed-vertex point-sample mode.
   - independently construct an augmentation using one point sample per ghost-amplitude degree of freedom;
   - prove or refute a triangular/unimodular (`det = +/-1`) certificate;
   - determine the weakest coefficient ring assumptions.

The task must decide whether this augmentation is information-theoretically minimal among linear scalar augmentations.

### G. No finite-support translation-invariant deghosting

Determine whether `G` admits a finite-support translation-invariant convolutional left inverse on the infinite translation carrier / Laurent group-ring model.

Return a proof or counterexample and state the consequence for reconstruction architecture.

## 6. Cross-domain reuse gates

### Domain 1 — Triaxial discrete tomography

Required. The tool must produce exact kernel / uniqueness / augmentation certificates on the native hex boxes.

### Domain 2 — Hive / rhombus discrete convexity

Required. Independently implement the three rhombus second-difference/Hessian orientations on a triangular/120-degree frame and demonstrate that the same `RHOMBUS2` + `TRIPLE_DEFECT` interface measures the complementary-direction variation of rhombus defects.

This gate is failed if the Hive regression requires a separate unrelated operator implementation merely sharing notation.

At minimum include:

- three rhombus orientations;
- cyclic covariance;
- a nontrivial test field with nonzero second and third defects;
- an affine/separable field regression with the expected vanishing pattern;
- explicit sign/translation convention reconciliation.

### Domain 3 — Y-Delta / three-port electrical response

Negative-boundary test, not a required supported domain.

Independently determine whether general Y-Delta boundary-response equivalence can be represented inside the fixed linear shift/difference operator interface.

Expected possibilities:

- prove it is out of scope because Schur-complement/rational nonlinear operations are essential; or
- exhibit a genuine encoding that contradicts the proposed boundary.

Do not broaden the tool merely to force this domain to fit.

## 7. Executable deliverables

The owner branch must contain at least:

1. an independent implementation candidate, recommended path:
   `src/enterprise_math/triaxial_directional_defect.py`;
2. exact regression tests, recommended path:
   `tests/test_triaxial_directional_defect.py`;
3. an independent checker or certificate generator sufficient to reproduce theorem-critical finite witnesses without depending on the originating researcher's code;
4. a frozen research return:
   `research_returns/TRIAXIAL_DIRECTIONAL_DEFECT_INDEPENDENT_TOOL_VERIFICATION_RETURN_20260825.md`;
5. the execution stamp required above.

Implementation must not hard-code expected rank/kernel tables as proof substitutes.

Run the repository's applicable test/build checks required by inherited policy; additionally run the new test file directly and report exact commands/results in the return.

## 8. Required finite regressions

Finite computation is validation evidence, not the proof itself.

At minimum independently test:

- one-frame native hex boxes through `R>=8`;
- multi-frame combinations with at least three distinct width patterns and at least one `W=R`, one `W<R`, and one `W>R` case;
- coefficient characteristics `2,3,5,7` plus characteristic zero/rational arithmetic where applicable;
- Euler-phi frame census through at least `w=30` if that theorem survives;
- exposed-augmentation rank/determinant certificates on several one-frame and multi-frame cases;
- Hive/rhombus second-to-third-defect identities on independent nontrivial fields;
- deliberate negative regressions that violate commuting-frame or support/domain hypotheses.

## 9. Phase B tool dedup / integration classification

Only after the independent mathematical return and checker are frozen, read current:

- `enterprise_toolbox_registry.json`;
- `research_method_inventory.json`;
- the relevant T1 finite-difference surfaces;
- relevant T7 orientation/symmetry and T10 Laplacian surfaces as needed.

Then classify the candidate as exactly one of:

1. `ACCEPT_T1_TRIAXIAL_DIRECTIONAL_DEFECT_GLOBAL_SUBTOOL`
2. `ACCEPT_AS_DOMAIN_OPERATOR_ONLY`
3. `NEEDS_NARROWER_TOOL_INTERFACE`
4. `REJECT_TOOL_UPGRADE`

The verdict must explicitly answer:

- what is genuinely reusable beyond existing T1 mixed finite differences;
- which capabilities are composition with T7/T10 rather than owned by this subtool;
- whether tomography and Hive are truly two independent reuse domains;
- whether any theorem/API should be narrowed by field/domain/commutativity assumptions;
- whether the proposed API surface is minimal or overbuilt.

## 10. PASS / KILL criteria

### PASS for `ACCEPT_T1_TRIAXIAL_DIRECTIONAL_DEFECT_GLOBAL_SUBTOOL`

Requires all of:

- independent proof/checker reconstruction succeeds;
- theorem-critical statements survive at the stated or explicitly narrowed scope;
- one shared typed operator ladder works in both tomography and Hive/rhombus domains;
- at least one exact reusable certificate beyond ordinary mixed-second-difference separability is present;
- explicit failure boundaries are demonstrated, not merely listed;
- no hidden carrier relation is promoted to native trace identity;
- Phase B shows the interface extends rather than duplicates T1;
- production candidate API and tests are coherent enough for a later integration task.

### KILL / narrow triggers

Return a narrower/reject verdict if any of the following occurs:

- the multi-frame kernel/width law fails under its claimed hypotheses;
- the Hive domain does not reuse the same core operators;
- the candidate collapses entirely to existing T1 APIs without a reusable new certificate/interface;
- orientation/chirality laws depend on an inadmissible carrier identification;
- exposed augmentation is not minimal/unimodular as claimed and no equally strong replacement survives;
- field/domain restrictions become so severe that only the original tomography example remains;
- the implementation needs Y-Delta-style nonlinear machinery to support its claimed core scope.

## 11. Stop condition

Freeze the return after one of the four verdicts is justified and all theorem-critical checker artifacts are committed/pushed.

Do not perform toolbox-registry integration, canonical promotion, or downstream application expansion in this task. Those require a separate Driver decision after the independent return.

## 12. Driver authoring instructions

To turn this handoff into a dispatchable taskbook, the Driver should generate a fresh V6 taskbook with the recommended metadata above, then copy only the task-local sections needed for execution, approve it with current policy digest, run the dispatch audit, create the owner branch if needed, and allocate a fresh runtime Researcher-ID in the separate dispatch envelope.

No proof text or originating-journal content should be added to the taskbook before independent freeze.
