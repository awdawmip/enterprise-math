# Stage436-B — Implicit exact future-class rank/unrank for native X6

2026-11-05. Author-side proof, exact integer check, UNREVIEWED / NOT_ADMITTED.
Parent Stage435-B: enterprise-math@2bf2a91420563ad2a970b42bb293db14ffb5e778.
Frozen scientific pins: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.

## Model
Within the original signed native X6 directions, set A=+E1, B=-E1, C=+E2. P is a length-m path with A at both ends and exactly k mutually nonadjacent internal B defects. Q starts at C^n. The current full observer records each six-component endpoint, each directed adjacency histogram J, lengths and absolute-position equality count K. For fixed m,k all admissible P form a single present observation fiber of size binom(m-k-1,k). P is fixed; Q may make p POP and r arbitrary X6 APPEND operations in any legal order. Assume n>=p+1, m>=n+r+2, p>=0, r>=1, 0<=k<=ceil((m-2)/2). The Stage435-B author-side theorem identifies full-future equivalence in this fiber with equality of defect-indicator bits S on I=[a,b]=[n-p+1,n+r].

Set w=p+r, L=m-2, ell=a-2, h=m-1-b, so L=ell+w+h. The aim is an exact implicit rank/unrank of *feasible* S, preserving their populations M(S), without enumerating every class.

## Theorem 436.1 — Support and exact population
Let S=(s1,...,sw) in {0,1}^w and j=sum S. It is feasible iff it has no adjacent 1's and
  j <= k <= j + floor((ell+1-s1)/2) + floor((h+1-sw)/2).
For feasible S, with binom(t,u)=0 when t<0, u<0 or u>t,
  M(S)= sum_{u=0}^{k-j} binom(ell-s1-u+1,u) * binom(h-sw-(k-j-u)+1,k-j-u).
For infeasible S, M(S)=0.

Proof. When s1=1 the last left-exterior position is forbidden; left free interval length is ell-s1. Likewise right free length is h-sw. On t consecutive sites the number of nonadjacent u-subsets is binom(t-u+1,u), by straightening ordered indices d_i -> d_i-(i-1), and every u from 0 to ceil(t/2) exists. Both exterior counts range independently through all integers in their capacity intervals, so the stated condition is necessary and sufficient. Their independent placements yield precisely the displayed integer convolution. If ell=0 and s1=1, effective interval length -1 has the unique empty selection and capacity zero; the formula retains this boundary case. QED.

## Theorem 436.2 — Deterministic support recursion
Let F(i,c,v,f) count feasible completions after i chosen window bits, c ones, last bit v, first bit f (initial f=-1). For i=w define
  F(w,c,v,f)=[c<=k<=c+floor((ell+1-f)/2)+floor((h+1-v)/2)].
For i<w, sum F(i+1,c+t,t, t if f=-1 else f) for t=0 and also t=1 if v=0, setting zero when c>k. Then q_F=F(0,0,0,-1) counts each distinct S exactly once.

Lexicographic rank with 0<1 adds the number of completions of each bypassed 0-branch when the actual bit is 1. Unrank chooses 0 iff its completion count exceeds the remaining rank, otherwise subtracts that count and chooses 1. The two maps are inverse bijections S <-> [0,q_F-1].

Proof. Future admissibility of a partially chosen word depends only on i,c,v,f: nonadjacency, total k and first/last boundary penalties. Each word has precisely one deterministic branch path; the exterior multiplicity M(S) is not inadvertently included in its class count. The 0- and 1-subtrees form consecutive disjoint lexicographic intervals of exactly the F counts; induction on remaining length proves rank/unrank and their inverse property. QED.

## Costs, BRC and retained information
Constructing the original observer and defect list from fully ordered native P,Q costs O(m+n) word operations. Extract S in O(w) indexed membership operations. F uses O(w(k+1)) states with <=2 transitions each, with O(w)-bit counts; preprocessing O(w^2 k) elementary bit time and O(w^2 k) bits space. Ranking/unranking each cost O(w) integer operations on O(w)-bit values, i.e. O(w^2) bit time. Minimal fixed-width class ID is ceil(log2(q_F)) bits when q_F>=1. The coder constructs no full exponential codebook.

An on-demand population query uses the above O(k)-term convolution. A Pascal table for lengths <=L and counts <=k requires O(mk) integer additions of O(m)-bit values; subsequent mass queries use O(k) products of O(m)-bit integers. Alternatively a length-L transfer DP computes one M(S) in O(mk) integer additions. Explicitly reporting q_F masses still takes Omega(q_F) output entries. All masses are nonnegative integers <=binom(m-k-1,k)<=2^(m-2); BRC branch multiplicity has not been replaced with Boolean support.

The class identifier is sufficient for the bounded *observer* under the Stage435-B future-equivalence premise; a particular original history needs an additional exterior-realization rank from 0..M(S)-1 for reconstruction. No theorem about both paths simultaneously mutable is asserted here.

## Exact check and next question
REPRO_STAGE436B.py exhaustively checks 428 admissible (m,n,p,r,k) test cases: 14,753 original defect histories, 2,355 feasible class words, exact M(S), q_F, lex ranking and unranking, and the mass of every possible binary word on each window. Tested k=2 and k=3, with edge/exterior reservoir constraints. Every integer comparison passed; see REPRO_STAGE436B_EXECUTED.json. For (m,n,p,r,k)=(13,6,2,2,2), 45 histories form 8 classes, with exact class masses (16,6,7,7,1,6,1,1), requiring a 3-bit class ID.

Next Stage437-B: identify a sufficient joint observer update state and cross-source K repair for both P and Q mutable under interleaved POP/APPEND. Test composability independently using exact native paths; preserve joint relation and provenance.
