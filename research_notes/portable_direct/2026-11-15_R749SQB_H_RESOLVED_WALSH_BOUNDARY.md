# R749SQB — H-resolved Walsh boundary layers and minimal dual-readout provenance residual

Date: 2026-11-15. Status: AUTHOR_EXACT_NOT_REVIEWED. Independent portable source research, following R749SQA at immutable scientific note commit 5532ab85b3e00e74a637f5594ae07d47bf35aa86. Fixed scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. This is the auxiliary signed 16-atom Walsh optimal-center model at (t,s)=(1/10,1/2), not a native X6 relation.

## Definitions

The 25 forced first-grid source letters F and two minimal 26-letter alphabets are those of R749SPU/SQA: A_0=F union {(0,0,0)}, A_1=F union {(-1,0,0)}. Let M_j(n,H,U,V) count unordered length-n multisets from A_j with summed reading (H,U,V). At arbitrary deficit D>=2 fix U=2n-D and V=0. Write N_D for the completely saturated total number of source patterns in either alphabet and M_j^full(D,H) for their stable H histogram; the latter is a formal saturation at any n>=2D. For n=2D-r define the missing histogram R_{r,D}^{(j)}(H)=M_j^full(D,H)-M_j(2D-r,H,2(2D-r)-D,0), where j=0,1 and D>=max(2,2r-2).

The forced zero-deficit letters are a=(-1,2,-1), b=(0,2,0). Among the other 23 forced letters, only e=(0,1,1) has zero slack s=2d-1-v=0, where d=2-u. Define L as the remaining 22 forced letters together with the optional 26th letter, so |L|=23. Each L letter has strictly positive slack s. For a letter (h,u,v), define d=2-u, and shifted readout weight B_j=h_j+d-v; for forced types h_0=h_1=h. For the optional type, (s,B_0,B_1)=(3,2,1).

## Theorem 1 — exact H-resolved layer, all r

For every integer r>=1 and D>=max(2,2r-2), form the bivariate rational series

$$
\Phi_j(z,x)=\prod_{\ell\in L}(1-z^{s_\ell}x^{B_{j,\ell}})^{-1}.
$$

Then the *entire missing H histogram* is exactly

$$
\boxed{\sum_H R_{r,D}^{(j)}(H)x^H
=x^{-D}\sum_{q=0}^{r-1}[z^q]\Phi_j(z,x).}
$$

In particular the missing histogram is a translation by -D of a finite, universal polynomial independent of D. Its support has **exactly 2r-1 consecutive integer readings**

$$
\boxed{H=-D,-D+1,\ldots,-D+2(r-1),}
$$

and every coefficient on this interval is strictly positive for both j=0 and j=1.

For r=1,2,3 the two missing histograms agree. At the first signed re-entry, r=4 and D>=6,

$$
\boxed{\sum_H (R_{4,D}^{(0)}-R_{4,D}^{(1)})(H)x^H
=x^{-D}(x^2-x).}
$$

Thus the signed profile at n=2D-4 is missing exactly the signed term x^{2-D}-x^{1-D}; at n=2D-3 it has completely stabilized, sharpening the H-position of the unique last signed contribution in R749SQA.

The universal shifted distributions [coefficient of x^{H+D}] for r=1 through 4 are:

| r | missing count | A0 shifted coefficients (from H+D=0 upward) | A1 shifted coefficients |
|---|---:|---|---|
| 1 | 1 | 1 | 1 |
| 2 | 4 | 2,1,1 | 2,1,1 |
| 3 | 14 | 4,4,4,1,1 | 4,4,4,1,1 |
| 4 | 42 | 8,8,12,7,5,1,1 | 8,9,11,7,5,1,1 |

## Theorem 2 — minimal BRC-style dual-readout provenance residual

For an individual source pattern in the missing layer, let S be its total positive slack, B_0 its total shifted A0 readout weight, and k its optional-letter multiplicity. The pair of H readings is

$$
H_0=B_0-D,\qquad H_1=B_0-D-k.
$$

The triple (S,B_0,k) therefore suffices to compute both readings and whether this pattern belongs to the missing layer (S<r). Given only (S,B_0), the **minimum worst-case additional binary information** for exact paired recovery over all admissible patterns in a layer of depth r is

$$
\boxed{\left\lceil\log_2\left(\left\lfloor\frac{r-1}{3}\right\rfloor+1\right)\right\rceil\ \text{bits}.}
$$

Indeed 0<=k<=floor((r-1)/3), so recording k attains this bound. It is also necessary: the optional letter and the forced letter (-1,1,-2) both have (s,B_0)=(3,2), but their k contributions are 1 and 0. Taking m=floor((r-1)/3) letters of these two types in every mixture gives m+1 different k values with the same (S,B_0)=(3m,2m), all admissible under D>=2r-2 and with different H_1. This is an optimal residual for this **paired readout**; reconstructing all 26 source multiplicities is a distinct, higher-information objective.

## Theorem 3 — exact source-transport moment for missing layers

Write C_r for the missing count, the same for both alphabets. Let T_r denote the sum of optional-letter multiplicities over missing patterns. The bivariate series yield

$$
\sum_{r\ge1}C_r z^r=\frac{z}{1-z}G(z),\qquad
\sum_{r\ge1}T_r z^r=\frac{z}{1-z}\frac{z^3}{1-z^3}G(z),
$$

where G(z)=Phi_0(z,1)=Phi_1(z,1), with slack multiplicities (1:3,2:4,3:6,4:4,5:3,6:2,7:1). In particular (C_r,T_r) for r=1,...,9 equal

$$
(1,0),(4,0),(14,0),(42,1),(113,4),(279,14),(651,43),(1437,117),(3040,293).
$$

The natural pairing of formal missing patterns by their identical 26-letter multiplicity vector shifts their H reading by k>=0. At any declared ground cost |H-H'|/(20n) with n>=1, the normalized missing H histograms consequently have exact W_1 value

$$
\boxed{W_1^{TV,\mathrm{missing}}=\frac{T_r}{20n C_r}.}
$$

This equality uses a one-dimensional monotone coupling and the mean-difference lower bound. These normalized *missing-pattern histograms* are formal boundary corrections, not distributions of actual length-n sources when n=2D-r.

## Proof

Fix D. A saturated pattern is uniquely specified by a multiset L of nonzero-slack letters, q copies of e, alpha copies of a, beta copies of b, with optional multiplicity already included in L. Set delta(L)=sum d and v(L)=sum v. The deficit and V constraints force

$$
q=D-\delta(L),\qquad \alpha=D-\delta(L)+v(L).
$$

The minimum length, when beta=0, is exactly n_min=2D-S(L), since each nonzero-slack letter contributes 2d-1-v and e has zero slack. Hence the pattern is missing from length n=2D-r exactly when S(L)<r.

For every nonzero-slack letter in L, direct enumeration of the 25 F types verifies 0<=B_0,B_1<=2s, d<=2s and d-v<=2s. Therefore delta(L)<=2S(L) and delta(L)-v(L)<=2S(L). If D>=2(r-1), then q>=0 and alpha>=0 for all L with S<r, so these L correspond bijectively to precisely the missing saturated patterns. Moreover the H reading is

$$
H_j=\sum_{\ell\in L}h_j(\ell)-\alpha
=-D+\sum_{\ell\in L}(h_j(\ell)+d(\ell)-v(\ell))
=-D+B_j(L).
$$

Generating all unordered L multisets via independent geometric-series factors proves Theorem 1.

The 23 types satisfy 0<=B_j<=2s, so every shifted H is in [0,2(r-1)]. The three slack-one forced letters have B_j=0,1,2. For every b in [0,2(r-1)], choose r-1 slack-one letters with these weights summing to b. Every integer in this interval therefore occurs. The optional factor first appears at slack 3; its A0/A1 contribution is z^3 x^2 versus z^3 x, yielding the r=4 difference.

The count of optional letters is a sufficient residual by the H-shift formula. Its maximum is floor((r-1)/3). The explicit forced/optional equal-(s,B0) collision family gives the matching lower bound, proving Theorem 2.

Setting x=1 in Phi_j gives G. Mark the optional letter with a variable y and differentiate at y=1; the derivative of its geometric factor multiplies G by z^3/(1-z^3). Summing all slack degrees 0,...,r-1 yields the C_r and T_r generating formulas. The paired coupling has cost k/(20n) and its mean-H gap is also E[k]/(20n), so it is optimal, proving Theorem 3.

## Reproducible exact evidence and boundaries

The accompanying dependency-free Node.js checker regenerates all 33 first-grid points from the eight R749SPR facet inequalities, reconstructs the forced 25 letters from unique unordered pair sums, and independently compares (i) the truncated slack-series H histograms against (ii) a direct finite-deficit multiset DP at D=max(2,2r-2) and D+1, for every r=1,...,9. It checks support, the first signed cutoff, the C_r and T_r counts, the forced/optional collision and the slack bounds. A separately executed Python integer implementation independently reproduced the same nine layers and additionally checked r<=7 at D+2. All observed checks are PASS, with the program and structured output published alongside this note.

The all-r theorem follows from the bijective symbolic argument and finite exact letter inequalities; the preceding R749SPR/SQA model classification is inherited author-level mathematical input, pending independent review. Native X6 signed-Port/event semantics remain a separate mapping problem.

## Next exact research question

Determine the parameterized H-resolved layer for moving deficit and nonzero V slices, where the unique-filler mechanism changes; test whether the additive residual (S,B0,k) remains sufficient under the additional observer and source-sensitive operations. In particular seek an exact coupling or explicit counterexample for a native BRC–X6 readout without identifying Walsh auxiliary source letters with native Cell/Port events by assumption.
