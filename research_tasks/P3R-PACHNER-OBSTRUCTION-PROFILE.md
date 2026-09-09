<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "P3R-PACHNER-OBSTRUCTION-PROFILE",
  "title": "Pachner-covariant arithmetic obstruction profile",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P3",
  "leverage": "MEDIUM",
  "frontier": "Bare triangulation scalar monotonicity is ruled out by Pachner reversibility; it is unknown whether an enlarged-state or covariant branch-obstruction profile transforms locally enough to guide simplification.",
  "next_action": "Analyze one 2-3 and one 1-4 Pachner move at the level of matching matrices and branch-cokernel data, looking for an exact local transport rule or a small counterexample that kills covariance.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@cd79471e16df9b4afd924ccae76a626eeb31ec9a:research_notes/POINCARE_BRC_ARITHMETIC_OBSERVER_HANDOFF_20260909.md",
    "awdawmip/chatgpt-global-knowledge@c63167f2f911e2425b8a70b0aabcc90574425235:knowledge/projects/enterprise-math/poincare-brc-normal-surface-arithmetic-observer-20260905.md"
  ],
  "evidence_status": "PROVED_BARE_SCALAR_NO_GO_PLUS_OPEN_COVARIANT_PROFILE",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "poincare",
    "pachner",
    "bistellar-moves",
    "BRC",
    "cokernel",
    "exploratory"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "P3R-PACHNER-OBSTRUCTION-PROFILE",
  "parent_objective_id": "POINCARE-BRC-RECOGNITION-20260909",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P3R4",
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

# Pachner-covariant arithmetic obstruction profile

Status: `READY / PUBLISHED-INTENT / EXPLORATORY-LOWER-PRIORITY`

## 0. Mother question

After the no-go for a strictly decreasing scalar of the bare triangulation, is there a useful Pachner-covariant arithmetic obstruction profile on an enlarged recognition state that transports branch-lattice information across local bistellar moves?

## 1. Frozen inputs and scope

Assume only the proved reversibility no-go from the durable handoff: a nonconstant scalar of the bare triangulation cannot strictly decrease under every nontrivial Pachner move. Therefore study covariance or directed-protocol quantities, not an impossible universal scalar entropy.

Restrict the first pass to explicit 2-3/3-2 and 1-4/4-1 local moves and the induced changes in normal-surface matching matrices, branch choices, cokernel classes, p-primary support, and BRC surviving search mass. Preserve enough provenance to distinguish a change of triangulation from a topological invariant.

## 2. Hard target and required outputs

For at least one move family, derive an exact local relation between pre-move and post-move integer systems, or produce a minimal counterexample showing that no useful bounded local transport of the proposed obstruction data exists. If transport exists only after adding repair coordinates, state the smallest such enlarged state and which observer it preserves.

Return concrete matrices/examples, not only analogy with Ricci flow or entropy. Any candidate directed quantity must state the orientation/simplification protocol under which monotonicity is claimed.

## 3. Research value to preserve

A positive covariance law could connect the arithmetic-observer route to triangulation simplification and explain how certificates survive representation changes. A sharp negative result is equally useful because it prevents spending research effort on a discrete-Perelman analogy that reversibility or local instability forbids.

## 4. Success, kill, and return criteria

SUCCESS is an exact nontrivial transport/covariance law with explicit hypotheses and a useful preserved observer. KILL the direction if small Pachner examples show branch-cokernel information changes without any bounded local repair adequate for recognition, or if the only preserved data collapse to already-known trivial topological invariants.

Return the smallest counterexample or the smallest sufficient enlarged state. Stop before promoting any search-complexity statistic to a topological invariant.
