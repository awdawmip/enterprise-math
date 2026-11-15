# BRC N=4 / S23 — exact K=17 phase on [1/6,1/5) and boundary jump

Date: 2026-11-05 (Asia/Shanghai). Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Author-side analytic proof with executed exact rational sign certificate. Independent review and native Result admission pending. Continues the immutable prior-cell result `fd0e00e297eec94dd5182c9bfc0c8d33738efa6e`. Native research-session registration request `research1-20261105-0004-session` was queued, not yet established as a completed activity/CLAIM when this report was prepared.

## Typed experiment and objective

Let a=11/21, b=10/21, d=sqrt(ab), 0<s<1. The complete ternary source observation T has P_T=(as,1-s,bs), Q_T=(bs,1-s,as), cost c_T=2-s. The Bernoulli observation B is the first-label indicator: P_B=(as,1-as), Q_B=(bs,1-bs), cost c_B=1. B is a declared projection; the complete T label/provenance is retained as its own type. No reduction of T to B is invoked.

With one *common* Chernoff exponent t in [0,1], set

    fT(t;s)=-log[1-s+s*(a^t*b^(1-t)+b^t*a^(1-t))],
    fB(t;s)=-log[s*a^t*b^(1-t)+(1-as)^t*(1-bs)^(1-t)],
    C(m,n;s)=max_{0<=t<=1}{m*fT(t;s)+n*fB(t;s)},
    CT(s)=C(1,0;s), CB(s)=C(0,1;s),
    F(s)=C(6,6;s), G(s)=F(s)-17*CB(s).

Optimize C(m,n;s) over nonnegative *integer* (m,n) subject to (2-s)m+n<=17. Because B has strictly positive information, for a fixed m it is optimal to take n=floor(17-(2-s)m).

## Theorem A — complete open cost cell

For every real s in [1/6,1/5), the only possible global optimizers are (m,n)=(6,6) and (0,17). There exists exactly one s_star in this cell, with the strictly certified rational bracket

    16668/100000 < s_star < 16674/100000.

For s<s_star, the unique global optimum is (6,6). For s>s_star, it is (0,17). At s=s_star, exactly the two indicated configurations tie for the global optimum.

## Theorem B — next integer-cost boundary

At s=1/5, the newly feasible configuration (5,8) is the unique global optimizer. The parameter s=1/5 is therefore a genuine integer-feasibility jump, not a continuation of the preceding continuous crossover.

## Proof: complete integer feasibility and exclusion

For 1/6<=s<1/5, feasible m ranges from 0 to 9. The maximal n at each m is

    m=0..5: n=17-2m;
    m=6: n=6;
    m=7: n=4;
    m=8: n=2;
    m=9: n=0.

At s=1/5, m=5 additionally permits n=8, while the other maxima remain unchanged. The positive B information reduces each fixed-m comparison to this maximal n.

Write qT=1-s+2sd and qB=sd+sqrt((1-as)(1-bs)), so CT=-log(qT) and fH=fB(1/2;s)=-log(qB). The exact identity

    qT-qB^2 = 2sd(1-qB) > 0

holds for all 0<s<1. Hence CT<2fH<=2CB. For 1<=m<=5 in the open cell, C(m,17-2m) <= mCT+(17-2m)CB<17CB.

To eliminate all m>=7, we prove the stronger uniform bound

    D(s):=13CB(s)-7CT(s)>0  for 1/6<=s<=1/5.       (1)

For m in {7,8,9}, n=17-2m+1. By (1), CT/CB<13/7<=(2m-1)/m; thus

    C(m,n;s)<=mCT+nCB<17CB.

Consequently the only potential winners in [1/6,1/5) are (6,6) and (0,17). The same exclusions cover all competitors to (5,8) at s=1/5, except (6,6) and (0,17), which are compared below.

## Proof: uniform convex secant inequalities

For every t, fT(t;s) is convex in s because its positive Chernoff coefficient is affine in s. Put v_t(s)=(1-as)^t(1-bs)^(1-t). A direct calculation gives

    v_t''(s)=-t(1-t)v_t(s)[a/(1-as)-b/(1-bs)]^2 <= 0.

Therefore s*a^t*b^(1-t)+v_t(s) is positive and concave, so fB(t;s) is convex in s. Supremums preserve convexity; in particular CT, CB, F are convex functions of s.

Let l=1/6, r=1/5, delta=1/1000 and define finite differences

    L  =[CB(l)-CB(l-delta)]/delta,
    RT =[CT(r+delta)-CT(r)]/delta,
    UF ={[6CT(r+delta)+6CB(r+delta)]-[6CT(r)+6fH(r)]}/delta.

The bounds F<=6CT+6CB and F>=6CT+6fH follow respectively from max-of-sum <= sum-of-max and evaluation at common t=1/2. Thus convex secant ordering yields, for every l<=x<y<=r,

    CB(y)-CB(x)>=L(y-x),
    CT(y)-CT(x)<=RT(y-x),
    F(y)-F(x)<=UF(y-x).

The executed exact rational certificate in VERIFY.py proves

    13L-7RT > 828314/10^9 > 0,
    17L-UF  > 419936/10^9 > 0,
    13CB(l)-7CT(l) > 17139389/10^12 > 0.

The first and third inequalities establish (1) throughout [l,r]. The second proves

    G(y)-G(x)< -(419936/10^9)(y-x) <0

for all l<=x<y<=r. Hence G is strictly decreasing and continuous (maximization of a jointly continuous function over compact t in [0,1]).

The two exact sign comparisons, each using the true common-exponent information envelopes, are

    G(16668/100000) >= 6CT+6fH-17CB > 2288183/10^15 >0,
    G(16674/100000) <= 6CT-11CB < -2541977/10^15 <0.

Therefore G has exactly one zero s_star in the indicated bracket, with the strict global optimizer classification of Theorem A. No t-specific assumption other than the shared Chernoff exponent was made.

## Proof: the s=1/5 boundary

The configuration (5,8) has cost 5*(2-1/5)+8=17. The exact certificate gives

    C(5,8;1/5)-17CB(1/5)
    >= 5CT(1/5)+8fH(1/5)-17CB(1/5)
    > 13951505/10^15 >0.

Furthermore G(r)<0 by strict monotonicity and the upper rational sign certificate

    11CB(r)-6CT(r)>25133931/10^12>0,

which implies F(r)<=6CT(r)+6CB(r)<17CB(r). All other available m were excluded above, so (5,8) is uniquely optimal. QED.

## Exact certificate, scope, and next unit

VERIFY.py uses only Python Fraction, isqrt, a 10^-48 enclosing square-root grid and 34 terms of the 2atanh logarithmic series with an explicit geometric remainder. The exact CB formula is H=log(a/b), J=log((1-bs)/(1-as)), rho=J/(H+J), CB=D_Bern(rho||as). The entire set of sign tests uses interval endpoints and exact rational arithmetic; numerical displays are floored *lower* bounds.

Execute `python VERIFY.py` and compare `RUN_EVIDENCE.txt`. This verifies every strict rational premise of the analytic secant proof, not an independent mathematical review. Status: author analytic proof / exact rational executed / unreviewed / not admitted.

The ten-label S23 minimax mother problem retains the recorded open [1/2,2/3] gap. The next independently executable cell is 1/5<=s<1/4 (K=17), starting from the newly proven (5,8) winner and investigating continuous switches and the next integer-cost feasibility boundary.
