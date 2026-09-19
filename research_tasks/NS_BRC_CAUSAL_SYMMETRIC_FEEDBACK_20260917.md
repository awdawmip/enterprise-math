<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-NS-BRC-CAUSAL-SYMMETRIC-FEEDBACK-20260917",
  "title": "NS/BRC Causal Propagator and Symmetric-Helical Feedback",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The current NS certificates use an all-mode causal inverse whose norm grows through a conservative time-dependent envelope. Common-output polarization and symmetric pairing reduce static feedback majorants, but their positive high-frequency kernels retain a nonzero floor. The unresolved layer is a time-ordered, phase/helicity-aware propagator and feedback estimate.",
  "next_action": "Derive the exact time-dependent linearized evolution about the heat/A3 reference using the symmetric convection form, then rewrite the remaining feedback in a helical/Waleffe basis before absolute values and prove either a materially smaller all-mode inverse/feedback bound or an exact obstruction.",
  "dependencies": [],
  "source_refs": [
    "research_notes/ns_brc_program_handoff_20260917.md",
    "research_notes/ns-coupled-polarization-20260910.md",
    "research_notes/ns-orthogonal-response-barrier-20260910.md",
    "research_notes/ns-causal-inverse-newton-basin-20260909.md",
    "research_notes/ns-critical-hermitian-tail-verification-20260909.json"
  ],
  "evidence_status": "RESEARCH_PROGRAM_INTEGRATION_V1",
  "last_progress_ref": "research_notes/ns_brc_program_handoff_20260917.md",
  "last_progress_at": "2026-09-17T12:53:00+08:00",
  "hard_block": "CAUSAL_INVERSE_AND_SIGNED_FEEDBACK_MAJORANTS_TOO_COARSE",
  "tags": ["Navier-Stokes", "BRC", "causal-inverse", "propagator", "helicity", "Waleffe", "symmetric-convection"],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-NS-BRC-CAUSAL-SYMMETRIC-FEEDBACK-20260917",
  "parent_objective_id": "EM-NS-BRC-JITTER-REGULARITY-PROGRAM-20260917",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R-NSCS",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# NS/BRC Causal Propagator and Symmetric-Helical Feedback

Status: `READY / DIRECT USER RESEARCH INTEGRATION / PUBLISHED_REGISTERED`

## 0. Mother question

Can the full time-dependent linearized Navier–Stokes propagator and the signed symmetric nonlinearity be controlled by phase-, helicity-, and polarization-aware bounds strong enough to replace the present conservative scalar growth envelope?

## 1. Frozen inputs and scope

Work in the classical three-dimensional periodic incompressible NS setting of the cited checkpoints. Reuse the exact trajectory spaces and all-mode causal inverse interface; do not replace them by a finite-mode model.

Retain time ordering, ordered input labels, helicity signs, radial shells, output polarization, complex phases, and same-output path identity until a justified norm bound is formed. Finite matrix calculations require analytic infinite-frequency tails.

The task targets the propagator and feedback bounds themselves. Do not spend the task merely extending the response dictionary under unchanged estimates.

## 2. Hard target and required outputs

Hard target: `CAUSAL_PROPAGATOR_AND_SIGNED_FEEDBACK_SHARPENED_OR_NO_GO`.

Deliver all of the following, or an exact obstruction replacing an impossible item:

1. An exact Duhamel/evolution-family representation for the current linearized operator using the symmetric convection form wherever valid.
2. A computable all-time bound for the propagator and causal inverse that keeps noncommuting time slices honest and states every time-ordering cost.
3. A branch-resolved helical formula for the symmetric convection interaction with exact Waleffe coefficients and radial/sign factors visible.
4. An all-frequency signed Gram, commutator, or polarization inequality that materially improves the present positive majorant, or an exact saturation counterexample.
5. An analytic high-frequency tail theorem; finite FCC shell cancellation is not sufficient.
6. Quantitative impact on the nonlinear feedback constant and the certified basin, including an exact lower-bound/no-go if the chosen norm cannot improve its amplitude scaling.

## 3. Research value to preserve

Recent progress shows that reducing upstream overestimates has more leverage than adding more response orders. This task attacks the two remaining structural losses together: conservative time propagation and loss of signed/helical information in the feedback estimate. A positive result could enlarge the basin qualitatively; a no-go would justify changing norm or reference flow instead of further local optimization.

## 4. Success, kill, and return criteria

Success is an all-mode propagator/feedback theorem that materially improves the current amplitude dependence or a structural lower bound proving that the present norm/reference cannot do so.

Kill any argument that assumes time slices commute, infers all-time control from sampled times, squares branches before same-output coherent summation, extrapolates finite-shell cancellation to all scales, or imports a helicity restriction without carrying it into the theorem statement.

Return the exact improved inequality or sharpest obstruction, with the next mathematical bottleneck it creates.
