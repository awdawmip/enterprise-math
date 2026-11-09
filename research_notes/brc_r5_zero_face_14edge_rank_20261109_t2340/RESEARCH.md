# R5 — Universal 14-edge bound on the zero-marginal Blackwell face; exact 12-dimensional full coupling polytope

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_RATIONAL_VERIFIED / INDEPENDENT_REVIEW_PENDING. This is an auxiliary seven-likelihood-ratio P/Q-BRC transport theorem. The indices 0,...,6 are statistical labels, not native P000 spatial axes.

## Frozen inputs and continuation

Frozen scientific pins: Global Knowledge `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. The precise preceding six-pivot simplex is [PR #1888](https://github.com/awdawmip/enterprise-math/pull/1888), immutable `afad8885f1831329fb12189ad0961585c7a8adde`, with prior fixed physical source X(delta), seedless F target Y, and all 21 exact Blackwell equalities. The present note takes a larger carrier than the preceding 19 edges. New exact validation is in `VERIFY.py`, with executed output in `EXACT_OUTPUT.txt`.

Likelihood-ratio nodes are
[
r=(1/10,1/2,3/4,1,5/4,3/2,19/10).
]
For nonnegative coupling E indexed by target i and source j, define target mass `mu_i=sum_j E_ij`, source mass `nu_j=sum_i E_ij`, and moments `sum_i r_i E_ij=r_j nu_j`. These comprise 21 scalar equations (some redundant). All equalities are over exact rationals or real numbers as stated.

## Theorem A — An exact uniform 14-edge transport bound on the face

**Statement.** For every pair `(mu,nu)` of nonnegative, normalized seven-node probability marginals for these strictly increasing likelihood ratios, assume `mu_1=0`, `nu_4=0`, and existence of at least one nonnegative Blackwell coupling satisfying all the above moment equations. Then there exists a coupling for the same marginals with **at most 14 positive entries**.

**Proof.** In every nonnegative coupling, `mu_1=0` annihilates row 1 and `nu_4=0` annihilates column 4. The minimum and maximum likelihood ratios occur uniquely at indices 0 and 6. In source column 0, nonnegativity and `sum_i (r_i-r_0)E_i0=0` imply `E_i0=0` for `i!=0`. Similarly, `sum_i(r_6-r_i)E_i6=0` implies `E_i6=0` for `i!=6`. Consequently every coupling is supported inside the fixed 26-edge set
[
D={(0,0),(6,6)}cup{(i,j):iin{0,2,3,4,5,6}, jin{1,2,3,5}}.
]

Let `A_D` be its 21-by-26 equality matrix. Its rank is **14**, independent of the numerical marginals. To prove the upper bound on rank, retain the six possibly nonzero row-sum equations, the six column-sum equations and four nontrivial moment equations for `j=1,2,3,5`. The two endpoint moment equations are identical to their corresponding column-sum equations times `r_0,r_6`. The remaining 16 rows obey two independent global identities: equality of total row/column mass and equality of total likelihood-ratio moments. Hence `rank(A_D)<=6+6+4-2=14`.

For the converse, the following 14 columns are linearly independent, as checked by exact rational elimination in `VERIFY.py`:
```
(0,0),(0,1),(3,1),(5,1),(0,2),(2,2),(3,2),
(2,3),(3,3),(4,3),(4,5),(6,5),(6,6),(6,1)
```
The corresponding 14-by-14 minor on row indices `0,2,3,4,5,6,7,8,9,10,12,15,16,17` has determinant `117/800`. Therefore `rank(A_D)=14`.

For a given feasible marginal vector b, the nonnegative coupling fiber `P_b={E in R^26_{>=0}:A_D E=b}` is a nonempty bounded polytope, since `sum E_ij=1`. Select one vertex. Its positive-support columns must be linearly independent: otherwise a nonzero kernel perturbation supported on those entries would produce two distinct nearby feasible nonnegative points whose midpoint is the purported vertex. Thus the vertex has at most `rank(A_D)=14` positive entries. QED.

This constructive finite-dimensional result applies simultaneously to all feasible marginals in this prescribed zero-row/zero-column face, not only the preceding four-parameter box.

## Theorem B — Full fixed-marginal coupling dimension is 12, with a 26-positive-edge point

Use the exact frozen R5 physical source at `delta=delta_max/2` on the PR #1888 ray and its fixed target Y. Both are physically legal and match their two stopping times, per the predecessor exact check. The **precise** resulting `mu,nu`, the 26 edge weights, and the seven LR ratios appear as standalone rational literals in `VERIFY.py` (no floating arithmetic).

The script validates all 21 equations, `mu_1=nu_4=0`, normalization, and **strict positivity of all 26 weights**, with the exact minimum `1/100000000`. Since the affine equality solution space has dimension `26-rank(A_D)=12` and contains a strictly positive point, the complete nonnegative Blackwell coupling polytope of this fixed marginal pair is *exactly 12-dimensional*. In particular the prior PR #1888 19-edge simplex is a proper five-dimensional support-restricted subpolytope of the full coupling space. Seven additional admissible edges are:
```
(0,3),(2,1),(4,1),(4,2),(5,2),(5,3),(5,5).
```
Four excluded row-1 edges `(1,1),(1,2),(1,3),(1,5)` remain forced zero. This gives a complete 30-candidate-edge classification for these fixed marginals: 26 can be simultaneously positive, four cannot.

## Theorem C — 14 is sharp for generic marginals in this face

Consider the image cone `K=A_D(R^{26}_{>=0})`. By the rank-14 calculation and the strictly positive witness, K has nonempty relative interior in its 14-dimensional linear span. The normalized section `sum_i mu_i=1` is 13-dimensional and has nonempty relative interior. Each fixed support of size at most 13 maps into a linear subspace of dimension at most 13 before normalization, hence into a subset of dimension at most 12 inside the normalized section. There are only finitely many such supports. Their union has empty relative interior and zero relative Lebesgue measure. Every normalized feasible marginal vector outside that finite union requires **at least 14 positive edges**. Theorem A supplies 14, so the generic exact minimum is 14. Rational marginals satisfying this property also exist by density.

The genericity statement here is about the 13-dimensional marginal face, not a claim that every point of the more restricted physical `g=b` family needs 14 edges. The current fixed physical point has explicit 14-edge representatives from PR #1888.

## Exact evidence, semantics, and next question

The `VERIFY.py` proof certificate uses Python standard-library `fractions.Fraction` and Gaussian elimination, checks all 21 exact equalities and the rank/basis. The universal bounds and genericity follow by the above algebraic arguments; finite exact computation supplies the concrete determinant and strict-positivity witness.

This is an auxiliary static Blackwell transport / BRC branch-support theorem. No pi/trigonometry, heartbeat dynamics or external physical calibration is inferred. The distinct positive branches and their labels are retained. P000's native six spatial dimensions and independent time remain as loaded.

**Next:** Determine whether every seedless F target allowed by the *entire* frozen R5 task actually satisfies `mu_1=0`. If yes, combine this theorem with the `g=b => nu_4=0` mass identity to close the R5 14-edge upper-bound question for that class. If not, analyze the remaining `mu_1>0` face and seek a legal exact 15-edge-needed witness or an additional support-rank reduction. In either case, preserve formal owner/CLAIM and independent review requirements. No formal mathematical admission is asserted by this author-side note.
