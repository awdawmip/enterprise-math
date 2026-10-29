# D25/LIFT GH-100–GH-101 — elliptic Hasse descent, quadratic-character trace, and exact finite-log contact

2026-10-29 · TASK_RESEARCH logical lane `chatgpt-research-hourly-enterprise-math-20260923`. Frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Parent: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION` / D25/LIFT/JT2 OPEN; historical Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.** No native authorized CLAIM/OPEN/checkpoint/Result or independent acceptance is implied.

## Exact independent sources

Throughout, p=8m+3 is prime, p>=11, d=2m=(p-3)/4, N=(p-1)/2, k=F_p, theta=z*d/dz. The GH-16 reflected Laurent source is

    h_0=1, h_(j+1)/h_j=(4j+3)^3/[(4j+4)(4j+5)(4j+6)], 0<=j<d;
    U(z)=sum_(j=0)^d h_j z^j; H_ref(z)=(8theta+5)U(z);
    R_p(a)=sum_(j=0)^d [(8j+5)h_j/(d+1+j)] a^(d+1+j).

All these denominators are p-units. The original GH-3 source T_(p,a)=(8theta+1)S_d(a), GH-83 Laurent B_0L, and elliptic Hasse coefficient are three distinct mathematical objects.

The actual cubic source C_T is v^2=u^3+u^2+(1+T)u/8; define the algebraic Hasse coefficient polynomial

    Ha_p(T)=[u^(p-1)] (u^3+u^2+(1+T)u/8)^N in k[T].

GH-81's proved coefficient identity gives Ha_p(T)=P_d(-T)=P_d(T) for even d. Hence Ha_p(T)=E_p(T^2) for a unique E_p(Y) of degree m. This descends polynomially to k even when sqrt(Y) is not in k. For smooth fibers T^2!=1, Ha is an actual elliptic Hasse coefficient; at a singular fiber this is only the coefficient polynomial. For T in k the true character-sum identity is Ha_p(T)=-sum_(u in k) chi(u^3+u^2+(1+T)u/8); for T in a quadratic extension, the same power-sum polynomial is valid but is NOT automatically an F_(p^2) quadratic-character count.

Let D=binom(3m+1,m) in k^*, G(z)=z^m E_p((z-1)/z) in k[z], L_p(t)=sum_(n=1)^(p-1) t^n/n, and chi the quadratic character on k (chi(0)=0).

## GH-100: Hasse descent and first genuine quadratic-character trace

**Theorem 100.1 (all primes p=3 mod8, p>=11):** the following are identities of polynomials / polynomial functions of the specified variables:

    U(z)=D^-2 G(z)^2;
    H_ref(z)=D^-2 [16 G(z) theta G(z)+5G(z)^2]
            =D^-2 z^d [16 z^-1 E_p(1-z^-1) E_p'(1-z^-1)-E_p(1-z^-1)^2].      (100.1)

**Proof:** F(z)=sum_(r=0)^m (-m)_r^2 z^r/[(2m+2)_r r!] solves
z(1-z)F''+(5/4-7z/4)F'-(9/64)F=0 in k because -m=3/8 and 2m+2=5/4 modulo p. Eliminating F'' and F''' from this ODE shows L_+(F^2)=0 for GH-78's exact operator L_+=theta(theta+1/4)(theta+1/2)-z(theta+3/4)^3. The GH-16 recurrence gives the unique solution of L_+q=0 with q(0)=1, deg q<=d, so U=F^2. On the other hand, G=z^m P_(2m)(t) with t^2=(z-1)/z is a genuine polynomial because P_(2m) is even. The Legendre ODE gives

    z(1-z)G''+[1/2-2m-(1-2m)z]G'-m^2 G=0.

Modulo p this is exactly the ODE for F, and coefficient recurrence makes the solution space of degree <=m one-dimensional. G's leading coefficient is P_(2m)(1)=1, whereas F's leading coefficient is m!/(2m+2)_m=D^-1; hence G=DF. Differentiate U=D^-2 G^2 and use 16m+5=2p-1=-1 (mod p). No forbidden characteristic-p denominators or unjustified infinite-series reductions occur.

GH-98 independently establishes R_p(a)=a sum_(x in k^*) x^d H_ref(x)L_p(x/a). Inserting (100.1), putting y=1-x^-1 and r=1-y, using r^-2d=r^((p+1)/2)=r chi(r) and the exact finite-log inversion L_p(t^-1)=-L_p(t)/t, gives the **new base-field Hasse/Legendre quadratic-character trace**

    R_p(a)=-D^-2 sum_(y in k) chi(1-y)
            [16(1-y)E_p(y)E_p'(y)-E_p(y)^2] L_p(a(1-y)),  a in k^*.          (100.2)

At y=1 the summand is zero. RHS contains the original curve's Hasse coefficient, its descended polynomial, a genuine quadratic character, and a finite logarithm, but no GH-16 h_j or R_p. This is a new composition/application of established Legendre and GH-98 identities; no claim of discovering classical identities anew. It requires no GH-74/75 CM premise.

## GH-101: eliminate Hasse derivative, but preserve the exact contact

**Theorem 101.1 (all same primes and a in k^*):** define the derivative-free moment and contact

    M_p(a)=sum_(y in k) chi(1-y) E_p(y)^2 L_p(a(1-y));
    C_p(a)=8 chi(a) E_p(1-a^-1)^2.

Then

    R_p(a)=D^-2 [C_p(a)-3M_p(a)].                                   (101.1)

In particular, R_p(a)=0 iff 3M_p(a)=C_p(a). This is a new exact finite-source equality, not a proof of a full-prime arithmetic zero classification.

**Proof:** write V(y)=E_p(y)^2, r=1-y, N=(p-1)/2, and K(y)=r^(N+1)L_p(ar). The degree bound

    deg(K V)<=N+1+(p-1)+d=(7p-5)/4 < 2p-1

ensures sum_(y in k)(K V)'(y)=0: the only derivative monomials whose power sums can survive are indices k=1 or p, and both have zero sums/coefficient in characteristic p. Thus sum K V'=-sum K'V. Because N+1=1/2 in k and dr/dy=-1,

    K'=-r^N[(1/2)L_p(ar)+ar L_p'(ar)].

Since 16r E E'=8rV', equation (100.2) reduces to

    R_p(a)=-D^-2 sum_(y in k) chi(r)V(y)[3L_p(ar)+8ar L_p'(ar)].

As a polynomial L_p'(t)=sum_(j=0)^(p-2)t^j; as a function on F_p its only nonzero values are L_p'(0)=1 and L_p'(1)=-1. The point ar=0 contributes zero since chi(r)=0. The unique point ar=1 is y=1-a^-1 and contributes -C_p(a), proving (101.1). Although L_p(1)=0, the derivative has a real *contact term* at 1; specializing before differentiation would erase it. This is the required operation/observer provenance.

## 3347 exact witness and computational coverage

For p=3347, m=418, d=836, at a=9:

    D=3073, E_p(8/9)=783, G(9)/D=1075;
    H_ref(9)=0, R_3347(9)=0;
    M_3347(9)=1568, C_3347(9)=1357=3*1568 (mod 3347).

Both moment and contact are nonzero, and their difference vanishes. The two chi=+1/-1 sectors of the derivative-bearing (100.2) sum to (1681,1681); this refines GH-99's 558 nonzero anharmonic orbit cancellations without proving a global prediction for exceptional primes.

An actually executed Python standard-library integer-only checker (`d25_gh100_gh101_compact_exact_check.py`) independently built Ha_p(T) from the original elliptic cubic binomial coefficient, its even descent E_p, the reflected h_j recurrence, and the finite-log polynomial from exact integer division modulo p^2. It verified U=G^2/D^2 as a complete polynomial and both (100.2), (101.1) against R_p(a) on **44 primes p=3 mod8** (all p<1000 plus 3347) and **168 distinct (p,a) specializations**. PASS, including all 3347 integers above. A separate larger 44-prime checker additionally compared full Ha_p(T) against independently constructed Legendre polynomials. These are author exact computations, not native Enterprise Math experiments or independent review.

BRC COMPOSE_APPLIED: keep reflected index j, cubic/Hasse source, base/extension chart, character sign, finite-log kernel, before/after derivative operation, and ar=1 contact; distinguish H_ref, Ha_p, E_p, M_p, original T and Laurent B_0L. F_p arithmetic is an auxiliary chart, not native Heartbeat World X6; P000 ACTIVE and the scientific Source pin remain unchanged.

**Next exact action:** seek an independent CM/Jacobi/WZ evaluation of the Hasse/log moment M_p(9) versus the contact C_p(9), explaining its equality at 3347 and testing whether it predicts further exceptional reflected-tail zeros. Independently continue the original GH-92 signed eigenport for T_(p,9)=0, with GH-20/21 p^2 moments and native p=373 obligations preserved. Control continuation/owner recovery belongs to enterprise-math #1558.
