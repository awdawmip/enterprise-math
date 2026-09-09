# EM-DVR-BSJ393 — Control Plane Task-Machine Responsibility

Status: `CURRENT / USER-DIRECTED / ROUTING_AND_CONTINUITY_ONLY / NOT TASK AUTHORITY`  
Effective: `2026-09-09`  
Driver: `EM-DVR-BSJ393 / CONTROL_PLANE`

## User-directed responsibility

`EM-DVR-BSJ393 / CONTROL_PLANE` is responsible for publishing Driver-created research/governance work into the canonical Enterprise Math task machine so that another authorized Driver, Researcher, or executor can take over and continue without depending on hidden chat context.

This is a persistent control-plane responsibility in addition to ordinary Driver coordination. It does not create a second task registry and does not itself make any task executable.

## Required takeover-ready publication package

When this Driver creates or identifies work that should be executed by another agent/session, the handoff is not complete until the work is represented through the existing canonical task-publication/runtime path with enough durable state for direct continuation.

The durable package must preserve, at minimum:

1. the mother question / parent objective and frozen task scope;
2. the exact current verified frontier and relevant source version(s);
3. work already completed and conclusions that must not be replayed;
4. the smallest unfinished unit and the next executable action;
5. durable evidence, code, Result/review, artifact, PR/commit, or other authoritative source pointers needed to continue;
6. unresolved blockers, dependencies, quarantines, or binding conditions;
7. success, kill, acceptance, and return criteria;
8. the execution/takeover conditions needed for the successor to claim or adopt the work safely.

Essential continuation state must not remain only in the current conversation. A successor must be able to reconstruct the executable frontier from durable source material.

## Canonical task-machine binding

Official task publication remains governed by the existing Enterprise Math control plane:

- immutable V2 publication record: `research_task_records/<task-id>/<publication-id>.json`;
- publication contract: `research_task_publication_contract_v2.json`;
- publication tool: `tools/research_task_records.py`;
- human protocol: `docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md`;
- live dispatch: `research_control_dispatch.py`;
- runtime/adoption guard: `tools/research_runtime_guard.py`;
- narrow control precedence: `control_plane/current_control_authority.json`.

Freeze:

`DRIVER_TASK_CREATED_FOR_HANDOFF -> TAKEOVER_READY_DURABLE_PACKAGE -> CANONICAL_V2_PUBLICATION -> SUCCESSOR_CAN_CLAIM_OR_ADOPT`

`CHAT_ONLY_TASK_DESCRIPTION != PUBLISHED_TASK`

`HIDDEN_PREDECESSOR_CONTEXT_REQUIRED -> HANDOFF_INCOMPLETE`

`EXISTING_VALID_OWNER_CLAIM -> ADOPT_EXISTING_CLAIM; DO_NOT MANUFACTURE A SECOND CLAIM`

## Authority boundary

This file records the user-directed responsibility and continuity expectation for `EM-DVR-BSJ393`. It is not itself a taskbook, immutable publication record, claim, Result, review, Working Truth, Foundation decision, theorem status, or promotion authority.

Where this handoff conflicts with a current machine contract, exact task publication, Result/review binding, or later explicit user direction, the current authoritative source controls. Before any remote mutation, refresh the applicable authority and use non-force / compare-and-swap semantics where supported.
