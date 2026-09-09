<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "P3R-PACHNER-OBSTRUCTION-PROFILE",
  "title": "Pachner transport of Q-row codes and arithmetic factor width",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P3",
  "leverage": "MEDIUM",
  "frontier": "Bare move-monotone scalar entropy is impossible by reversibility; the viable open question is whether local bistellar moves admit provenance-safe transport of Q-row codes and whether directed simplification toward lower dual-treewidth/arithmetic factor width is useful.",
  "next_action": "Analyze explicit 2-3 and 1-4 moves as local extension/puncturing/shortening operations on Q-matching row codes and repair-state observers, and test whether the resulting factor-width change is locally computable and useful.",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@3359de19ffb776ebfaa59bc7443b171b23d35f4d:research_notes/POINCARE_BRC_CORRECTED_FRONTIER_HANDOFF_20260909.md",
    "awdawmip/chatgpt-global-knowledge@8acfeac504eee85f6fbb66018470ad233ef33ff7:knowledge/projects/enterprise-math/poincare-brc-normal-surface-arithmetic-observer-20260905.md"
  ],
  "evidence_status": "PROVED_BARE_SCALAR_NO_GO_PLUS_OPEN_Q_CODE_TRANSPORT_AND_WIDTH_ROUTE",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": ["poincare","pachner","Q-matching","coding-theory","treewidth","BRC","factor-width","exploratory"],
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

# Pachner transport of Q-row codes and arithmetic factor width

Status: `READY / SUPERSEDING-GENERATION / EXPLORATORY-LOWER-PRIORITY`

## 0. Mother question

Can local Pachner moves transport the corrected Q-row-code / repair-state arithmetic observer by exact local operations, and can directed simplification toward lower dual-treewidth or arithmetic factor width reduce recognition cost without inventing a forbidden universal entropy?

## 1. Frozen inputs and scope

The bare scalar no-go is fixed: Pachner moves are reversible, so no nonconstant scalar of the triangulation alone can strictly decrease under every nontrivial move. Study local covariance and directed protocols instead.

Use the corrected Q-matching code, repair states, prime-local Euler cosets, and treewidth-FPT factor structure. Preserve branch/repair provenance. Begin only with explicit 2-3/3-2 and 1-4/4-1 moves. Candidate transports may use local extension, puncturing, shortening, or repair coordinates, but must be proved to preserve the declared observer.

## 2. Hard target and required outputs

For at least one Pachner move family, derive the exact pre/post relation between Q-matching rows, coordinate blocks, and repair-state data, or give a minimal counterexample showing that no bounded local transport adequate for the observer exists.

Define any proposed arithmetic factor-width precisely and compare it with dual-treewidth on explicit examples. If a directed simplification heuristic is proposed, state its orientation and measure whether it lowers the exact dynamic-program state space or observer cost. Do not call search-mass or width statistics topological invariants unless invariance is separately proved.

## 3. Research value to preserve

A positive local transport law could make arithmetic certificates reusable across triangulation simplification and connect the code-theoretic observer to known width-based 3-manifold algorithms. A negative result can kill a broad class of discrete-Perelman analogies early.

## 4. Success, kill, and return criteria

SUCCESS is an exact nontrivial transport law or a reproducible directed-width reduction with a proved observer interface. KILL a covariance claim if a small Pachner example changes the relevant code/repair information in a way not recoverable by the proposed local state. KILL a width heuristic if it merely renames dual-treewidth without improving observer execution or if computing it costs more than it saves.

Return the smallest sufficient enlarged state or the smallest counterexample. Do not claim a universal Pachner monotone.
