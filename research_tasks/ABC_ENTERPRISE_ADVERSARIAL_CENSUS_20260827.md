<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ABC-ENTERPRISE-ADVERSARIAL-CENSUS",
  "title": "ABC Enterprise Adversarial Census and No-Go Audit",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Build an exact census of primitive abc triples stressing the proposed Enterprise invariants, with special focus on high quality but low beta, high I_cap, delayed carry activation, and false local-payment heuristics.",
  "next_action": "Enumerate primitive triples in reproducible ranges, rank by q, beta/R, H/R, I_cap/R and carry features, then search for minimal counterexamples to every candidate inequality used by ABC1-ABC3.",
  "dependencies": [],
  "source_refs": ["definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md@c7a5a1c148f48f3c9d57cafe79536030541ed2d5","definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md@c7a5a1c148f48f3c9d57cafe79536030541ed2d5"],
  "evidence_status": "DIRECT_USER_DIRECTION / ABC_ENTERPRISE_PLANE_DECOMPOSITION_FROZEN_IN_CONVERSATION",
  "last_progress_ref": "Parent analysis already killed a boundary-only explanation using high-quality interior examples and identified several tautological local-payment forms.",
  "last_progress_at": "2026-08-27T08:02:00+00:00",
  "hard_block": null,
  "tags": ["abc","counterexample","census","stress-test","abc4"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ABC-ENTERPRISE-ADVERSARIAL-CENSUS",
  "parent_objective_id": "ABC_ENTERPRISE_PLANE_RESEARCH_20260827",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "ABC4",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4","review_state":"PASS","temporary_overrides":[]}
}
-->

# ABC Enterprise Adversarial Census and No-Go Audit

Status: `PUBLISHED_REGISTERED / READY / DIRECT_USER_DIRECTION`

## Mother question

Which primitive abc triples maximally stress or falsify the proposed capped-core, boundary and carry-activation inequalities, and which apparent Enterprise patterns survive adversarial enumeration rather than famous-example selection?

## Frozen inputs and scope

Use exact integer arithmetic. Enumerate only primitive positive triples `a+b=c`, compute radical and valuation-derived observables exactly, and isolate verifier access from any heuristic that is meant to be factor-blind or prediction-like. Enumeration may discover conjectures but cannot prove infinite claims.

## Hard target and required outputs

Hard target: `ABC_ADVERSARIAL_CENSUS_AND_NOGO_CERTIFICATES_FROZEN`.

Required outputs: reproducible corpus generator; exact metrics `q`, `R`, `H`, `beta`, `I_cap`, carry activation features; ranked extremal tables; minimal counterexamples to every tested inequality; candidate infinite families where visible; and return `research_returns/ABC_ENTERPRISE_ADVERSARIAL_CENSUS_RETURN_20260827.md`.

## Research value to preserve

A dedicated falsification lane prevents ABC1-ABC3 from overfitting to celebrated abc examples and can kill structurally wrong inequalities before proof effort is spent.

## Success, kill, and return criteria

Return one of `CENSUS_FROZEN_WITH_NOGO_CERTIFICATES`, `CENSUS_FROZEN_NO_COUNTEREXAMPLE_IN_RANGE`, `EXACT_INFINITE_OBSTRUCTION_FAMILY`, `PARTIAL_WITH_EXACT_BLOCKER`. Any finite-range survival must be labeled finite evidence only; a single exact counterexample kills the corresponding universal inequality.
