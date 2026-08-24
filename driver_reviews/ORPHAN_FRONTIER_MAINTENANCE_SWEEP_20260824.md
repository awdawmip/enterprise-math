# Orphan Frontier Maintenance Sweep — 2026-08-24

Status: `DRIVER_CONTROL_PLANE_AUDIT / NO_NEW_MATHEMATICS`

Driver-ID: `EM-DVR-ZX1UEJ`

Source snapshot: `main@e19ee6713be002dd9c346261173d39fd8d54f9dc`

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

### RS-P017-P018-ANALYTIC-MASS

The old analytic-mass expression was directly developed in PR #170, including local Euler cancellation, fixed-M leading behavior, moving-M separation, and a local-calibration negative boundary. The route later moved to token/capacity and Walsh weighted-boundary questions.

Verdict: `ABSORBED / DO_NOT_REDISPATCH_AS_IS`.

## 5. P018 ternary carry — formalization debt, not orphan mathematics

`RS-P018-TERNARY-CARRY` was claimed and handed off. Ordinary mathematics was already closed enough that the remaining action is Lean atlas decomposition/cardinality on Draft PR #328.

Verdict: `FORMALIZATION_DEBT / DEFER_BEHIND_CURRENT_FORMALIZATION_QUEUE`.

Do not restart the mathematical route merely because the draft is old.

## 6. P021 focusing/direction — old task too broad to revive as-is

The old `RS-P021-FOCUSING-DIRECTION` static entry has no runtime claim, but subsequent P021/R020/R021/BRC work resolved or upstreamed much of its generic witness/future-support content.

Verdict: `STALE_BROAD_TASK / REOPEN_ONLY_WITH_P021_SPECIFIC_OBSERVABLE`.

A future P021 task is justified only if it identifies a finite causal/focusing observable that is not already an A2/A4/BRC witness/future-signature instance. Do not revive the broad historical wording.

## 7. P025 witness precision — stale scheduler orphan absorbed by a long active lineage

The static `RS-P025-WITNESS-PRECISION` entry has no matching runtime event, but P025 subsequently advanced through many owner generations, including exact witness-radius layers, restricted-minimum prior-art classification, certificate/index/access geometry, future-relative precision, closure/witness width, helper/scheduler support, and Stage 155–160 state/action support Pareto results.

Verdict: `SUPERSEDED_STATIC_ENTRY / DO_NOT_REDISPATCH`.

Any future P025 continuation must pass the successor gate from the latest Stage-160 frontier, not return to the old scheduler task.

## 8. Open/no-assignee GitHub issues are mostly historical, not orphans

Several old open issues correspond to canonically resolved problems (including early P001/P002/P003/P011-era entries) or umbrella programs whose current owner/status lives elsewhere. Therefore `is:open no:assignee` is not a valid orphan detector.

The orphan detector for maintenance should use the conjunction:

`CANONICAL_STATUS + RUNTIME_EVENT_HISTORY + LATEST_OWNER_LINEAGE + CURRENT_SUCCESSOR_GATE + ACTIVE_MACHINE_ROUTING`.

## Priority after this sweep

1. **P0 maintenance:** close FQ-005 machine propagation drift. No new mathematics.
2. **P0/P1 bounded integration:** disposition FQ-007 PR #444 on current main; do not reopen its research question.
3. **P1 research:** execute Phase-B semantic consistency/minimality audit for the segment-rotation orthogonal trace-frame candidate.
4. **P1 active portfolio:** continue already-routed current gates (#609–#614 etc.) according to Driver Continuity; they are not orphans.
5. **Park:** old P017/P021/P025 scheduler entries unless a new successor gate is written from the latest semantic frontier.

## Maintenance invariant

`OLD_READY != CURRENT_RESEARCH_FRONTIER`.

`OPEN_UNASSIGNED_ISSUE != ORPHAN_RESEARCH`.

`SOURCE_CANONICAL + ACTIVE_MACHINE_ROUTE = MAINTENANCE_ORPHAN`.

`FROZEN_BOUNDED_CANDIDATE + NO_PHASE_B_OWNER + DISCRIMINATING_RESIDUE = RESEARCH_ORPHAN_WORTH_AUDIT`.
