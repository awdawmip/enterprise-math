# R5 — two-parameter time-hull rigidity and rotated four-observer separator

2026-10-31 (Asia/Shanghai). Status **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. This is a finite auxiliary two-law STOP/CONTINUE model; no claim about native X6 geometry, seven-dimensional Heartbeat physics, or a formally admitted theorem.

## Frozen provenance and authority

Verified reading pins: GLOBAL_KNOWLEDGE_V1 main@d5990db433ff77f964628ca8b8e440004660891e; Enterprise Math main@edc7a748fdadf9ffa499b3c50d308f02207ee3cc. Read canonical bootstrap/manual, ACTIVE worldview, locked P000, applicable mathematics/BRC/code/portable/registration rules. Immediate prior immutable input: ff982755ab11b3bec31fdd187aedc656a7180134 / research_notes/brc_r5_l_gate_error_kernel_minimax_20261031_t0836/RESEARCH.md. Source context is EXPOSED, not blind-independent. Native status research_authority_granted=false, executor_binding_configured=false, active-job quota 5/5, owner inventory returned CONTROL_QUOTA. No authenticated owner, CLAIM, Source Result, review or admission claimed.

## Exact chance tree

Initial origin Q masses (A0,A1,B,C0,C1)=(1/8,1/8,1/4,1/4,1/4), P masses (1/4,1/4,1/4,1/8,1/8). Continued A_i takes a source-labelled natural kernel on terminal LR classes Y,L,M,H with ratios r=(1,3/2,2,3):

\[
K_i(y_i,\ell_i)=(y_i,\ell_i,1-2y_i-\tfrac32\ell_i,y_i+\tfrac12\ell_i),\quad y_i,\ell_i>0,\ 2y_i+\tfrac32\ell_i<1.
\]

This is the COMPLETE strictly positive two-dimensional moment surface: sum K=1, sum r*K=2, and conditional P kernel is (r/2)K. At t=1 each A_i has a CONTINUE decision x_i, each C_i a CONTINUE decision z_i. Continued A reaching Y takes STOP-at-2/CONTINUE-to-3 decision u_i; B independently reaches Y and uses u_B. Continued A reaching L takes STOP-at-3/CONTINUE-to-4 decision v_i. M/H terminate t=3; C continued terminates t=3. All terminal actions genuinely alter stopping times. FULL has nine history probabilities (x0,x1,u0,u1,uB,z0,z1,v0,v1) in [0,1]. Seedless LR must share x0=x1=x, u0=u1=uB=u, z0=z1=z, v0=v1=v, with no external persistent seed.

Let x=(x0+x1)/2, z=(z0+z1)/2, Y=sum_i(y_i x_i u_i), E=sum_i(ell_i x_i v_i) and s=uB/4+Y/8. Exact chance summation under both measures gives

\[
T_P=\tfrac32+x+z/2-s+3E/16,\qquad
T_Q=\tfrac32+x/2+z-s+E/8. \tag{1}
\]

Error probabilities do not affect (1) as long as the chance tree and stop times remain fixed.

## Theorem A: complete all-real two-parameter classification

\[
\boxed{\operatorname{conv}\mathcal T_{\rm FULL}=\operatorname{conv}\mathcal T_{\rm LR}
\iff y_0=y_1\ \text{and}\ \ell_0=\ell_1.}
\]

For theta_y=(y0+y1)/2 define the signed direction

\[
H_y=(1-\theta_y/2)T_P+(-2+\theta_y/2)T_Q.
\]

Here alpha+beta=-1, z coefficient -3/2+theta_y/4<0, E coefficient (-1-theta_y/2)/16<0. Hence maximizers set z=v=0, uB=u_i=1 (LR u=1). Each independent FULL x_i then has coefficient (y_i-theta_y)/8; LR's common-x coefficient sums to zero. Its EXACT support gap over all real behavioral policies is

\[
\boxed{\Delta_y=\sup_F H_y-\sup_{LR}H_y=|y_1-y_0|/16.} \tag{2}
\]

For theta_ell=(ell0+ell1)/2 define

\[
H_\ell=-(4+2\theta_\ell)T_P+(8+3\theta_\ell)T_Q.
\]

Here alpha+beta=4+theta_ell>0, z coefficient 6+2theta_ell>0, E coefficient 1/4>0. Maximizers set z=1, uB=u_i=u=0, v_i=v=1. The FULL x_i coefficient is (ell_i-theta_ell)/4, while shared LR x coefficient sums to zero. Thus

\[
\boxed{\Delta_\ell=|\ell_1-\ell_0|/8.} \tag{3}
\]

Conversely, for equal source kernels (y,ell), any FULL aggregates satisfy 0<=x,z<=1, 0<=s<=1/4+yx/4, 0<=E<=2ell*x. A seedless LR strategy with the same x,z, u=s/(1/4+yx/4), v=E/(2ell*x) when x>0 (arbitrary v if x=0) exactly reproduces T_P,T_Q. The constraints are linear, and their image under (1) is a convex polytope. Therefore the ACTUAL real two-time images agree when kernels agree, proving sufficiency.

## BRC residual observation quantitative law

Keep positive labelled origins and both P/Q conditional rows until declared projection. Put dy=y1-y0, dell=ell1-ell0. Exact kernel TV is

\[
\mathrm{TV}(K_0,K_1)=\tfrac12(|dy|+|dell|+|2dy+3dell/2|+|dy+dell/2|).
\]

The singleton Y and L event differences and the triangle inequality prove

\[
\boxed{\max(16\Delta_y,8\Delta_\ell)\le\mathrm{TV}(K_0,K_1)
\le32\Delta_y+12\Delta_\ell.} \tag{4}
\]

Thus two purpose-chosen time-support directions detect ALL source-kernel residual within this specific moment surface: both gaps vanish iff TV=0. BRC reuse: REUSE_APPLIED to the earlier labelled positive flow carrier; no signed-amplitude cancellation, native BRC-Shor computation, or X6 embedding inferred.

## Theorem B: cancelling the inherited J support is not hull equality

Take a strictly positive symmetric line:

\[
\ell_0=\ell_1=1/4,\quad y_0=y_1=y,\quad 0<y<5/16;
\quad a_0=a_1=b_0=b_1=1/16,
\]

where a,b are L STOP and L CONTINUE error probabilities. Other stop errors stay at the earlier interior values 1/8 and 5/8. All four natural Q outcomes and all P outcomes are strictly positive for the entire y interval. The four-observer map O=(eP,eQ,TP,TQ) has

\[
e_P=1/8+u_B/8+(1-z)/8+3F/16,\quad
e_Q=1/8+u_B/8+(1-z)/4+F/8,
\quad F=-x/32;
\]
together with (1), Y=y(x0*u0+x1*u1), E=(x0*v0+x1*v1)/4.

For the previous signed direction J=14eP-19eQ+2TP-4TQ,

\[
8J=-53-u_B+2y(x_0u_0+x_1u_1)-(x_0+x_1)/32-E.
\]

For EVERY real 0<y<=1/64, FULL and LR maxima are BOTH -53/8, so the inherited J separation is exactly zero. Yet for H=514eP-643eQ+65TP-129TQ, exact elimination gives

\[
\boxed{H=-1669/8-u_B/8+8y(x_0u_0+x_1u_1)-63E/16}. \tag{5}
\]

FULL maximizes at x0=x1=u0=u1=1, uB=v0=v1=0, giving -1669/8+16y. For LR, the same expression becomes -1669/8+u(16yx-1/8)-63xv/32, whose maximum is -1669/8+(16y-1/8)_+. Therefore

\[
\boxed{\Delta_H=\min(16y,1/8)>0\qquad(0<y<5/16).} \tag{6}
\]

Hence this whole one-dimensional natural-change family has identical ACTUAL two-time images but strictly unequal 4D convex hulls, including the subinterval where J is silent.

The five LR vertex policies with base (x,u,z,v)=(0,0,0,0) and four difference points (1,0,0,0), (0,1,0,0), (0,0,1,0), (1,0,0,1) have 4D determinant -31/131072, independent of y. Thus the four-dimensional LR hull is full affine rank throughout this line. At y=1/128, the legal FULL witness (x0,x1,u0,u1,uB,z0,z1,v0,v1)=(1,1,1,1,0,0,0,0,0) is O*=(125/512,95/256,1279/512,1023/512). Its H support is -417/2 versus LR -1669/8, exact gap 1/8. Since ||H||_1=1351, every real LR observation is at infinity-norm distance at least 1/10808 from O*.

## Verification and disposition

The sibling actual executed Python standard-library Fraction verifier exhaustively checked five rational symmetric y values (each 512 FULL and 16 LR deterministic policies), including **independent positive-path enumeration of all 512 FULL policies per instance**, rational 2D hulls, J/H extrema, LR rank and witness. Four extra asymmetric (y0,y1,ell0,ell1) instances exhaustively checked both support formulas, time hulls and BRC bounds. Totals: 4608 FULL and 144 LR deterministic observation computations. EXACT_OUTPUT.txt ends PASS_EXACT_R5_TWO_PARAMETER_TIME_HULL_CLASSIFICATION_AND_ROTATED_SEPARATOR. Analytic signs and formulas (1)-(6), not finite sampling, establish the all-real claims. No Lean proof, independent review or official task/result admission was performed.

These results exclude the stated moment surface with both activated gates for unequal kernels as a 2D time-hull candidate, and exclude the stated equal-kernel/error line as a 4D hull candidate. They DO NOT exclude a genuinely new downstream chance merger, an upstream Y/B coupling change, new LR classes, other baseline rewards or persistent-seed policies. Original full-rank four-observer hull-equality / seedless-image-inequality mother question remains OPEN.

NEXT: introduce a new interacting merger that changes which Y/L histories share future LR states (or their upstream coupling); first require exact two-time hull equality; then exact <=5 LR rational-vertex convex certificates for EVERY FULL four-vector or an explicit Farkas separator, plus affine rank 4; only after hull equality investigate actual real LR-image nonmembership. Do not treat Delta_J=0 as a full convex-hull equality certificate.
