# X6 Unit264 — Exact optimal-BRC observer separation at original event 3 and event 7

Date: 2026-11-22, 16:00 Asia/Hong_Kong. Parent: `PO-X6-UPPER-STRUCTURE-20260906`. Task: `RS-X6-NATIVE-TIME-DYNAMICS`, publication `TP2-91D4A7C2F63805BE21A3`.
Research-lane continuity: `chatgpt-research-onhour-enterprise-math-20260923` (not a fresh authorization or another conversation's session). Author provenance: Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`. Status: **conditional exact finite theorem, AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_SOURCE_EXECUTION**.

## Frozen basis and original benchmark

P000 input remains `enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`. The original 36-case 12-OUTER Cell, two labeled intact triad, empty-target, directed single-center-Port, signed-winding input remains `enterprise-math@f56840285cafeb9f5767ea91e903e1f53808186f:research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json`. We have not replaced the original 28-event benchmark, the proposed event-3 C24 and event-7 C3 measurements, or the independent R063 task.

The exact conditional graph has state (s=(p_A,p_B,W_A,W_B)), (p_A\ne p_B), (p\in\{x_0,\dots,x_{11},P\}). Initial state is ((x_0,x_2,0,0)), final state ((x_0,x_2,-12,12)), and a single complete labeled triad moves by an allowed signed OUTER edge or the chosen directed ingress (x_i\to P) and egress (P\to x_j). (W_A,W_B) are accumulated signed OUTER ring edges. The original finite search bound is 48 in absolute winding per label.

For the two minimal-cost port choices ((i,j)=(6,0)) and ((8,2)), the existing exact minimum is 28 events and each has precisely 2,832 shortest ordered histories (Unit257). This unit **consumes**, rather than re-proves, those originals and asks whether their original timed observations can be compared in identical visible BRC states.

## New exact finite theorem: forced separation begins at event 7

Let (H_{ij}) denote all 28-event optimal complete histories at Port ((i,j)). Let (S_{ij}(t)) be the support of the full, label-preserving BRC state ((p_A,p_B,W_A,W_B)) immediately after event (t) among (H_{ij}).

Exact shortest-path-DAG counting establishes:

- (S_{60}(t)=S_{82}(t)) as sets for (t=0,1,2,3); at (t=3) all four states overlap, although their optimal-path multiplicities are different.
- At events (t=4,5,6), the intersection contains respectively **3, 2, 1** exact states. At event 6, **240** of the 2,832 histories for each Port occupy the shared state.
- At **every (7\le t\le27)**, the intersection is **empty**. At event 7, even the weaker sets of joint Cell positions ((p_A,p_B)) are disjoint.
- At event 28, both endpoint sets return to the same original terminal state.

In particular:

[
\boxed{S_{60}(7)\cap S_{82}(7)=\varnothing.}
]

No choice of two equally optimal 28-event histories can therefore make the event-7 C3 measurement occur in the same **full visible BRC state** across these two Port conditions. Even matching only the two labeled Cell positions is impossible at event 7. This is a **sampling-context obstruction within the declared graph**, not a claim about the yet-unobserved C3 sensor value or actual Source admission.

### Exact state supports at event 7

In the table below, (P=12), and states list ((p_A,p_B,W_A,W_B)); counts are exact numbers of optimal *ordered histories* occupying that state.

| Port (6,0) state | Histories | Port (8,2) state | Histories |
|---|---:|---|---:|
| ((P,x_2,-6,0)) | 340 | ((x_0,P,0,6)) | 340 |
| ((x_6,x_3,-6,1)) | 980 | ((x_{11},x_8,-1,6)) | 980 |
| ((x_7,x_4,-5,2)) | 1,092 | ((x_{10},x_7,-2,5)) | 1,092 |
| ((x_8,x_5,-4,3)) | 420 | ((x_9,x_6,-3,4)) | 420 |

At event 3, both Port alternatives share precisely the states
((x_0,x_5,0,3)), ((x_{10},x_3,-2,1)), ((x_{11},x_4,-1,2)), and ((x_9,x_2,-3,0)). Their ordered-history frequencies differ; equal support does not imply the same experimental probability distribution.

For the **two already frozen Unit245 witness strings**, both run the original event 3 as (A:x_{10}\to x_9), arriving at ((x_9,x_2,-3,0)). At event 7 they instead have:

- Port (6,0): (A:x_6\to P), a **center ingress**, state ((P,x_2,-6,0)).
- Port (8,2): (B:x_5\to x_6), an **OUTER movement**, state ((x_9,x_6,-3,4)).

Consequently, raw event-7 C3 readings between those original paths must not be interpreted as an isolated Port-internal H6-vs-H12 difference without typed state-conditioning. Recording source, destination, mover label, signed six-axis displacement, environment, complete triad, event time and any frame/mode observer is necessary for causal interpretation.

## Reproducible proof and checks

Exact forward BFS builds the complete bounded signed BRC graph through depth 28. Reverse dynamic programming counts every shortest suffix to the terminal state. Forward counts at each state times reverse suffix counts give the number of full 28-step histories passing that exact state; every event layer sums to 2,832 for each Port. The checker verifies 28 minimal cost, all 5,664 histories, the four-state event-7 disjointness, t4/t5/t6 overlap (3,2,1), all full-state event-7-through-27 disjointness and final return. The same original two Unit245 encoded routes are independently replayed for event 1/3/6/7 labels and states.

Checker: `research_checks/X6_TIME_UNIT264_OPTIMAL_BRC_OBSERVER_SEPARATOR_CHECK_20261122_1600.js`.
Exact machine result: `research_checks/X6_TIME_UNIT264_OPTIMAL_BRC_OBSERVER_SEPARATOR_RESULTS_20261122_1600.json`. A separate Python exhaustive enumeration of all 5,664 routes, not using this DAG counting implementation, confirmed the intersection sequence and event-3/event-7 state supports.

This result is a complete finite proof **conditional on the same source-frozen BRC graph**. It does not claim that physical/source-native whole triads, C24 or C3 observers were executed.

## Next source-native execution and control gap

The highest-value unchanged experiment begins with the actually admitted complete-triad move `A:x0→x11`, exact six-dimensional displacement `(0,0,-1,0,0,0)` (one-based P000 `-E3`), preserving all three force-token IDs, `TRIADIC_CLOSURE_E`, target vacancy, environmental updates, full ordered signed frame and SHELL/CLOSURE if observable, and the true event order. Continue the *original* 28-event paths, collect genuine C24 after event 3 and C3 after event 7, and **retain the event-7 path-context difference** established here. An experimental variant controlling for state would be a distinct experiment and may require longer routes; it cannot retroactively satisfy the original 28-event benchmark.

The current native gateway exposes Source control and read operations but no verified physical whole-triad event executor/observer in this run. Current winning CLAIM remains unverified; protected semantic PROGRESS for Units233–264 must not be written without actual current Source permission. Engineering support remains [#2903](https://github.com/awdawmip/enterprise-math/issues/2903). No new identity, dispatch, overwrite of canonical Result, or scheduler change is part of this author-science preservation.

**Classification:** AUTHOR_PROVED / EXACT_FINITE_EXECUTED / ORIGINAL_INPUT_REUSED / UNREVIEWED / NOT_ADMITTED / NATIVE_SIGNED_TRIAD_NOT_EXECUTED / ORIGINAL_C24_C3_NOT_EXECUTED.
