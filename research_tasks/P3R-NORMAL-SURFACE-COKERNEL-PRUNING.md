<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "P3R-NORMAL-SURFACE-COKERNEL-PRUNING",
  "title": "Canonical-Q repair-state arithmetic pruning benchmark",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The corrected subtree certificate uses canonical quadrilateral candidates plus repair states tau; it is unknown whether prime-local Euler-row dependence and exact gcd/valuation fallbacks prune enough real recognition branches to justify integration.",
  "next_action": "Prototype the repair-state observer on one-vertex Regina control triangulations: construct B, G_tau, good-prime d_{p,tau}, track surviving repair states S_beta, and measure exact first-pruned branch mass before stronger feasibility tests.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@3359de19ffb776ebfaa59bc7443b171b23d35f4d:research_notes/POINCARE_BRC_CORRECTED_FRONTIER_HANDOFF_20260909.md",
    "awdawmip/chatgpt-global-knowledge@8acfeac504eee85f6fbb66018470ad233ef33ff7:knowledge/projects/enterprise-math/poincare-brc-normal-surface-arithmetic-observer-20260905.md"
  ],
  "evidence_status": "CORRECTED_PROVED_REPAIR_STATE_SUBTREE_CERTIFICATE_PLUS_UNMEASURED_ALGORITHMIC_IMPACT",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["poincare","3-sphere-recognition","normal-surfaces","canonical-Q","repair-state","BRC","modular-pruning","gcd-valuation"],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "P3R-NORMAL-SURFACE-COKERNEL-PRUNING",
  "parent_objective_id": "POINCARE-BRC-RECOGNITION-20260909",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P3R1",
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

# Canonical-Q repair-state arithmetic pruning benchmark

Status: `READY / SUPERSEDING-GENERATION / EXPERIMENTAL-INTEGRATION`

## 0. Mother question

Do the corrected canonical-Q arithmetic observers—prime-local repair-state Euler dependence followed by exact gcd/valuation tests—produce practically significant early subtree pruning in normal-surface search for 3-sphere recognition?

## 1. Frozen inputs and scope

Use the corrected durable handoff, not the historical raw-standard-coordinate chi=2 relaxation. A closed triangulation has trivial triangle-only vertex-link spheres, so raw standard matching plus chi=2 is not an adequate nontrivial-sphere observer.

Use quadrilateral matching matrix B and canonical repair states tau that select one zero triangle coordinate around each global triangulation vertex. For each good odd prime p, derive d_{p,tau} by finite-field elimination of triangle coordinates. At partial branch beta, a repair state is killed when d_{p,tau,beta} lies in the row span of B_beta. Prune the whole branch only when every possible repair state is certified dead, i.e. the surviving repair-state set S_beta is empty.

After the cheap prime layer, optionally use the exact Euler-image generator g_{beta,tau}, its divisibility/valuation obstruction, and only then stronger cone or semigroup tests when justified. Preserve branch and repair-state provenance.

## 2. Hard target and required outputs

Implement or faithfully prototype the exact observer against documented Regina triangulations. At minimum include small S^3 controls, lens spaces, the Poincaré homology sphere, and one hyperbolic control family. For every tested triangulation record n, vertex count, repair-state count, chosen good primes, visited branch nodes, first-pruned nodes, surviving-repair-state bitset sizes, exact removed labeled branch mass, observer cost, and baseline search cost.

Preserve at least one explicit row-dependence certificate and one exact gcd/valuation certificate. Compare observer-on versus observer-off under the same search order. Report bad-prime rank failures rather than silently using them.

## 3. Research value to preserve

This is the direct empirical test of the corrected arithmetic contribution. A positive regime can become a reusable exact prefilter; a negative result can kill the integration route while preserving the theorem-level observer for other uses. The benchmark also determines whether the more expensive affine-semigroup-hole layer is worth implementing.

## 4. Success, kill, and return criteria

SUCCESS requires reproducible sound certificates and nontrivial pruning on a non-toy family without changing recognition outcomes. STRONG SUCCESS requires saved search cost that materially exceeds observer cost across a documented useful regime.

KILL expensive integration if repair-state coverage rarely becomes empty before existing cheap tests, or if observer overhead consistently dominates removed search. If performance correlates with dual-treewidth, vertex count, prime choice, or manifold family, return those discriminating features rather than a single average. Do not claim a new Poincaré proof or a worst-case complexity improvement from empirical pruning alone.
