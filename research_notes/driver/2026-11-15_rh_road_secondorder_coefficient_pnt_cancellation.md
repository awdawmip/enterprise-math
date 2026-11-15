# RH composite road: unconditional PNT cancellation of the second small-a coefficient

Date: 2026-11-15.
Status: SCOPED DRIVER MATHEMATICAL DERIVATION (using a classical external quantitative PNT and the standard Laurent expansion of zeta); not an RH proof, not a native Result, not an independent acceptance review.
Author of this derivation: RESEARCH_DRIVER EM-DVR-DEBB5E. Original program: EM-FREE-C4A91D; formal target RH-ROAD-TAIL-20260909 / TP2-DCE65A0EFCE8151C39BD. Existing source author/researcher identities and live claims are not reassigned.

## Statement and meaning

Define Lambda(n) as the von Mangoldt function, psi(x)=sum_{n<=x}Lambda(n), and gamma as Euler's constant. For every integer n>=1 define

h_2(n) = (1/2)[(Lambda*Lambda)(n) - Lambda(n) log n],
H_2(x) = sum_{n<=x}h_2(n).

The convolution is over **ordinary positive integer divisors**. The same function has the exact description

- h_2(p^k)=-(1/2)(log p)^2 for every prime power p^k (k>=1);
- h_2(p^k q^l)=(log p)(log q) for distinct primes p,q and k,l>=1;
- h_2(n)=0 if n has >=3 distinct prime factors, and h_2(1)=0.

This is precisely the second coefficient in the earlier complete-road Taylor formula for S_a(N)-1, not a newly substituted prime-only model.

**Theorem.** The classical Vinogradov–Korobov PNT error for psi(x), together with the standard Laurent expansion of zeta at 1, implies

H_2(x) = -gamma x + o(x)   as x->infinity.

Consequently the normalized second coefficient of the exact centered road discrepancy,

q_2(N)=[H_2(N)+gamma(N+1/2)]/N,

satisfies q_2(N)->0. In combination with psi(N)/N->1 this identifies **two successive** normalized Taylor coefficients at a=0 that vanish for large N. No interchange between the limit a->0 and an infinite sum over N is claimed.

## Proof 1: the arithmetic coefficient and Dirichlet series

For Re(s)>1, from the multiplicative identity R_a(n)=sum_{d|n}mu(d)d^{-a} obtain

sum_n R_a(n)n^{-s} = zeta(s)/zeta(s+a).

Twice differentiating at a=0 is justified by absolute majorants of the form (log n)^2/n^{Re(s)}. Since

zeta''/zeta = (zeta'/zeta)' + (zeta'/zeta)^2

and -zeta'/zeta = sum_n Lambda(n)n^{-s}, differentiating with respect to s gives

(zeta'/zeta)' = sum_n Lambda(n)log n n^{-s}.

Thus the Dirichlet series of the a^2 coefficient equals

(zeta'/zeta)^2-zeta''/(2zeta)
 = (1/2)[(zeta'/zeta)^2-(zeta'/zeta)']
 = (1/2)sum_n [(Lambda*Lambda)(n)-Lambda(n)log n] n^{-s},

proving the formula for h_2(n). For pure prime powers, Lambda*Lambda(p^k)=(k-1)(log p)^2 and Lambda(p^k)log(p^k)=k(log p)^2. For support on two different prime factors, convolution has exactly the two ordered prime-power factorizations; this establishes the explicit support cases.

## Proof 2: the constant in the weighted Mangoldt sum

Write e(x)=psi(x)-x. The unconditional Vinogradov–Korobov form gives, for all sufficiently large x,

|e(x)| <= C x exp(-c Phi(log x)),
Phi(u)=u^(3/5)/(log u)^(1/5), u>e,

with c,C>0. In particular, e(x)=o(x), and the integral I=int_1^infinity e(x)x^{-2}dx converges absolutely: after u=log x its tail is majorized by int exp(-c Phi(u))du.

For t>0, partial summation in the absolutely convergent Mangoldt series yields

sum_n Lambda(n)n^{-1-t}
 = (1+t)int_1^infinity psi(x)x^{-2-t}dx
 = 1/t+1+(1+t)int_1^infinity e(x)x^{-2-t}dx.

As t->0+, dominated convergence makes the constant term on the right 1+I. On the other hand the left side is -zeta'(1+t)/zeta(1+t) =1/t-gamma+O(t) by the standard Laurent expansion. Thus

1+int_1^infinity e(x)x^{-2}dx = -gamma.   (A)

For y>=1, another partial summation gives

M(y):=sum_{n<=y} Lambda(n)/n
=psi(y)/y+int_1^y psi(x)x^{-2}dx
=log y+1+e(y)/y+int_1^y e(x)x^{-2}dx.

By (A), e(y)/y->0 and the convergence of I imply the **constant-term limit**

M(y)=log y-gamma+o(1).   (B)

This step cannot be replaced by an unsupported Laurent-to-summatory inference; its validity here uses the absolute convergence supplied by the quantitative PNT.

## Proof 3: Dirichlet hyperbola and the second coefficient

Let A(x)=sum_{n<=x}(Lambda*Lambda)(n) and y=sqrt(x). Dirichlet's exact hyperbola decomposition is

A(x)=2 sum_{m<=y}Lambda(m)psi(x/m)-psi(y)^2.

For m<=y one has x/m>=y. The quantitative PNT (using monotonicity of Phi for sufficiently large arguments) bounds the accumulated error by

sum_{m<=y}Lambda(m)e(x/m)
=O(x exp(-c Phi(log y)) sum_{m<=y}Lambda(m)/m)
=O(x log x exp(-c Phi((log x)/2)))=o(x),

where (B) supplies M(y)=O(log y). Also psi(y)^2=x+o(x). Hence, using (B),

A(x)=2x[log y-gamma+o(1)]-x+o(x)
    =x log x-(2gamma+1)x+o(x).             (C)

For J(x)=sum_{n<=x}Lambda(n)log n, Stieltjes partial summation and psi(x)=x+o(x) yield

J(x)=psi(x)log x-int_1^x psi(u)/u du
    =x log x-x+o(x),                      (D)

where the error o(x) in the first term uses the **quantitative** PNT: e(x)log x=o(x). The integral error is o(x) by e(u)/u->0 and Cesaro averaging.

Finally,

H_2(x)=(A(x)-J(x))/2
      =[-2gamma x+o(x)]/2=-gamma x+o(x).

This proves the theorem.

## Scope and reproducibility

The proof is a genuine consequence of established **unconditional** PNT bounds; it is not a new zero-free region, a strengthened RH result, or a bound for the full infinite road energy. A finite independent arithmetic sanity check of H_2(N)/N+gamma at N=10,100,1000,10000,100000 gave approximately 0.2533, 0.1689, 0.0161, -0.0140, -0.0057 respectively; these examples do not establish the limiting theorem.

The coefficient q_2(N)->0 complements, but does not replace, the inherited q_1(N)=(psi(N)-N-1/2)/N->0. In the second-order expansion

B_{a,N}/N = a q_1(N)+a^2 q_2(N)+O(a^3[(log N)^3+1]),

the a^3 remainder is not summably uniform over arbitrarily large N. One cannot use coefficientwise limits to assert an all-scale energy bound or parent-objective closure. The next discriminating problem is whether the summatory cancellation can be made **uniform in a** in the truly escaping N range, without discarding full-integer composite terms.

### Provenance

- Exact uniform second-order road expansion (same Driver, distinct present result): awdawmip/enterprise-math@88c0c896181727ebb3fa9f6645f025491b0ac957:research_notes/driver/2026-11-15_rh_road_secondorder_uniform_composite_expansion.md.
- Frozen prior first-order proof: awdawmip/enterprise-math@049192c481c7f5c9e838772ab08e2afa95a354e9:research_notes/driver/2026-11-15_rh_road_small_a_primecount_firstorder_pnt_nearfield.md.
- Classical PNT error scope and its exact domain correction: awdawmip/enterprise-math@136a9756df0e69187b80178df798cc969af3398c:research_notes/driver/2026-11-15_rh_road_vinogradov_korobov_extended_nearfield.md.
- Native acceptance, independent review, Task completion and mother objective completion remain unasserted.
