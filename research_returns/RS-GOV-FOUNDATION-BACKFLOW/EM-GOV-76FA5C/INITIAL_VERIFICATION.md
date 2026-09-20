# P0 backflow — initial verification and durable continuation

Task: `RS-GOV-FOUNDATION-BACKFLOW` (P0, GOVERNANCE).
Publication: `TP2-2C438651496A928ADCB7`.
Researcher: `EM-GOV-76FA5C`.
Claim: `CL-P0-BACKFLOW-20260920-9fc58a6b278d`.
Work branch: `research/p0-backflow-9fc58a6b278d`.
Session key: `local-chat-p0-backflow-9fc58a6b278d` (locally assigned, not a ChatGPT server identifier).
Status: `INITIAL_VERIFICATION_COMPLETE / PARENT_TASK_NOT_COMPLETE`.

## Claim evidence and limits

The ordinary ANY/P0 request `EMREQ-P0-FILTER-66912430fffc4a11`, source
`9ae2c8b30a7239a3845a89854b26c709f438b518`, selected this exact unowned READY
publication. The actual raw CLAIM was posted as Issue 240 comment 5746935533:
https://github.com/awdawmip/enterprise-math/issues/240#issuecomment-5746935533

Server readback records author awdawmip / 30957095 / OWNER and identical
created/updated times 2026-09-20T02:08:22Z. The exact actor is authorized by
`research_control_event_authorization.json`. The inline claim's publication,
identity, branch/base, output scope and lease satisfy the current inline-CLAIM
contract in `tools/research_dispatch_core.py`. The branch was actually created.

The scoped recheck `EMREQ-P0-CLAIMCHECK-9fc58a6b278d`, source
`073bdc139bbc97459d1f57f4cdd9125623f95c7c`, completed canonical routing and now
selects a different fresh GOVERNANCE/P0 task. That next task was NOT claimed.
The intervening bounded Issue 240 read returned only our CLAIM. The source
comparison preserves the task/publication, reducer, selector, authorization and
result/review inputs; only transport/activity records and unrelated research
notes changed. Applying the current CLAIM transition to that verified
previously-unowned scope yields CLAIMED/LEASED with this claimant. Before any
later progress event, the server-clock lease end is 2026-09-20T04:08:22Z.

This is authenticated checkpoint-plus-delta verification, corroborated by actual
canonical routing. The second packet does NOT directly print our owner state.
No full local repository runtime-guard execution is claimed. Future runs must
refresh the actual winning owner and use guarded recovery; this report is not a
substitute for current live ownership.

## Work performed

Loaded the existing backflow route at source
`3359e465daf353c0bda3a748fa9e98dd3c8e4e0b`. It retains FQ-20260809-005 and
FQ-20260810-007 as ANSWERED routing links. They are intake pointers, not a new
queue or a claim that their later status has been exhaustively reviewed.
FQ-20260809-004 remains a closed regression example and was not restarted.

For FQ-20260809-005, read the original problem and the current geometry source.
The original concern was that a directed BFS API could be mistaken for an
undirected metric. The current source already separates `graph_distance` from
`directed_graph_distance`, validates closed/symmetric/loop-free adjacency for
the ordinary metric interface, and raises for cross-component queries.
Do not rebuild that already-present repair.

Reused the unchanged source module, verifying its exact Git blob
`a1a8dc4d1ca53fde2ca00d9b944c1b8aa346a152` before execution. Ran
`verify_graph_distance.py` against an independent integer Floyd-Warshall oracle:

- All 4,165 labelled loop-free directed graphs on 1..4 vertices; 66,129 queries.
- All 75 labelled simple undirected graphs on 1..4 vertices; 1,105 queries.
- Ten invalid-input boundary checks, including invalid edges outside the queried
  component and zero-length queries that must not bypass validation.
- One directed self-loop zero-distance check.

All checks passed. Unreachability uses None, not floating-point infinity. The
checker is task-local regression code, not a newly promoted general tool.
P000 was loaded and no worldview, native-coordinate or theorem-strength change
was made. This is existing-interface verification, not a new BRC mechanism.

The existing `tests/test_p012_geometry.py` was read, not run as a full package
suite. Package-export execution, repository-wide tests, complete downstream
compatibility, later Issue 164 status, and independent Steward/Driver acceptance
remain unverified. Finite passing tests are not a general mathematical proof.
No Foundation surface, theorem, task priority, Result or review was changed.

## Smallest next unfinished unit

1. Verify the package exports and the exact P012 API/theorem documentation at a
   current immutable source; compare with the FQ-005 return/integration evidence
   (route reference PR 431). Reuse the above verified module and test result
   unless source integrity or governing rules require rerun.
2. Check later Issue 164 dispositions for FQ-005, not just its original OPEN
   comment. Distinguish already-integrated implementation from remaining
   propagation or review work. Do not infer current OPEN status from an old post.
3. Produce the minimal evidence/propagation proposal in this task's output scope.
   A researcher cannot self-grant Driver/Steward acceptance or canonical promotion.
4. Only then intake FQ-20260810-007's exact return evidence. It has not been
   reviewed in this checkpoint.

## Recurring execution

The user authorized hourly task research. A ChatGPT hourly automation was
actually created, first scheduled for 2026-09-20T03:06:03Z (11:06 Taipei), then
hourly. Resume unfinished work first, preserve the live claim and durable
frontier, and claim at most one new P0 task when appropriate. Do not accumulate
claims to satisfy a clock or claim a completed research result every hour.
The automation is not an immortal researcher or continuous background process.

## Reproduction

From the repository, with this output directory restored:

```sh
python research_returns/RS-GOV-FOUNDATION-BACKFLOW/EM-GOV-76FA5C/verify_graph_distance.py \
  --source src/enterprise_math/geometry.py \
  --output /tmp/p0-backflow-verification.json
```

The checker rejects a different source blob. The exact source remains at
https://github.com/awdawmip/enterprise-math/blob/3359e465daf353c0bda3a748fa9e98dd3c8e4e0b/src/enterprise_math/geometry.py

Observed results are in `verification.json`. This checkpoint is not a frozen
terminal Result, an independent review, or completion of the P0 parent.
