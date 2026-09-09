<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "EM-FREE-W59A-JT2-RAMANUJAN-LEGENDRE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:1f84e78de591605da6106f3f14ffad3cd7fad66aa5bf67e29beb44906b976c8a",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-EMW59A-JT2-QTF3-FIXED-POINT",
  "title": "JT2 QTF3 fixed-point quadratic-transform lift",
  "frontier": "The p^3 quadratic-transform defect has been compressed to a reflection-compatible inhomogeneous hypergeometric differential equation. At u=1/2 the remaining lift is a single normalization scalar; the unresolved target is equality of the two truncated hypergeometric sums modulo p^3.",
  "next_action": "Use the residual differential equation and u<->1-u symmetry to identify the homogeneous Hasse component, evaluate its fixed-point normalization, and prove that the remaining scalar vanishes, yielding the truncated quadratic transformation modulo p^3.",
  "dependencies": [],
  "source_refs": [
    "research_notes/EMW59A_JT2_COMPLETE_RELEASE_AND_DRIVER_HANDOFF_20260909.md",
    "research_notes/EM_FREE_W59A_JT2_UR_QTF3_STATE_MACHINE_HANDOFF_20260909.md",
    "global-knowledge:awdawmip/chatgpt-global-knowledge@f48cd4d076f61a5b804a7617158359e198b2fd5d:journal/progressive-number-theory/2026-09-09/20260909T105443+0800-ur-legendre-barycentric-lift.md"
  ],
  "evidence_status": "FREE_RESEARCH_JT2_DURABLE_HANDOFF",
  "last_progress_ref": "research_notes/EM_FREE_W59A_JT2_UR_QTF3_STATE_MACHINE_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T11:03:17+08:00",
  "hard_block": "QTF3_FIXED_POINT_NORMALIZATION_SCALAR",
  "tags": [
    "EM-FREE-W59A",
    "JT2",
    "QTF3",
    "hypergeometric",
    "quadratic-transform",
    "p^3",
    "fixed-point",
    "BRC"
  ],
  "registry_key": "RS-EMW59A-JT2-QTF3-FIXED-POINT",
  "identity_lane": "RW59QT",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null
}
-->

# JT2 QTF3 fixed-point quadratic-transform lift

Status: `READY / FREE-RESEARCH INTEGRATION / PUBLISHED_REGISTERED`

## 0. Mother question

Can the current residual differential equation for the Mao-Pan-type quadratic-transform defect be normalized at the fixed point `u=1/2` strongly enough to prove the two truncated hypergeometric values equal modulo `p^3`?

## 1. Frozen inputs and scope

Read `research_notes/EM_FREE_W59A_JT2_UR_QTF3_STATE_MACHINE_HANDOFF_20260909.md` first and preserve its exact prime scope.

The current compressed carrier is the defect
`D_p(u)=L_p(u)-F_p(4u(1-u))`.
After removing the forced factor `u^p p^2`, the residual `r_p(u)` satisfies the displayed second-order inhomogeneous equation in the handoff. The differential operator commutes with `u<->1-u`, while the inhomogeneous term has the required reflection antisymmetry. Therefore the symmetrized residual lies in the homogeneous Hasse solution space.

Treat the one-dimensional numerical line previously observed for the residual scalar as evidence only, not as a proof. Preserve the truncation boundary, the `p^2` factor already extracted, and the full modulo-`p^3` target. Do not reopen CM0 or the UR slope-value problem inside this task.

## 2. Hard target and required outputs

Hard target: `QTF3_FIXED_POINT_NORMALIZATION_SCALAR`.

Prove, on the exact prime scope,

`sum_{k=0}^{p-1} ((1/3)_k (2/3)_k)/((k!)^2 2^k)`
`==`
`sum_{k=0}^{p-1} ((1/6)_k (1/3)_k)/(k!)^2`
`(mod p^3)`.

Required outputs:

1. Re-establish only the minimum residual differential identity needed for the proof, with the extracted `u^p p^2` factor tracked exactly.
2. Identify the homogeneous Hasse component of `r_p(u)+r_p(1-u)` or replace it by an equivalent exact invariant.
3. Evaluate the fixed-point normalization at `u=1/2` and prove the remaining scalar is zero.
4. Deduce the displayed truncated congruence with the truncation endpoint `p-1` and all denominators justified `p`-adically.
5. State whether the proof holds on a broader prime class than the parent route; any widening must be proved rather than inferred from examples.
6. If the scalar does not vanish under the frozen hypotheses, return its exact formula or the smallest missing normalization datum.

## 3. Research value to preserve

The reflection argument has compressed a full `p^3` transformation defect to one scalar at the fixed point. Closing that scalar avoids reintroducing large harmonic expansions and gives a reusable fixed-point lifting principle for truncated hypergeometric quadratic transformations. An exact nonzero scalar formula would be equally informative because it would identify the true correction term and prevent a false JT2 closure.

## 4. Success, kill, and return criteria

Success is a proof of the fixed-point congruence modulo `p^3` with the residual factorization and normalization visible.

Kill any route that stops at modulo `p^2`, infers the scalar from finite numerical samples, loses the `p-1` truncation boundary, or silently replaces the finite Hasse solution with an analytic infinite-series identity that does not control the required `p`-adic precision.

Return the full congruence proof or an exact normalization obstruction. The task grants no Working Truth or Foundation status merely by being published.
