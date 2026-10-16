# A positive top homogeneous c1 face and a uniform sum tail

AUTHOR ADDENDUM V2, UNREVIEWED NEW SCOPE. This strengthens the frozen highest-first-gap/scalar-boundary addendum within the SAME c1 research unit. The original V1 and its genuine third-person review remain unchanged and do not approve this stronger theorem. EM-DVR-BFF6DC authors the uniform two-parameter limit and its sign application. EM-DVR-F73673 contributes the already merged scalar-boundary refinement in Section 7, not this new limit proof. Neither author can independently approve the whole unit.

No scientific program, import, AST, compilation, numeric evaluation, symbolic expansion by a program, solver, scan or scientific consumer was used. The actual all-m paper input is Source ac9f1c0ffcfbb7ad5564721442480ad8e2236b83. This is not an execution of an old Task or a restart of the permanently stopped m7 fixed-certificate branch.

## 1. Exact normalization and the theorem

Let m>=2, n=m-1, W=m^2, S>=0, a>0,
r0=mS, L=ma, r=r0+L=m(S+a), and theta_i=(i+1)/m for 0<=i<=n.
The original normalized frame and metric are

G_L[i,j]=((r0+theta_i+L)_j-(r0+theta_i)_j)/(j!L), 1<=j<=n,
d_i(r)=((-1)^i binom(n,i)n!/m)/product_(h=0)^n(r+theta_i+h),
H(L)=G_L^T D(r)G_L, D=diag(d_i).

All L derivatives hold r0 fixed. This detail is essential below. The old restricted form is nondegenerate on the stated physical domain. Define

T(c)=tr(H(L+mc)^(-1)H(L))-n,
x=mr, beta=(W+1)/2, G_W(x)=product_(k=1)^W(x+k),
D_c=(x+Wc+beta)G_W(x), P(c)=D_c T(c)/c,
P1(S,a)=[c]P(c).

The original whole-trace common-denominator proof and the archived c1 interface prove that P is a rational-coefficient polynomial. D_c is the specified COMMON denominator; no arbitrary primitive-gcd normalization is substituted.

The author theorem is the following.

P1 has total degree exactly W-1. Its top homogeneous part H_m(S,a) satisfies

H_m(S,a) >= B_m(S+a)^(W-1),
B_m=(m^(2W+2)/2)(W-1)(m+2)>0                         (1)

for S,a>=0 with S+a>0. In particular its two pure-axis coefficients are positive. This is pointwise positivity of the whole top homogeneous face, NOT positivity of each mixed coefficient in that face.

Let A_m be the sum of the absolute values of all coefficients of the lower-degree polynomial P1-H_m, in the declared monomial variables (S,a). Then the finite coefficient-defined sufficient threshold

R_m=1+2A_m/B_m                                        (2)

has the following property on the physical domain:

S+a>=R_m implies P1(S,a)>=(B_m/2)(S+a)^(W-1)>0.       (3)

No value of A_m or R_m is computed. Formula (2) specifies a finite exact sufficient threshold from an already specified finite polynomial; it is not a practical complexity or evaluated-coverage claim. The theorem does not prove full c1 pointwise positivity, coefficientwise positivity, a full trace inequality, higher faces, HCM0 or the parent Goal. It gives a new uniform pointwise tail for this one polynomial coefficient, not for T(c) at arbitrary c.

## 2. Remove only the legitimately constant congruence

Use the n-dimensional polynomial space V of degree<=n-1 in theta, with basis 1,theta,...,theta^(n-1). Its evaluation matrix on the labeled nodes is Y[i,j]=theta_i^j, with 0<=j<=n-1. Let J be differentiation in this monomial basis: J[j-1,j]=j and its other entries are zero. Thus J^n=0.

The derivatives phi_j'(r0+theta) of the original rising-factorial basis form a basis of V. Consequently there is an invertible U(r0), independent of L, with their evaluation matrix equal to Y U(r0). The exact derivative-average identity gives

G_L=Y F_L(J) U(r0),
F_L(J)=sum_(k=0)^(n-1) L^k J^k/(k+1)!.

Its inverse is the finite geometric nilpotent inverse. Set

Q_r=Y^T D(r)Y, F=F_L(J), Hbar=F^T Q_r F.

Then H=U^T Hbar U, so K=H^(-1)H' and Kbar=Hbar^(-1)Hbar' are similar through U. No derivative of U is discarded: U depends on r0, which is held fixed for this derivative. This remains true when different physical parameter pairs later range over the whole domain.

Put Gamma_L=F_L'F_L^(-1). Differentiating Hbar first, before any asymptotic substitution, yields the exact identity

F Kbar F^(-1)
=Gamma_L+Q_r^(-1)Gamma_L^T Q_r+Q_r^(-1)Q_r'.          (4)

Here Q_r' is its derivative with respect to r, since dr/dL=1. Equation (4) keeps both frame-velocity terms. It is not a replacement of the moving frame by a constant one.

## 3. A uniform metric germ independent of the first-gap ratio

Let t=1/r. For monomial indices j,k in 0,...,n-1, rewrite theta_i^(j+k)=r^(j+k)(t theta_i)^(j+k). The metric entry becomes

Q_r[j,k]=(n!/m)r^(j+k-m) sum_i w_i f_jk(t theta_i,t),
w_i=(-1)^i binom(n,i),
f_jk(u,t)=u^(j+k) product_(h=0)^(m-1)(1+u+ht)^(-1).

The germ is analytic at (0,0). The exact finite-difference identities

sum_i w_i theta_i^q=0 for q<n,
sum_i w_i theta_i^n=(-1)^n n!/m^n

show that, after substituting u=t theta_i, the first possible term is t^n. At that order only u^n t^0 survives. Therefore, with

kappa=(-1)^(m-1)((m-1)!)^2/m^m,
M[j,k]=kappa [u^(m-1)]{u^(j+k)(1+u)^(-m)}
      =kappa binom(-m,m-1-j-k),                       (5)

where a negative lower binomial index means zero, one has

Q_r=C_r A_r C_r,
C_r=diag(r^alpha_j), alpha_j=j-m+1/2,
A_r=M+O(1/r), A_r analytic in 1/r at zero.             (6)

The matrix A_r is independent of r0 and L separately; it depends only on r. Thus this germ will be uniform in the ratio L/r. Its analyticity, rather than a bare O-symbol, also gives r A_r'=O(1/r). Nonsingularity of M is proved next.

## 4. Centered parity makes the limiting metric definite in blocks

The bilinear form M on polynomials is kappa times the residue at u=0 of

f(u)g(u) du/[u^m(1+u)^m].

Use the centered basis v^j=(u+1/2)^j, 0<=j<=n-1. This is a fixed real triangular change of basis. Under z=u/(1+u), the weight becomes

z^(-m)(1-z)^(2m-2) dz,
u+1/2=(1+z)/(2(1-z)).

For a product of centered basis vectors the resulting expression is a Laurent polynomial, because j+k<=2m-4. In particular it has no pole on the unit circle. Extracting its residue there, with z=exp(i theta), gives the centered matrix entries

Mcent[j,k]
=|kappa| 2^(2m-2) i^(j+k)/(2^(j+k) 2pi)
  integral_0^(2pi) sin(theta/2)^(2m-2)
  cot(theta/2)^(j+k) dtheta.                          (7)

This follows from 1-exp(i theta)=-2i exp(i theta/2)sin(theta/2) and (1+z)/(1-z)=i cot(theta/2); the phase from dz cancels the remaining exponential exactly. It can equivalently be read as the ordinary Fourier coefficient identity for a Laurent polynomial.

If j+k is odd, theta -> 2pi-theta changes the sign of the integrand, so the entry is zero. For j,k in the same parity p, write epsilon_j=(-1)^((j-p)/2). Then i^(j+k)=(-1)^p epsilon_j epsilon_k. Apart from this explicit diagonal congruence and the sign (-1)^p, (7) is a positive weighted Gram matrix of the distinct monomials (cot(theta/2)/2)^j.

The integrals are finite: the smallest endpoint vanishing order is 2m-2-j-k>=2. The weight is positive in the interior, and the distinct monomials are independent because cot(theta/2) ranges over the real line. Hence each parity Gram block is strictly positive definite. Mcent is positive definite on the even-degree block and negative definite on the odd-degree block. M is nonsingular. The possibly empty block at m=2 is harmless.

This is only a limiting metric statement; no definite-metric assertion about finite-r Q_r or the original H is made.

## 5. The exact frame symmetry preserves these blocks for every ratio

The finite nilpotent functions satisfy

F_(-L)(J)=exp(-LJ)F_L(J).

This is the identity for (exp(z)-1)/z in the truncated polynomial ring; all exponentials here are finite. Differentiating it and using commutation of polynomials in J gives

Gamma_(-L)=J-Gamma_L.

Moreover, the finite construction has the homogeneous form Gamma_L=sum_(k>=1)b_k L^(k-1)J^k. The reflection identity forces b_1=1/2 and b_k=0 for every odd k>=3. Thus

Gamma_L=J/2+sum_(2h<n)b_(2h)L^(2h-1)J^(2h).           (8)

No sign of the remaining rational coefficients is assumed or needed. For 0<=lambda<=1 define the finite polynomial

gamma_lambda(J)=J/2+sum_(2h<n)b_(2h)lambda^(2h-1)J^(2h).

Its endpoint lambda=0 is regular. Set lambda=L/r=a/(S+a), which lies in (0,1] on the physical domain. Because C_r J C_r^(-1)=J/r, one has the EXACT identity

r C_r Gamma_L C_r^(-1)=gamma_lambda(J).

Differentiating Q_r in (6) and substituting in (4) now gives an exact similarity transform of rKbar:

r C_r F Kbar F^(-1) C_r^(-1)
=Z_lambda+A_r^(-1)Z_lambda^T A_r+r A_r^(-1)A_r',
Z_lambda=D_alpha+gamma_lambda(J), D_alpha=diag(alpha_j).

The limit as r->infinity is therefore

R_lambda=Z_lambda+M^(-1)Z_lambda^T M,                  (9)

with an O(1/r) error UNIFORM for lambda in [0,1]. Indeed A_r and its derivative are independent of lambda and analytic at infinity, M is nonsingular, and gamma_lambda is a fixed finite polynomial on a compact interval. No condition number bound for the possibly large similarity F or C_r is needed; the displayed matrix identity is exact and trace is similarity invariant.

The L derivative in (4) held r0 fixed. We have not differentiated while holding lambda fixed: lambda enters only after that exact derivative has been taken and the scaling identity applied. Thus the variation of lambda=L/(r0+L) is not silently omitted.

In the centered variable v=u+1/2, D_alpha+J/2 is

v d/dv-(m-1/2)I.

Every additional term in (8) is an even derivative. Consequently Z_lambda preserves the even and odd centered polynomial subspaces for EVERY lambda. Since M has the same orthogonal blocks, R_lambda also preserves them and is M-self-adjoint. Reversing the sign of the negative block supplies a positive definite metric on each block. R_lambda therefore has n real eigenvalues, for every lambda in [0,1]. This assertion is ONLY about the limiting operators, not the actual finite-r logarithmic derivative.

The derivative polynomial gamma_lambda is nilpotent, so

tr R_lambda=2tr Z_lambda=2sum_(j=0)^(n-1)(j-m+1/2)=-(W-1).

The real-eigenvalue square inequality gives the UNIFORM bound

tr(R_lambda^2)>=(W-1)^2/(m-1),
tr(R_lambda^2)+W-1>=(W-1)(m+2)>0.                    (10)

Taking squared traces in the exact transformed matrix equation proves

r^2 tr(K^2)=tr(R_lambda^2)+O_m(1/r)                  (11)

uniformly over the physical ratios, including limits toward zero. No finite-r spectral continuity or positivity shortcut is used.

## 6. The positive homogeneous face and the tail threshold

The original actual c1 identity, with ell and h2 the contiguous-block scalar sums, is

P1=(W/2)(x+beta)G_W(x)[tr(K^2)+Wq_W(x)],
q_W(x)=2ell(x)/(x+beta)-h2(x), x=mr.

The finite sums give x^2q_W(x)->W-1, with a rational O(1/x) error after multiplication by x^2. Since W=m^2 and G_W is monic of degree W, (11) implies

P1/r^(W-1)
=(m^(W+3)/2)[tr(R_lambda^2)+W-1+O_m(1/r)]             (12)

uniformly in lambda. Let s=S+a and lambda=a/s. Since r=ms, this is

P1(S,a)/s^(W-1)
=(m^(2W+2)/2)[tr(R_(a/s)^2)+W-1+O_m(1/s)].            (13)

For fixed nonnegative direction (S,a) with a>0, scaling both variables by t and sending t to infinity gives a finite strictly positive limit at degree W-1. Polynomiality of P1 then forces all homogeneous components above degree W-1 to vanish: each such component vanishes on an open quadrant and is the zero polynomial. The nonzero limit forces total degree exactly W-1. Its top homogeneous component is precisely

H_m(S,a)=(m^(2W+2)/2)(S+a)^(W-1)
         [tr(R_(a/(S+a))^2)+W-1].                    (14)

This expression also extends to the two nonnegative axes. One can see polynomiality directly: gamma_lambda is a finite polynomial of degree at most n-2 when n>=2, so the squared-trace degree in lambda is at most 2n-4<=W-1 (the cases n<=2 are constant). Alternatively it follows from its identification with the top polynomial component. Equations (10) and (14) prove (1), including the formal boundary a=0 without a physical zero-gap assertion.

In particular the pure a^(W-1) coefficient is (14) at (S,a)=(0,1); this recovers the V1 highest-a theorem with its identical lower bound. The pure S^(W-1) coefficient is likewise positive. The mixed coefficients of H_m remain unresolved; a positive polynomial on a cone need not have positive monomial coefficients.

Now let L_m=P1-H_m, a polynomial of degree<=W-2. The nonnegative rational number A_m in (2) is its finite absolute coefficient sum. For s=S+a>=1, every monomial S^u a^v of total degree<=W-2 has absolute value at most s^(W-2). Hence

|L_m(S,a)|<=A_m s^(W-2).

Combining this with (1) and s>=1+2A_m/B_m proves (3). The threshold is coefficient-defined and could be obtained by finite exact algebra from the already specified polynomial, but no such execution, coefficient table or practical numerical value is supplied. This is a single uniform large-s statement, not a list of fixed-m or fixed-interval certificates.

## 7. Retained merged scalar boundary

For completeness of this SAME sign-boundary unit, retain the already merged small-x limitation. BFF6DC first recorded an m>=4 obstruction plus eventual positive q_W; F736 independently found the same mechanism with range m>=3 and a Jensen bound, after freezing the original identity review. The overlap was identified, the exact original notes exchanged, and their contributions merged. It is not counted as another discovery.

Convexity gives h2(x)>=(W-1)/(x+beta)^2>0. For H_W=sum1/k and H_W^(2)=sum1/k^2,

q_W(0)=4H_W/(W+1)-H_W^(2)-4/(W+1)^2.

H_N/(N+1) decreases for integers N>=2. Thus W>=9 gives

4H_W/(W+1)<=4H_9/10=7129/6300,
H_W^(2)>=49/36,
q_W(0)<=-241/1050-4/(W+1)^2<0.

Continuity yields a physical interval x>0 with q_W<0 for every m>=3, using S=0,a=x/W>0. Its eventual sign is positive by x^2q_W->W-1. There P1>=0 requires the actual compensation tr(Omega^2)>=-Wq_W>0. The uniform large-s result does not establish that small-x compensation, and is not a counterexample to it.

## 8. Exact limits and contribution record

The completed author claim is (1)-(3) for the common-denominator P1, with the fully specified top homogeneous form (14). It does not infer monomial coefficient positivity from pointwise positivity, supply a practical threshold, settle small or moderate s, prove full T(c)>0, or change any Task or Goal. The first new paper remains only an explicit identity, and the V1 highest-a review remains valid only for its frozen V1. Neither is silently promoted to this uniform result.

Original mathematical input: ac9f1c0ffcfbb7ad5564721442480ad8e2236b83, path research_notes/owner_goal_20261016/p11_independent_native_driver/parity_all_m_c1_curvature_author/PARITY_ALL_M_C1_FACE_INVERSE_FREE_CURVATURE_OBSERVER_AUTHOR.md, 13131 bytes, SHA256 1b0a3105eadb9e3dc59f12183b5dcc7a0bc28417e1707031d363d8f1c6902908. The original eleven Source inputs and all later local freeze/review artifacts are pinned in the context. Old whole-trace algebra already implicitly determines every coefficient; no generic inverse-free or standard spectral-method novelty is claimed. Stronger old finite m3..6 results are not counted anew. The sign-resolved uniform top face is the precise derived application requiring new peer review.

BFF6DC developed the uniform metric and ratio argument after freezing the V1 proof and before receiving any repair suggestion. F736 contributes only the merged scalar-boundary part to this version. Their original Driver histories and NONBLIND exposure remain intact. The old third-person V1 reviewer supplied no construction or repair for this new uniform proof; reading a review is not represented as new blind independence. Root routes the research and serializes Source but supplied no mathematical construction.

During this derivation BFF6DC received metadata for a separate F736 frozen global reflection working note, but did not read that new 7500-byte body or use it as an input. The local centered parity in Sections 4-5 is fully proved here; no external attestation of private reasoning chronology is claimed. Any future use of that other note must be separately disclosed.

This remains one strengthened c1 addendum, not multiple independent discoveries for its highest-a consequence, scalar obstruction and uniform tail. A genuine different nonauthor must examine the complete V2, all scale factors, the derivative-at-fixed-r0 issue, the uniform lambda endpoints, and the coefficient-defined threshold. No scientific program, Native vote, new Task, RA/SID change or shared Tool was created. The permanently stopped m7 compact branch and every old budget remain unchanged; no claim that its r=[7,8] interval is covered follows from an unevaluated R_m. The all-m parent Goal remains OPEN.
