# X6 Unit259 — Bipartite native-event parity and sharp half-clock repair

Date: 2026-11-22, onhour Research lane. Task `RS-X6-NATIVE-TIME-DYNAMICS` / publication `TP2-91D4A7C2F63805BE21A3`; parent `PO-X6-UPPER-STRUCTURE-20260906`. Researcher `EM-X6-FB6990`, own SID `MCP-082892eb480e45dea6d4b9fcc0491034`. Status: **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_PHYSICAL_EXECUTION**.

## Immutable scope and exact model
Frozen P000: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Original directed-center BRC path source: `enterprise-math@f56840285cafeb9f5767ea91e903e1f53808186f:research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json`. Consume Unit258 finite guard evidence, not redo its E4/E16 covers. Two labeled intact triads occupy different cells of the 12-vertex OUTER cycle `x_0,...,x_11` and common center `P`. Serial events are individual whole-triad moves to empty destinations; signed OUTER steps `x_r -> x_(r+1)` or `x_(r-1)` respectively add +1/-1 to that triad's signed winding. Center events only `x_i -> P -> x_j`, with `i,j` even and no winding increment; for the two original minima the port pairs are (6,0),(8,2). Visible BRC state is `S=(posA,posB,wA,wB)`. We call `t in Z_{>=0}` the number/ordinal of primitive serial events since initial `S0=(0,2,0,0)`. This event index is NOT calibrated physical time, fixed heartbeat duration, a seventh spatial axis, or a verified Source transfer law.

## Theorem A: event parity is already observable, not new independent clock memory
Let `kappa(x_r)=r mod 2`, `kappa(P)=1` and `q(S)=kappa(posA) XOR kappa(posB)`. Every permitted signed OUTER event joins adjacent ring parity classes, and each center event joins an even ring vertex and center P. Every single serial triad event therefore reverses exactly one kappa bit, giving `q(S_{t+1})=1-q(S_t)`. Initially q=0, hence, for *every* valid serial history in this model,

`t mod 2 = q(S_t)`.

This is a global induction for unbounded history lengths, not a finite extrapolation. The assertion holds for every even-even directed Port pair, not just the two optimal pairs, under the stated one-event-per-step graph.

## Theorem B: modulo-2^m event time needs exactly m-1 more bits
Under the symmetric signed candidate transfer, the two events `A:x0->x1 (+e1)` and `A:x1->x0 (-e1)` are legal with B fixed at x2, because x1 is initially empty. They return ALL four visible BRC fields to S0 and preserve intact-triad identity in the candidate model. Repeating the two-event detour k times produces the same S0 at times 2k. For any m>=1, these realize all `2^(m-1)` even residues modulo `2^m` at identical S0. Thus an observer of S alone cannot determine event time modulo `2^m`; any exact repair needs at least `log2(2^(m-1)) = m-1` additional bits at S0.

The bound is attained everywhere: retain `h=floor(t/2) mod 2^(m-1)` together with the existing BRC state and its observable `q`. Recover `t mod 2^m = 2h+q`. At each primitive event use the exact carry update `q'=1-q, h'=h+q (mod 2^(m-1))`. This adds exactly m-1 bits. For m=1 the repair is empty; for m=2 only a single half-clock bit is needed. It distinguishes the initial state from the two-event-return state even though their positions and signed windings are identical.

This is a sharp information statement for the specified ordinal clock observer, NOT a claim that the full physical heartbeat can be recovered from event counts. Simultaneous triad moves, environment-only events, a different center connectivity, hidden guards or additional physically clocked transitions require separate modeling and may invalidate the parity invariant.

## Executed finite check and provenance
The attached standalone Node checker independently generates all signed serial moves with occupancy for each of (6,0),(8,2), confirms q flips for every explored event and q=t mod2 for each reachable full BRC state at all depths 0..28. For each Port it visits 3,711 distinct BRC states, of which 3,039 appear with both compatible `t mod4` residues by depth 28; the exact depth-28 layer has 1,814 states. It verifies the explicit two-event return and tests the half-clock reconstruction/carry algebra for m=1..10 and all t in [0,2^(m+1)). See the exact result JSON for total assertion count. Finite exploration supports and regression-checks the proof; the theorems use induction and the constructive two-event loop.

## Direct native experiment / missing evidence
A precise Source-history-dependence test is to compare admission of `A:x0->x11 (-e2)` in two independently prepared trials: (1) at S0 before any movement; (2) at the same visible S0 after the permitted signed two-event detour x0->x1->x0. Preserve full force-token IDs, closure, occupancy, environment responses, timestamps, and independent C24/C3 observation where defined. A different response at identical S0 falsifies any guard depending only on these four BRC fields. Agreement is only local evidence, not proof of a global Markov guard. These are proposed native measurements; NO real Source admission or physical sensor action has been performed.

Original request `onhour-20261122-1000-x6-exact-task-read-v1` has now been consumed as SUCCEEDED (as-of Task read, not current CLAIM). Earlier continuation failures `SOURCE_TREE_TRUNCATED` remain terminal and are not replayed. No current valid winning claim or protected native semantic PROGRESS is asserted. Existing support: https://github.com/awdawmip/enterprise-math/issues/2903 . Preserve Units233–258 and the R063 unrelated frozen benchmark.
