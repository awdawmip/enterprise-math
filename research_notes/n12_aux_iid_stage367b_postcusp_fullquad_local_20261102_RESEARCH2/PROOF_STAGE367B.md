# Stage367-B — full four-parameter constrained local minimum throughout the post-audit-cusp interval

Date: 2026-11-02, Asia/Shanghai. Author: Research2 portable mathematical research, authenticated GitHub account awdawmip. Independent Driver review and native CLAIM are separate. Immutable scientific inputs: GLOBAL_KNOWLEDGE_V1 bf84bd7c61a2444b59b1da96be57df0e9ae47e53; Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 V5 original blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative controls read at GLOBAL main 4d8bdb9ad4e90fab69a8dc5d1d22c21b3ed4cd0f and EM main 90b640853e310b8fdf53dbf1c428dbc77ea8d6de. Reuse the exact published Stage363, 365 and 366 sources in Draft PR #1736. Scope: external Bernoulli/BRC auxiliary observer with the original 16 labelled source-word comparisons, not native X6 dynamics.

## Exact model

For k=0,1,2,3, let B_k(z)=z^k(1-z)^(3-k), w=(1,3,3,1), m=(61,21,9,9), and

r_k(x,y)=(4 B_k(x)+B_k(y))/5-m_k/160,
b(x,y)=(5/32) sum_k w_k |r_k(x,y)|,
D_3(a,z)=(1/2) sum_k w_k |B_k(a)-B_k(z)|,
c(x,y)=[63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)]/256.

The source-word-port comparisons are four separately labelled four-word blocks; no histogram merging is used. The unrestricted objective is T(P,Q)=33/1024+c(P)+c(Q), subject to b(P)+b(Q)<=2 beta_*+E, where P,Q are independent members of [0,1]^2. Let q*=(x*,y*) be the central simultaneous r0=r1=0 root, beta_*=b(q*). Put alpha=(1+sqrt(13))/8, q_alpha=(x_alpha,alpha) with r1(q_alpha)=0, E_c=b(q_alpha)-beta_*. For s>=0 on the right r1=0, r0<=0 branch define q_s by b(q_s)=beta_*+s.

## Theorem — strict local optimum for every post-cusp budget

For every real E with E_c<E<=11/5000 put s=E-E_c>0, A=q_s, C=q_alpha and rho=1/100000000. For every real P,Q in [0,1]^2 with ||P-A||_infty<=rho, ||Q-C||_infty<=rho and b(P)+b(Q)<=b(A)+b(C), write

u=|r1(P)|, v0=(r0(P))_+, w=||Q-C||_infty,
h=b(A)+b(C)-b(P)-b(Q)>=0.

Then

T(P,Q)-T(A,C) >= u/20 + v0/8 + w/4000 + h.                 (T)

Equality can occur only at P=A and Q=C. Hence (q_{E-E_c},q_alpha) and its exchange are strict constrained local minimizers in the entire four-independent-real-coordinate family for each E in the stated interval, uniformly in an explicit product radius 10^(-8). The endpoint E=E_c has the separate Stage366-B sharp local certificate. This statement is local, not a global optimality theorem.

## 1. Algebraic root isolation and uniform sign region

Exact rational brackets:

x* in (2310839,2310840)/10^7; y* in (5555086,5555091)/10^7;
x_alpha in (2378068,2378070)/10^7; alpha in (5756939,5756940)/10^7.

They give 0.002181<E_c<0.002182 and 0<s<=11/5000-E_c<1/50000. The curve r1=0 has y=Y(x) increasing since r1_x>0 and r1_y<0, while r0 decreases along it and crosses zero exactly at q*. Work in the rational box N=[23108/10^5,23115/10^5] x [55550/10^5,55572/10^5]. Here r2>0>r3 and f:=(15/16)r2 increases along the graph. At the right x_R=23115/10^5 the exact checker verifies r1(x_R,55571/10^5)>0>r1(x_R,55572/10^5) and f(x_R,55571/10^5)-f(2310840/10^7,5555091/10^7)>1/50000. Therefore every q_s lies in N, satisfies r1=0, r0<0 and b(q_s)=f(q_s).

All signed labels have a fixed sign at the star/near-star and cusp boxes, except residuals r0,r1 and a single cusp audit comparison. The four port sign blocks are (-,+,+,+),(-,-,+,+),(+,+,-,-),(-,-,+,+); at the cusp the (3/4,y), k=2 comparison changes sign. Since sum_k w_k r_k=0 and r2>0>r3, at both neighborhoods

b=f+(5/16)(r0)_+ +(15/16)(r1)_+.                           (1)

Expanding all 16 weighted labelled audit comparisons gives the smooth branch C_lo with

grad C_lo = (-3(1-x)(63-61x)/256, 3 y(1-y)/64).           (2)

Near q_s, c=C_lo. At the cusp,

c=C_lo+(21/256)(B_2(y)-9/64)_+.                            (3)

The executable checker expands every original label separately with SymPy and checks (1)–(3), all root endpoints, and the uniform sign enclosures including 10^(-8) perturbations. The external analytic model is used with its original source data intact.

## 2. Common budget multiplier and transverse/cusp supporting normals

On the near-star branch define

Y'(x)=-r1_x/r1_y,
lambda_s=-(c_x+c_y Y')/(f_x+f_y Y') evaluated at q_s.       (4)

Outward exact Fraction interval arithmetic over all N verifies

119/100 < lambda_s < 121/100.                              (5)

Put L_s=c+lambda_s b. At A=q_s define
V_s=lambda_s(15/16) grad r1(A),
W_s=grad C_lo(A)+lambda_s grad f(A),
theta_s=-(W_s)_x/(V_s)_x.

The choice (4) and nonzero r1_x imply W_s+theta_s V_s=0; the rational interval certificate gives 3/4<theta_s<9/10. The positive part is essential: for every signed scalar t,
(t)_+-theta_s t >= min(theta_s,1-theta_s)|t|.
The coefficient of (r1)_+ exceeds 1/10 and the coefficient of (r0)_+ exceeds 1/4. For every v=P-A with ||v||<=rho, a Taylor/positive-part estimate using |B_k''|<=6 gives

L_s(P)-L_s(A) >= |r1(P)|/10 +(r0(P))_+/4 -12||v||_infty^2.   (6)

The residual r0 may change sign for fixed radius when s approaches zero; its positive part is retained, not deleted.

At the cusp C=q_alpha put
U_c=(0,(21/256)B_2'(alpha)),
V_c=lambda_s(15/16)grad r1(C),
W_c=grad C_lo(C)+lambda_s grad f(C).

Uniform rational root-box interval bounds for every lambda_s satisfying (5) give the unique coefficients in W_c+theta_U U_c+theta_V V_c=0:

1/2<theta_U<9/10; 3/4<theta_V<9/10;
det(U_c,V_c)<-1/400; every entry of U_c,V_c has absolute value <1/4. (7)

Thus for nonzero z the one-sided derivative
L_s'(C;z)=(U_c dot z)_+-theta_U(U_c dot z)
            +(V_c dot z)_+-theta_V(V_c dot z)
is >||z||_infty/1000: both coefficients are strictly positive, and Cramer's rule gives |U_c dot z|+|V_c dot z|>||z||_infty/100. Cubic Taylor/hinge remainder is <10||z||_infty^2. For ||z||<=rho this proves

L_s(Q)-L_s(C) >= ||Q-C||_infty/2000.                       (8)

This is a uniform strict sharp support at the audit cusp for the whole multiplier interval, not an inference from a zero Clarke subgradient alone.

## 3. Controlling the remaining tangent coordinate using the shared budget

The near-star observation map F=(r1,f) has Jacobian determinant
det(grad r1,grad f)>1/60 on N, and all four gradient entries have absolute value <1/3. The linear inverse infinity operator norm is <40. Exact polynomial Taylor remainders in each component are <=3||v||^2; for ||v||<=rho and 40/(1-240rho)<41 this proves

||P-A||_infty <=41 (|r1(P)|+|f(P)-f(A)|).                  (9)

Using b(A)=f(A), (1), and the exact additive budget slack h,
|f(P)-f(A)|
 <= |b(P)-b(A)| +(5/16)(r0(P))_++(15/16)|r1(P)|
 <= |b(Q)-b(C)|+h +(5/16)v0+(15/16)u.

The original b is globally Lipschitz in infinity norm with constant 15/4<4 (each B_k' absolute bound <=3 and the original weighted coefficients are retained), so |b(Q)-b(C)|<4w unless w=0, where <= is enough. Consequently

||P-A||_infty <=164(u+v0+w+h).                             (10)

Combining (6), (8), (10), the exact identity

T(P,Q)-T(A,C)
  = [L_s(P)-L_s(A)]+[L_s(Q)-L_s(C)]+lambda_s h,

and 12 rho*164<1/50000 yields

T(P,Q)-T(A,C) >=
 (1/10-1/50000)u + (1/4-1/50000)v0
 +(1/2000-1/50000)w +(119/100-1/50000)h
 >= u/20+v0/8+w/4000+h.

When u=v0=w=h=0, (9) forces ||P-A||=0 and Q=C. Every other feasible pair has a strict cost increase. This proves (T) over the entire stated continuous-real domain with one uniform explicit product radius.

## Exact verification and scope

Accompanying REPRO_STAGE367B.py contains standalone SymPy identities for the separately labelled 16-source audit costs and Python Fraction outward interval arithmetic for algebraic brackets, sign charts, the lambda/normal coefficients, determinants, remainder and radius inequalities. Actual independent local executions of the original long-form checker twice gave identical output (see the separately saved execution log), ending STAGE367B_POST_CUSP_UNRESTRICTED_STRICT_LOCAL_OPTIMUM_EXACT_PASS. The submitted compact equivalent checker reuses the same exact assertions. The analytic steps above provide the real-domain theorem from those exact premises; no finite mesh is substituted for universal quantifiers. These are portable author-side results, currently UNREVIEWED/NOT_ADMITTED.

BRC usage: REUSE_EXECUTED original provenance-preserving 16 Bernoulli comparisons; COMPOSE_APPLIED coupled 2-source residual-budget map, moving Lagrange multiplier, two independent cusp normals, exact coordinate inverse. Unrestricted global optimality and any bridge to P000 native X6/three-dimensional slice/triadic closure/independent time/registered six-field Cell address are separate open obligations.

## Next discriminator (Stage368-B)

Fix rational E=11/5000. Seek an exact rational four-parameter competitor outside the certified product neighborhoods that beats the algebraic candidate's cost while obeying the exact algebraic reference budget, or rigorously exclude a specified continuous competition region by a finite exact interval certificate. A no-hit sampling search is not global proof. Keep labels, frozen pins and separate owner/review authority.
