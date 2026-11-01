# D25/LIFT GH-151–GH-152: one independently counted CM anchor and exact Picard–Fuchs transport

2026-10-30. **Author-only, exact-checkable, unreviewed, not admitted, portable-only, registration pending.** Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Research logical conversation chatgpt-research-hourly-enterprise-math-20260923 (not maintenance). P000 ACTIVE_LOCKED; frozen science Source c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

## Input provenance and discriminating question

GH-148 shows that the actual reduced trace line is a degree-at-most-2m square J(W)=G(W)^2 for primes p=8m+3; 2m+1 distinct square-parameter integer traces therefore suffice for its oriented derivative. GH-149 independently counts a_3347(E_(1/8))=-114 by an ordinary prime-field Legendre sum. GH-150 proves an information-theoretic 2m+1 worst-case bound for the **generic** degree/square/signed-anchor model, expressly not for G constrained by extra equations. We now exploit a precise extra equation of the actual Hasse family. Inputs are author-side proofs, not independently reviewed foundation facts.

## GH-151. One numerical trace anchor plus a universal Picard–Fuchs equation determines the full trace line

Take p=8m+3 prime, p>=11; N=(p-1)/2; rho^2=2 in K=F_(p^2). Define

- E_B: y^2=x^3+x^2+Bx.
- H_p(B)=[X^N](X^2+X+B)^N, a polynomial over F_p.
- B(v)=1/8+rho*v, W=v^2 for v in F_p.
- Phi_p(W)=sum_(k=0)^m u_k W^k, where u_0=1 and

**u_(k+1)=4(8k+1)(8k+3)u_k/((k+1)(2k+1)) modulo p, 0<=k<m.**

These denominators are nonzero in F_p, and the next numerator vanishes at k=m, because 8m+3=p. This is the finite-polynomial avatar of the hypergeometric 2F1(1/8,3/8;1/2;128W); no infinite-series convergence or external analytic assertion is required.

**Theorem (polynomial identities).**

H_p(1/8+rho*v)=h_0 Phi_p(v^2), with h_0=H_p(1/8)=a_p(E_(1/8)) mod p.

For v in F_p, the previously established GH-147 trace identity gives

J_p(W):=a_(p^2)(E_(B(v))) mod p=t_0 Phi_p(W)^2,

where t_0=a_(p^2)(E_(1/8)) mod p=h_0^2.

**Proof.** Expanding the fixed coefficient gives H_p(B)=sum_(k=0)^floor(N/2) [N!/((N-2k)!(k!)^2)] B^k, with integral multinomial coefficients. Comparing adjacent integer coefficients yields (k+1)^2 h_(k+1)=(N-2k)(N-2k-1)h_k. Consequently

B(1-4B)H_p''+(1-8B)H_p'-(3/4)H_p=0

identically modulo p: reduce the integral-parameter Gauss equation B(1-4B)H''+[1-(6-4N)B]H'-N(N-1)H=0, using N=-1/2 mod p. GH-131's reflection H_p(1/4-B)=H_p(B), together with rho^p=-rho, implies H_p(B(v)) is an even polynomial in v with F_p coefficients and degree <=2m. Write it as G(W), deg G<=m.

Under B=1/8+rho*v and W=v^2 one has B(1-4B)=1/16-8W, dH/dB=(2v/rho)G', and d^2H/dB^2=G'+2WG'' (because rho^2=2). The differential equation becomes

**(2W-256W^2)G''+(1-384W)G'-12G=0.**

Coefficient comparison gives

(k+1)(2k+1)g_(k+1)=4(8k+1)(8k+3)g_k.

This recurrence has unique solution of degree <=m for any g_0=G(0), proving G(W)=g_0 Phi_p(W). Its single scalar normalization is independently determined from E_(1/8): Euler's criterion gives a_p(E_B)=-sum_(x in F_p)(x^3+x^2+Bx)^N modulo p, and the only exponent divisible by p-1 in that polynomial is 2N; finite-field power sums therefore give a_p(E_B)=H_p(B) modulo p. Since E_(1/8) is defined over F_p, integer Frobenius gives a_(p^2)=a_p^2-2p, hence t_0=g_0^2. Apply the GH-147 Hasse/trace relation for all v in F_p to finish.

The result replaces a sufficient 2m+1 independent *numerical* trace samples with **one** independently computed anchor plus 419 exact coefficient-transport terms at p=3347. It does **not** reduce the universal GH-150 bound for unconstrained square polynomials; the actual Picard–Fuchs equation is the new constraint. This is not an independent CM evaluation of the target parameter, because the transport still uses the existing Hasse/Picard–Fuchs family relation.

## GH-152. Unsigned anchor suffices, but the future-oriented observation loses information under v -> -v

The trace answer depends on g_0 only through t_0=g_0^2. Thus even the **unsigned** integer extension-trace anchor a_(p^2)(E_(1/8)) mod p suffices to determine J_p(W) and J_p'(W), without fixing the sign of a_p. The marked first moment, by GH-124/GH-147, satisfies S_1(B)=2H_p(B)H_p'(B) at the reflected original family. Thus

**S_1(B(v))=rho*v*J_p'(v^2).**

At v_0=1/12 and W_0=1/144,

**S_1(B_0)=(rho/12)*t_0*(Phi_p^2)'(W_0).**

The trace function is invariant under the identification v ~ -v, whereas S_1 changes sign. Hence whenever v!=0 and J_p'(v^2)!=0, forgetting the orientation is an *unsafe BRC observer quotient* for the future operation S_1. This statement concerns a finite-field marked observer, not native six-dimensional P000 dynamics.

## The 3347 certificate and precise independence boundary

Over K=F_3347[rho]/(rho^2-2), independent 3347-term prime-field point-count summation gives integer a_3347=-114. Integer a_(3347^2)=(-114)^2-2*3347=6302; t_0=6302 mod 3347=2955. Set m=418, W_0=144^(-1)=860 modulo 3347. The exact coefficient recurrence above then gives G(W_0)=783, G'(W_0)=2824, J(W_0)=588, J'(W_0)=997, and

**S_1(B_0)=(997/12)rho=362rho mod 3347.**

The same unmarked trace J(W) under reversed orientation gives -362rho=2985rho. No additional 836 large-curve integer point counts are required under the proved recurrence. The 3347 multinomial Hasse evaluation H_p(B_0)=783 is only a **dependent consistency check**, not a second independent CM special-value evaluation.

This is field extension p^2, **not** a native divided-power / [X]U modulo p^2 certificate. It does not prove R_3347(9)=0 independently, GH-83, GH-3, or the required original-class p=373 Frobenius/eta comparison.

## Executed checks, source and next action

The exact executed Python-stdlib checker is d25_gh151_gh152_one_cm_anchor_picard_fuchs_check.py; its remote blob was verified equal to the executed 4346-byte program (Git blob 339996b919f7398d3cfba25f0b0bd74409b5ef1e). Its actual clean exit code is zero and terminal PASS_GH151_GH152_ONE_CM_ANCHOR_AND_ORIENTED_JET_EXACT. Direct p^2-field character-moment sums, independent prime-field trace sums and multinomial Hasse coefficients agree at p=11,19,43,59,67,83,107. For p3347, independent a_p counting, coefficient equation, signed/unsigned normalization and dependent Hasse spot-check all pass; no 3347^2 field enumeration was repeated.

Control is separate from this mathematics: Gateway 0.6.11 status reports research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5 and Source CODE_REVIEW_REQUIRED; the exact D25 continuation read this run returned INVALID_ARGUMENT / CONTROL_QUOTA. No native CLAIM, OPEN, Source checkpoint, Result or review is claimed; no old session/staging or maintenance identity was touched. Control support owner is enterprise-math #1558; exact native p373 benchmark support remains #1559.

**Parent OPEN; author-side preservation only.** Do not repeat GH-150's generic 836-point witness, any 3347^2 full enumeration or the earlier 836 Hasse-generated mock-independent traces. Next portable scientific question: find a genuinely independent Gauss/Jacobi/CM or p-adic special-value evaluation of the finite hypergeometric Phi_3347(1/144) and its first derivative at 8/9, then check the source-original definition of R_3347(9), without promoting Hasse transport to independent CM evidence. Native D25 still needs original-class H0/B0 divided-power module, [X]U mod p^2, semilinear Frobenius, eta, and real p373 experiment.
