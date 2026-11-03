# PREFIX-458 — Exact seventh-degree native X6/BRC boundary rank

Date: 2026-11-03. Status: AUTHOR_EXACT_COMPUTER_ASSISTED_PROOF / UNREVIEWED / NOT_ADMITTED. Direct predecessor: PREFIX-457, Enterprise Math commit 6201bd34724d5f67087b3f536df402730d172870. Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. This is a separate author-side exact computation, not a formal native Source CLAIM.

## Exact statement

The P000 native X6 model has six signed integer displacement axes, not twelve independent dimensions. A legal ordered path has N signed unit-axis steps. Its history sector is the number of -e1 steps modulo q. For each sector retain all rational-positive weighted endpoint monomials x^alpha with alpha in N^6 and |alpha| <= 7. There are B_7 = binom(13,6) = 1716 standard coordinates per sector.

THEOREM (computer-assisted finite-lemma proof). For every integer q >= 7, at N = q + 5 the exact rank over Q of all sector-separated degree-<=7 endpoint observations is

R_7(q) = 1716*q - 96.

All sectors r=0,...,q-2 have full rank 1716; sector r=q-1 has rank 1620, an exact deficiency of 96. In this fixed known-support model, 96 of the last-sector moments can be recovered by rational-linear expressions in the 1620 pivot moments. The result concerns snapshot rank and arbitrary finite positive-rational source mass; original ordered-path provenance remains separate.

## Proof A: earlier sectors are unisolvent

Put D = {+e1,+/-e2,...,+/-e6}, the 11 legal steps excluding -e1. For each r <= q-2, concatenate r copies of -e1, q-r-2 copies of +e1, and 7 freely chosen D steps. The length is q+5, and the exact -e1 count is r. Within D choose seven affinely independent vertices v0=-e2 and v1,...,v6=(+e2,+e1,+e3,+e4,+e5,+e6). Their difference matrix has determinant of absolute value 2. All 7-step sums over these vertices give an invertible affine image of the six-dimensional integer simplex {a in N^6 : |a|<=7}. By multivariate falling-factorial (Newton) interpolation, evaluation of all polynomials of total degree <=7 on these 1716 nodes is nonsingular over Q. So each earlier sector has rank 1716.

## Proof B: last sector and characteristic-zero certificate

When r=q-1 and q>=7, a second wrap would require at least 2q-1 > q+5 negative-first-axis steps, impossible. Exactly q-1 steps are -e1; the remaining six steps lie in D. After translating the first endpoint coordinate, the last-sector support is W6: the distinct sums of six D-vectors. Its size is 4396. This count can be independently derived from the exact ordinary generating function for W_m sizes: sum_{m>=0} |W_m| z^m = (1+z)^4/(1-z)^7.

Construct the complete integer evaluation matrix A in Z^(4396 x 1716), A[x,alpha] = prod_i x_i^(alpha_i), for every x in W6 and every monomial degree<=7. The executable certificate supplied alongside this note does the following:

1. It computes exact finite-field echelon ranks modulo the two independently checked primes 32003 and 32009; both equal 1620 with identical pivot and free columns. A modular nonzero 1620-minor proves rank_Q(A)>=1620.
2. It builds the full 1716 x 96 modular nullspace at each prime, with a 96 x 96 identity in the free-coordinate rows. Chinese remaindering modulo 1024384027 and bounded rational reconstruction recover a rational nullspace basis; clearing each column denominator (largest encountered 15) yields an explicit integer matrix K of shape 1716 x 96. The free-coordinate submatrix of K is diagonal with positive entries, proving its 96 columns independent over Q.
3. It checks A*K=0 on all 4396 rows and 96 columns with exact signed 64-bit integer arithmetic; a conservative entrywise accumulation bound is 279936*3024*1716=1452639412224, strictly less than 2^63. The reconstructed K has 2041 nonzero coefficients and maximum absolute coefficient 3024. Hence nullity_Q(A)>=96, so rank_Q(A)<=1620.

Thus rank_Q(A)=1620 exactly, combining lower and upper bounds. The program writes a reproducible sparse-friendly compressed integer-kernel artifact PREFIX458_INTEGER_KERNEL.npz in its working directory; publication of the program and actual log is sufficient to regenerate the certificate. As in PREFIX-457, this is a computer-assisted proof of one finite exact integer matrix lemma, coupled with a paper argument for all q>=7.

## BRC observation and decoder

For the last-sector known support W6, select the 1620 pivot monomials as a sufficient rational-linear readout. Each of the 96 omitted standard seventh-degree moments is exactly decoded by the integer kernel K, because its free-coordinate submatrix is diagonal and nonzero. The earlier sectors retain their full 1716 coordinates. For finite parallel addition of positive-rational sources, history-conditioned positive-rational branching, and rational-affine endpoint pullback, first reconstruct all standard moments and apply the usual polynomial pullback identities. This preserves the degree-<=7 observations for finite compositions within this operation language; no signed amplitude/phase or native physical-time claim is made.

The result is a direct seventh-degree continuation of the verified deficiency sequence 32,48,64,80,96 at degrees 3,...,7. The general candidate defect 16(d-1), for d>=3 at N=q+d-2 under sufficiently large q, remains a conjecture. No unproved all-degree statement is promoted.

## Verification and provenance

Executed source: prefix458_septic_exact_certificate.py, Python 3.13 with NumPy and Numba; all matrix values, modular computations, CRT coefficients, and final A*K verification are exact integers. The two moduli were independently checked prime. Actual execution log: PREFIX458_EXACT_EXECUTION.log. Reproducibility: python prefix458_septic_exact_certificate.py (the output NPZ destination in the script is /mnt/data/prefix458_work). Timing figures are diagnostic, variable by runtime.

Frozen scientific input source: f42f2906d77f24085c123f3ccfe9667d41caa96d. The current normative context was re-read from canonical global and Enterprise Math main. This run used the proven signed-native-path BRC readout semantics of the previous PREFIX series rather than a new upstream-native class integration; earlier native integration evidence remains PREFIX-452. Mathematical status AUTHOR_PROVED_WITH_EXACT_INTEGER_CERTIFICATE, not independently reviewed or admitted.

GitHub authenticated user: awdawmip with push/admin permission. Native owner dispatch during this run returned CONTROL_QUOTA and Site status research_authority_granted=false, so no current formal Task owner, CLAIM, independent Review or Admission was asserted.

## Next scientific unit — PREFIX-459

Develop an algebraic proof of 16(d-1) for arbitrary d>=3, using graded vanishing ideals of W_(d-1) and the sign-complete native path support. A separate executable unit is to benchmark the 96-coordinate integer decoder, including actual byte/bit complexity for large rational weights, and compare an explicit kernel-basis codec against storing 1716 full moments in the terminal sector. Retain the frozen scientific input for that task.
