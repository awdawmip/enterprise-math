# R284JI — Full second-branch window positivity via joint coefficient representation
2026-11-27. Author proof and exact replay, NOT_REVIEWED. Auxiliary binary-tag joint observer, not a native spatial or dynamical transfer. Continuation of existing directed activity RA-B82240E8488EF5A1DA5186C4, EM-DIRECT-0C386E / TASK_RESEARCH. Own session recovery returned registered, unclosed, no runs; no Task claim or shared owner change. Owner inventory r1-20261127-1055-owner SUCCEEDED, as-of 2026-11-27T02:56:27.140977Z, no LEASED entries, admitted Source a338cfa206138982a68a88b2d858c8fca1c54c5d, later Source drift 99e369a4bdb0abefa154f6e8c4dd6e9f62678ee0 recorded. P000 V5, ACTIVE worldview, joint and residual preservation consulted.
Frozen input: decfd2e7f01e53d1036716b13efda9bf1bb36e87:research_notes/portable_direct/R284JH_SECOND_BRANCH_REMOVABLE_POLE_AND_HALF_WINDOW_20261127.md, JH, full read; c7853ca73cbf8d3c4e85fd3810293d63a485c000:research_notes/portable_direct/R284JG_SECOND_BRANCH_GROWING_OFFSET_CERTIFICATES_20261127.md, JG, full read. JG gives pole reduction for all 3<=r<d; JH proved positivity only for r<=d/2. Here positivity extends to every 3<=r<d, including the exterior coefficient zero d=2r-3.

## 1. Statement and exact joint coefficient identities
Retain JG's primal q>=64, d^2<=4q, u_primal=q+d, m=2q+d, R_n(k)=prod_{i<k}(n-i)/(n+i+3), full V,Q,A,E,Z,C,Y. At second-branch pole N=2q+2d-r+2, j=d-r, T=R_m(j), p|N and p>4d+6, JG proves C/T^2 mod p equals G below, all normalized observations reduce as specified there. Use formal u=(r-2)/2, q0=u-d, b=2j+2, c_h=(-1)^h binom(2j+h+1,h), U_k=R_u(k), B_k=B0 R_{u-1}(k) with B0=(u+2)/(2(2u+1)). This B identity follows from JH's exact zero-safe recurrence. Put h=r-k,l=d-k. Reduced V,Q,A sum (k+1)(l+1)c_h U_k, (k+1)l c_(h-1) U_k, and B_k times the sum of the two coefficient weights, respectively; omit the second weight at h=0. E*=0 only at this normalized layer; keep primal E for higher jets. Write Z=q0 A+Q+V and G=3q0(4q0+3d+1)^2 A Q-32(3q0+d+1)Z^2.
Define F_w(x)=sum_{k>=0}(k+1)(-1)^k R_w(k)x^k and K(w,a,n)=[x^n](1+x)(1-x)^(-a)F_w(x).
Then EXACTLY:
(-1)^r V=(j+1)K(u,b+1,r),
(-1)^(r-1) Q=(j+1)K(u,b+1,r-1),
(-1)^r A=(j+1)B0 K(u-1,b,r),
(-1)^r(V+Q)=(j+1)K(u,b,r).
Indeed sum_h binom(2j+h+1,h)x^h=(1-x)^(-b); weighting by j+h+1 gives (j+1)(1+x)(1-x)^(-b-1). The shifted b fiber has h'=h-1 and l=j+h'+1, so Q uses exactly the same coefficient kernel shifted by one; in the signed joint sum the shift is subtraction, multiplying by (1-x). No discarded signed term or inference from absolute mass.

## 2. Coefficient positivity lemma (new, unbounded)
For w in {-1/2,0,1/2,1,...}, integer a>=2 and integer n>w, prove [x^n](1-x)^(-a)F_w(x)>0.
Beta integral identity (auxiliary proof device; exact rational coefficients):
F_w(x)=(w+1)(w+2) integral_0^1 t(1-t)^w (1-tx)^w dt.
Expand at x=0 and integrate termwise near 0; integration by parts gives integral t^(k+1)(1-t)^w=(k+1)!/[(w+1)...(w+k+2)], producing precisely the defining coefficient. All integrals converge for w>=-1/2. Write Cw=(w+1)(w+2)>0.
Case a>=w: the product at fixed 0<t<1 equals exp(sum_{i>=1}(a-w t^i)x^i/i); every log coefficient is positive (also w=-1/2), so all coefficients are positive.
Case w integer >=0, a<w: expand (1-tx)^w=((1-x)+(1-t)x)^w by binomial theorem. Each term after division by (1-x)^a is a nonnegative constant times x^k(1-x)^(w-k-a). If exponent is nonnegative, polynomial degree w-a<n, hence its coefficient is zero. Otherwise the series has nonnegative coefficients; k=w gives strictly positive coefficient at n>w for t<1. Integrate.
Case w positive noninteger half-integer and a<w. Let gamma=w-a>0. Taylor in y=1-x at y=0 gives the exact expression
(1-tx)^w/(1-x)^a
= sum_{i=0}^{a-1} binom(w,i)(1-t)^(w-i)t^i (1-x)^(i-a)
+ a binom(w,a)t^a integral_0^1 (1-s)^(a-1)(1-t+st-stx)^gamma ds.
The finite pole part has positive coefficients. Its i=0 contribution after the outer weighted integration, divided by Cw, is binom(a+n-1,n)/[(2w+1)(2w+2)] >= (n+1)/[(2w+1)(2w+2)]. The signed remainder is retained and paid. For 0<t<1, 0<=s<=1, A0=1-t+st, z=st/A0<=t and A0<=1. Its x^n coefficient magnitude is at most |binom(gamma,n)| t^n because A0^gamma<=1. The binomial magnitude is <=1 for n>gamma: at ceil(gamma) compare factors with ceil(gamma), and subsequent magnitudes decrease. Integrating s and t, remainder magnitude divided by Cw is <=binom(w,a) integral_0^1 t^(a+n+1)(1-t)^w dt <= binom(w,a) 4^(-w), since n>w and t(1-t)<=1/4. The latter bound is strictly less than the pole lower bound:
- for w>=11/2, binom(w,a)<=2^ceil(w), so bound <=2^(1/2-w)<1/(4w+2)<(n+1)/[(2w+1)(2w+2)]. The first strict inequality follows at w=11/2 (32>24) and persists under each integer increment.
- for w=5/2, 7/2, 9/2, max over 2<=a<=floor(w) of binom(w,a)4^(-w) is respectively 15/256,35/1024,63/4096; lower bound at n=ceil(w) is respectively 2/21,5/72,3/55. All strict. These cases exhaust the half-integer domain with a<w.
Thus the coefficient is strictly positive, with actual signed remainder bounded, on the entire stated domain. No asymptotic conjecture or numerical approximation is used.

## 3. Full-window theorem and zero exterior factor
For every d>=4, 3<=r<d, b>=4 and r-2=2u>u since u>=1/2. Both coefficients of each K in section 1 lie in the positivity lemma (even Q uses indices r-1 and r-2). Therefore (-1)^r V, (-1)^(r-1) Q, (-1)^r A, and (-1)^r(V+Q) are strictly positive. Since q0<0 and 3q0+d+1<0, G>0 immediately unless 4q0+3d+1=0, i.e. d=2r-3=4u+1.
In this special case u>=1, q0=-3u-1, b=4u. For fixed t let H=(1+x)(1-x)^(-b)(1-tx)^(u-1), whose coefficients are positive by the log argument in section 2. Multiplying H by (1-tx) reduces its x^r coefficient. The beta weight for F_u divided by that for F_(u-1) is (u+2)(1-t)/u <= (u+2)/u. Thus K(u,b,r)<(u+2)/u K(u-1,b,r) by pointwise strict comparison and positive integration. It follows from the identities that
0<(V+Q)/A<2(2u+1)/u.
For u>=3/2, 2(2u+1)/u <3u+1 (equiv 3u^2-3u-2>0). Consequently (-1)^r Z<0, so the squared term makes G>0 even with the exterior coefficient zero. The one remaining u=1 case d=5,r=4 has V=160,Q=-80,A=55,Z=-140,G=3763200, directly by rational sums.
Hence G>0 for ALL 3<=r<d, with no half-window restriction. For p|N and p>4d+6, any p not dividing the integerized residue certifies Y!=32/3 by JG. r=1 and r=2 keep their JA/JH special treatments; r=d is outside JG's pole model.

## 4. Uniform height, scope and next issue
JG's Dbar=8(r-2)(r-1) lcm(1,...,3r+2) clears all six reduced observations for all r<d by its factor-count proof; 2 Dbar^2 G is a positive integer, and p>4d+6 never divides Dbar. For the extended range, |U_k|<=1, |B_k|<=B0<=1 and |c_h|<=|c_r|. Bound each sum by O(d(r+1)^2 |c_r|)=O(d^3 |c_r|), Z=O(d^4 |c_r|), G=O(d^9 |c_r|^2). With |c_r|<= (e(2d+1)/r)^r and log Dbar=O(r+log r), log(2 Dbar^2 G)=O(r log(ed/r)+log d), uniformly on the full range. Hence the JF/JG exceptional prime budget O(1+r log(ed/r)/log d) survives unchanged in order. The new theorem supplies all interior second-branch candidate positions; it alone does not bound simultaneous exceptional congruences more sharply, or certify all q. BRC contribution: exact joint generating coefficient kernel with signed Taylor residual explicitly paid, not a raw branch erasure. All full primal sources remain for higher jets. Next: derive cross-offset recurrence for integerized residues and use the full window to study simultaneous failures; separately lift r=2 exceptional primes and investigate r=d edge.

## 5. Actual exact replay (Python Fraction)
Executed: 7938 coefficient-positivity checks (w=-1/2..20 by halves, a=2..22, nine n>w each); 6903 full-triangle (d=4..120,3<=r<d) checks, including 3539 outside JH half-window and 58 exterior-factor zero cases. Verified all four coefficient identities, strict signs, G>0, Dbar and integerized residue. Six additional checks: (5,4),(301,300),(300,299),(1000,999),(1001,1000),(10^60,100), bit lengths of 2 Dbar^2 G respectively 71,2703,2703,8798,8821,40910. All assertions passed. No fresh primal congruence replay is claimed: JG's full-range congruence is reused at its unchanged hypotheses. Analytic proof, not finite extrapolation, bears the unbounded conclusion.

```python
from fractions import Fraction as F
from math import comb,lcm

def coeff(w,b,n):
    if n<0: return F(0)
    t=F(1); s=F(0)
    for k in range(n+1):
        s+=(k+1)*t*comb(b+n-k-1,n-k)
        t*=-(w-k)/(w+k+3)
    return s

def reduced(d,r):
    u=F(r-2,2); q=u-d; j=d-r
    c=[(-1)**h*comb(2*j+h+1,h) for h in range(r+1)]
    U=[F(1)]; B=[(u+2)/(2*(2*u+1))]
    for k in range(r):
        U.append(U[-1]*(u-k)/(u+k+3)); B.append(B[-1]*(u-k-1)/(u+k+2))
    V=Q=A=F(0)
    for k in range(r+1):
        l=d-k; h=r-k
        a=(k+1)*(l+1)*c[h]; b=(k+1)*l*c[h-1] if h else 0
        V+=U[k]*a; Q+=U[k]*b; A+=B[k]*(a+b)
    Z=q*A+Q+V; G=3*q*(4*q+3*d+1)**2*A*Q-32*(3*q+d+1)*Z**2
    return V,Q,A,Z,G

def check(d,r):
    V,Q,A,Z,G=reduced(d,r); u=F(r-2,2); j=d-r; b=2*j+2; s=(-1)**r
    def K(w,b,n):return coeff(w,b,n)+coeff(w,b,n-1)
    assert s*V==(j+1)*K(u,b+1,r)
    assert -s*Q==(j+1)*K(u,b+1,r-1)
    assert s*A==(j+1)*(u+2)/(2*(2*u+1))*K(u-1,b,r)
    assert s*(V+Q)==(j+1)*K(u,b,r)
    assert s*V>0 and -s*Q>0 and s*A>0 and s*(V+Q)>0 and G>0
    D=8*(r-2)*(r-1)*lcm(*range(1,3*r+3)); P=2*D*D*G
    assert all((D*x).denominator==1 for x in (V,Q,A,Z)) and P.denominator==1
    if d==2*r-3: assert s*Z<0
    return P.numerator.bit_length()

nc=0
for h in range(-1,41):
    w=F(h,2)
    for b in range(2,23):
        for n in range(max(0,int(w)+1),max(0,int(w)+1)+9):
            assert n>w and coeff(w,b,n)>0
            nc+=1
print('coefficient checks',nc)
count=outer=deg=0
for d in range(4,121):
    for r in range(3,d):
        check(d,r); count+=1;outer+=2*r>d;deg+=d==2*r-3
print('full triangle',count,'new outer half',outer,'degenerate',deg)
for d,r in [(5,4),(301,300),(300,299),(1000,999),(1001,1000),(10**60,100)]:
    print('large/special',d,r,check(d,r))
```
