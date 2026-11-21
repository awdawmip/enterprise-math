# PREFIX-991 — Exact composable terminal-port BRC histogram signature

Date: 2026-11-22 (Asia/Shanghai)
Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_CHECKED / NOT_REVIEWED.
Scope: independent portable continuation of PREFIX-990; auxiliary signed-source bit-flip observer, not native X6 dynamics. Frozen scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json (P000 V5).
Historical antecedents: PREFIX-989 / PREFIX-990 under research_notes/portable_direct/. Canonical positive histogram semantics: WBRC-T36/T37 in definitions/ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md; labeled port contextual boundary: WBRC-T31 in definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md.

## Exact problem

Let S be a finite labeled directed multigraph, with named edges a:s→t and a source port j(a)∈J. Availability and destination depend only on old state s, not the incoming history h. Work in the exact positive rational BRC histogram semiring H=N[Q_{>0}^×], where [r][s]=[rs] and addition recoalesces exact equal weights with multiplicity. For strictly positive rational u_h,v_a, choose the one-step historical weight g(h,a)=u_h v_a and update h to j(a) after traversing a.

This is an explicitly declared WBRC-T36-compatible historical feedback test law, not a claimed native Cell/Link/Port feedback law.

## Theorem 991.1 — terminal-port interface and composability

Define H-valued old-state matrices
 T(s,t)=Σ_(a:s→t) [u_(j(a)) v_a]
and
 D_j(s,t)=Σ_(a:s→t, j(a)=j) [v_a].
Let K_n^(h,j)(s,t) be the complete positive exact-weight histogram of n-edge named paths starting with old state s and previous port h, ending with old state t and last selected port j, with chronological historical feedback weights. For all n≥1:

  K_n^(h,j)(s,t) = [u_h] (T^(n-1) D_j)(s,t).          (991.1)

For zero length use K_0((s,h),(t,j))=δ_(s,t)δ_(h,j)[1]. For all n,m≥0:

  K_(n+m)^(h,k)(s,t)=Σ_(y∈S) Σ_(j∈J∪{0}) K_n^(h,j)(s,y) K_m^(j,k)(y,t). (991.2)

Proof: fix a valid path a_1...a_n with ports j_1,...,j_n. Its exact chronological weight
 (u_h v_(a_1))(u_(j_1) v_(a_2)) ... (u_(j_(n-1)) v_(a_n))
equals
 u_h (Π_(r=1)^(n-1) u_(j_r) v_(a_r)) v_(a_n).
The product of the first n-1 revised factors is exactly the T weight, while D_j contributes the terminal factor and selects the final port. Distinct named paths are summed as separate H branches; recoalescence preserves multiplicity, giving (991.1). Every path of length n+m admits a unique split at (y,j) after n edges, and its positive rational weight is the product of the corresponding two chronological weights. Distribution in H proves (991.2), including the empty path. Consequently, finite future positive-histogram operations connected only through the declared old-state/last-port interface preserve the exact histogram, counts, masses, dominant degeneracies and integer moments. QED.

The old-state power T has size |S|×|S|; the full K is a boundary-indexed signature, not a blanket reduction of all output-port data. It is exact for positive mass/histogram contexts with no direct hidden-path access. Named internal source identity, signed amplitude cancellation, X6 spatial identity and provenance-demanding future operations are not compressed by this assertion. Preserve the original named edges.

## Theorem 991.2 — least necessary last-port memory for future histograms

Fix one old state t and compare prior ports j,k under the observer "all future nonempty-length positive exact-weight histograms from t" (without an explicit last-port-identity readout). Their future histograms coincide for every length if and only if

  outdegree(t)=0 OR u_j=u_k.                         (991.3)

If there is no outgoing edge, every nonempty histogram is zero. If u_j=u_k, every future named path receives identical chronological weight. Conversely, when an outgoing edge exists, the length-one histograms for ports j and k are two nonempty finite multisets obtained from the same one by scaling all weights by u_j and u_k respectively. Equality of their largest rational weights implies u_j=u_k. QED.

Hence, for this exact future-histogram observer, a nonterminal state t needs precisely the distinct u_j values among its reachable incoming histories, while terminal states may merge histories. If last-port label itself or named provenance is observed, retain the full j interface of Theorem 991.1. This is an observer/horizon-specific certificate, not a universal erasure of joint directions.

## Concrete obstruction and exact verification

In the frozen auxiliary named-source model, sources a=(q,i,j,s) satisfy c_q=2^i-s·2^j with s=±1; a is legal when bit j of odd input x equals (1-s)/2 and flips bit j. At width six, w=(6,24,6,-3), initial (q,x)=(0,1), two different valid seven-step source sequences end at the same old state (3,3) but with last ports 1 and 2. A common next source (3,0,2,+1) has next-step weight 2 versus 3 if u_1=2,u_2=3 and v_a=1, or 4 versus 6 if the source-sign factor is v_a=2 for s=+1 and 3 for s=-1. The old-state-only quotient cannot preserve this future positive histogram.

A self-contained Python checker reconstructs the two frozen source words (6,24,6,-3) and (6,24,8,40), takes all odd phase-zero active-bit inputs, and tests two integer BRC laws: u_0=1,u_1=2,u_2=3,u_3=5,u_4=7,u_5=11,u_6=13; v_a=1 or v_a=2/3 according to source sign. For both words and both laws, the full endpoint-state/last-port/weight/multiplicity table from direct history-augmented enumeration agrees exactly with T^(n-1)D_j at every n=0,...,12. Gluing splits (1,1), (2,3) and (3,4) also match direct enumeration for both words/laws. Python Fraction and integer counters provide exact rational arithmetic.

For (6,24,6,-3), 64 reachable old states: n=8 has 96 paths, mass 276480 with v=1 and mass 393465600 with sign-aware v. For (6,24,8,40), 120 reachable old states: n=8 has 84 paths, mass 1901600 with v=1 and mass 4277577600 with sign-aware v. Exact certificate and explicit witness sources accompany the checker.

Theorems hold for all finite graphs with the specified separable positive feedback. This work reuses canonical WBRC-T36/T37 operations and refines PREFIX-990 from fixed-length aggregate mass to a fully composable endpoint observer. Independent mathematical review is pending. The mother problem B_fix,odd(32)∈{19,20} remains open.

## Next scientific question

Extract one actual Source-typed BRC/X6 Cell/Link/Port feedback law, including the reachable prior-port/current-source pairs, and test the PREFIX-990 bipartite cycle-factorization criterion against it. If the law is nonseparable, obtain the smallest context-safe endpoint memory with an exact witness; preserve native X6 state, ordered source history, composite/joint observers and separately typed time where required. No formal shared Task CLAIM, Result, or Review has been made.
