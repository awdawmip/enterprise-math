# X6 Unit260 — Global signed wrap-edge cut for native-time BRC: beyond optimal paths

2026-11-22 11:57 Asia/Hong_Kong. Parent `PO-X6-UPPER-STRUCTURE-20260906`; Task `RS-X6-NATIVE-TIME-DYNAMICS`; publication `TP2-91D4A7C2F63805BE21A3`. Existing onhour Research author provenance: `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`. Status: **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_PHYSICAL_EXECUTION**.

## Scientific input and exact scope

Frozen P000 `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`, full signed X6 Cell torsor, and original immutable Unit245 certificate `enterprise-math@f56840285cafeb9f5767ea91e903e1f53808186f:research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json`, Git blob `113d2102fe393bfd6f77bf7cca093b4cecf6796f`. Reuse Unit257's complete shortest-path cut and Unit258's contextual refusal distinction; do not rerun their shortest-path enumeration.

The declared conditional BRC model has OUTER directed ring edges on `x0,...,x11` with positive (clockwise) ring winding (+1) and negative (counterclockwise) ring winding (-1). The central port has exactly one directed ingress `x_i -> P` and one directed egress `P -> x_j`, where `i,j` are even in `{0,2,4,6,8,10}`. Center events add zero ring winding. Both labeled intact triads start and end on OUTER Cells; in the original experiment A starts/ends at x0 with signed winding (-12), B at x2 with (+12). Only one triad moves per event, into an unoccupied Cell. A position trace is an ordered BRC history, not an externally verified physical force update.

## Exact global winding conservation identity (all event lengths)

For either labeled triad T in any finite closed OUTER-to-OUTER event history define:

- $R_T$: completed center passages `x_i -> P -> x_j` (ingress and egress counts agree);
- $U_T$: positive ring-boundary traversals `x11 -> x0`;
- $D_T$: negative ring-boundary traversals `x0 -> x11`;
- $W_T$: cumulative signed OUTER winding.

**Theorem.** In the exact directed-port graph, irrespective of path length, event interleaving, or occupancy guard,

$$
\boxed{W_T=R_T(i-j)+12(U_T-D_T).}
$$

**Proof.** Use the integer index potential $\phi(x_k)=k$. For every ring edge except boundary crossing, the signed ring contribution equals $\Delta\phi$. A positive boundary crossing `x11 -> x0` contributes (+12) relative to $\Delta\phi=-11$; a negative boundary crossing `x0 -> x11` contributes (-12) relative to $\Delta\phi=+11$. Each completed center passage changes the index potential by (j-i) while adding zero ring winding. Because T returns to its initial OUTER Cell, the ring-edge potential sum is (-R_T(j-i)=R_T(i-j)). Summing signed ring contributions gives the formula. Occupancy restrictions can only delete paths; they cannot invalidate this identity.

For A's frozen target $W_A=-12$, solve exactly:

$$
\boxed{D_A=U_A+1+\frac{R_A(i-j)}{12}.}
$$

Feasibility therefore requires $12\mid R_A(i-j)$. If **i >= j**, then $D_A\ge1$: **the A-labeled negative primitive edge `x0 -> x11` is unavoidable for EVERY feasible closed target history, regardless of length**. The even-port grid has exactly $6+5+4+3+2+1=21$ ingress/egress choices with $i\ge j$. This includes both original 28-event minimizers `(6,0)` and `(8,2)`. For `(6,0)`, any history with two completed A-center passages requires $D_A\ge2$. For `(8,2)`, an A history with zero center passages requires (D_A\ge1).

This upgrades Unit257's all-5,664-shortest-history negative-edge cut to an **unbounded-length topological necessity** for these port orientations. It does not depend on counting the shortest paths or assuming a temporal period.

## Sharp orientation limit, constructive A-only converse

For each of the 15 port choices (i<j), let (d=j-i), (g=\gcd(12,d)), (R=12/g), (K=d/g-1\ge0). Construct an A-only closed walk from x0:

1. Move positively from x0 to x_i (i ring steps).
2. Complete R passages `x_i -> P -> x_j`. Between consecutive passages travel negatively along the linear OUTER interval from x_j down to x_i. After the last passage travel negatively from x_j to x0.
3. Make K complete positive OUTER tours `x0 -> x1 -> ... -> x11 -> x0`.

Every negative ring edge lies inside the ordinary index interval, so **no `x0 -> x11` event occurs**. The net winding is (-Rd+12K=-12). This proves the orientation-specific cut condition is sharp **in the one-triad conditional graph**. The construction may collide with a concurrently present second triad and is not a two-triad execution witness; a real Source force/environment guard is also separate.

## Executed integer certificate using original evidence

The new standalone Node verifier consumes the exact Unit245 original JSON unchanged. It decodes all 36 chronological two-triad paths (1,312 primitive events), checks proper actor/Cell targets, empty destination, only selected directed Port ingress/egress, both signed winding targets, both individual Cell returns, and the exact identity above for each labeled triad. It also constructs and validates all 15 explicit A-only bypass words under the converse orientation and tests both original 28-event minimizers' exact center/wrap counts. **3,931 exact assertions passed; zero mismatches**.

Original optimal witness readback:

| directed Port | A center passages R_A | A positive boundary wraps U_A | A negative boundary wraps D_A |
| --- | ---: | ---: | ---: |
| (6,0) | 2 | 0 | 2 |
| (8,2) | 0 | 0 | 1 |

Code: `research_checks/X6_TIME_UNIT260_GLOBAL_WINDING_CUT_CHECK_20261122_1157.js`; result: `research_checks/X6_TIME_UNIT260_GLOBAL_WINDING_CUT_RESULTS_20261122_1157.json`. Exact output retains each original Port and every A-only constructed bypass route. This is a conditional signed-BRC exact computation and mathematical proof, not a Source-admitted physical transfer.

## Direct native consequence and next exact action

The original Source discriminant is still signed intact-triad movement `A:x0 -> x11,-e2` with actual token IDs, TRIADIC_CLOSURE_E, Cell occupancy and environment/observer response. **If Source proves context-independent rejection of this transfer over all relevant full states**, the frozen A target is impossible at *any path length* for all 21 port orientations $i\ge j$, including the two original optima. If Source rejects only one observed precontext, apply Unit258's actual-context distinctions; do not extrapolate to a global ban. For (i<j), the A-only bypass construction identifies an alternate orientation class to study only through an authorized Task route; it does not replace the current frozen benchmark.

Current original Research continuation read `onhour-20261122-1103-x6-own-continuation-after-task-terminal-v1` has been consumed: `SUCCEEDED / error=null` as of 2026-11-22T03:18:18Z, `execution_authorized=false`. It does not prove a present winning CLAIM. Prior terminal `SOURCE_TREE_TRUNCATED` requests are not replayed. Existing engineering support is [#2903](https://github.com/awdawmip/enterprise-math/issues/2903). Native semantic PROGRESS, physical Source event and original unrelated R063 six-file benchmark remain unexecuted by this unit. Preserve independent review and mathematical admission boundaries.
