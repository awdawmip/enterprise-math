<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ABC-ENTERPRISE-CAPPED-CORE-ENERGY",
  "title": "ABC Enterprise Capped-Core Energy Bound",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Control the capped repeated-prime core I_cap after boundary-paid tower height has been removed, and determine whether the interior regime admits a bound strong enough to force abc quality q<=1+epsilon.",
  "next_action": "Derive exact decompositions and inequalities for I_cap in terms of one-time prime support R and beta; search first for counterexamples to any coefficient-2 bound before attempting proof.",
  "dependencies": [],
  "source_refs": [
    "definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md@c7a5a1c148f48f3c9d57cafe79536030541ed2d5",
    "definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md@c7a5a1c148f48f3c9d57cafe79536030541ed2d5",
    "definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md@c7a5a1c148f48f3c9d57cafe79536030541ed2d5"
  ],
  "evidence_status": "DIRECT_USER_DIRECTION / ABC_ENTERPRISE_PLANE_DECOMPOSITION_FROZEN_IN_CONVERSATION",
  "last_progress_ref": "Parent abc-on-Enterprise-plane analysis isolated exact defect, Pascal-ray invariance, carry spectra, boundary payment and capped-core frontier.",
  "last_progress_at": "2026-08-27T08:02:00+00:00",
  "hard_block": null,
  "tags": ["abc","enterprise-plane","radical","p-adic","prime-towers","abc1"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ABC-ENTERPRISE-CAPPED-CORE-ENERGY",
  "parent_objective_id": "ABC_ENTERPRISE_PLANE_RESEARCH_20260827",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "ABC1",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# ABC Enterprise Capped-Core Energy Bound

Status: `PUBLISHED_REGISTERED / READY / DIRECT_USER_DIRECTION`

## Mother question

Control the capped repeated-prime core I_cap after boundary-paid tower height has been removed, and determine whether the interior regime admits a bound strong enough to force abc quality q<=1+epsilon.

The task must treat both a positive theorem and a precise obstruction/counterexample family as valuable terminal outcomes. It must not assume the abc conjecture or any statement equivalent to the desired bound.

## Frozen inputs and scope

Work with primitive positive triples \(a+b=c,\ \gcd(a,b)=1\), and the typed Enterprise interpretation in which the additive point is sector-local while prime valuations, radical, repeated-prime height, Pascal scaling and carry data are derived arithmetic/readout layers.

The already derived identities may be used as starting lemmas, but every theorem claimed in this task must be reproved or independently checked in the task return if it is load-bearing. Keep native point addresses separate from the derived diagonal displacement quotient; no classical or derived readout is promoted to native ontology by this task.

## Hard target and required outputs

Hard target: `ABC_CAPPED_CORE_BOUND_PROVED_OR_EXACT_OBSTRUCTION_FROZEN`.

Required outputs:

1. Exact definitions of every task-specific invariant and its semantic layer.
2. At least one active counterexample search against the strongest proposed inequality.
3. A proof, exact obstruction, or bounded-computation certificate with clearly stated scope.
4. A comparison showing whether the result is strictly stronger than a tautological restatement of abc.
5. A list of surviving assumptions and the smallest unresolved unit.
6. A durable return at `research_returns/ABC_ENTERPRISE_CAPPED_CORE_ENERGY_RETURN_20260827.md`.

## Research value to preserve

This isolates the genuinely unresolved arithmetic core after the exact boundary-payment inequality, avoiding re-proving abc in disguised notation.

## Success, kill, and return criteria

Freeze exactly one primary verdict:

- `THEOREM_PROVED`;
- `WEAKER_THEOREM_PROVED`;
- `EXACT_OBSTRUCTION`;
- `FINITE_EVIDENCE_ONLY`;
- `NO_PROGRESS_WITH_EXACT_BLOCKER`.

Kill any route whose decisive inequality algebraically simplifies to the abc conjecture itself, or whose proof imports the target bound under another name. Finite enumeration cannot be reported as a global proof. Task termination is task-scoped and returns control to `ABC_ENTERPRISE_PLANE_RESEARCH_20260827`.
