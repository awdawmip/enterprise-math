# X6 determinant-17 exact minimum: the first expanded-diagonal layer still closes exactly

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NONCANONICAL / NOT_FOUNDATION / NOT_WORKING_TRUTH`
Date: `2026-09-08`
Scope: `Enterprise Math / P000 X6 / one-step prime anisotropy / post-saturation exact certificate`
Parents:
- `research_notes/x6_p13_exact_minimum_saturated_ternary_self_gluing_20260908.md`
- `research_notes/x6_prime_discriminant_pairing_gluing_principle_20260908.md`
Exact finite certificate:
- `research_notes/certificates/x6_p17_sparse_gram_exact_certificate_20260908.py@dede6fa905049b604c4ca935b0e7b1d59d0974c8`
EM source snapshot before theorem write: `awdawmip/enterprise-math@dede6fa905049b604c4ca935b0e7b1d59d0974c8`

## 0. Theorem

For every integer full-rank transport

`A in M_6(Z)`

with

`|det A|=17`,

let

`G=A^T A`

and

`Delta_6(A)=6 tr(G^2)-tr(G)^2`.

Then

`boxed: Delta_6(A)>=72`.

The bound is sharp. Therefore

`boxed: min_{|det A|=17} Delta_6(A)=72`.

This is the first exact prime minimum in the route for which the old `minimum Gram diagonal <=2` reduction is no longer sufficient. The proof expands the exact sparse-Gram window to include minimum diagonal 3 and still closes by a finite integer certificate.

## 1. Why p=17 is the first new diagonal layer

The earlier p=7/p=11/p=13 arguments used the prime-independent fact that for sufficiently low Delta and every Gram diagonal at least 3, the determinant is at least 216.

That was enough because

`7^2=49`, `11^2=121`, `13^2=169`

are all below 216.

But

`17^2=289>216`.

So a determinant-289 Gram with low defect can in principle live with every diagonal at least 3. The old finite window cannot simply be reused.

This is a genuine proof-method transition, not a change in P000 or in the definition of Delta.

## 2. Low-defect forcing

Write

`d_i=g_ii`,

`D=sum_(i<j)(d_i-d_j)^2`,

`M=sum_(i<j)g_ij^2`.

Then

`Delta_6=D+12M`.

Assume for contradiction that

`Delta_6<72`.

Then

`M<=5`.

The diagonal range is at most 4: the minimum possible pairwise-square-difference total for six integers containing values separated by 5 is 77, already above the bound.

Thus any candidate diagonal multiset lives in a width-4 integer window.

## 3. Excluding minimum diagonal >=4

Write a candidate with all diagonals at least 4 as

`G=4I+E+R`,

where E has zero diagonal and R is diagonal nonnegative.

The defect bound gives

`sum_(i<j) E_ij^2=M<=5`.

The same norm estimate used in the preceding sparse proofs shows `4I+E` is positive definite throughout this finite E-family. Hence increasing any diagonal coordinate by R strictly increases the determinant because the corresponding principal cofactor is positive.

The exact companion certificate enumerates every admissible off-diagonal E with `M<=5` and proves

`min det(4I+E)=2560`.

Since

`2560>289`,

no determinant-289 Gram below the defect bound can have minimum diagonal at least 4.

Therefore the only remaining possible minimum diagonals are

`1,2,3`.

## 4. Exact expanded sparse-Gram certificate

After the analytic reductions, the finite search is:

- symmetric integral `6x6` matrices;
- minimum diagonal in `{1,2,3}`;
- diagonal range at most 4;
- exact `D+12M<72`;
- `M<=5`;
- target determinant 289.

The corrected result-specific certificate uses only integer arithmetic and a fraction-free Bareiss determinant.

It checks exactly

`3,057,843`

matrices in this reduced window and finds

`boxed: zero determinant-289 matrices with Delta_6<72`.

Hence every abstract symmetric integral Gram matrix of determinant 289 already satisfies

`Delta_6>=72`.

Unlike p=7, no later discriminant-form nonlift obstruction is needed below the bound.

## 5. Exact equality construction

Take

`A_17=`

`[[-1,-1, 0, 0, 0,-1],`

` [ 1,-1,-1, 0, 0, 0],`

` [ 0, 0, 0,-1, 1, 1],`

` [ 0, 1,-1, 0, 1,-1],`

` [ 0, 0, 0, 1, 1, 0],`

` [ 0, 0, 1,-1, 0,-1]]`.

Then exactly

`det A_17=17`.

Its Gram matrix is

`G_17=`

`[[ 2, 0,-1, 0, 0, 1],`

` [ 0, 3, 0, 0, 1, 0],`

` [-1, 0, 3,-1,-1, 0],`

` [ 0, 0,-1, 3, 0, 0],`

` [ 0, 1,-1, 0, 3, 0],`

` [ 1, 0, 0, 0, 0, 4]]`.

The exact invariants are

`det G_17=289`,

`tr G_17=18`,

`tr(G_17^2)=66`.

Therefore

`Delta_6=6*66-18^2=72`.

The lower bound is attained.

## 6. The equality Gram is genuinely six-dimensional in the displayed basis

The support graph of the off-diagonal entries of `G_17` is connected. Thus, unlike the displayed p=3,5,7,11,13 representatives, the equality Gram does not split into an obvious coordinate-orthogonal direct sum of two determinant-17 blocks in this basis.

Its characteristic polynomial is

`lambda^6-18 lambda^5+129 lambda^4-467 lambda^3+890 lambda^2-832 lambda+289`.

No direct-sum factorization is asserted here.

This is important for the next methodological step: a block-pair variational calculus may be a powerful lower-envelope model, but p=17 warns that an exact minimizer can present itself as a genuinely coupled full-X6 Gram rather than a visible orthogonal block pair.

## 7. First seven exact prime minima

The exact one-step atlas now contains

| p | exact `delta_min(p)` | one displayed equality geometry | strict closure exponent `tau_X6(p)` |
| ---: | ---: | --- | ---: |
| 2 | 8 | pair Hadamard | 3 |
| 3 | 32 | A2 differences + common depth | 6 |
| 5 | 48 | doubled discriminant-5 binary gluing | 3 |
| 7 | 68 | ternary + binary complementary phase | 6 |
| 11 | 68 | rank4 + binary complementary phase | 6 |
| 13 | 56 | doubled determinant-13 ternary gluing | 3 |
| 17 | 72 | connected full-X6 equality Gram | 3 |

The sequence is

`8,32,48,68,68,56,72`.

No simple monotone law in p, no simple mod-4 law for the one-step minimum, and no universal visible support-rank ladder survives all seven examples.

The strict-closure exponent and the one-step minimum remain distinct observers.

## 8. What the p=17 transition teaches

The p=17 theorem separates three questions that had coincided in some smaller examples:

1. **Current metric quality:** minimize `Delta_6`.
2. **Integral admissibility:** does an abstract Gram lift to an index-p X6 transport?
3. **Future multiplicative closure:** which branch/schedule reaches strict isotropy fastest?

For p=5 these already selected different branches. For p=7 integral admissibility killed a better abstract Gram. For p=17 the equality state is globally coupled in the displayed X6 basis.

Thus the prime geometric fiber must retain all three layers rather than treating any one as the definition of the number.

## 9. BRC / operation-safe boundary

`T0_BRC`: `REUSE_APPLIED`.

- exact determinant/index, Gram, branch/eigenlattice state and future schedule are retained beyond Delta.

`T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`.

- scalar Delta is used as the optimization observer only;
- no claim is made that equal Delta or equal spectrum gives future-equivalent arithmetic geometry.

`T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED`.

- the displayed A17 is a representative, not a canonical axis frame.

The companion finite certificate is `RESULT_ONLY`.

## 10. Status ledger

Exact proved in this note:

- `min_{|det A|=17} Delta_6(A)=72`;
- minimum-diagonal-3 must be admitted at p=17;
- exact `4I+E` determinant floor 2560 for the low-M family excludes minimum diagonal >=4;
- exact expanded finite window of 3,057,843 matrices has no determinant-289 candidate below 72;
- explicit determinant-17 equality transport and Gram;
- displayed equality Gram has connected off-diagonal support.

Still open:

- full equality-orbit classification at p=17;
- whether G17 is integrally equivalent to any useful determinant-17 block-pair gluing after a nontrivial unimodular basis change;
- a non-prime-specific lower-envelope theorem for `delta_min(p)`;
- exact p=19 minimum;
- whether finite quadratic/genus/spinor-genus data predict the one-step optimum without sparse enumeration.

## 11. Next frontier

The next high-leverage task is not to declare the finite p=19 candidate a theorem.

Use the proved seven-prime atlas as calibration for a **rank-graded determinant-p variational/gluing calculus** that keeps:

- rank;
- `tr H`, `tr(H^2)`;
- determinant p;
- discriminant form/phase;
- integral gluing/lift condition;
- X6 padding/coupling cost;
- future strict-closure state.

The known finite p=19 construction with `Delta_6=77` should be held as a falsification target/upper bound until an exact lower-bound certificate or general theorem reaches it.
