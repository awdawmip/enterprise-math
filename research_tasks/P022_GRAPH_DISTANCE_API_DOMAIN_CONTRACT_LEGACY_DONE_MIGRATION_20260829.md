<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P022-GRAPH-DISTANCE-API",
  "title": "P022/P012 graph-distance API legacy DONE migration",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "DONE",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Legacy durable frontier recovered: the graph-distance API/domain task completed on 2026-08-10 with PR #431 and FQ-20260809-005 return evidence; no fresh research execution remains.",
  "next_action": "Consume the existing layered API result and do not redispatch this task unless a new foundation question creates a distinct information gap.",
  "dependencies": [
    "P012 intrinsic discrete geometry theorem-domain statement",
    "current src/enterprise_math/geometry.py graph_distance implementation and exports"
  ],
  "source_refs": [
    "foundation question FQ-20260809-005",
    "docs/P012_INTRINSIC_DISCRETE_GEOMETRY.en.md",
    "src/enterprise_math/geometry.py",
    "src/enterprise_math/__init__.py",
    "tests"
  ],
  "evidence_status": "LEGACY_DONE_MIGRATED_V2",
  "last_progress_ref": "PR #431 / ca351e5446b3a84835ade9509f1ab97c276841d9 / FQ-005 return Issue #164 comment 5242436041",
  "last_progress_at": "2026-08-10T23:35:00+08:00",
  "hard_block": null,
  "tags": [
    "P022",
    "P012",
    "graph-distance",
    "api-domain",
    "foundation-question"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P022-GRAPH-DISTANCE-API",
  "parent_objective_id": "FQ-20260809-005",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P022",
  "origin_kind": "FOUNDATION_QUESTION",
  "origin_foundation_question_id": "FQ-20260809-005",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:7ae52d1c45fefb96c7f127599c0dad100519ebc671c3c299b76174bd60760b26",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P022/P012 graph-distance API legacy DONE migration

Status: `DONE / PUBLISHED / NOT CLAIMABLE`

## 0. Mother question

What is the exact mathematical domain on which the repository's hop-count graph distance is a genuine finite metric, and how should the public API separate that theorem-facing object from a general directed shortest-walk helper?

## 1. Frozen inputs and scope

This publication records a recovered durable terminal frontier rather than opening new research. The controlling evidence is the 2026-08-10 completed execution: PR #431 frozen head `ca351e5446b3a84835ade9509f1ab97c276841d9`, FQ-20260809-005 return on Issue #164 comment `5242436041`, and the scheduler DONE event reporting exact-head quality, bilingual-sync, and reference-integrity success. Current `src/enterprise_math/geometry.py` still contains the resulting layered `directed_graph_distance` and theorem-facing `graph_distance` surface.

## 2. Hard target and required outputs

The historical hard target is already satisfied. The durable result separates literal outgoing-relation shortest directed-walk distance from the P012 undirected-simple theorem-facing distance, validates the stable API domain, and preserves explicit failure on unreachable cross-component queries. No new implementation or proof output is authorized by this terminal migration.

## 3. Research value to preserve

Preserving the recovered DONE state prevents stale static READY data or expired owner leases from causing duplicate work, while retaining the theorem/API distinction already incorporated into the source tree.

## 4. Success, kill, and return criteria

Success for this migration is terminal-state integrity: the prior result remains consumable, the stale redispatch path is closed, and any future work must arise from a genuinely new information gap under a new or superseding task. Kill any fresh attempt to repeat the 2026-08-10 graph-distance API resolution without such new evidence.
