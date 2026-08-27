<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P018-TERNARY-CARRY",
  "title": "P018 Exact Ternary Quotient-Root Carry Completion — Current-Policy Replay",
  "kind": "RESEARCH",
  "owner": "program/p018-precision-v2",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Complete the exact threshold-to-cardinality layer for the P018 quotient-root atlas by turning the already-proved high/low/horizon realization lemmas into a finite-set atlas decomposition and then specializing the existing ternary carry partition to the exact state-count formula.",
  "next_action": "Resume from Draft PR #328 current head 9b5ec8d1190bf14f00309df421e51734c36b2f24. Define the finite positive quotient-root atlas, prove its disjoint high/low/optional-horizon decomposition and cardinality N+1=D+H+kappa, then instantiate ternary_count_from_binary_carry and warning-fatal-check the resulting theorem without sorry/admit.",
  "dependencies": [
    "legacy research_scheduler.json RS-P018-TERNARY-CARRY frozen baseline",
    "Issue #240 HANDOFF comment 5234892334",
    "Draft PR #328 current head 9b5ec8d1190bf14f00309df421e51734c36b2f24",
    "PR #226 ternary carry predecessor",
    "PR #228 exact quotient-root denominator fiber predecessor"
  ],
  "source_refs": [
    "EnterpriseMath/Precision/RootStateAtlasCardinality.lean@research/p018-ternary-atlas-cardinality",
    "EnterpriseMath/Precision/RootStateCountCarryExact.lean@research/p018-ternary-atlas-cardinality",
    "EnterpriseMath/Precision/TernaryBandCarryCount.lean@research/p018-ternary-atlas-cardinality"
  ],
  "evidence_status": "LEGACY_HANDOFF_REPLAY / ORDINARY_MATHEMATICS_REPORTED_CLOSED / FINAL_FINSET_AND_LEAN_THEOREM_OPEN",
  "last_progress_ref": "Issue #240 HANDOFF 5234892334 plus Draft PR #328 current head 9b5ec8d1190bf14f00309df421e51734c36b2f24",
  "last_progress_at": "2026-08-27T11:29:00+08:00",
  "hard_block": null,
  "tags": ["P018","precision","quotient-root","ternary-carry","Finset","Lean","legacy-migration"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P018-TERNARY-CARRY",
  "parent_objective_id": "P018_QUOTIENT_ROOT_PRECISION_COMPLETION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P018TC",
  "origin_kind": "REPLAY_OR_INTEGRATION",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:497a0467870c4d495d4dbf161cf492e9d3d4a51d0a7b34e685086f25daa395f4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P018 Exact Ternary Quotient-Root Carry Completion — Current-Policy Replay

Status: `PUBLISHED_REGISTERED / REPLAY_OR_INTEGRATION / REPLAY`

## Mother question

For positive state `n` and root-order parameter `s+1`, complete the exact finite quotient-root atlas theorem that the legacy P018 task left at HANDOFF: prove the distinct positive root-state count from the already-closed high-denominator branch, all positive roots below the coalescence horizon, and the single optional horizon state; then reduce that exact binary count through the already-proved ternary carry partition.

The intended terminal theorem is the exact threshold-to-cardinality formula, not another denominator-band estimate and not an asymptotic approximation.

## Frozen inputs and scope

Use the current head of Draft PR #328, `9b5ec8d1190bf14f00309df421e51734c36b2f24`, as the replay source. The following mathematics is frozen input and must not be reproved unless a contradiction is found:

- the exact quotient-root denominator fiber;
- the three-point denominator band for `D`;
- the forced lower/upper carry cases;
- high denominators `1..D` produce roots strictly above `H`;
- the high branch is injective;
- every positive root `t<H` is realized;
- the horizon root `H` is realized exactly under its one carry threshold;
- `ternary_count_from_binary_carry` converts a correct binary atlas count into the three-valued threshold formula.

The replay may introduce only the finite-set object needed to state the atlas and the proof glue needed for exact cardinality. No prime, asymptotic, continuum, physical, or historical-priority claim is in scope.

## Hard target and required outputs

Hard target:

`P018_TERNARY_THRESHOLD_TO_CARDINALITY_EXACT_AND_LEAN_CHECKED_NO_SORRY`

Required outputs:

1. an exact finite definition of the positive quotient-root atlas for fixed `(s,n)`;
2. a proof that its high branch has exactly `D` states;
3. a proof that the low strict branch is exactly `{1,...,H-1}`;
4. a proof that `H` is the only optional low state and is present exactly at the frozen carry threshold;
5. the exact binary count in subtraction-free form `N+1=D+H+kappa`;
6. the exact ternary threshold-to-cardinality theorem obtained from `ternary_count_from_binary_carry`;
7. warning-fatal Lean validation on the pinned EnterpriseMath build, with no `sorry`, `admit`, or custom axiom;
8. a durable return at `research_returns/P018_TERNARY_CARRY_THRESHOLD_TO_CARDINALITY_RETURN_20260827.md` plus the exact changed Lean file(s) and any finite regression certificate used.

## Research value to preserve

This closes an old P018 semantic/combinatorial frontier that already has all difficult local inequalities proved. The remaining value is not another empirical scan: it is to turn the high/low/horizon geometry into one exact cardinality theorem and thereby close the quotient-root threshold-to-cardinality layer in a reusable formal form.

The result is also a clean test of whether the ternary carry theorem is genuinely downstream of the binary atlas decomposition rather than dependent on hidden analytic or geometric assumptions.

## Success, kill, and return criteria

Success is a warning-fatal Lean-checked theorem with the exact atlas count and its ternary specialization, no weakened hypotheses beyond those already required by the frozen predecessor theorems, and no use of `sorry`, `admit`, or custom axioms.

Kill or narrow the route if the current high/low/horizon lemmas do not actually imply a disjoint exhaustive atlas decomposition, if a small exact counterexample is found, or if the desired theorem requires a new unproved arithmetic premise. In that case freeze the smallest exact missing lemma or counterexample rather than masking it with computation.

Finite scans are regression/falsification only. Task completion requires the general exact argument and durable return.
