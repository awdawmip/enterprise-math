# R284IH — Critical square-root inverse profile for the true K observer

2026-11-26. Author derivation, NOT_REVIEWED. Independent continuation of IG, no shared CLAIM/Result/Review mutation. Auxiliary binary-tag safe-word total-count observer; no native physical attribution. Frozen science:
- IG @ffafbea4ff15ff1e169cb6752c2ba8863c362752:research_notes/portable_direct/R284IG_LINEAR_BUDGET_VARYING_LEVEL_NO_RESONANCE_20261126.md
- IC @6a347839e01058e1953013562b1af46cb0603279:research_notes/portable_direct/R284IC_MODE_ANCHORED_INTERVAL_CERTIFICATES_20261126.md (exact joint carrier).
- HY @0164790b93645d9e15c65baa4d77260fcaa8e1c9:research_notes/portable_direct/R284HY_CAPACITY_COUPLING_AND_SQRT_DOMAIN_20261125.md (convolution log-concavity).
- ID @000fb8cf43bf42509bcb2b90e65fdbb5edc95ca8 (global monotonicity author chain, used only for minimal-budget implications).
Current global main entries matched 9c11f74dd15e66d67956007f9e2628d8ec3e000c. P000 V5, ACTIVE worldview and joint preservation read. Prior Activity RA-B82240E8488EF5A1DA5186C4 is historical provenance; own live session not reauthenticated this turn. Native owner inventory request r1-20261126-0758-read-only-owner last observed RUNNING. No protected task writes.

## Theorem
For integer q tending to infinity, d=u-q, s=d/sqrt(q) in any fixed compact subset of (0,infinity), the true combinatorial K satisfies uniformly
q K(q,q+d) = 32/3 + Phi(s)/sqrt(q) + O(1/q),
I(s)= integral_0^s x(s-x) exp(-x^2-(s-x)^2/2) dx,
Phi(s)=112s/9 - (16/3) I'(s)/I(s).
Phi is continuous, strictly increasing, onto R, with slope at least 112/9. For each fixed real lambda, target c(q)=(32/3+lambda/sqrt(q)+O(1/q))/q has a unique limiting transition scale s_lambda>0 defined by Phi(s_lambda)=lambda. Conditional on ID's global author monotonicity, the smallest valid u with K>=c(q) (also with K>c(q)) satisfies u=q+s_lambda sqrt(q)+O(1). No claim of exact rounding or explicit uniform onset.

At lambda=0 the unique root satisfies 968081/10^6 < s_0 < 968082/10^6, certified by rational Taylor-integral enclosures below. Thus the critical level 32/(3q) requires a deficit asymptotic to 0.968081... sqrt(q), not the fixed-slope formula extrapolated to t=1.

## Proof from the actual joint branches (no signed-tail approximation)
IC: m=2q+d, M_n(k)=(k+1)/(n+1) binom(2n+2,n-k) for 0<=k<=n; zero outside. C_(n,m)(g)=sum_k M_n(k)M_m(g-k). Q=C_(u,m)(d-1), V=C_(u,m)(d), A=C_(u-1,m)(d)+C_(u-1,m)(d-1), E=M_(m-1)(0)[M_(u-1)(d)+M_(u-1)(d+1)]. L=(3u+q+1)^2/(u+2q+1). K=L(A+E)Q/(Q+V+qA)^2.

Normalize by H=M_u(0)M_m(0), write R_n(k)=prod_(i=0)^(k-1) (n-i)/(n+i+3). Then joint branches P_k/H=(k+1)(l+1) R_u(k)R_m(l), l=d-k. For s in a compact interval [a,b] of positive numbers, k,l<=b sqrt(q). The log of each product is -(k^2+2k)/n+O_b((k+1)^3/n^2): expand log(1-i/n)-log(1+(i+3)/n) with uniform quadratic remainder. Therefore R_u(k)=exp(-x^2)(1+O_b(q^-1/2)), R_m(l)=exp(-y^2/2)(1+O_b(q^-1/2)), x=k/sqrt(q), y=l/sqrt(q). This is uniform including endpoints. Riemann sums of smooth integrands on the compact triangular domain, including the +1 factors, give V/H=q^(3/2)[I(s)+O_b(q^-1/2)]. I is bounded below on [a,b].

To obtain the needed first difference, do NOT subtract separate Riemann approximations. Use IC's exact t(l)=l(m+l+2)/[(l+1)(m-l+1)] for Q/V. The exact cancellation gives
(l+1)(t(l)-1)=[2l(l+1)-m-1]/(m-l+1)=y^2-1+O_b(q^-1/2).
Thus (Q-V)/H=q[integral_0^s x(y^2-1) exp(-x^2-y^2/2) dx + O_b(q^-1/2)]=-q[I'(s)+O_b(q^-1/2)], where the endpoint contribution in differentiating I is zero. Consequently Q/V=1-q^-1/2 I'/I+O_(a,b)(q^-1).

The shared count A/H is the sum of P_k/H times v(k)(1+t(l)), v(k)=(u-k)(u+k+2)/(2u(2u+1))=1/4+O_b(1/q) uniformly. Hence A=(Q+V)(1/4+O_b(1/q)), not an independent marginal. The exact boundary E/H=(d+1)R_u(d) v(d)(1+r) gamma_m, r=(d+2)(u-1-d)/[(d+1)(u+d+2)], gamma_m=(m+2)/(4m+2), is O_b(sqrt(q)) (all multipliers bounded). Therefore E/A=O_(a,b)(1/q). This pays the genuine boundary contribution at its actual order. L/q=16/3+(56/9)s/sqrt(q)+O_b(1/q). Now
qK=(L/q)(1+E/A)(Q/A)(1+(Q+V)/(qA))^(-2).
Since Q/A=2-I'/[I sqrt(q)]+O_(a,b)(1/q), multiplication gives the asserted expansion. All approximations are solely for this K observer and carry uniform errors.

For strict increase of Phi: use the exact convolution log-concavity from HY, or the usual discrete convolution log-concavity of two nonnegative log-concave sequences without gaps. Hold capacities n=q,m=2q fixed (do not vary them with d). The same product/Riemann proof gives C_(q,2q)(d)/(M_q(0)M_(2q)(0) q^(3/2)) -> I(s) uniformly on compact positive intervals. Piecewise linear interpolation of the logs is concave by discrete log-concavity. The limit log I is concave, so I'/I is nonincreasing. Hence Phi(s2)-Phi(s1)>=112(s2-s1)/9 for s2>s1. Also I(s)=s^3 J(s), J(s)=integral_0^1 y(1-y) exp(-s^2 g(y))dy, g=y^2+(1-y)^2/2 in [1/3,1]. So I'/I=3/s-2s E_s[g]. In particular Phi(s) -> -infinity at 0 and +infinity at infinity. For inversion take d at nearest integer to s_lambda sqrt(q) plus or minus a fixed sufficiently large constant. Uniform O(1/q) remainders and the lower slope bound give strict bracketing of c(q); ID supplies global minimality. This argument does not extrapolate beyond the compact s-window.

Supplement, fixed positive integer d: normalize as above and let q grow. V/H -> binom(d+3,3), Q/H -> binom(d+2,3), A/H -> (V/H+Q/H)/4, E/H -> (2d+3)/16. Thus
lim qK = 32 d(2d^2+6d+7)/[3(d+1)(d+2)(2d+3)]
=32/3 - 32(d^2+2d+2)/[(d+1)(d+2)(2d+3)].
In particular every fixed deficit stays strictly below the critical level eventually. Retaining E was essential for this fixed-d limit; it is lower order only in the compact square-root window.

## Exact executed certificates
Root interval: s Phi(s)=(112/9)s^2-16+(32/3)s^2 E_s[g]. For 0<s<=1 use alternating Taylor bounds for exp(-s^2 g), orders 16 and 17. Polynomial moments of y(1-y)g^j are exact rationals; bounding the ratio of two positive integrals gives strict signs at both rational endpoints. In addition, the true finite K observer was evaluated using 80-bit outward integer intervals, with exact recurrence and all E terms retained. Actual outputs (decimal displays are not the comparisons):
q=100: d=12,13, qK-32/3 upper/lower gaps -0.11531164849308595,+0.11540146085441841
q=10000: d=98,99, gaps -0.0031066888988601007,+0.00014813857518938258
q=1000000: d=970,971, gaps -5.1807204333848665e-06,+2.8493188921976675e-05
q=100000000: d=9682,9683, gaps -2.976196774653454e-07,+4.058322125644428e-08
These four pairs are strict actual K brackets by interval separation. Minimality depends on ID, not the bisection alone. The proof of the unbounded profile is analytic, not extrapolated from these samples.

Reproduction (Python 3; integers/Fraction; all sign tests exact; float only for output):
```python
from fractions import Fraction as F
from math import factorial,isqrt
from functools import lru_cache
@lru_cache(None)
def moment(j):
    p=[F(1)]
    for _ in range(j):
        v=[F(0)]*(len(p)+2)
        for i,c in enumerate(p):
            for h,a in enumerate([F(1,2),-1,F(3,2)]):v[i+h]+=c*a
        p=v
    return sum(c/F((i+2)*(i+3)) for i,c in enumerate(p))
def enclosure(s,j,N=16):
    def sm(n):return sum((-s*s)**i*moment(i+j)/factorial(i) for i in range(n+1))
    return sm(N+1),sm(N)
def sign(s):
    a,b=enclosure(s,0);c,d=enclosure(s,1)
    h=F(112,9)*s*s-16;z=F(32,3)*s*s
    assert a>0
    return h+z*c/b,h+z*d/a
a,b=0,1000000
while b-a>1:
    m=(a+b)//2;lo,hi=sign(F(m,1000000))
    if hi<0:a=m
    elif lo>0:b=m
    else:raise ValueError(m)
print('root enclosure:',a,b,'/1000000')
assert sign(F(a,1000000))[1]<0<sign(F(b,1000000))[0]
S=1<<80
def mul(w,n,d):return (w[0]*n//d,(w[1]*n+d-1)//d)
def add(w,v):return (w[0]+v[0],w[1]+v[1])
def prod(w,v):return (w[0]*v[0]//S,(w[1]*v[1]+S-1)//S)
def weights(n,d):
    w=[(S,S)]
    for i in range(d):w.append(mul(w[-1],n-i,n+i+3))
    return w
def Kq(q,d):
    u=q+d;m=u+q
    p,r=weights(u,d),weights(m,d)
    V=Q=A=E=(0,0)
    for k in range(d+1):
        l=d-k;w=mul(prod(p[k],r[l]),(k+1)*(l+1),1)
        tn=l*(m+l+2);td=(l+1)*(m-l+1);vn=(u-k)*(u+k+2);vd=2*u*(2*u+1)
        V=add(V,w);Q=add(Q,mul(w,tn,td));A=add(A,mul(w,vn*(tn+td),vd*td))
        if l==0:E=mul(mul(mul(w,vn,vd),(d+1)*(u+d+2)+(d+2)*(u-1-d),(d+1)*(u+d+2)),m+2,4*m+2)
    B=add(add(Q,V),mul(A,q,1));ae=add(A,E)
    f=F(q*(3*u+q+1)**2,u+2*q+1)
    return f*F(ae[0]*Q[0],B[1]**2),f*F(ae[1]*Q[1],B[0]**2)
for q in [100,10000,1000000,100000000]:
    a,b=0,2*isqrt(q)+1
    while b-a>1:
        m=(a+b)//2;lo,hi=Kq(q,m)
        if hi<F(32,3):a=m
        elif lo>F(32,3):b=m
        else:raise ValueError((q,m))
    lo,hi=Kq(q,a);lo2,hi2=Kq(q,b)
    assert hi<F(32,3)<lo2
    print(q,a,b,float(F(b,isqrt(q))),float(hi-F(32,3)),float(lo2-F(32,3)))
```
Each operation encloses a nonnegative exact rational after common scaling by S; denominators are positive for the actual sample deficits. No overflow (Python integers). The embedded replay is the executed algorithm with unused imports and illustrative sign printouts removed.

## Next
Compute the second-order uniform profile, including the genuine boundary E, to resolve the O(1) shift; study rounding near irrational s_0 sqrt(q). Independent audit of ID remains open. Reconcile current own session and Activity checkpoint rather than inventing a live binding.