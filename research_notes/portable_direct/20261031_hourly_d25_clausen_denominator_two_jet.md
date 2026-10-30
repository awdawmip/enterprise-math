# D25/LIFT — terminating Clausen lower-denominator two-jet and CM scalar observer

Date: 2026-10-31, Asia/Hong_Kong.
Lane: chatgpt-research-hourly-enterprise-math-20260923 (NOT the maintenance lane).
Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3, unchanged; P000 ACTIVE_LOCKED. This is classical auxiliary p-adic arithmetic, not an Enterprise native X6 theorem.

## Exact coefficient transport

Let p=6l+1 be prime >5, m=2l, h=3l, q=4l. Work in Z_(p), coefficientwise modulo p^3. Define theta=z d/dz and W=1+6theta.

T_l(z)=sum_{n=0}^{m} t_n z^n,  t_n=(-1)^n binom(h,n)binom(m,n)binom(q,n).

This is the *terminating low-band* source underlying the previously proved original-216/E.2 four-port decomposition; it is NOT the full 216 series. Let
G(z)=sum_{j=0}^l g_j z^j, g_j=binom(l,j)binom(2l,j).
Define harmonic H_n=sum_{r=1}^n 1/r, H_n^(2)=sum_{r=1}^n 1/r^2. For a polynomial P(z)=sum c_n z^n of degree <=m, let
Hcal(P)=sum H_n c_n z^n,
Hcal11(P)=sum H_n^2 c_n z^n,
Hcal2(P)=sum H_n^(2) c_n z^n.
Set G1=Hcal(G), G2=Hcal11(G)+Hcal2(G).

**Lemma 1: exact terminating rational Clausen transport.**
Set F(z) = 2F1(-l,-2l;1-p/2;z), of degree l. The classical Clausen square identity specializes to the finite rational polynomial identity

    F(z)^2 = sum_{n=0}^{m} t_n * (n!)^2 / [(1-p/2)_n (1-p)_n] z^n.  (1)

Proof: the upper parameters of the 3F2 are -2l,-4l,-3l, and the lower parameters are 1-p and 1-p/2. The -2l parameter terminates at n=m, before the lower 1-p parameter becomes zero. All used finite coefficients are defined and denominators are p-units. An undefined infinite 3F2 is *not* invoked. This is an application, not a novelty claim for Clausen's classical identity (NIST DLMF §16.12.2, https://dlmf.nist.gov/16.12#E2).

Let r_n=((1-p/2)_n(1-p)_n)/(n!)^2. Equation (1) gives the *exact* coefficientwise statement t_n=r_n[z^n]F^2 for 0<=n<=m.

**Lemma 2: explicit two-jet.**
The two Pochhammer expansions are

    F = G + (p/2)G1 + (p^2/8)G2            (mod p^3),
    r_n = 1-(3p/2)H_n + (p^2/8)(9H_n^2-5H_n^(2)) (mod p^3). (2)

Proof: n!/(1-p/2)_n is the product of inverses 1-p/(2j), whose logarithm through order p^2 is (p/2)H_n+(p^2/8)H_n^(2). The logarithm of r_n is -(3p/2)H_n-(5p^2/8)H_n^(2). Exponentiation yields (2). Every 1<=j<=m is a p-unit.

**Theorem: full polynomial Clausen lower-denominator two-jet.**
Multiplying the coefficients of F^2 by r_n in (1), collecting the exact polynomial coefficients and powers of p, yields

    T_l(z) = G(z)^2
      + p * [ G G1 - (3/2) Hcal(G^2) ]
      + p^2 * [ (G1^2+G G2)/4 - (3/2)Hcal(G G1)
                + (9 Hcal11(G^2)-5 Hcal2(G^2))/8 ]       (mod p^3). (3)

The congruence is in Z_(p)[z], coefficientwise at ALL degrees 0..m; it holds for every prime p=6l+1>5. It is not an interpolation from computed primes. Both second-harmonic and first-harmonic-square terms are needed at p^2. This is a denominator deformation, distinct from the project's earlier TOP-parameter jet in GH-178/179. It has no degree>=p projection since T_l terminates at m.

## CM first-digit observer and source-preserving next obstruction

Let z0=1/2, S_t=[W T_l](z0). For the frozen classes p mod24 in {13,19}, consume the earlier CM-root input G(z0)=0 (mod p), without claiming to reprove it. Define g=G(z0), j=G1(z0), K=Hcal(G^2). Since p divides g, applying W to (3) and dividing by p yields

    S_t/p = 6*(g/p)*G'(z0) + 3*G'(z0)*j
            - (3/2)*[W K](z0)               (mod p).   (4)

Proof: W(G^2)(z0)=g^2+6gG'(z0), and W(GG1)(z0)=g j+3G'(z0)j+3gG1'(z0); the terms with g vanish mod p after taking the appropriate order. The quotient g/p is legitimate ONLY under the stated CM hypothesis. No individual port is asserted to vanish.

Consume the previous ORIGINAL-216 four-port theorem and the published alternating E.2 supercongruence: the still-unproved first-digit bridge is equivalent to S_t/p + H_A + U = 1 (mod p). Hence its new low-polynomial version is the joint condition

    6*(G(z0)/p)*G'(z0)+3G'(z0)G1(z0)
    -(3/2)*[W Hcal(G^2)](z0) + H_A + U  ?=  1 (mod p). (5)

This is an exact equivalence with previously sourced dependencies, NOT a general proof of (5) or of A_p = p (mod p^3). H_A and U remain distinct source-labeled original-216 harmonic and first-crossing ports. BRC use: COMPOSE_APPLIED; carrier (p,l,index,source,valuation,CM carry,harmonic jet,H_A,U,signed weight,precision) retains the needed source distinction. No positive-weight mass or native X6 transfer is inferred.

## Computation and reproducibility

Attached executed Python standard-library verifier checks (3) at 65,973 polynomial coefficients over all 175 primes <=2400 congruent to 1 mod6, plus 92 frozen-class primes for (4) with actual CM-root and integral quotient check. Independently it checks exact Q-rational (1) for all coefficients at l=1..6 (including l where 6l+1 is not prime, purely as a rational Clausen regression). No floating-point arithmetic and no native H0/B0 experiment.

Actual marker: PASS_D25_CLAUSEN_DENOMINATOR_TWO_JET_COEFFICIENTWISE_EXACT

Representative rows (p; g/p, G', G1, W Hcal(G^2), S_t/p) modulo p:
13: (7,1,3,7,8)
19: (6,2,17,12,4)
37: (21,11,28,20,23)
157: (4,118,149,1,77)
373: (340,215,321,346,209).

At p=373 the low-band S_t=15521276 (mod 373^3), S_t=77957 (mod 373^2), so S_t/p=209 (mod373). The already independently sourced original-216 other ports at p373 are H_A=138 and U=27: 209+138+27=374=1 (mod373). This is one exact anchor for the open joint equation (5), not proof of an infinite-family supercongruence.

The original hard target A_p=sum_{n=0}^{p-1}(6n+1)binom(2n,n)^2 binom(3n,n)/216^n = p (mod p^3) for p mod24 in {13,19} remains OPEN. Next legitimate scientific unit: seek a finite WZ certificate, proven CM connection, or counterexample for the ENTIRE signed expression (5), then advance its second-digit joint cancellation (D0+D1)/p^2+I_p=0 (mod p) under proved divisibility. Original D25 native H0/B0 divided-power, [X]U mod p^2, semilinear Frobenius, eta/kappa, p373 experiment, independent review and formal admission remain separate.

## Source and control boundary

Consumed without recrediting: original four-port report at enterprise-math main f53d9c10a841f1e09d27b4219127c517cbe9cbfb; E.2 second harmonic at 92ea1758627b6620538af4acadc1163fd56ef6d8; GH-178/179 top-parameter jet at 9adc91a8cc7b5dc1ac5aa0984972a261051ec40f. Published E.2 source is Guo–Schlosser, 2023, https://pmc.ncbi.nlm.nih.gov/articles/PMC10027641/. Frozen scientific Source pin unchanged.

Current service 0.6.11 status: research_authority_granted=false, executor_binding_configured=false, native active_jobs=5/5, CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED. Original actual Research lane read-only recovery/continuation: kimi-query-bridge #6424 and #6425, execution_authorized=false. No new session registration, CLAIM/OPEN, Source checkpoint, Result, review, or admission occurred; no previous staging, maintenance identity or scheduler was modified. Native control repair remains enterprise-math #1558 and original native experiment #1559. Remote author-side storage, if successful, is NOT canonical scientific admission.