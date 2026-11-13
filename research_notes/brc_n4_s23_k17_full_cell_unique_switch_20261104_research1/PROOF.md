# BRC N=4 / S23: unique K=17 switch on [1/8,1/7), and the s=1/7 jump

Date: 2026-11-04. Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Author-side proof / exact rational certificate, UNREVIEWED / NOT_ADMITTED. Extends the two-candidate reduction and switch existence from `e0a9646557ad2fe4a42cdd229d29da46ad7f1ea0` on PR #1765.

## Source-labelled model

Let a=11/21, b=10/21. T has P=(as,1-s,bs), Q=(bs,1-s,as), cost 2-s; B is the first-T-label indicator, P_B=(as,1-as), Q_B=(bs,1-bs), cost 1. The true product Chernoff information with ONE COMMON exponent is

    C(m,n;s)=max_{t in [0,1]} [m fT(t;s)+n fB(t;s)],  (2-s)m+n<=17,

    fT(t;s)=-log[1-s+s(a^t b^(1-t)+b^t a^(1-t))],
    fB(t;s)=-log[s a^t b^(1-t)+(1-as)^t (1-bs)^(1-t)].

Define CT=C(1,0;s), CB=C(0,1;s), F(s)=C(8,2;s), G(s)=F(s)-17CB(s). Let d=sqrt(ab), qT=1-s+2sd, qB=sd+sqrt((1-as)(1-bs)), fH=-log(qB). T is symmetric, so CT=-log(qT). Identity qT-qB^2=2sd(1-qB)>0 shows CT<2 fH<=2CB for 0<s<1.

## Theorem A: one and only one continuous switch on the full cell

For every real 1/8<=x<y<=1/7,

    G(y)-G(x)<-(y-x)/2000.

Consequently exactly one s_star exists in (12501/100000,12503/100000) with G(s_star)=0. For all real 1/8<=s<1/7, the unique global K=17 optimum is (8,2) when s<s_star and (0,17) when s>s_star; at s_star these two, and only these two, are tied.

Proof. For fixed t, u_t=a^t b^(1-t) and v_t(s)=(1-as)^t(1-bs)^(1-t). Direct differentiation gives

    v_t''(s)=-t(1-t)v_t(s)[a/(1-as)-b/(1-bs)]^2<=0.

Thus s u_t+v_t(s) is concave and positive. As -log is convex decreasing, fB(t;s) is convex in s. Likewise fT(t;s)=-log of a positive affine function in s, hence convex. A supremum of convex functions is convex, so CB(s)=max_t fB(t;s) and F(s)=max_t[8fT+2fB] are both convex for 0<s<1.

Put delta=1/1000, a0=1/8-delta, a1=1/8, b0=1/7, b1=1/7+delta, and

    L=[CB(a1)-CB(a0)]/delta,
    U=[8CT(b1)+2CB(b1)-8CT(b0)-2fH(b0)]/delta.

For every s, 8CT+2fH<=F<=8CT+2CB. Thus the right secant [F(b1)-F(b0)]/delta<=U. Convexity of F puts every secant slope within [a1,b0] below this right secant; convexity of CB puts every secant slope in [a1,b0] above L. Hence for x<y in [a1,b0],

    G(y)-G(x) <= (U-17L)(y-x).

The attached exact rational interval program proves 17L-U>1/2000 (the strict lower bound exceeds 563200/10^9), giving the asserted global monotonicity. No derivative or uniqueness of an optimizer t is assumed.

For s=12501/100000, the program proves 8CT+2fH-17CB>883434/10^15>0, hence G>0; for s=12503/100000 it proves 15CB-8CT>2893186/10^15>0, hence G<0 because F<=8CT+2CB. By continuity of the maxima over compact t in [0,1], existence follows, and strict monotonicity gives uniqueness.

For 1/8<=s<1/7, feasible m satisfies m<=9. Maximal n is 17-2m for m<=7, 2 for m=8, and 0 for m=9. Every 1<=m<=7 obeys C(m,17-2m;s)<=mCT+(17-2m)CB<17CB, by CT<2CB. For m=9, 9CT<8CT+2fH<=F, by CT<2fH. Positive information forces maximal n at fixed m. Thus the two named configurations exhaust global candidates, completing the classification. QED.

## Theorem B: discrete boundary jump at s=1/7

At s=1/7, the unique global K=17 optimizer is (7,4), with exact cost 17. It is newly feasible precisely at this boundary, whereas the unique optimizer for s in (s_star,1/7) is (0,17).

Proof. For 1<=m<=6, max n=17-2m and CT<2CB excludes them. The m=9 candidate is below (8,2) as above. By Theorem A, F(1/7)<17CB(1/7), so m=8 loses to pure B. The verifier proves

    7CT(1/7)+4fH(1/7)-17CB(1/7) > 8383034/10^15 > 0.

Since C(7,4;1/7)>=7CT+4fH, the newly feasible (7,4) strictly defeats pure B and all other candidates. QED.

## Exact verification contract and scope

`VERIFY.py` is Python stdlib `Fraction`+`isqrt` only. Square roots use enclosing adjacent 10^-48-grid rationals. Logs use 34 terms of the 2atanh-series with explicit geometric remainder; every argument has |(x-1)/(x+1)|<1/3. The Bernoulli optimum is evaluated without numerical optimization through H=log(a/b), J=log((1-bs)/(1-as)), r=J/(H+J) and CB=r log(r/(as))+(1-r)log((1-r)/(1-as)). All decisive inequalities are asserted exactly and stdout is preserved as RUN_EVIDENCE.txt.

The analysis proves real-parameter statements within the declared model; exact computation certifies finite rational premises. T retains ternary source provenance and B remains a declared projection. P000, ACTIVE worldview, original ten-label minimax bound [1/2,2/3], native CLAIM/Result, and independent review remain in their existing states.
