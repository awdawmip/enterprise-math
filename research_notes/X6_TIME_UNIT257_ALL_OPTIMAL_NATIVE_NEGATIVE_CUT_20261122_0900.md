# X6 Unit257 — all 28-event optimal BRC histories, universal negative-link cuts and contextual native admission

**2026-11-22 · RS-X6-NATIVE-TIME-DYNAMICS · parent PO-X6-UPPER-STRUCTURE-20260906.** Research provenance: original onhour Research lane `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`; separate from CONTROL_PLANE_MAINTENANCE. Frozen science `enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; original Unit245 exact BRC model/certificate `enterprise-math@f56840285cafeb9f5767ea91e903e1f53808186f`. Status **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_PHYSICAL_EXECUTION**.

## Why Unit256's frontier matters

Unit256 found two *stored* 28-event optimum histories for directed Ports (6,0) and (8,2); both start with `A:x0→x11,-e2`, and their negative directed links share eight members. But a stored BFS witness is not *all* shortest histories. The missing scientific test is whether the link is unavoidable across all shortest labeled BRC paths, including different orders of moving A and B. This directly governs whether a failed first physical Source probe excludes merely a selected witness or an entire optimal route class.

## Exact conditional population and complete proof

Re-use exactly Unit245's 12 OUTER Cells `x0..x11` and centre `P`, **two individually labeled intact triads** A,B; ring steps `x_k→x_(k±1)` increment signed winding by ±1, while `x_i→P` and `P→x_j` are the sole allowed directed Port steps and change winding by zero. Every event is a native signed unit-axis step in the declared six-dimensional X6 chart. A serial move into the Cell of the other triad is forbidden. Initial complete state `(A=x0,B=x2,wA=0,wB=0)`; goal `(x0,x2,-12,+12)`. The partial three-axis display is a declared restricted X6 construction, not a separately existing native plane or physical law. No environment, force-update or sensor approval is silently added.

A FIFO breadth-first search on the complete four-register state gives distance **28** for the two previously proved minimum Port settings (6,0), (8,2), consistent with Unit245. The winding bound ±48 does not exclude any route of length ≤28. Construct the layer-by-layer shortest-path DAG and count all accepting completions by the exact integer recurrence `C(goal)=1`, `C(s)=Σ C(t)` over permitted next-depth successors. **Independently enumerate** every accepting 28-event history and compare the path count, typed signed edges and per-path *presence* of each directed link. Presence is Boolean per history; an edge appearing twice must not masquerade as an unavoidable edge merely by summing occurrence counts.

Both the Python independently executed local checker and the persisted runnable JavaScript checker give the same exact outcomes. The GitHub JavaScript is a new reimplementation of the same Unit245 model, not a separate native physics engine.

| Directed centre Port | All shortest histories | First A:x0→x11 | First B:x2→x3 | x0→x11 occurrences in every history |
|---|---:|---:|---:|---|
| (6,0) | **2,832** | 2,200 | 632 | **2** |
| (8,2) | **2,832** | 632 | 2,200 | **1** |

These are counts of distinct complete labeled serial event histories, **not statistical probabilities**. A fully explicit B-first 28-event alternative witness is contained for each Port in the exact result JSON; this disproves an erroneous universal interpretation of Unit256's **first** event. Yet the directed link `A:x0→x11,-e2` itself appears somewhere in *all* 5,664 shortest histories.

For each Port, every shortest history contains ten individually mandatory negative directed Cell links. Their **common intersection of eight** across the two Port choices is:

`x0→x11 (-e2)`; `x11→x10 (-e0)`; `x10→x9 (-e1)`; `x3→x4 (-e1)`; `x4→x5 (-e0)`; `x5→x6 (-e2)`; `x6→x7 (-e1)`; `x8→x7 (-e0)`.

This upgrades the two-witness overlap of Unit256 into a **universal directed edge cut** for the *entire* finite conditional 28-event optimal population. It says nothing about longer histories, a changed target, a different Port or physical native execution.

## The decisive context qualification

Although `A:x0→x11,-e2` is mandatory as an edge, its permitted BRC **pre-event state is not unique**. For Port (6,0), the edge can occur at event positions **1,2,3,4,9,10,11,12,20,21**, across ten distinct reachable BRC precontexts. For Port (8,2), it can occur at positions **1–16**, across sixteen BRC precontexts. Each is represented in the certificate by exact event depth, positions `(posA,posB)`, integer windings `(wA,wB)` and moving triad.

Consequently:

* A **context-independent** native Source rejection of the signed intact-triad link, or an actual refusal covering every relevant reachable physical environment, excludes all 5,664 conditional 28-event histories under the fixed two Port choices.
* A rejection of this **single event in only the initial actual environment** is not proof of that stronger result. Another history may first move B or change its environment. Test whether the Source guard is context dependent; preserve the full triad/token IDs, target occupancy, time ordering, ambient response and observer evidence.
* Admitting the initial link only certifies that one actual Source event and its guard context. It does **not** validate the other seven shared links, the remaining 27 events of a chosen witness, C24/C3 readings, or the original native benchmark.

This distinction follows the project BRC observer/provenance preservation rule: reducing the event history to a bare directed-edge name is **not** sound for a state-dependent admission decision without a separately verified descent/fiber-constancy certificate.

## Execution evidence and next action

Persisted files: `research_checks/X6_TIME_UNIT257_ALL_OPTIMAL_BRC_NEGATIVE_CUT_CHECK_20261122_0900.js` and `research_checks/X6_TIME_UNIT257_ALL_OPTIMAL_BRC_NEGATIVE_CUT_RESULTS_20261122_0900.json`; a second Python checker was independently executed in this research turn. Both computations returned 2,832 per Port, first-event split 2,200/632 and 632/2,200, ten mandatory negative links per Port, eight shared, and ten/sixteen exact event-precontexts.

Next actual scientific test: obtain **authorized Source admission/rejection** of intact triad A's `x0→x11,-e2` movement in the true initial configuration, recording its actual force-closure, target occupancy, environment and time/observer receipt. If rejected, determine the real guard's scope before generalizing to other precontexts. If admitted, advance only the originally specified 28-event Port sequence under its own live guards, taking the original Unit251–252 C24/C3 measurements. Preserve all original native input pins and the separate R063 benchmark.

Original Research continuation requests `onhour-20261122-0004-x6-own-source-continuation-v1` and `onhour-20261122-0756-x6-own-source-continuation-read-v1` remain terminal `FAILED/SOURCE_TREE_TRUNCATED`; Gateway status was 0.6.11. No current winning CLAIM was established. Protected Native semantic PROGRESS, formal Result, independent review and native physics run were **not published**. Existing engineering support remains [#2903](https://github.com/awdawmip/enterprise-math/issues/2903). No maintenance identity, scheduler or hosted CI was used.
