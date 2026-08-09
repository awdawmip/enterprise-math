# Enterprise Math Research Scheduling Protocol

Status: `ACTIVE / CANONICAL SCHEDULING CONTRACT`  
Effective: 2026-08-09  
Scope: all L1 core owners, L2 program owners, L3 bridges/probes, and L4 integration replays.

This protocol resolves ambiguity created during Architecture v2 migration. Where older migration notes, replay manifests, branch ledgers, or Relay wording can be read as requiring one research line to wait for another, this protocol controls the scheduling interpretation.

## 1. Primary invariant: research is parallel, canonical promotion is serialized

Enterprise Math separates two different activities:

- **research/discovery**: new proofs, counterexamples, constructions, tools, experiments, and specializations;
- **canonical promotion**: semantic ownership audit, numbering, bilingual replay, reference/lineage registration, final repository gates, and merge to `main`.

Research/discovery is parallel by default. Canonical promotion is serialized only where repository consistency requires it.

A dependency needed for canonical ownership or later integration is **not automatically a dependency of ongoing research**.

## 2. `defer` is not a blocker

The words `defer`, `consume from`, `owner moved`, `audit against`, `replay after`, `depends on owner`, or equivalent routing language mean:

> do not duplicate or prematurely promote the mother theorem here.

They do **not** mean:

> stop this research line until another branch finishes.

A route continues with every question that can be stated and tested without the missing result. It may use an already proved upstream theorem, keep a downstream statement conditional, construct examples/counterexamples, derive specializations, or isolate the exact missing lemma.

## 3. Only an explicit `HARD_BLOCK` may stop a route

A route may wait only if all of the following are recorded:

```text
HARD_BLOCK:
  missing_object: <exact theorem/data/experiment/artifact>
  owner: <route or external source>
  necessity: <why no meaningful independent next step exists>
  unblock_condition: <precise condition that resumes work>
```

If any field is absent, the condition is not a hard block.

`HARD_BLOCK` must be exceptional. If a route can continue by proving a conditional theorem, searching for a counterexample, weakening assumptions, building an executable oracle, testing a special case, or attacking a different open frontier, it is not blocked.

## 4. L1/L2/L3 owners may always create new mathematics

- L1 core owner: new reusable mother theorems are allowed and expected.
- L2 program owner: new program-specific mathematics, applications, counterexamples, and candidate generalizations are allowed and expected.
- L3 bridge/probe: new mathematics is allowed within the bridge's declared question.
- L4 integration replay: **NO NEW MATHEMATICS**.

A replay manifest on an L1/L2/L3 owner branch containing

`no_new_mathematics_during_replay = true`

applies only to the identified replay slice or replay operation. It must never freeze the owner branch as a whole.

If a new theorem is discovered while moving one replay slice, record it on the appropriate L1/L2/L3 research frontier; do not smuggle it into the L4 transport commit.

## 5. Moving `main` is not a research blocker

Repeatedly rebuilding the same validated result every time `main` advances creates integration livelock.

Use this rule instead:

1. freeze the proved semantic payload by source commit/blob/theorem identity;
2. continue unrelated research normally;
3. create or refresh the L4 integration replay when promotion is actually ready;
4. perform one final combination gate against the then-current `main` before merge;
5. if `main` moved only by unrelated changes, do not create a new research generation or restart the proof;
6. restart research only when the new `main` introduces a genuine semantic conflict or invalidates an assumption.

Thus the requirement is **final-state compatibility**, not continuous chase of every intermediate `main` head.

## 6. Relay action classes

Every new cross-route Relay entry should classify its requested downstream action as exactly one of:

- `INFORM` — useful context; no action required before continuing;
- `CONSUME` — reuse this result rather than duplicating it;
- `TEST` — pressure-test or seek a bridge/counterexample when convenient to that route;
- `HARD_DEPENDENCY` — the downstream route truly cannot continue on its declared frontier without this result.

Only `HARD_DEPENDENCY` may create a `HARD_BLOCK`, and the downstream route must still record the four `HARD_BLOCK` fields itself.

Absence of an acknowledgement does not block the upstream route.

## 7. Route heartbeat

Every active owner should be able to state:

```text
frontier: <current mathematical question>
hard_block: NONE | <HARD_BLOCK record>
last_progress: <commit/PR/Relay result>
shared_surface_seen: <main SHA or common-surface revision>
```

If `hard_block = NONE`, the route should continue research rather than waiting for another conversation, branch, review, or replay.

## 8. Relationship to Architecture v2

This protocol preserves Architecture v2's theorem ownership and non-destructive replay rules. It changes only the mistaken scheduling interpretation:

> ownership is unique; knowledge is shared; research remains parallel.

The A0–A5 ownership axis prevents duplicate mother theorems. It must not become a serial dependency chain.