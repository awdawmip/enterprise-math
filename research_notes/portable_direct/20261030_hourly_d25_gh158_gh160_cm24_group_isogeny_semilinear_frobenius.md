# D25/LIFT GH-158–GH-160: CM(-24) group invariants, conjugating 2-isogeny, and semilinear Frobenius square

2026-10-30. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Research lane chatgpt-research-hourly-enterprise-math-20260923; do not use CONTROL_PLANE_MAINTENANCE identity. D25/LIFT/JT2 OPEN. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / publication TP2-B6F4FC938FF94941C1B7. P000 ACTIVE_LOCKED, ACTIVE worldview and scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3 retained. Working GH labels are not native task IDs.

## Exact assumptions

Let p≥11 be prime, p≡3 (mod 8), q=p², rho²=2 over F_q, B+=1/8+rho/12, B−=1/4−B+=B+^p. E_B is y²=x³+x²+Bx, and B(1−4B)=1/144. GH-155 author-side CM identification gives j(E_B) a root of the Hilbert class polynomial of discriminant −24, with CM maximal order O_K=Z[s], s²=−6; use the classical Deuring ordinary/inert reduction classification. GH-156 already proved inert p≡19 (mod 24) has integer q-trace 2p. The new GH-160 supplies an alternative geometric derivation of GH-157's split trace; it still depends on GH-155 CM identification rather than an independent CM review.

## GH-159: normalized 2-isogeny

For p≡3 (mod 8), (−2/p)=1. Choose u∈F_p with u²=−2. Put B*=1/4−B. For affine x≠0 define X=x+1+B/x, Y=y(1−B/x²) and

  phi_B(x,y) = (−X/2, −Y/(2u)) : E_B → E_(B*).

Direct substitution gives Y²=X³−2X²+(1−4B)X, hence the displayed normalization maps to E_(B*). Vélu's degree-two kernel is {O,(0,0)}, with canonical extension over the exceptional affine point. The invariant-differential multiplier is u: phi_B^*(dx*/2y*)=u dx/2y. The two nonzero abscissas alpha,beta of x²+x+B=0 have X=0 and are mapped to (0,0). Thus phi_(B*)∘phi_B kills E[2] and is separable degree 4, so equals ±[2]. Its differential multiplier is u²=−2, fixing the sign:

  phi_(B*) ∘ phi_B = [−2].                                    (1)

At the original marked B+, B*=B+^p, so this isogeny connects the two Frobenius-conjugate CM marks.

## GH-160: a degree-2p Frobenius-twisted endomorphism

Let Fr_p:E_(B+)→E_(B−) be relative p-Frobenius and Psi=phi_(B−)∘Fr_p:E_(B+)→E_(B+). It has degree 2p. Since u belongs to F_p, the defining maps conjugate under Frobenius exactly, so (1) implies an equality of actual algebraic morphisms:

  Psi²=[−2]∘pi_q,                                               (2)

where pi_q is q-Frobenius. This is a precise auxiliary semilinear Frobenius-square relation, not the formally required D25 native H0/B0 divided-power/Frobenius experiment.

For p≡11 (mod 24), E is ordinary and its geometric endomorphism ring is the maximal O_K by CM specialization. Consequently Psi=A+Cs (A,C integers), Norm(Psi)=A²+6C²=deg Psi=2p. Parity forces A=2x, C=y, x even, y odd, x,y nonzero, and p=2x²+3y². Relation (2) gives pi_q=−Psi²/2 and therefore

  a_q(E_(B±))=Tr(pi_q)=−(A²−6C²)=6y²−4x².                   (3)

This determines the integer trace *sign* without GH-157's separate binary-form class enumeration or rational-2-torsion sign argument. Tr(Psi)=±4x remains dependent on u and the selected CM orientation; do not falsely fix that sign. For inert p≡19 (mod 24), GH-156 gives Tr(pi_q)=2p and Norm(pi_q)=p². The reduced norm of (pi_q−[p]) in the supersingular quaternion division endomorphism algebra is p²+p²−p·(2p)=0; definiteness forces pi_q=[p]. Hence (2) yields Psi²=[−2p], and the quaternionic Psi has trace 0 and norm 2p.

For p=3347=2·40²+3·7², gamma=80+7s has norm 6694=2p and gamma²=6106+1120s. Thus pi_q=−3053±560s, trace −6106, integer #E(F_(3347²))=11,208,516. This is a different author-side proof route to the previously known trace, not a new independently reviewed result.

## GH-158: full rational group, not just its order

Inert p≡19 (mod 24): pi_q=[p] implies E(F_q)=ker([p−1])=E[p−1] (p−1 prime to p), hence

  E_(B±)(F_q) ≅ Z/(p−1) × Z/(p−1).                             (4)

Split p≡11 (mod 24): write pi_q=a+bs with a=3y²−2x², b=±2xy. Put N=(a−1)²+6b²=(p−1)²+8x² and d=gcd(|a−1|,|b|). Then

  E_(B±)(F_q) ≅ Z/d × Z/(N/d).                                 (5)

Proof: E(F_q) has invariant factors n1|n2 and p∤n1, since geometric E[p] has rank≤1. For every m coprime to p, full rational E[m] is equivalent to (pi_q−1) killing E[m], i.e. to (pi_q−1)∈m End(E) by factoring through separable [m]. Since End(E)=Z[s], the last condition is exactly m|(a−1) and m|b. Thus n1 equals the largest prime-to-p divisor common to a−1,b. The estimate 0<|b|=2xy<p follows from 2x²+3y²≥2sqrt(6)xy; hence p∤d and n1=d. Total order N forces n2=N/d, with d²|N. This avoids silently assuming a prime-to-p Tate-module formula controls the p-primary part of E(F_q).

At p=3347: a=−3053, |b|=560, d=gcd(3054,560)=2, N=11,208,516. Therefore E(F_(3347²)) ≅ Z/2 × Z/5,604,258. Other examples: p=11 -> (2,66); p=19 -> (18,18); p=43 -> (42,42); p=59 -> (6,582).

## First-jet obstruction and next open science

The marked condition B^p=1/4−B holds at exactly p points B(v)=1/8+rho v, v∈F_p. Its polynomial is L(B)=B^p+B−1/4=∏_(v∈F_p)(B−1/8−rho v), with derivative L'(B)=1. For B=B0+eps h over dual numbers eps²=0, L(B)=eps h, so there is no nonzero first-order tangent in this conjugating-isogeny locus. On the parameter line L(B(v))=−rho(v^p−v). This identifies GH-146's Frobenius sampling-alias factor as the precise first-jet obstruction: differentiating a relation valid at the p marked points does not establish the split CM-jet H'_p(B+)=6rho H_p(B+).

Exact computation: an author-executed Python stdlib finite-field program enumerated every E(F_(p²)) point for p=11,19,43,59,67,83,107, computed all 5,708 affine point orders for p=11,19,43,59 and deterministic 161–162-point subsets for larger tested p; checked exponent and full integer point count for seven p. For each p it checked 30 rational-point instances each of explicit phi composition and Psi²=[−2]Fr_(p²), 210 each in total. It independently computed p3347 arithmetic/gcd without p3347² exhaustive enumeration. Terminal: PASS_GH158_GH159_GH160_CM24_GROUP_ISOGENY_FROBENIUS_SQUARE. Finite tests verify formulas at listed fields; generality rests on algebraic proof and standard CM theorems.

Source dependencies: GH-155/156 (blob 8c3dcbaa1f0ae8cf7e69d00f08e452d207a0ad2b), GH-157 (blob aa6b9dbcfaa3a0737588a285d8853107b3fd5aba), GH-153 (blob 020d102ed87069b2281e0503496a07b5d2f48835). External background: Sage isogenies https://doc-gitlab.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_curve_isogeny.html ; CM reduction https://alexjbest.github.io/buntes/sec-deuring-lift.html .

BRC observer/provenance: retain characteristic and p mod24 branch, F_q root/parameter orientation, u sign, separable/inseparable operation order, integral Frobenius, full group invariant factors, first-order parameter and valid observation scope. Isogeny/CM point data do not automatically determine first derivatives. These are auxiliary elliptic-curve results, not P000 native X6 spatial theorems.

Continuation: completed author-portable units GH-158 group, GH-159 conjugating isogeny, GH-160 twisted Frobenius-square and alternative trace; no formal Source checkpoint or acceptance. Next exact action is a genuinely deformation-sensitive CM/Gauss-Manin or Gauss/Jacobi identity establishing split p≡11 (mod 24) K(1/144)=0 (equiv H'_p(B+)=6rho H_p(B+)), separately GH-3 original-vs-reflected comparison, then D25 native original-class H0/B0 divided-power module, [X]U mod p², rank, semilinear eta, p373 experiment. Do not repeat GH-155–157 numeric trace or old GH-151 Hasse coefficient route. Preserve protected old service session, requests and staging; register only with an actually authorized role/session/claim. 
