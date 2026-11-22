# EC49FXO — Sharp whole-activation symbol-observer law, every distance 4–20

Date: 2026-11-23 (Asia/Shanghai). Frozen scientific pin: BRC16943, unchanged.
Predecessor: EC49FXN at e743dce51861ebc61f9b5dca05fdeb5a10bc61ea (Draft PR #2989).
Status: AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.

## Exact frozen auxiliary observer

Physical activations are distinct sites t in Z/110. For relative phase d in D_k={0,...,k-1} with 5<=k<=55, support color i in Z/5 and missing column j in Z/11, let

\[
G_S(d,i,j)=\sum_{t\in S}{\bf1}\{(t\bmod5=i\ \land\ t\bmod11\ne j)\ \lor\ ((d-t)\bmod5=i\ \land\ (d-t)\bmod11\ne j)\}.
\]

An activation reads one ordered two-bit symbol: it differs when *either* channel differs. Define N_r(k) as the minimum cardinality of S such that G_S(d,i,j)>=r for every d,i,j. This is symbol distance, not the sum of two individual channel-bit distances. The native same-anchor Farey reachable set, signed branch, physical X6 embedding and P000 are not changed or claimed by this auxiliary statement.

## Exact theorem

For all integers 4<=r<=20, 5<=k<=55, write [x]_0^5=min(5,max(0,x)). Then

\[
\boxed{N_r(k)=5r+[k-55+5\lceil r/2\rceil]_0^5+[k-55+5(r-10)]_0^5.}
\]

For all r>=21 and 5<=k<=55, **no** fixed activation set satisfies the same distance requirement. For r<=10 the final clamp vanishes, exactly recovering EC49FXN on its previously proved scope. New content is the complete r=11,...,20 family and the second saturation threshold imposed by mod-11 column capacity.

For r=11: N=55 for k<=25, then N=56,...,60 at k=26,...,30, N=60 for 30<=k<=50, then N=61,...,65 at k=51,...,55. For r=20: N=100 at k=5, increases by two for each k=6,...,10, and remains 110 for k>=10.

## Proof: an exact five-color capacity reduction

(1) As k>=5, D_k contains every residue mod5. For each color i in Z/5 there is therefore a self-color phase d with d mod5=2i. Denote by m_i the selected sites with t mod5=i. Every other color contributes zero in that row, hence m_i>=r. Group these sites into residues x=t mod55; each has at most two physical lifts (x,x+55). A selected lift disappears from *both* channels in a self-color row if and only if j=x mod11 and d=2x mod55. Define A_i(k)={x in [0,54]:x mod5=i and 2x mod55>=k}, with s_i=|A_i(k)|. Call these safe residues; all other residues of color i are unsafe.

For an unsafe x, the permitted phase d=2x mod55 and j=x mod11 deletes exactly the selected n_x in {0,1,2} lifts at x. Since multiplication by 2 is invertible modulo 55, any self-color (d,j) deletes at most one such residue group. Thus all self-color rows for color i hold exactly when

\[
m_i-\max_{x\notin A_i(k)} n_x\ge r,\qquad m_i=\sum_{x\equiv i\bmod5}n_x,
\]

where an empty maximum is zero.

(2) There are 11 residues x per color: s safe and 11-s unsafe. If m=r, no unsafe lift can be present, giving capacity 2s; this is feasible exactly when 2s>=r. If m=r+1, unsafe occupancies may be at most one each; capacity is 2s+(11-s)=11+s. This is feasible precisely when 2s<r and 11+s>=r+1. Otherwise m>=r+2; since r<=20, selecting any r+2 physical lifts (maximum 22) achieves the self-color condition because no single unsafe residue holds more than two. Consequently the exact per-color optimum is

\[
f_r(s)=r+\mathbf1\{s<\lceil r/2\rceil\}+\mathbf1\{s<r-10\},
\qquad 4\le r\le20.
\]

(3) For d mod5 != 2i, the two channels use *distinct* colors i and d-i. For any fixed missing column, the left side loses at most two sites (one mod55 residue has two physical lifts); likewise the right. Thus G_S(d,i,j)>=m_i+m_{d-i}-4>=2r-4>=r for r>=4. Every independent per-color minimizing layout consequently satisfies all cross-color rows. The global optimum is exactly sum_i f_r(s_i).

(4) Multiplication by 2 permutes Z/55 and permutes colors modulo 5. Hence s_i is the number of z in [k,54] with z mod5=2i; these five numbers differ by at most 1 and sum to 55-k. For every threshold a in [0,10],

\[
\#\{i:s_i<a\}=[k-55+5a]_0^5.
\]

Substituting a=ceil(r/2) and a=r-10 into the sum of f_r establishes the boxed formula.

(5) For r>=21 and k>=5, s_i<=10. If no unsafe lift is selected, m_i<=2s_i<=20. If all unsafe occupancies are at most 1, m_i<=11+s_i<=21 yet losing 1 requires m_i>=22. If some unsafe occupancy equals 2, m_i<=22 yet losing 2 requires m_i>=23. Every case fails one self-color row. QED.

## Deterministic attaining activations

For each color i, list safe residues A_i and unsafe residues U_i in ascending order. If 2s_i>=r, select the first r lifts from the ordered safe pairs (x,x+55). Else if 11+s_i>=r+1, select the first r+1 sites from all safe pairs followed by one site x for each unsafe residue. Otherwise select the first r+2 sites from all safe and unsafe pairs. Unite the disjoint colors. This is an explicit exact cardinality N_r(k) witness for every case.

## Finite reproducibility

EC49FXO_SYMBOL_R4_R20_VERIFY.js is a dependency-free Node integer verifier of all 867 (r,k) constructions and exactly 1,430,550 (d,i,j) row inequalities. It separately enumerates all per-residue occupancies n_x in {0,1,2} by dynamic programming for 11 safe counts and 17 requested distances (187 local optima). The author executed this script locally: all assertions passed. Independent Python/NumPy vectorization of the same G_S formula covered all 867 layouts with no counterexample. The exhaustive finite checks support the analytic proof but do not constitute independent mathematical Review.

The accompanying JSON holds the compact full optimum-value table and actual validation summary. The fixed science pin and upstream P10/Farey–CRT support assumptions are inherited, not repinned. No new CLAIM, formal Result, independent review, native Farey dynamics claim, P000 amendment or ACTIVE worldview change is asserted.

## Next open problem

Derive and certify the *correlated* reachable triples (d,i,j) from actual same-anchor Farey trajectories, preserving anchor, branch and height provenance; compare the optimum under that restricted observer with the free-phase auxiliary N_r(k). Record any information-loss witness before attempting an X6 three-dimensional-slice transfer.
