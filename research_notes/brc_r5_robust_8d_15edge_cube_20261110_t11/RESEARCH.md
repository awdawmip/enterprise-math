# R5: explicit eight-dimensional lawful Blackwell chamber with minimum support exactly 15

Date: 2026-11-10 (Asia/Shanghai).
Evidence status: AUTHOR_DERIVATION / EXACT_RATIONAL_REPRODUCTION / INDEPENDENT_MATH_REVIEW_PENDING.
Frozen scientific inputs (unaltered): GLOBAL `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`.
Predecessor evidence: PR #1902 (exact forced-10 and complete 4,845-case rational/modular exclusion, plus one-dimensional interval); PR #1913 (physical map and eight independent observer directions); PR #1918 (six-dimensional quotient and physical tangent computations). This note is independent author-side research evidence, not an R5 CLAIM or theorem admission.

## New theorem: full-dimensional *all-point* 15-edge region

Let `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`, with allowed Blackwell carrier
`D={(0,0),(6,6)} union {(i,j): 0<=i<=6, j in {1,2,3,5}}`.
The linear map `C` has columns `C_(i,j)=(e_i,e_j,r_i e_j)` in 21 row/marginal/moment coordinates, with right hand side `b(p)=(M(Y),M(X),(r_j M(X)_j)_j)`.
Physical `p=(X,Y)` is the same 14-vector constrained by `g(X)=b(X)`, `g(Y)=1`, `z(Y)=a(Y)/10`, and the two matched stopping times, using exactly the mass/slack/time maps in #1902 and #1918.

Use the original rational physical center `p0` from PR #1902, reproduced in `VERIFY_8D.py`. Let `J_c` be the 5x14 Jacobian of the physical equalities and `n_0,...,n_8` be the rational RREF kernel basis in the order used in PR #1918. Set
`P=(n_0,n_1,n_2,n_4,n_5,n_6,n_7,n_8)` (14x8),
`B_8=J_b P` (21x8), where `J_b` is the right-hand-side Jacobian.
The inherited exact rank certificate proves `rank(B_8)=8`.

**Theorem.** Every real parameter vector `t=(t_1,...,t_8)` satisfying
`|t_k| <= 10^-100` determines a physically lawful matched-time `g=b`/seedless-F pair
`p(t)=p0+P t`, with a nonnegative Blackwell coupling supported on the fixed 15-edge basis
`SB=((0,0),(0,1),(2,1),(0,2),(2,2),(4,2),(0,3),(1,3),(3,3),(4,3),(5,3),(4,5),(5,5),(6,5),(6,6))`.
For every such `t`, every legal nonnegative Blackwell coupling has at least 15 positive edges. Consequently
`min_support(b(p(t))) = 15` **at every point of an explicit nondegenerate eight-dimensional parameter box**, not only almost everywhere.

## Exact proof

The five physical equalities hold identically along all eight kernel directions. The 26 capacity slacks are affine in `t`. Three structurally zero slacks (indices `4,15,23`, zero-based) have zero derivatives; the remaining positive slacks at `p0` have minimum `7/2000000`, while the maximum eight-coordinate absolute derivative row sum is `27`. Thus the full cube `|t_k|<=10^-100` is physically lawful.

The same 15-column basis `SB` from PR #1902, restricted to pivot rows
`I=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)`,
has determinant `-299/1600`. Let `E_B(p0)` be its exact 15-entry solution and `Delta_B=(C_{I,SB})^{-1}(B_8)_I`. The exact full 21-row identities `C_SB E_B(p0)=b0` and `C_SB Delta_B=B_8` hold. Direct rational computation gives minimum center weight `23/4000000` and maximum absolute derivative row sum `535/52`. Each of these 15 weights therefore remains strictly positive throughout the cube and all 21 Blackwell equalities hold exactly.

It remains to exclude all supports of size at most 14 uniformly. PR #1902 establishes ten exact full-carrier dual vectors `y_e` satisfying `y_e C_f <= 1_{e=f}` for all thirty edges. Their ten values `beta_e(t)=y_e b(p(t))` have exact minimum center value
`18052765669/88328232000000`; their maximum absolute eight-coordinate derivative row sum is `585227/46800`. Both are positive under the cube perturbation, so all ten forced edges `F` remain mandatory. Every putative <=14-positive support is thus contained in `F union T` for some four of the twenty remaining edges: exactly `binom(20,4)=4845` cases.

The executed modular/rational checker of PR #1902 gives a rank increase `rank([C_S|b0])>rank(C_S)` for all 4,845 candidates `S=F union T`. It does so on the 15 selected rows `I`, with every moment row scaled by 20, producing an integer coefficient matrix with entries bounded by 38 in absolute value. Write `r_S=rank(C_{I,S})<=14`. For each `S`, select one nonzero `(r_S+1)x(r_S+1)` determinant involving the appended RHS column. Its absolute value at the center is at least `1/D0`, where the actual exact common denominator is bounded by `D0=1148267016000000`.

The scaled 15x8 RHS tangent block `diag(1,...,1,20,...) (B_8)_I` has maximum absolute eight-coordinate row sum exactly `457/8`. For `|t_k|<=rho=10^-100`, multilinearity of the determinant in its last column and the Leibniz inequality give the *same* uniform perturbation bound for each selected minor:
`|det_S(t)-det_S(0)| <= 15! * 38^14 * (457/8) * rho`.
The entire certificate reduces to the explicit integer comparison
`D0 * 15! * 38^14 * (457/8) = 1122894789788793882288676685880159872483328000000000 < 10^100`.
Thus every selected augmented determinant stays nonzero for **all real** points of the cube. Consequently all 4,845 supports remain impossible, and the 15-positive-edge basis remains possible. This proves the theorem.

The four source deficits `nu_j-mu_j>0` for `j in (1,2,3,5)` also remain strict: their minimum center value is `654982477/81785400000` and maximum derivative row sum is `17/2`. This provides an independent observer-stratum diagnostic, although the ten dual certificates carry the proof of support necessity.

## Scope and reusable BRC observer interpretation

This is a parameterized eight-dimensional *physical affine slice*, with eight independent statistical readout directions. The ninth physical direction in the kernel retains a structural observer-fiber residual. All statements concern the declared seven-likelihood-ratio nonnegative Blackwell mass/moment observer; they do not change P000 native X6 semantics or physical calibration.

The result strengthens the one-dimensional robust interval of PR #1902 and the almost-everywhere eight-dimensional conclusion of PR #1918. The tiny radius is an explicit conservative witness, not a claim of optimal radius. Next: optimize margins using support-specific certificates and classify the adjoining exceptional 13/14-edge strata.

## Precise proof-audit correction to PR #1918

PR #1918's six-dimensional quotient-flat enumeration is useful for excluding full-dimensional <=14 coverings. But its final exact-rational conclusion additionally states that **every <=14-edge support is contained in one of the seven quotient rank-five flats**. That inference is false without assuming the projected support has rank <=5 (for example, that its column span contains the whole 9D physical hull).

A concrete 14-edge *index set* in PR #1918's own ordered D is
`S=(0,1,2,3,4,5,6,7,8,9,10,11,15,22)`.
The six projected columns with indices `(0,1,3,8,15,22)` have determinant `-294840000` in the integer 6x30 quotient matrix. Therefore `rank(Q(C_S))=6` and this 14-edge set is not contained in any rank-five quotient flat. This witnesses the logical gap in that particular attempted exhaustive argument; it does not construct a feasible 14-edge coupling at `p0`.

PR #1902 supplies a different, mathematically appropriate 4,845-case exclusion based on ten mandatory positive edges. The new robust-cube proof uses that certificate, not the defective exact-rational inference in #1918. The independent review of both sets of source evidence remains open.

## Verification and continuation

Independent local verification in Python 3/SymPy with exact rationals checked: `rank(B8)=8`, exact 15-column full equations, dual inequalities for all 300 edge pairs, four nonnegativity/deficit/dual/basis derivative bounds, scaled RHS bound `457/8`, and the universal integer determinant inequality. See `VERIFY_8D.py` plus `EXACT_OUTPUT.txt`. Original 4,845-case center enumeration is inherited from PR #1902, with the precise coverage and executable artifact recorded there; this artifact verifies its *uniform extension*.

Researcher activity and formal Owner/CLAIM are independently controlled; this note is an author-side publication for later independent review.
