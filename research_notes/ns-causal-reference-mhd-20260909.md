# Causal coherent residual certificates, damped references, and an MHD transfer

Record-ID: FINDING-EM-PDE-CAUSAL-REFERENCE-MHD-20260909
Status: TESTING / ORDINARY_PROOFS_AND_EXACT_FINITE_CHECKS / NOT_INDEPENDENTLY_REVIEWED
Researcher-ID: EM-DIRECT-F00A51
Research-Activity-ID: RA-076944AE1950A916ACC95399
Date: 2026-09-09
Authority: global c8c2340964a2d4be76e17843473cd897c30ebb46; EM 2886f23cb2199f37827ed87cec5999db4716725c.
Parent: research_notes/ns-jitter-initial-data-certificate-20260909.md, blob db3a72e6203398e3a876b31a0285679a21e6e131.

## 0. Scope and attribution

Continue the user-selected NS/BRC project. P000 is unchanged; A3/FCC below is the existing classical Fourier carrier, not a construction of native X6 dynamics. This record extends an existing result-specific method, not the accepted BRC Foundation or a new top-level toolbox family. It proves an abstract stability interface, an improved causal certificate, exact damped-reference improvement for specified NS families, and application to equal-viscosity/resistivity incompressible MHD. It does NOT prove arbitrary-data global regularity of either PDE.

Approximate-solution/control-inequality methods for NS already exist (Morosi-Pizzocchero, arXiv:1104.3832). The MHD analogue also already exists (Pizzocchero-Tassi, arXiv:1905.13722). Large-data/nonlinear-smallness NS methods already exist (Chemin-Gallagher, arXiv:math/0508374 and math/0611044). No priority claim is made for these general ideas. The present concrete contribution is the critical-norm, heat-packet, damped-reference composition and the exact examples below.

All concrete computations use the normalized torus (R/2pi Z)^3, zero-mean real divergence-free fields. Fourier coefficients are normalized so L2 squared is their squared sum. C0 is a PROVEN constant for ||B(f,g)||_-1/2 <= C0||f||_1||g||_1, B(f,g)=P((f.grad)g). A numerical C0 is not certified in this record.

## 1. Abstract critical-scale interface

Let Lambda be a positive self-adjoint generator on a Hilbert space and E_s its Hilbert scale, with ||w||_1^2 <= ||w||_1/2 ||w||_3/2. Let a bilinear map B satisfy

||B(f,g)||_-1/2 <= C0 ||f||_1 ||g||_1.                         (1)

Consider U_t+nu Lambda^2 U+B(U,U)=0, nu>0. Smooth local existence and a continuation principle must be supplied for each concrete equation; the abstract inequality does not create those hypotheses.

For a prescribed smooth reference V define the FULL residual

f=V_t+nu Lambda^2 V+B(V,V), W=U-V.

Then exactly

W_t+nu Lambda^2 W+B(W,W)+B(V,W)+B(W,V)=-f.                 (2)

Write X=||W||_1/2^2, Y=||W||_3/2^2, r=||f||_-1/2. Pairing with Lambda W gives

X'/2+nu Y <= C0 sqrt(X)Y+2C0||V||_1 X^(1/4)Y^(3/4)+r sqrt(Y).

On X<h^2, h=nu/(4C0), the parent's exact Young allocation gives

X'+nu Y/2 <= a(t)X+2r(t)^2/nu,
a(t)=216 C0^4 nu^-3 ||V(t)||_1^4.                         (3)

Proof: the three nonlinear/source terms cost nu Y/4 each; the middle Young remainder is 108 C0^4 nu^-3 ||V||_1^4 X before doubling. No feedback mode is omitted.

## 2. Causal weighted certificate and restarts

Define A(t)=int_0^t a(s)ds and

Z(t)=exp(A(t))*[X(0)+(2/nu)int_0^t exp(-A(s))*r(s)^2 ds].   (4)

An integrating factor in (3) proves

X(t)+(nu/2)int_0^t exp(A(t)-A(s))*Y(s)ds <= Z(t).           (5)

Since a>=0, Z is nondecreasing and the integral on the left is at least int Y. If A(T)<infinity and Z(T)<h^2, a first-exit argument keeps (3) valid, gives sup X<h^2 and int Y<infinity. With a reference bounded in E_1/2 and square-integrable in E_3/2, the exact solution inherits these bounds. For NS, interpolation gives ||U||_6^4 <= C K(U)Q(U), hence Prodi-Serrin continuation at a finite endpoint. Infinite-horizon bounds prove global continuation by the same argument at every candidate finite endpoint.

The previous sufficient bound was

Z_old(T)=exp(A(T))*[X(0)+(2/nu)int_0^T r(s)^2ds].

Equation (4) is no larger: a residual born at s is amplified only over [s,T], not retrospectively over [0,s]. For example if a=a0 on [0,t0] and a=0 later, while all forcing is after t0 and X(0)=0, then Z=2 int r^2/nu whereas Z_old=exp(a0*t0)Z. This is an exact scalar-estimator comparison, not a constructed arbitrary NS orbit.

At a change of reference at t_j, a certified radius e bounds the new error by

e_new <= e+||V_old(t_j)-V_new(t_j)||_1/2.                  (6)

Use its square as the next X(0). A restart must not reset the unknown error to zero. Finite certified windows can be glued this way; infinitely many windows need a separate uniform budget.

## 3. Weighted heat-rate Gram

Suppose a finite residual is represented as

fhat(k,t)=sum_(sigma,m) F_(k,sigma,m) t^m exp(-nu sigma t),

with sigma>0 and integer m>=0. Retain output, rate, polynomial degree, components, and complex phase before compression. For any nonnegative scalar weight w(t),

int_0^T w(t)||f(t)||_-1/2^2dt
= sum_(k!=0) |k|^-1 sum_(sigma,m),(tau,n)
  Re<F_(k,sigma,m),F_(k,tau,n)> G_(sigma,m;tau,n),

G_(sigma,m;tau,n)=int_0^T w(t)t^(m+n)exp[-nu(sigma+tau)t]dt. (7)

G is positive semidefinite by its integral Gram representation, not by signs of individual off-diagonal entries. For w=1,T=infinity,

G=(m+n)!/[nu(sigma+tau)]^(m+n+1).                          (8)

For finite T replace (8) by its exact incomplete-gamma / finite exponential-sum expression. For (4), use w=exp(-A(t)); positivity survives although entries generally are not rational functions. The current executable implements exact unweighted positive-integer-rate packets; rigorous numerical integration of general causal weights remains an extension, not a claimed executed feature.

## 4. Damped first response: why full inclusion is not automatically better

Let v1 be the heat flow and v2 its first nonlinear Duhamel response, with v2(0)=0 and (partial_t+nu Lambda^2)v2=-B(v1,v1). For a constant theta in [0,1], use

V_theta=v1+theta v2.

Its FULL residual is

f_theta=(1-theta)B(v1,v1)+theta[B(v1,v2)+B(v2,v1)]
         +theta^2 B(v2,v2).                               (9)

Thus the unweighted residual action is a quartic polynomial in theta with Gram coefficients. The reference action S_theta=int ||V_theta||_1^4 is also a finite quartic polynomial. The parent zero-initial-error certificate score is

L(theta)=(2/nu)R_theta exp(216 C0^4 S_theta/nu^3).          (10)

Choosing theta by R_theta alone is not sufficient: the reference amplification factor also changes. Including theta=0 in a validated search prevents selecting a reference worse than the original heat one; failure of the test is not evidence of PDE blow-up.

### 4.1 Completely explicit benchmark

Take u0=A*u_*, with

u_*=(1,1,0)cos(x1-x2)+(0,0,1)cos(x1+x2).

Set q=A/nu and tau=nu*t. Its unit first response is

v2/Aq=tau exp(-4tau)(0,0,1)[sin(2x1)+sin(2x2)].

Exact full Fourier calculation gives, with c=(sqrt(2)+1/sqrt(10))/864,

R_theta/nu^3 = r_theta=q^4(1-theta)^2/16+c q^6 theta^2,
S_theta/nu^3 = s_theta=9q^4/8+q^6 theta^2/36+3q^8 theta^4/8192. (11)

The v2 self-interaction vanishes, but B(v1,v2) is retained and has six modes. Source terms in the two pieces have disjoint supports, which proves their integrated cross Gram is zero. The reference H1 pairing v1-v2 vanishes as well. Independent packet calculations verify (11).

At q=1, R_1/R_0=0.03204520978499876; at q=8 it is 2.0508934262399205. Thus a full next-order correction can actually worsen the residual. These ratios do not use any unproved numerical Sobolev constant. This field has only two-dimensional spatial dependence and serves as a certificate benchmark, not a new global-regularity example.

Nevertheless there is an explicit rigorously improving damping. Define

d=16c q^2,
D=1+d+6C0^4 q^6+(81/1024)C0^4 q^8,
theta_safe=1/D.

For q,C0>0, D>1. From log(x)<=x-1 and theta^4<=theta^2 on [0,1],

log[L(theta)/L(0)] <= -2theta+D theta^2.

Therefore

boxed: L(theta_safe)/L(0) <= exp(-1/D)<1.                 (12)

This improves the full certificate, not merely the residual. It does not say the improved score passes the threshold.

### 4.2 The preceding genuinely rank-three NS A3 family also improves

Use the parent's unit positive-helicity coefficients at a's frequencies (1,1,0),(1,0,1),(0,1,1), and b's frequency (2,-2,0), plus conjugates. Let u0=Aa+Bb with A,B>0. Its first nonlinear source has 12 packets at rate 10; v2 has 20 packets. The mixed v1-v2 source has 130 packets at A=B=1.

The exact certificate separately verifies

<H1 v1,H1 v2>(t)=0 for every t,
int <N2,N3_a>_-1/2 dt=0,
int <N2,N3_b>_-1/2 dt=0,

where the subscript a/b distinguishes which component of v1 drives the next response. These identities therefore hold for arbitrary A,B, not only A=B. Differentiating (9)-(10) at theta=0 gives

boxed: (d/dtheta)log L(theta)|_0=-2.                     (13)

For every fixed A,B,nu,C0>0, some sufficiently small positive theta strictly improves the heat-reference score. This also gives a strict enlargement of the sufficient region: on each nonzero shape's amplitude ray the heat score is continuous, strictly increasing from zero to infinity, so its boundary point becomes interior to a suitable damped-reference certificate. No universal amount of enlargement or arbitrary-data algorithm is asserted.

## 5. Transfer to incompressible MHD with equal diffusivities

Take viscosity and magnetic diffusivity both nu>0, constant density, magnetic field in velocity units, and define Elsasser variables z_+=u+b,z_-=u-b. Their projected equations are

(z_+)_t+nu Lambda^2 z_+ +B(z_-,z_+)=0,
(z_-)_t+nu Lambda^2 z_- +B(z_+,z_-)=0.                    (14)

For U=(U_+,U_-), V=(V_+,V_-), define

B_E(U,V)=(B(U_-,V_+),B(U_+,V_-)).

In the direct-sum Sobolev norms,

||B_E(U,V)||_-1/2^2
<=C0^2[||U_-||_1^2||V_+||_1^2+||U_+||_1^2||V_-||_1^2]
<=C0^2||U||_1^2||V||_1^2.                                (15)

Thus the abstract certificate transfers with the SAME admissible C0. This is a checked interface, not a helicity-to-Elsasser identification. Smooth local existence is the standard MHD input. The needed continuation also follows directly: testing each equation with -Delta z_s bounds its convection by

C||z_-s||_6 ||grad z_s||_2^(1/2)||Delta z_s||_2^(3/2)
<=nu||Delta z_s||_2^2/2+Cnu^-3||z_-s||_6^4||grad z_s||_2^2.

Bounded critical norm and integrated critical dissipation give int(||z_+||_6^4+||z_-||_6^4)<infinity; Gronwall controls H1 and yields smooth continuation.

With K_E=||Z0||_1/2^2 and R_E=int_0^infinity ||B_E(S(tau)Z0,S(tau)Z0)||_-1/2^2dtau, the inherited heat-reference argument gives

R_E exp(54 C0^4 K_E^2/nu^4)<nu^4/(32C0^2)                 (16)

as a sufficient condition for global smooth MHD. Neither arbitrary-data MHD nor unequal-diffusivity MHD is claimed.

### 5.1 Exact rank-three A3 near-Alfvenic example

Set

F=(1,-1,0)cos(x1+x2)+(1,0,-1)cos(x1+x3)
  +(0,1,-1)cos(x2+x3),
G=(1,1,0)cos(x1-x2),
z_+(0)=A F, z_-(0)=B G.

All are real, mean zero, divergence free and on the same radius sqrt(2); F's frequencies have rank three. Exact convolution gives

K_E=sqrt(2)(3A^2+B^2),
R_E=c_E A^2B^2,
c_E=11sqrt(6)/576+3sqrt(2)/64+1/8>0.                      (17)

Each residual output channel has 12 nonzero packets, all at input heat rate 4. Thus for A,B>0 the dynamics is not just the zero-residual Alfvenic heat flow. For every fixed finite A, choosing a sufficiently small nonzero B satisfies (16). This is a rigorously specified restricted large-amplitude class, not new priority for the general near-Alfvenic stability idea.

## 6. Reuse, verification and unresolved step

REUSE_EXECUTED: the inherited Fourier convolution/heat-response implementation, full-file SHA256 ac6a0a34994c85832bde55e38e195e9552df308906f1a4c4460d3dbdafb1db59, unchanged in the attached package. EXTEND_EXISTING_TOOL: polynomial-rate coherent Gram, exact reference residual, damping score and explicit benchmark damping. COMPOSE_APPLIED: critical reference theorem with direct-sum MHD nonlinearity. No current Foundation/tool admission is requested by this persistence.

Actual checks: exact residual polynomial; exact reference action; zero/nonzero source support; damping certificate algebra; 15 high-precision scalar damping regressions; rank-three A3 split cross-Gram zeros; MHD direct-sum norm inequality and exact source coefficient. No numerical PDE simulation was used. The high-precision regressions are not substitutes for (12)'s analytic proof. No numerical C0 was certified; values used in scalar regressions test algebra only.

The next unresolved unit is to select damped/higher references using rigorous weighted Grams and sharpen their reference-growth cost, with validated analytic constants. Residual decrease alone is inadequate, and neither increasing degree nor restarting provides an automatic all-data global proof. The original full NS problem remains unclosed.
