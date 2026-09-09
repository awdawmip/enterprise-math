<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-PERFECT-PRIME-AP-HCM0-TANGENT-FACE-INDUCTION",
  "title": "Perfect Prime AP HCM0 tangent-face induction",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "For the normalized extreme three-support trace defect T_m(S,a,c), the parent execution proves that the entire c^0 numerator face is coefficientwise strictly positive for every m via the contiguous m^2 denominator block. Exact full-parameter certificates for m=3,4,5,6 have positive primitive numerators of degree m^2. No dimension-free formula is yet proved for the c^1 or higher faces.",
  "next_action": "Differentiate the normalized inverse/trace identity one further order at c=0, derive the exact c^1 numerator face in terms of the contiguous m^2 block G_(m^2)(x)=prod_(k=1)^(m^2)(x+k), and prove coefficientwise positivity uniformly in m or freeze the first exact obstruction; if positive, formulate and test an induction over c-degree.",
  "dependencies": [],
  "source_refs": [
    "git:awdawmip/enterprise-math@623a4ee81911cc79d07ed5db1887a06ebe91ffd5:research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/HCM0_RESEARCH_HANDOFF_INDEX_20260909.md",
    "git:awdawmip/enterprise-math@623a4ee81911cc79d07ed5db1887a06ebe91ffd5:research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/ALL_M_TANGENT_FACE_COEFFICIENTWISE_POSITIVITY_20260906.md",
    "git:awdawmip/enterprise-math@623a4ee81911cc79d07ed5db1887a06ebe91ffd5:research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/M6_ALL_PARAMETER_NORMALIZED_TRACE_CERTIFICATE_20260906.md",
    "git:awdawmip/enterprise-math@623a4ee81911cc79d07ed5db1887a06ebe91ffd5:research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/EXTREME_COEFFICIENT_SIGNED_BRANCH_BRC_REDUCTION_20260906.md"
  ],
  "evidence_status": "ALL_M_TANGENT_C0_FACE_POSITIVE / FULL_PARAMETER_POSITIVE_NUMERATORS_M3_TO_M6 / HIGHER_FACES_OPEN",
  "last_progress_ref": "git:awdawmip/enterprise-math@623a4ee81911cc79d07ed5db1887a06ebe91ffd5:research_artifacts/PERFECT_PRIME_AP_SIGNED_SECANT_HCM0_HAUSDORFF_LIFT/HCM0_RESEARCH_HANDOFF_INDEX_20260909.md",
  "last_progress_at": "2026-09-09T01:07:54+00:00",
  "hard_block": "TANGENT_C1_FACE_POSITIVE_OR_EXACTLY_OBSTRUCTED",
  "tags": [
    "Perfect-Prime",
    "HCM0",
    "tangent-face",
    "contiguous-block",
    "positive-polynomial",
    "three-support"
  ],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-PERFECT-PRIME-AP-HCM0-TANGENT-FACE-INDUCTION",
  "parent_objective_id": "OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PPTAPFACE",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT",
  "successor_gate": {
    "new_information_gap": "The parent task produced an all-m tangent-face theorem: after sign resolution the complete c^0 numerator face is an explicitly coefficientwise positive polynomial coming from one contiguous m^2 block. This creates a new c-degree filtration not visible in the original HCM0 formulation.",
    "why_parent_result_does_not_close_it": "Only the tangent c^0 face is proved for arbitrary m. Full numerators are known to be positive only in the exact all-parameter cases m=3,4,5,6, so no all-m control of c^1 or higher faces exists.",
    "discriminating_outcomes": [
      "Prove a dimension-free positive formula for the c^1 numerator face and identify a valid induction or recursion for higher c-degree.",
      "Freeze the first m or coefficient where the c^1 face fails coefficientwise positivity while the trace inequality may still survive.",
      "Find a positive basis other than ordinary monomials in which every tangent face has a uniform sign and prove that basis suffices for the trace inequality.",
      "Show that tangent-face coefficient positivity cannot imply the full trace theorem and isolate the missing nonlocal c-dependence."
    ],
    "kill_condition": "Reject extrapolation from m=3,4,5,6, raw symbolic expansion at another fixed dimension as a uniform proof, assuming c^0 positivity propagates automatically, and any argument that loses the contiguous m^2 block provenance before sign resolution.",
    "alternative_route_or_free_exploration_considered": "The separate extreme-branch parity-domination task attacks the all-m trace directly on a signed branch carrier. The tangent-face route is retained because the all-m c^0 theorem exposes a distinct contiguous-block mechanism and may yield a coefficientwise induction unavailable to branch pairing.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "This isolates the first unproved face c^1 as a small exact theorem with a clear success or obstruction criterion. It allows independent work on the observed m^2-degree positive-polynomial structure without repeating the broader parent exploration."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Perfect Prime AP HCM0 tangent-face induction

Status: `READY / RESEARCHER-PUBLISHED CONTINUATION`

## 0. Mother question

Does the all-`m` coefficientwise positivity of the tangent `c^0` face of the normalized extreme three-support trace defect extend to the `c^1` face, and if so does the contiguous `m^2` denominator block support a dimension-free induction over higher `c`-degree?

## 1. Frozen inputs and scope

Read the immutable HCM0 handoff index first. The principal theorem input is `ALL_M_TANGENT_FACE_COEFFICIENTWISE_POSITIVITY_20260906.md`, which proves that for
`G_M(x)=prod_(k=1)^M (x+k)`, `M=m^2`, the tangent numerator
`A_M(x)=(x+(M+1)/2)G_M'(x)-G_M(x)`
has every coefficient strictly positive. This gives the complete `c^0` face for every `m`.

Also retain the exact full-parameter certificates for `m=3,4,5,6`, whose primitive positive numerator has total degree `m^2`. Those finite dimensions motivate but do not prove a uniform face recursion.

Keep the actual block variables `S,a,c` and the contiguous `m^2` affine-factor block intact through sign resolution. The signed determinant origin remains relevant; a positive polynomial may be used only after the exact algebra has produced it.

## 2. Hard target and required outputs

Hard target: `TANGENT_C1_FACE_POSITIVE_OR_EXACTLY_OBSTRUCTED`.

1. Differentiate the normalized inverse/trace identity to the next order at `c=0` and derive an exact dimension-free expression for the `c^1` numerator face.
2. Express that face through `G_(m^2)` and its derivatives, elementary symmetric sums, labeled complement factors, or another exact contiguous-block basis.
3. Prove every coefficient of the `c^1` face is strictly positive for all `m>=2`, or freeze the first exact coefficient obstruction.
4. If the `c^1` theorem is positive, formulate the strongest justified recursion or induction for higher faces and identify the first additional lemma needed. Do not assert full induction without proving the transition.
5. Relate the face result back to the normalized trace theorem, stating exactly which neighborhood or coefficient information it controls and what remains global in `c`.

Exact fixed-`m` calculations may be used only as regression for a proposed general formula.

## 3. Research value to preserve

The parent execution discovered a repeated `m^2`-degree positive polynomial structure at `m=3,4,5,6` and then proved its complete tangent face uniformly in `m`. A positive next-face theorem would convert that pattern into a genuine dimension-free hierarchy and may provide an inductive route to the first dangerous three-support coefficient. A negative face obstruction would precisely identify where the low-dimensional positive-polynomial pattern stops being structurally stable.

## 4. Success, kill, and return criteria

Success is a proved all-`m` positive formula for the `c^1` face, preferably with a rigorously justified recurrence that exposes the next higher face. A valid negative result is the first exact `m` and face coefficient violating coefficientwise positivity, together with a deterministic certificate and an analysis of whether the trace inequality itself remains plausible.

Kill raw expansion at a new fixed dimension as a substitute for proof, automatic propagation from the `c^0` face, and algebraic simplifications that erase the contiguous block labels before the sign is resolved. If ordinary monomial positivity fails, test an exact alternative positive basis only when its implication to the trace target is proved.

The parent HCM0 objective remains open unless the returned face theorem is separately connected to every required HCM0 finite-difference cell.
