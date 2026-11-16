# R223 — Exchangeable Markov source-support spectrum and exact observable reduction

Date: 2026-11-17 (Asia/Shanghai). Classification: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Native BRC EffectHistogram: NOT_EXECUTED.

## Sources, model and invariant boundary

Scientific input frozen at awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Direct antecedents: R215@71e9d86c4fea71a0ff1b2da66fe2b5656998a68b; R220@a51ddb6ed7e91842c567855bf3fbee118a6816c8; R221/R222@ef026a5e4f953c6db56efd4f411e4aa653f235b4. Current P000, ACTIVE worldview and operational rules were read separately without altering scientific pins.

Work only in the abstract paired-event observer J_(m,k,L), with m>=1 signed-direction choices, k>=1 selected nonneutral sources, tail depth L>=1, and neutral source 0. At n>=L, the ideal-cardinality readout is F_n=T_|S_n|, where S_n is the set of selected source labels seen by time n. R215 supplies

  W_r = r! m^L sum_(j=0)^min(r,L) Stirling2(L+1,j+1) > 0,
  T_r = sum_(j=r)^k binom(k-r,j-r) W_j.

R221 gives the Boolean zeta survival representation

  E[F_n] = sum_(U subseteq [k]) W_|U| Pr(S_n subseteq U).             (1)

The source-label Markov marginal is stationary uniform and exchangeable:

  N=k+1,  pi=(1/N,...,1/N),
  P(alpha)=alpha I_N + (1-alpha) 11^T/N,
  -1/k <= alpha <= 1.                                              (2)

The range is necessary and sufficient for all transition entries to be nonnegative: the diagonal is (1+k alpha)/N, off-diagonal (1-alpha)/N, and every row sums to 1. The full spectrum is 1 (simple) and alpha (multiplicity k). Direction choices are arbitrary conditional on retaining the source-label marginal. The ideal observer is not the full native X6, 21-bit affine action or typed BRC carrier.

## Theorem A — Explicit positive observable spectrum for the exchangeable Markov family

Define for r=0,...,k

  lambda_r = alpha + (1-alpha)(r+1)/N,
  A_r = binom(k,r) W_r (r+1)/N > 0.

For every n>=L,

  E[F_n] = sum_(r=0)^k A_r lambda_r^(n-1).                          (A)

All lambda_r lie in [0,1]. In particular the ideal expectation is completely monotone:

  (-1)^j Delta^j E[F_n]
       = sum_r A_r lambda_r^(n-1)(1-lambda_r)^j >= 0                (B)

for all n>=L, j>=0.

Proof. For a subset U containing r selected labels, restrict P to D_U={0} union U of size s=r+1. The killed matrix is P_U=alpha I_s + (1-alpha)11^T/N. Its all-ones eigenvector has eigenvalue lambda_r. Since pi_U=1_s^T/N, the exact probability that all n sources remain inside D_U equals pi_U P_U^(n-1)1_s=(s/N)lambda_r^(n-1). There are binom(k,r) possible U; group (1) by r to get (A). At the allowed endpoints, lambda_0=(1+k alpha)/N>=0, lambda_k=1, and lambda_(r+1)-lambda_r=(1-alpha)/N>=0. The finite-difference formula holds termwise; lambda=0 at n=1 uses 0^0=1. QED.

## Theorem B — Exact minimal linear recurrence

For -1/k<alpha<1, the k+1 lambda_r are pairwise distinct and strictly positive. All A_r are positive. Therefore the exact minimal recurrence polynomial for the tail sequence n>=L is

  chi(x)=product_(r=0)^k (x-lambda_r),

with degree k+1. For rational alpha the (k+1)x(k+1) Hankel matrix H_(ij)=E[F_(L+i+j)] has rank k+1 over Q.

Proof. Put V_(i,r)=lambda_r^i. Then H=V diag(A_r lambda_r^(L-1)) V^T; the Vandermonde determinant is nonzero, as are all diagonal entries. A recurrence of degree d forces Hankel rank <=d. The displayed polynomial annihilates each exponential, proving the matching bound. At alpha=-1/k, lambda_0=0 yields a single nonzero impulse at n=1. Consequently the minimal degree is k+1 when L=1 and k when L>=2. At alpha=1, every lambda=1, giving a nonzero constant and degree 1. For k=0, the neutral-only observer likewise has degree 1. QED.

## Corollary C — Negative full-kernel eigenvalues compatible with complete monotonicity

Take (m,k,L,alpha)=(1,2,1,-1/4). Then

  P = [[1/6,5/12,5/12],
       [5/12,1/6,5/12],
       [5/12,5/12,1/6]]

is symmetric and irreducible, with stationary uniform pi and eigenvalues {1,-1/4,-1/4}. Its exact ideal readout is

  E[F_n]=4+(1/3)(1/6)^(n-1)+(8/3)(7/12)^(n-1)  for n>=1.

It has minimal recurrence order 3 and all alternating differences nonnegative. Hence the full-chain nonnegative spectrum in R222 is a sufficient but not necessary hypothesis for this particular support-ideal observation. The negative modes are unobservable along the restricted all-ones input/output used in (1).

## Corollary D — Universal Markov recurrence upper bound 256 -> 250 for k=6

For arbitrary stochastic P and arbitrary initial probability row pi, R221 constructs a block realization of dimension D=sum_(U subseteq [k])(|U|+1)=(k+2)2^(k-1). Its U=[k] block contributes exactly pi P^(n-1)1=1 at every n>=1 and therefore needs one scalar constant mode, not a (k+1)-dimensional block. The observable recurrence consequently has degree at most D-k; for k=6, at most 250. This is an upper bound, not a generic minimality result. The exchangeable interior family realizes the exact degree 7.

## Native-size arithmetic example

At (m,k,L,alpha)=(12,6,2,1/4):

  W=[144,576,1440,4320,17280,86400,518400],
  lambda_r=(10+3r)/28 (r=0,...,6),
  A_r=binom(6,r)W_r(r+1)/7,
  chi(x)=product_(r=0)^6(x-(10+3r)/28).

The seven eigenvalues are distinct and positive, so the minimal recurrence order is 7. Exact rational calculation gives E[F_12]=149648228779334204799/226775649501184 and limit 518400.

## Exact validation and remaining work

The companion reference Python program uses only Fraction and integer combinatorics. It reported PASS on 90 exact parameter cases (k=1..3, m=1/12, L=1..3, alpha=0,1/4,-1/(2k),-1/k,1), 1530 exact dynamic-programming/spectral comparisons, 90 Hankel ranks, 1260 recurrence identities and 2250 alternating difference inequalities. It also checks 7x7 Hankel rank for the six-source case. See R223_verification.json.

Independent mathematical review: NOT_REVIEWED. Formal Task CLAIM / Result / Foundation admission: NONE. The physical BRC EffectHistogram, exact ports, branch provenance, phase/sign, multiplicity, rational mass and cross-moments were not operated on in this experiment.

Next: (1) calculate controllable/observable minimal order for generic rational P, checking whether the upper bound 250 is attained; (2) characterize observable complete monotonicity beyond equilibrium exchangeability; (3) integrate this query-only spectral projection with the full typed native EffectHistogram without replacing its richer carrier.