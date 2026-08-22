# Enterprise Math Research Architecture V2

Status: `DRIVER-PROPOSED / NO_NEW_MATHEMATICS / GOVERNANCE / V2.3`
Date: `2026-08-22`
Driver-ID: `EM-DVR-K7Q4N8`
Machine contract: `research_architecture.json`
Candidate lifecycle: `research_axiom_candidate_state_machine.json`
Promotion liveness: `docs/GOVERNANCE_MAINTENANCE_LIVENESS.md`

## 1. Why this architecture exists

Enterprise Math needs two opposite capabilities at the same time:

1. **independent exploration** that can discover a new primitive or axiom without being pulled toward the most recent successful route;
2. **decisive exploitation** that can push a selected/frozen question hard enough to prove, falsify, formalize and integrate it.

Trying to make one generic `RESEARCHER` behavior do both creates:

- recent-route / scheduler anchoring;
- continuation inertia;
- tool/representation anchoring;
- early conjectures becoming `WORKING_TRUTH` before audit;
- candidate provenance being lost when a Driver selects it;
- Foundation backflow treating discovery drafts as mature shared structure;
- large common-surface preloads reducing both independence and performance;
- stale ready promotion candidates becoming accidental repository-wide locks.

V2 separates research by **mode** while keeping identity compact.

## 2. Four functional roles/modes

### FREE_AXIOM_DISCOVERY

Receives current foundation, not current agenda:

`FOUNDATION SNAPSHOT -> INDEPENDENT STRUCTURAL SEARCH -> FROZEN CANDIDATE -> OPEN-CONTEXT AUDIT`.

Before candidate freeze it does not auto-dispatch, inherit another branch's `WORKING_TRUTH`, or use recent route/task/PR/Relay/success/failure/tool availability as the discovery prior.

The current foundation is a starting substrate and comparison authority, not a required final axiom list.

### TASK_RESEARCH

Executes a selected mother question from the user, Driver, scheduler or an audited-candidate transition.

This mode may see task-scoped history/current route context because the question is already selected. It still loads only the smallest exact task/dependency packet.

Driver-frozen `WORKING_TRUTH` applies only when explicitly activated.

### RESEARCH_DRIVER

Owns portfolio control, not primary-discovery monopoly. The Driver:

- routes, closes, parks, returns, splits and promotes;
- de-duplicates and attacks novelty claims;
- turns an **audited** candidate into a task/Foundation question when justified;
- preserves candidate origin and semantic task lineage;
- prevents automatic successor-stage cascades;
- owns Working Truth activation;
- maintains continuity as routing state rather than theorem memory.

### FOUNDATION_STEWARD

Maintains shared mathematical language, status, interfaces and reusable tools. Raw free candidates are not Foundation inputs; audited mature objects are classified/verified without making the Steward the default investigator.

## 3. Exploration and exploitation use different information regimes

For FREE Phase A, information withholding is deliberate experimental control.

Allowed:

- current foundation facts actually needed;
- relevant protected worldview facts;
- identity/safety/provenance;
- native/foundational typing when needed.

Withheld as discovery priors:

- scheduler/current taskbooks;
- Relay/PR/issue summaries and recent commits;
- Driver Continuity/recent project journal/candidate packets from other runs;
- theorem-family success/failure catalogs;
- other-branch Working Truth;
- suggested questions and target/teacher answers chosen to steer discovery;
- ambient recent-project memory not explicitly supplied by the current user;
- convenient existing tools, coordinates, filenames, router order and names as ontology hints.

After freeze, all may be opened for audit/verification.

For TASK research, this blind barrier does not apply because the mother question is already selected.

## 4. Axiom candidates have a lifecycle

Machine state: `research_axiom_candidate_state_machine.json`.

A candidate is not a theorem, task, Working Truth or Foundation truth merely because it is interesting.

`DISCOVERY_IN_PROGRESS -> BLIND_CANDIDATE_FROZEN -> PHASE_B_AUDIT_IN_PROGRESS`

then classify as one of:

- `FALSIFIED`;
- `DUPLICATE_OR_ALREADY_KNOWN`;
- `DERIVED_NOT_AXIOM`;
- `IMPLEMENTATION_ARTIFACT`;
- `PRIOR_ART_ANALOGUE`;
- `EXACT_NEGATIVE_OBSTRUCTION`;
- `AUDITED_AXIOM_CANDIDATE`;
- `AUDITED_REPLACEMENT_CANDIDATE`.

Only audited/mature classifications may enter Driver intake for replication, explicit task, Foundation question, park/reject or owner return.

Freeze:

`RAW_AXIOM_CANDIDATE != WORKING_TRUTH != CANONICAL_FOUNDATION`.

## 5. Candidate origin survives task selection

Selecting a free candidate for exploitation changes its control-plane status; it does not erase discovery provenance.

A task opened from free discovery must retain:

- `origin_kind=FREE_AXIOM_CANDIDATE`;
- `origin_candidate_id`;
- audited `origin_candidate_state`.

It may not be repackaged as `DRIVER_ROADMAP` merely because the Driver selected it.

`TASK_ORIGIN_AND_LINEAGE_CANNOT_BE_ERASED_BY_RENAMING`.

## 6. Working Truth starts later than discovery

`WORKING_TRUTH` is a TASK execution discipline.

It activates only after explicit Driver direction freeze or a Driver-approved taskbook and does not apply to:

- FREE Phase A;
- raw candidate packets;
- Phase-B prior-art/dedup audit;
- unreviewed side proposals.

This prevents early speculation from becoming a self-confirming premise.

## 7. PASS does not automatically create Stage N+1

A completed stage may expose a real gap, but completion is not itself a gap.

A `CONTINUATION` task requires:

- parent task;
- exact new information gap;
- why parent result does not close it;
- discriminating possible outcomes;
- kill condition;
- `alternative_route_or_free_exploration_considered`;
- why another stage/task is better than same-task continuation, owner return, closure or renewed exploration.

Any explicitly named **Stage 2 or later** task is continuation semantics by construction and must use `task_lineage=CONTINUATION`.

Renaming the next unresolved layer without the word “Stage” does not reset semantic lineage when the parent result remains a necessary premise/motivation.

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

If the gate is absent/weak, close/park, continue the same mother task, return to another owner, or reopen independent exploration.

## 8. Portfolio balance without quotas

A chain of successful task stages is not evidence that the highest-leverage next question remains on that route.

Before another continuation, the Driver records whether closure, another owner/route or independent/free exploration was considered and why continuation still produces the best new information.

No artificial numeric quota between exploration and exploitation is imposed. A task-local exact dependency can legitimately justify continuation; it just cannot be justified by momentum alone.

## 9. Scheduler is exploitation infrastructure

Scheduler coordinates selected `TASK_RESEARCH`. It does not choose the free researcher's question.

A static fallback is a task catalog, not truth authority; validate stale scope/dependencies before claim.

Scheduler `DONE` means execution closure only—not theorem truth, canonical status or successor-stage creation.

## 10. Foundation backflow is a maturity boundary

Raw discovery does not automatically become a Foundation question.

Minimum free-candidate intake is an audited candidate/replacement candidate or exact negative obstruction. Steward/Driver then classifies maintenance vs Foundation question vs local/not-ready.

No discovery draft bypasses ordinary evidence/promotion gates.

## 11. Independent replication

For independence evidence:

1. separate fresh contexts;
2. same frozen foundation/worldview snapshot when comparability matters;
3. no candidate sharing before each run freezes its own;
4. compare afterwards.

Record independence honestly:

- `CLEAN_INDEPENDENT_CONTEXT`;
- `SHARED_AMBIENT_CONTEXT_DISCLOSED`;
- `NOT_INDEPENDENT`.

A fresh Researcher-ID alone does not prove independent discovery.

Independent convergence raises structural interest but is not proof. Preserve divergence before Driver selection.

## 12. Snapshot and evidence discipline

A free run records the foundation/worldview snapshot before candidate generation and does not chase moving main during Phase A. Later movement is Phase-B comparison/supersession evidence.

Discovery evidence used to choose/shape a candidate is typed separately from independent validation evidence:

`DISCOVERY_EVIDENCE != INDEPENDENT_VALIDATION_EVIDENCE`.

Later comparison may reclassify the candidate but must not rewrite its origin story.

## 13. Read-path performance

`SMALLEST_SUFFICIENT_ROLE_PACKET > UNIVERSAL_PRELOAD`.

The Common Surface remains an index/tool registry/ownership/conflict lookup, not a default context dump.

TASK startup normally:

`AGENTS -> exact task entry -> first exact dependency -> work -> triggered expansion`.

FREE starts from the foundation-only route.

Repeated rereads, CI polling, whole-repository preflight and unrelated theorem catalogs are performance defects.

## 14. Promotion is an attempt, not a permanent PR lock

Promotion liveness is defined by `docs/GOVERNANCE_MAINTENANCE_LIVENESS.md`.

Freeze:

`READY_PR != PROMOTION_LANE_LEASE`.

A mathematical PR being ready-for-review means it is a candidate. The mathematical L4 lane exists only while a Driver is executing one bounded promotion attempt:

`SELECT -> CURRENT_MAIN_SNAPSHOT -> CONFLICT_SNAPSHOT -> FROZEN_HEAD_VALIDATION -> FINAL_COMBINATION -> MERGE_OR_DEFER -> RELEASE`.

Only one mathematical L4 promotion attempt is active at a time. A stale/unmergeable ready candidate does not permanently block every later repository action.

## 15. Governance maintenance is separate from mathematical L4

A bounded `NO_NEW_MATHEMATICS` governance-maintenance attempt may proceed while mathematical L4 candidates are ready when all narrow eligibility gates pass.

Eligible examples include role/policy/router repair, machine/human synchronization, stale-status repair, and authority routing to an **already-frozen** canonical definition.

Governance maintenance must not introduce or change:

- theorem claims or proof strength;
- proof status without evidence;
- native mathematical definitions;
- semantic content of frozen current definitions;
- evidence interpretation;
- theorem ownership.

If the semantic delta is uncertain, it is not governance maintenance: route it through mathematical/Foundation promotion.

Governance maintenance still requires a fresh current-main snapshot, path/semantic conflict audit, relevant regression evidence, and an atomic/expected-head merge guard when supported. Only one governance-maintenance merge attempt should be active at a time.

This prevents control-plane starvation without weakening mathematical canonical gates.

## 16. Persistence and canonical truth

- L1/L2/L3 remote-silent between semantic checkpoints;
- normally one owner branch + at most one Draft PR per bounded owner generation;
- mathematical L4: one **bounded active attempt** at a time, not one permanent ready-PR lock;
- governance maintenance: separate bounded `NO_NEW_MATHEMATICS` attempt;
- GLOBAL_KNOWLEDGE journal = history/provenance, not theorem truth;
- Driver Continuity = routing only / no implicit default next route;
- canonical mathematical truth = gated source main.

## 17. Legacy interpretation

Older surfaces may still contain broad `auto_select_when_user_task_absent=true`, `mandatory_preflight` lists, or wording that sounds like a ready PR permanently owns the L4 lane.

Under V2.3:

- generic auto-selection applies to TASK research, not FREE discovery;
- legacy preflight lists are triggered lookup/reference surfaces, not unconditional startup sequences;
- specific FREE contracts override generic scheduler wording for that scope;
- ready PR status is candidate status, not an indefinite lane lease;
- the later narrow governance-maintenance liveness protocol controls the NO_NEW_MATHEMATICS maintenance slice.

This retyping preserves historical provenance without allowing legacy control fields to override current role/promotion semantics.
