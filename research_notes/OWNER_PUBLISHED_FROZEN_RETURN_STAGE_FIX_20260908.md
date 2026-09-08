# Preserve the published frozen-return stage

Status: bounded control implementation candidate; no formal publication or review.

Base: `1e338a83e19d45557de1d3e0026b606017d224fc`, tree
`94113b2cb75ea150c5ef14bbb95bcd1ac05a026c`.

The startup packet at source `f179a3a53470d563eff2ef52a079e293824bfb44`
offered `RS-A3-A4-GENERATED-SUPPORT` through `CLAIM_NEW_OWNER`. Its preserved
generation `TP2-F4F7A34423E2D6CDC0CF` has `HANDOFF_READY` as its initial state,
while the independently read PR955 is an existing research delivery awaiting
Driver disposition. The migration's old prose saying it had no V2 publication
is historical; the migration itself supplied a V2 publication. Neither this
observation nor an open PR is a mathematical acceptance or task-closure verdict.

The runtime deliberately maps ordinary `HANDOFF_READY` to `NEEDS_DISPATCH`.
The fresh selector chooses that state, the canonical router creates the existing
`CLAIM_NEW_OWNER` action, and the compact packet copies it. Disabling all
handoffs would break continuation and owner recovery. Parsing `next_action`
would improperly make free text an authority source.

An authorized superseding publication can express the existing runtime state
`FROZEN_RETURN` in a new pinned taskbook. However, `registered_definition` did
not recognize that state and silently converted it to `READY` when the record
was claimable. The production change adds only `FROZEN_RETURN` to that existing
state-preservation set in `tools/research_dispatch_core.py`. The unchanged
reducer maps it to `AWAITING_REVIEW` and refuses a CLAIM while in that state.
No schema, action enum, shadow registry, task-ID whitelist or new authority is
introduced. Result, review, publication clock, claim, session and cohort
implementations remain unchanged.

The code change alone does not rewrite generation 1 or close the legacy task.
The authorized Driver must publish a separate corrected taskbook and generation
using the exact supersedes link. Original taskbook/publication bytes stay
immutable. The Driver still has to review the real delivered research. The
current derived Driver queue traverses actual Results, so a Result-less legacy
PR does not silently become a Result queue entry through this patch.

## Actual bounded evidence

Python 3.12.14, using `-X utf8 -B`:

- Before the patch, the new superseding-publication test passed real preparation,
  current policy lint, record construction, repository audit and current-head
  selection. It then failed at the intended assertion:
  `FROZEN_RETURN != READY` (1 test, process 9.265 seconds).
- After the one-line change, all 6 new methods passed (process 10.547 seconds;
  unittest 4.943 seconds). They exercise a real temporary second publication,
  exact old-book/record preservation, existing claim refusal, ordinary and typed
  continuation, valid READY ownership, stale adoption, active-session retention,
  a complete hard block, another task ID and absence of prose inference.
- Four existing related modules passed after canonical bootstrap: registered
  HANDOFF scope, frozen Result handoff, startup transport and session observation
  time (33 tests, process 8.875 seconds). No broad CI or eight-shard run was made.

The new fixture invokes the same `prepare_taskbook`, `_prepared`, `build_record`
and exclusive record writer used by the existing CLI, with an explicit temporary
root and the current policy input bytes. The canonical validators are not mocked.
An existing independent semantic-fault fixture supplies its real required
registry. Synthetic authenticated comment objects exercise the event gate only
inside the tests; no comment, researcher identity, claim, execution or Result is
persisted to the repository or a remote service.

The original failure stderr SHA256 is
`d9b003c142a5f4423e2714e234a06b25eb154ab38d0f2c1c734b861ba154e4ca`.
The 6-test success stderr SHA256 is
`a96866de8b3e5f4751c795c7a5fc2d10ad03d92a8093d8129f5e7ee799f4ed58`.
The 33-test success stderr SHA256 is
`2719502fe3e295b26cae95b99f84c6fb3ac03d600e29bdeef0665c85a18bea79`.

Reproduce the new methods from the repository root:

```text
python -X utf8 -B -m unittest discover -s tests -p test_published_frozen_return_stage_20260908.py -v
```

## Existing publication route for the authorized Driver

Create a new taskbook path and preserve the original task identity, parent,
lineage, owner, mathematical frontier, original source provenance and body.
Set `base_state` to `FROZEN_RETURN` and state the current Driver review action.
Keep original files intact. Use the actual authorized publisher identity and
publication time:

```text
python -X utf8 -B tools/research_task_records.py prepare --taskbook <NEW_BOOK> --publisher-role RESEARCH_DRIVER --parent-objective-id LEGACY_CONTROL_CUTOVER_RS_A3_A4_GENERATED_SUPPORT
python -X utf8 -B tools/research_task_records.py publish --taskbook <NEW_BOOK> --publisher-role RESEARCH_DRIVER --publisher-id <AUTHORIZED_DRIVER_ID> --research-value <PRESERVED_VALUE> --published-at <ACTUAL_UTC_TIME> --supersedes-publication-id TP2-F4F7A34423E2D6CDC0CF
```

Preparation computes the current policy stamp and preserves `FROZEN_RETURN`.
Do not hand-write a PASS stamp. The existing writer sets `record_state=ACTIVE`
and `claimable=true`; there is no claimable CLI switch, and neither field needs
an ad hoc override. Execution eligibility comes from the derived stage.

On Windows, freeze the intended LF taskbook bytes after preparation and before
publication if LF is the final repository representation. The writer must hash
the final taskbook bytes; do not normalize or otherwise modify them afterward.
Confirm the published taskbook blob at the final commit. This note records the
existing route; it is not authorization to mint execution or Result evidence.

Global-Knowledge-Sync: main@e27fd4d / GLOBAL_KNOWLEDGE_V1
