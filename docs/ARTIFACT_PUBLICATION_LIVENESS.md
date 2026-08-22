# Enterprise Math Artifact Publication Liveness

Status: `ACTIVE / CANONICAL PUBLICATION-LIVENESS SUPPLEMENT`
Effective: `2026-08-22`
Scope: post-research artifact generation, checkpoint persistence, duplicate-writer avoidance, user-visible liveness, and parent-task continuation.
Authority: supplements `docs/GITHUB_INTERACTION_BUDGET.md`.

## Core invariant

> **Artifact persistence is a bounded subflow. It never becomes a second research project and never consumes the parent user's continuation intent.**

Freeze:

`PUBLICATION_COMPLETE != PARENT_USER_OBJECTIVE_COMPLETE`.

`PUBLICATION_COMPLETE -> RESUME_PARENT_TASK` unless the parent objective itself is complete.

Active-turn behavior is governed by `docs/ACTIVE_TURN_CONTINUATION_LIVENESS.md`.

## Required publication path

Once the mathematical/research payload is coherent:

1. generate the complete required artifact set once;
2. run the task-relevant checker/validation pass once on that frozen set;
3. freeze a manifest only when the task requires one;
4. take one current owner-branch/head snapshot immediately before publication;
5. if the same owner generation already contains an equivalent checkpoint, consume/reconcile it instead of building a duplicate;
6. publish the frozen set in one bounded source checkpoint;
7. create/update at most one Draft PR for the owner generation when useful;
8. terminate publication work;
9. **return immediately to the parent research/Driver/user objective in the same turn.**

## Prohibited choreography

Do not expand publication into repeated regeneration/checker/manifest/archive/minification/blob/tree/commit strategy loops when a simpler bounded path exists.

Do not optimize commit aesthetics after the semantic payload is already complete.

If the connected GitHub capability cannot atomically publish the whole set, prefer the simplest supported bounded sequence. Do not switch to ChatGPT/container GitHub networking as a fallback remote transport.

## Duplicate-writer / concurrency guard

Before the first publication write, take one owner-head snapshot.

If the branch advanced since freeze:

- determine whether the new head contains an equivalent/superseding same-generation checkpoint;
- if yes, consume/reconcile it and publish only a genuinely missing delta;
- if no, preserve owner isolation and use normal conflict/reconciliation rules.

Do not poll the branch repeatedly. Recheck only after a concrete publication failure or new semantic input.

A concurrency event is a publication subflow event; it does not terminate the parent task when other work remains.

## User-visible liveness

Mechanical publication remains part of the active interaction.

For long operations, send concise progress updates at the normal platform cadence. A progress update is observability, not a pause point.

After the update, continue automatically.

## Failure classification

Useful process signals include:

- `PUBLICATION_CRITICAL_PATH_EXPANDED`;
- `DUPLICATE_PUBLICATION_PATH_DETECTED`;
- `UNATTACHED_DUPLICATE_COMMIT`;
- `PUBLICATION_SIMPLIFY_REQUIRED`;
- `REMOTE_BUDGET_EXCEEDED`.

These are performance/process signals, never mathematical `HARD_BLOCK`s.

If a publication path fails and a supported alternative exists, take the alternative in the same turn. If no publication route remains, preserve the completed research payload, report the exact persistence limitation, and continue any independent parent work still possible.

## Current-only surface

This file contains only the current publication-liveness contract. Incident history and superseded publication strategies remain in Git history.
