# D25 216/2304 Heun candidate: a fixed-band obstruction and exact p-adic non-transfer certificate (2026-11-07)

Status: AUTHOR_SIDE_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED.
Research logical lane: chatgpt-research-onhour-enterprise-math-20260923 (distinct from CONTROL_PLANE_MAINTENANCE).
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## Mother objective and consumed frontier

The frozen LIFT target is Delta_p=R_p modulo p for all primes p congruent 13 or 19 modulo 24, conditionally equivalent by the existing accepted bridge to W_p=p modulo p^3. The author-side fourth-digit conjecture H is 2V_p-W_p-p*(-3/p)=0 modulo p^4. The previously proved exact fourth-digit tail decomposition and its low-window residual C_A,J_A,K_B,Wilson law are consumed from 20261107_onhour_d25_p4_signed_tail_lift.md, not repeated here. This note supplies a new choice of research route and two exact mathematical results.

Let a_k = (1/2)_k(1/3)_k(2/3)_k / ((k!)^3 2^k) = binom(2k,k)^2 binom(3k,k)/216^k.
Let b_k = (1/4)_k(1/2)_k(3/4)_k / ((k!)^3 9^k) = binom(2k,k)^2 binom(4k,2k)/2304^k.
Set A(z)=sum a_k z^k, B(z)=sum b_k z^k. The unweighted periods below are A(1), B(1), which converge absolutely; the frozen weighted streams have factors (6k+1) and (8k+1).

## Theorem 1 (proved): no p-independent fixed-band rational-index gauge

There is no fixed finite J subset of Z and family r_j(k) in Q(k) for which b_k=sum_{j in J} r_j(k)a_{k+j} holds for all sufficiently large integers k with defined terms. The same is true for the weighted sequences (6k+1)a_k and (8k+1)b_k.

Proof. Each fixed-shift quotient a_{k+j}/a_k is a rational function of k because a_{k+1}/a_k belongs to Q(k). The claimed identity would make R(k)=b_k/a_k a nonzero rational function. But every such rational function has R(k+1)/R(k) tending to 1, whereas from the factorial term ratios a_{k+1}/a_k tends to 1/2 and b_{k+1}/b_k tends to 1/9; thus R(k+1)/R(k) tends to 2/9, contradiction. Multiplication by the two linear weights does not change those limits. QED.

This eliminates exactly the fixed-width, p-independent rational-contiguous termwise route. It does not eliminate algebraic argument pullbacks, nonlocal summation, p-dependent WZ certificates or the conjectured mod-p^4 sum congruence.

## Analytic candidate (not a theorem): certified rational enclosure

Let A_inf=sum_{k>=0}a_k, B_inf=sum_{k>=0}b_k. A possible Heun/modular period relation is A_inf ?= (3 sqrt(2)/4) B_inf. The attached exact Python checker rigorously establishes only

| A_inf - (3 sqrt(2)/4) B_inf | < 2 * 10^(-110),

by rational geometric upper bounds after 351 terms of A and 121 terms of B and the integer-isqrt bracketing of sqrt(2) to 110 decimal places. This tiny interval is *not* an equality proof. Clausen's identity writes these 3F2's as squares of Gauss 2F1(1/6,1/3;1;1/2) and 2F1(1/8,3/8;1;1/9). Appendix A, pp.34-35, of Bostan et al., "Ising n-fold integrals as diagonals of rational functions and integrality of series expansions", displays a HeunG function by algebraic 2F1 pullbacks involving these parameter families. The source motivates, but does not supply here, the exact argument-/derivative-matching identity needed for the two special values.

## Theorem 2 (proved): p=19 is an exact non-transfer counterexample

For p>3 let A_p=sum_{0<=k<p}a_k and B_p=sum_{0<=k<p}b_k, reduced modulo p^3. Two independent exact methods (binomial coefficients and recurrence ratios) give:

p=19: A_19=2888=8*19^2; B_19=2527=7*19^2 (mod 19^3=6859).
p=373: A_373=9878159=71*373^2; B_373=28243187=203*373^2 (mod 373^3=51895117).

The tempting scalar p-adic truncation A_19=(3 sqrt(2)/4)B_19 modulo 19^3 in the unramified quadratic extension is FALSE. Indeed 2^9=-1 (mod 19), so sqrt(2) is not in F_19. Dividing the asserted congruence by 19^2 and reducing mod 19 would force 8=(21/4)sqrt(2) in F_(19^2), contradicted by the basis 1,sqrt(2) over F_19 and 21/4 nonzero modulo 19. This one-prime certificate is conclusive for this scalar-transfer claim, independently of whether the analytic period candidate is eventually established.

Scientific consequence: an analytic value transformation must carry its differentiated finite-cutoff/Frobenius and signed valuation data before it can support the frozen weighted supercongruence. BRC observation tracks the two source streams independently by (source,k,cutoff,valuation,derivative/Wilson carry), and only then makes a typed residual readout; no native X6 semantic identification is asserted.

## Next exact action and Source recovery

Resolve concrete Heun/2F1 argument pullbacks at 1/2 and 1/9, including derivatives, then derive an explicit finite-index mod-p^4 correction that matches the earlier low-window identity involving C_A,J_A,K_B,omega_p. Test any candidate first at p=11 (known p^5 counterexample), p=19 and p=373. The p=373 native H0/B0, Frobenius, divided-power, Hesse-kappa, independently reproduced experiment remains a separate unexecuted benchmark, GitHub issue #1559.

Source recovery exact original request: onhour11-20261106-1400-exact-research-lane-continuation; state UNKNOWN_NOT_RESENT. 2026-11-07 04:01 UTC Site: CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false; em_status and original receipt: BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Session/CLAIM/run not verified. REGISTER_PENDING / SYNC_DEBT. Required operator path: dedicated Site-bound backend client/version/secure credential, then read original Source receipt before role-bound write. This is an author-side research note, not a Source Result.

Source literature: Guo & Zudilin, A q-microscope for supercongruences, Adv. Math. 346 (2019) 329-358, arXiv:1803.01830; Bostan et al. (above), Appendix A.