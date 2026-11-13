# R5 P/Q-BRC — universal 17-edge martingale sparsity bound is sharp

**Date:** 2026-11-09 (Asia/Shanghai). **Evidence:** author-side exact derivation, executed integer/Fraction checker, independent review pending. **Inputs:** frozen science pins GK a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e are unchanged. Current applicable behavioral context read separately from GK main e0b41088be1d8d9c518cae06d17e2c7a7eb1e3af and EM main b38a5af20fa09d17703c7a7331edffacf6ab62a7. P000 and ACTIVE worldview unchanged.

Predecessor: draft PR #1835, immutable head 3862ee316944563bb538b3e58c65fc3919ea04ec, proves a **3n−4 upper bound** on support size for any nonnegative martingale coupling on a strictly increasing common likelihood-ratio grid. We now give a matching lower bound, including an explicit rational normalized seven-node construction. The model here is a statistical Blackwell transport observer, not native X6 dynamics.

## 1. Exact theorem: the upper bound is generically optimal

Let n >= 3 and r_0 < r_1 < ... < r_(n−1), with r_0 < 1 < r_(n−1). Take source Q-distribution ν and target Q-distribution μ, both nonnegative, such that

\[
\sum_i \mu_i=\sum_j\nu_j=1,\qquad
\sum_i r_i\mu_i=\sum_j r_j\nu_j=1.
\]

A martingale transport is a nonnegative E satisfying

\[
\sum_j E_{ij}=\mu_i,\quad
\sum_i E_{ij}=\nu_j,\quad
\sum_i r_i E_{ij}=r_j\nu_j. \tag{1}
\]

**Theorem A.** The normalized feasible marginal pairs in the strict chamber

\[
\nu_0>0,\quad \nu_{n-1}>0,\qquad
0<\mu_j<\nu_j\quad (1\le j\le n-2)
\]

contain a nonempty relatively open set for which the minimum support size in (1) is exactly 3n−4. In fact, the pairs with a smaller support lie in a finite union of proper linear sections of the balanced marginal space. When the ratios are rational, rational marginal pairs with the same exact minimum exist.

**Proof.** The minimum and maximum LR source columns force only their endpoint diagonal edges: nonnegative terms in the moment defects cannot cancel. In each interior column j, a representation for a marginal pair with μ_j < ν_j must contain a nonzero off-diagonal edge, since otherwise E_jj=ν_j≤μ_j. On that column the equation

\[
\sum_i (r_i-r_j) E_{ij}=0 \tag{2}
\]

is therefore a nonzero linear equation. Across interior columns, these n−2 equations involve disjoint variables and are independent.

Fix any candidate support S with at most 3n−5 edges that could represent a pair in the strict chamber. The vector space of signed matrices on S satisfying (2) has dimension at most |S|−(n−2)≤2n−3. Let U_S be its image under the linear row/column Q-marginal map.

Before P/Q mean normalization, the image of the signed martingale matrices has dimension 2n−2. Indeed the row and column marginals obey only two independent relations: equality of total Q masses, and equality of their LR-weighted moments. Conversely, given any ν and μ with those two relations, start with diagonal E=diag(ν) and put the correction d_i=μ_i−ν_i in any one interior source column. The column has zero extra Q mass and moment because Σd_i=Σr_i d_i=0. This gives the requested signed martingale array.

Impose the further homogeneous normalization of average LR to one, Σ_j(r_j−1)ν_j=0. This defines a balanced linear marginal space W of dimension

\[
\dim W=2n-3. \tag{3}
\]

Every viable S contains (0,0), because ν_0>0. The singleton matrix supported on (0,0) belongs to its signed martingale kernel, but its marginal image has mean ratio r_0≠1 and is outside W. Thus U_S is not contained in W. Since dim U_S≤dim W, W cannot be contained in U_S; W∩U_S is a proper subspace of W.

There are finitely many candidate S. Their union of proper subspaces cannot cover a relatively open set in W. Such an open feasible chamber exists because r_0<1<r_(n−1): choose all ν_j positive with mean ratio one, and for each interior column send most mass to a positive barycentric mixture of the two extreme rows, retaining tiny strictly positive mass on every other allowed edge. The resulting μ_j<ν_j for all interior j, and E is strictly positive on all permitted edges. Small signed perturbations of this positive E, satisfying the martingale and mean constraints, map onto a neighborhood in W by the surjectivity argument above. Intersect with the affine Q-normalization Σν=1; that relatively open affine section spans W under scaling, so no proper linear section of W contains it. Rational points are dense in the rational-defined chamber, proving the rational existence assertion. The upper bound 3n−4 comes from PR #1835. QED.

Here “generic” is an explicit complement of finitely many proper linear sections; it has no probabilistic distribution assumption.

## 2. An explicit rational, normalized, seven-node witness

Use the exact common LR grid

\[
r=(2,10,15,20,25,30,38)/20.
\]

The attached independent script VERIFY_SHARP17.py constructs eleven integer nonnegative martingale matrices G_0,...,G_10, each globally balanced (P total equals Q total), all in the strict chamber. Their 21-coordinate output vectors — seven row Q masses, seven column Q masses and seven integer LR-weighted moments — have an exact **nonzero 11×11 minor**

\[
\det=-7140677472000,
\]

using zero-based output row indices [0,1,2,3,4,5,7,8,9,10,11]. Hence these eleven images form a basis of W, which has dimension 11 for n=7.

Construction details (all executable in the script): set k=(2,10,15,20,25,30,38). The diagonal atom D(j) has only E_jj=1. For any a<j<b, the positive barycentric atom P(a,j,b) has E_aj=k_b−k_j and E_bj=k_j−k_a. Summing all 42 diagonal and barycentric atoms gives E0, balanced by reflection and strictly positive on all 37 allowed edges. Let O=Σ_(j=1)^5 P(0,j,6) and BASE=E0+100O. Ten additional balanced rays are D(3), P(0,3,4), P(0,3,5), P(0,3,6), P(1,3,4), P(2,3,4), and balanced combinations D(0)+D(4), D(0)+D(5), D(0)+D(6), D(1)+D(4). Each combination uses the positive integer coefficients in the script's balanced_pair routine, chosen to cancel Σ(k_i−20)E_ij. Define G_0=BASE and G_k=BASE+R_k for the ten rays.

Set

\[
L=2242200,\quad H=12!L^{12},\quad B=H+2,\qquad
E_B=\sum_{k=0}^{10}B^k G_k. \tag{4}
\]

Let M=Σ_ij (E_B)_ij, and normalize the row Q marginals μ_i and column Q marginals ν_j by M. These are explicit rational probability vectors with Σr_i μ_i=Σr_j ν_j=1. Every permitted edge of E_B is positive, both endpoint source masses are positive and all interior deficits ν_j−μ_j are strictly positive. The checker executes all these integer equalities; B has 85 decimal digits and M has 854 decimal digits, but (4) is a compact exact specification.

**Why the normalized pair (4) cannot be represented with 16 or fewer edges.** Any admissible support S with ≤16 edges has the five independent interior equations (2), so its signed martingale kernel has dimension d≤11. Build an integer basis by pivoting on one coefficient k_i−k_j in each middle column and eliminating the other coordinates. Each basis vector has ≤2 nonzero entries, each of absolute size at most 36. Under the integer constraint map A_int (row/column masses multiplied by 20 and LR moments using k_i), all images of these basis vectors have entries of size at most 2×38×36=2736. The integer images of the eleven G_k have entries of size at most L by the exact checker.

As proved above, U_S does not contain W. At least one of the eleven independent generator images is therefore outside U_S. A (d+1)×(d+1) minor of the augmented basis matrix with the column image(E_B) is consequently a **nonzero integer polynomial**

\[
f(B)=\sum_{k=0}^{10}c_kB^k
\]

whose coefficient magnitudes are bounded uniformly by

\[
|c_k|\le(d+1)!L^{d+1}\le 12!L^{12}=H.
\]

A nonzero integer polynomial of degree m≤10 with |c_k|≤H cannot vanish at any integer B>H+1: its leading term has magnitude ≥B^m, whereas all smaller powers have combined magnitude at most H(1+B+...+B^(m−1))<B^m. Our choice B=H+2 makes f(B) nonzero, contradicting membership in U_S. Therefore every martingale representation of these **explicit normalized rational marginals** needs at least 17 edges. The predecessor's general upper bound supplies a 17-edge representation. The minimum is exactly 17.

The argument avoids the exponential enumeration of supports; the finite program verifies the generator/minor/bound inputs to this general exact coefficient-separation proof.

## 3. Executed evidence and scope

Locally executed command: python -S VERIFY_SHARP17.py (exit code 0); stdout is preserved in EXACT_OUTPUT_SHARP17.txt. It checks the nonzero minor, independence of all eleven balanced generators, their strict chamber, the full 37-edge E_B, integer mass and LR-moment preservation, normalization and determinant bound parameters. The all-support lower bound follows from the above exact proof, rather than a numerical search.

BRC observer lease: full Q-edge transport graph, source/target histograms, LR node identities and weighted moments, with randomized terminal declarations as the downstream observer. Source-to-target Blackwell reduction preserves that observer class. The strict optimality theorem concerns the unrestricted normalized common-grid martingale class; the extra lawful FULL_HIST and seedless LR flow relations of R5 are the next specialized question.

## 4. Next independent unit

Determine whether the R5 physical-flow family intersects a 17-edge-necessary marginal region. Fetch the frozen seven-node marginal formula, impose its lawful capacities and seedless constraints, evaluate the interior deficits ν_j−μ_j and the affine dimension of attainable normalized pairs, and perform an exact sparse-support feasibility/dual test on a concrete interior candidate. If the physical family lies in a smaller class, derive a sharper physical-family support theorem instead. The full-domain R5 feasibility stitch in PR #1831 also remains pending independent scientific review.

**Status:** author-side proved with exact computation; portable research evidence only. No change to task OWNER/CLAIM, P000, Working Truth, Foundation or formal Result/Review is asserted.
