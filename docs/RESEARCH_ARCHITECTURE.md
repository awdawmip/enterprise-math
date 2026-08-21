# Enterprise Math Research Architecture V2

Status: `DRIVER-PROPOSED / NO_NEW_MATHEMATICS / GOVERNANCE`
Date: `2026-08-22`
Driver-ID: `EM-DVR-K7Q4N8`
Machine contract: `research_architecture.json`

## 1. Why this architecture exists

Enterprise Math needs two opposite capabilities at the same time:

1. **independent exploration** that can discover a new primitive or axiom without being pulled toward the most recent successful route;
2. **decisive exploitation** that can push a frozen question hard enough to prove, falsify, formalize and integrate it.

Trying to make one generic `RESEARCHER` behavior do both creates failure modes:

- recent-route anchoring;
- scheduler anchoring;
- continuation inertia;
- tool/representation anchoring;
- early conjectures becoming Driver `WORKING_TRUTH` before audit;
- Foundation backflow treating discovery drafts as mature shared structure;
- large common-surface preloads reducing both independence and performance.

V2 therefore separates research by **mode**, while keeping the existing role/identity system compact.

## 2. Four functional roles

### 2.1 FREE_AXIOM_DISCOVERY

A free researcher receives the current foundation but not the current agenda.

Mission:

`FOUNDATION -> INDEPENDENT STRUCTURAL SEARCH -> FROZEN CANDIDATE -> OPEN-CONTEXT AUDIT`.

Before candidate freeze it does not auto-dispatch, does not inherit another branch's `WORKING_TRUTH`, and does not use recent task/PR/Relay/success/failure/tool availability as the discovery prior.

The current foundation is a starting substrate and comparison authority, not a required final axiom list.

### 2.2 TASK_RESEARCH

A task researcher owns a selected mother question. The question may come from the user, Driver or scheduler.

This mode may see task history and relevant current route context because the question is already selected. It should still load only the smallest task packet and exact dependencies actually used.

Driver-frozen `WORKING_TRUTH` applies here when explicitly activated.

### 2.3 RESEARCH_DRIVER

The Driver owns portfolio control, not primary discovery monopoly.

The Driver:

- decides whether a result continues, stops, parks, returns, splits or promotes;
- de-duplicates and attacks novelty claims;
- turns an **audited** candidate into an explicit task or Foundation question when justified;
- prevents automatic successor-stage cascades;
- owns Working Truth activation;
- maintains continuity as routing state rather than theorem memory.

### 2.4 FOUNDATION_STEWARD

The Steward maintains shared mathematical language, status, interfaces and reusable tools.

The Steward does not treat a raw free-research candidate as Foundation input. Candidate intake occurs only after the Phase-B audit has classified the object at sufficient maturity.

## 3. Exploration and exploitation are different information regimes

For FREE Phase A, information withholding is deliberate experimental control.

Allowed context:

- current foundation facts actually needed;
- relevant protected worldview facts;
- identity/safety/provenance;
- native/foundational typing when needed.

Withheld as discovery priors:

- current scheduler/taskbooks;
- Relay/PR/issue summaries;
- recent commits;
- current theorem-family success/failure lists;
- other branch Working Truth;
- suggested questions;
- benchmark/teacher targets selected to steer discovery;
- ambient recent-project memory not explicitly supplied by the user;
- convenient existing tools, coordinates, filenames and names as hints about ontology.

After the candidate is frozen, all of that context may be opened for audit and verification.

For TASK research, this blind barrier does not apply because the question is already selected.

## 4. Axiom candidates have a lifecycle

Machine state: `research_axiom_candidate_state_machine.json`.

A candidate is not a theorem, not a task, not Working Truth and not Foundation truth merely because it is interesting.

Lifecycle:

`DISCOVERY_IN_PROGRESS`

`-> BLIND_CANDIDATE_FROZEN`

`-> PHASE_B_AUDIT_IN_PROGRESS`

then classify into one of:

- `FALSIFIED`;
- `DUPLICATE_OR_ALREADY_KNOWN`;
- `DERIVED_NOT_AXIOM`;
- `IMPLEMENTATION_ARTIFACT`;
- `PRIOR_ART_ANALOGUE`;
- `EXACT_NEGATIVE_OBSTRUCTION`;
- `AUDITED_AXIOM_CANDIDATE`;
- `AUDITED_REPLACEMENT_CANDIDATE`.

Only after this classification may the Driver route it into replication, an explicit task, a Foundation question, park/reject, or another existing owner.

## 5. Working Truth starts later than discovery

`WORKING_TRUTH` is a task-execution discipline, not a candidate-generation discipline.

It activates only after an explicit Driver direction freeze or Driver-approved taskbook.

It does not apply to:

- blind free discovery;
- a raw candidate packet;
- Phase-B prior-art/dedup audit;
- an unreviewed side branch.

This prevents early speculation from becoming a self-confirming control-plane premise.

## 6. PASS does not automatically create Stage N+1

A completed stage may expose a real new gap, but completion alone is not such a gap.

A new continuation/stage requires a **successor gate** recording:

- parent task;
- exact new information gap;
- why the parent result does not already close it;
- discriminating possible outcomes;
- kill condition;
- why another task/stage is better than continuing or closing the current one.

If this information is absent, the Driver should close/park, continue the same mother task, return to an existing owner, or reopen independent exploration.

`PASS -> NEXT_STAGE` is forbidden as an automatic control rule.

## 7. Scheduler is exploitation infrastructure

The scheduler coordinates selected work. It does not choose the free researcher's problem.

`TASK_RESEARCH` may be scheduler-eligible.

`FREE_AXIOM_DISCOVERY` is not.

A static scheduler fallback is a task catalog, not a truth source. Before claiming an old fallback task, validate that its scope/dependencies still make sense against current source.

Scheduler `DONE` means execution closure only. It does not imply theorem truth, canonical promotion or successor-stage creation.

## 8. Foundation backflow is a maturity boundary

Raw discovery does not automatically become a Foundation question.

Minimum free-candidate intake is an audited candidate/replacement candidate or exact negative obstruction. The Steward/Driver then decides whether it is:

- direct maintenance already determined by canonical evidence;
- a Foundation question requiring research;
- application-local/not ready.

No discovery draft bypasses the ordinary evidence and promotion gates.

## 9. Independent replication

When structural importance justifies multiple free researchers, run them independently:

1. separate fresh contexts;
2. same frozen foundation snapshot when comparability matters;
3. no sharing of candidate packets before each run freezes its own candidate;
4. compare only afterwards.

Independent convergence raises structural interest but is not proof. Divergence is preserved before Driver selection.

## 10. Snapshot discipline

A free-discovery run should record the foundation/worldview snapshot that existed before candidate generation and should not chase moving `main` during Phase A.

Later source changes are handled in Phase B as comparison/supersession evidence.

This makes discovery provenance reproducible and prevents moving-main changes from silently rewriting the premises mid-search.

## 11. Read-path performance

The architectural principle is:

`SMALLEST_SUFFICIENT_ROLE_PACKET > UNIVERSAL_PRELOAD`.

The Common Surface remains valuable as an index, tool registry and conflict/ownership lookup. It is not a default context dump.

Task researchers should normally start from:

`AGENTS / exact task entry / exact first dependency`.

Free researchers start from the foundation-only route.

Repeated rereads, CI polling, whole-repository preflight and unrelated theorem catalogs are performance defects.

## 12. Persistence and promotion

- L1/L2/L3: remote-silent between semantic checkpoints;
- one bounded owner generation: normally one owner branch and at most one Draft PR;
- canonical promotion: one active ready L4 lane by default;
- GLOBAL_KNOWLEDGE journal: history/provenance, not theorem truth;
- Driver Continuity: routing only, no implicit default next route;
- canonical truth: gated source `main`.

## 13. Legacy interpretation rule

Older surfaces may still contain broad wording such as `auto_select_when_user_task_absent=true` or long `mandatory_preflight` lists.

Under this architecture:

- auto-selection is generic TASK_RESEARCH behavior, not FREE discovery behavior;
- legacy preflight lists are triggered lookup lists, not unconditional startup sequences;
- role-specific FREE contracts control over generic scheduler wording for the same scope.

This retyping avoids rewriting historical provenance merely to make newer role semantics explicit.
