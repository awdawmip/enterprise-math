# PREFIX-497 — Exact five-color Parikh reduction for BRC–KMP/source fiber supports

Date: 2026-11-05 (Asia/Shanghai). Researcher: EM-DIRECT-3F61FC; source session MCP-59fcf553f9694d3ab0027c06578c1385.
Scientific input pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Current research predecessors: PREFIX-493 (BRC append closure), PREFIX-495 (base rank), PREFIX-496 (joint support and dense rank).
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. Independent author-side note; no formal Task CLAIM or Review.

## 1. Model and precise objective

Use Heartbeat World's native signed six-axis space, restricted to the X6 path subfamily in which the sixth signed axis is never used. The native alphabet is a,A,b,B,c,C,d,D,e,E. The output at length n consists of signed displacements y_i=u_i-v_i, cancellation numbers p_i=min(u_i,v_i), BRC observations V=p_b+2p_d+p_e and W=p_c+p_e, KMP state q in {0,1,2,3} for gate g in {aab,aba}, and first-source t in {N,B,C}. t=N until the first b/B or c/C, then retains B or C. Native direction append is an allowed operation. This work studies the complete *set* C_g(n,y,V,W) of controller states (q,t) realizable by a word giving one fixed BRC base observation. The output preserves the n,y,V,W fields; the internal reduction below computes only their controller-support set.

PREFIX-496 computed C_g via full ten-symbol reachable-state propagation. We replace that support-query step with five-color Parikh reachability and at most a two-dimensional cancellation lattice enumeration.

## 2. Five-color congruence theorem (all n)

Map each native direction to its action color:
  a -> a; b -> b; B -> B; c,C -> c; A,d,D,e,E -> x.

The KMP state machine for aab or aba and the first-source machine react identically to any two native letters assigned the same color. This follows directly from their transitions: lowercase a and b are the only letters occurring in either gate; uppercase B starts source B without advancing a gate prefix; c/C start source C without advancing a gate prefix; A,d,D,e,E neither starts a source nor advances a gate prefix. All listed non-gate letters reset the KMP suffix in the same way. The statement includes a full KMP match state because the deterministic suffix update uses g[:q]+letter.

Let h_g(q,t;w) be the final controller state. For each 5-tuple k=(k_a,k_b,k_B,k_c,k_x) of nonnegative counts, with |k|=n, define H_g(k) as the set of all h_g reached by permutations of a multiset of these five colors. Then for **every** fixed original ten-letter occupancy vector (u_a,v_a,...,u_e,v_e), the collection of all terminal (q,t) reachable by words with exactly that occupancy vector is *exactly* H_g(k), where

 k_a=u_a,
 k_b=u_b,
 k_B=v_b,
 k_c=u_c+v_c,
 k_x=v_a+u_d+v_d+u_e+v_e.

Proof: every raw word maps to a color word with the same automaton trajectory. Conversely any color word of that signature can be lifted to a raw word with the prescribed ten occupancies: distribute each color's occurrence positions arbitrarily among the original directions having that color, using each prescribed count exactly once. Because every raw letter within one color has the same controller transition, lifting preserves q and t. This proves equality, including k_i=0 and n=0.

## 3. Exact five-color automaton recurrence

Let the controller states range over the finitely reachable KMP/source pairs of g (11 for aab and 10 for aba). Set H_g(0,0,0,0,0)={(0,N)}. For every signature k,

 H_g(k+e_j) includes T_g(H_g(k),j), j in {a,b,B,c,x},

and define H_g(k) as the union over all last colors j with k_j>0 of T_g(H_g(k-e_j),j). This is an equality for all signatures by last-letter decomposition. Because every transition is deterministic, an exact 11-bit (aab) or 10-bit (aba) support mask implements H_g(k). A layer of length n has binomial(n+4,4) signatures. Computing all layers 0..N uses O(N^5) fixed-controller transitions and two consecutive length layers need O(N^4) mask entries; the O(N^4 log N) bit estimate allows storing the count-index keys. Retaining all layers for online variable lengths uses O(N^5 log N) bits.

Equivalently, introduce five commuting variables Z_a,Z_b,Z_B,Z_c,Z_x and a fixed controller transition matrix M_g(Z) of size at most 11. The exact weighted sum of all words is e_(0,N)^T (I-M_g(Z))^(-1) e_(q,t), as a formal power series. Every coefficient is a nonnegative integer. H_g(k) records which coefficients are positive. Thus the recurrence and the fixed-size rational transfer representation describe the same exact reachability set; in this use, Boolean support is retained rather than silently identifying it with multiplicity.

## 4. Exact BRC lattice projection

For a fixed proposed base observation x=(n,y,V,W), let m=(n-sum_i |y_i|)/2. If m is not a nonnegative integer, C_g(x)=empty. Otherwise every native occupancy realization has unique cancellations p_i>=0 with sum_i p_i=m and

 V=p_b+2p_d+p_e, W=p_c+p_e.

Choose d=p_d and e=p_e. The remaining variables are then determined:

 p_b=V-2d-e,
 p_c=W-e,
 p_a=m-V-W+d+e.

Define Lambda(x) as the set of integer (d,e)>=0 for which all p_a,p_b,p_c above are nonnegative. These formulas prove an exact bijection between Lambda(x) and all cancellation vectors yielding x.

For (d,e) in Lambda(x), put
 k_a = p_a + max(y_a,0),
 k_b = p_b + max(y_b,0),
 k_B = p_b + max(-y_b,0),
 k_c = 2 p_c + |y_c|,
 k_x = p_a + max(-y_a,0) + 2(d+e) + |y_d| + |y_e|.

Then |k|=n and the complete all-length, all-base support formula is

 **C_g(x) = UNION_{(d,e) in Lambda(x)} H_g(k(d,e)).**

Proof: the five-color theorem applies to every raw occupancy vector corresponding to a cancellation vector. The lattice equations enumerate all and only those vectors. Union is exact for each q,t. Therefore k_g(x)=|C_g(x)| is also computed exactly by this formula. Empty, boundary and interior fibers are covered without special-case assumptions.

Enumeration of Lambda(x) takes at most O(n^2) integer pairs (0<=e<=W<=n/2, 0<=d<=V/2<=n/2). With a precomputed H_g table at length n, a single C_g(x) or k_g(x) query needs O(n^2) constant-word bitmask unions, O(1) auxiliary query storage, and O(n^4) shared length-n masks. This replaces an explicit table of every n-length joint state for *sparse support queries*. It is not yet an O(n^2) global dense-rank builder: ranking all base fibers needs additional prefix counting of k_g(x).

## 5. Executed exact verification

Attached program prefix497_five_color_support_certificate.py ran under Python 3 with exact integer/set arithmetic and returned ALL_CHECKS_PASS. For both gates and each n=0..9 it:
  (i) constructed all ten-direction joint states by the original native append recurrence;
  (ii) computed every reachable base fiber's full control support from independent five-color count DP plus Lambda(x);
  (iii) compared the two supports exactly for every base fiber;
  (iv) checked the five-color signature count binomial(n+4,4).
It additionally independently enumerated all 11,111 native ordered words through n=4 for each gate and checked the raw occupancy, q and t observer map against the original recurrence.

At n=9: 715 five-color signatures, versus 48,620 ten-letter occupancy signatures and 43,054 distinct BRC base fibers. Exact joint state counts are 127,403 for aab and 127,298 for aba. Every one of the 43,054 base support sets matched its independent direct-state result for each gate. At n=8: 495 five-color signatures and 22,275 BRC base fibers; the direct joint totals are 60,590 and 60,550. The logged status is ALL_CHECKS_PASS.

The all-n theorems follow from the two lifting/bijection arguments, independent of finite test length. Program results check the implementation and finite range only.

## 6. Reuse, scope and next question

BRC reuse: PREFIX-493's exact append update for n,y,V,W, PREFIX-495's base rank and PREFIX-496's definition of controller support were used without changing the native X6 substrate or task scientific pin. The five-color quotient is certified for the KMP+first-source control observer; native y,V,W and future append remain separately retained, and raw path provenance/time are outside this observer contract.

The current result provides a compact support-query interface and the cardinality k_g(x) required for PREFIX-496's dense rank. Next: compress the prefix-sum P_g(n,r)=sum_{j<r} k_g(x_j) along the y,W,V base rank order, combining the five-color support predicate with block/generating-function counts to avoid an O(n^7) materialized fiber table. Test whether interior and boundary regions admit short piecewise-Presburger formulas; compare preprocessing, rank/unrank and append cost against the exact n<=9 reference states.

Sources: project P000, ACTIVE Heartbeat World and joint-observer preservation contracts; docs/PORTABLE_RESEARCH_PROTOCOL.md; global MATH_RESEARCH_POLICY; prior PREFIX-493,495,496 notes. All current control-policy reads are separate from the immutable scientific input pin.
