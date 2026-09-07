# Exact invalid-review and follow-up isolation — 2026-09-07

Classification: `NO_NEW_MATHEMATICS_CONTROL_PLANE_ONLY`.

This unit implements the owner-authorized eight-review/eight-packet proposal on
integration HEAD `e1587b033c8ce5b551722889437bff4f1d74303a`. The proposal SHA-256 is
`b05ee3641b6f5e29f2aae6b4c9b094ae7f36ba023beef07bec0a7866c21a1913`.
All 50 frozen source pins were checked before implementation and after validation.
The original reviews, Results, Driver dispositions, review artifacts, packets,
publication records and taskbooks remain byte-identical.

## Failure and resulting control behavior

Eight immutable reviews failed their complete current review-record audit while
their direct follow-up packets were still present in the operational packet view.
The existing review-audit quarantine supports these errors without changing its
validator. Eight rows were appended with exact review/result pins and complete
error sets. Its original 17 rows remain byte-identical.

The follow-up registry received eight rows, preserving its original two rows.
Every new row explicitly selects `INVALID_REVIEW_RECORD_AUDIT` as its source
basis. Its source must continue to satisfy the complete pinned review-audit
quarantine; a recovered review, changed source bytes, missing quarantine, extra
audit error or stale expected error fails closed. The existing
`DRIVER_REVIEW_AUTHORITY` basis and source-adapter interface remain available for
the earlier rows and their existing source authorities.

Four packets have a nonempty task set. Four have no tasks: three retain the
literal `PARENT_CLOSED` decision and one retains `PARENT_OBJECTIVE_CLOSURE`.
The new `PACKET_ONLY_NO_DERIVED_TASK_AUTHORITY` type requires that exact closure
decision and an explicit empty task list in both the immutable packet and its
quarantine. It filters the packet without inventing a task or rewriting an
objective, publication, or Driver decision.

| Review | Packet | Exact packet scope |
| --- | --- | --- |
| `DR-007256B8119682DF8EFA` | `DFU-998EB492E2A5C7188EC3` | Three GEO6 prerequisite publications |
| `DR-19B757A8E5D817B5E495` | `DFU-E79D7C72DF1A2D5137F5` | Typing-minimality publication, shared source |
| `DR-4B7A2D91E6C0538FA124` | `DFU-19C7A4E25B8063DF91A2` | `PARENT_CLOSED`, empty task set |
| `DR-4C239DD3C0C251A78E45` | `DFU-07F2C626AB51FAADD478` | `PARENT_OBJECTIVE_CLOSURE`, empty task set |
| `DR-8E3C51A7D2B9046F1C85` | `DFU-6D3A91B84E205FC713A9` | `PARENT_CLOSED`, empty task set |
| `DR-B66959082DC75F6225C0` | `DFU-1B0311E52B57CE82D55D` | First-collision-frontier publication |
| `DR-C20A9201B684ECE69AF8` | `DFU-343CAA302296B0CE47B3` | Same typing-minimality publication, shared source |
| `DR-C6A128F3B95D407E2A71` | `DFU-9D7E05C41A682BF330D7` | `PARENT_CLOSED`, empty task set |

The shared typing-minimality publication is `TP2-C00220B16C3714BDED46`.
Both packet rows explicitly declare the complete two-packet source set. Shared
rows must agree on the task, publication, canonical record path, record pin,
taskbook path and book pin. The validator compares registered sources with every
raw packet referencing that exact publication, including additional sources from
other reviews. It also checks all direct packets of each covered source review.
Missing or newly added sources, duplicate identities, conflicting pins, or copied
files substituted for canonical record paths are rejected.

`derived_task_rows` preserves all shared packet and review IDs in plural fields.
The BLOCKED runtime definition and its `hard_block` retain both sources instead
of selecting one. Existing singleton source fields remain unchanged. These
mechanisms remove source-derived control authority; they create no replacement
review, claim, task, mathematical conclusion or successor permission.

## Executed verification

The existing review validator accepted 25 exact rows and the follow-up validator
accepted 10 packet rows. There are seven derived task quarantines including the
two pre-existing tasks. The actual follow-up isolation audit returned no errors.

Python 3.12.14 on Windows installed the complete runtime bootstrap before loading
tests through `scripts.run_unittest_shard.load_file_suite`. **42 tests passed**,
with zero failures, errors or skips: 16 new source-set regressions and 26 existing
follow-up, immutable-baseline, control-isolation and review-write regressions.
The tests took 28.865 seconds; total time including startup was 33.032 seconds.
The negative cases exercise real temporary review, Result, packet, publication
and taskbook files through the production validators. No authority validator or
selector is mocked to create a passing result.

A separately executed before/after runtime comparison established:

- exactly the eight listed reviews and eight packets left their operational
  views, with no additions;
- exactly five target definitions changed to follow-up-authority `BLOCKED` with
  `publication_id=None`; the other 188 definitions remained identical;
- two target publications newly left the current-publication view; the other
  three were already absent, and every unrelated current publication was
  unchanged;
- all 50 source files kept their exact Git blob and SHA-256 pins;
- the original 17 review rows and two follow-up rows, plus surrounding registry
  fields, retained their original bytes. Both edits were append-only.

`git diff --check` passed. No commit or remote write was made by this assistant.
The owner retains integration, publication, and the complete reference-integrity
gate. Separate invalid-Result authority work is outside this unit's completion
claim.

## Evidence and frozen files

Local evidence directory:
`C:/Users/Administrator/AppData/Local/Temp/owner-review-followup-isolation-20260907-9vuuks2r/`.
It contains the original three implementation/registry files, the verified
proposal, `baseline_views.json`, `after_views.json`, and
`preservation_verification.json`. The final test log and summary are under
`run-p0wgt6e8/`; the earlier 41-test run is retained separately.

| File | Validated SHA-256 |
| --- | --- |
| `research_result_review_audit_quarantines.json` | `7686defb8884e596a7da4e578dcf1940bd8d96fd581284e686bbea9dadabad88` |
| `research_driver_followup_authority_quarantines.json` | `1e2e8b0187fa00ddfed90f02e793ebd1e47e4c8aee2129991976e0498126f73b` |
| `control_plane/research_driver_followup_fault_isolation.py` | `60bfcd0e5b6a14008ba1bbcce2b5fc9c739f681e0d20f12a43588b9af67c766a` |
| `tests/test_review_followup_source_set_isolation_20260907.py` | `9ec43cefe70d7c12d9c1eea141928199eeedf6fab39cb5aecfefd7ede9b672fa` |
