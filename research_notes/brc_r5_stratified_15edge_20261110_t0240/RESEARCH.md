# R5 — Stratified 15-edge necessity in the seven-node Blackwell face

Date: 2026-11-10 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING.

## Frozen provenance and exact question

Continue immutable author-side PR #1896 (commit `1ad4649af24cbd5c3a4527ecdd226b721c49aac9`) and PR #1894 (commit `b4d0594d3f9705dbe403b607741871ec9ff97842`). Preserve their declared frozen science pins: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. This is the *statistical* seven-likelihood-ratio P/Q-BRC observer, not seven native space axes or a new P000 claim.

Question: after the correction that the normalized `nu_4=0` marginal affine face is 10-dimensional and includes open 12-edge regions, are there nevertheless precise open regions where the 15-edge vertex upper bound is sharp? Answer: **yes**, with a constructive exact 15-needed (transcendental-parameter) statistical marginal pair.

## Model and theorem

Set `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. Let

`D={(0,0),(6,6)} union {(i,j): 0<=i<=6, j in {1,2,3,5}}`.

For a nonnegative `E` supported in `D`, require `sum_ij E_ij=1`, and set
`mu_i=sum_j E_ij`, `nu_j=sum_i E_ij` with the exact martingale/Blackwell constraints
`H_j(E)=sum_i (r_i-r_j)E_ij=0` for all `j`.

Define `U` as the feasible normalized marginal pairs `(mu,nu)` with `nu_4=0` and

`nu_j>mu_j` for **all** `j in J={1,2,3,5}`.

**Theorem A (stratified sharpness).** `U` contains a nonempty relatively open subset of the full 10-dimensional compatible marginal affine space. For every pair in `U` some Blackwell transport uses at most 15 positive edges; almost every pair in `U` (relative 10D Lebesgue measure) needs *exactly* 15. Thus 12-edge relatively open chambers and 15-edge generic regions coexist on the same normalized `nu_4=0` face. The upper bound is global on this face; the lower statement is stratified to `U`.

**Theorem B (explicit exact witness).** There is an explicit marginal pair `(mu*,nu*)` given below, defined by a finite formula using `t=e/10^11`, which is feasible with all 30 entries positive, satisfies `nu*_j>mu*_j` for all four `j in J`, and for which **every** nonnegative Blackwell coupling has at least 15 positive edges. A coupling with at most 15 exists by Theorem A, so its exact minimum is 15.

## Proof of Theorem A

For any coupling `E` of a pair in `U`, source column `j in J` must contain an off-diagonal positive edge: if it were solely diagonal, then `mu_j>=nu_j`, contrary to `nu_j>mu_j`. Hence on **every** realizing support `S`, the `j`th martingale defect row `H_j` has some nonzero coefficient. As different source columns have disjoint edge variables, these four defect rows are linearly independent: `rank H_S=4`.

If `|S|=k<=14`, the linear space `ker H_S` has dimension `k-4`. The probability-mass normalization is an independent equation on this kernel (it takes value 1 at the realized coupling), so its normalized affine section has dimension `k-5<=9`. Its rational linear marginal image therefore lies in a **proper rational affine subspace** of the 10D compatible marginal face. There are finitely many `S subseteq D` with `|S|<=14`; their images form a measure-zero finite union. All remaining pairs in `U` require at least 15 edges.

The augmented 21-row Blackwell column matrix for `D` has rank 15, certified by the exact 15-by-15 minor `-299/1600` below. The feasible transport polytope is nonempty and compact; at any vertex, its positive columns are linearly independent, so a vertex uses at most 15 edges. This proves the upper bound.

Nonempty full-dimensional relative interior is established constructively by the `E0` and 10 rational tangent vectors in the next section: `E0` has 30 strictly positive entries and all four strict deficits; the 10 observation vectors span the compatible 10D marginal tangent space, so sufficiently small changes remain feasible and in `U`.

## Proof of Theorem B: completely specified exact construction

Use the exact rational `mu0,nu0` listed in `VERIFY.py`, obtained in PR #1894 from a lawful matched-time `g=b` physical source/seedless target. The physical precursor is provenance for **E0 only**. Denote by `C_(i,j)` the 21-vector with entries 1 in target-row coordinate `i`, 1 in source-column coordinate `7+j`, and `r_i` in moment coordinate `14+j`. Take the 15 columns in ordered set

`B=((0,0),(0,1),(2,1),(0,2),(2,2),(4,2),(0,3),(1,3),(3,3),(4,3),(5,3),(4,5),(5,5),(6,5),(6,6))`

and pivot rows

`(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17)`.

Set `E0_e=1/10000000` for every `e in D`; solve the rational 15-by-15 subsystem for corrections on columns `B` against `(mu0,nu0,(r_j nu0_j))-sum_e E0_e C_e`. The exact determinant is `-299/1600`, all 21 equations hold, and the final minimum weight remains `1/10000000`.

The four positive exact deficits `nu0_j-mu0_j`, for `j=(1,2,3,5)`, are respectively

`199781/12000000,` `654982477/81785400000,` `32437731732967/574133508000000,` `112091952623/545236000000`.

Define the 12-edge rational chart
`S12={(0,0),(1,1),(2,2),(3,3),(6,6)} union {(i,5):i=0,...,6}`.
Its augmented column matrix has an exact 12-by-12 minor equal to `1` at row indices `(0,1,2,3,4,5,6,7,8,9,10,12)`.

Take pivot edges `a=(6,5)`, `b=(0,5)`. Let `f_1,...,f_10` be the ten remaining edges of `S12` in the order returned by the definition. Write `h_f=r_{i(f)}-r_{j(f)}`. Define the rational vector `V_k` supported on `{f_k,a,b}` by

`(V_k)_(f_k)=1; (V_k)_a=(-7/5-h_(f_k))/(9/5); (V_k)_b=-1-(V_k)_a.`

Each `V_k` has zero total mass and zero martingale defect in each source column. All its coefficients have absolute value at most 1. Their ten free coordinates form the identity matrix. The augmented `S12` full-column-rank certificate shows that their ten marginal images are independent, spanning the entire normalized 10D compatible marginal tangent space.

Now use the **exact transcendental real** `t=e/10^11`, with `e` Euler's number (known to be transcendental and `2<e<3`), and set

`E*=E0+sum_(k=1)^10 t^k V_k;   mu*=row_sums(E*); nu*=column_sums(E*).`

The total change at every matrix entry is bounded by `sum_(k=1)^10 t^k <10t<3/10^10<1/10000000`. For each source-row deficit `nu_j-mu_j`, the change is bounded by `4 sum_(k=1)^10 t^k <12/10^10<1/1000`. The displayed four original deficits are each greater than `1/1000`. Consequently all 30 weights of `E*` are positive, the four strict deficits persist, the mass is 1 and all martingale equations hold.

Every `S` with at most 14 edges realizing `(mu*,nu*)` must lie in a proper **rational** affine hyperplane of the 10D normalized marginal space, by Theorem A. Suppose a rational affine hyperplane contained `(mu*,nu*)`. Compose its nonconstant rational affine defining functional `L` with
`(mu0,nu0)+sum_k t^k Psi(V_k)`.
This is a polynomial in `t` with rational coefficients, **not** the zero polynomial because the ten `Psi(V_k)` form a basis of the 10D tangent space. Since `t` is transcendental, that polynomial cannot vanish. Contradiction. Thus no coupling with 14 or fewer positive edges exists.

The displayed construction is an exact auxiliary *statistical* coupling. Whether the perturbed `(mu*,nu*)` itself has a lawful physical `g=b` realization with matched stopping times remains a separate R5 question.

## Verification and next unit

`VERIFY.py` uses only Python `Fraction` to reconstruct `E0`, verify all 21 equalities, nonnegativity, 15- and 12-column determinants, four exact strict deficits, 10 independent martingale-preserving tangent directions and the rational perturbation bounds. The final exclusion uses the explicit transcendence/polynomial proof above, not a floating-point solver.

A separate exploratory mixed-integer feasibility probe on the *unperturbed physical* PR #1894 rational pair found a 15-edge solution and reported infeasibility for budgets 11 through 14 (SciPy HiGHS); this is a numerical lead only, not an exact infeasibility certificate. The next discriminating unit is an exact rational/support or modular certificate of the **physical** witness's minimum support, or an exact physical perturbation subspace where no 14-edge chart can contain the whole affine family. Current R5 owner/claim, native checkpoint and independent review require their own control receipts.

Author-side researcher: `EM-DIRECT-9788C0`; activity `RA-C5546CF775BD31C44A4B3A42`; no formal R5 CLAIM asserted.
