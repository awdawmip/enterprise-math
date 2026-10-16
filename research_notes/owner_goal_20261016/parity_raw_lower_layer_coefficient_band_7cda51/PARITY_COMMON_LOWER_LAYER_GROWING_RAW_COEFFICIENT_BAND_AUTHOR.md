# A growing raw-coefficient band in the COMMON Parity lower layer

Status: FROZEN_AUTHOR_PAPER_CANDIDATE_UNREVIEWED.

Author: EM-PUBLIC-7CDA51. This is new author work after the completed independent review of the older one-coefficient paper. That older peer judgment does not accept the present extension. All prior authorship, review and CONTROL exposure remains NONBLIND. No scientific program, sample, matrix evaluation or coefficient-generation artifact is used.

## 1. The precise layer and proposed range

Use the original COMMON normalization, without any nonconstant gcd cancellation:

P(c)=(x+Wc+beta)G_W(x)T(c)/c, P1=[c]P,
W=m^2, beta=(W+1)/2, x=W(S+a).

The original physical parameters remain S>=0,a>0; coefficient extraction is in the polynomial variables S,a. Put h=beta/W, Q(sigma,a)=P1(sigma-h,a), D=W-1 and d=W-3. Let H_d^raw be the degree-d homogeneous component of P1. The old result determines just [S^(W-4)a]P1, alongside its negative centered counterpart. Here the intended statement is a uniform range, not a sequence of separately counted j cases:

For every integer m>=7 and every integer 0<=j<=floor(m/6),

A_(m,j):=[S^(d-j)a^j]H_d^raw >0.                         (1)

In fact the proof below gives the explicit margin

A_(m,j) >= K binom(d,j)m^6(m^3/40-m/6-7/2)>0,
K=m^(2W)/2.                                             (2)

The range grows with m. The old j=1 theorem remains old coverage; its inclusion where applicable is not counted again. No coefficient with j>floor(m/6), other homogeneous layer, full P1 coefficientwise positivity, physical-domain trace sign or all-M Goal is settled. This is not an actual numerical coefficient computation, a new Tool or a new Task.

Three frozen background papers are used with their exact Source identities: original13131B P1/COMMON proof at ac9f1c0ffcfbb7ad5564721442480ad8e2236b83, old16649B V2 frame/top-face proof at65a880f63fce7488f5c3af126fa42e18a6a90a1f, and21245B lower-layer paper at89771a21e47aaff2407985b7dc62adffa88a67b7. Full paths/hashes and own actual Source consumption belong in the context. The following proof imports no new external theorem: the weighted derivative estimate and formal majorant are proved here.

## 2. What is already known, and the actual new question

Let V=Q[u]_(degree<=m-2), n=m-1, J=d/du. Retain the nondegenerate residue Gram form

M(f,g)=[u^(m-1)]f(u)g(u)(1+u)^(-m).

The irrelevant scalar kappa in the original limiting Gram matrix cancels from adjoints and compression. A star denotes this M-adjoint. In the exact rescaled secant frame, after differentiating at fixed original r0,

Z_lambda=uJ-(m-1/2)I+gamma_lambda(J), R_lambda=Z_lambda+Z_lambda*,
gamma_lambda(J)=(1/lambda)[exp(lambda J)f(lambda J)^(-1)-I],
f(z)=(exp z-1)/z=sum_(k>=0)z^k/(k+1)!.

All expressions are finite on V: J^(m-1)=0, f(lambda J)-I is nilpotent and the inverse terminates. At lambda=0 use the removable value gamma_0=J/2. Thus Z0=(u+1/2)J-(m-1/2)I.

Put

B(lambda)=tr(R_lambda^2)+W-1,
tau=(m^4-1)/(24m), g=(W^2-1)/24=m tau,
A=B_(1/u^2),
C(lambda)=2tau tr(A[Z_lambda,R_lambda])-4tau tr(A R_lambda),
F(lambda)=C(lambda)-g(B(lambda)+2).                       (3)

Here B_(1/u^2) means the residue compression, not the polynomial B(lambda). Formula(3) is the full version of the already known lower-layer readout: cyclicity converts tr(R[Z*,B_metric]) to tr(B_metric[Z,R]); reflection permits the trace-level replacement B_metric ->tau A. It is not a matrix equality. The old theorem's exact trace also gives

B0:=B(0)=m(3m-2)(m+1)/2,
(3/2)m^3<=B0<=2m^3.                                    (4)

The known centered metric/scalar parity and polynomiality give homogeneous degrees D,D-2,D-4,... only. The actual old top layer has prefactor m^2K, whereas the lower layer has prefactor K:

H_D=m^2K(sigma+a)^D B(a/(sigma+a)),
H_d^centered=K(sigma+a)^d F(a/(sigma+a)).

Translating sigma=S+h, the degree-d component receives exactly the old lower layer and h^2 partial_S^2 H_D/2. Therefore

H_d^raw=K(S+a)^d Psi(a/(S+a)),
Psi=F+alpha[D(D-1)B-2(D-1)lambda B'+lambda^2B''],
alpha=(W+1)^2/(8W).                                    (5)

This composition itself is not new. The new proof is a uniform coefficient-functional margin for this particular Psi. Pointwise Gram positivity alone cannot give it: if L_(d,j)(lambda^k)=(j)_k/(d)_k and t=j/d, then L((lambda-t)^2)=-t(1-t)/(d-1)<0 for0<j<d. A nonnegative square can have a negative coefficient-functional value.

## 3. The positive contour form and two finite weighted estimates

Use the real contour u=-1/2+iv, v real. Residue closure, with the same degree cutoff as the old Gram construction, identifies M(f,I g), up to one nonzero real scalar independent of f,g, with

<f,g>_+=integral_R f(-1/2+iv) overline(g(-1/2+iv))
                     (1+4v^2)^(-m) dv,
I g(u)=g(-1-u).

More explicitly, for complex coefficients the residue expression is c_m M(f,I overline_coeff(g)), with c_m a nonzero real scalar chosen to make it positive. Conjugation of the value on the contour is exactly I followed by coefficient conjugation. The integrand decays at least as v^(-4), so closing the contour introduces no residue at infinity. The same argument applies to the rational multipliers1/u^2 and1/(1+u)^2, whose poles remain off the contour. This is an auxiliary finite-dimensional positive form, not positivity of the original finite-rho metric.

If a real operator X commutes with I, its M-adjoint is its positive Hermitian adjoint. Indeed the positive form is a scalar multiple of M(f,I g), and I commutes with X. Both Z0 and E_lambda:=gamma_lambda(J)-J/2 commute with I. For the latter, f(-z)=exp(-z)f(z) shows that exp(z)/f(z)-1-z/2 is even in z, so E contains only even powers of J. Thus every coefficient of Z_lambda and R_lambda has this adjoint compatibility.

Let || || be the operator norm for this positive form. On the contour, J=-i partial_v and Z0=v partial_v-(m-1/2)I. To bound derivatives without a new primary import, put w=(1+4v^2)^(-m) and define on polynomials of degree<=m-2

L f=-(1+4v^2)f''+8(m-1)v f'.

Integration by parts gives <f,Lf>_+=integral(1+4v^2)|f'|^2w. Boundary terms vanish at the declared polynomial cutoff. L is self-adjoint, preserves degree, and its triangular diagonal in monomials is

ell_k=4k(2m-1-k), 0<=k<=m-2.

These eigenvalues are distinct and increasing in that range. Finite-dimensional self-adjointness and the triangular characteristic polynomial give

integral(1+4v^2)|f'|^2w <=4(m-2)(m+1)||f||_+^2<4m^2||f||_+^2.

Consequently

||J||<=2m, ||v partial_v||<=m, ||Z0||<=2m.                (6)

No matrix spectrum at a sampled m is used.

Two multiplier bounds are also needed. The old residue integration-by-parts identity gives

R0=(m/2)B_(1/[u(1+u)]).

On the contour,1/[u(1+u)]=-4/(1+4v^2), so R0 is the positive-Hermitian orthogonal compression of that real multiplier times m/2. Hence

||R0||<=2m.                                             (7)

Let A_e=(A+IAI)/2. It is orthogonal compression of the real part of1/u^2 on the contour, bounded in absolute value by4. Thus

||A_e||<=4.                                            (8)

Every X used against A in(3) commutes with I. Therefore tr(AX)=tr(A_eX). The proof never claims A=A_e or uses a positive-Hermitian norm bound4 for an unrelated uncompressed operator.

## 4. A coefficient norm and a majorant for the actual finite frame

For a matrix polynomial X(lambda)=sum X_k lambda^k define

N_xi(X)=sum ||X_k||xi^k, xi>=0.

It is submultiplicative; for the compatible adjoints it is unchanged by star. For a scalar polynomial, use the same notation with absolute values. Trace estimates follow from |tr X|<=n||X||. This coefficient norm is not an assertion that L_(d,j) is positive.

Fix a target j in(1), and set xi=j/d, u0=xi||J||. First consider xi>0. By(6),

u0<=2m xi<=m^2/[3(m^2-3)]<=3/8,                         (9)

where the last inequality follows from m^2>=27. To control E_lambda use the exact formal identity

E_lambda=(1/lambda)N(lambda J)f(lambda J)^(-1),
N(z)=exp z-(1+z/2)f(z)
    =sum_(k>=2)(k-1)z^k/[2(k+1)!].

The coefficients displayed for N are nonnegative and at most1/12. Also1/(k+1)!<=1/2^k for k>=1. Therefore the finite polynomial expressions, bounded by convergent scalar majorants, give

N_xi(f(lambda J)-I)<=u0/(2-u0),
N_xi(N(lambda J))<=u0^2/[12(1-u0)],
N_xi(f(lambda J)^(-1))<=(2-u0)/(2-2u0).

The inverse is actually finite because of nilpotence; bounding it by the larger geometric series introduces no analytic assumption about an infinite operator inverse. Combining these estimates,

delta:=N_xi(E_lambda)
 <=u0^2(2-u0)/[24xi(1-u0)^2]
 <=(13/75)xi||J||^2
 <=(26/225)m^3/(m^2-3)
 <=m/8.                                                (10)

The scalar function(2-u)/(24(1-u)^2) increases on0<=u<=3/8 and its endpoint value is13/75. The last inequality in(10) is17m^2>=675, valid for m>=7. At xi=0, E has zero constant coefficient, so delta=0 and the same bound applies by its removable limit. No Bernoulli coefficient table or asymptotic estimate is needed.

The actual nilpotent cutoff has been retained throughout. Z_lambda and R_lambda have degree at mostm-3, and B,C,F,Psi have degree at mostq=2m-6<d. This upper bound is sufficient; it is not a continuation of a fixed small-m matrix or endpoint formula into missing degrees.

## 5. Uniform scalar bounds for the whole layer

Put E_R=E_lambda+E_lambda*. Equations(6)-(10) yield

N_xi(Z)<=17m/8, N_xi(R)<=9m/4, N_xi(E_R)<=2delta.

Since B-B0=tr(R0E_R+E_RR0+E_R^2),

N_xi(B-B0)<=8nm delta+4n delta^2
             <=(17/16)n m^2<=(17/16)m^3.                (11)

Together with(4), this gives the useful positive margin

B0-N_xi(B-B0)>=(7/16)m^3.                              (12)

For C, use tr(AX)=tr(A_eX), ||A_e||<=4, and the submultiplicative coefficient norm:

N_xi(C)<=16tau n N_xi(R)(N_xi(Z)+1).

For m>=7,17m/8+1<=7m/3, and tau<=m^3/24. Thus

N_xi(C)<=84tau n m^2<=(7/2)m^6.                        (13)

Also N_xi(B)+2<=2m^3+(17/16)m^3+2<=4m^3, whence

g(N_xi(B)+2)<=m^7/6.                                   (14)

The complete C(lambda), including all its nilpotent higher powers and cross traces, is bounded here. This avoids falsely treating the old six traces, which determine only F0 and F'0, as an all-coefficient elimination.

## 6. The coefficient-functional margin

If Psi=sum psi_k lambda^k, direct homogeneous extraction in(5) gives

A_(m,j)/(K binom(d,j))=L_(d,j)(Psi),
L_(d,j)(lambda^k)=(j)_k/(d)_k.

For0<=k<=q<d these numbers lie in[0,xi^k]; when k>j the numerator is zero. The inequality follows factor by factor from(j-l)/(d-l)<=j/d for0<=l<k<=j. Thus arbitrary scalar coefficients can be bounded by their absolute coefficient norm, without any positivity assumption about L on squares.

The differentiated top-face operator in(5) is diagonal on lambda^k, with weight(D-k)(D-k-1). Since0<=k<=q<=D-2,

0<=(D-k)(D-k-1)<=D(D-1).

Separate the constant coefficient B0 and bound every other coefficient in absolute value. Using(3),(5),(11)-(14),

L_(d,j)(Psi)
 >=alpha D(D-1)[B0-N_xi(B-B0)]
    -N_xi(C)-g[N_xi(B)+2]
 >=alpha D(D-1)(7/16)m^3-(7/2)m^6-m^7/6.                (15)

For W=m^2>=49, alpha>=W/8 and(W-1)(W-2)>=W^2/2. Hence alpha D(D-1)>=m^6/16. Since7/256>=1/40, (15) implies

L_(d,j)(Psi)>=m^9/40-m^7/6-(7/2)m^6
              =m^6(m^3/40-m/6-7/2)>0.

The last strict inequality needs no scan: m^3>=49m and m>=7 give

m^3/40-m/6-7/2 >=127m/120-7/2>=469/120>0.

Multiplication by the positive K binom(d,j) proves(1)-(2). Every constant is independent of the target j and of m within the specified range. The argument handles the whole growing band as one unit, not isolated extra coefficients.

## 7. Scope, prior route and remaining gap

The earlier direct pointwise-Gram-to-coefficient route was correctly killed; this proof does not revive it. It uses a quantitative absolute-coefficient margin for the actual nilpotent frame at xi=j/d, with small xi||J|| uniformly guaranteed by j<=m/6. For larger j the displayed smallness bound no longer holds, and no extrapolation is made. This is a theorem candidate for a growing edge band of one homogeneous layer, not for its middle coefficients or the full all-M problem.

No m2..6 theorem is recounted, no stopped m7 execution is restarted, and no source normalization, observer, fixed field or parameter family is altered to obtain the conclusion. The variables on the contour and in the coefficient functional are auxiliary external algebraic/analytic parameters, not a new physical dimension or physical time.

The author has performed only paper derivation and administrative text/hash/Source-custody work. Scientific programs, imports, AST, compilation, tests, samples, solvers, matrix evaluations and generated coefficient expansions are zero. M7 permanent STOP, fixed233 STOP, core98 HOLD and original budgets remain unchanged. No Native vote, Task/Goal closure or new Tool is claimed. A genuinely nonauthor whole-proof review of the final frozen main/interface/context is required before ordinary acceptance; the original author's previous peer vote is not that review.
