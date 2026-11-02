# D25 original-216: precise two-state spectral obstruction and basis-preserving kernel repair

2026-11-03, TASK_RESEARCH author-side. Frozen task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, TP2-B6F4FC938FF94941C1B7, science pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane chatgpt-research-onhour-enterprise-math-20260923 (not maintenance). Status: PROVED IN THE DECLARED TWO-STATE TRANSFER CLASS / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. Last own frontier 461e048433fdbb68e3ab8adac70d66ae18f378ab; consume its recurrence and terminal p^4 lemma, without re-proving them.

## Exact statement for all primes p >= 5

Keep the original coefficients and signed original observer:

b_k = binom(2k,k)^2 binom(3k,k)/216^k,
w_k = (6k+1)b_k,
S_n = sum(k=0..n) w_k, S_-1=0.

The exact ratio b_(k+1)/b_k = rho(k) = (2k+1)(3k+1)(3k+2)/(36(k+1)^3). In the fixed original coefficient/accumulator basis v_(k-1)=(S_(k-1),b_k)^T, use transition

T_k = [[1,6k+1],[0,rho(k)]], 0<=k<=p-2.

Every denominator is a p-unit in that range. The ordered transfer T_(p-2)...T_0 is EXACTLY the triangular matrix

T = [[1,s],[0,b]],  s=S_(p-2), b=b_(p-1).                         (1)

The inherited original-factorial endpoint theorem proves b=-p^3 (mod p^4), hence b=0 (mod p^3). In both R_e=Z/p^eZ for e=3,4, 1-b is invertible. Define the explicit gauge

P_s = [[1,-s/(1-b)],[0,1]].

Direct multiplication yields

T = P_s diag(1,b) P_s^{-1}.                                      (2)

Consequently, for fixed p and this original coefficient direction, the entire similarity class and all its similarity-invariant functions are independent of the signed accumulated observer s. Mod p^3 every such matrix is a rank-one projector conjugate to diag(1,0), with characteristic polynomial X(X-1), trace 1, determinant 0, T^2=T. Mod p^4 the eigenvalues are 1 and -p^3, again with no signed observer digit. An unanchored characteristic-polynomial/spectrum/similarity-only CM intertwiner cannot decide the original D25 second-carry congruence. The scope of this obstruction is this particular two-state transfer and unrestricted change of basis; it does not rule out CM relations retaining the original basis or the separate native H0/B0 model.

## Explicit counter-control

Keep b_k and rho(k) fixed, replace the top-right original weight by lambda*(6k+1) for lambda=0 or 1. Formula (2) shows identical similarity data. At the in-domain target prime p=13, direct exact arithmetic gives original W(12)=13 (mod 13^3=2197) for lambda=1, versus W(12)=0 for lambda=0. Thus transfer similarity data alone cannot imply the signed D25 value. This is a counterexample to the specified proof mechanism only; lambda=0 is a labelled control with a changed observer.

## Constructive retained observer: based kernel chart

In the original fixed basis, T mod p^3 has image spanned by (1,0) and kernel spanned by (-s,1). With the y=1 chart, W(p-1)=s (mod p^3), because the original endpoint b_(p-1) has valuation 3. Thus for primes p=13,19 (mod24),

W(p-1)=p (mod p^3)  <=>  ker(T mod p^3)=span((-p,1)) IN THE ORIGINAL BASIS.   (3)

A basis-aware CM or WZ proof must transport the signed normalized kernel chart, not just the basis-free eigenvalues. At p^4 the second eigenvector is (-s/(1-b),1), and its mod p^3 chart is (-s,1). The original signed 5p^3 terminal correction is still needed at p^4. This repair retains the index, integer valuation, observer and allowed future operation, as required by BRC.

The previously established finite Clausen/Gauss source formula supplies an independent original-basis readout:
W = G(1/2)^2 + 6G(1/2)G'(1/2) + p^2 E (mod p^3),
where G(1/2)=pA and D=G'(1/2), hence the chart is
-s = -6pAD-p^2(A^2+E) (mod p^3).
The accepted D24 first digit gives 6AD=1 (mod p); the remaining uniform second digit is exactly
(6AD-1)/p + (A mod p)^2 + E = 0 (mod p).
Equations (2)-(3) identify why the spectrum alone cannot supply this missing signed scalar; they do not prove the all-prime cancellation.

## Executed exact evidence

Standard-library checker d25_two_state_spectral_scope_20261103.py ran on nine primes p=5,7,13,19,37,43,109,181,373. It performed original modular adjacent-ratio accumulation mod p^4 and a structurally independent direct-binomial calculation of b_(p-1), checked b=-p^3, endpoint correction 5p^3, the kernel chart, rank-one projector, original signed full W, and the zero-weight control. All assertions passed. Examples:
- p=13: original W(12) mod 2197 = 13, normalized kernel chart x=-13=2184, zero-weight control = 0.
- p=19: original W(18) mod 6859 = 19, chart x=6840.
- p=373: original W(372) mod 51,895,117 = 373, chart x=51,894,744; full W mod 373^4 = 11,832,087,049; b_(372) mod 373^4 = 19,304,983,524; signed terminal difference = 259,475,585 = 5*373^3.
- p=5 is outside frozen residue classes and yields original W(4)=-5 mod 125, confirming the necessity of retaining the prime-class input.
Finite tests check the formula and sample values; the theorem-level transfer obstruction follows from (1)-(2) for all declared primes, not from enumeration.

## Actionable next unit and separate native gap

Seek an explicit p-adic CM-normalized map on the *original coefficient/accumulator basis* preserving the normalized y=1 kernel coordinate mod p^3, including its source, sign, p-unit denominator and eta. Falsify/validate a candidate at p=13,19,373 before an all-prime claim. A parameterized finite WZ approach remains a separate valid route. The original all-prime Delta_p-R_p=0 and second-carry identity remain OPEN.

The same-original-class native p=373 H0/B0 divided-power [X]U mod139129, rank, semilinear Frobenius, eta normalization, odd signed Green/Hesse/kappa and independent replay remain NOT_EXECUTED / PENDING_OWNER at Enterprise Math #1559. Ordinary scalar transfer does not satisfy that native benchmark.

Native Source authority was not granted in this Sites client (gateway 0.6.11; research_authority_granted=false). Own recovery bridge issue awdawmip/kimi-query-bridge#6632 is a historical read-only projection; original dispatch request research-onhour-20261031-0205-dispatch-r15 at #6633 definitively FAILED UPSTREAM_CODE_REVIEW_REQUIRED. No new request, session, CLAIM, run, native checkpoint, Research Activity, Result, review, admission or maintenance identity. Earlier neutral staging remains isolated. This document is GitHub author-side evidence only. No scheduler changes.
