# X6 R20 — Consumable-resource Port vacancy depth and joint-credit residual

**Date:** 2026-11-19 (Asia/Shanghai). **Task:** RS-X6-NATIVE-TIME-DYNAMICS; publication TP2-91D4A7C2F63805BE21A3. **Author-side continuation:** EM-X6-214D9C; Activity RA-545183ADD4EF71C3E4698AEE (historical identity/source attribution, without a new claim). **Scientific status:** conditional propositions proved by the author, with exact finite checks, **NOT_REVIEWED**. This portable source file does not constitute a formal native PROGRESS or a frozen Result.

## Input and preserved science pin

Immutable task P000 V5 input: awdawmip/enterprise-math at commit a72226e2430ffa4786321ac86e7f0c599d5f0389, path p000_reality_foundation.json. Immutable taskbook: research_tasks/RS_X6_NATIVE_TIME_DYNAMICS_20260906.md at f41c2690daba467ecbde99615a1337e67be46ffd, verified Git blob eba80ae0be492033f9eda082aac2b017f7398114. Current GLOBAL_KNOWLEDGE_V1 P000 V4 and ACTIVE worldview were applied to interpretation, without repinning the scientific input.

Direct predecessor: [R19 directed vacancy theorem](2026-11-19_x6_directed_port_guarded_vacancy_r19.md), which computed directed vacancy distances with persistent static Port edges and exhibited a failure when two individually legal edges share one nonrenewable credit. The predecessor's conditional whole-triad relocation model is located at research_artifacts/mcp/RS-X6-NATIVE-TIME-DYNAMICS/MCP-456b8f22a648400585024ffbcc1c2c94/5a04daccb6795e494dbc/X6_TIME_GUARDED_TRIADIC_RESOURCE_CONFLICT_20261118.md at immutable Source f41c2690daba467ecbde99615a1337e67be46ffd.

P000 fixes six native spatial axes, signed primitive directions, the separate non-spatial time dimension and triadic closure as the minimal nonzero stable action. A general concrete Cell/Link/Port transfer authorization is still an open derived law. R20 studies an explicitly declared class of conditional controllers.

## Event system and observer

Let W be a finite set of addresses in one chart of the six-dimensional native Cell torsor over the integers. A fixed directed Port graph E consists only of edges u→v with v−u equal to one of the twelve signed native unit-axis displacements. Every occupied Cell contains a unique labelled **intact triadic carrier** satisfying a declared common closure-valid frame/type. The whole carrier moves, and there is no two-force primitive intermediate state. All carriers at the same site have identical admissible E-ports: **source-neutrality**.

Each directed edge e consumes a fixed nonnegative integer resource vector c(e) in N^q. Initially the shared controller has C in N^q; no resource is ever replenished, refunded or transferred. An event (source-label,u→v) is legal iff the labelled carrier occupies u, e belongs to E, v is vacant, and the remaining credit vector dominates c(e). The event moves that carrier intact, updates the vacancy, reduces remaining credit by c(e), and preserves chronological Port and source labels. Source labels do not determine the guard. The Boolean BRC observable is the support of all completely labelled **successful event words**; it is not a success/failure-oracle language, an unlabeled occupation histogram, or a physical duration.

Write S for initial occupied sites, V=W\S for initial vacancies. Define the credit-constrained directed distance for an occupied initial site z:

\[
D_C(z,V)=\min\left\{ |p|:\ p:z\leadsto v\in V \text{ is an E-path},\
\sum_{e\in p} c(e)\leq C\text{ componentwise}\right\},
\]

with value infinity when no feasible path exists. Each edge counts as one event, even when c(e)=0. For r≥0 let

\[
T_C(z,r)=\{x\in W:\ \exists p:z\leadsto x,\ |p|\leq r,\
\sum_{e\in p}c(e)\leq C\}.
\]

In a finite graph, a shortest resource-feasible path can be chosen simple because all edge lengths are one and costs are nonnegative.

## R20.1 — Exact first movement with nonreplenishing shared credits

**Theorem.** For every finite W,E,c,C,S as above and occupied z, the minimum positive event index at which the source *initially at z* can execute its first move in some fully legal labelled event history is **exactly** D_C(z,V). In particular, D_C(z,V)=infinity iff that source can never move under this controller.

**Proof of lower bound.** Give each initial vacancy an auxiliary unique token (the tokens are proof devices, not observable source labels). Whenever an occupied source moves u→v into a vacancy, that vacancy token moves backward v→u. Suppose the original source at z moves for the first time at event k into a vacant site y. Trace the vacancy token found at y backward through its previous carriers to one original vacancy v in V. The edges along this token ancestry, plus the final edge z→y, form a directed walk from z to v of at most k edges. The ancestry moves form a submultiset of the executed moves, so their nonnegative credit cost is componentwise at most the total credit consumed by that history, which is ≤C. Deleting cycles from this walk retains a directed path of no greater length or cost. Therefore D_C(z,V)≤k.

**Proof of attainment.** Choose a shortest feasible directed path z=x_0→x_1→...→x_d=v in V, d=D_C(z,V)<infinity. Every x_i with i<d must be initially occupied, or else a shorter feasible path to that intermediate vacancy would exist. Move the entire carriers in reverse-path order x_{d−1}→x_d, x_{d−2}→x_{d−1}, ..., x_0→x_1. Every target is vacant at the instant of its move; the resource cost of every chronological prefix is a sub-sum of the feasible path's nonnegative costs and thus is at most C. The original source z moves at event d. For infinite distance, the lower-bound argument excludes a first movement. QED.

This replaces R19's generally non-sharp static-graph lower bound by an **exact answer for this particular stateful controller class**. Zero-cost vectors recover the predecessor. A controller with replenishment, source-specific Port restrictions or other history-dependent guards requires a different product state.

## R20.2 — Exact unequal-depth label transposition and permanent invisibility

Let P and Q have the same occupied set S, directed edges, costs and starting C, with labels A and B interchanged between occupied distinct a,b. All other labels remain fixed. Let L_h(X) be the Boolean BRC language of successful source/Port event words of length at most h from X, and let δ(P,Q) be the least h≥1 with L_h(P) different from L_h(Q), or infinity if none. Put d_a=D_C(a,V), d_b=D_C(b,V).

**Theorem.** The two languages coincide for all words of length strictly less than min(d_a,d_b). If d_a and d_b differ, then

\[
\delta(P,Q)=\min(d_a,d_b).
\]

If both are infinite, their full finite-word future languages are identical: L_infinity(P)=L_infinity(Q). Equal finite depths require a further test.

**Proof.** Before either swapped label can move, the remaining labels, vacancies and shared credits evolve identically on any common legal prefix, by source-neutrality. This proves indistinguishability below the minimum depth. Suppose d_a<d_b. A shortest credit-feasible path from a to an initial vacancy cannot traverse b, since its suffix starting at b would be credit-feasible and strictly shorter than the whole path, contradicting d_b>d_a. The reverse-release sequence for this path consists of identical unaffected-source labelled events in P and Q until its final A event; the latter succeeds from a in P at index d_a. In Q, A begins at b and by R20.1 no A event can be legal at index d_a<d_b. This is a distinguishing word. The case d_b<d_a is symmetric. If both depths are infinite, neither swapped label can ever move; source-neutrality implies by induction that every successful word involving only the other labels is legal in both or neither state. QED.

This observer sees executed labelled moves only. A direct snapshot showing every labelled Cell would of course distinguish the transposition without waiting for an event.

## R20.3 — Sharp credit-constrained immobility shield

**Theorem.** For prescribed initial occupied a,b and event horizon r≥0, neither initially placed source can move in any legal event history of length at most r iff

\[
T_C(a,r)\cup T_C(b,r)\subseteq S.
\]

The smallest occupied population enforcing this **particular two-source immobility certificate** under fixed E,c,C is therefore exactly

\[
N_{E,c,C}(a,b;r)=|T_C(a,r)\cup T_C(b,r)|.
\]

**Proof.** R20.1 says that z can first move by event r iff a reachable initial vacancy occurs in the credit-constrained r-ball T_C(z,r). Both sources are immobile through r precisely when neither ball contains an initial vacancy; this is the stated inclusion. Every admissible S must contain the union, and choosing S to equal that union attains the bound. QED. This is a population extremum for guaranteed immobility, not a claim about the minimum over every conceivable history-language aliasing mechanism.

## R20.4 — Two spatially disjoint moves fail Boolean-support factorization

Choose four native six-coordinate Cells 0, e_1, e_2, e_1+e_2. Initially occupy 0 and e_1 with distinct intact triadic carriers, leaving the other two vacant. Permit only the directed signed-axis moves 0→e_2 and e_1→e_1+e_2, each consuming one unit from **the same global credit**, with C=1. Either labelled one-event word succeeds. After either, the common credit is exhausted, so both two-event concatenations fail. Consequently independent single-source Boolean BRC factors would falsely assert a two-event branch. The **joint remaining-credit coordinate** is a genuine future-language residual and cannot generally be erased by assuming that disjoint Cell footprints imply independent resource footprints. This is an exact conditional counterexample, not a physical energy law.

## Exact algorithm and independently computed evidence

For any fixed q and finite W, compute D_C by BFS over states (Port vertex, cumulative credit vector) with componentwise bounds 0≤used≤C; each transition has event length one and adds c(e). A predecessor chain provides the shortest feasible path and, by reverse vacancy propagation, a fully labelled witness. There are at most |W| times the product of (C_i+1) states and at most |E| times that product of transitions in the straightforward explicit adjacency model; credit magnitudes are input-dependent. For mathematical evidence the Boolean carrier retains the complete source/event label words and does not collapse to positive total mass.

Executable Node.js verifier: [x6_guarded_consumable_vacancy_brc_verify_r20.js](x6_guarded_consumable_vacancy_brc_verify_r20.js), with saved exact result [JSON](x6_guarded_consumable_vacancy_brc_results_r20.json). Six declared Cell sites use full six-coordinate records and span a three-axis **subchart**, not a native two-dimensional plane or the complete X6 world. All 14 signed primitive directed links among those six sites are available for selection. The deterministic checker covers 24 chosen graph/cost patterns (six named and eighteen seeded), 63 nonempty occupied subsets, and each initial credit vector in {0,1,2}^2. It independently BFS-explores the complete occupancy/first-labelled-source/remaining-credit product, compares earliest events with the constrained path algorithm, replays strict transposition witnesses preserving identity, and checks the resource-ball shield characterization at horizons 0..3. The one-credit no-factorization witness is also checked.

**Actual exact verification result: PASS.** There were 41,472 first-source movement comparisons, 24,597 strict label-swap witness tests, 165,888 shield equivalence checks, and 13,213 pairs for which both exchanged labels were permanently immobile within the tested finite-credit controller. This does not exhaust every possible six-dimensional directed graph or arbitrary triadic native controller. General statements R20.1–R20.3 are supported by the proofs above; exact finite enumeration is independent evidence for its stated domain.

## Native transfer and next unresolved unit

The frozen P000 triadic predicate does not alone give source-neutral persistent Port eligibility or a nonreplenishing integer credit law. To obtain a native X6 transfer, read an actually authenticated Cell/Link/Port update specification, including source-frame variation, triadic stability across the whole event, resource replenishment, and chronological ledger semantics. If the actual law is of R20's type, supply a faithful map of actual states/events to (placement, E, remaining credit) and prove it respects both enabled transitions and labels. Otherwise compute exact guarded Boolean BRC first-hit depth and future-language equivalence in the real product state, retaining source/Port/triad provenance. A smallest counterexample with replenishing credit or a source-dependent Port is the next discriminating test. Native physical adoption and independent review remain open.
