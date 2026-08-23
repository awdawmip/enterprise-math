<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "GS-PRIME-FUSION-EVIDENCE-TYPED-PACKAGE-INTEGRATION",
  "title": "Prime Fusion — Evidence-Typed T1–T15 Package Reconciliation and Integration",
  "kind": "GOVERNANCE",
  "owner": "integration/prime-fusion-evidence-typed-package",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "PRIME_FUSION_EVIDENCE_TYPED_PACKAGE_CURRENT_MAIN_READY_OR_SPLIT",
  "next_action": "Reconcile the source T1–T15 package with the accepted blind-core and targeted phase-extension reviews, narrow T10 to the channel-oriented mixed locus, preserve theorem-by-theorem evidence strength, and produce either one publication-ready evidence-typed package or an explicit core/extension split without adding mathematics.",
  "dependencies": [
    "research/prime-fusion-theorem-package-clean@e5138e17f8c4009f5e357f43326f2812c9df1359",
    "driver_reviews/PRIME_FUSION_INDEPENDENT_REPLICATION_DRIVER_REVIEW_20260823.md@be07e5d9af0ca428ae74c2807fdde586d0d665a3",
    "driver_reviews/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_DRIVER_REVIEW_20260823.md@ffaf098cb612f8a54f1d49df33484d3d36019a92"
  ],
  "source_refs": [
    "PR #597@e5138e17f8c4009f5e357f43326f2812c9df1359",
    "driver_reviews/PRIME_FUSION_INDEPENDENT_REPLICATION_DRIVER_REVIEW_20260823.md@be07e5d9af0ca428ae74c2807fdde586d0d665a3",
    "driver_reviews/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_DRIVER_REVIEW_20260823.md@ffaf098cb612f8a54f1d49df33484d3d36019a92"
  ],
  "evidence_status": "DRIVER_REVIEWS_COMPLETE_READY_FOR_NO_NEW_MATHEMATICS_INTEGRATION",
  "last_progress_ref": "driver_reviews/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_DRIVER_REVIEW_20260823.md@ffaf098cb612f8a54f1d49df33484d3d36019a92",
  "last_progress_at": "2026-08-23T20:15:00+08:00",
  "hard_block": null,
  "tags": [
    "prime-fusion",
    "theorem-package",
    "evidence-typing",
    "source-reconciliation",
    "no-new-mathematics"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PFPKG",
  "origin_kind": "REPLAY_OR_INTEGRATION",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": "RS-PRIME-FUSION-INDEPENDENT-REPLICATION",
  "successor_gate": "PACKAGE_MUST_PRESERVE_EXACT_EVIDENCE_STRENGTH_AND_T10_SCOPE_REPAIR",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:9c1f03a5086432f83d1a3821893be5589124293bc5be5b14d4b7e196220271c7",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Prime Fusion — Evidence-Typed T1–T15 Package Reconciliation and Integration

Status: `READY / DRIVER_APPROVED / NO_NEW_MATHEMATICS`

Task-ID:

`GS-PRIME-FUSION-EVIDENCE-TYPED-PACKAGE-INTEGRATION`

Intended owner branch:

`integration/prime-fusion-evidence-typed-package`

Hard target:

`PRIME_FUSION_EVIDENCE_TYPED_PACKAGE_CURRENT_MAIN_READY_OR_SPLIT`

## 1. Purpose

The arithmetic core blind replay is accepted. The previously missed T3/T6/T10/T11 cluster has now received targeted independent verification, with mandatory scope narrowing for T10. The remaining work is source reconciliation, evidence typing, and package construction—not theorem discovery.

This task must not claim that all fifteen theorems were independently reconstructed at exact source strength. The controlling evidence matrix is:

- exact/equivalent blind convergence: T1, T2, T5, T9, T12, T13, T14, T15;
- substantial partial blind convergence: T4, T7, T8;
- targeted independent verification: T3, T6, T10, T11;
- mandatory T10 repair: four powers describe the channel-oriented mixed locus / `U(12)` orbit, not necessarily all roots of the fused polynomial modulo `pq`.

No material source-theorem counterexample remains after that repair.

## 2. Exact integration duties

### A. Theorem-by-theorem evidence ledger

For T1–T15 record separately:

- source proof status;
- blind independent reconstruction status;
- targeted verification status;
- checker coverage;
- scope repair or strengthening;
- classical-prior-art boundary.

Use labels that cannot be mistaken for one another, including `SOURCE_PROVED`, `BLIND_EXACT`, `BLIND_PARTIAL`, `TARGETED_EXACT`, `TARGETED_NARROWED`, and `FINITE_CHECK_ONLY` as applicable.

### B. Mandatory T10 source repair

The integrated T10 statement must define the channel-oriented mixed locus explicitly. It must not state or imply that

`{r,r^5,r^7,r^11}`

is the complete root set of the full fused polynomial modulo every admissible `pq`.

Retain the exact pressure case from the accepted Driver review as a regression/wording guard.

### C. Dependency graph repair

Preserve the accepted non-linear dependency facts:

- T6 need not depend on the product-ring interpretation T3;
- T10 follows from local orders plus CRT and need not depend on T3;
- T11 does not require completeness of the T10 orbit;
- V6 and V11 channel splits are equivalent on odd channels through the accepted identity.

Do not force the late layer into an inaccurate linear proof chain.

### D. Package shape decision

Return exactly one:

1. `ONE_EVIDENCE_TYPED_FIFTEEN_THEOREM_PACKAGE_READY` — one package is retained, with theorem-level badges and T10 narrowed;
2. `CORE_AND_EXTENSION_SPLIT_REQUIRED` — arithmetic core and fusion/phase extension are published separately with an explicit interface;
3. `SOURCE_CONFLICT_REQUIRES_NEW_RESEARCH` — only if exact source comparison finds a substantive conflict not covered by the accepted reviews;
4. `INTEGRATION_BLOCKED_BY_UNRESOLVED_SCOPE`.

Evidence typing is sufficient for option 1; do not open another verification task merely to replace honest `BLIND_PARTIAL` labels for T4/T7/T8.

## 3. Required outputs

Produce:

1. current-main package source, either
   `research/PRIME_FUSION_THEOREM_PACKAGE_EVIDENCE_TYPED_20260823.md`
   or an explicitly named core/extension pair;
2. `research/PRIME_FUSION_T1_T15_EVIDENCE_MATRIX_20260823.csv`;
3. `research/PRIME_FUSION_DEPENDENCY_GRAPH_20260823.md`;
4. a reconciled checker entrypoint that runs the source checker, independent-core checker, and targeted-extension checker without duplicating their logic;
5. `driver_reviews/PRIME_FUSION_EVIDENCE_TYPED_PACKAGE_INTEGRATION_REVIEW_20260823.md`;
6. reference-integrity and artifact-digest records required by current repository policy.

PR `#597` must remain Draft or be superseded explicitly; do not silently mutate its historical evidence state.

## 4. Hard boundaries

This task must not:

- add T16/T17 or any new theorem;
- upgrade T4/T7/T8 from partial blind convergence without new evidence;
- call finite checker coverage a proof;
- claim factorization speedup, prime asymptotics, or historical novelty;
- erase the T10 pressure case;
- merge source, replication, and comparison evidence into one undifferentiated status;
- change Foundation mathematics.

Kill condition:

If the integrated wording cannot preserve both the corrected T10 scope and theorem-level evidence typing, return `CORE_AND_EXTENSION_SPLIT_REQUIRED` rather than weakening the record.

## 5. Stop condition

Stop when one package shape is frozen, all fifteen statements have exact evidence labels, T10 is repaired, the dependency graph is accurate, and the combined checker/references pass. Formalization is a later gate.
