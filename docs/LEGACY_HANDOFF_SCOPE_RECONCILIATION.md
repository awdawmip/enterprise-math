# Legacy handoff scope reconciliation

Status: ACTIVE / CONTROL_PLANE_ONLY / NO_NEW_MATHEMATICS
Issue: 1479

## Problem and boundary

An imported HANDOFF_READY task or an old untyped HANDOFF can preserve a frozen
research return only in next-action prose. Neither prose nor an open PR is a
machine terminal or review disposition. Repeating that work is also unsafe.

The runtime now preserves the unknown scope as
LEGACY_HANDOFF_SCOPE_UNRESOLVED / BLOCKED. It does not classify the mathematics.
The trigger is the typed migrated evidence_status plus HANDOFF_READY, or a
reducer-applied registered HANDOFF without a scope/terminal marker. It does not
search task prose for words such as Driver, PASS, completed or review.

Existing events, publications, Results, reviews, author attribution, source
branches and artifacts are not rewritten. Genuine HARD_BLOCK, terminal/cohort
and parent-Objective gates keep their authority. Ordinary READY tasks and typed
CONTINUATION handoffs retain their routing.

The explicit forward claim-enforcement clock is 2026-09-17T04:00:00Z. This is a
runtime rule, not a claim about deployment time. Earlier owner races remain
replayable. A still-live earlier owner is preserved; expiration alone does not
turn its unresolved old handoff into fresh work. A substantive new PROGRESS
reference under a valid existing owner or a typed handoff preserves the new
frontier. A no-op progress reference does not clear scope uncertainty.

## Claimless, exact-frontier repair

Use a new raw Issue 240 event named RECONCILE_HANDOFF_SCOPE. It is a scope
annotation, not a CLAIM, Result, review, DONE or task publication. The existing
raw server-comment loader and exact authorized-author allowlist remain required.

Required payload fields, in addition to schema/event/task_id:

- publication_id and taskbook_blob_sha1: exact current operational generation;
- source_handoff: exactly progress_ref, progress_at, server_comment_id from the
  unresolved frontier (server_comment_id is null for the imported task baseline);
- handoff_scope: CONTINUATION or FROZEN_RETURN_AWAITING_DRIVER_REVIEW;
- source_evidence: exactly repository, commit, path, git_blob_sha1, sha256;
- progress_ref: the immutable GitHub blob URL matching source_evidence;
- next_action: the precise remaining action.

Read the source in full at its immutable commit and verify its actual Git blob
and SHA-256 before publishing the event. Preserve the original source; do not copy
or reauthor another researcher's Result merely to register the annotation.
The pure reducer checks source-pin shape/address and exact frontier binding. It
neither fetches remote bytes nor verifies mathematics: the authorized event
producer is responsible for the observed source binding. A hash-shaped string is
not a claim of server-signed verification.

The event requires no current claim and cannot steal a live owner, remove a real
hard block, reopen a terminal/frozen state, act on a different publication, or
create Result/review/cohort authority. Unknown/mismatched scope is rejected. A
repeat after successful reconciliation is ignored without changing the accepted
annotation. A frozen annotation stays AWAITING_REVIEW; it never implies accepted
mathematics. CONTINUATION only makes the frontier eligible; a real CLAIM is still
required before execution.

Operational Results retain precedence. The canonical bootstrap composes
research_handoff_scope_runtime before the parent-Objective gate. Only the current
fault-isolated Result reader may supply a RETURN_TO_EXECUTION review time. This
reopens execution at that edge, not permanently: a later untyped return requires
its own scope resolution. Supplied task flags are discarded before this binding.

## Issue-comment transport

The entire Issue 240 event comment body must be one JSON object. No Markdown code
fence, prose prefix/suffix, or second JSON document is allowed. The source loader
uses json.loads on the complete body; non-JSON comments remain human discussion.
Do not broaden that loader to revive historical malformed event-looking comments.

A connector returning a comment ID proves that the comment exists, not that the
canonical reducer accepted its event or that the caller won a claim. Read back
server metadata and verify the derived owner/task state. Correct an ignored event
by appending a properly serialized, currently authorized event; never edit the
old event to change history or retroactively claim research authorization.

## Local regression and publication

Run:

    python -m unittest discover -s tests -p 'test_legacy_handoff_scope_reconciliation.py' -v

The targeted suite covers migrated and nonmigrated tasks, untyped and typed
handoffs, explicit frozen/continuation reconciliation, immutable-source binding,
wrong generation/source/author/clock, live and expired owners, no-op progress,
ordinary hard blocks, terminal states, real review reopen edges, and input
immutability. Ordinary scenarios were also replayed against the exact original
reducer blob 85b471104ad29d088b9c1fa76b31541ad056c52c.

This change does not introduce or enable Actions, a scheduler or a daemon. Local
regression runs precede publication. The already-binding canonical dispatch
bridge may be consumed for its authenticated live-event receipt; that narrow
transport dependency is not a substitute for local tests or a claim that the
full repository suite was run.
