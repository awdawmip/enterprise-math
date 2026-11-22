# PREFIX-1024 — Eventual strict Hankel positivity for positive-port signed BRC masses

Date: 2026-11-23 Asia/Shanghai. Status: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_LAURENT_CHECKED / NOT_REVIEWED.

## Frozen object and provenance

Continuation of PREFIX-1023 (positive-port infinite Hankel rank and an early negative 3x3 Hankel minor) without changing the scientific task pin: `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json`, P000 V5, candidate Stage46 12-direction signed BRC kernel W=J_12-6I_12, fixed chosen Cell, initial incoming -e1, double-direction absorption of Link {0,e1}, and exactly one negative outgoing direction (grade k=1). In a joint Cell–terminal-port–grade fibre, signed amplitudes are combined *before* square-mass observation. All Q values below are integer numerators, divided by 36^n for physical normalized outputs.

Let S=sum_{i=1}^6 z_i, S*=sum_{i=1}^6 z_i^(-1), L=SS*. For a positive terminal port j, PREFIX-1023 gives the verified exact Laurent packet (m=n-4>=1):

A_(m,j)=(m+3)(L-36)+E_j,  E_j=72-6S(z_1^(-1)+z_j^(-1)),
B_(m,j)=z_j[(S-z_1)A_(m,j)+z_1(L-36)+25z_1],
Q^+_(m+4,j)=CT[S^m B_(m,j) (S^m B_(m,j))*].

Duplicate terms for j=1 retain their full multiplicity. The fixed Laurent packet is not modified in this result. The X6 model is an internal discrete research model, with asymptotic torus integrals used here as an exact external-analysis observer for the integer Laurent coefficients, not as a replacement for native Cell/port state.

## Theorem — eventual strict positive definiteness at each fixed Hankel order

For every positive port j=1,...,6 and every fixed integer h>=1, there exists an integer N_h,j such that the matrix

H_h(n0,j) = [Q^+_(n0+a+b,j)]_(0<=a,b<h)

is strictly positive definite for every integer n0>=N_h,j. More sharply, set m=n0-4, alpha=5/2, C=7063875/(4*pi^(5/2)). For every fixed h,

det H_h(m+4,j)
  ~ C^h * 36^(h*m+h*(h-1))
      * m^(-alpha*h-h*(h-1))
      * product_(k=0)^(h-1) [k! (alpha)_k],

where (alpha)_k is the rising factorial, (alpha)_0=1. The leading constant is strictly positive. The same leading determinant asymptotic applies independently to all six positive ports.

This establishes eventual positivity for **each fixed finite order**, with an order-dependent onset. It does not assert one universal threshold simultaneously covering unbounded h.

## Proof

1. PREFIX-1023's positive-port Laurent packet admits the exact five-relative-phase Parseval integral

 Q^+_(m+4,j)=(2*pi)^(-5) int_(T^5) [L(u)]^m |B_(m,j)(u)|^2 du,

 where the global phase has been fixed by z_1=1. The unique maximum of L on T^5 is u=0, with L(0)=36. With q(u)=sum_(i=2)^6 u_i^2-(sum_(i=2)^6 u_i)^2/6, its quadratic expansion is L(u)=36-6q(u)+O(|u|^4). The quadratic q is positive definite.

2. Near u=0, B_(m,j)=(m+3)P_j(u)+R_j(u) for fixed analytic Laurent functions P_j,R_j, where P_j(u)=O(|u|^2) and R_j(0)=25. Rescale u=y/sqrt(m). Then [L(y/sqrt(m))/36]^m tends to exp(-q(y)/6) and B_(m,j)(y/sqrt(m)) tends to 25-30q(y). The integrand is analytic near the unique nondegenerate maximum, the complement is exponentially small, and complex conjugation gives parity under u -> -u. Expanding in the rescaled variables with Gaussian domination proves the **full** asymptotic series to arbitrary integer order K (not just a leading equivalent):

 Q^+_(m+4,j)/36^m = C*m^(-alpha) * (1+sum_(r=1)^K c_(j,r)/m^r+O_(j,K)(m^(-K-1))).

 In particular the positive leading C follows from the exact Gaussian integral derived in PREFIX-1023. Full arbitrarily high-order remainder control is essential for finite differences; merely knowing the leading equivalent would not suffice.

3. Let g_m=Q^+_(m+4,j)/36^m. For every fixed integer k>=0, the full series (take K>k) implies

  (Delta^k g)_m = (-1)^k C (alpha)_k m^(-alpha-k) [1+O_k(1/m)],

 with Delta g_m=g_(m+1)-g_m. To see this, apply the binomial finite-difference sum termwise to the descending-power expansion, using Delta^k(m^(-beta))=(-1)^k(beta)_k m^(-beta-k)+O(m^(-beta-k-1)) and choosing the expansion order so its remainder is negligible.

4. Factor 36^(m+i+j) from row/column powers of the h-by-h Hankel matrix and apply the unimodular binomial difference transform to both its rows and columns. This changes [g_(m+i+j)] into [(Delta^(i+j)g)_m] without changing determinant. Extract the factors C*m^(-alpha/2-i) by rows and m^(-alpha/2-j) by columns (with C counted once per row); after this normalization the matrix tends entrywise to [(-1)^(i+j)(alpha)_(i+j)].

5. The sign factors (-1)^i in rows and (-1)^j in columns cancel in the determinant. The remaining rising-factorial matrix is positive definite, because (alpha)_(i+j) is the (i+j)-moment of the positive Gamma(alpha,1) density. Its determinant is exactly
 D_h(alpha)=product_(k=0)^(h-1) k!(alpha)_k.
 An elementary derivation: factor (alpha)_i from each row in ((alpha)_(i+j))=(alpha)_i (alpha+i)_j; the remaining columns are monic rising-factorial polynomials evaluated at alpha+i, so their determinant is the Vandermonde product product_(i<k)(k-i)=product_(k=0)^(h-1) k!. Therefore D_h(alpha)>0.

6. The determinant equivalent follows. The same argument applies to each of the finitely many leading principal minors of size k<=h. For sufficiently large n0 all their determinants are positive, so Sylvester's criterion gives H_h(n0,j) strictly positive definite.

## Exact finite integer experiment and identified transient sign reversal

A fresh independent stdlib Python Laurent-coefficient script constructed S^m and B_(m,j) with integer coefficient maps, combined each Cell–port fibre, then summed coefficient squares for both j=1 and a representative j=2 at n=5..18. It exactly matched PREFIX-1023's published values on n=5..11. The remaining j=3..6 have the same mass by the exact permutation symmetry of axes 2..6 in the model.

For the representative **other-axis positive port**, exact Hankel determinant signs at consecutive starts are:

- Order h=2: positive for all checked n0=5..16.
- Order h=3: negative at n0=5,6, positive at n0=7..14. In particular, det H_3(7,j)=1467655835015118265181899984 > 0.
- Order h=4: negative at n0=5..8, positive at n0=9..12. In particular, det H_4(9,j)=151417102814755883010796402464726203772201355050000 > 0.

For first-axis positive port j=1, orders h=2,3,4 are all positive across the corresponding checked starts. These are finite computations and do not claim a certified earliest permanent transition threshold. They precisely exhibit why PREFIX-1023's negative early Hankel minor is compatible with eventual fixed-order positivity.

The reproducible Python program is `PREFIX1024_R6_EVENTUAL_POSITIVE_HANKEL_CHECK.py` and its complete large-integer table is `PREFIX1024_R6_EXACT_INTEGER_RESULTS.json` in this directory. The full asymptotic determinant theorem is author-proved, not an independently reviewed Result.

## Research consequence and next question

The positive-port sequence is non-C-finite (PREFIX-1023), and its early Hankel Gram matrix can be indefinite, yet *every fixed finite Hankel order eventually becomes strictly positive*. This is a transient-to-asymptotic positivity restoration result, not an exact time-invariant finite-state closure. A useful next question is to derive an **explicit effective N_h** from quantitative higher-order torus Laplace remainder estimates or a native BRC positivity certificate, and to compare order-dependent thresholds against a time-varying Gram/jet carrier preserving future Cell–port interference.

History: PREFIX-1014/1017/1018/1021/1022/1023. Original contributor provenance: historical EM-DIRECT-FBEA5D / RA-3FB2D033BE6048D8712FF056 / MCP-45ad6d29cd534c1aad25595a72e3c532. These are historical source identifiers, not a credential, current CLAIM or research execution authorization. This portable result does not assert mathematical admission or a formal shared Result/Review. The mother objective B_fix,odd(32) in {19,20} remains open.
