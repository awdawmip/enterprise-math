# R762HI — Exact five-vertex coloured-graph factor oracle and two-layer Euler saturation on six-axis Port walks

**Status:** AUTHOR-PROVED (HI1–HI3); EXACT FINITE CHECK (all named closed Port walks from 01 at m=2,4,6,8); NOT_REVIEWED.  
**Scope:** signed six-axis three-support composite Port candidate language. No native primitive TRIADIC_CLOSURE_E admission or physical force law is claimed.  
**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142; original contribution line EM-X6-3050F6, RA-6068F717D991DF54FBBDDEED (historical association only).  
**Frozen source:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json, with the corresponding P000 definitions and joint-relation preservation rule.  
**Predecessor:** R762HH at awdawmip/enterprise-math@3f26bc100cf7089c3b91a9b533457c20a4cc72d6:research_notes/portable_direct/R762HH_FIVE_AXIS_DUAL_EULER_AND_PASCH_OBSTRUCTION.md.

## Model and question

Let X={0,1,2,3,4,5}. A named Port is a 2-subset P of X. An unsigned Port event P->Q is allowed in this **candidate** language when |P∩Q|=1; its support is S=P∪Q, of size three. Independently assigning an event sign ε_t in {+1,-1} gives composite chart-relative Cell displacement ΔC=Σ_t ε_t h_{S_t} in Z^6. Repeated supports, order, Port and event identities remain distinct BRC source occurrences. An event of this kind is not asserted primitive under P000. We seek a complete finite exact sign-existence and multiplicity oracle for each unsigned history, and an unbounded six-axis sufficient family beyond the five-axis restrictions of R762HG/HH.

## HI1. Exact coloured-graph factor theorem (arbitrary finite length)

Choose **any** distinguished axis c∈X and put Y=X\{c}, |Y|=5. For every event occurrence t, define a coloured *edge occurrence* E_t⊂Y and type δ_t∈{0,1} by

- if c∈S_t: δ_t=1 and E_t=S_t\{c};
- if c∉S_t: δ_t=0 and E_t=Y\S_t.

In either case |E_t|=2. Parallel edges retain individual time/source identities. Let G be this five-vertex edge multigraph, d_v its edge incidence degrees, and m_1=Σ_t δ_t. An unsigned history has a signed zero-Cell completion **if and only if** G has a subset F of its individual edges such that

(1) deg_F(v)=d_v/2 for every v∈Y; and  
(2) |F∩{t:δ_t=1}|=m_1/2.

If a target degree or m_1/2 is nonintegral, there is no completion. More strongly, the number N(S_1,...,S_m) of signed zero-Cell completions, with distinct temporal occurrences retained, is exactly

\[
\boxed{N(S_1,\ldots,S_m)
=[u^{m_1/2}\prod_{v\in Y}x_v^{d_v/2}]
 \prod_{t=1}^{m}\left(1+u^{\delta_t}\prod_{v\in E_t}x_v\right).}
\]

A coefficient with a nonintegral target exponent is defined here to be zero. Every coefficient is a nonnegative integer and no negative-weight BRC cancellation is used.

**Proof.** Let η_t=ε_t for δ_t=1 and η_t=−ε_t for δ_t=0. Write A=Σ_{δ=1}η, B=Σ_{δ=0}η, and V_v=Σ_{t:v∈E_t}η_t. The original signed c-coordinate is A, while each original signed coordinate v∈Y is V_v−B. If all six original coordinates vanish, A=0 and V_v=B for all five vertices. Summing these five identities gives 5B=Σ_v V_v=2(A+B)=2B, so B=0 and V_v=0. Conversely, A=0 and all V_v=0 imply 2(A+B)=Σ_v V_v=0, hence B=0 and every original coordinate vanishes. Thus zero Cell is equivalent to A=0 and V_v=0 for every v.

Select F={t:η_t=+1}. Then V_v=2deg_F(v)−d_v and A=2|F∩{δ=1}|−m_1. The equations are precisely (1),(2). Each F defines exactly one η sign assignment and hence exactly one ε sign assignment. Expanding the finite product selects each individual t independently, giving the coefficient identity. QED.

**Scope of data reduction:** HI1 supplies an exact coefficient for the declared final signed Cell readout at a fixed unsigned history. The polynomial factor is an observation/computation interface; it does **not** erase Port order, source/provenance identities, intervening Cells, Link, time or future-event permission. Unconditional observer-safe quotienting is not inferred.

## HI2. All-length two-layer Euler sufficiency on all six axes

Suppose the original word is incidence-even: for every i∈X, the number of supports containing i is even. Fix c and form the graph G above. Split its edges into two type layers G_1 (δ=1) and G_0 (δ=0). If **each vertex in G_1 has even degree** (equivalently each vertex in G_0 has even degree), then there exists a zero-Cell signing, for arbitrary m.

**Proof.** The original c-incidence count is |G_1|=m_1, hence m_1 is even. Total original incidences are 3m, so m is even and |G_0|=m−m_1 is even. For v∈Y, the full G degree has parity
d_G(v)≡d_{S}(v)+|G_0|≡0 (mod 2).
Thus vertex-degree parity in G_0 and G_1 is the same, so evenness of one layer implies the other.

Every nonempty connected component of an Eulerian loopless multigraph having an odd number of edges requires at least three distinct vertices: one-vertex components have no edges and a two-vertex even-degree component has an even number of parallel edges. On five vertices there can be at most one odd-edge component. Each G_j has an even total edge count, so it has no odd-edge component. Every nonempty component of each layer therefore has an even number of edges.

Choose an Euler circuit for every component and alternately mark its individual edges +,−,+,−,... . Since its length is even, the edge signs balance at every vertex, including the start/end pairing, and also have zero sum over that component. Perform this independently for G_0 and G_1. We obtain signed vertex-degree V_v=0 and marked total A=0. HI1 then converts these graph signs into a zero-Cell event signing. QED.

This is a new unbounded family even when all six native axes occur and there is neither a globally included axis nor a globally omitted axis. The additional layer-degree condition is a sufficient test; HI1 remains the full necessary-and-sufficient test.

## HI3. Exact finite Port-BRC census and nontrivial six-axis witness

C++17 verifier R762HI_CHECK.cpp enumerates **every** named closed walk based at Port {0,1} for m=2,4,6,8. It retains all eight distinct unsigned choices per Port update, including repeated support masks. For every incidence-even walk, it separately counts sign solutions by (a) original six-axis half-incidence subset enumeration and (b) HI1's five-vertex graph factor subset enumeration; both counts agree *on every walk*, not just in aggregate. It also counts whether at least one distinguished c meets HI2. The exact aggregates are:

| m | All closed unsigned Port walks | Incidence-even | Zero-Cell signed completions (with multiplicity) | Incidence-even walks certified by HI2 for at least one c | Incidence-even walks using all six axes | Those all-six walks certified by HI2 |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 8 | 8 | 16 | 8 | 0 | 0 |
| 4 | 288 | 168 | 624 | 168 | 0 | 0 |
| 6 | 17,536 | 4,960 | 34,688 | 4,864 | 816 | 720 |
| 8 | 1,118,720 | 177,536 | 2,413,424 | 162,368 | 73,824 | 58,656 |

At m=8 the 177,536 incidence-even histories split into 15,168 not certified by HI2, 14,208 certified for exactly one c, 98,400 for exactly two c, and 49,760 for all six c (no intermediate 3/4/5 count). The 15,168 not certified by the *sufficient* criterion are nonetheless signable, as checked directly and already established in R762HF. This is a genuine distinction between a sufficient shortcut and exact HI1, not a counterexample to parity sufficiency.

An all-six-axis closed Port walk with eight *distinct* three-support event types is:

P: 01→03→02→04→14→45→25→05→01.

S: 013, 023, 024, 014, 145, 245, 025, 015.

All six axis incidences are even; c=4 and c=5 satisfy HI2. The explicit ordered sign assignment (−,+,−,+,−,+,−,+) yields zero in all six original signed Cell coordinates. This example has neither a common included axis nor a common omitted axis; it belongs to the new unbounded sufficient class.

All finite checks use integer arithmetic, no floating-point approximations. They exhaust the indicated m≤8 closed-Port populations only. The independently proved arbitrary-m statements are HI1 and HI2. No all-length equivalence between incidence parity and signability for **all** closed Port histories is asserted; finding a longer lawful counterexample or proving that universal claim remains open.

## Continuation / unresolved dependency

1. Determine whether HI1's coloured half-degree factor is feasible for *every* incidence-even closed Port history of arbitrary even length. A useful route is the exact-b-matching condition (HI1) with the extra marked-edge cardinality; enumerate or classify configurations that fail this constraint while respecting all successive two-axis overlaps and Port closure.
2. Improve the sufficient-condition coverage and potentially derive a full Port-language decomposition, retaining the original signed BRC multiplicities.
3. Independently resolve primitive TRIADIC_CLOSURE_E force/Cell/Link/Port/time permissions and rotation covariance under frozen P000. The composite Port model is not that native event.
4. Maintain original task owner, contribution history and NOT_REVIEWED state. This note is a GitHub author-side scientific artifact, not a native Result, accepted review, or Foundation change.
