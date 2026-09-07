# Independent audit: five unresolved publication forks

Status: PASS for the exact local snapshot and seven author files below. This is auxiliary review by `/root/stability_research`, not a publication, claim, mathematical result, or live task ownership declaration. No implementation, event, source publication, taskbook, commit, or remote was changed by this reviewer.

Baseline: `16cc5663c191a73e997e3a973f589197d0694c89`, worktree `D:/em/integration-owner-control-20260907`. The worktree also contains the separately owned control integration delta; this audit does not attribute that delta to the fork-patch author or certify a future main snapshot.

## Finding and scope

The patch removes five invalid operational selections and applies the existing exact `UNRESOLVED_PUBLICATION_FORK` contract. It grants no selection or synthesis. All five tasks have canonical selection `None`, no current record, and BLOCKED definition/reducer projections. Raw strict selection still rejects each unresolved multihead. Passing the isolation-aware aggregate/checker therefore means a valid, closed control boundary; it does not mean the forks have been resolved or their mathematical results revoked.

Every row has `operational_publication_id: null`, `isolation_scope: CONTROL_PLANE_ONLY`, and exact false values for `working_truth_granted`, `foundation_authority_granted`, `canonical_promotion_granted`, and `successor_triggered`. Exact rows omit `tracking_mode` and `lineage_anchor_publication_ids`.

Independent reconstruction from immutable records gives these complete active-head sets:

| Task | Active publication IDs |
|---|---|
| `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE` | `TP2-3F6A92D8C1E740B5A2C9`, `TP2-4A84B81FD5CAB8CD0359`, `TP2-FBDBDBE1C5BDF65F97A0` |
| `RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N13-COLLISION-FRONTIER` | `TP2-2BB590EA80230A7A7D4C`, `TP2-6C812E92A7C937795A59` |
| `RS-P022-OBSERVATION-HISTORY` | `TP2-2346F5D3E731ED56DB0A`, `TP2-D78DBA0243911E0363FA`, `TP2-DE338F269CA11E9BC01B` |
| `RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF` | `TP2-3EAC29B49F71ABB92BEA`, `TP2-5547117E54D7A556279B` |
| `RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE` | `TP2-9D0A43C4F217B6E8C531`, `TP2-A63015C2EB99D00F2500` |

The existing contract is enforced by `control_plane/research_publication_fault_isolation.py:48` (row authority/type), `:140` (exact live-head match), and `:268` (blocked definition). No validator was changed. Added/removed heads, residual resolution rows, authority flags, unrelated forks and unrelated malformed records remain rejected by real validators in the tests.

## Preservation and P022 lifecycle

Compared directly with baseline Git objects: all 33 historical record files for these five tasks and all 12 current-head taskbooks retain identical bytes; each current book's declared Git-blob pin matches recomputation. The four registries change only their authorized arrays: fork quarantine 0 to 5, resolution 5 to 0, compatibility waiver 3 to 2, base audit quarantine 27 to 28. Top-level metadata is unchanged. Both remaining waiver objects and all 27 prior audit-quarantine objects retain exact original object bytes.

The author note's first JSON block equals the complete original five-resolution array, including reasons, timestamps, authority identifiers, aliases and preserve-existing-result/claim fields. Original registry bytes remain at baseline blob `bbe64c5c8c4da5a501ccb52bdf62d702001789fb` (SHA256 `177fb25aa8420c7ebb9c93e69d591917781e520a45061cbb36fd440883786eff`). Markdown history is outside runtime registries; no old selection is silently reactivated.

The only same-cause compatibility dependency among the five tasks is `TRCW-P022-D78-LEGACY-HEADINGS-20260827`. The former alias waiver requires a retained/superseded nonoperational publication and a different current operational witness (`tools/research_task_records.py:205`, especially `:251` and `:272`). Removing the invalid resolution removes that eligibility. Keeping a fake resolution to sustain the waiver would be incorrect.

The replacement row `TRAQ-P022-D78-FORK-BLOCKED-BODY-20260907` uses the already implemented `TASK_BLOCKED_BY_PUBLICATION_FORK_QUARANTINE` basis (`control_plane/research_task_record_audit_fault_isolation.py:42`, `:235`). It is nonoperational, history-preserving, has all four authority flags false, and pins:

- Record `research_task_records/RS-P022-OBSERVATION-HISTORY/TP2-D78DBA0243911E0363FA.json`: `sha1:a7fb4c39766e8895306e21938da35f4a919cb9ef`.
- Book `research_tasks/P022_OBSERVATION_HISTORY_FORCED_MIDPOINT_FALLBACK_REPLAY_20260827.md`: `sha1:15b495b7a21af748260363a6969097abe1f79611`.

Direct original-book validation reproduces exactly four missing-or-empty mandatory-section suffixes: `Frozen inputs and scope`, `Hard target and required outputs`, `Research value to preserve`, and `Success, kill, and return criteria`. These four errors remain explicitly recorded. The row adds no envelope-error permission. Pin validation is at `research_task_record_audit_fault_isolation.py:181`; fork membership at `:235`; stale/unused or extra-error detection at `:270`. Removing the fork basis, changing either pin, or changing/adding errors fails the relevant validation.

The complete old P022 waiver is the author note's third JSON block and equals its original baseline row. Original registry blob `cb786726040fbaab649a849440397e0911b45927` has SHA256 `baca99efa0d28cfad11916a789d2789df3750818fadd0a398ac97097dd091e4b`. This migration records the current nonoperational integrity condition without claiming the historical alias waiver was invalid when originally used.

The lineage test change dispatches on exact versus lineage-forward type. Its existing anchor/ancestry safety assertions are retained; exact isolation receives a full three-head/no-selection check. No test is skipped and no false lineage anchor is introduced.

## Independent verification

All commands/checks below ran in the named worktree, against the frozen production bytes. Author-run reports were not substituted for reviewer execution.

- `python -B -X utf8 control_plane/check_publication_fault_isolation.py`: exit 0, PASS. This is the standalone CI gate, not just an aggregate report.
- `python -B -X utf8 -m unittest tests.test_publication_fault_isolation -v`: 3/3 PASS.
- `python -B -X utf8 -m unittest tests.test_owner_unresolved_publication_forks_20260907 tests.test_publication_quarantine_lineage_forward_safety_unittest -v`: 13/13 PASS (10 new, 3 existing).
- Installed `research_control_bootstrap` and called canonical `research_task_records.audit(ROOT)` and `research_operational_publications.audit(ROOT)`: both returned `[]`. For every target, canonical current/selection and `research_dispatch.merged_definitions`/`reduce_definition` were checked independently. The reducer used an explicitly empty event list as a deterministic contract probe, not as a claim about live event history.
- Compared frozen SHA256 values, baseline JSON structure and unchanged object bytes, actual head sets, source record/book bytes and book blob pins. Parsed author-note evidence blocks and compared them with baseline originals.
- Scoped `git diff --name-only HEAD` over source record/taskbook directories, publication/audit validators, compatibility code, bootstrap, standalone checker and CI workflow returned no changed paths. No implementation-wide relaxation accompanies the data repair.

## Frozen author files

| Path | SHA256 |
|---|---|
| `research_task_publication_quarantines.json` | `2486ce2d0a7995fab99ebebdd50a09d39829ebbac4625af4b7eadcfbeaf8e95c` |
| `research_task_publication_resolutions.json` | `ea9261c939b359fb5959e5689495247c7a86382113cb76d37c0fe5b66adb72a2` |
| `research_task_record_compatibility_waivers.json` | `1097c5d45a19d36cc90974adbaba3eb92b88d83967d33dfd3c8829dd1f1d5f05` |
| `research_task_record_audit_quarantines.json` | `c3d43814f05cc8446939afd3345da98eee09ed2ce0d43676680aaee9f7af8547` |
| `tests/test_publication_quarantine_lineage_forward_safety_unittest.py` | `8eeb2d8cbef3d200ec117f02d72baeeff2a3d0908e4caa635c8dcb495e6fa48e` |
| `tests/test_owner_unresolved_publication_forks_20260907.py` | `97ca0928dbba84956941ed815e9898c9155d40415e645136e136db6aad6cfa2e` |
| `research_notes/OWNER_UNRESOLVED_PUBLICATION_FORK_ISOLATION_20260907.md` | `aa7de36dc0883948964a9f75293b98ecdd7268b7ba80fcc4809c9c1bcdda4b59` |

No blocking finding remains in this patch. Restoring an operational publication still requires a valid existing reference-pass/synthesis selection and coordinated retirement of the corresponding exact fork quarantine and any now-invalid dependent audit row. A later snapshot or head-set change requires fresh validation.

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
