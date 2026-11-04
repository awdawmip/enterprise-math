# BRC N=4 / S23: four exact phase switches on 2/5 <= s <= 1/2, K=17

Date: 2026-11-05 Asia/Shanghai. Author-side analytic theorem and executed exact rational certificate. Scientific input pin: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Continuation frontier: awdawmip/enterprise-math@bdb0577e7f640bbf31bf9ae1dc95dd19984ed40f. This is an auxiliary S23 discrimination experiment, with source/projection distinction retained. Status: UNREVIEWED / NOT_ADMITTED.

## Exact model

Set a=11/21, b=10/21 and 0<s<=1/2. The original ternary observation T has P=(as,1-s,bs), Q=(bs,1-s,as); its declared Bernoulli projection B has P=(as,1-as), Q=(bs,1-bs). For 0<=t<=1, put

    fT(t;s) = -log(1-s+s*(a^t*b^(1-t)+b^t*a^(1-t)))
    fB(t;s) = -log(s*a^t*b^(1-t)+(1-as)^t*(1-bs)^(1-t))
    F(m,n;s) = max_{0<=t<=1} [m*fT(t;s)+n*fB(t;s)]
    CT(s) = F(1,0;s), CB(s) = F(0,1;s), H(s) = fB(1/2;s).

Maximize F over integers m,n>=0 and (2-s)m+n<=17. The Chernoff exponent t is shared across the T and B observations. F strictly increases in each count, so for feasible m the relevant n is n_m=17-2m+floor(ms). CT(s)=-log(1-s+2s sqrt(ab)). CB has the exact Bernoulli-KL representation recorded in VERIFY.py.

## Theorem: complete phase classification

There are four unique real crossings alpha_0,alpha_1,alpha_2,alpha_3, with respective defining equations

    F(10,1;alpha_0)=17 CB(alpha_0),
    F(7,6;alpha_1)=17 CB(alpha_1),
    F(9,3;alpha_2)=17 CB(alpha_2),
    11 CT(alpha_3)=17 CB(alpha_3),

and strict rational isolating intervals

    2/5  < alpha_0 < 2/5  + 1/1000,
    3/7  < alpha_1 < 3/7  + 1/1000,
    4/9  < alpha_2 < 4/9  + 1/1000,
    5/11 < alpha_3 < 5/11 + 1/1000.

On each half-open feasibility cell [l,r) with l=(2/5,3/7,4/9,5/11), r=(3/7,4/9,5/11,1/2), the unique maximizer is respectively (10,1), (7,6), (9,3), (11,0) for l<=s<alpha_i; precisely this pair and (0,17) tie at alpha_i; (0,17) is uniquely optimal for alpha_i<s<r. At s=1/2, the unique maximizer is (10,2). Hence 3/7, 4/9, 5/11 and 1/2 are integer-feasibility activation transitions, each selecting the newly feasible design immediately.

## Proof 1: exact finite feasible hulls

For m<=11, floor(ms) can change on [2/5,1/2] only at 2/5,3/7,4/9,5/11,1/2. Twelve T observations are infeasible throughout because 12(2-s)>=18>17. For each open cell, computing n_m exactly gives the upper convex-hull vertices of all feasible integer count pairs:

    [2/5,3/7):  (0,17), (10,1)
    [3/7,4/9):  (0,17), (7,6), (10,1)
    [4/9,5/11): (0,17), (9,3), (10,1)
    [5/11,1/2): (0,17), (11,0)
    s=1/2:      (0,17), (10,2), (11,0).

Each hull is printed and asserted from exact Fraction arithmetic in VERIFY.py. Since F(m,n;s) is the maximum over t of a linear function of (m,n), it is convex in the counts. As it is strictly increasing in n, an optimizer is a vertex of one of these upper hulls, up to a possible collinear tie. This reduces the global search to the displayed vertices.

The candidate (10,1) is strictly inferior to (0,17) for every s in [3/7,5/11): indeed F(10,1;s)<=10 CT(s)+CB(s) and the verifier proves 16 CB(s)-10 CT(s)>0 throughout [3/7,5/11] by eight strict rational point/secant tests.

For possible collinear pairs, uniqueness follows from different maximizing Chernoff exponents: T has unique optimum t=1/2 and B has unique optimum t_B>1/2 for 0<s<1. At t=1/2 the derivative of the Bernoulli coefficient is (as-bs)*(psi(log(a/b))-psi(log((1-bs)/(1-as))))<0, where psi(u)=u/(2 sinh(u/2)) is strictly decreasing on u>0; a/b>(1-bs)/(1-as)>1. Thus fB'(1/2)>0 and the joint optimum of any design with positive T differs from pure-B optimum. If two endpoint designs have distinct maximizing exponents, any proper convex interpolation has strictly smaller F than the larger endpoint. This applies to the hull edges that could produce ties and gives the announced unique choices.

## Proof 2: strict monotonicity via finite convex secants

For fixed t, the Chernoff coefficient of T is affine in s; that of B is the sum of a linear term and the weighted geometric mean (1-as)^t(1-bs)^(1-t), concave in s. Hence fT(t;s) and fB(t;s) are convex in s, and so are F(m,n;s), CT and CB.

Let G_mn(s)=F(m,n;s)-17 CB(s). For a rational subinterval [x,y] and d=1/10000, convexity gives for all x<=u<v<=y

    (G_mn(v)-G_mn(u))/(v-u) <= U_mn(y)-17 L(x),
    L(x)=[CB(x)-CB(x-d)]/d,
    U_mn(y)=[m CT(y+d)+n CB(y+d)-m CT(y)-n H(y)]/d.

This uses m CT+n H<=F<=m CT+n CB at the specified endpoints. VERIFY.py splits each of the four feasibility cells into 12 equal rational subintervals and proves 17 L(x)-U_mn(y)>0 strictly on every one of the 48 subintervals. Thus all four G functions are strictly decreasing on their respective entire cells.

At the respective left endpoints the rigorous lower bound m CT+n H-17 CB is positive; at left+1/1000 the rigorous upper bound m CT+n CB-17 CB is negative. Eight strict sign checks, continuity and global monotonicity give the four distinct unique alpha_i and the complete classification of the open cells. The additional 16CB-10CT certificate eliminates the extra hull vertex (10,1) in the middle two cells.

Finally at s=1/2, the upper hull has three vertices. The strict certified inequalities

    10 CT(1/2)+2 H(1/2) > 17 CB(1/2),
    10 CT(1/2)+2 H(1/2) > 11 CT(1/2)

make (10,2) the unique maximizer at this boundary, completing the theorem.

## Arithmetic coverage and result status

VERIFY.py uses Python standard-library Fraction and isqrt, outward rational square-root brackets of width 10^-48, 34 terms of the artanh log expansion with exact geometric-tail bounds, and outward rational intervals for the Bernoulli Chernoff tilt and KL expression. All 66 asserted signs and the five finite hull checks executed successfully; full stdout is RUN_EVIDENCE.txt. The printed GT integer/10^13 statements are strict rational lower bounds. The scope is the exact K=17 ternary/projection statistical experiment with its given rational source and costs. Independent mathematical review and native Result admission are outstanding; the ten-label S23 minimax mother target retains its previously established open bounds [1/2,2/3].
