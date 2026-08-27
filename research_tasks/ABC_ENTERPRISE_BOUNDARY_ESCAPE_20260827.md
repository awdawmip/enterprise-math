<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ABC-ENTERPRISE-BOUNDARY-ESCAPE",
  "title": "ABC Enterprise Boundary-Escape Regime",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "Classify the high-beta regime where one addend is small and determine the strongest rigorous abc-quality control obtainable from boundary escape plus existing S-unit/small-addend methods.",
  "next_action": "Translate beta thresholds into explicit min(a,b)/c ranges, separate unconditional theorems from conjectural inputs, and derive the best quantitative quality envelope in each boundary band.",
  "dependencies": [],
  "source_refs": ["definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md@c7a5a1c148f48f3c9d57cafe79536030541ed2d5"],
  "evidence_status": "DIRECT_USER_DIRECTION / ABC_ENTERPRISE_PLANE_DECOMPOSITION_FROZEN_IN_CONVERSATION",
  "last_progress_ref": "Parent analysis derived beta as an exact boundary-escape term and proved the excess tower-height bound D_sup <= 2 beta + log 16.",
  "last_progress_at": "2026-08-27T08:02:00+00:00",
  "hard_block": null,
  "tags": ["abc","boundary","small-addend","s-unit","abc3"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ABC-ENTERPRISE-BOUNDARY-ESCAPE",
  "parent_objective_id": "ABC_ENTERPRISE_PLANE_RESEARCH_20260827",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "ABC3",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4","review_state":"PASS","temporary_overrides":[]}
}
-->

# ABC Enterprise Boundary-Escape Regime

Status: `PUBLISHED_REGISTERED / READY / DIRECT_USER_DIRECTION`

## Mother question

Can the high-boundary-escape region be isolated sharply enough that existing rigorous small-addend/S-unit methods control it, leaving the interior capped-core problem with a clean beta restriction?

## Frozen inputs and scope

Use primitive triples `a+b=c`, the exact beta definition and boundary-payment inequality from the parent analysis, plus current rigorous external arithmetic theorems only after checking their hypotheses. Distinguish unconditional results from conjectural or abc-dependent inputs.

## Hard target and required outputs

Hard target: `ABC_BOUNDARY_REGIME_ENVELOPE_FROZEN`.

Required outputs: explicit beta-to-small-addend conversion; a partition into quantitative boundary bands; best proved quality/radical envelope in each band; exact uncovered gap; and return `research_returns/ABC_ENTERPRISE_BOUNDARY_ESCAPE_RETURN_20260827.md`.

## Research value to preserve

A clean boundary theorem prevents the interior route from silently discarding exceptional triples and separates genuinely geometric escape from the harder repeated-prime core.

## Success, kill, and return criteria

Return one of `THEOREM_PROVED`, `WEAKER_THEOREM_PROVED`, `EXACT_OBSTRUCTION`, `FINITE_EVIDENCE_ONLY`, `NO_PROGRESS_WITH_EXACT_BLOCKER`. Kill any argument that cites abc itself, assumes the desired radical bound, or mixes conjectural and unconditional regimes without typing them.
