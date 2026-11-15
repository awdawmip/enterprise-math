# R749SQD — Exact earliest deficit threshold for all nonzero-V Walsh boundary layers

Date: 2026-11-15. Status: **AUTHOR_EXACT_NOT_REVIEWED**. Model: frozen auxiliary signed 16-atom Walsh source with (t,s)=(1/10,1/2), scientific pin awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Previous R749SQB (PR #2487) and R749SQC (PR #2488, commit c6d4a3b43417eff77e330129c46b76c95637dbab). This improves R749SQC's sufficient D threshold to the **exact earliest threshold**; the prior bound remains valid.

## Definition

As in R749SQC, let D≥2, V=J∈Z, n=2D−r, r≥1, t=r−J. The source alphabet is F (25 forced types) plus one optional type, either (0,0,0) in A0 or (−1,0,0) in A1. The nonzero-slack 23-letter multiset alphabet L, slack s=2d−1−v>0, and weight B_j=h_j+d−v define the universal finite bivariate polynomial

$$
\mathcal{B}_{t,j}(x)=\sum_{q=0}^{t-1}[z^q]\prod_{\ell\in L}(1-z^{s_\ell}x^{B_{j,\ell}})^{-1}
$$

for t≥1. The polynomial has 2t−1 consecutive strictly positive coefficients at degrees 0,...,2t−2.

## New exact threshold theorem

**Theorem.** Suppose t=r−J≥1. Among all integers D≥2, the smallest deficit for which *every* source multiset represented in the universal positive-slack missing-layer polynomial corresponds to a well-defined saturated source pattern with the chosen total deficit D and V=J is

$$
\boxed{D_*(r,J)=\max\{2,\;2(t-1),\;J+t-1\},\qquad t=r-J.}
$$

Equivalently, for any D≥D_*, the full missing H histogram at n=2D−r is exactly

$$
\boxed{\sum_H R_{r,D,J}^{(j)}(H)x^H=x^{J-D}\mathcal{B}_{t,j}(x),\quad j=0,1.}
$$

For every 2≤D<D_*, at least one nonnegative coefficient contributed by the polynomial is not realizable by a saturated source multiset at that deficit, so the formula with universal polynomial fails even at the total missing mass. Thus D_* is the **sharp earliest applicability threshold**, not merely a sufficient bound. If t≤0 the missing-layer histogram is identically zero after the nonnegative-length source constraints, as in R749SQC.

**Examples at r=4:**

| V=J | -3 | -2 | -1 | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|---:|---:|---:|
| t=r-J | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
| exact D_* | 12 | 10 | 8 | 6 | 4 | 3 | 3 |
| missing count C_t | 651 | 279 | 113 | 42 | 14 | 4 | 1 |

For example, R749SQC's conservative sufficient inequality gave D≥4 for (r,J)=(4,2); the exact threshold is **D=3**.

## Proof

A positive-slack multiset C of L with total slack S(C)<t has deficit δ(C), signed V sum v(C), and nonoptional H data. The mandatory zero-slack e=(0,1,1) count q and zero-deficit a=(-1,2,-1) count α are uniquely

$$
q=D-\delta(C),\qquad\alpha=D-\delta(C)+v(C)-J.
$$

The remaining zero-deficit b=(0,2,0) count is then nonnegative in the saturated limit; the minimal source length is n_min=2D−J−S(C). Hence C is represented in the full saturated source family at deficit D,V=J exactly if δ(C)≤D and δ(C)−v(C)+J≤D.

Every L letter has d≤2s and d−v≤s because s=2d−1−v and d≥1. Summing these constraints gives

$$
\delta(C)\le2S(C)\le2(t-1),\qquad
\delta(C)-v(C)+J\le S(C)+J\le(t-1)+J.
$$

Thus D≥D_* makes all C valid, proving sufficiency for the formula. The length n=2D−r is nonnegative under this bound, including all integer J with t≥1 and r≥1.

Both inequalities are sharp on explicit *forced*, positive-slack source types:
- The type (h,u,v)=(0,0,2) has (d,v,s)=(2,2,1). Taking t−1 copies achieves δ(C)=2(t−1), so D<2(t−1) makes q negative.
- The type (h,u,v)=(0,1,0) has (d,v,s)=(1,0,1). Taking t−1 copies achieves δ(C)−v(C)+J=J+t−1, so D<J+t−1 makes α negative.

For t=1 the empty multiset gives the same necessity of D≥J where relevant. These are genuine source types reconstructed from the eight R749SPR facet inequalities and the 25 uniquely forced types. Each invalid C is a positive unit contribution to the universal polynomial but is absent from the saturated source count, so no cancellation can restore equality. Domain D≥2 supplies the final term in D_*. This establishes sharpness for every admissible integer (r,J), independent of the finite checks below.

## Exact computation and verification

The accompanying self-contained Node.js program reconstructs the 33 first-grid lattice points from the eight facets, derives the 25 forced types by unique two-source sums and compares the full integer source multiset DP directly to the bivariate slack formula. For J=−3,...,4 and r=1,...,6 with t≥1 it checks both alphabets at D_*,D_*+1, and, whenever D_*>2, verifies a *strict* missing-mass mismatch at D_*-1. This gives 38 parameter pairs, 152 equality checks and 64 penultimate strict checks, all PASS. An independently written Python integer DP also verified these ranges. No floating tolerance or probability sampling is used; the all-integer theorem rests on the symbolic witness argument.

## Scope and next

All results concern only the declared auxiliary 16-atom Walsh source model, with inherited author-level F classification. A formal native X6 signed-Port/Cell lifting is unproved. The next research question is to derive sharp conditions when V varies with n, and to identify which additional path/branch residuals are needed by any permitted native future observation.
