<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-PHILOSOPHY-FIRST-NONLOCAL-PROBE-JOINT-SEPARATION",
  "title": "哲学先行 Q9：最弱非局部探针与联合分离",
  "kind": "RESEARCH",
  "owner": "research/p000-phil-q9-nonlocal-probe-joint-separation",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "After Q2 and Q6, fixed-radius local observations are neither reconstruction-complete nor representability-complete. Determine the weakest P000-native nonlocal observation that separates the known indistinguishable families and rejects known virtual profiles without encoding native identity by fiat.",
  "next_action": "Freeze the exact Q2/Q6 countermodels, define at least three candidate nonlocal probe families, and compare them by exact separation, representability, minimality, and invariance tests.",
  "dependencies": [
    "RR-5C9238DB872A93F13D37",
    "RR-49FC19221CA5D69B00E6",
    "RR-1C8E7A4F2B9D6053E126",
    "RR-4B0C6E0CAEE305D5B844"
  ],
  "source_refs": [
    "RESEARCH_DOCTRINE.md",
    "driver_reviews/P000_PHILOSOPHY_FIRST_Q1_Q8_DRIVER_REVIEW_20260830.md",
    "RR-5C9238DB872A93F13D37",
    "RR-49FC19221CA5D69B00E6",
    "RR-1C8E7A4F2B9D6053E126",
    "RR-4B0C6E0CAEE305D5B844"
  ],
  "evidence_status": "DRIVER_ACCEPTED_PHILOSOPHY_FIRST_Q1_Q8 / SECOND_WAVE_UNEXECUTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "P000",
    "philosophy-first",
    "probe",
    "nonlocal",
    "reconstruction",
    "representability",
    "path",
    "holonomy"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-PHILOSOPHY-FIRST-NONLOCAL-PROBE-JOINT-SEPARATION",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PHQ9",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 哲学先行 Q9：最弱非局部探针与联合分离

Status: `READY / P0 / PHILOSOPHY-FIRST-SECOND-WAVE`

## Mother question

Q2 proved that every fixed finite radius misses an unbounded family such as `C_(2m)` versus `C_m disjoint_union C_m`; Q6 proved that the same restricted observation language also admits formal profiles with no native realization. The next question is not “which fancy probe should we add?” but:

**What is the weakest P000-native nonlocal observation that simultaneously reduces noninjectivity and nonsurjectivity, while not smuggling native Cell identity into the observable?**

Candidate mechanisms may include adaptive radius, path/transport signatures, overlap-composition data, or holonomy/groupoid summaries, but none is assumed to be correct.

## Frozen inputs and scope

Freeze Q2/Q3/Q4/Q6 only at their reviewed declared scopes. P000 remains six-dimensional discrete Cell space plus relational time. Carrier `S4`, K4/FCC, graph connectedness, path labels, and holonomy are not automatically native primitives.

The task must compare at least three candidate probe families on exact finite model classes. A candidate probe must be definable from declared P000-native or explicitly enriched relational data, invariant under the allowed model equivalences, and weaker than full identity lookup. Classical graph reconstruction, groupoid, and descent language may be used only after the native probe semantics are stated.

## Hard target and required outputs

Hard target: `P000_NONLOCAL_PROBE_JOINT_SEPARATION_OR_NO_GO_CLASSIFIED`.

Required outputs:

1. Exact definitions of at least three candidate nonlocal probe families.
2. For each candidate, a proof/check whether it separates the Q2 `C_(2m)` versus `2 C_m` family at a stated parameter range.
3. For each candidate, a representability test against the Q6 virtual profile mechanism, including at least one explicit formally compatible but unrealizable profile or a proof that the candidate removes it at the tested scope.
4. A minimality comparison: identify information retained by the strongest successful candidate that is absent from each weaker failed candidate.
5. At least one negative certificate showing a plausible nonlocal summary that still fails.
6. A final joint-separation verdict: exact success scope, exact remaining indistinguishability kernel, or a no-go proving that the tested probe class cannot be jointly conservative.

## Research value to preserve

This is the first task that asks whether the accepted philosophy-first results can recover genuinely global Cell information without simply declaring the full object observable. A successful minimal probe could become the first native tomography/reconstruction interface connecting observation, path structure, and gluing.

## Success, kill, and return criteria

Success: one candidate probe is proved jointly stronger in a precise finite scope, splitting the known Q2 collision family and shrinking or eliminating the tested Q6 virtual sector, with invariance and minimality certificates.

Kill/no-go: every tested candidate either fails exact separation, fails representability, or is shown equivalent to encoding native identity by fiat. Such a no-go is terminal and valuable.

Return must preserve all failed candidates and countermodels. Do not escalate to a higher categorical language unless an explicit lower-language failure remains after the probe semantics are fixed.
