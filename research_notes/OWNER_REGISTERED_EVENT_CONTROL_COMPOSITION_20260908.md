# Registered event authority gate composition

Status: revised local review candidate on main `86a04d17cbffd687b1ef74ab4990cf6b2b7e093a`
(tree `7ab67689a86e47a2c0be43ca2fb5e2c4feefdfc5`). This note does not publish a
Result, Driver review, claim, or mathematical conclusion.

## Source and composition

The candidate semantically integrates PR1359
`d69a606970e3ad868afaed0a941ad4241db9929e` and PR1360
`6c44a7ea7ddbf1e05f456d96f28f2b320a024a39`. All nine peer changed-file blob IDs
match the owner's frozen peer snapshot. The source snapshot SHA256 is
`4f9a0a139d23a32e948350895a9ca2edf10cd28f934dd09db33800523fd57834`; the independent
semantic composition report SHA256 is
`4e7edbf194793afefb0f71a88caf15a63ab32e7363d3178eea604ede24673613`.

The dispatch wrapper preserves this order: resolve the exact-publication Result
view; invoke the original lifecycle gate with no operational Result when held;
bind intent-backed CLAIMs; enforce immutable publication time; enforce typed
HANDOFF scope; retain the existing held-event filter. A rejected prepublication
CLAIM cannot supply live-claim provenance for a HANDOFF or DONE barrier. The
Result overlay, mixed-cohort overlay and Result read snapshot remain installed,
alongside the publication-definition and provisional terminal-barrier hooks.

The six existing wrapper functions `_bind_intent_claim_publications`,
`_event_source_index`, `_post_review_runtime_transition`, `_overlay_result_state`,
`_overlay_active_cohort` and `_dispatch_result_read_snapshot`, plus the complete
held-filter tail, retain their exact source text from the base. The reducer and
scheduling addendum retain the peer's typed scope semantics and historical
compatibility boundary. No new Issue #240 audit or mutation was performed here.

One real integration defect was reproduced and corrected in the new PR1360
helper: its scope filter also rejected another task's HANDOFF. It now accepts
the current task, applies only to registered tasks, and preserves other-task
events. The cross-task and nonregistered compatibility assertions remain in the
new regression suite. No strict validator is relaxed.

The independent review of the initial ten-path freeze then found three further
defects: mappings in HANDOFF scope fields could raise uncaught `TypeError`;
the provisional barrier replay used a separate 90-minute lease default; and a
matching claim ID with a mismatched researcher could obtain blocking authority.
The revision rejects nonstring HANDOFF fields safely in the wrapper and pure
reducer. Both reducers use the same extracted claim/researcher identity check,
including optional-field handling, validation, normalization and original error
text. The core passes its already-resolved lease into the provisional hook with
one keyword argument; task-specific and caller-supplied defaults therefore reach
the same replay. This adds three lines to `tools/research_dispatch_core.py`.
Existing direct hook calls without replay context retain their compatibility;
replay with no resolved lease raises an explicit configuration error instead of
inventing a default. Publication-bound filtered input and time order are retained.

## Verification and fixture correction

The first six-module peer regression run passed 45 tests. The first existing
held-authority run had 18 passes and one fixture error in 19 tests: its generated
independent publication omitted `published_at`. The sole change to that existing
test supplies the copied frozen publication's actual timestamp,
`2026-09-01T12:13:05+00:00`, preceding the fixture CLAIM at `12:34:00+00:00` and
Result freeze at `12:35:00+00:00`. The original independent-lane authorization
assertion remains. No frozen source timestamp or source byte changed.

New cross-test development logs separately retain fixture API/enrichment,
missing `next_action`, and loader-path errors; these are not production defects.
The scope defect above was observed after correcting the initial fixture APIs.
The final new nine cross tests plus the affected existing mixed-lane method
passed together: 10 tests, 10.047 unittest seconds. These use real pinned Result,
review, publication and execution dependencies, a real intent selector, actual
public reducer/guard calls, and a snapshot byte-drift rejection; validators and
authority selectors are not mocked. Each fixture preserves all copied source
dependency bytes at teardown.

The initial candidate's focused-control workflow was run in its exact ten-command
order, each in a fresh Python 3.12.14 process with `PYTHONPATH` cleared. All 82
tests passed in 12.938 seconds total. All 4,559 tracked and untracked input files
present at that run retained their pre-run SHA256. The original six-module and
19-test results are retained as earlier-input evidence, not relabeled as reruns.

The three added review-regression methods reproduced the defects before the
fix: 18 failing subtests and four subtest errors across three methods, separately
from the initial fixture-development errors. After the revision, eight affected
peer, reducer and cross modules passed 62 tests. An exact copy of the independent
six-case collector was rerun in a new evidence directory, and each observed state
was compared with its expected result; its exit code alone was not used as proof.
All six cases passed. The combined eight-module and collector run took 16.187
seconds, with every input SHA256 unchanged. The new regressions cover both the
120-minute live renewal and 10-minute expired renewal, task and caller defaults,
HANDOFF and DONE, optional/normalized/mismatched researcher identities, and
nonstring scope fields on the public and pure-reducer paths. The original peer
legacy marker and direct hook compatibility tests also pass.

Local evidence is under `%TEMP%/em-event-compose-ywuypu1x`: original failure and
success logs, the unchanged initial freeze manifest, `focused-final/summary.json`
for the initial run, and `revision-1/summary.json` plus the revised manifest for
the corrected input. Each run records exact argv, exit code, duration and log
SHA256. All eleven candidate paths are UTF-8 with LF endings.
Immutable authority records, registries, taskbooks,
Driver dispositions and mathematical sources are outside the diff.

## Remaining admission

This is an eleven-path uncommitted overlay on the stated main commit, not a tested
published head. Owner independent review and the final published commit's full
reference-integrity chain, eight quality shards and applicable CI gates remain.
The earlier base commit's passing full CI is not claimed for this candidate.

Global-Knowledge-Sync: main@990d7c1 / GLOBAL_KNOWLEDGE_V1
