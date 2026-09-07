# Exact invalid frozen Result control authority isolation — 2026-09-07

Status: IMPLEMENTED; AUTHOR SELF-VALIDATION COMPLETE; independent owner admission pending.

Global-Knowledge-Sync: main@ad231516 / GLOBAL_KNOWLEDGE_V1. This is internal CONTROL_PLANE_MAINTENANCE, not a formal Driver review, researcher claim, mathematical disposition, publication or canonical promotion. Root authorized the twelve-row design and the later minimal runtime-guard extension. The integration checkpoint used for the fixed public-view baseline is `2dd4c296f713f6bb3b2e509ba65104dc4a2a8ce0`.

## Scope and immutable boundary

The new registry `research_result_authority_quarantines.json` has twelve explicit rows under `EXACT_INVALID_FROZEN_RESULT_CONTROL_AUTHORITY_WITHHELD`. Each fixes the raw Result path/blob, task/publication identity, publication and execution path/blob, exact dependency path set with Git blob and SHA-256 pins, and complete raw strict error list. There are 114 distinct pinned source paths. Every registered Result must have exactly one raw-store occurrence at its canonical path; derived reviews likewise require the complete exact raw source set. Changed bytes with unchanged error text, omitted/extra pins, extra errors, stale suppressions, alternate-path duplicates and extra reviews all fail closed.

No immutable ER, RR, publication, taskbook, Driver review, review artifact, mathematical artifact or replacement edge was edited. The previously frozen pure per-Result audit helper/test/note were not changed. Root owns the separate RR68 superseded audit-only registry row. The follow-up colleague owns the explicit RESULT_CONTROL_AUTHORITY basis and five appended packet rows; this unit does not edit those four paths.

## Runtime behavior

Ordinary replacement validation and final sink selection run before Result authority filtering. BFB's authenticated replacement edge to AE11 remains intact; withholding AE11 cannot resurrect BFB. Same-execution recovery must be backed by the ordinary validated replacement chain. A valid independent execution on the same publication remains separate evidence; B923's clean RR00F7 and the four linked clean Results remain operational.

When a queried generation has held Results and no lawful survivor, task_result_state returns RESULT_CONTROL_AUTHORITY_WITHHELD, terminal=false, result=None and review=None, with historical execution-claim references. No Result or Driver disposition is manufactured. Implicit selection with no current publication follows existing publication isolation and does not fall back to historical Results. An explicit historical generation can still report its hold without affecting a lawful different current generation.

Dispatch reports BLOCKED/control recovery. Authenticated pre-freeze CLAIM provenance remains available, while new CLAIM/HANDOFF/DONE/UNBLOCK/SUPERSEDE admission cannot restore the held generation. The repository runtime guard checks ordinary execution, direct canonical CLAIM binding, adoption and exact lane publication bindings, so an old live CLAIM cannot bypass the overlay. A cohort containing only held-generation lanes stays blocked. A mixed cohort keeps lane routing when a separate lawful publication lane exists; the exact held lane still cannot authorize execution or adoption. Ordinary unrelated cohort semantics remain unchanged.

The review filter is composed after existing review isolations. Its install marker belongs to the current function, so a later bootstrap wrapper replacing the facade triggers safe recomposition. The explicit public nonoperational-review report can show overlapping Result/review causes; the temporary legacy Driver follow-up union deliberately excludes Result-only causes. New Result-derived packets must name RESULT_CONTROL_AUTHORITY and use its dedicated raw-source validator; relabelling that basis as Driver/review audit is rejected.

A ContextVar snapshot may reuse this validation within one reduction only. The registry, dependency bytes, and full execution/Result/review source path and byte inventories are checked again on exit. Changes abort the derived answer; later calls validate fresh evidence. No persistent authorization cache is introduced.

## Raw strict audit versus historical diagnostics

The twelve rows account for 32 actual raw strict errors: 21 enum errors, four legacy execution/metadata errors, and seven primary output/return drift errors. The three exact legacy bridges remain absent from the canonical execution map. Passing their fixed raw ER only to the pure audit helper additionally diagnoses three taskbook pin mismatches; the RR133 method_harvest error is also repeated in that diagnostic list. These diagnostic strings are not registered as absent raw-audit suppressions. All other raw errors remain strict and the existing superseded Result registry keeps its independent stale/unused checks.

The existing replacement contract preserves metadata, return pins and common manifest pins. This patch therefore does not claim that those defects can be repaired by editing immutable sources or merely installing a new same-execution Result. Recovery must satisfy the contracts actually in force; no corrected Result was synthesized.

## Validation and bounded failures

Python: `C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe` (3.12.14).

- Final new module: 19 tests PASS, 19.049 seconds. Command: `python -m unittest discover -s tests -p test_exact_invalid_result_authority_isolation_20260907.py -v`.
- Earlier combined run: 64 tests PASS, 64.719 seconds, covering this unit's then-18 cases, new Result-derived follow-up cases, frozen pure audit completeness, existing replacements, cohort dispatch and ordinary/lane claim authorization. The later function-marker import-order correction is covered by all final 19 cases including a fresh interpreter installing the Result adapter before complete bootstrap twice.
- Original reference step24 CLI: `python control_plane/check_result_review_binding_fault_isolated.py` PASS; binding reviews=1, invalid reviews=25, superseded result audit rows=3, withheld Result rows=12.
- Fresh full bootstrap and fixed 2dd public-view comparison: Results 161→149 (exact twelve removals), reviews 117→113 (exact four removals), packet_map 105→100 (exact five removals), current publications 153→149 (four removals; the fifth target was already noncurrent), definitions 193→193 with exactly five affected derived-task definitions changed. No surviving Result/review/packet/current-publication row changed and no old isolated review was restored.
- All 114 dependency paths match registered bytes; all three legacy canonical IDs remain absent; BFB remains nonoperational. Git diff whitespace check passes. No eight-shard suite, commits or pushes were performed by this assistant.

Initial test failures were retained: a fixture lacked the already-required nonempty semantic quarantine registry, and a cohort fixture incorrectly supplied one lane. The fixture now uses the repository's real `_write_semantic_fixture` and lawful two-lane cohort. A fresh-bootstrap fixture also required the existing Driver-authority quarantine, so the final import-order test uses the actual canonical repository in a new read-only process. No validator or guard was mocked to pass these tests. Separately, the colleague exposed Result-source basis masquerading; the legacy temporary union was corrected and the colleague's negative test retained. The independent reviewer exposed the mixed-cohort routing boundary; the final real mixed-lane authorization test covers that correction. The initial temporary packet comparison used packet IDs while the fixed baseline uses review-keyed packet_map; the saved final comparison explicitly uses the same API and retains legacy packets lacking packet_id.

## Frozen implementation SHA-256

| Path | SHA-256 |
|---|---|
| `research_result_authority_quarantines.json` | `9451f426fe16c4463289f425120b8c81f4664666a13b75b704c687cb6c21560f` |
| `control_plane/research_result_authority_fault_isolation.py` | `cffeacf7cd1b0c1f1189cb5e908ac5c78d03c9e1eee814509d7cac8671c21b15` |
| `tools/research_result_records.py` | `38e400fb8abdd7bf1a89ee83bcf442fe23eda135afd58b0cc4d0077d5b36bb8a` |
| `tools/research_dispatch.py` | `c19c2b692ddd4c67881f45f8d8c722648418cf39c00889ccfaa9627f91efc115` |
| `control_plane/check_result_review_binding_fault_isolated.py` | `b042c06c304e8d56743a73c5894c540664155305477ec76b8fbf4be2834dc098` |
| `control_plane/research_nonoperational_review_source_adapter.py` | `a7910c7b97fd2899c5ec8eb2e68dff8f53ef6f1f0b43de4f9bce00fed7698e8e` |
| `control_plane/research_control_bootstrap.py` | `87e703148f5ed4089476da408bfe012bf23922922c70f61b6d07229ba14a451f` |
| `control_plane/research_runtime_guard_core.py` | `d48bc398b7f80614d3448f15d3b27274988c536cf07939e8619a877fdefabf11` |
| `tests/test_exact_invalid_result_authority_isolation_20260907.py` | `d2634b53510c04125eff788188effdcbae6355159d6e952230f36b1fd5a1fad3` |

## Evidence

Local evidence directory: `C:/Users/Administrator/AppData/Local/Temp/owner-result-authority-isolation-20260907`. These are local test evidence, not mathematical or remote publication authority.

| Evidence | SHA-256 |
|---|---|
| `tests-final-19.log` | `69d8134e45049ec9bf1f15fe58e683f2822c4d4e3bbd5683ab540d0d131cf9ca` |
| `tests-combined.log` | `f7551a1071f259a815b9e9327fbe0aaf20528e137ef93757b5c748c5e072379b` |
| `step24-cli.log` | `030fbba700a0ec65c29015d26075b7b09f3d27603d02f741e0d03d4e648aefb5` |
| `full-bootstrap-delta.json` | `93f798944907a9f8340f65a935ce0b6c95c72df6bc241cff019f6b8563223915` |

The approved design and exact five-packet manifest remain in `TEMP/owner-control-reference-chain-20260907/execution-independent-review/`. The fixed independent baseline is `TEMP/owner-control-step24-2dd4c29-20260907T141855Z/public-runtime-baseline-2dd4c29.json`.
