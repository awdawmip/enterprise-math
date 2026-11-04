# BRC N=4 / S23 — exact K=17 phase on [1/7,1/6] and its boundary jump

Date: 2026-11-04. Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Author-side proof and executed rational certificate; independent review and native admission pending. This extends the immutable preceding-cell proof 615962f9528839ea23d8515f016663392114f711. Researcher-ID EM-DIRECT-4BE1B9; activity RA-020CF4DC49690CC12628E8DE.

## Model

Let a=11/21, b=10/21, 0<s<1. A complete source T has P_T=(as,1-s,bs), Q_T=(bs,1-s,as), cost 2-s. B is the indicator of the first source label, with P_B=(as,1-as), Q_B=(bs,1-bs), cost 1. Retain the T provenance and B projection as distinct, typed observations. With ONE COMMON Chernoff exponent t in [0,1], define

    fT(t;s)=-log[1-s+s*(a^t*b^(1-t)+b^t*a^(1-t))],
    fB(t;s)=-log[s*a^t*b^(1-t)+(1-as)^t*(1-bs)^(1-t)],
    C(m,n;s)=max_{0<=t<=1}[m*fT(t;s)+n*fB(t;s)],
    CT=C(1,0;s), CB=C(0,1;s),
    F(s)=C(7,4;s), G(s)=F(s)-17*CB(s).

The integer budget constraint is (2-s)*m+n<=17.

## Theorem 1 — unique continuous switch

There is exactly one real s_star in [1/7,1/6) such that G(s_star)=0, with

    14287/100000 < s_star < 14291/100000.

For every real 1/7<=s<s_star the unique global optimal configuration is (7,4); for s_star<s<1/6 it is (0,17). Exactly those two configurations tie at s_star.

## Theorem 2 — new boundary jump

At s=1/6 the unique global optimizer becomes (6,6). Its cost is exactly 17. The sixth B sample is newly affordable at this boundary.

## Proof: integer budget reduction

For 1/7<=s<1/6, feasible m satisfies 0<=m<=9. The greatest B count at fixed m is n_m=17-2m+floor(ms). Thus n_m=17-2m for m<=6, n_7=4, n_8=2, n_9=0. B carries strictly positive Chernoff information, so the maximal n_m is the relevant choice at fixed m.

Let d=sqrt(ab), qT=1-s+2sd and qB=sd+sqrt((1-as)(1-bs)). T is symmetric, hence CT=-log(qT). Let fH=-log(qB)=fB(1/2;s). The exact identity

    qT-qB^2=2sd*(1-qB)>0

implies CT<2*fH<=2*CB for 0<s<1. Therefore for 1<=m<=6,

    C(m,17-2m;s)<=mCT+(17-2m)CB<17CB.

The uniform strict bound 8CT<15CB proved next yields C(8,2;s)<=8CT+2CB<17CB. Also 9CT<8CT+2fH<=8CT+2CB<17CB. The only possible winners are (7,4) and pure (0,17).

## Proof: uniform convex secant certificate

For fixed t, fT(t;s) is convex as negative log of a positive affine function. Set v_t(s)=(1-as)^t*(1-bs)^(1-t). Then

    v_t''(s)=-t(1-t)v_t(s)[a/(1-as)-b/(1-bs)]^2<=0.

Hence s*a^t*b^(1-t)+v_t(s) is positive concave; negative log is convex decreasing, so fB(t;s) is convex in s. Taking maxima over t preserves convexity of CT, CB and F(s)=max_t[7fT+4fB].

Let l=1/7, r=1/6, delta=1/1000 and define rational-information secants

    L=[CB(l)-CB(l-delta)]/delta,
    RT=[CT(r+delta)-CT(r)]/delta,
    UF={[7CT(r+delta)+4CB(r+delta)]-[7CT(r)+4fH(r)]}/delta.

Since 7CT+4fH<=F<=7CT+4CB, convex secant ordering gives for l<=x<y<=r:

    CB(y)-CB(x)>=L(y-x),
    CT(y)-CT(x)<=RT(y-x),
    F(y)-F(x)<=UF(y-x).

Executed exact rational interval arithmetic certifies

    15L-8RT>785596/10^9>0,
    17L-UF>512012/10^9>0,
    15CB(l)-8CT(l)>12435954/10^12>0.

Consequently 15CB(s)-8CT(s)>0 on [l,r], excluding (8,2) and (9,0) as used above. Furthermore, for all l<=x<y<=r,

    G(y)-G(x)<-(512012/10^9)*(y-x).

Thus G is strictly decreasing. Continuity follows because C is a maximum of a continuous function on compact t∈[0,1]. To locate its root, the strict interval verifier establishes

    7CT(14287/100000)+4fH(14287/100000)-17CB(14287/100000)>537526/10^15>0,
    13CB(14291/100000)-7CT(14291/100000)>5110796/10^15>0.

These are respectively a lower bound for G at the first rational endpoint and a negative upper bound at the second. The intermediate value theorem and strict monotonicity prove Theorem 1.

## Proof: boundary s=1/6

The newly feasible (6,6) satisfies C(6,6;r)>=6CT(r)+6fH(r). The exact certificates are

    6CT(r)+6fH(r)-17CB(r)>10529918/10^15>0,
    13CB(r)-7CT(r)>17139389691/10^15>0.

For m<=5 the strict CT<2CB bound excludes m samples with n=17-2m. The second certificate excludes (7,4), and the already proved uniform comparison excludes (8,2) and (9,0). Therefore (6,6) is the unique global optimizer at r. QED.

## Verification and status

VERIFY.py uses only Fraction, isqrt, the 10^-48 enclosing square-root grid, and 34 terms of the 2atanh log series with an explicit geometric tail. CB is evaluated by the Bernoulli Chernoff optimizer formula H=log(a/b), J=log((1-bs)/(1-as)), rho=J/(H+J), CB=D_Bern(rho||as). All sign tests use exact outward rational bounds. Re-run with python VERIFY.py and compare RUN_EVIDENCE.txt.

This is an analytically proved phase-cell statement with executed exact finite premise certificates, author-side UNREVIEWED / NOT_ADMITTED. The separate ten-label S23 minimax objective retains the currently documented [1/2,2/3] interval.
