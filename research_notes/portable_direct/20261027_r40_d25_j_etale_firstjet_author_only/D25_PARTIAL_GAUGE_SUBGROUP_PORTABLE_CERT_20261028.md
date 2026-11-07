# D25/LIFT — partial residual-gauge rank-two orbits (author-only certificate, 2026-10-28)

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific source c47e13e4aba0e006366f989d6334d443f6333ae3. Status AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. This continues, but does not re-prove, the rank-two full-centralizer theorem and the trace-annihilator image theorem previously stored in Draft PR #1566.

## Theorem, all finite fields k=F_q of odd characteristic

Fix A in M_2(k), H <= Z_GL2(k)(A), and the signed commutator port K=[B,A] for source matrices B. Count H-conjugacy classes of admissible K, NOT equivalence classes of the original B sources.

(S) If A has distinct eigenvalues in k, choose an ordered eigenbasis. Then K(u,v)=[[0,u],[v,0]]. The effective H image is R={s/t:diag(s,t) in H} <= k^*, with h=|R| dividing q-1. Its action is (u,v) -> (lambda*u,lambda^(-1)*v). Exactly
    N_S=1+(q^2-1)/h
orbits remain. A complete polynomial observer is I_S=(u^h,v^h,uv), including zeros. All nonzero orbits have h members. This recovers the full-centralizer q+2 result when h=q-1.

(I) If the characteristic polynomial of A is irreducible, identify k^2=F_(q^2), A=m_theta and K_y=m_y*tau, tau(z)=z^q. The effective image Q={s^(1-q):m_s in H} lies in the order-(q+1) norm-one subgroup and has order h dividing q+1. It acts by y->lambda*y. Exactly
    N_I=1+(q^2-1)/h
orbits remain, classified by I_I=y^h, including zero. The determinant -Norm(y) is complete precisely when h=q+1; a proper subgroup leaves multiple distinct orbits in each nonzero norm fiber. This recovers the full-centralizer q count.

(J) If A=aI+E12, admissible K(u,v)=[[-v,u],[0,v]]. Write g=s(I+cE12) and C={c:g in H} <= (k,+), h=|C|. The action is (u,v)->(u+2cv,v). Exactly
    N_J=q+q(q-1)/h.
There are q singleton orbits (u,0), and for each v !=0 the orbit is the additive coset u+2vC. For C=k, the complete polynomial observer is (v,u*(1-v^(q-1))). If q=p is prime, h can only be 1 or p; the counts are p^2 or 2p-1. When A is scalar, K=0 and N=1.

## Proof

For nonscalar A the established commutator-image theorem gives q^2 admissible K. In the split case, the diagonal-centralizer ratio map is a group homomorphism and its effective image R acts freely on all nonzero (u,v); hence one zero orbit and (q^2-1)/h nonzero orbits. Cyclicity of k^* makes R the unique order-h subgroup, so equal h-th powers identify the same R-cosets; the preserved product uv couples the two nonzero coordinates, establishing the polynomial observer.

For irreducible A, every k-linear map on F_(q^2) is uniquely m_x+m_y*tau. Its commutator with m_theta spans exactly the m_y*tau component because theta^q != theta. Conjugation by m_s multiplies y by s^(1-q). The image Q is an order-h subgroup of the cyclic F_(q^2)^*, acting freely on nonzero y. Equality of y^h is exactly equality up to that subgroup, giving the formula and the complete observer. Norm fibers have q+1 nonzero points, so they are single orbits precisely for h=q+1.

For Jordan A, E12^2=0 makes the gauge parameter c additive under multiplication, and direct conjugation gives (u+2cv,v). Each of the q points with v=0 is fixed. For every v!=0 the u coordinate has q/h cosets of h points, because 2v is a unit. Sum q+(q-1)q/h. If C=k, use v^(q-1)=1 for v!=0 and 0 for v=0; the polynomial observer follows. In the prime field, the additive group has no proper nontrivial subgroup. The scalar case has trivial commutator image. QED.

## Exact numerical and provenance boundaries

At p=373, formulas give split h=6 -> 23189 orbits; nonsplit h=11 -> 12649; Jordan effective full -> 745, trivial -> 139129. These are symbolic consequences, not exhaustive p373 native runs or identifications of the original H0/B0 gauge group.

A standard-library integer checker was actually run and passed all effective subgroups for p=3,5,7,11,13,17: 24 split, 27 irreducible, 12 Jordan subgroup families, 63 cases total; a distinct fuller author checker recorded 8015 point-membership checks and 8794 orbit-action elements. See the companion compact executable and author-check report. Both checks share the author context; there is no independent review.

The declared quotient is observer-safe only for H-invariant readouts and future operations proved H-equivariant. It does not erase source B, a marked odd matrix port, signed provenance or unknown future interactions. Original H0/B0 rank, normalized A, exact allowed H, semilinear Frobenius direction, signed observer, kappa and Delta_p-R_p remain required at existing support Issue #1559. The external finite-field K carrier is not the P000 six-dimensional native Cell geometry; no native-state or three-dimensional-slice transfer is inferred. UR V2 original mathematics is not repeated; its exact 94687-byte SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 remains provenance-pending.

Use existing Source authorization and original request receipts before any formal continuation. GitHub Draft PR storage is author-side evidence only; Source CLAIM/OPEN/checkpoint, independent review and admission remain unverified.
