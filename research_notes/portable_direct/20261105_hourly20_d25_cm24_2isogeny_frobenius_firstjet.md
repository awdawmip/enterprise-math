# D25: CM(-24) degree-two isogeny / Frobenius class switch and first-jet defect

Date: 2026-11-05. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). **AUTHOR-DERIVED / PROVED IN STATED SCOPE / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED**. Auxiliary CM Legendre observer, not the original-class crystalline H0/B0 experiment.

## 1. Exact two-isogeny and class switch

Let Q(t)=t^4-140t^3+294t^2-140t+1 and take t in A=Z[t,t^{-1},(1-t)^{-1}]/(Q). Both t and 1-t are invertible, since Q(0)=1, Q(1)=16.

For E_t: y²=x(x-1)(x-t)=x³-(1+t)x²+tx, the rational 2-torsion P=(0,0) gives a separable degree-2 isogeny φ with kernel {O,P}:

X=x-(1+t)+t/x,  Y=y(1-t/x²),

E'_t: Y²=X³+2(1+t)X²+(1-t)²X.

Direct substitution proves the isogeny equation and φ*(dX/(2Y))=dx/(2y). The chosen 2-isogeny and its differential normalization remain explicit.

The Weierstrass j formula gives

j(E_t)=256(1-t+t²)^3/[t²(1-t)²],
j(E'_t)=16(1+14t+t²)^3/[t(1-t)^4].

Set u=t+t^{-1}; then u²-140u+292=0. Exact reduction yields

j(E_t)=144(247u-502),
j(E'_t)=144(34078-247u),

hence **j(E_t)+j(E'_t)=4834944**, **j(E_t)j(E'_t)=14670139392**, and each j satisfies the Hilbert class polynomial H_{-24}(J)=J²-4834944J+14670139392. The exact integer identity certifying the sum is

256(1-t+t²)^3(1-t)²+16t(1+14t+t²)^3-4834944t²(1-t)^4
=16Q(t)(16t^4+2161t³-4098t²+2161t+16).

Thus the chosen 2-isogeny exchanges the two CM j classes; at small reduction primes the values may coincide, without invalidating the identity.

## 2. All-prime Frobenius equality on the CM subscheme

For every prime p>=5 with p≡5 (mod8), in A_p=F_p[t]/(Q) let u=70+48s, where s²=2. Since (2/p)=-1, s^p=-s and u^p=140-u. Consequently

**j(E_t)^p=j(E'_t)** in A_p.

On each geometric branch of Q, E'_t is isomorphic over the algebraic closure to E_t^(p). Composing the explicit φ with such an isomorphism produces a degree-2 isogeny E_t→E_t^(p); composing with Verschiebung yields an endomorphism of degree 2p. The isomorphism/twist, signed differential scalar and native H0/B0 comparison are still to be determined.

## 3. Exact first-jet mismatch / transversality

Put D_p(t)=j(E'_t)-j(E_t)^p as a rational function over F_p, with denominators t and 1-t. Every geometric CM root a of Q satisfies D_p(a)=0. But differentiation in characteristic p gives

D'_p(a)=j(E'_t)'(a)
=16(a+1)(a²-34a+1)(a²+14a+1)²/[a²(a-1)^5].

The exact integer Sylvester resultants are

Res(Q,t+1)=576=2^6·3²,
Res(Q,t²-34t+1)=10969344=2^8·3^4·23²,
Res(Q,t²+14t+1)=5992704=2^8·3^4·17².

For p≡5 (mod8), no prime p equals 2,3,17,23. Q is squarefree for p>=5. Therefore **D'_p(a)≠0 at each of its four roots**, and D_p has a simple zero at every CM branch. This proves that class-switching equality on CM points cannot be differentiated as a global family identity. The explicitly nonzero first-order defect is a reusable observer for the still-open Hasse derivative problem.

## 4. Split-prime binary-form norm channel

The reduced primitive positive-definite forms of discriminant -24 are [1,0,6] and [2,0,3]: the reduction bound a<=sqrt(8) restricts a to 1 or 2. For every p≡5 (mod24), (-6/p)=1, and the classical binary quadratic form representation theorem gives representation by one of these forms. The principal form p=x²+6y² is impossible modulo 3, hence

**p=2a²+3b²** with a,b odd.

Therefore π=2a+b√(-6) in Z[√(-6)] has **Norm(π)=2p**. Examples: p=5:(a,b)=(1,1); p=29:(1,3); p=53:(5,1); p=101:(7,1). This arithmetic candidate is retained separately from the geometric degree-2p endomorphism. Their precise comparison, orientation and normalization is a next research question.

## 5. Verification and remaining objective

Python standard-library finite-ring checker executed on 2026-11-05. Exact integer polynomial identity and resultant computations were checked, and 569 primes p<=20000, p≡5 mod8, passed j-Frobenius/trace/norm checks. The 281 split primes passed 2a²+3b² representation; 288 inert primes passed the opposite representation test. All-prime proof uses the displayed algebra, quadratic reciprocity and standard reduced-form theory; finite checks are corroborating evidence.

Next local action: compute the isomorphism E'_t≅E_t^(p) with a **chosen invariant differential and twist**, preserving the derivative mismatch D'_p; test whether the resulting Hasse scaling implies the still-open split-class Q|C_p, C_p=16t(1-t²)H'_p+(1+2t-7t²)H_p. If successful, connect to the Jacobi–Green–Wronskian p² observer. In parallel the original frozen task still requires authenticated p=373 H0/B0 divided-power module, [X]U mod p², rank, semilinear direction, normalization η and native κ / Δ_p−R_p. Native CM experiment NOT_RUN; no Result/admission claim.

References for classical background: https://crypto.stanford.edu/pbc/notes/numbertheory/form.html ; https://encyclopediaofmath.org/wiki/Binary_quadratic_form . Prior CM/Hasse author-side notes in research_notes/portable_direct are provenance, not native source progress.
