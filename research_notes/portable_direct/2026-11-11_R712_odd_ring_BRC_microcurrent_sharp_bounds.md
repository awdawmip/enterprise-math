# R712 — Sharp area and peak bounds for transient BRC current on full odd rings

Date: 2026-11-11 (Asia/Shanghai). Status: independently derived author-side theorem in the explicit R709b/R710s/R711 frozen-gate candidate model; finite certificate executed; independent mathematical review pending.
Mother task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS` (`PO-X6-UPPER-STRUCTURE-20260906`).
Frozen scientific source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` (P000 V5 and X6 foundation). Exact historical predecessors: R709b@15057fffe4aef6610e8686b20495771cd071f8ef, R710s@e78df51f52957e9402a38083056559a9f24742a1, R711/R711b@8fe4c9ce43183e9394d1e4047585ba51c336c483. BRC resolution: COMPOSE_APPLIED — retains each source-labelled positive transfer occurrence; signed current is a derived physical-edge observer only.

## Defined carrier, observation and legal future operations

Take an **odd** labelled cycle of `m >= 5` X6 Cells with the old adjacent active-triad field and inventory gate frozen for one candidate macrostep. Assume **all m physical edges fire**. For every edge `i` execute exactly one positive source-labelled `+` transfer and one positive source-labelled `-` transfer (opposite direction) in **distinct** phases. The single-incident-transfer-per-Cell-per-phase capacity of R711 applies; completed macro events keep typed positive counters and do not combine or cancel their positive BRC weights. A phase may act on any matching of physical edges. R711 proved five phases are minimum for odd full cycles of length at least five.

Let `p_i<q_i` be the phase labels in `{1,2,3,4,5}` carrying edge i's two transfers, with either type assigned to the earlier event. The derived signed physical current after phase t is `j_i(t)=(# plus completed)-(# minus completed)`. It is 0 outside `p_i<=t<q_i` and +/-1 inside. Thus for t=1..4,

    D_t = sum_i |j_i(t)| = #{i: p_i <= t < q_i},
    A = D_1+D_2+D_3+D_4 = sum_i(q_i-p_i).

Different phase pairs on adjacent cycle edges must be **disjoint** because a common Cell has capacity one. This defines the observer / allowed schedule language precisely; BRC signed current is never used as a replacement for positive occurrence provenance.

## Theorem — simultaneous sharp area and peak

For every odd integer `m>=5`, among all **optimal five-phase schedules** of the full typed-transfer cycle,

    min A = m+3;
    min max(D_1,D_2,D_3,D_4) = ceil((m+3)/4).

Both minima are attained simultaneously by the same explicit family. Since every edge requires at least one phase gap, the extra transient area in an odd ring is exactly **three** above the `m` edge baseline; this is a parity/topology penalty in the explicitly specified schedule graph.

### Lower bound via an exact ten-state graph

Associate each physical edge i with the unordered phase pair `v_i={p_i,q_i}` (two distinct elements of {1,2,3,4,5}). Adjacent physical edges require disjoint pairs. The ten two-element subsets of a five-element set, connected when disjoint, form the **Petersen graph**. Hence `v_0,...,v_(m-1)` is a closed walk of odd length in this graph.

Give a vertex `v={p<q}` nonnegative integer weight `w(v)=q-p-1`. Then

    A-m = sum_i w(v_i).

Every odd closed walk decomposes into closed subwalks, one of which is an odd simple cycle; nonnegative weights imply that the total weight is at least the minimum total weight of an odd simple cycle. The Petersen graph has exactly 12 undirected simple 5-cycles, no 3- or 7-cycles, and 20 undirected simple 9-cycles. The complete finite 10-vertex adjacency DFS in `R712_ODD_RING_VERIFY.py` enumerates all these simple cycles with rotation/reversal deduplication, and obtains minimum total weight 3 for a 5-cycle and 7 for a 9-cycle. This finite graph result supplies a finite exhaustive lemma, valid independently of the input ring length. Therefore `A-m>=3`. Also `4 max_t D_t >= A`, so `max_t D_t >= ceil((m+3)/4)`.

For an additional hand check on the 9-cycle bound, weights over all ten vertices sum to 10; a simple 9-cycle visits nine distinct vertices, so its weight is at least 10-3=7. For 5-cycles the exhaustive small graph checker enumerates precisely twelve and finds excess-weight distribution 3,5,7 with multiplicity four each. The finite checker source is part of the proof certificate rather than a finite-m extrapolation.

### Explicit simultaneous attainment

Write `m=2(a+b)+1`, where

    a=floor((m-1)/4),  b=(m-1)/2-a,

so a,b are positive and differ by at most one. Assign edge phase pairs in cyclic order by

    (12,34)^a, 15, (23,45)^b.

Adjacent pair sets are disjoint, including wrap-around `45|12`; this is a valid phase-matching decomposition. Give the first occurrence on each edge its + type and the second its - type. Every type is posted once, stocks remain nonnegative under the R711 frozen old gate, and the completed macro ledger and V36 candidate state commit are unchanged. The exact transient profile is

    (D_1,D_2,D_3,D_4,D_5)=(a+1,b+1,a+1,b+1,0).

Consequently

    A=2(a+b)+4=m+3,
    peak=1+max(a,b)=ceil((m+3)/4).

This construction is a **single uniform formula for all odd m>=5**. For m=5 use pairs [12,34,15,23,45], giving residual profile [2,2,2,2,0]; for m=7 choose [12,34,15,23,45,23,45], giving [2,3,2,3,0].

## Exact verification / reproducibility

`R712_ODD_RING_VERIFY.py` contains (1) exhaustive simple-odd-cycle enumeration of the 10-vertex Petersen graph, (2) construction checks for all 49 odd sizes m=5,7,...,101, including every phase's Cell-disjointness and the four exact current values, and (3) independent base-3-state dynamic programming over **all possible five-phase matchings** for m=5,7,9,11,13, minimizing lexicographically (peak,area). All asserted formulae passed; `R712_ODD_RING_RESULTS.json` records the exact certificate. The arbitrary-size claim follows the graph lemma and construction, not finite m coverage.

The pending scientific question is to reconcile this candidate frozen-old-gate five-phase schedule with the actually permitted X6 native Link/Port timing and joint trivalent updates without introducing unstated prepare/commit authority. Another useful next unit is to classify the first-phase signed-current information fiber under simultaneous peak/area minimizers, preserving raw source-labelled event histories.

## Status and evidence classification

The theorem is an exact combinatorial result under the defined capacity/observer/stock-gate hypotheses. It refines the R711b even-ring transient theorem by supplying **odd-ring sharp metrics**. It is author-side evidence, not a native Result, accepted Foundation theorem, heartbeat physical-time assertion, or independent review. The physical-edge signed observer is derived from typed occurrence counts; signed-zero macro flux does not erase positive BRC sources. No PI, trigonometric, complex amplitude, continuous simulation, or non-BRC native residual attribution is used.