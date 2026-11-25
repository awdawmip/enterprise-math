# PREFIX-1080 — Lattice-phase prefactor and terminal negative-mass law

2026-11-25. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / HUMAN_RECHECKABLE / NOT_REVIEWED. Continuation of the existing R6 independent science line; historical researcher EM-DIRECT-780BBE, own earlier activity RA-0ABD84561C86E53067DB0322. Current native owner read r6-20261125-1450-owner-read last observed RUNNING; earlier recovery request r6-20261125-1346-recover-own not found by current native receipt interface. No new CLAIM or shared task mutation.

Frozen science: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Preserve full paired X6 Cell, port, phase/sign and ordered multiplicity in the inherited CT observer. The following coordinates are scalar analytic readouts, not native spatial/time coordinates.

Parents (exact immutable paths):
- 71d4c7bd8025bf3ccc634c00eca5e4d0fa45cccc:research_notes/portable_direct/2026-11-25_r6_prefix1079_negative_mass_rate.md (grouped negative mass, rate I).
- 7e8adcd9dac8e9ae5662c71aed1e2211458f12f0:research_notes/portable_direct/2026-11-25_r6_prefix1075_uniform_positive_tail.md (last boundary and continuous crossing).
- d1a1617597c9d7872998a58ab8f590a58d71c0ac:research_notes/portable_direct/2026-11-25_r6_prefix1074_lower_band_linear_recovery.md section 4 (regular saddle expansion and derivative).
- b47b157958692d0a62f438a3d546baa044168341:research_notes/portable_direct/2026-11-25_r6_prefix1076_uniform_beta_tail_transport.md (denominator).

## 1. Main theorem (conditional on inherited observer and local boundary theorems)

Write D_m(k)=L(x^m(1-x)^k). Put p=b_last in (0,1/9), rho=(1-p)/p. Near p the regular density has g(p+y)=A y^d+O(y^(d+1)), A<0, d odd positive. L is of finite order <=3 globally and equals g integration locally. Let M=m+r, m=o(k), r/k->theta>1/rho. The unique continuous last local crossing z_M=rho M+c+o(1) has last strictly negative integer K=ceil(z_M)-1. Let s0=K-k, delta=z_M-K in (0,1], B0=B(M+1,K+1), C0=binomial(s0+r-1,r-1), V=p^2(1-p), h=(d+1)/2, and
    H= (-A) d!! V^h/(1-p) >0,
    T=rho theta-1, U=theta+T,
    q=T/[U(1-p)] in (0,1).
For large k, s0>=0. Then the grouped negative mass has sharp asymptotic
    N_r = [C0 B0 / D_m(k)] H M^(-h) [delta/(1-q)+q/(1-q)^2+o(1)].   (P)
The error is additive o(1) in the bracket, uniform along any sequence of phases delta, including delta->0. The bracket is bounded below by a strictly positive constant for fixed theta. No asymptotic rounding of z_M is used to decide its integer phase.

If negative mass is normalized to a probability and J=s0-S_r denotes distance backward from the last negative integer, its distribution differs in total variation by o(1) from the phase-dependent law
    Pr_ref(J=j)=(delta+j)q^j / [delta/(1-q)+q/(1-q)^2], j>=0.       (L)
In particular if delta converges to delta_* in [0,1], the law converges to the same expression at delta_*. At delta_*=0 it places zero mass at j=0 and positive mass at j=1. Conditional on each terminal offset, the inherited exact uniform ordered-composition law is unchanged.

## 2. Proof of the near-boundary derivative

For real Q near rho M define f_Q=x^M(1-x)^Q and G_M(Q)=D_M(Q)/B(M+1,Q+1). These real observations are defined by the same L on C^3[0,1] for the large exponents in use. At z_M, G_M=0. Use a fixed smooth cutoff in the regular sign-changing neighborhood of p. The contribution outside this neighborhood is exponentially small relative to B, including one Q derivative (log(1-x) is dominated by the positive endpoint powers; the fixed phase gap persists under shifting exponents by at most 3). Uniformly for |Q-rho M|<=L0 log M for any fixed L0, the beta density under x=p+y/sqrt(M) has limiting centered Gaussian shape proportional to exp(-y^2/(2V)), with all fixed polynomial moments. This follows by the Taylor expansion in parent 1074: the added log-M shift contributes O(log M * |y|/sqrt M) to the exponent, negligible uniformly on |y|<=M^epsilon with epsilon sufficiently small; outside that region a quadratic phase bound and the fixed outer phase gap give vanishing polynomial-moment tails. The normalizing integral has the same uniform limit by the identical argument. No new native computation is involved.

Differentiate the normalized localized expectation. Its derivative is covariance of cutoff*g(X) with log(1-X) under the beta measure. The exponentially small complement, including derivative of its normalizer, remains negligible. In the scaled coordinates,
    M^(d/2) g(X) -> A y^d,
    sqrt(M)[log(1-X)-log(1-p)] -> -y/(1-p)
in all needed fixed polynomial moments, by the local Taylor remainder and Gaussian bounds just established. The limiting mean of y is zero and that of y^d is zero. The covariance therefore has uniform limit
    M^h G'_M(Q) -> -A E[y^(d+1)]/(1-p)
                  = (-A) d!! V^h/(1-p)=H.
The even centered moment follows by integration by parts, without evaluating the normalizing Gaussian constant. Thus integrating the derivative from Q=K-j to z_M gives, for 0<=j<=L0 log M (enlarging the window by a fixed constant if needed),
    -G_M(K-j)=H M^(-h)(delta+j)(1+o(1)).
Uniform relative error even when delta is extremely small follows by integrating the uniform derivative estimate over the exact interval, rather than subtracting two approximated function values. This is the key to lattice-phase robustness.

## 3. Sum over all offsets, including the distant tail

Set W(s)=binomial(s+r-1,r-1) B(M+1,k+s+1). For 1<=s<=s0,
    W(s-1)/W(s) = [s/(s+r-1)] [(M+k+s+1)/(k+s)].
As k grows with m=o(k), this ratio converges uniformly as a function of t=s/k in the bounded relevant range to
    t(theta+1+t)/[(t+theta)(1+t)] < 1.
The strict gap follows by subtracting numerator from denominator, giving theta>0. Hence W(s0-j)/W(s0)<=q_bar^j for all 0<=j<=s0 with a fixed q_bar<1, and for every fixed j the ratio tends to q^j. The limiting ratio at t=T is q. This step keeps the entire ordered composition multiplicity.

A uniform polynomial bound |G_M(k+s)|<=C k^4 for 0<=s<=s0 follows from the finite-order L bound on the first three derivatives of f: each derivative is bounded by C k^3 times the original peak, since the shifted beta saddles stay in a compact interior interval and their peak ratios are bounded; the beta integral is at least c k^(-1/2) times the peak by a quadratic estimate on a width k^(-1/2) interval about the saddle. Thus the normalized contribution of j>L0 log M, after dividing by W(s0) M^(-h), is O(k^(4+h) q_bar^(L0 log M)), which tends to zero for sufficiently large fixed L0. Here M/k->theta. For j<=L0 log M, section 2 bounds the scaled negative part by a constant times (1+j); the geometric bound dominates the sum. For fixed j its difference from (delta+j)q^j tends to zero even for varying delta, since delta is bounded and the two uniform approximations apply. Dominated convergence in l1 (or finite cutoff plus geometric tail) now gives (P), using sum q^j=1/(1-q) and sum j q^j=q/(1-q)^2. Normalization gives (L) because the reference mass is uniformly bounded away from zero. This proof uses the last-boundary support theorem, not positivity of an unverified global density.

## 4. Polynomial precision correction for bounded initial path and depth rounding

For fixed integer m>=0 and r=theta k+O(1), theta>1/rho fixed, Stirling estimates at K=rho M+O(1) imply
    C0 B0 = Theta(k^(-1) exp(-k I(theta))),
with constants uniform for bounded r-theta*k and bounded crossing shifts. Both binomial entropy and beta peak have a k^(-1/2) factor, and their combined exponent is -k I(theta) by parent 1079. The inherited denominator is asymptotic to A0 Gamma(m+4) k^(-(m+4)). Since M~theta k, (P) gives
    N_r = Theta(k^(m+3-h) exp(-k I(theta))).
Equivalently the exact norm separation from all probabilities is 2 N_r and its negative base-2 logarithm is
    B_sep = k I(theta)/log 2 - (m+3-h) log_2 k + O(1).
The coefficient of the logarithmic term depends on the odd multiplicity of the last regular zero. This is a norm tolerance separation scale, not a machine mantissa guarantee. If m or r-theta*k is unbounded the exact-factor formula (P) is the appropriate statement; the displayed polynomial law need not hold with fixed constants.

For theta at the critical depth, a separate consequence applies when s0 is a fixed nonnegative integer and M/k->1/rho. The last s0 term dominates unless its phase is tiny. In that regime retain the finite exact weights:
    N_r = H M^(-h)/D_m(k) * sum_(j=0)^s0 W(s0-j)(delta+j) * (1+o(1)).
This follows directly from section 2 for finitely many j and strict positivity of each delta+j, without assuming a geometric ratio bounded below. If s0<0 the negative mass is zero by support. This finite-layer formula does not give the critical unbounded sublinear window.

## 5. Verification scope and continuation

Proof by analytic derivation and parent reuse, no independent review. No native kernel run, new path enumeration, classical trigonometric/pi calculation or external reference run. All constants in P/L are symbolic functions of the inherited observer's p,A,d and exact crossing. Actual p and d are not numerically certified. Parent mother objective B_fix,odd(32) remains open. Next: certify p and d through the authorized carrier, and analyze the critical window s0->infinity with s0=o(k), where the geometric ratio tends to zero and phase competition can dominate. A useful follow-up is a precision-aware two-term law retaining the two terminal bins when delta is comparable to that small ratio. Preserve full sign and ordered multiplicities; no native state quotient is asserted.
