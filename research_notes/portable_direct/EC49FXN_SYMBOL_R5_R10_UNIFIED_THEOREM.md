# EC49FXN — A unified sharp whole-activation symbol-distance law (r=4,...,10)

**Date:** 2026-11-23 (Asia/Shanghai). **Frozen scientific input:** BRC16943, unchanged. **Status:** AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.

**Predecessor:** EC49FXL–FXM, immutable 7808b4d9b61e19f7c83fcd5bf33d8c46fd94cb54, Draft PR #2986. In particular r=4 was already solved there; the new contribution is a uniform r=4,...,10 theorem, the exact r=5 and r=6 classification including k=1,...,4, and additional r=7,...,10 results for k>=5. The old results are reused at their original scope.

## Precisely frozen auxiliary model

Physical positions are t in Z/110. At one activated t the left and right Boolean readings form **one** ordered two-channel symbol, so corruption of an entire activation counts as one symbol error. Relative phase d is restricted to D_k={0,...,k-1}, with 1<=k<=55; i in Z/5 is the CRT support color, and j in Z/11 is the missing column. For a fixed set S of distinct activated sites define

G_S(d,i,j) = sum_{t in S} 1[ (t mod 5=i AND t mod 11 != j) OR ((d-t) mod 5=i AND (d-t) mod 11 != j) ].

Let N_r(k) be the minimum |S| with G_S(d,i,j)>=r for every d in D_k, i in Z/5 and j in Z/11. No assumptions on probability distributions are used. In particular, this is the *activation-symbol* distance, not the sum of separate channel-bit distances.

## Theorem A — universal sharp r=4,...,10 formula when 5<=k<=55

For **every integer 4<=r<=10** and **every integer 5<=k<=55**, put h=ceil(r/2) and [x]_0^5=min(5,max(0,x)). Then

\[
\boxed{N_r(k)=5r+[\,k-55+5h\,]_0^5.}
\]

Equivalently, the optimum equals 5r when k<=55-5h; increases by one at each k=56-5h,...,60-5h; and equals 5(r+1) for k>=60-5h.

As examples: r=4 has its previously proved jumps at k=46,...,50; r=5 and r=6 jump at k=41,...,45; r=7 and r=8 at k=36,...,40; and r=9 and r=10 at k=31,...,35.

### Proof of the lower bound

Write m_i=|{t in S:t mod5=i}|. Because k>=5, D_k contains phases d=0,1,2,3,4, hence for every i there is an allowed d with d mod5=2i. In the resulting self-color row, only positions t mod5=i can contribute, so m_i>=r.

If m_i=r, **each** of its selected sites t must have (2t mod55)>=k. To see why, otherwise d=(2t mod55) lies in D_k, matches the self-color condition, and j=t mod11 deletes the entire contribution of t (both channels). Then G_S(d,i,j)<=m_i-1<r, a contradiction.

Define A_i(k)={x in {0,...,54}: x mod5=i, (2x mod55)>=k}. Every x has exactly two physical lifts x and x+55, so m_i=r requires |A_i(k)|>=h=ceil(r/2). Consequently each color for which |A_i(k)|<h must have m_i>=r+1.

Multiplication by 2 permutes Z/55 and maps color i to 2i mod5. Therefore |A_i(k)| counts those z in {k,...,54} with z mod5=2i. Put 55-k=5q+s with 0<=s<=4. Exactly s colors have q+1 safe residues, and 5-s have q safe residues. The number H of colors with fewer than h safe residues is

H=0 if k<=55-5h; H=k-(55-5h) when 55-5h<k<60-5h; and H=5 if k>=60-5h.

Thus |S|=sum_i m_i >=5r+H=5r+[k-55+5h]_0^5.

### Explicit attaining construction, valid for every specified r and k

For each color i independently:

* If |A_i(k)|>=h, choose h different x in A_i(k) (e.g. the least h). From their two lifts x,x+55 select exactly r distinct physical sites, using both lifts of as many selected residues as needed. Each of the r sites is safe.
* If |A_i(k)|<h, choose the r+1 positions i,i+5,...,i+5r. Because r+1<=11, these have distinct residues modulo11.

Different colors are disjoint. Total size is 5r+H.

To check G>=r, take any allowed d,i,j. If the row is self-color (d mod5=2i), each light/color-safe site survives: losing it in both channels would imply d≡2t (mod55), forbidden by safety. A heavy color has r+1 distinct mod11 columns, of which at most one can disappear in a self-color row; at least r remain.

Otherwise the two channels are supported on distinct colors i and d-i (mod5). In one channel the missing column can eliminate at most two sites of a light color (the two lifts of one residue), or one site of a heavy color. Hence two light colors contribute at least 2r-4 >=r (this is **exactly** where r>=4 is used); a light/heavy pair contributes >=2r-2>=r; and two heavy colors contribute >=2r>=r. The construction therefore satisfies every required row and meets the lower bound. QED.

**Boundary of the result:** The uniform proof uses (i) r>=4 for light/light pairs and (ii) r<=10 for r+1 distinct mod11 columns in every heavy color. The proof makes no claim for r<=3 or r>=11.

## Theorem B — complete r=5 and r=6 functions on all 55 intervals

For r in {5,6}, Theorem A combines with the following sharp k<5 values:

\[
\boxed{N_r(k)=
\begin{cases}
3r+2, & k=1,2,\\
4r+1, & k=3,4,\\
5r+[k-55+5\lceil r/2\rceil]_0^5, & 5\le k\le55.
\end{cases}}
\]

Thus N_5 is 17 for k=1,2; 21 for k=3,4; 25 for k=5,...,40; k-15 for k=41,...,44; 30 for k=45,...,55. Similarly N_6 is 20,25,30,k-10,35 on the corresponding ranges.

### Lower bound for the small intervals

For d=0 the self-color row gives m_0>=r. The two disjoint pairs of different colors {1,4} and {2,3} each need m_i+m_h>=r+1: at least one site must disappear for some missing column j, hence pair occupancy r is inadequate. The sum gives |S|>=r+2(r+1)=3r+2 for k=1,2.

For k=3 or 4, the allowed phases d=0,1,2 give self-color constraints m_0,m_3,m_1>=r; d=1 gives the distinct-color pair {2,4}, with m_2+m_4>=r+1. Therefore |S|>=3r+(r+1)=4r+1.

### Exact upper-bound witnesses for k=2 and 4

Each witness also serves all smaller k in its range because the constraints are nested.

* r=5, k=2, 17 sites: {59,65,68,69,70,71,73,74,82,85,89,90,93,98,99,105,108}.
* r=5, k=4, 21 sites: {58,60,61,69,70,73,75,76,79,81,85,86,88,89,90,93,102,103,104,106,109}.
* r=6, k=2, 20 sites: {56,58,59,63,64,65,68,69,78,80,84,85,89,90,92,93,94,100,105,108}.
* r=6, k=4, 25 sites: {58,59,60,63,64,65,67,69,70,73,76,78,80,81,85,86,88,91,94,95,96,103,104,106,109}.

The accompanying integer script exhausts all d,i,j rows for these four witnesses, showing minimum distances respectively 5,5,6,6. These finite exact witnesses, together with the analytic lower bound, establish sharpness. QED.

## Reproducibility and source restrictions

Use EC49FXN_SYMBOL_R5_R10_VERIFY.js with Node.js; no dependencies and only integer modular arithmetic. The program checks all r=4,...,10 and k=5,...,55 (7*55*sum_{k=5}^{55}k=589,050 row inequalities) plus r=5,6 and k=1,...,4 (2*55*sum_{k=1}^{4}k=1,100 inequalities). **Total 590,150** exact rows; all pass, zero failed assertions. Each site's physical position and the observed minimum distance for every (r,k) are deterministically reconstructible from the algorithm; the compressed output reports all optimum values, scopes and sample witnesses.

An independent local SciPy/HiGHS binary MILP check for r=5 and 6, k=1,...,5, produced the same optima (17,17,21,21,25 and 20,20,25,25,30). The standalone proof does not use solver optimality. Previous r=4 values agree with EC49FXM's exact theorem.

This is an **auxiliary** Farey–CRT observer theorem under frozen BRC16943/P10/one-missing-column assumptions. Original same-anchor Farey trajectory, signed branch and height provenance, the actual reachable phase relation, P000-native X6 space and three-dimensional-slice transfer remain separate questions. Do not promote this to an independently reviewed Result or rewrite protected foundations.

**Next discriminating questions:** (1) classify r>=11, where heavy colors cannot use r+1 pairwise-distinct mod11 columns; (2) derive the reachable correlated d,i,j set from genuine same-anchor Farey trajectories, then recompute the optimum under those actual correlations; (3) distinguish whole-activation symbol errors from independent channel-bit errors.