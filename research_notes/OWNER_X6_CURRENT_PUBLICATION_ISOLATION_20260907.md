# Six current X6 publications: exact fail-closed isolation

Date: 2026-09-07. Classification: `NO_NEW_MATHEMATICS_CONTROL_PLANE_ONLY`.
Role: owner-directed, ANCHOR_EXPOSED internal control helper; no official Researcher-ID, claim or V2 review authority.

## Decision and scope

This change **newly blocks six invalid current publications**. It does not claim that they were already nonoperational historical records. Owner chose the existing current-task integrity quarantine while complete research semantics are prepared for ordinary authorized V2 superseding publications.

Only six rows were appended to `control_plane/task_integrity_quarantine_addendum_20260902.json`, using its existing `ENTERPRISE_MATH_TASK_INTEGRITY_QUARANTINE_V1` schema. The previous seven rows and every pre-existing top-level field remain unchanged. No validator, original publication, original taskbook, claim event or unrelated task was changed. All authority-grant flags remain false; each `operational_publication_id` is null.

The read-only diagnosis used main `fd532560af31b36c736bb4bd21e75c8326835541`. The control checkout HEAD before these uncommitted additions was `57cc1add4160049cb89dae3fcb788c2a54423dd2`. Exact relevant production helpers and all twelve target publication/taskbook files were byte-identical to the pinned main snapshot. Existing owner control changes and the concurrent router/test repairs were preserved.

## Why current-task isolation applies

Before this change, canonical bootstrap plus `research_task_records.current_records()` selected the sole ACTIVE generation for each task. `research_dispatch.merged_definitions()` exposed each as `READY / IMMUTABLE_TASK_RECORD`. No direct superseding publication, current integrity/semantic quarantine, audit-only quarantine, compatibility waiver or publication resolution matched the six targets. `research_result_records.task_result_state()` returned null for each.

Their metadata names `PO-X6-UPPER-STRUCTURE-20260906`, but there was no operational Objective head or Objective record for that ID. The existing parent Objective gate explicitly leaves state unchanged when the head is absent; this was not evidence of closure or an OPEN Objective authority.

The bounded Issue #240 check queried comments updated since the common publication time `2026-09-05T23:56:00Z`, with `per_page=20`, pages 1/2/3. Results were 20/15/0 comments, all unedited, from comment 5557417144 (2026-09-06T06:19:35Z) through 5567346519 (2026-09-07T08:00:17Z). Exact JSON `task_id` matches for these six tasks were zero. This establishes no matching post-publication events in that snapshot; it is not a claim to have replayed all pre-publication history or to hold a fresh remote write lease. Root must recheck relevant live authority before publication.

Audit-only isolation presently does not apply: its supported independent bases are direct same-task supersession or publication-fork blocking. Heading-alias compatibility also cannot supply missing complete exit semantics. The existing current-task integrity mechanism is the correct explicit local block for these sole invalid current heads.

## Exact record and taskbook pins

All identifiers below include the `RS-X6-` task prefix. Record paths are `research_task_records/<task-id>/<publication-id>.json`. Taskbook paths are the corresponding existing `research_tasks/RS_X6_<TASK_SUFFIX>_20260906.md` files. Hashes in the two right columns are Git blob SHA-1, with `sha1:` prefixes in the manifest.

| Task suffix | Publication | Record blob | Taskbook blob |
| --- | --- | --- | --- |
| CELL-CHANNEL-INTERNAL-STATE | TP2-B5E2097A3C6418DF42E5 | 6a7e07fc9c3229f8480ac6a62f8821bdbe7d3baa | 72daccfc33a8aa1572a69416a7c2052f38745fc1 |
| NATIVE-ROTATION-DYNAMICS | TP2-6A1F9D8C2047E3B51C01 | c6a1d09d7f513f4ad5e9f04445225ece49b38050 | 448120b04ecdadf44d8a06516605bfcca94474a1 |
| NATIVE-TIME-DYNAMICS | TP2-91D4A7C2F63805BE21A3 | f6139c919f375176117a1c7c6f58dc895daecde2 | eba80ae0be492033f9eda082aac2b017f7398114 |
| NONFCC-SLICE-REALIZATION | TP2-A3C8E1D754209B6F31D4 | b4769da0e58f72288aca3027efbefd7d622f4cfd | fab0109c7959faf249ea0c9383f8b12f584fe1c9 |
| TRIADIC-CLOSURE-DYNAMICS | TP2-8B7E13C5904A2D6F1142 | 4a93d8dd46803ff6afb9b9933f36b8e4ab66fa04 | 218bf9ce05fd2dd79f477ac269fc3590f83f482e |
| UPPER-STRUCTURE-INTEGRATION | TP2-C7F31A8D520B49E653F6 | c106778f518eb30d464dbf3799362ed6a37fdfe5 | b9a5979e5c10169badf13c0ff643f0a6f8c203bd |

Each row pins exactly these four existing strict-audit suffixes:

```text
mandatory body section is missing or empty: Frozen inputs and scope
mandatory body section is missing or empty: Hard target and required outputs
mandatory body section is missing or empty: Research value to preserve
mandatory body section is missing or empty: Success, kill, and return criteria
```

Existing target content and `research_value` JSON fields are source material for a future corrected publication. This isolation does not invent its success, kill or return criteria and does not claim the research objectives are complete.

## Verification and its boundaries

`python -m unittest discover -s tests -p test_x6_current_publication_integrity_isolation.py -v` passed **7 tests in 16.114 seconds**. The tests verify:

- Exact validated task/publication/blob/error bindings and false authority flags.
- Before/after manifest views reconstructed in memory: 193 total definitions, exactly six changed; all 187 unrelated definitions and all remaining current-publication records equal. Selected current publications changed from 166 to 160.
- Six resulting definitions and reducer projections are BLOCKED with `publication_id=None`, `claim_id=None`, and the original publication retained only as the fault pin.
- An unrelated authenticated CLAIM fixture retains the same winner and LEASED state before and after. Its real parser, server-author authorization, publication binding and reducer run; only its absent Result/intent/cohort lifecycle is fixed as a fixture. This is a regression test, not a newly posted or observed claim.
- Removing the six new rows in memory restores exactly the 24 original envelope errors. With the validated rows, the envelope audit returns no errors.
- Record and taskbook pin drift fail validation. Missing or invented suppression entries fail the strict error-set audit. A new bad record in a temporary fixture cannot inherit any existing exact-path exception.

The initial CLAIM fixture lacked `author_association=OWNER` and was correctly rejected by the existing authorization gate. Only the fixture was corrected, and it now explicitly verifies `control_authorized`; no permission assertion or gate was weakened.

An additional **48 existing tests passed in 7.234 seconds**, covering `test_task_integrity_fault_isolation` (4), `test_superseded_task_integrity_lifecycle` (3), `test_publication_quarantine_lineage_forward_safety_unittest` (3), `test_control_plane_adversarial_simulation` (16), `test_research_dispatch_event_envelope` (8), `test_research_runtime_lane_authority` (6), `test_current_control_authority_dispatch` (4), and `test_legacy_control_dispatch_event_boundary` (4).

Actual early checker output:

```text
post-cutover publication envelope audit: OK (current invalid publications blocked=30; nonoperational immutable audit defects pinned=28; all other records require canonical envelope/blob/body preflight)
```

After canonical `research_control_bootstrap.install()`, `research_task_records.audit()` returned `[]`; all current quarantine suppressions were members of `research_task_records.strict_audit()` (unused count 0), and `isolation.audit_runtime_projection()` returned `[]`.

The early envelope checker alone does **not** validate exact error-set exhaustion: current quarantine validation there binds the sole head, record/taskbook bytes and required fields, then recognizes exact known defect paths. The strict audit/suppression check must also run. An invented or removed error is caught by those existing strict checks and by the regression tests above. Running the current-task isolation module alone leaves existing audit-only historical errors visible; it is not the canonical aggregate audit. No existing validation layer was changed or silently treated as equivalent to another.

All twelve frozen target files were re-compared against `fd532560af31b36c736bb4bd21e75c8326835541`; differences were empty. No commit, remote write or Issue event was made by this work package.

## Restoration contract and source binding

Restoration requires ordinary authorized complete V2 publications with exact supersedes edges and an explicit quarantine lifecycle update. A corrected generation changes the sole active head, so retaining the old current-task quarantine unchanged must fail. After valid direct supersession, the old frozen defect may be handled by the existing audit-only historical mechanism; this note grants no permission to manufacture research semantics, choose an Objective or promote mathematics.

SHA-256 at this validation checkpoint:

- `control_plane/task_integrity_quarantine_addendum_20260902.json`: `4641aa092610401d1b1d098bb05d4513eea1b21fa97afccc6cfb172f8aaf1a24`.
- `tests/test_x6_current_publication_integrity_isolation.py`: `b20b78dd4908d94fc16378ac77d1ca2f93c63af4e47ffa4fd12746a70aaf2490`.

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
