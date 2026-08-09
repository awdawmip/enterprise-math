# Enterprise Math Research-to-Foundation Closed Loop

Status: `ACTIVE / CANONICAL GOVERNANCE CONTRACT`  
Effective: 2026-08-09  
Machine router: `foundation_backflow.json`  
Runtime surfaces: Research Relay #82, Foundation Problem Set #164, Research Dispatch Board #240

## 1. Purpose

Enterprise Math must support two directions at the same time:

1. `Foundation -> research`: every route consumes common definitions, theorems, tools, and boundaries;
2. `research -> Foundation`: mature research exposes weaker primitives, smaller sufficient states, minimal repair data, shared tools, and negative boundaries that may revise the common bottom layer after verification.

Without the second direction, Foundation becomes a historical starting point rather than a live layer continuously pressure-tested by research.

This protocol connects three existing live surfaces:

- **#82 Research Relay** propagates reusable theorems, counterexamples, and tool findings;
- **#164 Foundation Problem Set** records foundation questions that survived minimum steward verification but still require real research;
- **#240 Research Dispatch Board** coordinates which conversation continues which research or governance frontier through leases and handoffs.

The three surfaces have different authority. None of them alone determines canonical truth.

## 2. Authority boundaries that must not be collapsed

Maintain these distinctions:

- Relay `PROVED` is not `CANONICAL_MAIN`;
- Scheduler `DONE` means only that the declared execution frontier finished; it does not mean a theorem is proved or merged;
- FQ `ANSWERED` means a researcher returned an answer; it does not mean the steward accepted it;
- Steward `ACCEPTED` is still not main and must pass current-main integration and applicable gates;
- **only gated content in source-repository `main` is canonical source truth.**

The canonical path is therefore:

`research evidence -> backflow packet -> classification -> FQ/research when needed -> returned answer -> steward verification -> current-main integration -> gates -> main -> common surface/tool routing -> later research pressure test`.

## 3. Logical state machine

A backflow candidate uses the following stages; not every candidate needs every stage.

### `DETECTED`

A research route, engineering pressure test, Relay result, tool audit, or foundation-maintenance audit exposes a potentially cross-route structure.

### `PACKETIZED`

Compress it into a Foundation Feedback Packet, answering as many of these as apply:

- `candidate_object_or_tool`;
- `weakest_scope_hypotheses`;
- `minimal_state`;
- `minimal_repair_or_extension`;
- `negative_boundary`;
- `cross_route_evidence`;
- `proof_status`;
- `tool_surface`;
- `prior_art_and_owner`;
- `foundation_destination`.

### `CLASSIFIED`

Exactly one handling class is chosen:

1. `DIRECT_FOUNDATION_MAINTENANCE`;
2. `FOUNDATION_QUESTION`;
3. `APPLICATION_LOCAL_OR_NOT_READY`.

The third class exits the loop here and remains with its current owner; that is not a failure.

### `FQ_OPEN`

A candidate requiring real research receives a stable `FQ-*` entry in #164. The entry must separate `verified_so_far` from `unknown`; a conjecture must not be smuggled in as an already-established premise.

### `RESEARCH_SCHEDULED`

Every OPEN/CLAIMED/RESEARCHING FQ that needs execution must be traceable through `foundation_backflow.json` to a #240 scheduler task:

- mathematical research links to a `RESEARCH` task owned by the appropriate L1/L2/L3 active owner or bridge;
- the task itself explicitly declares that FQ in its `foundation_questions` field;
- an existing owner task may carry the FQ only when the FQ is genuinely inside that task's declared frontier; sharing an owner is not enough;
- a live claimed task is never retroactively reinterpreted to solve a different FQ; use a distinct bounded scheduler task when the question is separate;
- the steward does not impersonate a research owner;
- once an FQ has returned an answer, it moves to governance-side steward verification rather than being automatically re-dispatched as the same research.

### `RESEARCHING`

Execution follows the #240 lease machine when that runtime surface is available. #164 remains the mathematical question/answer record; #240 remains the execution-continuity record. Scheduler availability is not a research startup gate, and neither surface replaces the other.

### `ANSWERED`

The researcher returns proof, counterexample, or exact tool evidence to #164, together with weakest scope, source ref, ownership/prior-art boundary, and a recommended canonical change. Reusable results are also relayed through #82.

### `STEWARD_VERIFICATION`

The foundation steward independently checks the returned answer against current `FOUNDATIONS`, `THEOREMS/PROBLEM_STATUS`, common surface, source/tests/Lean, Relay, and provenance.

Possible outcomes are:

- `ACCEPTED`;
- `NEEDS_NARROWER_ANSWER`;
- `REJECTED`;
- `KEEP_OPEN`.

### `INTEGRATION`

An `ACCEPTED` result is turned into the smallest canonical patch from the **then-current latest main**. The mathematical source/owner evidence is frozen; integration must not invent new mathematics while transporting the verified result.

### `CANONICALIZED`

After applicable gates pass and the patch enters main:

1. the corresponding #164 FQ is marked `CANONICALIZED`;
2. the common research surface and machine routers expose the new bottom-layer interface;
3. theorem/tool/status/lineage surfaces are updated as needed;
4. the relevant #240 governance frontier is completed or handed off when the runtime path is available;
5. GLOBAL_KNOWLEDGE records the durable architecture/state;
6. later research consumes the revised Foundation and continues pressure-testing it.

This closes back into `DETECTED`: revised Foundation is an input to the next round of research, not an endpoint.

## 4. Scheduler integration

`research_scheduler.json` remains the durable task/frontier definition and #240 remains the runtime event log when available.

`foundation_backflow.json` adds only **semantic links**; it does not duplicate the scheduler state machine. Each active FQ link records at least:

- `question_id`;
- `phase`;
- `scheduler_task_id`;
- `scheduler_role`;
- `research_owner` when applicable;
- `source_refs`.

Rules:

- `scheduler_role=RESEARCH` must reference a scheduler `kind=RESEARCH` task;
- the referenced research task must explicitly list the FQ in `foundation_questions`;
- `scheduler_role=STEWARD_VERIFICATION` or `INTEGRATION` must reference a `kind=GOVERNANCE` task;
- an FQ may change links as its phase changes, but research answer and steward acceptance must never be collapsed into one state;
- an existing owner task may carry a compatible FQ only when that FQ is explicitly declared in the task; `owner` equality by itself is insufficient;
- do not mutate the meaning of an already-live claim merely to reuse its task ID; create a distinct bounded task for a distinct question;
- if carrying the FQ would create owner scope drift, create a bounded L3 bridge/probe rather than forcing it into an unrelated owner;
- after an FQ is canonicalized, remove it from the active scheduler-link set and retain it under `canonicalized_examples`/provenance instead of pretending it still needs execution.

These links are durable recovery metadata. Failure to read or write #240 is a coordination degradation, not a mathematical `HARD_BLOCK` and not a reason to stop an explicit user task.

## 5. Relay integration

A route should create or update a Feedback Packet when any of these occurs:

- a new mother-theorem candidate appears;
- multiple routes repeat the same minimal-state or minimal-repair pattern;
- an application counterexample falsifies an attractive Foundation-level generalization;
- an executable tool exposes a theorem/API domain mismatch;
- a new tool is reused by at least two owners;
- a coordinate is proved to be only a derived representation rather than a required primitive.

If a result has already been propagated through Relay #82, the Feedback Packet should cite that Relay entry rather than copy another theorem statement.

## 6. Canonical-promotion integration

The backflow loop does not lower existing promotion gates:

- owner research remains parallel;
- canonical promotion remains serialized;
- latest-main integration is the final combination surface;
- bilingual/reference/quality/Lean gates apply according to the changed surface;
- WIP, experiments, physical interpretation, or branch-ahead count never automatically upgrade canonical status.

The protocol guarantees that valuable results can travel back down. It does not imply every result belongs in Foundation.

## 7. Regression examples

### FQ-20260809-004 — closed-loop canonicalized example

FQ-004 is the first completed research-to-Foundation example. The returned A1/A2 result was independently steward-verified, narrowed to the minimal interface, replayed through a clean canonical integration, and merged by PR #268 at `fe94a3201c4f6ca996c78cb55e719709d5144a54` with `quality`, `bilingual-sync`, and `reference-integrity` all successful.

Its canonical scope is:

`typed state -> deterministic/observation functional kernel -> declared future-signature kernel`.

The whole P018 substrate was not promoted:

- `State Pair = X×X` is a derived carrier;
- Difference/defect/critical-grid coordinates may replace state only after task-specific factorization/sufficiency is proved;
- P023 retains ownership of generic future-compatible refinement/minimal repair constructions;
- P024 retains integer action-language specializations;
- A3 structured relation-state and A4 multivalued support remain explicit extensions;
- generic kernel, behavioral-equivalence, and partition-refinement machinery is established prior mathematics and is not claimed as novel abstraction.

This example now lives under `canonicalized_examples`, not the active scheduler-link set.

### FQ-20260809-005 — active scheduled example

FQ-005 remains at `FQ_OPEN -> RESEARCH_SCHEDULED`: the stable `graph_distance` API has a broader operational domain than the P012 ordinary-metric theorem domain.

A5/P012/P022 geometry research must decide the API/domain layering. The foundation steward must not silently choose between narrowing the stable API and retaining a separately named directed shortest-walk helper. `foundation_backflow.json` links this question to the dedicated `RS-P022-GRAPH-DISTANCE-API` research task under `program/p022-geometry-v2`. This deliberately does **not** reinterpret the separate `RS-P022-OBSERVATION-HISTORY` frontier or any live lease on it.

The two examples intentionally occupy opposite ends of the loop so the mechanism stays regression-testable.

## 8. Completion test

A healthy loop lets a maintainer answer for every important Foundation candidate:

1. where did it first appear?
2. where is its Feedback Packet?
3. why was it direct maintenance, an FQ, or local/not-ready?
4. if research is needed, which explicitly-declared #240 task/owner continues it?
5. where was the answer returned and what is its proof status?
6. has the steward independently accepted it?
7. which current-main integration made it canonical?
8. where do later researchers discover and consume the revised bottom layer?

If any answer depends only on memory from a particular conversation, the loop is still incomplete.