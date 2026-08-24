# Orphan Frontier Maintenance Sweep — 2026-08-24

Status: `DRIVER_CONTROL_PLANE_AUDIT / NO_NEW_MATHEMATICS`

Driver-ID: `EM-DVR-ZX1UEJ`

Initial source snapshot: `main@e19ee6713be002dd9c346261173d39fd8d54f9dc`

Scheduler maintenance recheck: `main@0aa8824250c609283363c662ed875d661972dd43`

## Purpose

Perform one bounded maintenance sweep over current Foundation routing, scheduler/runtime evidence, open owner/provenance PRs, and frozen candidate intake. Distinguish:

1. **maintenance orphan** — mathematics/source already closed but machine routing remains active;
2. **research orphan** — a bounded unresolved question/candidate has no active owner or next execution object;
3. **stale scheduler entry** — an old READY/HANDOFF entry has been superseded by later owner work;
4. **publication/formalization debt** — mathematics is already closed enough that reopening research would be wasteful;
5. **active routed work** — already has an owner/gate and is not orphaned.

No issue/PR being open or unassigned is by itself evidence of an orphan. Canonical problem status, runtime scheduler events, later owner generations, and candidate lineage control classification.

## 1. Immediate maintenance orphan — FQ-20260809-005

Verdict: `DIRECT_FOUNDATION_MAINTENANCE_REQUIRED / DO_NOT_REOPEN_RESEARCH`.

Evidence:

- research task `RS-P022-GRAPH-DISTANCE-API` emitted runtime `DONE` on 2026-08-10 with frozen PR #431 head `ca351e5446b3a84835ade9509f1ab97c276841d9` and all three exact-head gates successful;
- Foundation Steward accepted the answer;
- canonical L4 source replay PR #436 merged as `3a40fe680e7aad4bc458540483c3c753e15f2cc4`;
- PR #436 explicitly left Common Surface / Foundation alert cleanup as a direct post-source-canonical maintenance step;
- current `foundation_steward.json`, `research_common_surface.json`, and `foundation_backflow.json` nevertheless still expose FQ-005 as active/scheduled.

Required bounded repair:

- remove `FQ-20260809-005` from active Foundation question sets;
- remove its active interface alert;
- remove its active scheduler link;
- add it to canonicalized backflow examples with PR #436 / canonical merge `3a40fe680e7aad4bc458540483c3c753e15f2cc4`;
- expose the canonical graph-distance API layering as the A5/P012 specialization if not already indexed;
- preserve the historical scheduler task/runtime DONE events as provenance; do not redispatch it.

This is stale propagation, not mathematical uncertainty.

A control-plane maintenance note was posted to Foundation Issue #164 during this sweep. The machine-file propagation repair remains a bounded governance write and is not represented as already merged here.

## 2. FQ-20260810-007 — not a research orphan

Verdict: `MATHEMATICALLY_ANSWERED / SOURCE_INTEGRATION_DEBT`.

The R004/FQ-007 research task reached a finite counterfactual-completion no-go and emitted runtime DONE. Steward verification/closure recommendation exists. PR #444 is the narrow L4 source candidate for T01–T03/C01 and is still open/unmerged on an old base.

Consequence:

- do not open another causal-identifiability research task merely because current machine routers still list FQ-007 active;
- the next action is bounded current-main source-integration disposition for PR #444 or an exact replay of its frozen payload, followed by active-set propagation if merged;
- later derived R004 sharpenings remain separate provenance and must not be silently folded into the T01–T03 payload.

## 3. Genuine research orphan — segment rotation orthogonal trace-frame candidate

Frozen source: `driver_reviews/SEGMENT_ROTATION_ORTHOGONAL_TRACE_FRAME_DRIVER_INTAKE_20260824.md@c6d2e2f89a2f59a00323f2b0d8c1427a738bd382`.

Lifecycle: `CANDIDATE_FROZEN / ANCHOR_EXPOSED / PHASE_B_SEMANTIC_AUDIT_REQUIRED`.

Verdict: `HIGH_VALUE_ORPHAN / ADVANCE_TO_PHASE_B_AUDIT`.

Why it is worth continuing:

- it has a small, explicit semantic delta rather than a broad new direction;
- the candidate already produced exact algebraic consequences (`C3` coordinate rotation, gauge invariance, positive `Delta_S`, carrier-frame sublattice index/integrality boundary, and a lower-envelope inequality candidate);
- the unresolved residue is semantic/foundational, not a request for more parameter fitting;
- there are four discriminating outcomes and hard kill conditions;
- no formal Phase-B audit object currently owns the residue.

The candidate must **not** be promoted directly to a taskbook: the candidate state machine requires Phase-B audit before task/Foundation promotion.

A bounded Phase-B audit packet is added separately in this maintenance generation.

## 4. P017 scheduler orphans — stale entry names, not clean new starts

### RS-P017-GLOBAL-CAPACITY

Runtime search found no claim under this exact old task id, but later P017 owner work materially executed the same frontier:

- PR #191: signed/full-core collision geometry and CG12 arbitrary composite-divisor signed capacity;
- PR #170: P017×P018 divisor-token descent/capacity and analytic core-mass bridge;
- PR #526: Walsh-L2 pause checkpoint with an updated weighted-boundary resume frontier.

Verdict: `SEMANTICALLY_ABSORBED_BY_LATER_OWNER_WORK`.

Do not redispatch the old broad task as written. If P017 is resumed, use the exact resume frontier frozen by the latest P017×P018 checkpoint, not the 2026-08-09 scheduler wording.

Runtime maintenance action: `SUPERSEDE` emitted on Issue #240 at `2026-08-24T10:06:20+08:00`.

### RS-P017-P018-ANALYTIC-MASS

The old analytic-mass expression was directly developed in PR #170, including local Euler cancellation, fixed-M leading behavior, moving-M separation, and a local-calibration negative boundary. The route later moved to token/capacity and Walsh weighted-boundary questions.

Verdict: `ABSORBED / DO_NOT_REDISPATCH_AS_IS`.

Runtime maintenance action: `SUPERSEDE` emitted on Issue #240 at `2026-08-24T10:06:30+08:00`.

## 5. P018 ternary carry — formalization debt, not orphan mathematics

`RS-P018-TERNARY-CARRY` was claimed and handed off. Ordinary mathematics was already closed enough that the remaining action is Lean atlas decomposition/cardinality on Draft PR #328.

Verdict: `FORMALIZATION_DEBT / DEFER_BEHIND_CURRENT_FORMALIZATION_QUEUE`.

Do not restart the mathematical route merely because the draft is old.

## 6. P021 focusing/direction — possible residue, but old task is too broad

The old `RS-P021-FOCUSING-DIRECTION` static entry has no runtime claim. Canonical P021 already promoted a causal-boundary slice through PR #202, while historical/v2 work developed direction-orbit, composability and witness-transport structure. Generic witness/future-support/composition content is now upstream A2/A4/BRC territory.

Verdict: `POSSIBLE_OWNER_LOCAL_RESIDUE / DO_NOT_REDISPATCH_BROAD_TASK`.

This is the **second-best orphan candidate**, but only after narrowing. A future P021 task is justified if it declares one finite P021-specific observable such as a genuinely causal focusing/direction-role invariant that does not reduce to an A2 future signature, A4/BRC witness join, or generic finite symmetry orbit. No runtime `SUPERSEDE` is emitted here because owner-local residue may still exist.

## 7. P024 higher-action precision — old generic task already executed by later generations

The static `RS-P024-HIGHER-ACTION-PRECISION` entry has no runtime event, but later P024 owner work explicitly covered the task's named targets:

- state-dependent guarded translations and exact prefix profiles (#310);
- positive guarded reduction (#314);
- two-sided peak/defect/affine horizon laws (#315);
- interval prefix-envelope/nonconvex-fiber boundary (#316);
- higher-dimensional one-linear-guard scalar factorization (#320);
- multi-guard bottleneck lifetime (#323);
- exact guarded-word operational normal form (#326).

Verdict: `SEMANTICALLY_EXECUTED / SUPERSEDED_STATIC_ENTRY`.

Runtime maintenance action: `SUPERSEDE` emitted on Issue #240 at `2026-08-24T10:06:40+08:00`.

Any new P024 task must name a residue not already owned by these generations and pass the current successor/tool-dedup gate.

## 8. P025 witness precision — stale scheduler orphan absorbed by a long active lineage

The static `RS-P025-WITNESS-PRECISION` entry has no matching runtime event, but P025 subsequently advanced through many owner generations, including exact witness-radius layers, restricted-minimum prior-art classification, certificate/index/access geometry, future-relative precision, closure/witness width, helper/scheduler support, and Stage 155–160 state/action support Pareto results.

Verdict: `SUPERSEDED_STATIC_ENTRY / DO_NOT_REDISPATCH`.

Runtime maintenance action: `SUPERSEDE` emitted on Issue #240 at `2026-08-24T10:06:50+08:00`.

Any future P025 continuation must pass the successor gate from the latest Stage-160 frontier, not return to the old scheduler task.

## 9. R037/R038 static READY entries — runtime is already complete

The durable scheduler still shows old `READY` base states, but runtime authority already closes both:

- R037 returned independent replication PR #522 with zero theorem-critical mismatch and a typed evidence matrix;
- R038 emitted runtime `DONE` for Draft PR #521 / owner head `d45cb42de4e259439ce1b56c7fa00debabbeb129`;
- subsequent R044/R045 semantic backtest/repair preserved conditional mathematics and repaired R038-C05/C06 at N0 typing strength (PR #533).

Verdict: `STATIC_BASE_STATE_STALE_BUT_RUNTIME_COMPLETE`.

No new scheduler event is needed; the reducer already treats DONE as complete. The long-term maintenance improvement is to reconcile durable base-state prose with runtime-complete generations so human readers do not mistake old READY text for current frontier.

## 10. P022 observation-history — old handoff is not yet classified as an orphan

`RS-P022-OBSERVATION-HISTORY` has real CLAIM/PROGRESS/HANDOFF history, including a nontrivial composite-index/unimodular-completion frontier. Unlike the stale P017/P024/P025 entries, it cannot be retired solely from age or lack of recent scheduling.

Verdict: `DORMANT_HANDOFF / NEEDS_EXACT_LATEST_OWNER_LINEAGE_AUDIT_BEFORE_REACTIVATION`.

It is not promoted into the current priority list because current Driver Continuity has stronger active gates, and because the old handoff mixes several geometry/valuation subfrontiers that must first be checked against later P022/R033/R034/R037 work. Preserve rather than redispatch blindly.

## 11. Open/no-assignee GitHub issues are mostly historical, not orphans

Several old open issues correspond to canonically resolved problems (including early P001/P002/P003/P011-era entries) or umbrella programs whose current owner/status lives elsewhere. Therefore `is:open no:assignee` is not a valid orphan detector.

The orphan detector for maintenance should use the conjunction:

`CANONICAL_STATUS + RUNTIME_EVENT_HISTORY + LATEST_OWNER_LINEAGE + CURRENT_SUCCESSOR_GATE + ACTIVE_MACHINE_ROUTING`.

## Runtime maintenance performed in this sweep

The following stale static task entries had no live runtime claim and were backed by later owner evidence strong enough to make the old wording unsafe to redispatch. Issue #240 now contains `SUPERSEDE` events for:

1. `RS-P017-GLOBAL-CAPACITY`;
2. `RS-P017-P018-ANALYTIC-MASS`;
3. `RS-P024-HIGHER-ACTION-PRECISION`;
4. `RS-P025-WITNESS-PRECISION`.

This changes runtime dispatch state to `COMPLETE` for those exact old task IDs without rewriting their historical static definitions.

## Priority after this sweep

1. **P0 maintenance:** close FQ-005 machine propagation drift. No new mathematics.
2. **P0/P1 bounded integration:** disposition FQ-007 PR #444 on current main; do not reopen its research question.
3. **P1 research:** execute Phase-B semantic consistency/minimality audit for the segment-rotation orthogonal trace-frame candidate.
4. **P2 conditional research:** if a second orphan lane is desired, narrow P021 to one owner-local causal focusing/direction observable and dedup it against A2/A4/BRC/T7 before task creation.
5. **P1 active portfolio:** continue already-routed current gates (#609–#614 etc.) according to Driver Continuity; they are not orphans.
6. **Preserve/defer:** P018 formalization debt and P022 dormant handoff until the relevant current queue/frontier warrants them.

## Maintenance invariant

`OLD_READY != CURRENT_RESEARCH_FRONTIER`.

`OPEN_UNASSIGNED_ISSUE != ORPHAN_RESEARCH`.

`SOURCE_CANONICAL + ACTIVE_MACHINE_ROUTE = MAINTENANCE_ORPHAN`.

`FROZEN_BOUNDED_CANDIDATE + NO_PHASE_B_OWNER + DISCRIMINATING_RESIDUE = RESEARCH_ORPHAN_WORTH_AUDIT`.

`STATIC_READY + LATER_OWNER_EXECUTION + NO_RUNTIME_CLOSURE = EMIT_RUNTIME_SUPERSEDE`.
