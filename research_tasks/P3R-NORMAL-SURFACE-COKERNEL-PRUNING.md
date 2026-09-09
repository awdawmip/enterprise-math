<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "P3R-NORMAL-SURFACE-COKERNEL-PRUNING",
  "title": "Normal-surface cokernel pruning benchmark",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Unknown whether exact integer-cokernel / mod-p^k separators prune enough partial quadrilateral branches in real 3-sphere-recognition instances to justify integration.",
  "next_action": "Build a minimal exact adapter from a triangulation plus partial quadrilateral assignment to M_beta,b, generate a separating character when b is outside the integer image, and benchmark first-pruned depth and removed leaf mass on a controlled census.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@cd79471e16df9b4afd924ccae76a626eeb31ec9a:research_notes/POINCARE_BRC_ARITHMETIC_OBSERVER_HANDOFF_20260909.md",
    "awdawmip/chatgpt-global-knowledge@c63167f2f911e2425b8a70b0aabcc90574425235:knowledge/projects/enterprise-math/poincare-brc-normal-surface-arithmetic-observer-20260905.md"
  ],
  "evidence_status": "PROVED_SUBTREE_PRUNING_DERIVATION_PLUS_UNMEASURED_ALGORITHMIC_IMPACT",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "poincare",
    "3-sphere-recognition",
    "normal-surfaces",
    "BRC",
    "smith-normal-form",
    "modular-pruning"
  ],
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

# Normal-surface cokernel pruning benchmark

Status: `READY / PUBLISHED-INTENT / EXPERIMENTAL-INTEGRATION`

## 0. Mother question

Does the exact branch-cokernel obstruction produce practically significant early pruning in normal-surface branch traversal for 3-sphere recognition, beyond the feasibility and domination tests already used by existing implementations?

## 1. Frozen inputs and scope

Start from the durable Poincaré BRC handoff and preserve its theorem-strength boundaries. Use standard normal-surface matching equations, per-tetrahedron quadrilateral branching, and the target Euler-characteristic equation for a 2-sphere. For a partial branch beta, construct the relaxed integer matrix M_beta by deleting only already-forbidden quadrilateral columns. Reuse the existing Smith/local-support, modular exact linear algebra, and finite-observer-completeness interfaces where adequate.

The benchmark population must include controlled triangulations of S^3, lens spaces, the Poincaré homology sphere, and a documented sample of hyperbolic homology spheres or comparable census manifolds. Record triangulation sizes and provenance. Do not infer a topological invariant from branch-search statistics, and do not treat omega_beta=0 as a sphere-existence certificate.

## 2. Hard target and required outputs

Produce an executable exact adapter that, for each visited partial branch beta, can return either UNKNOWN/SURVIVES or a verified finite separator (p^k,y) satisfying y^T M_beta = 0 mod p^k and y^T b != 0 mod p^k. Integrate or faithfully simulate this check at a branch-traversal point early enough to measure real pruning.

Return a benchmark table with at least: tetrahedron count n, number of visited partial nodes, first-pruned depths, number of separator hits, exact removed ternary leaf mass sum 3^(n-|beta|) over first-pruned antichain nodes, separator moduli, time spent in the observer, and total traversal cost with/without the observer under the same baseline. Include at least one preserved example certificate that a small independent checker can verify.

## 3. Research value to preserve

This is the direct test of whether the strongest new arithmetic observation from the originating Poincaré reroute is merely correct or algorithmically useful. A negative benchmark is also valuable because it kills the route before deeper integration; a positive benchmark can become a reusable exact prefilter for normal/almost-normal search.

## 4. Success, kill, and return criteria

SUCCESS requires reproducible exact certificates and a documented nontrivial pruning effect on at least one non-toy family without changing the recognized topology. STRONG SUCCESS requires consistent early subtree removal whose saved search cost materially exceeds observer cost on a meaningful census slice.

KILL the integration direction if exact separators almost never fire before existing cheap feasibility tests, or if their computation consistently costs more than the search they remove. If results are mixed, return the discriminating manifold/triangulation features rather than averaging them away. Stop after the benchmark establishes a clear useful regime, a clear no-go regime, or the smallest specific unresolved implementation blocker.
