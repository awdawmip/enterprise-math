# Stage365-B — exact equal-error projection across the first audit-label cusp

Date: 2026-11-02 (Asia/Shanghai). Research2 portable author proof. Current normative reads: GLOBAL_KNOWLEDGE_V1 main@d3ebf7b4e9c1566dd94238753f20f720e8ca877e and Enterprise Math main@50bf997b8d71444b78f8cddb2debb489ec85ed8b. Frozen scientific sources: global bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, original P000 V4. Model and evidence are author-side; no native admission is asserted.

## Original 16-label Bernoulli/BRC observer

For k=0,1,2,3 define B_k(z)=z^k(1-z)^(3-k), weights w=(1,3,3,1), reference m=(61,21,9,9), residuals r_k(x,y)=[4B_k(x)+B_k(y)]/5-m_k/160. Set b(x,y)=(5/32) sum_k w_k |r_k(x,y)|. Define D_3(a,z)=(1/2) sum_k w_k |B_k(a)-B_k(z)|, and c(x,y)=[63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)]/256. All sixteen source/word sign comparisons remain distinct.

Let R=[237/1000,239/1000] × [287/500,289/500], K=[2373/10000,2387/10000] × [1149/2000,231/400] and eta=1/100000. Let alpha be the unique root B_2(alpha)=9/64 in (5756/10000,5757/10000). This is the changing B_2 comparison at audit port (3/4,y), and the r_1=0 arc crosses y=alpha at a unique point inside K.

## Theorem A — quantitative cusp-crossing equal-error projection

For every real p=(x,y) in K satisfying |r_1(p)|<=eta, there exists q in R with **r_1(q)=0 and b(q)=b(p)**. If r_1(p)>0 then c(p)-c(q)>(2/25)r_1(p). If r_1(p)<0 then c(p)-c(q)>(14/25)(-r_1(p)); for r_1(p)=0 choose q=p. Thus a two-source additive-error global minimizer cannot include a source with p in K and 0<|r_1(p)|<=eta. Replacement keeps its exact error unchanged and strictly lowers cost. The theorem includes trajectories crossing the nonsmooth audit cusp.

## Theorem B — one-sided marginal-cost jump on the right kink

Along the increasing-x arc r_1=0, write s=b(x,y)-b(q_star), where q_star is the original r_0=r_1=0 junction, and phi(s)=c(x,y). At the unique audit-cusp budget s_alpha the cost is continuous but has **phi'_right(s_alpha)-phi'_left(s_alpha)>1/10**. This upward jump may affect later budget allocations; a global optimality/phase-transition claim requires the next two-source analysis.

## Exact proof

**Signs.** In R, r_0<0,r_2>0,r_3<0 by Bernstein monotonicity and exact corner tests. From the exact identity sum_k w_k r_k=0, the two total-variation branches are b_-=(15/16)r_2 when r_1<0 and b_+=(15/16)(r_2+r_1) when r_1>0. The four original audit sign tuples are (-,+,+,+),(-,-,+,+),(+,+,-,-),(-,-,sigma,+); sigma=+ below alpha and sigma=- above. All fifteen remaining individual audit signs are constant and strict on R. Because B_2 is strictly increasing on the y interval, there is exactly one audit cusp. r_{1x}=(4/5)u_1(x)>0 and r_{1y}=(1/5)u_1(y)<0, for u_1(z)=(1-z)(1-3z); exact endpoint inequalities at KXL,alpha_lo and KXU,alpha_hi give its unique crossing with r_1=0 inside K.

**Audit cusp is retained, not smoothed.** Put u_2(z)=z(2-3z). Expanding all sixteen labeled absolute-value terms gives
c_x=-3(1-x)(63-61x)/256, c_y(before)=3y(1-y)/64, c_y(after)=3y(18-25y)/256.
Their y-derivative difference is (21/256)u_2(y)>0. The two polynomial branches differ by exactly (21/256)[B_2(y)-9/64]; hence they coincide at alpha, giving a continuous piecewise smooth cost and a genuine upward gradient jump.

**Common Jacobian.** The two error gradients are grad b_-=(3u_2(x)/4,3u_2(y)/16) and grad b_+=(3(1-2x)/4,3(1-2y)/16). For f=r_1, their same wedge J=f_x b_y-f_y b_x=(3/20)[u_1(x)u_2(y)-u_1(y)u_2(x)] satisfies 1/60<J<1/40 on all R. Let D_±=c_x b_{±,y}-c_y b_{±,x}. With XL,XU,YL,YU the four endpoints of R, put g_min=3(1-XU)(63-61XU)/256, h_min=3YU(1-YU)/64 and h_max=3YL(18-25YL)/256. On either audit side, c_x<=-g_min and h_min<=c_y<=h_max. Exact rational corner bounds give
D_- <= -g_min (3/16)u_2(YU)-h_min (3/4)u_2(XL) < -7/500
and
D_+ >= g_min (3/16)(2YL-1)-h_max (3/4)(1-2XL) > 1/500.
Therefore **D_-/J<-14/25 and D_+/J>2/25**, uniformly across both audit-label sign choices.

**Fixed-error continuation.** Given t0=r_1(p), solve dx/dt=b_y/J, dy/dt=-b_x/J on the smooth r_1 sign branch, starting at p. Then dr_1/dt=1 and db/dt=0. Across R, |b_y|<1/30 and 0<b_x<2/5; with J>1/60 this yields |dx/dt|<2, |dy/dt|<24. The K-to-R horizontal margin is at least 3/10000 and vertical margin at least 1/2000. Since 2eta<3/10000 and 24eta<1/2000, standard ODE continuation cannot reach the R boundary before t=0. The endpoint q obeys r_1(q)=0, b(q)=b(p). Moreover dy/dt<0, so the path crosses y=alpha at most once. Cost is continuous and piecewise C1; integrate dc/dt=D_±/J on either side of that possible single crossing to obtain both strict bounds in Theorem A, for **every real p** in the stated tube.

**Arc derivative at the audit cusp.** On r_1=0, Y'(x)=4u_1(x)/[-u_1(Y(x))]>0, and B'(x)=3u_2(x)/4+[3u_2(Y(x))/16]Y'(x)>0 is the common along-arc b derivative. The cost derivative along that arc jumps by (21/256)u_2(alpha)Y'(x_alpha), hence phi'_right-phi'_left=(21/256)u_2(alpha)Y'(x_alpha)/B'(x_alpha). With Yp_min=4u_1(XU)/[-u_1(YU)], Yp_max=4u_1(XL)/[-u_1(YL)] and Bp_max=3u_2(XU)/4+[3u_2(YL)/16]Yp_max, exact bounds give (21/256)u_2(YU)Yp_min/Bp_max>1/10. This proves Theorem B.

## Exact execution and scientific scope

REPRO_STAGE365B.py checks the original 16-label sign matrix, both polynomial cost branches, weighted residual identity, common Jacobian, all rational interval bounds, cusp root bracket, ODE distance barrier and jump bound using Python Fraction and SymPy. Executed twice locally, with byte-identical stdout saved in REPRO_STAGE365B_EXECUTED_STDOUT.txt, ending STAGE365B_AUDIT_CUSP_EQUAL_ERROR_TRANSVERSE_PROJECTION_EXACT_PASS. Exact symbolic checks certify algebraic premises, while the real-domain implication uses the stated monotonicity and ODE argument. Rational examples p_before=(2377/10000,5755/10000) and p_after=(2379/10000,5758/10000) witness nonempty admissible tubes on both cusp sides.

BRC COMPOSE_APPLIED to the original provenance-preserving Bernoulli observer; existing exact symbolic interfaces REUSE_EXECUTED. Native P000 X6/three-dimensional slice, independent time, triadic closure and six-field Cell addressing remain separate typed obligations. GitHub account is awdawmip; native v0.6.11 reported research_authority_granted=false, and active-owner read returned CONTROL_QUOTA. No formal CLAIM, Source Result, Driver review or mathematical admission.

Next Stage366-B: certify algebraically the audit-cusp budget and the before/after marginal two-source allocation, comparing the actual Stage353-B restricted incumbent with Stage363-B's near-star cost stability, and test exact rational four-parameter competitors outside K. Full unrestricted global optimum remains open.
