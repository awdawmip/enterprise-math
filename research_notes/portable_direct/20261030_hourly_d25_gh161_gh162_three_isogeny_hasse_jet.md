# D25/LIFT GH-161–GH-162: 3-isogeny first jet proves full-prime reflected stationarity

2026-10-30. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.** Logical lane `chatgpt-research-hourly-enterprise-math-20260923`; not CONTROL_PLANE_MAINTENANCE. Parent D25/LIFT/JT2 OPEN, Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Preserve P000 ACTIVE_LOCKED, active worldview and frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. GH labels denote author-side portable units, not native Task IDs.

## Question and new proof route

GH-153 reduced the reflected polynomial's stationary-point question to a marked Hasse first jet. GH-160 observed correctly that the finite Frobenius-conjugate locus has zero tangent and cannot support an unqualified differentiation. We construct a *nonconstant* 3-isogeny correspondence, compute its first jet at the CM mark, and apply Hasse–Witt/Cartier covariance. This uses neither the prior CM integer-trace formula nor the GH-151 special-value coefficient transport. Only the final reflected-tail corollary imports the earlier author-side GH-108/GH-153 factorization.

Let p>=11 be prime p≡3 mod8, N=(p−1)/2, K=F_(p²)=F_p[rho] with rho²=2, E_B:y²=x³+x²+Bx, and H_p(B)=[x^N](x²+x+B)^N. Mark B_+=1/8+rho/12, B_−=1/8−rho/12=1/4−B_+=B_+^p. Here B_+(1−4B_+)=1/144 !=0.

## GH-161: explicit 3-isogeny with nondegenerate deformation

The three-division polynomial is psi_3(r,B)=3r⁴+4r³+6Br²−B². At B_+ there is an exact root

`r_0=−1/3−rho/4,` with `psi_3(r_0,B_+)=0` and `partial_r psi_3(r_0,B_+)=r_0/3 !=0`.

The last nonvanishing follows from Norm(4+3rho)=−2. Consequently the three-torsion abscissa has a legitimate formal/étale deformation r(B), with r'(B_+)=6+3rho.

On the open 3-division cover, let P and −P denote the points with x-coordinate r. Vélu's degree-three quotient by {O,P,−P} has a_2=1 and a_4^V=B−10(3r²+2r+B). The image of the marked two-torsion point (0,0) has x-coordinate t=2(B/r−r), since x(P+(0,0))=B/r. Translate the quotient coordinate by t and normalize its x² coefficient with

`A(B,r)=1+3t`,
`T(B,r)=(a_4^V+2t+3t²)/A².`

The resulting marked quotient is E_T over an algebraic closure. Vélu preserves invariant differentials; the final scale x_old=A*x_new and y_old=A^(3/2)*y_new makes the differential pullback sqrt(A).

Exact implicit differentiation at the marked root gives the new **first-jet certificate**

```
r_0=-1/3-rho/4    r'(B_+)=6+3rho
t(B_+)=2/3        A(B_+)=3
T(B_+)=B_−        A'(B_+)=-72rho
T'(B_+)=1
```

Primes p>=11 introduce no zero denominator (the relevant norm is −2). These are derivatives along the full positive-dimensional 3-division cover, not derivatives of the isolated condition B^p=1/4−B.

## GH-162: exact isogeny covariance and first-jet theorem

The Hasse coefficient H_p is the Hasse–Witt coefficient of the elliptic curve with differential omega=dx/(2y). Naturality and p^(-1)-semilinearity of the Cartier operator show that for a separable isogeny with phi*omega'=c omega,

`H(E')=c^(1-p) H(E).`

Applying it to the normalized 3-isogeny gives the polynomial identity on the 3-division cover:

`H_p(T(B,r))=A(B,r)^(-N)*H_p(B).` **(1)**

The explicit normalized two-isogeny E_B→E_(1/4−B) of GH-159 has differential multiplier u with u²=−2. Since (−2/p)=1 for p≡3 mod8, u belongs to F_p and hence its Hasse multiplier is 1. Thus, for every B,

`H_p(1/4−B)=H_p(B)`, `H'_p(1/4−B)=−H'_p(B)`. **(2)**

At B_+, A=3, so A^(-N)=(3/p). For p≡11 mod24, (3/p)=+1. Differentiating (1) **along r(B)** and using (2), T'=1 and A'/A=−24rho yields

`−H'_p(B_+)=H'_p(B_+)−N*(−24rho)*H_p(B_+).`

Because N=−1/2 in F_p:

**`H'_p(B_+)=6rho H_p(B_+)` for every p≡11 mod24.** **(3)**

For p≡19 mod24, (3/p)=−1. Taking values in (1)–(2) gives H_p(B_+)=−H_p(B_+), whence

**`H_p(B_+)=0` for every p≡19 mod24.** **(4)**

The split H_p(B_+) is necessarily nonzero, and the inert zero is simple: H_p satisfies the exact polynomial differential equation B(1−4B)H''+(1−8B)H'−(3/4)H=0, whose leading coefficient is 1/144 at the mark. A nonzero polynomial of degree <=N<p satisfying this regular ODE cannot have a multiple zero (Taylor-coefficient induction; all factorials up to N invertible). Thus (3)–(4) additionally prove an elementary marked ordinary/supersingular Hasse dichotomy without the earlier CM trace calculation.

**All-prime reflected stationarity, conditional only on the imported GH-108/GH-153 factorization.** For p=8m+3, W=(z−1)/(128z), f(W)=H_p(1/8+rho*sqrt(W)) as an even polynomial and K=(1−128W)f'−8f, GH-153 gives

`R'_p(z)=z^(4m)*f(W(z))*K(W(z))/(8D²)`, D=binom(3m+1,m)!=0 (mod p).

At z=9, W_0=1/144. If p≡11 mod24, (3) is f'(W_0)=72 f(W_0), so K(W_0)=0. If p≡19 mod24, (4) is f(W_0)=0. Hence

**`R'_p(9)=0` for every prime p>=11 with p≡3 mod8.** **(5)**

This is a full-prime proof of the *reflected stationary-point* subtarget. It does not turn the reflected R into the original GH-3 sum or prove that the **value** R_p(9) vanishes. Indeed the direct reflected definition gives R_11(9)=5 mod11 and R_19(9)=8 mod19, despite R'(9)=0; p=3347 retains its *previously established* R(9)=0 and R''(9)=2331 !=0 from GH-153. This finite counterexample prevents an overstrong all-prime root claim.

## Exact executed checks, observer scope and next frontier

The Python-stdlib checker `d25_gh161_gh162_three_isogeny_hasse_check.py` ran with exit 0 and terminal `PASS_GH161_GH162_THREE_ISOGENY_HASSE_JET_ALL_PRIME_STATIONARITY`. It checked the algebraic 3-division root, r', the quotient map T, A', T', Hasse reflection, differentiated 3-isogeny covariance, and split/inert conclusions at 20 specified p from 11 to 3347. Six small primes exhaustively covered 252 nonsingular rational three-subgroup *abscissas* over F_p, of which 108 displayed a nontrivial quadratic-twist Hasse sign. It directly regenerated the reflected R and checked R'_p(9)=0 for the 20 primes; these finite tests do not replace the general proof.

At p3347: H(B_+)=783, H'(B_+)=1351rho, A'=−72rho, T'=1, R(9)=R'(9)=0. At p11: H=10, H'=5rho, R(9)=5, R'(9)=0; at p19 H=0, H'=12rho, R(9)=8, R'(9)=0.

BRC `COMPOSE_APPLIED`: retain (p, B, 3-kernel abscissa r, two-torsion mark, quotient T, differential scaling A, reflection orientation and jets r',A',T',H'). A zero-order Hasse equality does not retain A' and cannot recover the directional first jet; the marked source/target and deformation operation are essential. This is an auxiliary finite-field observer result, not an X6 native spatial transfer.

**Next:** seek an independent arithmetic explanation for exceptional R_3347(9)=0; consult the exact Source GH-83 hard target before any formal closure; separately compare the *source-original* GH-3 sum to this reflected polynomial. D25 still needs its original-class H0/B0 divided-power, [X]U mod p², semilinear Frobenius/eta and actual native p373 experiment. No new native CLAIM/OPEN, Source checkpoint, Result, independent review or admission is asserted. As of this run Gateway 0.6.11 reports `research_authority_granted=false`, `CODE_REVIEW_REQUIRED` upstream and no verified new execution binding. Existing old service session, requests and staging remain untouched.
