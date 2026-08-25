# Enterprise Math Research Control State Machine V1

Status: `CANDIDATE CANONICAL CROSS-LAYER CONTROL / NO NEW MATHEMATICS`

Machine-readable contract: `research_control_state_machine.json`  
Task runtime submachine: `research_scheduler.json`  
Cross-layer validator: `tools/research_control.py`  
Event emitter: `tools/research_scheduler_event.py`

## 1. What this machine is

Enterprise Math already has several valid local state machines: identity, role/mode, FREE candidate lifecycle, taskbooks, Scheduler V2, active-turn continuation and promotion. None of them should be duplicated.

This file defines their **composition**.

The operative state is a vector:

`ACTOR × OBJECT × RUNTIME × INFORMATION × EVIDENCE × ROUTING × PARENT`.

The point is to make questions such as the following decidable without relying on chat memory:

- who has authority to act;
- which task/generation is live;
- whether the context is blind, statement-exposed or post-freeze;
- whether source and independent evidence are open/closed;
- whether a Driver verdict is still pending;
- whether formalization is admitted;
- whether a benchmark supports a performance claim;
- whether a successor gate is satisfied;
- whether the current task is locally done but the parent user objective is still open.

Scheduler V2 remains the source of truth for task-runtime state. The cross-layer machine does **not** invent a second scheduler.

## 2. The one algorithm every role follows

For every substantive Enterprise Math action:

1. **Resolve role + identity.** Use the current role contract and identity state machine.
2. **Resolve object.** Identify task/candidate/control object, origin, lineage and exact immutable refs.
3. **Classify control profile.** Choose one of `STANDARD_RESEARCH`, `FREE_CANDIDATE_AUDIT`, `INDEPENDENT_AUDIT`, `FORMALIZATION`, `FOUNDATION_DISPOSITION`, `INTEGRATION`, `BENCHMARK`, `GOVERNANCE_MAINTENANCE`.
4. **Materialize runtime state.** For task work, reduce current Scheduler V2 events; do not infer state from a filename, PR or chat.
5. **Materialize information/evidence state.** Record firewall/freeze/source exposure plus source, independent, Driver, formalization/benchmark/canonical state.
6. **Execute only an allowed transition.** Role permissions and profile guards both apply.
7. **Before Driver closure, bind evidence + routing.** Every accepted/narrowed return needs evidence class, method-harvest classification and explicit route disposition.
8. **Evaluate the parent objective.** `scheduler DONE`, Stage PASS, PR creation, checkpoint freeze or remote pending never ends an open parent objective by itself.
9. **Persist changed control facts, then continue.** If the parent objective is open and an executable action exists, execute it in the same turn.

## 3. Role-specific use

### Task researcher

`READY/HANDOFF_READY -> CLAIM -> PROGRESS* -> SUBMIT`.

Never emit V2 `DONE`. Never self-review. A hard block must name a genuinely missing object/dependency, its owner, necessity and unblock condition.

### FREE researcher

Phase A stays outside automatic claiming. Preserve blindness until candidate/no-go freeze. After freeze, a concrete proposal may be published only to `REVIEW_PENDING`; that publication is not Working Truth and is not dispatchable authority.

### Independent auditor / replicator

This is a `RESEARCHER` task specialization, not a new authority role.

The task must declare its information firewall. Clean independence requires a distinct execution context when the protocol claims independent replication. Source proofs/checkers withheld by the taskbook stay withheld until the named freeze.

**Do not use same-task handoff to represent a new independent replication.** If a Driver decides a new independent run is needed, the parent review is parked and a **distinct child task id/taskbook** is opened with fresh provenance and an explicit independence/firewall protocol.

### Formalizer

This is a `RESEARCHER` task specialization with profile `FORMALIZATION`.

Formalization may start only after Driver admission and frozen/corrected source mathematics. `NO_NEW_MATHEMATICS` is binding. If Lean or another proof kernel exposes a statement/interface mismatch, return it to the Driver. Never weaken a theorem, change the accepted universe, add an unreviewed hypothesis or insert an axiom merely to pass the build.

### Driver

Drivers own task publication/review, return review, route disposition, method harvest, successor gating, formalization admission, Foundation routing and promotion routing.

For every accepted/narrowed return, record:

- `evidence_class`;
- `method_harvest`;
- `route_disposition`;
- route/successor/child refs when applicable.

A Driver verdict is a routing event, not parent-objective completion.

### Foundation Steward

Steward disposition may change the Foundation semantic gate. Until that gate is explicitly resolved, canonical mutation and gated downstream formalization remain blocked. Steward verification does not automatically promote a theorem.

## 4. Publication approval is two gates, not one

Taskbook content gate:

`python tools/research_taskbook.py audit <taskbook> --dispatch`

Runtime gate:

`PUBLISH -> different Driver REVIEW_CLAIM -> APPROVE -> READY`.

New `APPROVE` events must bind both:

- `taskbook_audit=PASS`;
- current `policy_digest=sha256:...`;
- immutable `taskbook_ref`;
- `review_ref`.

This prevents a cross-Driver runtime approval from silently bypassing the taskbook policy gate.

## 5. Return review is a semantic routing gate

New `REVIEW` events carry four mandatory fields:

- `review_ref`;
- `evidence_class`;
- `method_harvest`;
- `route_disposition`.

Additional guards:

- `RETURN_TO_RESEARCH` -> `CONTINUE_SAME_TASK`;
- `OPEN_CONTINUATION` requires `successor_gate_ref` and a distinct route/task ref;
- `ROUTE_TO_FOUNDATION`, `ROUTE_TO_FORMALIZATION`, `ROUTE_TO_PROMOTION` require the concrete route ref;
- independent replication uses `PARK + OPEN_INDEPENDENT_REPLICATION_CHILD`, with distinct child task id/ref and independence protocol;
- `REQUEST_INDEPENDENT_REPLICATION` as a same-task Scheduler verdict is forbidden.

## 6. Profile guards for the current research portfolio

### Prime Fusion F1 / formalization

Profile `FORMALIZATION`: corrected/frozen package + closed independent evidence + Driver admission are prerequisites. A source-repair-required state cannot enter formalization.

### Native-prime companion replay and CBRC F5R

Profile `INDEPENDENT_AUDIT`: firewall and freeze state are first-class control fields. A blind audit cannot close before raw freeze and cannot claim clean independence from the source execution context if it reused that context.

### FQ010 scale-role decision

Profile `FOUNDATION_DISPOSITION`: pending Steward disposition blocks canonical mutation and downstream formalization admission.

### Valley / third-sector computational claims

Profile `BENCHMARK`: structural theorem status is separate from performance status. Positive performance claims require benchmark PASS, fair baseline and complete cost accounting. Partial/negative evidence cannot be relabeled L4.

### Prime Fusion package repair/integration

Profile `INTEGRATION`: package freeze is illegal while mandatory source repair or required independent evidence remains open.

### Scheduler/control-plane repair

Profile `GOVERNANCE_MAINTENANCE`: `NO_NEW_MATHEMATICS`; use current-main conflict audit and the bounded governance-maintenance lane.

## 7. Cutover and orphan rule

A taskbook discovered outside V2 registration is not silently READY. It appears as `ORPHANED`.

This is intentional and covers work created concurrently with the V2 cutover. A Driver must reconcile it explicitly:

- `MIGRATE` for already-live cutover work;
- `ADOPT` for genuine orphan recovery;
- `SUPERSEDE` for dead/stale work;
- or re-author/review/publish it through the ordinary V2 gate.

No live task is allowed to disappear merely because it was issued during a control-plane migration.

## 8. Mandatory checks

Static machine:

`python tools/research_scheduler.py validate`

`python tools/research_control.py validate-spec`

For an exported Scheduler event stream before control-plane acceptance/migration:

`python tools/research_control.py validate-events <events.jsonl>`

For a materialized cross-layer snapshot:

`python tools/research_control.py validate-snapshot <snapshot.json>`

The validator is a guard over the existing submachines. A PASS never proves mathematics; it proves only that the control state is internally admissible.

## 9. Nonterminal rule

Always end the control decision with:

`PARENT_USER_OBJECTIVE -> CURRENT_SUBFLOW -> NEXT_EXECUTABLE_ACTION`.

If the parent objective is open and the next executable action is known, continue now. Do not turn `DONE`, `PASS`, freeze, publication, review, PR/CI pending or a progress update into a user wake-up barrier.
