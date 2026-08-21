# Enterprise Math Research Architecture V2 — Driver Audit

Status: `DRIVER_AUDIT / NO_NEW_MATHEMATICS / DRAFT_PROMOTION_PAYLOAD`
Date: `2026-08-22`
Driver-ID: `EM-DVR-K7Q4N8`
Base: `main@f1cf9d88428c14ae56e228ed97eba9b657b1fb90`

## Audit question

Does the current research control plane preserve both independent discovery and decisive task execution without letting recent routes, scheduler state, tools, representation choices, successful stage momentum, Working Truth, Foundation backflow, continuity snapshots or repository read order silently choose the next research question?

## Findings that required repair

1. The old free-research role was a waiting/topic-supplied role, not autonomous axiom discovery.
2. Generic scheduler/common-surface machine fields could re-route no-user-task research into the exploitation queue even when a free role was intended.
3. `RESEARCHER` had no machine-level mode distinction between independent discovery and selected-task execution.
4. Raw axiom candidates had no explicit lifecycle boundary before Driver Working Truth or Foundation intake.
5. Driver policy encouraged same-task continuation but had no hard rule preventing `Stage PASS -> Stage N+1` inertia.
6. New taskbooks carried no machine lineage/successor-information-gap contract.
7. Foundation backflow/Steward surfaces had no explicit raw-free-candidate maturity gate.
8. Driver Continuity could grow into theorem/route memory and implicitly select one next route.
9. The Common Surface was useful as an index but too large and agenda-rich to remain a default research context dump.
10. Discovery evidence and independent validation evidence were not explicitly separated in the candidate lifecycle.

## V2 architecture

The control plane now separates four functions:

- `FREE_AXIOM_DISCOVERY` — foundation-only independent question/axiom search;
- `TASK_RESEARCH` — selected mother-question execution;
- `RESEARCH_DRIVER` — portfolio/routing/Working Truth/promotion control;
- `FOUNDATION_STEWARD` — shared maintenance and verification.

A candidate follows:

`DISCOVERY -> FROZEN CANDIDATE -> PHASE-B AUDIT -> DRIVER INTAKE -> TASK/FQ/REPLICATION/PARK/REJECT -> NORMAL PROOF/PROMOTION`.

There is no direct candidate-to-Working-Truth, candidate-to-scheduler, candidate-to-Foundation, or candidate-to-main path.

## Successor-stage invariant

Freeze:

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

New `CONTINUATION` taskbooks require:

- parent task;
- exact new information gap;
- why the parent result does not close it;
- discriminating outcomes;
- kill condition;
- why another stage/task is better than same-task continuation or closure.

The taskbook tool now enforces this mechanically on dispatch.

## Anti-anchoring invariant

Free Phase A withholds:

- current scheduler/tasks/Relay/PR/recent commits;
- success/failure catalogs and suggested questions;
- other-branch Working Truth;
- ambient recent project memory not explicitly supplied by the user;
- tool availability and implementation convenience;
- coordinate/file/name ordering as ontology hints.

A clean blind-discovery claim requires a context that was clean before candidate generation and a pinned foundation/worldview snapshot. Already-exposed contexts remain valid research but are typed `ANCHOR_EXPOSED`.

## Evidence invariant

Freeze:

`DISCOVERY_EVIDENCE != INDEPENDENT_VALIDATION_EVIDENCE`.

Independent free-research replication uses separate fresh contexts and hides candidate packets until each run freezes its own candidate.

## Compatibility boundaries

- No mathematical R063/R061/R062/Hodge theorem/task/result file is changed by this payload.
- The existing large Common Surface remains preserved as a machine/index/provenance surface; V2 retypes its broad auto-dispatch/preflight fields instead of rewriting historical content.
- Already-running frozen tasks are not erased. Subsequent new/re-dispatch control-plane actions use the current policy digest and lineage gate.
- Generic AGENTS scheduler wording remains TASK_RESEARCH behavior and cannot override the more specific free-role contract.
- Canonical promotion and the single ready L4 lane are unchanged.

## Changed-surface classes

- architecture + candidate lifecycle;
- researcher role/mode and identity typing;
- free researcher anti-anchoring;
- Driver portfolio/Working Truth/successor gate;
- taskbook lineage + machine audit;
- Foundation backflow/Steward maturity gate;
- regression tests.

## Payload classification

`NO_NEW_MATHEMATICS`.

`RESEARCH_ARCHITECTURE_V2_CLOSED_ON_OWNER_PAYLOAD`.

Canonical promotion remains subject to ordinary repository governance.
