<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R1160B-GREGORY-MACHIN-RATIONAL-SUPPORT3-PARETO",
  "title": "Gregory-Machin rational support-three Pareto census",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Compute the first exact generalized-rational support-three endpoint/Pareto surface under an explicit finite atom-resource budget, using valuation-plane structure rather than cubic atom enumeration.",
  "next_action": "Load the #1160 handoff and support-two H=1000 regression, then declare one finite atom-resource universe and construct exact rank-two candidate grouping for three-atom endpoint relations.",
  "dependencies": [
    "RS-R1160A-GREGORY-MACHIN-RATIONAL-ATOM-GENERATOR"
  ],
  "source_refs": [
    "research_handoffs/GREGORY_MACHIN_1160_DURABLE_HANDOFF_20260909.md",
    "research_notes/GREGORY_MACHIN_VALUATION_CIRCUIT_TARGET_THEOREM_20260903.md",
    "research_notes/GREGORY_MACHIN_GENERALIZED_BIT_PARETO_BOUND_20260904.md",
    "research_notes/GREGORY_MACHIN_RATIONAL_SUPPORT2_H1000_PARETO_20260904.md",
    "research_notes/experiments/gregory_machin_rational_support2_h1000_census_20260904.py"
  ],
  "evidence_status": "SOURCE_BACKED_OPEN_FRONTIER",
  "last_progress_ref": "research_handoffs/GREGORY_MACHIN_1160_DURABLE_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T10:30:46+08:00",
  "hard_block": null,
  "tags": ["R1160", "gregory-machin", "rational-turn", "support-three", "gaussian-valuation", "pareto"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-R1160B-GREGORY-MACHIN-RATIONAL-SUPPORT3-PARETO",
  "parent_objective_id": "EM-OBJ-1160-GREGORY-MACHIN-DISCRETE-WINDING",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "R1160B",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:8ac3d9c2fa05d6e96b01415562970e7b856d38e44479aa76fbf99ca875959fb6",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Gregory-Machin rational support-three Pareto census

Status: `READY / SOURCE_BACKED / DEPENDENCY_DECLARED`

## Mother question

Under an explicit finite coordinate-height or bit budget, what is the exact endpoint-feasible Pareto frontier for formulas using three distinct primitive positive rational-turn atoms, and at what resource scale does support three first strictly improve the verified support-two frontier?

## Frozen inputs and scope

Use `research_handoffs/GREGORY_MACHIN_1160_DURABLE_HANDOFF_20260909.md` as the route entrypoint. The `C8 + free Gaussian valuation` endpoint signature, valuation-circuit target theorem, finite tangent-sheet lift, generalized rational-alphabet no-go, resource lower bound and H=1000 seven-point support-two Pareto frontier are frozen predecessor inputs at their stated scopes.

This task depends on `RS-R1160A-GREGORY-MACHIN-RATIONAL-ATOM-GENERATOR` for a complete finite atom universe at the chosen enlarged budget. If that task returns a negative generation result, this task may use its certified finite universe/oracle boundary instead, but must preserve the exact scope.

Retain resource coordinates separately. At minimum record generalized Lehmer measure `mu`, atom-coordinate bits, support, coefficient `l1` size, maximum atom height, and finite winding/sheet data. Do not replace them by an arbitrary weighted scalar.

Endpoint recognition must be exact integer/rational arithmetic. Floating logarithms may rank an already certified candidate in the analytic-completion coordinate but may not recognize endpoint equality.

General circuit operations should reuse the existing typed circuit calculus. The task-specific computational object is the sparse Gaussian-valuation rank-two geometry of primitive rational atoms.

## Hard target and required outputs

1. Declare one finite atom-resource universe that strictly extends or structurally generalizes the H=1000 support-two baseline and is completely enumerable by the dependency result.
2. Construct an exact candidate-reduction method for three atoms using normalized valuation-plane data, exterior/Pluecker coordinates, sparse support incidence, or an equivalent exact invariant; avoid raw cubic enumeration over the full atom set.
3. Enumerate every rank-two minimal three-atom circuit in the declared universe that can hit the diagonal `C8` target, derive its primitive integer coefficient vector, and attach a finite winding/sheet certificate.
4. Compute the nondominated frontier in the declared resource coordinates and compare it against the seven verified support-two Pareto points under the same resource convention.
5. State exactly which support-three points, if any, strictly dominate a support-two point and identify the smallest declared resource level at which the first strict improvement occurs.
6. If support three yields no improvement in the declared complete universe, return that bounded no-improvement theorem with exact counts rather than extending the search informally.
7. Preserve executable regression counts: atom count, candidate-plane count, exact endpoint-circuit count, winding-valid count and Pareto-front size.

## Research value to preserve

The H=1000 support-two result established that generalized rational turns form a real resource Pareto surface rather than an integer-reciprocal formula list. Support three is the first higher-support test of that surface. A complete census can reveal a genuine Pareto phase transition; a bounded negative result would instead show that additional support does not automatically buy completion efficiency once input complexity is charged.

## Success, kill, and return criteria

**Success:** a complete bounded support-three theorem with exact candidate reduction, endpoint and winding certificates, reproducible counts, and a resource-consistent comparison to the support-two baseline.

**Kill:** exact evidence that the declared budget cannot be enumerated completely or that the proposed candidate reduction misses certified baseline circuits. In that case narrow the universe to the largest fully certified scope and return the obstruction instead of claiming exhaustiveness.

**Return:** report the complete finite universe, algorithmic reduction, exact frontier, all strict support-two dominations or their absence, checker evidence and the next discriminating resource scale. Historical or numerical formula recognition is not a substitute for endpoint certification.
