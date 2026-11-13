# R36 — Batched last-survivor ranks for exact multi-arc extinction

Date 2026-11-10. Mathematical status: author derivation with exact computation; independent review pending.

Scientific pin: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Predecessor R35: Draft PR #1946, immutable commit b6543a34e1de8db9dd56468cfe52c08b72c68dc2. This is an auxiliary irrational circle-rotation observer, not an X6 physical-dynamics assertion. P000 and the typed provenance-preservation constraints are unchanged.

## Exact theorem

Fix an irrational angle 0<theta<1 and historical indices H={0,...,m-1}. Let I_k be their m oriented, left-closed rotation-phase arcs. Fix one Farey stage n0<=n<=n1<=i+j with neighboring fractions a/i<theta<c/j and ic-ja=1. The exact long-gap sources are

    W(n)=[n-i,j) ∩ Z.

The source-owned population in arc I_k is C_k(n)=#{t in W(n):owner(t)=k}, and F(n)=#{k:C_k(n)=0}.

For each arc k form its **owner-labelled final survivor**:

    tau_k=max{t in [n0-i,j) ∩ Z : owner(t)=k},

using tau_k=-infinity if the set is empty. Let T be the sorted multiset of finite tau_k values, and h=|T|. For every n in the fixed Farey stage:

    C_k(n)>0 iff tau_k>=n-i,
    F(n)=m-h+rank_T(n-i),

where rank_T(x)=#{t in T:t<x}.

**Proof.** Increasing n removes an initial segment of the index interval [n0-i,j), leaving precisely those sources with index t>=n-i. An arc retains a source iff its largest original source index has not been removed. Taking complements and counting the finite maxima yields the formula, including initially vacant arcs and the zero-source end of a stage. The labelled tau vector retains provenance; the sorted T is an exact quotient only for the declared scalar extinction observer. QED.

R35 established that F(n+1)-F(n) belongs to {0,1} and, within one Farey stage, the exact scalar risk difference is

    R_b-R_a=[F(b)-F(a)]*min(i*theta-a,c-j*theta).

Given two queried endpoints a<b, if F(b)-F(a)=0, every intermediate increment is zero; if F(b)-F(a)=b-a, every intermediate increment is min(u,v); otherwise bisect the interval and repeat. Adjacent equal affine increments are merged.

## Two exact ways to batch all historical arcs

**Sparse window.** Let N=i+j-n0. Sort the m historical phases once. Scan the N source indices in ascending order, locate each historical arc by exact circular predecessor binary search, and overwrite its tau. The m owner-labelled maxima are obtained in O(m log m+N log m) comparisons; further F(n) requests require only a binary rank query O(log m).

**Dense window.** For each historical arc, first test whether its initial source range contains any member using the exact Euclidean Floor Sum owner count from R29. If nonempty, binary-search the monotone predicate #{t in [x,j):owner(t)=k}>0 for its final index tau_k. This requires O(m log(N+1)) exact Floor Sum calls across the whole stage (plus sorting). Later F(n) requests are O(log m) comparisons, without scanning N indices. The count oracle uses a logarithmic number of Euclidean steps in its integer arguments; total bit costs depend on the rational-enclosure and index bit lengths.

The bisection emits maximal equal-increment intervals using O(K log(W+1)) rank queries for K output runs across a stage of W updates. Stage discovery, preprocessing, exact boundary-risk queries, integer bit costs and output bytes are counted separately. Phase ordering over each finite parameter enclosure is certified by rational endpoint floor stability for all relevant index differences, preserving owner classifications.

## Executed exact checks

The locally executed standalone R36 program rebuilt all intermediate phase partitions and compared the last-source histogram to a separate Floor Sum source-count oracle at every stage position. Five families were tested:

| angle / history | m | horizon n | Farey stages | F queries | independent complete phases | independent arc-count checks |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Frozen S23/AV | 128 | 389 | 3 | 19 | 261 | 33,536 |
| sqrt(2)-1 | 16 | 96 | 5 | 23 | 80 | 1,296 |
| sqrt(3)-1 | 32 | 180 | 5 | 34 | 148 | 4,768 |
| 1/3+sqrt(2)/10^7 | 21 | 126 | 36 | 71 | 105 | 2,226 |
| sqrt(2)-1 extended | 16 | 320 | 8 | 50 | 304 | 4,880 |

All comparisons passed using integer/Fraction arithmetic and certified square-root enclosures; the extended sqrt(2) family exercised both sparse-scan and dense rank/select paths.

For S23 the three starting source windows contained 36,60,163 indices (259 total). The 19 F queries were serviced by histogram rank, replacing 2,432 per-arc owner counts in R35's extinction subroutine. Exact whole-risk boundary validation retains 2,304 independent source-count calls. The four exact prefix increment blocks are:

    129..164 : 16-61*theta
    165..292 : 164*theta-43
    293..328 : 0
    329..389 : 164*theta-43

Thus R_389=-7551+28800*theta. A separate integrated regression reuses the immutable R33/R32 calculation interfaces and produces the unchanged 298 affine runs up to n=10^12+128; SHA256 2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6, terminal risk -4017401528447+15321634290944*theta.

The companion compact verifier is executable against the exact R34 predecessor VERIFY_R34_PREFIX.py from commit f326670b828dd19bd66a44f0564e9e7932c683cd, path research_notes/brc_s23_av_rank_select_prefix_20261110_r34/VERIFY_R34_PREFIX.py. The full standalone R36 verifier, owner-labelled certificate, five-family evidence and integration regression are also preserved in the downloadable R36 research bundle from this research turn.

Next: multi-target Ostrowski/three-gap rank-select to improve dense-stage preprocessing beyond separate per-arc binary searches, with a full bit-complexity account and further high-m independent tests. No shared Task CLAIM or independent mathematical review is asserted.