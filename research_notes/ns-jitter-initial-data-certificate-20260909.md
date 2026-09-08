# Latent jitter: exact dissipation square and an initial-data certificate for full Navier–Stokes

Record ID: `FINDING-EM-PDE-JITTER-INITIAL-CERTIFICATE-20260909`
Type: `FINDING`
Status: `TESTING`
Mathematical status: `ORDINARY_PROOFS_PROVIDED / EXACT_FINITE_FOURIER_CHECKS / NOT_INDEPENDENTLY_REVIEWED / NOT_ARBITRARY_DATA_REGULARITY`
Date: `2026-09-09`
Researcher-ID: `EM-DIRECT-F00A51`
Research-Activity-ID: `RA-076944AE1950A916ACC95399`
Projects: `enterprise-math`
Sensitivity: `confidential`
Authority: global `3ad395d666b488e89f4e1cef56ec8fbdf9732a18`; EM `bdef46f3f0309f41c8c9837a2be55c3523328058`.
Parent: EM `research_notes/ns-viscous-jitter-budget-20260909.md`, immutable source commit `f797247d78e24ee8451c3df1f10e8b71f67958ff`.
Other exact parent: global `knowledge/projects/enterprise-math/pde-coherent-heat-packet-nonlinear-bootstrap-20260907.md` (Wiener reference-flow certificate; do not relabel that existing method as new).

## 0. Scope and value

Continue the explicit user-selected NS/BRC residual-amplification problem. P000 is unchanged. A3/FCC vectors below are the existing classical Fourier carrier; they are not a construction or empirical verification of native six-dimensional dynamics.

The previous combined energy was positive, but its continuation condition still involved injection along the unknown true solution. This note obtains an INITIAL-DATA sufficient condition: a small explicitly computable heat residual, including its phase cancellations, controls the ENTIRE perturbation equation. For one initial helicity, the latent-jitter Gram bounds that residual. For mixed initial helicities it does not, and an exact counterexample to that substitution is provided.

This is an application/refinement of established approximate-solution and nonlinear-smallness methods, not a novelty claim for large-data regularity in general. It does not prove that arbitrary initial data satisfy the condition.

All formulas use the normalized torus T^3=(R/2pi Z)^3, with Fourier series u=sum uhat(k)e^(ik.x), spatial measure dx/(2pi)^3, zero mean, real divergence-free fields, and viscosity nu>0. The analytic argument has the usual whole-space homogeneous counterpart. Existence/continuation statements are first made for smooth initial data; no endpoint rough-data claim is needed.

## 1. Notation and one explicit analytic constant

Let Lambda=(-Delta)^(1/2), P be Leray projection, and

B(f,g)=P((f.grad)g),  N(u)=-B(u,u)=P(u x curl u).

Fix ANY valid constant C0 for

||B(f,g)||_(Hdot^-1/2) <= C0 ||f||_(Hdot^1)||g||_(Hdot^1).       (1)

It may be chosen as the product of constants in Hdot^(1/2)->L3 and Hdot^1->L6 (including vector conventions). Indeed duality, Holder with exponents 6 and 2, and the L2-based contraction of P prove (1). C0 is fixed by the domain and normalization, independent of frequency, amplitude, and Fourier cutoff. No numerical value for C0 is claimed.

Write u=u_+ +u_-, curl u_s=s Lambda u_s, and

K=||u||_(Hdot^1/2)^2, Q=||u||_(Hdot^3/2)^2,
C_s(v)=[Lambda,v x]v=-v x Lambda v,
A=sum_s ||C_s(u_s)||_(Hdot^-1/2)^2.

With S(tau)=exp(-tau Lambda^2), set

J(u)=sum_s int_0^infinity ||C_s(S(tau)u_s)||_(Hdot^-1/2)^2 dtau,
I(u)=sum_s D J_s(u_s)[P_s N(u)].

The parent identities are

K'/2+nu Q=Pcrit,
Pcrit=2<Lambda u_+,C_-(u_-)>-2<Lambda u_-,C_+(u_+)>,
J'+nu A=I.                                                   (2)

All inner products below are real inner products, or real parts of complex pairings.

## 2. Exact positive square, not just the previous inequality

In the direct-sum L2 space define

X=(Lambda^(3/2)u_+, Lambda^(3/2)u_-),
Y=(Lambda^(-1/2)C_-(u_-), -Lambda^(-1/2)C_+(u_+)).

Then ||X||^2=Q, ||Y||^2=A, and Pcrit=2<X,Y>. For c>0 put

F_c=J+c nu^2 K.

Substitution into (2), followed by completing a square, gives EXACTLY

F_c' + nu ||Y-2c nu X||^2 + (2c-4c^2)nu^3 Q = I.             (3)

Thus c=1/4 maximizes the guaranteed Q coefficient within this constant-weight one-parameter family:

F=J+nu^2 K/4,
F' + nu ||Y-(nu/2)X||^2 + nu^3 Q/4 = I.                      (4)

F>=nu^2 K/4 globally. The square measures the mismatch between the visible commutator and the direction that would saturate its critical-energy pairing. It is not another omitted error term. The net source is I minus this nonnegative square. Positivity of F alone still does not imply monotonicity: no sign or arbitrary-data bound for I has been proved.

## 3. Full-feedback reference-flow certificate

Let v(t) be a prescribed smooth, zero-mean, divergence-free reference on [0,T), with

sup_(t<T)||v(t)||_(Hdot^1/2)<infinity,
int_0^T||v(t)||_(Hdot^3/2)^2dt<infinity.

Define its FULL equation residual

f=v_t+nu Lambda^2 v+B(v,v).

For the exact NS solution u, put w=u-v. No Fourier mode or feedback is removed:

w_t+nu Lambda^2 w+B(w,w)+B(v,w)+B(w,v)=-f.                    (5)

Set

Xw=||w||_(Hdot^1/2)^2, Yw=||w||_(Hdot^3/2)^2,
V=||v||_(Hdot^1), R=||f||_(Hdot^-1/2).

Pair (5) with Lambda w. By (1) and

||w||_(Hdot^1)^2 <= sqrt(Xw Yw),

one has

Xw'/2+nu Yw <= C0 sqrt(Xw)Yw
                 +2C0 V Xw^(1/4)Yw^(3/4)+R sqrt(Yw).         (6)

On Xw<nu^2/(16C0^2), absorb the first term by nu Yw/4. The exact scalar Young bounds are

2C0 V Xw^(1/4)Yw^(3/4)
 <=nu Yw/4+108 C0^4 nu^(-3)V^4 Xw,

R sqrt(Yw)<=nu Yw/4+R^2/nu.

Hence

Xw'+(nu/2)Yw <=216 C0^4 nu^(-3)V^4 Xw+(2/nu)R^2.             (7)

### Theorem R1

Define

S_T=int_0^T V^4dt,
R_T=int_0^T R^2dt,
L_T=[Xw(0)+(2/nu)R_T] exp(216 C0^4 S_T/nu^3).

If

L_T < nu^2/(16C0^2),                                        (8)

then u is smooth on [0,T) with a uniform critical bound and finite critical dissipation; a finite endpoint T is extendible.

Proof: a first-exit argument and the integrating factor for (7) give, for every t<T,

Xw(t)+(nu/2)int_0^tYw <=L_T.

The strict inequality (8) prevents reaching the bootstrap boundary. Together with the stated reference bounds this controls K(u) uniformly and int Q(u). Interpolation and Sobolev give

||u||_6^4<=C ||u||_(Hdot^1)^4<=C K(u)Q(u).

Thus u lies in L_t^4 L_x^6 at every candidate finite endpoint, and classical Prodi–Serrin continuation applies. For a reference on [0,infinity) satisfying (8) with T=infinity, the solution is global. Smooth local existence is used only to start the bootstrap, not assumed for all time.

The constant 108 is conservative but exact for the displayed scalar allocation: maximize b y^(3/4)-(nu/4)y with b=2C0 V Xw^(1/4). No unspecified endpoint multiplication theorem is being used.

## 4. Initial data only: the heat-residual Gram

Take v(t)=exp(-nu t Lambda^2)u0 and w(0)=0. Define the unit-generator full heat residual

Rcal(u0)=int_0^infinity ||N(S(tau)u0)||_(Hdot^-1/2)^2 dtau.     (9)

Then R_infinity=Rcal/nu. Also, along the heat reference,

||v||_(Hdot^1)^4<=K(v)Q(v),  K(v)'=-2nu Q(v),

so

S_infinity<=K(u0)^2/(4nu).                                   (10)

### Corollary R2: all initial helicity configurations

A sufficient condition for the full smooth NS solution to be global is

Rcal(u0) exp[54 C0^4 K(u0)^2/nu^4] < nu^4/(32C0^2).          (11)

Both quantities are functions of the initial data alone. The exponential is a conservative perturbative penalty for the reference flow; it is not a fundamental law or a sharp threshold.

For finite Fourier data, group the source by output k AND input rate sigma:

A_(k,sigma)=sum_(p+q=k, |p|^2+|q|^2=sigma)
            -i P_k[(uhat0(p).q) uhat0(q)].

Then exactly

Rcal=sum_(k!=0) |k|^-1 sum_(sigma,tau)
      Re<A_(k,sigma),A_(k,tau)>/(sigma+tau).                   (12)

This positive Gram retains all same-output phase interference and unequal-rate cross terms. It is computable without evolving the unknown true solution.

### Corollary R3: latent jitter certifies one initial helicity

If initially P_-u0=0 (or symmetrically P_+u0=0), then the heat reference stays in that sector and

N(S(tau)u0)=-P C_+(S(tau)u0),
Rcal(u0)<=J(u0).

Consequently the INITIAL-DATA condition

J(u0) exp[54 C0^4 K(u0)^2/nu^4] < nu^4/(32C0^2)               (13)

implies global regularity of the FULL equation. Subsequent generation of the other helicity is allowed and is controlled by (5)-(8). This is not a helical-decimated equation or an assumption of preserved purity.

### Important boundary: mixed helicities

Initial J=0 does not make the heat reference an exact solution if both helicities are present. For

u0=(1,1,0)cos(x1-x2)+(0,0,1)cos(x1+x2),

both initial sectors are single-shell, hence J(u0)=0, but

N(u0)=(0,0,1)[sin(2x1)+sin(2x2)],
Rcal(u0)=1/16 >0.                                          (14)

Thus replacing Rcal by J in (11) without the initial one-helicity hypothesis would erase a genuine source. Equation (14) refutes that replacement, not global smoothness of this particular example.

## 5. Exact rank-three A3 family, with nonzero opposite-helicity birth

For k having one zero coordinate, let e(k) be the corresponding coordinate unit vector and

h_+(k)=[e(k)+i k x e(k)/|k|]/sqrt(2).

This is a unit positive-helicity polarization. Define real fields a,b by their positive-frequency coefficients:

a_hat(k)=h_+(k), k=(1,1,0),(1,0,1),(0,1,1),
b_hat(2,-2,0)=h_+(2,-2,0),

with conjugate negative modes and no other coefficients. The three frequencies of a have rank three. Every initial direction is an A3/FCC root ray. Let

u0=A a+B b,  A>0, B>0.

The two radii are sqrt(2) and 2sqrt(2). Each block separately has zero Euler nonlinearity. Their interaction is

C(u0)=-sqrt(2) A B (a x b).

It has one input heat rate sigma=2+8=10. Exact calculation gives

K(u0)=sqrt(2)(6A^2+4B^2),
J(u0)=cJ A^2 B^2,
Rcal(u0)=cR A^2 B^2,                                      (15)

where

cJ=sqrt(14)/80+3sqrt(10)/100+sqrt(6)/16
   =0.29473215606367426...,

cR=3sqrt(14)/245+7sqrt(10)/250+sqrt(6)/20
   =0.2568344745231463... .                                 (16)

There are 12 nonzero first nonlinear outputs, on squared radii {6,10,14}. The generated negative-helicity part is nonzero; at A=B=1 its squared Hdot^-1/2 source norm is

-117sqrt(2)/70+6sqrt(14)/49+7sqrt(10)/25+sqrt(6)/2>0.

Therefore this is not a single-shell heat solution and not a trajectory constrained to the initial helicity.

For every finite A, choose B>0 sufficiently small to satisfy

cJ A^2B^2 exp[54 C0^4 {sqrt(2)(6A^2+4B^2)}^2/nu^4]
 <nu^4/(32C0^2).                                           (17)

The resulting full NS solution is global by R3. Thus the certificate permits arbitrarily large amplitude in a genuine rank-three A3 family, at the cost of a possibly extremely small off-shell component. Replacing cJ by cR gives the sharper R2 certificate.

This is not arbitrary-data regularity: the size of B is restricted and may have to be exponentially small in A^4. Similar large-data/small-nonlinearity themes are established in the literature. The result-specific value is the explicit latent-jitter/heat-Gram interface and the exact A3 coefficients.

## 6. Finite response trees can certify their entire omitted tail

Define the homogeneous Duhamel responses

v1=exp(-nu t Lambda^2)u0,
(vn)_t+nu Lambda^2 vn=-sum_(i+j=n)B(vi,vj), vn(0)=0, n>=2.

For V_m=sum_(n=1)^m vn, its EXACT residual is

f_m=sum_(1<=i,j<=m, i+j>m) B(vi,vj).                        (18)

Apply R1 to V_m, not to an assumption that sum_(n>=1)vn converges. The remainder w=u-V_m satisfies the full quadratic equation (5). A successful inequality (8) controls all its modes and all subsequent feedback.

For finite initial Fourier support and finite m, all vn are finite sums of vector coefficients times t^ell exp(-nu sigma t), with sigma>0. The squared residual action and int ||V_m||_(Hdot^1)^4 are exact integrals of such finite packets. Resonant polynomial powers are retained rather than discarded. This gives a practical route to certified examples and comparison of references.

No proof is provided that increasing m always makes (8) succeed, or that it handles every initial state. Infinite-tree convergence is not inferred from finite Gram positivity. The present checker verifies the finite residual indexing identity, not a universal convergence algorithm.

## 7. Reuse, checks and confidence

BRC population: labeled ordered Fourier input pairs, their common output, input heat rate, helical labels and complex amplitude; for response references, retain generation and time-polynomial degree as well. Quotient only after same-output/same-rate coherent contraction; square through the complete Gram.

`REUSE_EXECUTED`: unchanged inherited Fourier implementation, SHA256 `ac6a0a34994c85832bde55e38e195e9552df308906f1a4c4460d3dbdafb1db59`.
`COMPOSE_APPLIED`: the existing latent heat Gram, full-feedback reference-flow method, Sobolev bilinear inequality, explicit scalar Young bounds and the continuation interface.
`NOT_APPLICABLE`: positive mass replacing phase, finite checks proving infinite-scale convergence, or the one-helicity source identity used for mixed initial sectors.

The checker verifies (3), c=1/4 optimization, constants 108/216/54, all polarizations and full nonlinear outputs for (15)-(16), the nonzero opposite-helicity source, the exact counterexample (14), and residual indexing through m=5. No numerical NS time simulation is used. These finite checks support the algebra; the analytic proof of R1 is Sections 1-4, not an extrapolation from the example.

## 8. Literature boundary and next unit

Chemin and Gallagher, *Wellposedness and stability results for the Navier–Stokes equations in R^3*, Ann. IHP ANL 26 (2009), 599-624, DOI 10.1016/j.anihpc.2007.05.008, establishes an important large-data nonlinear-smallness/stability framework. Primary page: https://ems.press/journals/aihpc/articles/4076654 .

Chernyshenko, Constantin, Robinson and Titi, *A Posteriori Regularity of the Three-dimensional Navier-Stokes Equations from Numerical Computations*, arXiv:math/0607181, establishes approximate-solution certification as a rigorous research approach. https://arxiv.org/abs/math/0607181 .

The classical Prodi–Serrin continuation interface is the same (time,space)=(4,6) criterion used in the parent. These sources establish context and standard continuation, not independent verification or priority of this note's calculations.

The next useful comparison is a finite reference V_m versus the heat reference: can preserving the A3/helicity/phase cancellations make its exact residual action sufficiently smaller WITHOUT making the reference-growth exponential worse? The arbitrary-data obstruction remains a uniform, initial-data-controlled estimate. This note closes a nontrivial sufficient class, not that universal estimate.
