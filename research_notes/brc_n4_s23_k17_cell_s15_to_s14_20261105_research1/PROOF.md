# BRC N=4 / S23: full K=17 phase for 1/5 ≤ s < 1/4, two continuous switches and an integer-feasibility jump

Date: 2026-11-05 Asia/Shanghai. Scientific input frozen at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Author analytic proof with executed exact rational certificate, pending independent review and native admission. Direct successor of `85045dc8ac46874b440f03984117125fce3ee0fb`.

## Experiment and budget

Set a=11/21, b=10/21, d=√(ab). A complete typed ternary source T has P=(as,1−s,bs), Q=(bs,1−s,as), cost 2−s. Its specified Bernoulli projection B has P=(as,1−as), Q=(bs,1−bs), cost 1. These source/observer types remain distinct. For one **common** Chernoff exponent t∈[0,1], let

fT(t;s)=−log[1−s+s(a^t b^(1−t)+b^t a^(1−t))],
fB(t;s)=−log[s a^t b^(1−t)+(1−as)^t(1−bs)^(1−t)],
C(m,n;s)=max_t(m fT+n fB), CT=C(1,0), CB=C(0,1), H=fB(1/2;s).

Optimize C over nonnegative integers m,n with (2−s)m+n≤17. All information is positive, so n_m=⌊17−(2−s)m⌋ when feasible.

## Theorem (complete open cell)

There are exactly two continuous transitions α,β, uniquely specified by
C(5,8;α)=17 CB(α) and C(9,1;β)=17 CB(β), with

1/5 < α < 20015/100000 < 2/9 < β < 2224/10000 < 1/4.

The **complete** global maximizer classification for 1/5≤s<1/4 is:

* 1/5≤s<α: uniquely (5,8); s=α: exactly (5,8) and (0,17);
* α<s<2/9: uniquely (0,17);
* 2/9≤s<β: uniquely (9,1); s=β: exactly (9,1) and (0,17);
* β<s<1/4: uniquely (0,17).

At **s=1/4**, the unique maximizer is (8,3). Thus the boundary 2/9 activates (9,1), and 1/4 activates (4,10) and (8,3), of which (8,3) wins. Each continuous zero and discrete jump is global within the given exact experiment and integer budget.

## Proof: full feasible set and exclusion

For 1/5≤s<1/4, m ranges 0..9. For m=0..4, maximal n=17−2m; for m=5,6,7,8, maximal n is 8,6,4,2, respectively; for m=9, n=0 on [1/5,2/9) and n=1 on [2/9,1/4). At s=1/4, additionally n_4=10 and n_8=3 (all other maxima unchanged).

Write qT=1−s+2sd and qB=sd+√((1−as)(1−bs)). The exact identity qT−qB²=2sd(1−qB)>0 implies CT<2H≤2CB on 0<s<1. Hence every m=1..4 on the open cell is inferior to (0,17).

The exact rational certificate below proves D(1/5)=11CB−6CT>0 and D(y)−D(x)>0 for all 1/5≤x<y≤1/4. Thus CT/CB<11/6 throughout. It follows that (6,6),(7,4),(8,2) and (9,0) all lose to (0,17), since their total individual information envelopes mCT+nCB are strictly below 17CB. The only candidates on the first subcell are (5,8) and (0,17); on the second, add (9,1).

## Proof: convex-secant certificate and unique crossings

For fixed t, fT is convex in s. Also v_t(s)=(1−as)^t(1−bs)^(1−t) satisfies
v_t''=−t(1−t)v_t[a/(1−as)−b/(1−bs)]²≤0;
therefore fB(t;s)=−log[s a^t b^(1−t)+v_t(s)] is convex. Supremums preserve convexity, so CT, CB and each F_{m,n}=C(m,n) are continuous convex functions.

Let δ=1/10000, l<r, and define
L_l=[CB(l)−CB(l−δ)]/δ,
U_{m,n,r}=[m CT(r+δ)+n CB(r+δ)−m CT(r)−n H(r)]/δ.

For l≤x<y≤r, convexity and the bounds mCT+nH≤F_{m,n}≤mCT+nCB give

[F_{m,n}(y)−F_{m,n}(x)]/(y−x)≤U_{m,n,r},
[CB(y)−CB(x)]/(y−x)≥L_l.

Hence whenever 17L_l−U_{m,n,r}>0, G_{m,n}=F_{m,n}−17CB strictly decreases on [l,r]. All inequalities here are exact certified rational comparisons, not floating-point scans. The attached executable `VERIFY.py` establishes positive 17L−U margins for (m,n)=(5,8) on each of [1/5,41/200], [41/200,2/9], [2/9,1/4], and for (9,1) on [2/9,1/4]. It also establishes 11L−6[CT(1/4+δ)−CT(1/4)]/δ>0.

The actual common-t envelopes obey
mCT+nH ≤ C(m,n) ≤ mCT+nCB.
At s=1/5, 5CT+8H−17CB>0; at s=20015/100000, 9CB−5CT>0. Strict monotonicity and continuity yield one and only one α in the stated bracket. At s=2/9, 9CT+H−17CB>0; at s=2224/10000, 16CB−9CT>0. Strict monotonicity yields one and only one β in the stated bracket. Because α<2/9, (5,8) loses to pure B throughout the second subcell. This proves the complete open-cell classification and all uniqueness claims.

## Boundary s=1/4

The two newly feasible configurations are (4,10), (8,3). The rational certificate proves
8CT+3H−17CB>0 and
8CT+3H−(4CT+10CB)>0.
Hence (8,3) beats both pure B and (4,10) using a genuine common exponent. On this endpoint (5,8) is below pure B by the preceding monotone result; (6,6),(7,4) are below pure B by D>0; (9,1) is below pure B by the separate verified 16CB−9CT>0; m=1..3 remain inferior by CT<2CB. Thus (8,3) is the unique global maximum. QED.

## Exact validation and scope

`VERIFY.py` uses Python `Fraction`, `isqrt`, 10^-48 square-root enclosures and 34 terms of 2atanh log series with explicit geometric tail. The Bernoulli CT and CB bounds use Hlog=log(a/b), J=log((1−bs)/(1−as)), ρ=J/(Hlog+J), CB=D_Bern(ρ||as), as in the exact preceding-cell source. Each ASSERT is strict over enclosing rational intervals. `RUN_EVIDENCE.txt` contains the actual execution output. Scientific scope: fixed typed S23 statistical experiment, real parameter domain, integer budget 17. The ten-label S23 minimax mother problem retains the recorded [1/2,2/3] open interval. Project Result admission and independent review remain pending.
