# R284HR — Balanced-port concentration, signed moderate-deficit curvature and complete first-step sign classification

2026-11-25. Author proof and exact checks, NOT_REVIEWED. Auxiliary binary-tag safe-word total-count observer only, as in R284HQ; no native physical attribution, P000 change, or global K monotonicity claim. Frozen scientific inputs: b0572296445fe5355dd4807ac4d6073fe69e8144:research_notes/portable_direct/R284HQ_EXACT_CURVATURE_BRANCH_BALANCE_20261125.md (exact branch balance and small-deficit sign); ee8f08bb614ff06cb63f6e2567d14ead674e42ff:research_notes/portable_direct/R284HM_SUBCRITICAL_POLYA_PORT_TRANSPORT_20261125.md (K and convolution definitions). Current canonical entry files read on main; global entry blobs also matched immutable 81e7c222b9c2e66e9e6176705a6af39cde49673d; EM continuation entry blob matched 40b9b6c658683c1eb9083ec7cf9a516de5fbc7e3. Source P000 V5 and companions, ACTIVE worldview, residual and portable protocols read separately from frozen science. Own original session registration r1-20261124-0256-r284gd-session-v1 recovery returned open RESEARCHER session MCP-8cd6c4fa26b9459d923ff73ba0082220; RA-B82240E8488EF5A1DA5186C4, EM-DIRECT-0C386E. Current LEASED inventory r1-20261125-1604-owner-inventory-read SUCCEEDED, empty page and no next cursor as of 2026-11-25T08:05:34.737995Z; no shared CLAIM. No other owner's state changed.

## Definitions and new claims

Reuse HQ: M_z(k)=(k+1)/(z+1) binom(2z+2,z-k) for 0<=k<=z and zero otherwise. C_g=sum_k M_n(k)M_m(g-k), c_g=binom(g+3,3), A_g=C_g/(M_n(0)M_m(0)c_g), r_g=A_(g+1)/A_g with r_(n+m)=0. The true conditional joint law is mu_g(k)=M_n(k)M_m(g-k)/C_g. Let t=min(n,m), T=max(n,m).

1. **Mode-centered concentration (balanced capacities).** For integers t>0, T<=2t, 3<=g<=t/2, define k0=ng/(n+m). Every mode k* of mu_g satisfies |k*-k0|<=3t/g+8. For Z=|k-k*| and every integer j>=1,
   Pr(Z>=j)<=2 exp[-j(j-1)/(2t)].
   In particular E Z²<=12t, E Z^4<=80t².
2. **New explicit moderate-deficit signed curvature band.** If T<=2t and 256 sqrt(t)<=g<=t/2 (integer conditions equivalently g²>=65536t, 2g<=t), then
   r_g-r_(g+1)>1/(64t).
   This is an unbounded sign theorem, reaching linear deficit t/2, using concentration around a capacity-proportional center instead of global support-range payment. The constants are conservative, not onset claims. Nonempty band requires t>=262144.
3. **Complete g=0 sign classification.** For all nonnegative n,m with n+m>0, r_0-r_1<0 iff t=0,T>=10 or t=1,T>=81. All other pairs have r_0-r_1>0, with no tie. HQ proved the two low-capacity thresholds; this turn closes all t>=2 without a capacity-ratio assumption.

## Proof of 1: concentration without deleting the joint allocation

For integer 0<=k<g write l=g-k. The exact adjacent ratio of the conditional masses is
   R(k)=mu_g(k+1)/mu_g(k)
       = (k+2)/(k+1) * l/(l+1) * (n-k)/(n+k+3) * (m+l+2)/(m-l+1).
Here g<=t/2 ensures full support and positive factors. Extend this rational formula to real k in [0,g-1] solely to compare consecutive integer ratios. Each of the first two log factors has nonpositive derivative. The last two factors have log derivatives containing respectively -1/(n-k) and -1/(m-l+1); all their remaining derivative terms are negative. As k>=0 and l>=1, these terms alone are <=-1/n-1/m<=-1/t. Hence (log R)'<=-1/t.

Put a=g/(n+m)<=1/4 and l0=ma, k0=na. Both k0,l0>=g/3, so k0 lies in [0,g-1] (g>=3). The log of the product of the first two factors at k0 has absolute value <=3/g: their logs have opposite signs and each magnitude is at most 3/g. In the last two factors the common (1-a)/(1+a) and its reciprocal cancel exactly. Remaining log terms are
   -log(1+3/[n(1+a)]) + log(1+2/[m(1+a)]) - log(1+1/[m(1-a)]).
Their sum has absolute value <=7/t by log(1+x)<=x and a<=1/4. Therefore |log R(k0)|<=3/g+7/t. At a mode, R(k*)<=1 when k*<g, and R(k*-1)>=1 when k*>0. The derivative bound, using whichever of these comparisons is on the relevant side of k0, gives |k*-k0|<= t |log R(k0)|+1<=3t/g+8. It also proves unimodality, including an adjacent equal-mode pair.

For the right tail, whenever the indices exist,
   mu_g(k*+i+j)<=mu_g(k*+i) exp[-j(j-1)/(2t)], i>=0,j>=1,
because each successive forward ratio from k*+i is at most exp[-(i+h)/t] at h=0,...,j-1. For the left tail use reciprocal ratios beginning at k*-1 and the same derivative bound. Summing the inequalities over i gives the stated two-sided tail estimate. For real x>=2 use j=ceil(x) and j(j-1)>=j²/2>=x²/2, so Pr(Z>=x)<=2 exp(-x²/(4t)). Tail integration gives E Z²<=4+8t<=12t and E Z^4<=16+64t²<=80t². This is an exact analytic bound on the discrete law, not a Gaussian replacement of the law.

## Proof of 2: center-stationary port observation and branch balance

HQ's exact identity is
   r_g(r_g-r_(g+1)) = D-Var_mu_g(X)-J,
   p=(k+2)/(g+4), l=g-k, x=rho_n(k), y=rho_m(l),
   rho_z(s)=(z-s)/(z+s+3), X=p x+(1-p)y,
   J=E[p(1-p)(x-y)^2/(g+5)],
   D=E[p(k+3)/(g+5) x (x-rho_n(k+1))
        +(1-p)(l+3)/(g+5) y(y-rho_m(l+1))].
The three terms are retained, with the exact joint law.

In this band t>=262144, g>=131072. By part 1, |k*-k0|<=3t/g+8 <= (3/256+8/512)sqrt(t)<sqrt(t)/32. Put Y=|k-k0|. Minkowski for second and fourth moments yields
   (E Y²)^(1/2) <= (sqrt(12)+1/32)sqrt(t)<sqrt(13t),
   (E Y^4)^(1/4) <= (80^(1/4)+1/32)sqrt(t)<100^(1/4)sqrt(t).
The rational constants can also be bounded by squaring: sqrt(12)<7/2, 80^(1/4)<3, so both strict inequalities follow (for the second moment 7/2+1/32<sqrt(13); for fourth 3+1/32<sqrt(10)).

Define f_z(s)=(s+2)rho_z(s)=-(s+2)+(2z+3)(s+2)/(z+s+3). Then
   f'_z(s)=-1+(2z+3)(z+1)/(z+s+3)^2,
   |f''_z(s)|=2(2z+3)(z+1)/(z+s+3)^3<=4/t.
The joint observation is X(k)=[f_n(k)+f_m(g-k)]/(g+4).
At s=za, f'_z(za) differs from -1+2/(1+a)^2 by at most 20/z: expand the numerator divided by z² as 2+5/z+3/z² (difference <=8/z), and bound the difference between (1+a+3/z)^(-2) and (1+a)^(-2) by 6/z using its derivative on [1,infinity). Thus |(g+4)X'(k0)|<=40/t. The bound on second derivatives gives
   |X(k)-X(k0)| <= [40Y+4Y²]/[t(g+4)].
Because a variance is at most the expected squared difference from any constant, Minkowski and the moment bounds give
   sqrt(Var X) <= [40 sqrt(13)/sqrt(t)+40]/(g+4) <41/(g+4).
This is the essential quadratic rather than linear sensitivity around k0: the capacity-proportional center cancels the leading first derivative even if n differs from m. Hence Var X<1681/g²<=1681/(65536t).

Similarly |rho'_z(s)|<=2/t, and at s=za the two rho values differ by at most 6/t (each differs from (1-a)/(1+a) by <=3/t). Thus |x-y|<=4Y/t+6/t, giving sqrt(E(x-y)^2)<15/sqrt(t), and J<225/[4t(g+5)].

For D, reuse the pointwise bound from HQ: x,y>=L=(t-g)/(t+g+3)>=3/10. The loss for an additional unit at either port is >=delta=(2t+3)/[(T+g+3)(T+g+4)]>=9/(32t), using T+g+4<=(8/3)t. The sum of same-color two-step probabilities is >=1/2. Consequently D>=L delta/2>=27/(640t).
Subtracting,
   t r_g(r_g-r_(g+1))
     > 27/640-1681/65536-225/(4*131072)
     = 42227/2621440 > 1/64.
The inequality is exact rational; 0<r_g<=1 by the HQ weighted branch identity. This proves the sign and claimed strict lower bound. Unlike HQ's uniform support-range estimate, the variance bound is O(g^-2); the reinforcement term is O((tg)^-1), and neither obscures the O(t^-1) same-port capacity loss when g/sqrt(t) is sufficiently large. The full positive joint allocation is retained.

## Proof of 3: first-step exact sign

Use HQ's definitions a=n/(n+3), b=m/(m+3), c=a(n-1)/(n+4), e=b(m-1)/(m+4). Then r_0=(a+b)/2, r_1=(3c+4ab+3e)/(5(a+b)), and the exact signed identity is
   10(a+b)(r_0-r_1)=6(a²-c+b²-e)-(a-b)².
Each of a²-c, b²-e is nonnegative; e.g. a²-c=n(2n+3)/[(n+3)^2(n+4)]. Without loss n=t, m=T. Then |a-b|<=3/(t+3), while 6(a²-c)=6t(2t+3)/[(t+3)^2(t+4)]>9/(t+3)^2 for t>=2, since 12t²+9t-36>0 there. Thus strict positive curvature for all t>=2, unrestricted T. For t=0,T>=1, HQ's sign expression reduces to the sign of -(T²-8T-18), changing between 9 and 10 and never zero on integers. For t=1,T>=1, HQ's sign is that of -(T³-78T²-183T-60), negative cubic for T<=80 and positive for T>=81 (check 79,80, then expand at 81). This completes the exact classification without a tie.

## Executed evidence

Python 3 exact integers and Fraction, finite checks only. No float is used for sign comparisons. This first experiment deliberately tests supporting bounds in feasible smaller ranges, not the large analytic band itself; the unbounded theorem follows from the proof. Code:
```python
from math import comb,isqrt
from fractions import Fraction as F
from functools import lru_cache
@lru_cache(None)
def M(n,g):
    a=[comb(2*n+2,n)//(n+1)]
    for k in range(g):
        v,r=divmod(a[-1]*(k+2)*(n-k),(k+1)*(n+k+3)) if k<n else (0,0)
        assert r==0
        a.append(v)
    return a
def check(n,m,g):
    t=min(n,m); assert t>0 and max(n,m)<=2*t and 3<=g<=t//2
    a,b=M(n,g+2),M(m,g+2)
    c=[sum(a[k]*b[j-k] for k in range(j+1)) for j in (g,g+1,g+2)]
    r=F(c[1]*(g+1),c[0]*(g+4)); rn=F(c[2]*(g+2),c[1]*(g+5))
    w=[a[k]*b[g-k] for k in range(g+1)]; assert sum(w)==c[0]
    mode=max(range(g+1),key=w.__getitem__)
    center=F(n*g,n+m)
    assert abs(mode-center)<=F(3*t,g)+8
    for k in range(g-1):
        assert w[k+2]*w[k]*(t+1)<=w[k+1]**2*t
    z2=F(sum(v*(k-mode)**2 for k,v in enumerate(w)),c[0])
    z4=F(sum(v*(k-mode)**4 for k,v in enumerate(w)),c[0])
    assert z2<=12*t and z4<=80*t*t
    assert r>rn
    return float(t*(r-rn)),float(z2/t),float(z4/(t*t))
rows=[]
for t in [32,64,128,256,512,1024,2048]:
    for m in [t,t+t//2,2*t]:
        for g in sorted(set([3,isqrt(t),t//4,t//2])):
            rows.append((t,m,g,*check(t,m,g)))
assert F(27,640)-F(1681,65536)-F(225,4*131072)>F(1,64)
print('cases',len(rows),'ratio_checks',sum(g-1 for t,m,g,*_ in rows))
print('min_scaled_curvature',min(r[3] for r in rows),'max_mode_second',max(r[4] for r in rows),'max_mode_fourth',max(r[5] for r in rows))
print('constant_margin',F(27,640)-F(1681,65536)-F(225,4*131072))
print('selected',[(t,m,g,round(v,9)) for t,m,g,v,*_ in rows if t in [256,2048] and m==2*t])
N=negative=0
for n in range(101):
    for m in range(101):
        if n+m==0: continue
        a,b=F(n,n+3),F(m,m+3)
        c,e=a*F(n-1,n+4),b*F(m-1,m+4)
        r0=(a+b)/2; r1=(3*c+4*a*b+3*e)/(5*(a+b))
        assert 10*(a+b)*(r0-r1)==6*(a*a-c+b*b-e)-(a-b)**2
        t,T=min(n,m),max(n,m)
        neg=(t==0 and T>=10) or (t==1 and T>=81)
        assert (r0<r1 if neg else r0>r1)
        N+=1; negative+=neg
print(N,negative)
```
Actual outputs:
```
cases 84 ratio_checks 9540
min_scaled_curvature 0.4164613077324116 max_mode_second 0.3218683829395445 max_mode_fourth 0.31074800288994653
constant_margin 42227/2621440
selected [(256, 512, 3, 0.862615491), (256, 512, 16, 0.725527661), (256, 512, 64, 0.530097368), (256, 512, 128, 0.472848995), (2048, 4096, 3, 0.89516171), (2048, 4096, 45, 0.778605028), (2048, 4096, 512, 0.560211918), (2048, 4096, 1024, 0.487410668)]
10200 222
```

## Next

HQ's small-deficit sign band and HR's explicit concentration band leave a compact scaled gap roughly sqrt(t)/4 < g < 256sqrt(t), and g>t/2 outside this theorem. Improve constants using both log-ratio derivative terms and localized variance, or prove a uniform signed critical-window curvature theorem. Need to propagate port curvature and mixed capacity shifts through the full P,Q,S ratio before drawing any K conclusion, including shifted port domains. The large-band result is not an effective global K onset. Preserve HN/HO and HQ original evidence; no repeat of asymptotic coverage or finite scans. Independent review and strict Activity observation audit remain pending.
