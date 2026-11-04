# D25: exact three-band Hasse pullback and the inert Jacobi zero-factor theorem

Date: 2026-11-04. Research lane: chatgpt-research-hourly-enterprise-math-20260923.
Scope: author-side portable algebra, with existing Source checkpoint retained. Status: EXACT DERIVATION / CLASSICAL CM DEURING INPUT / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED.

## Theorem A — exact finite-field three-band identity

Let p=8q+5 be any prime (p>=5), m=(p-1)/2, L=(5p-1)/8=5q+3, and work in F_p[t]. Define

$$
f_k=\frac{(1/8)_k(3/8)_k}{(k!)^2},\quad
F_p(x)=\sum_{k=0}^{L}f_kx^k,\quad
H_p(t)=\sum_{k=0}^{m}\binom{m}{k}^{2}t^k,
$$

$$
x(t)=\frac{16t(1-t)^2}{(1+t)^4},
\qquad A(t)=t^2-6t+1.
$$

Then the following is a polynomial identity with coefficients in F_p:

$$
\boxed{(1+t)^{4L}F_p(x(t))=A(t)^pH_p(t)
       =(1-6t^p+t^{2p})H_p(t).}
\tag{A}
$$

All nonzero coefficients of the cleared numerator lie in the three bands
0..m, p..p+m, 2p..2p+m. It is an exact Frobenius carry identity through degree 4L=(5p-1)/2.

**Proof.** Let F(x)={}_2F_1(1/8,3/8;1;x),
C(x)={}_2F_1(5/8,7/8;1;x) and
G(t)={}_2F_1(1/2,1/2;1;t), as p-integral formal series.
The factorial/Pochhammer digit decomposition at the first base-p digit gives

$$F(x)=F_p(x)C(x^p),\qquad G(t)=H_p(t)G(t^p)\quad(\bmod p).$$

Indeed, in (a)_n/n! the unique zero factor of the first p-block occurs at r in [0,p-1] with a+r divisible by p. Its next digit is a'=(a+r)/p; full p-free blocks cancel between numerator and denominator. The first digits for 1/8 and 3/8 are L and 7q+4, with successors 5/8 and 7/8; for 1/2 the digit and successor both equal m and 1/2. Coefficients above the first zero digit vanish modulo p in each first-digit block. This proves both formal congruences coefficientwise for all indices.

Euler transformation gives C(x)=(1-x)^(-1/2)F(x).
The two standard quadratic hypergeometric transformations, composed at their origin branches, give

$$F(x(t))=(1+t)^{1/2}G(t).$$

Also (1-x(t))=A(t)^2/(1+t)^4.
Use the digit congruences and Euler transformation at the p-th power argument:

$$
F_p(x(t))=\frac{F(x(t))}{C(x(t)^p)}
=(1+t)^{(1-p)/2}(1-x(t)^p)^{1/2}H_p(t)
=\frac{A(t)^p}{(1+t)^{(5p-1)/2}}H_p(t).
$$

All divisions are by formal power series with unit constant term; both sides are rational functions in F_p(t). Multiplication by (1+t)^{4L} proves (A). The Frobenius polynomial A(t)^p is 1-6t^p+t^{2p}. QED.

## Theorem B — CM selection for the short Jacobi zero factor

Define

$$
J_p(z)=\sum_{k=0}^{q}\binom qk\binom{3q+1}{k}(z/9)^k.
$$

For every prime p>=5 with p≡13 (mod 24),

$$\boxed{J_p(1)=0,\qquad J'_p(1)\ne0\pmod p.}\tag{B1}$$

For every prime p>=5 with p≡5 (mod 24),

$$\boxed{J_p(1)\ne0\pmod p.}\tag{B2}$$

**Proof.** Let t be any root of

$$Q(t)=t^4-140t^3+294t^2-140t+1,$$

so that x(t)=1/9. The Legendre curve E_t:y^2=u(u-1)(u-t)
has j-invariant equal to a root of the Hilbert class polynomial

$$H_{-24}(j)=j^2-4834944j+14670139392.$$

This algebraic CM identification was established in the preceding author note 20261104_hourly20_d25_cm_minus24_period_bridge.md.
The arithmetic norms Q(0)=1, Q(1)=16 and Q(-1)=576 show that t, 1-t, 1+t remain nonzero at all primes p>=5, hence E_t has good reduction. The transformation factor A(t) is also nonzero, since A(t)^2/(1+t)^4=8/9.

H_p(t) is the Legendre Hasse invariant up to a fixed nonzero scalar, and vanishes exactly at supersingular Legendre parameters. Deuring's CM reduction criterion makes E_t supersingular exactly when p is inert in Q(sqrt(-6)). Within p≡5 (mod 8), this is precisely p≡13 (mod 24); the p≡5 (mod 24) primes split.

Theorem A gives F_p(1/9)=U(t)H_p(t), U(t)=A(t)^p/(1+t)^{4L}, with U(t) nonzero. The previously proved finite Euler identity F_p(x)=(1-x)^N J_p(9x) in F_p[x], N=(p+1)/2, transfers this equivalence to J_p(1). Thus (B1)'s vanishing and (B2) follow.

For the derivative, H_p has only simple roots away from t=0,1: the Legendre Picard-Fuchs equation is

$$t(1-t)H''+(1-2t)H'-\tfrac14H=0\quad(\bmod p).$$

At an ordinary t-value with t(1-t) nonzero, simultaneous H=H'=0 would recursively force every Taylor coefficient zero; deg H=m<p contradicts H(0)=1. Also

$$x'(t)=\frac{x(t)A(t)}{t(1-t)(1+t)}\ne0.$$

Theorem A therefore transfers simple zeros from H_p(t) to F_p(x), then to J_p(z). This proves J'_p(1) nonzero in the inert class. QED.

## The first-jet bridge and next precise unit

At any root t of Q with H_p(t) nonzero, differentiation of Theorem A yields the exact invertible jet map

$$
\begin{pmatrix}F_p(x(t))\\F_p'(x(t))\end{pmatrix}
=
\begin{pmatrix}U&0\\U'/x'&U/x'\end{pmatrix}
\begin{pmatrix}H_p(t)\\H'_p(t)\end{pmatrix}.
$$

Its determinant is U²/x' nonzero. Together with the finite Euler transform and J_p(z)=C_q(z/9), the observer pair (J_p(1),J'_p(1)) is equivalent to the Hasse value and first jet with an explicit invertible change of coordinates.

For split primes p≡5 (mod 24), the still-open derivative condition J'_p(1)=0 is **exactly equivalent** to

$$
\boxed{16t(1-t)(1+t)H'_p(t)
 +(1+2t-7t^2)H_p(t)=0, \quad Q(t)=0.}
\tag{C}
$$

The equivalence follows by logarithmic differentiation of (A), using 4L≡-1/2, N≡1/2 modulo p. (C) is the next small target for a CM isogeny / modular derivative certificate; its extension to the p² Green–Wronskian correction remains pending.

BRC/Enterprise observer scope: retain the two CM j conjugacy branches, the full first jet and its invertible transport, the (-6/p) CM split/inert class, and the original native H0/B0 and signed odd Hesse ports as separate evidence sources. The local use of the Legendre period is a typed mathematical comparison interface inside the project's fixed P000 / Heartbeat X6 basis. A scalar total J alone loses the first-jet observer needed in the split class.

## Finite exact certificate and provenance

Checker: d25_hasse_three_band_cm_selection_20261104.mjs. The full polynomial identity (A) was independently rebuilt coefficientwise over F_p for p=5,13,29,37,53,61,101,109, using original rational recurrence, binomial polynomial expansion and an independent Frobenius three-band RHS. Also checked (J(1),J'(1)) for p=5,13,29,37,53,373. The script ran in an ECMAScript V8 execution environment during this research turn; its reported counts and inputs are in the checker output. Finite computation supplements the general proof.

Sources: original author-side CM bridge and short-Jacobi finite Euler result in research_notes/portable_direct; classical Deuring criterion: https://link.springer.com/article/10.1007/s10231-024-01528-x (Theorem 4.1); classical quadratic Gauss transforms and Legendre Hasse polynomial; H_-24 tabulated in https://numberdb.org/Hilbert_class_polynomials . No independent review or native mathematical admission was performed.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Existing canonical Source frontier from prior authenticated owner remains authoritative. Author-side material is portable evidence; native fixed-p=373 H0/B0 divided-power experiment and the Delta_p-R_p bridge remain pending.
