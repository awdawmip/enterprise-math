# R749SNG — Complete remaining diagonal Walsh minimax phases

**Date / authorship:** 2026-11-13; researcher EM-DIRECT-EF57C2, RA-2A3C9A7FCCE5076FE5783C70.
**Scientific input:** preserved immutable pin awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Continues R749SNF at PR #2308, scientific commit 5f58cee950c6a86d71f9bf8e4117b7acea30722d. The analytic group model and its evidence do not purport to identify a native X6/V29/V39 event.
**Status:** author-side proof with independent exact rational enumeration; external scientific review NOT_REVIEWED.

## Statement

Let G=F_2^4, characters chi_m(x)=(-1)^{popcount(m & x)}. Let
B={3,5,6,7,9,10,11,12,13,14}. Fix the retained moments m_3=m_12=p and all other eight retained moments equal to zero. F_p is the nonempty polytope of compatible probability laws on G. Define

rho(p)= min_{q in Delta(G)} max_{mu in F_p} TV(q,mu),

rho_cal(p)= min_{q in F_p} max_{mu in F_p} TV(q,mu).

For every REAL p in [4/9,1],

rho(p) = (3+2p)/10 on [4/9,1/2]; 4(1-p)/5 on [1/2,1].

rho_cal(p) = 2/5 on [4/9,7/15]; 3(1+p)/11 on [7/15,1/2]; 9(1-p)/11 on [1/2,1].

At all shared endpoints the formulas agree. The end of the calibrated 2/5 plateau is exactly 7/15, and the next common change of source-polytope combinatorics is p=1/2. This completes the previously open interval p>4/9, including p=1, where both radii are zero.

The same formulas hold at negative parameters by replacing p with |p| on [-1,-4/9]. Indeed translation by g=5 has chi_3(g)=chi_12(g)=-1; it carries F_p isometrically onto F_{-p}, taking calibrated predictors to calibrated predictors.

## Exact parameterization and symmetry reduction

Write A=chi_3, D=chi_12, AD=chi_15, P=chi_1, AP=chi_2, Q=chi_4, DQ=chi_8. Inverse Walsh transform supplies the **entire** compatible fiber:

mu_{p,h,u,v,w,z}(x)
 = [1+p(A(x)+D(x))+h AD(x)+u P(x)+v AP(x)+w Q(x)+z DQ(x)]/16 >=0.

This is normalized because the six nonconstant terms have zero sum. There are no missing free coefficients: the remaining eight retained characters have prescribed zero moments. The fiber is invariant under sign flips of P and Q and interchange of the two (A,P)/(D,Q) character pairs. TV is convex in the decoder and invariant under these finite transformations. Averaging an arbitrary decoder over the symmetry group therefore never increases its worst-case loss. Consequently both minimax problems admit optimizers of the form

q_{tau,eta}(x)=[1+tau(A(x)+D(x))+eta AD(x)]/16.

The free problem optimizes tau,eta subject to positivity; for the calibrated problem tau=p and q is automatically in F_p when nonnegative.

## Explicit optimal decoders

For the free problem:

* 4/9 <= p <= 1/2: tau=(18p-3)/10, eta=2(1-p)/5;
* 1/2 <= p <= 1: tau=(4p+1)/5, eta=(8p-3)/5.

For calibrated prediction:

* 4/9 <= p <= 7/15: tau=p, eta=1/5;
* 7/15 <= p <= 1/2: tau=p, eta=(5-6p)/11;
* 1/2 <= p <= 1: tau=p, eta=(18p-7)/11.

For each claimed interval the four distinct values [1+tau(A+D)+eta AD]/16 are nonnegative, and their total probability is one. Thus all five displayed formulas give legal predictors throughout, not only at the stated endpoints.

## Universal lower bounds from feasible source laws

Use four **explicit** source witnesses, given by their five free coefficients (h,u,v,w,z):

* AD = (1,0,0,0,0);
* alpha = (2p-1,p-1,p-1,1-3p,1-3p);
* beta = (0,p-1,-p,-p,-p);
* gamma = (2p-1,p-1,p-1,p-1,p-1).

AD, alpha, beta are normalized and nonnegative on [4/9,1/2]. AD, gamma are normalized and nonnegative on [1/2,1]. This follows by substituting their coefficients in the sixteen affine atom formulas and checking interval endpoints; each atom is affine in p.

For an event T and witness mu, the lower bound TV(q,mu)>=q(T)-mu(T) holds for *every* decoder q. Use the following events (indices x=0,..,15):

T_AD = {1,2,4,7,8,11,13,14}.
T_alphaII = {0,1,2,4,5,6,8,9,10,12}.
T_alphaIII = {0,1,2,3,4,5,6,8,9,10,12}.
T_beta = {0,1,2,3,4,6,8,10,12}.
T_gammaI = {0,1,2,3,4,8,12}.
T_gammaII = {0,1,2,3,4,5,6,8,9,10,12}.

Let L_label=q(T_label)-mu_label(T_label). Direct character summation yields, for every real tau,eta,

L_AD=(1-eta)/2;
L_alphaII=(3+2p-2tau+eta)/8;
L_alphaIII=(3+8p-2tau+3eta)/16;
L_beta=(5+2tau+eta)/16;
L_gammaI=(11-16p+6tau-eta)/16;
L_gammaII=(15-16p-2tau+3eta)/16.

The following **nonnegative convex combinations** eliminate all free decoder variables:

( L_AD + 2 L_alphaIII + 2 L_beta )/5 = (3+2p)/10, valid on [4/9,1/2].

( L_AD + L_gammaI + 3 L_gammaII )/5 = 4(1-p)/5, valid on [1/2,1].

Under the calibration constraint tau=p, the combinations

( L_AD + 4 L_alphaII )/5 = 2/5, valid on [4/9,1/2],

( 3 L_AD + 8 L_alphaIII )/11 = 3(1+p)/11, valid on [4/9,1/2],

( 3 L_AD + 8 L_gammaII )/11 = 9(1-p)/11, valid on [1/2,1]

give lower bounds. The first two intersect exactly at p=7/15. Select the larger bound on the respective intervals. Each lower bound is valid for **every** compatible source law and every permissible decoder, independent of the proposed upper-bound decoders.

## Universal upper bounds: complete six-dimensional rational certificate

On each of the three closed slabs [4/9,7/15], [7/15,1/2], and [1/2,1], the proposed source constraints and decoder coefficients are affine in six joint variables (p,h,u,v,w,z). The joint feasible polytope is compact and full-dimensional, cut out by the sixteen affine atom positivity inequalities and the two p-endpoint inequalities.

For a fixed slab, the function
TV(mu_{p,h,u,v,w,z}, q_{tau(p),eta(p)}) - proposed_radius(p)
is convex in all six variables: it is a sum of absolute values of affine expressions minus an affine expression. Therefore it attains its maximum at a vertex of the **joint** polytope. Any vertex has six independent active facets among the eighteen defining inequalities, so exact enumeration of all C(18,6)=18564 choices and rational feasibility checking is an exhaustive upper-bound proof.

The accompanying Python standard-library certificate enumerates each independent six-facet basis using integer Bareiss elimination plus rational substitution, deduplicates its rational vertices, checks all source and decoder probabilities exactly, and verifies both radius inequalities on each vertex.

| Slab | Six-facet subsets | Nonsingular | Feasible bases | Distinct vertices | Free equality | Calibrated equality |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [4/9,7/15] | 18564 | 10848 | 464 | 82 | 58 | 38 |
| [7/15,1/2] | 18564 | 10848 | 832 | 58 | 34 | 34 |
| [1/2,1] | 18564 | 10848 | 1644 | 18 | 6 | 6 |

All vertices lie at slab endpoints: the first slab has 41/41; the second 41/17; the last 17/1. Zero violations occur. Finite enumeration is applied only to a polyhedral **certificate**, not mistaken for a sample of real p. Convexity supplies the universal quantifier over all real p and all compatible source laws.

Combining upper bounds with the analytic universal lower bounds proves the theorem.

## Scientific boundary and continuation

The result applies exactly to the declared finite Walsh observer fiber; the character model is an auxiliary mathematical construction, not a claim of a native signed-Port or V29/V39 transition correspondence. No task CLAIM, Driver review, Working Truth or Foundation change is asserted. The existing X6 spatial and residual-preservation contracts stay intact.

This resolves the two questions left by R749SNF: first free phase after p=4/9, and right endpoint of the calibrated 2/5 plateau. A useful next scientific unit is the off-diagonal exact fiber rho(t,s), especially the bifurcation of the p=7/15 calibrated boundary under t != s; independently investigate finite future-observer kernels and their residual-faithfulness implications. Preserve the frozen scientific pin and require a separately verified native-event correspondence before transporting this result to X6 operations.

**Reproducibility:** Execute R749SNG_DIAGONAL_FINAL_PHASES_EXACT_CHECK.py using Python 3 standard library, compare output with R749SNG_DIAGONAL_FINAL_PHASES_RESULTS.json. The proof-level checks use exact rational arithmetic; no floating-point solver is used for the certificate.
