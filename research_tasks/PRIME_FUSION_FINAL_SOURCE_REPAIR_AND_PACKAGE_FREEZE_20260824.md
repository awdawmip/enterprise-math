<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "GS-PRIME-FUSION-FINAL-SOURCE-REPAIR-AND-PACKAGE-FREEZE",
  "title": "Prime Fusion — Final Source Repair and Fifteen-Theorem Package Freeze",
  "kind": "GOVERNANCE",
  "owner": "integration/prime-fusion-evidence-typed-package",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "PRIME_FUSION_15_THEOREM_CORRECTED_SOURCE_PACKAGE_FROZEN_AND_REVIEW_READY",
  "next_action": "Consume the frozen 15-of-15 independent evidence reconciliation, repair the T10 source universe, refresh theorem-level evidence typing and the non-linear dependency graph, compose the existing checker families without duplicating their logic, freeze one corrected current package, and stop without adding mathematics.",
  "dependencies": [
    "driver_reviews/PRIME_FUSION_15_THEOREM_FINAL_EVIDENCE_RECONCILIATION_20260824.md@e19ee6713be002dd9c346261173d39fd8d54f9dc",
    "driver_reviews/PRIME_FUSION_T4_T7_T8_FINAL_EXACT_CLOSURE_DRIVER_REVIEW_20260824.md@ed016687bcd2d75957041ce820e335678aeb1f53",
    "driver_reviews/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_DRIVER_REVIEW_20260823.md@ffaf098cb612f8a54f1d49df33484d3d36019a92",
    "driver_reviews/PRIME_FUSION_INDEPENDENT_REPLICATION_DRIVER_REVIEW_20260823.md@be07e5d9af0ca428ae74c2807fdde586d0d665a3",
    "research/prime-fusion-theorem-package-clean@e5138e17f8c4009f5e357f43326f2812c9df1359"
  ],
  "source_refs": [
    "driver_reviews/PRIME_FUSION_15_THEOREM_FINAL_EVIDENCE_RECONCILIATION_20260824.md@e19ee6713be002dd9c346261173d39fd8d54f9dc",
    "research_returns/PRIME_FUSION_T4_T7_T8_FINAL_EXACT_CLOSURE_RETURN_20260823.md@5723685c3ef3b43b5fb826af3b185f142a60d0ec",
    "research_returns/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_RETURN_20260823.md@research/prime-fusion-phase-extension-targeted-verification",
    "research_returns/PRIME_FUSION_INDEPENDENT_REPLICATION_RETURN_20260823.md@research/prime-fusion-independent-replication",
    "research/PRIME_FUSION_THEOREM_PACKAGE_20260823.md@e5138e17f8c4009f5e357f43326f2812c9df1359"
  ],
  "evidence_status": "FIFTEEN_OF_FIFTEEN_RETAINED_THEOREM_ROWS_INDEPENDENTLY_AUDITED_SOURCE_TEXT_REPAIR_ONLY",
  "last_progress_ref": "driver_reviews/PRIME_FUSION_15_THEOREM_FINAL_EVIDENCE_RECONCILIATION_20260824.md@e19ee6713be002dd9c346261173d39fd8d54f9dc",
  "last_progress_at": "2026-08-24T09:51:00+08:00",
  "hard_block": null,
  "tags": [
    "prime-fusion",
    "source-repair",
    "package-freeze",
    "evidence-typing",
    "T10-scope-repair",
    "no-new-mathematics"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PFFINAL",
  "origin_kind": "REPLAY_OR_INTEGRATION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "GS-PRIME-FUSION-EVIDENCE-TYPED-PACKAGE-INTEGRATION",
  "successor_gate": {
    "new_information_gap": "The earlier integration task was authored when T4/T7/T8 still had only partial blind coverage. A later exact-closure return and Driver review now establish exact statement-exposed independent verification for T4/T7/T8, and the final reconciliation records independent audit coverage for all fifteen retained theorem rows. The remaining gap is therefore source/package accuracy, not mathematical evidence.",
    "why_parent_result_does_not_close_it": "The parent integration task freezes an obsolete evidence matrix and explicitly forbids upgrading T4/T7/T8 beyond partial status. Executing it unchanged would now understate the frozen evidence and produce an internally stale package. The corrected T10 universe also still has to be written into source text.",
    "discriminating_outcomes": [
      "one corrected fifteen-theorem package is frozen with exact theorem-level evidence types and repaired T10 scope",
      "a concrete source-text inconsistency prevents faithful integration and is recorded without inventing new mathematics",
      "artifact/reference composition fails and the package is returned blocked with the exact integrity defect"
    ],
    "kill_condition": "If source repair requires a new theorem, a new hypothesis not already present in the frozen reviews, deletion of the T10 pressure case, or conflation of blind and statement-exposed evidence, stop and return a package-blocked result rather than silently changing theorem content.",
    "alternative_route_or_free_exploration_considered": "Another replication round was considered and rejected because all fifteen retained theorem rows already have independent audit coverage. A core/extension split is no longer required merely by evidence incompleteness; it remains permissible only if source organization cannot preserve the exact corrected statements in one package.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Closure now would leave the historical theorem text with an ambiguous T10 universe, while executing the old integration task would preserve a false partial-evidence matrix. A superseding bounded continuation is the minimal way to convert the completed evidence record into an accurate frozen source package without reopening research."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Prime Fusion — Final Source Repair and Fifteen-Theorem Package Freeze

Task-ID: `GS-PRIME-FUSION-FINAL-SOURCE-REPAIR-AND-PACKAGE-FREEZE`

Owner branch: `integration/prime-fusion-evidence-typed-package`

Hard target:

`PRIME_FUSION_15_THEOREM_CORRECTED_SOURCE_PACKAGE_FROZEN_AND_REVIEW_READY`

## 0. Status and supersession

This is a bounded source/integration task. It adds no mathematics.

It supersedes the execution semantics of the earlier task

`GS-PRIME-FUSION-EVIDENCE-TYPED-PACKAGE-INTEGRATION`

because that task was frozen before T4/T7/T8 exact closure and therefore carries an obsolete evidence matrix.

The final controlling evidence statement is:

`15/15 retained theorem rows have independent audit coverage`.

Do not rewrite that as `15/15 blind replication`.

## 1. Authoritative inputs

Use the frozen sources named in task metadata. The final Driver reconciliation at

`e19ee6713be002dd9c346261173d39fd8d54f9dc`

controls theorem-level evidence labels.

The historical theorem package at

`e5138e17f8c4009f5e357f43326f2812c9df1359`

is the text to repair, not an evidence authority that can override later exact reviews.

## 2. Mandatory T10 repair

Define explicitly

`M_{p,q}={x mod pq : x^2+1=0 mod p and x^2+x+1=0 mod q}`.

The corrected theorem must state

`M_{p,q}={r,r^5,r^7,r^11}`

under the retained dual-prime hypotheses.

Do not state or imply that these four elements are always the complete root set of

`F(X)=(X^2+1)(X^2+X+1)`

modulo `pq`.

Preserve the exact pressure witness

`(a,b)=(2,3)`, `(p,q,H)=(13,7,91)`

with four oriented mixed roots and eight full fused roots as a regression guard or evidence note.

The shared-coefficient pair remains exactly

`{r,r^11}={r,r^{-1}}`.

## 3. Final T1–T15 evidence ledger

The package must record these final statuses without downgrading or homogenizing them:

- T1 `INDEPENDENT_EXACT`;
- T2 `INDEPENDENT_EXACT`;
- T3 `INDEPENDENT_EXACT_STATEMENT_EXPOSED`;
- T4 `INDEPENDENT_EXACT_STATEMENT_EXPOSED`;
- T5 `INDEPENDENT_EQUIVALENT_EXACT`;
- T6 `INDEPENDENT_EXACT_STATEMENT_EXPOSED`;
- T7 `INDEPENDENT_EXACT_STATEMENT_EXPOSED`;
- T8 `INDEPENDENT_EXACT_STATEMENT_EXPOSED`;
- T9 `INDEPENDENT_EXACT`;
- T10 `INDEPENDENT_EXACT_AFTER_SCOPE_REPAIR`;
- T11 `INDEPENDENT_EXACT_STATEMENT_EXPOSED`;
- T12 `INDEPENDENT_EXACT`;
- T13 `INDEPENDENT_EXACT`;
- T14 `INDEPENDENT_EXACT`;
- T15 `INDEPENDENT_EXACT_STRONGER_FORM`.

There are no remaining `PARTIAL` or `MISSED` rows.

## 4. Source-strength notes to preserve

Mandatory theorem truth change:

- T10 universe repair above.

Strongly preferred explanatory strengthenings, already independently proved:

- T4: component quotient SNF gives cyclicity iff `gcd(a,b)=1`;
- T6: `F(r)=0` already makes `r` a unit; reciprocal trace gives the universal idempotent factor split;
- T7: for idempotent `e`, `NC=H` and `gcd(N,C)=1` are automatic; distinguish positive-cell minimal hypotheses from strict-interior hypotheses;
- T8: distinguish abstract `F_p x F_q` ring shape from canonical Gaussian/Eisenstein channel labels;
- T11: retain the exact composite parity extension as a note, not as a replacement for the source dual-prime statement;
- T15: identify the source mean law as a special case of the independently proved all-function unimodular slice identity.

Do not introduce T16/T17.

## 5. Dependency graph

Freeze an explicit dependency graph that reflects the accepted non-linear structure:

- T6 needs the reciprocal polynomial identity and pointed/local equations; it does not logically require T3 product-ring interpretation;
- T10 follows from local orders plus CRT and does not logically require T3;
- T11 follows from the two local equations and does not require T10 orbit completeness;
- on the oriented locus, the accepted relation `x^6=2e-1 mod H` connects T6 and T11;
- T4 uses the T3 product decomposition for the product-quotient presentation;
- T7 uses the channel split and square reconstruction;
- T8 uses the quotient/channel structure plus primality/semiprime equivalence.

Do not impose a false single chain `T3 -> T6 -> T10 -> T11`.

## 6. Required artifacts

Freeze exactly one package shape unless an integrity defect forces an explicit split.

Preferred outputs:

1. `research/PRIME_FUSION_THEOREM_PACKAGE_EVIDENCE_TYPED_FINAL_20260824.md`;
2. `research/PRIME_FUSION_T1_T15_FINAL_EVIDENCE_MATRIX_20260824.csv`;
3. `research/PRIME_FUSION_FINAL_DEPENDENCY_GRAPH_20260824.md`;
4. `experiments/prime_fusion_final_package_checker.py` as a thin composition of the existing source, blind-core, phase-extension, and T4/T7/T8 checker families;
5. `research_output/evidence/PRIME_FUSION_FINAL_PACKAGE_MANIFEST_20260824.json` with source refs and artifact digests;
6. `research_returns/PRIME_FUSION_FINAL_SOURCE_REPAIR_AND_PACKAGE_FREEZE_RETURN_20260824.md`.

The composed checker must not copy theorem logic from the component checkers merely to make one larger script.

## 7. Final classifications

Return exactly one:

- `PRIME_FUSION_FINAL_PACKAGE_FROZEN`;
- `PRIME_FUSION_FINAL_PACKAGE_FROZEN_WITH_EXPLICIT_CORE_EXTENSION_SPLIT`;
- `PRIME_FUSION_PACKAGE_BLOCKED_BY_SOURCE_INTEGRITY_DEFECT`.

A new-mathematics outcome is outside this task.

## 8. Hard boundaries

Do not:

- add theorem rows;
- change Foundation definitions;
- claim asymptotic prime infinitude, historical novelty, or factoring speedup;
- erase negative controls or the T10 pressure witness;
- collapse blind and statement-exposed evidence into one label;
- downgrade T4/T7/T8 back to partial;
- use finite computation as a substitute for the already frozen proofs.

## 9. Stop condition

Stop when the corrected package, final evidence ledger, dependency graph, composed checker, manifest, and frozen return agree on the same fifteen retained theorem rows and the T10 scope ambiguity is eliminated.

Do not open another replication task from this package freeze.
