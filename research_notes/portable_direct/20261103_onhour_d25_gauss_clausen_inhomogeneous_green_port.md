# D25 onhour: exact Gauss-to-Clausen inhomogeneous boundary transport

Date: 2026-11-03 +08. TASK_RESEARCH author-side proof. Logical lane: chatgpt-research-onhour-enterprise-math-20260923, distinct from maintenance. Status: ALGEBRAICALLY PROVED / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.

Mother task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Original W_216(p-1) = p (mod p^3) for p = 13,19 (mod24) is OPEN, equivalently frozen Delta_p-R_p=0 (modp). This work directly consumes and does not re-prove the finite Clausen square, H4/U1 far-tail unit, terminal B_(p-1)/p^3=-1, D24 first digit, or prior argument jets.

## Exact setup and source separation

Take any prime p=6r+1>=7; in particular all target primes. Work with p-integral rationals and p-adic modular arithmetic, with theta=z d/dz:

c_k=(1/6)_k(1/3)_k/(k!)^2,
a_k=(1/2)_k(1/3)_k(2/3)_k/(k!)^3,
G(z)=sum_(k=0)^(p-1) c_k z^k,
F(z)=sum_(k=0)^(p-1) a_k z^k.
Original B_k=a_k/2^k and W_216(p-1)=[(1+6theta)F](1/2).

Define L2=theta^2-z(theta+1/6)(theta+1/3),
L3=theta^3-z(theta+1/2)(theta+1/3)(theta+2/3).
Formal infinite Clausen says _3F2(a_k;z)=_2F1(c_k;z)^2. For every n<p, [z^n]F=[z^n]G^2 exactly. Existing original Gauss valuation bands are v_p(c_k)=0 for k<=r, 1 for r<k<=2r, 2 for 2r<k<p. Define the finite high defect polynomial H(z)=(F(z)-G(z)^2)/p^2 modp. Divisibility and high support are coefficientwise.

## Theorem A: matched terminal forcing, proved

The exact coefficient recurrences, without an infinite-tail approximation, imply
L2 G = -(p-5/6)(p-2/3)c_(p-1) z^p.
The established prime-uniform Gauss edge unit c_(p-1)/p^2=1/10 (modp) therefore gives

    L2 G = -(p^2/18) z^p (mod p^3).                            (A)

Independently the original 3F2 recurrence gives
L3 F = -(p-1/2)(p-2/3)(p-1/3)a_(p-1) z^p.
The earlier B_(p-1)/p^3=-1 (modp) and a_(p-1)=2^(p-1) B_(p-1) show that
a_(p-1)/p^3=-1 (modp), by Fermat. Hence

    L3 F = -(p^3/18) z^p (mod p^4).                            (B)

Both are exact finite-polynomial congruences, including the only terminal coefficient, and are proved for every p=6r+1>=7. Their precision differs by one p-adic digit. The latter is an original finite 216 operator, not native H0/B0.

In ordinary derivatives A at z=1/2 yields the new explicit next-digit correction

    G''(1/2)+G'(1/2)-(2/9)G(1/2) = -(2/9)p^2 (mod p^3).       (C)

The previous mod-p^2 homogeneous Gauss equation is recovered on reduction.

## Theorem B: exact symmetric-square transfer and finite inhomogeneous source

For any differentiable/formal y let R=L2 y. Direct Euler-operator expansion proves the following operator identity over Q[z,y,theta y,...]:

    L3(y^2) = 2y theta R + 6(theta y) R.                         (D)

No CM period, Frobenius normalization or division by y is involved. Apply (D) to finite G and substitute (A). Since theta(z^p)=p z^p, modulo p^3 this gives

    L3(G^2) = -(p^2/3) z^p theta G (mod p^3).

By (B), L3 F=0 (mod p^3). Therefore

    L3 H = (1/3) z^p theta G (mod p),                           (E)

where H=(F-G^2)/p^2 coefficientwise and all p-divisions were made after proving exact divisibility.

The high-index pair support is the existing H4 provenance theorem: if i+j>=p, only pairs with one low index i in [1,r] and one far-upper j in [p-i,p-1] survive modulo p^3. Thus the polynomial H has no terms below z^p and no terms above z^(p+r-1) modulo p. Write uniquely H(z)=z^p K_p(z), deg K_p<=r-1 in F_p[z]. As theta(z^p K)=z^p theta K in characteristic p, (E) is equivalent to the new inhomogeneous differential law

    L3 K_p = (1/3) theta P_r,                                  (F)

where P_r(z)=G(z) modp=sum_(k=0)^r ell_k z^k and
ell_k=binom(r,k)binom(2r,k) modp. This equation retains the exact ordered pair/valuation/weight source via the equality H=z^p K, rather than asserting that the low Gauss observer is the whole original state.

## Theorem C: unique bounded-degree Green/recurrence certificate

For 1<=t<=r, put Q_t=(2t-1)(3t-2)(3t-1)/18 in F_p. All Q_t are p-units in the stated domain. The coefficient of z^t in (F), using K_r=0, is exactly

    t^3 K_t - Q_t K_(t-1) = (t/3) ell_t.                        (G)

Hence the entire defect has a constructive backward evaluation:

    K_r=0,
    K_(t-1)=Q_t^(-1)[t^3 K_t -(t/3)ell_t], t=r,...,1.         (H)

This proves uniqueness among polynomials of degree <r: the homogeneous difference obeys (G) with zero RHS and terminal K_r=0, so backward inversion makes every coefficient zero. The existing H4 two-prefix construction and (H) are two source-preserving representations of *the same* Clausen defect, not two independent scientific defects. Computational cost of (H) is O(r) field operations given ell; it needs no p^2-length convolution.

The exact original weighted defect observer is recovered, without abandoning its provenance, as

    E_p=[(1+6theta)(F-G^2)](1/2)/p^2
       = (1/2)[K_p+6theta K_p](1/2) (mod p).                  (I)

The factor (1/2) comes from Frobenius (1/2)^p=1/2 modulo p. This reconstructs the previously defined E_p, so the original open second-digit certificate now has the explicit differential boundary form

    (6AD-1)/p + h^2 + (1/2)[K_p+6theta K_p](1/2) ?= 0 (modp),  (J)

where A=G(1/2)/p, D=G'(1/2), h=A modp, and 6AD=1 modp comes from D24/first carry. Equation (J) is an exact equivalent OPEN obligation; (F)-(I) are proved for all p=6r+1. The next action is to seek an adjoint / terminating WZ certificate pairing (F) with Gauss first-carry so (J) follows without assuming its desired cancellation, with p=13,19,373 checking normalization and signs.

## Actually executed finite checks, distinct evidence

An exact integer/modular Python checker was executed for all 77 target-class primes <=2000. It evaluates K by (H), verifies all coefficients of (F), evaluates E independently from the original weighted 216 and Gauss g,d modulo p^3, verifies the Gauss terminal correction (C), and checks the p^4 original terminal source. For p=13,19,37,373, it also reconstructs the ENTIRE p^2-divided high Clausen convolution coefficient by coefficient without using (H). All PASS.

At p=13: (K_0,K_(r-1),E)=(12,4,0). At p=19: (18,15,7). At p=373: r=62, (K_0,K_61,E)=(58,5,177), Gauss ordinary ODE residual 28799703 modulo 373^3. These are finite checks alongside, not substitutes for, the universal algebraic proofs.

## BRC/Enterprise source and operational scope

BRC use: COMPOSE_APPLIED using the established exact H4 low/far-upper valuation-provenance carrier, Gauss finite Clausen, and prior second-carry readout; (F) is an operator-coordinate representation of the same bounded-degree source, and (I) proves factorization for the DECLARED scalar observer. For future native X6/H0/B0 operations or other signed ports the original pair/strip evidence is retained; this is not a native transfer, primitive-worldview change or new general tool family.

Native p=373 H0/B0 divided-power [X]U mod139129, module rank, semilinear Frobenius/eta, odd signed Green/Hesse κ and independent replay remain NOT_EXECUTED/PENDING_OWNER in support issue #1559. Historical bridge recovery #6632 contains no onhour claim/run; original dispatch #6633 failed UPSTREAM_CODE_REVIEW_REQUIRED. As of this run, Sites is static read only with research_authority_granted=false and write_relay_enabled=false. No new role-bound session, claim, run, Source checkpoint, Result, independent review or admission has been established.

This proof and its companion Python program are author-side durable research, with frozen source pin unchanged. Mother second-carry and native benchmark remain open.