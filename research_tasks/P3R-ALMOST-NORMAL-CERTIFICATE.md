<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "P3R-ALMOST-NORMAL-CERTIFICATE",
  "title": "Exact canonical-Q and QO arithmetic certificates",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "HIGH",
  "frontier": "The corrected certificate is repair-state typed and lives in Q/QO coordinates; the exact theorem/checker package, bad-prime boundary, gcd/valuation fallback, and octagon correction are not yet packaged for independent reuse.",
  "next_action": "State and verify the prime-local repair-state row-dependence theorem and global S_beta-empty pruning rule, then package exact gcd/valuation and QO octagon correction certificates in one deterministic checker interface.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@3359de19ffb776ebfaa59bc7443b171b23d35f4d:research_notes/POINCARE_BRC_CORRECTED_FRONTIER_HANDOFF_20260909.md",
    "awdawmip/chatgpt-global-knowledge@8acfeac504eee85f6fbb66018470ad233ef33ff7:knowledge/projects/enterprise-math/poincare-brc-normal-surface-arithmetic-observer-20260905.md"
  ],
  "evidence_status": "CORRECTED_PROVED_Q_REPAIR_STATE_THEOREMS_PLUS_OPEN_CERTIFICATE_PACKAGING_AND_QO_ADAPTER",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["poincare","canonical-Q","almost-normal-surfaces","QO","repair-state","certificate","BRC","valuation"],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "P3R-ALMOST-NORMAL-CERTIFICATE",
  "parent_objective_id": "POINCARE-BRC-RECOGNITION-20260909",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P3R2",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:1f84e78de591605da6106f3f14ffad3cd7fad66aa5bf67e29beb44906b976c8a",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Exact canonical-Q and QO arithmetic certificates

Status: `READY / SUPERSEDING-GENERATION / EXACT-CERTIFICATE`

## 0. Mother question

Can the corrected repair-state arithmetic observers be packaged as small exact certificates and checkers for both quadrilateral normal-surface search and quadrilateral-octagon almost-normal search?

## 1. Frozen inputs and scope

Use the corrected canonical-Q formulation. Do not use raw standard-coordinate chi=2 as a nontrivial-sphere certificate. The finite-field layer is valid only for repair states tau and good odd primes p for which H_tau=[T;G_tau] has full triangle-column rank and therefore yields a certified prime-local Euler row d_{p,tau}.

At a partial Q branch beta, row dependence of d_{p,tau,beta} on B_beta kills only the state (beta,tau). Global branch pruning requires all repair states dead. Descendant safety comes from column deletion preserving the row-dependence witness. The exact integer layer uses the image subgroup gZ of the Euler homomorphism on ker_Z(B_beta), with descendant divisibility and p-adic monotonicity.

For QO coordinates, fix the exceptional octagon location/type explicitly and carry its linear Euler correction. Do not infer final sphere recognition, connectedness, or simple connectivity merely from these arithmetic certificates.

## 2. Hard target and required outputs

Return exact statements and independently checkable certificate formats for: good-prime validation; construction/verification of d_{p,tau}; row-dependence witness; surviving repair-state aggregation; descendant reuse; exact g-divisibility/valuation obstruction; and the determinantal-divisor formula in the rank-increasing case.

Provide deterministic checkers with regression cases for a valid kill, a bad-prime rejection, a state that survives, overlapping repair states, and a descendant reuse. Extend the same interface to one explicit QO almost-normal example with the octagon correction visible in the certificate.

## 3. Research value to preserve

This task turns the corrected mathematical insight into a trusted portable interface. It is useful even if empirical speedup is modest, because it separates expensive search from small exact verification and prevents later implementations from reintroducing the vertex-link/Euler-projection error.

## 4. Success, kill, and return criteria

SUCCESS requires a self-contained theorem/certificate package that another researcher can use without the originating conversation, including every rank and repair-state hypothesis. KILL any shortcut that uses a rank-dropping prime, treats one killed repair state as a dead branch, assumes Euler descends through bare Q projection, or loses the octagon correction.

Return proved derivations, executable/formal verification status, and unresolved implementation gaps separately. Stop when normal and QO certificate semantics are exact and regression-tested, even if no speed claim is available.
