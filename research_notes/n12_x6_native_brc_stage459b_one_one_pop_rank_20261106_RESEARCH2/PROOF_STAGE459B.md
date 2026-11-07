# Stage459-B: one-POP-each exact grouped BRC mass and lexicographic ranking

Date: 2026-11-06. Status: AUTHOR_SIDE_PROOF / EXACT_INTEGER_EXECUTED / FINITE_FULL_FUTURE_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Pins and mathematical scope

Continue Stage453-B theorem at 7b8227a64ecd9c88a5ac4877a1b5aa7bccb9f948 and Stage458-B at dc8183463b0ffdebe49d4f597f3da77210772b43. Frozen global science bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM science 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Read current behavioral norms separately.

Original ordered P,Q are binary A=+E1, B=-E1 native X6 paths, 2<=m<n; both start and end A; B defects are interior and pairwise nonadjacent. Fix kP,kQ B defects and d positional mismatches among positions 1..m. Each distinct source-ordered history pair has positive BRC mass 1. The full current observer O contains both lengths, both six-dimensional signed endpoint vectors, both full 12x12 directed adjacency histograms and K=m-d positional matches.

Allowed labeled futures: P and Q each at most one POP; P at most r>=0 APPEND; Q a prescribed finite APPEND budget. Each APPEND is one of all twelve native signed directions. Compare full O at every legal labeled operation prefix; source provenance stays distinct when counting mass.

## Theorem 459.1 (exact future-equivalence key)

Let t=min(n,m+r), S=sorted union of {m,m+1,...,t} and {n-1}, with any repeated index included once. Define

R459(P,Q)=(P_(m-1), (Q_i) for i in S).

On every fixed initial full-observer fiber, for ALL legal labeled operation prefixes, two histories have identical future observer trees if and only if their R459 keys coincide.

Proof: With a=b=1, the Stage453-B exact arbitrary-budget theorem has common stable prefix c=min(m-1,n-1)=m-1. Its exposed predecessor tails consist of P_(m-1) and Q_(n-1); the Q alignment/probe window is Q_m,...,Q_t; the P alignment window adds only fixed P_m=A. Their union is exactly R459. The Stage453 factorization reconstructs deleted original endpoint and directed-adjacency changes and all match changes from initial full O and this key. Conversely successive single POPs expose each unknown predecessor edge in J; P POP exposes the match bit at m and hence binary Q_m since P_m=A; P APPEND probes identify each further Q_i through the match bit by choosing a signed direction. The opposite Q APPEND cannot expose other original P letters (n>m); append-before-pop labels are explicitly known. Cases m=2 and n=m+1 reduce the key via fixed P_1=A and coalesced Q_(n-1)=Q_m. Thus the original full observer factors exactly through R459 under these futures. QED.

## Theorem 459.2 (grouped integer mass, support, rank/unrank)

For a given admissible key w, write u=P_(m-1), x=Q_m, z=Q_t, y=Q_(n-1), v=number of B among visible Q positions S. Define joint hidden-prefix transfer T_(u,x)(j,ell) over pairs (P_i,Q_i) for 1<=i<=m-1, retaining their ordered provenance. Starting from P_1=Q_1=A, track counts (number of P B, number of Q B, number of mismatches, last P, last Q). Require last P=u, last Q=ell, exactly kP P defects, j Q defects and d-[x=B] mismatches. Exclude consecutive B in either source, including edge (ell,x), and retain source multiplicity as exact nonnegative integer transition weights.

If n-1>t, there is a hidden Q-only gap of length g=n-t-2 between exposed boundaries Q_t=z and Q_(n-1)=y. Let U_g(z,y,h) be the exact number of binary B-isolated words of length g with h B and valid joins to both fixed neighbors. If n-1<=t, the suffix is completely visible, including all Q adjacency joins, so the hidden transfer is an indicator of h=0.

The exact class population is
M(w)=sum_(j,ell) T_(u,x)(j,ell)*U_g(z,y,kQ-j-v)   when n-1>t,
and M(w)=sum_(j,ell) T_(u,x)(j,ell)*[j+v=kQ] otherwise.

Proof: Each source-distinct original pair splits uniquely into its visible key, the length-(m-1) joint prefix, the fixed Q_m interface, and optionally the Q-only gap. The two retained end letters enforce every adjacency crossing a hidden/visible boundary. The transfers count every admissible completion once, with identical defect and mismatch counters. This proves the M formula without enumerating original histories.

For aggregate support, emit u and the visible Q letters by increasing index, forcing Q_n=A and rejecting exposed adjacent BB. Memoize the suffix using (visible-index, u, Q_m, Q_t, Q_(n-1), visible-B-count, previous visible letter). At terminal evaluate M(w) and return support 1 iff M(w)>0, together with population M(w). Sum the two integer components across children. Since M depends only on the retained summary, all completions merged by memoization have equal terminal mass. Hence root gives exactly q_F=sum_w[M(w)>0] and |F|=sum_w M(w) without listing keys; lexicographic rank/unrank descend support counts, skipping the A subtree before B.

Complexity: T needs O(m(kP+1)(kQ+1)(d+1)) exact integer operations. Binary-boundary gap tables and suffix DP use at most O(n(kQ+1)^2) integer operations conservatively. Thus total O(m(kP+1)(kQ+1)(d+1)+n(kQ+1)^2), with polynomial storage; integer masses have at most O(m+n) bits. Post-precomputation rank/unrank uses O(|S|) cached transitions. This is an exact integer-operation bound, not the bit-operation bound. QED.

## Executed results and scope

The full executable is STAGE459B.py (imports STAGE459B_CORE.py); run from this directory with Python 3 standard library. Executed output: STAGE459B_EXECUTED.json. 3,132 small deterministic parameter runs (1,137 nonempty), all 2,488 supported key masses and ranks checked against independently generated source words. Full six-axis observer future-tree oracle checked 60 configurations and 372 history pairs, with all twelve APPEND letters, 7,244 cached states. All assertions passed.

Exact larger results (m,n,kP,kQ,d,r) -> (classes,population):
(64,80,15,17,1,0) -> (6,5061384194832966)
(64,80,15,17,1,3) -> (24,5061384194832966)
(64,80,15,17,1,12) -> (523,5061384194832966)
(92,126,20,25,3,15) -> (10134,1121449082621221549433213976).

For each larger instance class-rank/unrank roundtrips at first, median and last were tested. The 523-class example coincides with the separately published Stage449-B result for the same budgets. These are results in this declared ordered-history observer, not physical heartbeat dynamics, and remain author-side pending independent review.

## Stage460-B

Investigate pP=pQ=2, initially rP=rQ=0, preserving BOTH predecessor tails, original match cross-window, exact boundary joins, and positive mass. Either produce grouped polynomial exact counting/ranking with independent full future oracle or give a minimal precise failed-join counterexample. Then extend signed future APPEND and test aggregate refinement.
