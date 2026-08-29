<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P022-GRAPH-DISTANCE-API",
  "title": "P022/P012 graph-distance API and theorem-domain resolution",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Resolve the stable API/domain layering between a general directed shortest-walk helper and the P012 connected-undirected graph metric contract.",
  "next_action": "Audit P012 theorem hypotheses and current graph-distance consumers, derive the exact domain theorem and counterexamples, then freeze a compatibility-preserving API recommendation with executable regression evidence.",
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
  "evidence_status": "TASKBOOK_PUBLISHED_V2",
  "last_progress_ref": null,
  "last_progress_at": null,
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

# P022/P012 graph-distance API and theorem-domain resolution

Status: `READY / PUBLISHED / CLAIMABLE`

## 0. Mother question

What is the exact mathematical domain on which the repository's hop-count graph distance is a genuine finite metric, and what API layering preserves the existing general shortest-walk computation without letting P012 metric statements silently range over directed or disconnected inputs?

## 1. Frozen inputs and scope

Read the P012 intrinsic discrete geometry statement, the current geometry implementation and export surface, and directly relevant tests or consumers. Treat the current implementation behavior as evidence to audit, not as a theorem. The task is limited to unweighted hop-count distance and its domain contract; weighted shortest paths, continuous geometry, and unrelated P022 semantics are out of scope.

## 2. Hard target and required outputs

Hard target: `GRAPH_DISTANCE_API_DOMAIN_CONTRACT_EXACTLY_RESOLVED`.

Return all of the following:
1. an exact theorem-level characterization separating the general directed shortest-walk object from the finite metric specialization;
2. explicit smallest counterexamples showing which metric axioms fail when symmetry or connectedness is absent;
3. an audit of current callers/tests sufficient to determine whether narrowing the existing exported function would be compatibility-safe;
4. one canonical API recommendation that states which name remains general, which wrapper or validator carries metric semantics, and how unreachable pairs are represented;
5. an executable regression checker covering asymmetric and disconnected cases plus representative valid metric cases.

Finite enumeration may support the audit but does not substitute for the theorem argument.

## 3. Research value to preserve

This task prevents a semantic type error at the P022/P012 boundary: an algorithm that computes shortest directed walks can be perfectly correct while failing to define a finite symmetric metric. Preserving the distinction lets later geometry proofs cite an explicit domain theorem while keeping general graph consumers available.

## 4. Success, kill, and return criteria

Success requires the exact domain theorem, counterexamples, consumer audit, compatibility conclusion, and executable regression evidence to agree. If current callers require incompatible semantics, do not force a rename or narrowing; freeze the conflict and recommend a layered transition. If the source surface has already been repaired by newer work, verify that repair against the same theorem and return the verified state rather than duplicating implementation work. Stop after a durable research return and immutable task result are frozen for review.
