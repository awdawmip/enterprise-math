<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-TRIAXIAL-DIRECTIONAL-DEFECT-INDEPENDENT-TOOL-VERIFICATION",
  "title": "Triaxial Directional Defect Calculus — Independent Tool Reconstruction and Cross-Domain Verification",
  "kind": "RESEARCH",
  "owner": "research/triaxial-directional-defect-independent-tool-verification",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "TRIAXIAL_DIRECTIONAL_DEFECT_CALCULUS_T1_SUBTOOL_INDEPENDENTLY_RECONSTRUCTED_AND_CROSS_DOMAIN_VERIFIED_OR_NARROWED_OR_REJECTED",
  "next_action": "Independently reconstruct the declared 120-degree directional-difference interface from the whitelisted plane semantics, prove or refute its tomography and hive/rhombus certificates, implement an independent checker/API surface, freeze a verdict, then perform Phase-B dedup against the current toolbox before any integration recommendation.",
  "dependencies": [
    "definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md",
    "definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md"
  ],
  "source_refs": [
    "definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md@main",
    "definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md@main"
  ],
  "evidence_status": "DRIVER_APPROVED_READY_FOR_INDEPENDENT_TOOL_RECONSTRUCTION",
  "last_progress_ref": "driver_handoffs/TRIAXIAL_DIRECTIONAL_DEFECT_INDEPENDENT_TOOL_VERIFICATION_HANDOFF_20260825.md@d79fbdd0d8f4eaa02f8fb7947caeeb63464f1674",
  "last_progress_at": "2026-08-25T18:57:00+08:00",
  "hard_block": null,
  "tags": [
    "triaxial",
    "tool-verification",
    "independent-reconstruction",
    "tomography",
    "hive",
    "finite-difference",
    "T1-extension"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "TDDEF",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": [
      {
        "conflict_id": "TB-REMOTE-RUNTIME",
        "scope": "single pre-math independence execution stamp on the declared owner branch",
        "reason": "The replication must establish a durable timestamped boundary before withheld derivations become visible.",
        "replacement_behavior": "Allow exactly one pre-math commit and push of evidence/triaxial_directional_defect_execution_stamp.json and one confirmation of that remote commit; no other remote preflight or status waiting is required by this task.",
        "expires_when": "the execution-stamp remote commit is confirmed before Phase A mathematics begins"
      }
    ]
  }
}
-->

# Triaxial Directional Defect Calculus — Independent Tool Reconstruction and Cross-Domain Verification

Status: `READY / DRIVER_APPROVED / INDEPENDENT TOOL VERIFICATION`

Task-ID:

`RS-TRIAXIAL-DIRECTIONAL-DEFECT-INDEPENDENT-TOOL-VERIFICATION`

Owner branch:

`research/triaxial-directional-defect-independent-tool-verification`

Hard target:

`TRIAXIAL_DIRECTIONAL_DEFECT_CALCULUS_T1_SUBTOOL_INDEPENDENTLY_RECONSTRUCTED_AND_CROSS_DOMAIN_VERIFIED_OR_NARROWED_OR_REJECTED`

## 0. Mother question

Does the proposed `TRIAXIAL_DIRECTIONAL_DEFECT_CALCULUS` constitute a genuine reusable `GLOBAL_SUBTOOL` extension of `T1_SCALE_ENUMERATION_VALUATION`, rather than merely a tomography-specific theorem package or a renamed instance of existing finite-difference machinery?

The decision must be based on an independent proof/checker reconstruction and reuse of one typed operator interface in at least two mathematically distinct domains.

## 1. Independence boundary and Phase A whitelist

Before reading mathematical sources beyond this taskbook, create, commit and push:

`evidence/triaxial_directional_defect_execution_stamp.json`

with at least:

- resolved runtime `researcher_id`;
- this `task_id`;
- `phase = "STARTED_BEFORE_WITHHELD_DERIVATIONS"`;
- `verification_verdict = null`;
- owner branch;
- start timestamp.

Confirm the remote stamp commit before Phase A mathematics.

During Phase A, use only:

1. this approved taskbook;
2. `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`;
3. `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md` only where translated min-zero decoding is actually required;
4. standard mathematics and independently written standard-library code.

Until the Phase A return and independent checker are frozen, do not read:

- originating free-research journals or conversation material about triaxial tomography, ghost kernels, chirality augmentation or tool validation;
- the Driver handoff that generated this taskbook;
- source proof derivations or source checker code for the candidate claims;
- any future implementation of this candidate subtool;
- downstream integration or review material.

After the Phase A return/checker freeze, Phase B must inspect the current toolbox/method inventory and executable surface for dedup and ownership classification before making any method-novelty or integration claim.

This is independent implementation/proof replication, not independent candidate discovery. The target interface is visible; its proof is withheld.

## 2. Candidate interface to reconstruct

Fix a declared 120-degree frame

`F=(S, rho S, rho^2 S)`

with commuting endpoint translations `tau_1,tau_2,tau_3` on the declared finite carrier/domain.

Independently reconstruct and type-check:

`Delta_i = tau_i - I`

`H_ij = Delta_i Delta_j`

`G = Delta_1 Delta_2 Delta_3`.

The implementation may choose internal names, but the final interface must expose semantic equivalents of:

- `DECLARE_FRAME`
- `DIFF1`
- `RHOMBUS2`
- `TRIPLE_DEFECT`
- `XRAY_KERNEL_CERT`
- `FRAME_WIDTH`
- `MULTIFRAME_UNIQUENESS`
- `EXPOSED_AUGMENT`
- `CHIRALITY_AUGMENT`
- `GRAM_FACTOR`.

No API may silently identify carrier endpoint equality with native trace identity.

## 3. Required independent mathematical results

### A. Frame covariance and orientation

Prove or refute, under explicit hypotheses:

1. cyclic covariance/invariance of `G` under the declared `rho` action;
2. simultaneous frame reversal changes the sign of `G`;
3. the resulting object is correctly typed as a triaxial orientation/chirality defect rather than a coordinate-free scalar.

A globally consistent alternative sign convention is acceptable.

### B. Second-to-third defect bridge

For the three cyclic rhombus operators, prove or refute

`Delta_1 H_23 = Delta_2 H_31 = Delta_3 H_12 = G`

up to the chosen translation/sign convention.

This exact operator implementation must be reused in the Hive/rhombus regression; a separate lookalike implementation fails the cross-domain gate.

### C. Eight-state cube versus endpoint six-point stencil

Expand `(tau_1-I)(tau_2-I)(tau_3-I)` as an eight-state signed cube.

Under the declared endpoint carrier closure of the three frame directions, classify which endpoint terms coalesce/cancel and independently derive or refute a six-point switching stencil.

Preserve explicitly:

`ENDPOINT_COALESCENCE != TRACE_IDENTITY_COALESCENCE`.

### D. Native hex-box tomography kernel

For

`B_R={(A,B,C) in N_0^3 : min(A,B,C)=0, max(A,B,C)<=R}`,

construct the three-direction line-sum/X-ray operator for one primitive frame and finite sets of pairwise distinct frame orbits.

Independently prove or refute an exact kernel certificate of the form

`ker X_F(B_R)=P_F K^{B_{R-W}}`

with

`W=sum_{S in F} w(S)`

and an independently derived frame-width quantity `w(S)`.

Do not assume in advance that `w(S)=max(A,B,C)`; derive the support-erosion quantity and compare.

Determine whether

`dim ker X_F(B_R)=|B_{R-W}|`

and

`W>R iff X_F is injective`

hold exactly, require narrowing, or fail.

A finite-rank table alone is not a proof.

### E. Primitive frame census

Determine independently the number of primitive frame orbits at exact width `w`.

Test the proposed Euler-phi law rather than assuming it. If it holds, provide an explicit orbit parameterization and proof; otherwise return the first counterexample.

### F. Minimal ambiguity-killing augmentation

Analyze both modes independently.

**Adjoint/chirality mode**

`Omega=G^* f`.

Determine:

- coefficient domains/characteristics on which it is injective on the ghost space;
- whether `G^*G` factors into the three directional Laplacians;
- exact small-characteristic failures.

**Exposed-vertex point-sample mode**

Construct one point sample per ghost-amplitude degree of freedom and prove or refute a triangular/unimodular (`det=+/-1`) certificate. State the weakest coefficient-ring assumptions.

Decide whether the number of added scalar measurements is information-theoretically minimal among linear augmentations.

### G. No finite-support translation-invariant deghosting

On the infinite translation carrier/Laurent group-ring model, determine whether `G` admits a finite-support translation-invariant convolutional left inverse.

Return a proof or counterexample and the exact reconstruction consequence.

## 4. Cross-domain reuse gates

### Domain 1 — triaxial discrete tomography

Required. Produce exact kernel, uniqueness and ambiguity-killing certificates on the native hex boxes.

### Domain 2 — Hive / rhombus discrete convexity

Required. Independently implement the three rhombus mixed-second-difference/Hessian orientations on a triangular/120-degree frame and demonstrate that the same `RHOMBUS2` plus `TRIPLE_DEFECT` interface measures complementary-direction variation of rhombus defects.

This gate fails if the Hive regression uses an unrelated second implementation that merely shares notation.

### Negative discriminator — three-port Y-Delta response

Test whether the same linear directional-defect interface can represent general three-port star/triangle boundary-response equivalence.

Do not force unification. If rational Schur-complement structure is genuinely outside the interface, record that as a hard boundary rather than widening the tool.

## 5. Independent implementation and regression requirements

Write an independent candidate module and tests on the owner branch. Minimum expected surfaces:

- `src/enterprise_math/triaxial_directional_defect.py` or an equivalently scoped module;
- `tests/test_triaxial_directional_defect.py`;
- exact checker/regression code sufficient to reproduce every machine claim in the return;
- `research_outputs/TRIAXIAL_DIRECTIONAL_DEFECT_INDEPENDENT_TOOL_VERIFICATION_20260825.md`;
- `research_output/evidence/TRIAXIAL_DIRECTIONAL_DEFECT_INDEPENDENT_TOOL_VERIFICATION_MANIFEST_20260825.json`;
- `research_returns/TRIAXIAL_DIRECTIONAL_DEFECT_INDEPENDENT_TOOL_VERIFICATION_RETURN_20260825.md`.

At minimum the regression suite must include:

- base-frame tomography boxes through a nontrivial range of `R`;
- random/mixed multi-frame cases;
- coefficient characteristics `2,3,5,7` plus characteristic zero/rational tests where relevant;
- at least one Hive/rhombus cross-domain regression using the same operators;
- explicit failure/regression cases for every claimed hard boundary.

Finite computation supports but does not replace theorem proof.

## 6. Phase B dedup and method classification

Only after the independent Phase A return/checker is frozen, inspect the current tool registry, method inventory and executable source.

Classify the result as exactly one of:

- `EXTEND_EXISTING_TOOL` under T1;
- `REUSE_EXISTING_TOOL` / duplicate specialization;
- `DOMAIN_OPERATOR_ONLY`;
- `CAPABILITY_GAP_CONFIRMED` for a different interface;
- `NO_TOOL_PAYLOAD` if the mathematics is sound but not reusable as a tool.

If the accepted result is an extension, identify which existing tools remain owners of symmetry, Laplacian solving, quotient/gluing or other generic mechanisms rather than reimplementing them inside this module.

## 7. Final verdict

Return exactly one primary verdict:

- `ACCEPT_T1_TRIAXIAL_DIRECTIONAL_DEFECT_GLOBAL_SUBTOOL`;
- `ACCEPT_AS_DOMAIN_OPERATOR_ONLY`;
- `NEEDS_NARROWER_TOOL_INTERFACE`;
- `REJECT_TOOL_UPGRADE`.

`ACCEPT_T1_TRIAXIAL_DIRECTIONAL_DEFECT_GLOBAL_SUBTOOL` requires all of:

1. independently reconstructed mathematics, not copied source derivation;
2. exact reusable I/O and checker surface;
3. proved structural laws/certificates;
4. explicit coefficient/domain/finiteness/trace boundaries;
5. successful reuse in tomography and Hive/rhombus with the same operators;
6. Phase-B dedup establishing genuine T1 extension value rather than duplicate naming;
7. no claim that Y-Delta/general rational three-port response is covered unless independently proved.

## 8. Stop condition

Stop when one primary verdict is justified and the return includes:

- theorem/proof-status ledger;
- checker/regression manifest;
- tomography verdict;
- Hive/rhombus reuse verdict;
- coefficient-domain boundary;
- Y-Delta discriminator result;
- Phase-B tool-ownership/dedup classification;
- exact recommended API surface if accepted or narrowed.

Do not modify the shared toolbox registry in this task. Integration, if justified, is a later Driver decision.
