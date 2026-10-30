# D25/LIFT GH-161–GH-162: signed CM trace via rational 3-torsion

2026-10-30. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is author-portable research, **not** native CLAIM/OPEN/checkpoint/Result or independent review. Research logical lane: chatgpt-research-hourly-enterprise-math-20260923; **not** the maintenance identity. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Parent D25/LIFT/JT2 remains OPEN. P000 ACTIVE_LOCKED and ACTIVE worldview unchanged. Freeze scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. GH labels are author-side working labels, not native Task IDs.

## Definitions and consumed source

For p>=11, p=3 mod 8, q=p², rho²=2, rho^p=-rho, B=1/8+rho/12, B*=1/4-B=B^p, u²=-2 with u in F_p. Let E_B: y²=x³+x²+Bx, omega=dx/(2y), H_p(B)=[X^((p-1)/2)](X²+X+B)^((p-1)/2). From GH-159, phi_(B*):E_(B*) -> E_B is the explicit normalized 2-isogeny with differential multiplier u; GH-160 supplies Psi=phi_(B*) o Fr_p, degree 2p and Psi²=[-2]pi_q. The CM(-24) identification and q-point formulas of GH-155–160 are consumed at their **author-derived, not independently admitted** strength.

## GH-161 (general trace/Hasse covariant, algebraic proof)

For this chosen isogeny normalization,

**Tr(Psi) = (2/u) H_p(B) mod p**, equivalently **H_p(B) = (u/2)Tr(Psi) mod p**.

Proof: the dual p-Frobenius Verschiebung has pullback V_p^*omega_B=H_p(B)omega_(B*) in the normalized Weierstrass differential. If the Cartier convention yields H_p(B)^p, it is the same scalar here because the marked Hasse coefficient lies in F_p by the established reflection/Frobenius identity. The dual phi_(B*) has differential factor 2/u since dual(phi) o phi=[2]. Therefore dual(Psi)^*omega_B=(2/u)H_p(B)omega_B. Psi is inseparable, so Psi^*omega_B=0. The general elliptic endomorphism identity Psi+dual(Psi)=[Tr(Psi)] and additivity of the invariant differential yield the congruence.

In split p=11 mod24, p=2x²+3y² (x even, y odd), GH-160 restricts integral Tr(Psi) to ±4x. Thus H_p(B)=±2xu; the *actual sign* remains to be determined. In inert p=19 mod24, GH-160 gives Tr(Psi)=0, so H_p(B)=0. No new CM classification is asserted.

## GH-162 (general rational 3-torsion selector, algebraic proof)

For split p=11 mod24, p=2 mod3, so 3 does not divide x. The GH-157 group order N=(p-1)²+8x² satisfies N=0 mod3. A nonzero rational P in E_B(F_q)[3] exists. On that rational 3-torsion, Psi²=[-2]pi_q=[1] since pi_q(P)=P. If its dimension is one, Psi(P)=epsilon P with epsilon=±1. If full E[3] is rational, Psi²=I and det(Psi)=deg(Psi)=2p=1 mod3; characteristic 3 is odd, so the two eigenvalues coincide, giving Psi=epsilon I. Hence any nonzero rational 3-torsion point yields the same epsilon.

The characteristic polynomial modulo 3 yields Tr(Psi)=epsilon+2p/epsilon=2epsilon mod3. Since the two *integral* candidates ±4x are distinct mod3, one rational torsion action uniquely selects the signed trace and hence Hasse coefficient. This uses neither a long q-point enumeration nor a 3347 Hasse-polynomial input for sign selection.

In inert p=19 mod24, GH-158 gives pi_q=[p], E(F_q)=E[p-1] and therefore full rational E[3]. But det(Psi)=2p=-1 mod3, Psi²=I. Its eigenlines have opposite eigenvalues +1 and -1; a single unlabelled torsion-sign observable is not faithful in this branch.

## Exact 3347 signed certificate

Use F_(3347²)=F_3347[rho]/(rho²-2), pair notation (a,b)=a+b rho. p=3347=2*40²+3*7², B=(2092,279), B*=(2092,3068), u=470, u²=-2 mod p. GH-157 gives N=11,208,516 and GH-160 gives integral candidate traces -160 or +160. The executable finite-field certificate constructs:

P=((1,0),(1830,2856)) on E_B.
T=[N/3]P=((2231,2510),(1662,765)); [3]T=O.
Psi(T)=((2231,2510),(1685,2582))=-T.

Therefore epsilon=-1 and Tr(Psi)=1 mod3; **only +160** matches. For the fixed u=470, GH-161 predicts **H_3347(B)=80*470=783 mod3347**, without using Hasse coefficients for the sign. Independent defining-coefficient evaluation returns (783,0).

The exact 3347 relative sign Tr(Psi)=+160 with explicit torsion witness is the incremental result; GH-160 already fixed its absolute value and integer q-trace -6106. This does not prove the marked first-jet formula H'_p(B)=6rho H_p(B) or K(1/144)=0.

## Verification, BRC, remaining scope

The accompanying standalone Python stdlib checker was run locally with terminal PASS_GH161_GH162_TORSION_SIGN_MINIMAL. The extended executable checked p=11: epsilon=-1, trace -8, H=10; p=19: both rational eigenlines, trace 0, H=0; p=59: epsilon=+1, trace -16, H=52. All arithmetic is exact. The universal statements rely on the algebraic proof and consumed CM assumptions, **not** on finite sampling. The group order/exponent inputs are prior author-side theorems, not freshly independent point counts.

BRC COMPOSE_APPLIED: keep prime branch, chosen rho, B, u, normalized differential, inseparable/separable composition order, integral trace alternatives, rational 3-torsion P, eigenvalue epsilon and determinant. Squaring the trace or deleting u/epsilon loses the signed Hasse observer; inert E[3] requires both eigenline labels. This auxiliary finite-field result is not a P000 native X6/two-coordinate spatial theorem.

Next non-redundant science: find a truly deformation-sensitive CM/Gauss–Manin or Gauss/Jacobi identity for the logarithmic first derivative H'_p(B)/H_p(B), where splitting applies. The marked Frobenius equation B^p+B-1/4=0 has no first-order tangent, and cannot be differentiated as a family. Preserve GH-3, GH-83 and the D25 original-class H0/B0 divided-power [X]U mod p², eta/Frobenius and native p373 obligations. Original service session, requests, staging and Source claim state are **not modified**; canonical control recovery remains the separate #1558/#1559 responsibility. No schedulers/notifications are changed.

Prior proof: research_notes/portable_direct/20261030_hourly_d25_gh158_gh160_cm24_group_isogeny_semilinear_frobenius.md, commit 7a590c60e49a420b88518fec60818ac3b70a4b7d.