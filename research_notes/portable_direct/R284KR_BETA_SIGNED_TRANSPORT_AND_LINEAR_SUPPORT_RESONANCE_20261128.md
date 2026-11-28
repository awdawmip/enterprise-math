# R284KR - Beta signed transport, linear moving-support wedge, and macroscopic resonance

2026-11-28. Author proof and exact Fraction calculations, NOT_REVIEWED. Auxiliary R284 arithmetic; not native spatial transfer. Existing own EM-DIRECT-0C386E / TASK_RESEARCH / RA-B82240E8488EF5A1DA5186C4. Native own metadata read r1-20261128-2156-own-metadata-read recovered original open registration and no formal runs; metadata is not execution authority. Native owner read r1-20261128-2156-owner-read SUCCEEDED, inventory INV-22aa7896843bdb1aa8d674a9bd0e4203, as of 2026-11-28T13:56:41.388149Z, 547 tasks, LEASED filter empty, no new Task/claim/owner mutation. Continue existing independent frontier. Global canonical entries at 7f5319e5095a8948483ebddb65d862bd649bfe77, current Source normative/foundation/portable/method at c6f9d9519686f97193e91062414b5f23215b425d, P000 V4 and V5 projection, ACTIVE worldview, joint and residual typing read. Frozen science:
- JR 88211c0912397b00536b6c4d6427cab29d4499f2:research_notes/portable_direct/R284JR_GLOBAL_BUDGET_POLYNOMIAL_AND_INTEGER_ROOT_EXCLUSION_20261127.md
- KO 0c99ee610045cd1d36e9da996f257ae4afabc0be:research_notes/portable_direct/R284KO_FIXED_SUPPORT_FAMILY_AND_EVEN_DECIC_20261128.md
- KP 3446e2f82ae8f61a7893f961d0c7ac065b6f2e39:research_notes/portable_direct/R284KP_FIXED_SUPPORT_NONVANISHING_AND_RESONANCE_20261128.md
- KQ 9f197a62d294f15210a2cc1c161ad2201d5c583b:research_notes/portable_direct/R284KQ_UNIFORM_SUPPORT_WEDGE_AND_RESONANT_SIGN_20261128.md

## 1. Exact signed beta transport

Maintain JR's complete V,Q,A,E,W,Z,C, R_v(k)=product_{j<k}(v-j)/(v+j+3). KO fiber q0=(s-d)/2, u=(d+s)/2, r=R_u(d) nonzero by d+s odd, with integer s>=0 and d>=max(3,s+2). This proof works on d>=8(s+4); all results below retain parity. Set a=(3d+s+4)/2, b=(d-s-2)/2, and let X have the auxiliary classical beta density with parameters b+1 and a-b. Set Y=1/X. For i<=s+1, b>i-1, so the exact beta integral gives E[Y^i]=a_falling_i/b_falling_i. In particular KO's signed backward ratio is rho_i=(-1)^i E[Y^i]. This is a mathematical integration identity for the signed arithmetic observer, not a random physical model.

Define S_s(y)=sum_{i=0}^s (i+1) R_s(i)(-y)^i, T_s(y)=-y S_s(y), D_y=y d/dy. The coefficients of T are exactly the shifted second branch, including the i=s+1 term. By expanding (1-yt)^s and integrating t^(i+1)(1-t)^s,
S_s(y)=(s+1)(s+2) integral_0^1 t[(1-t)(1-yt)]^s dt.
Set L_d=1+(1-D_y)/d. With Vbar=V/(rd), Qbar=Q/(rd), Abar=A/(rd), Ebar=E/(rd):
Vbar=E[L_d S_s(Y)], Qbar=E[L_d T_s(Y)].
For the A weights define w(i)=(-d+s+2i)(3d+s-2i+4)/(4(d+s)(d+s+1)). Then exactly
Abar=E[w(D_y)L_d(S_s+T_s)(Y)].
All operators here are finite polynomials in D_y; no interchange of divergent series. The endpoint is
Ebar=-(s+2)/(4(2s+1)) * (1-s/d)*(1+3/(2d))/(1+(s+1)/d).
Thus the whole joint observer, including endpoint, is retained, not reduced to unsigned mass. This is a reusable exact transport for these declared finite moment observers; not a full-state equivalence for arbitrary future operations.

## 2. Uniform tail suppression (the step that removes KQ's exponential loss)

Let d>=8(s+4), a<=25d/16, b>=7d/16+1, m=floor(d/32). For 0<=j<=s, (a-j)/(b-j) <=23/5, and at j=0 <=25/7. For 0<=j<=s+m, the ratio <=5 (use j<=5d/32). The function log((a-j)/(b-j)) is convex in real j<b since its second derivative is 1/(b-j)^2-1/(a-j)^2>0. Its sum for j=0..s is bounded by (s+1)/2 times the sum of the endpoint log values (also true when s=0 using the looser endpoint bounds). Therefore
E[Y^(s+1)] <= (sqrt(115/7))^(s+1).
Since log(sqrt(115/112)) <=3/224 and s<=d/8,
4^(-s) E[Y^(s+1)] <=5 exp(3d/1792).
Take tail Y>11/2. On the tail Y^(-m)<=(2/11)^m. The next m inverse moment factors are <=5. Hence
4^(-s) E[Y^(s+1) 1_(Y>11/2)] <=5 exp(3d/1792)(10/11)^m <=6 exp(-d/1000).
The last inequality follows from m>=d/32-1, log(11/10)>=1/11 and 1/352-3/1792>1/1000. Every inverse moment here exists because b>s+m.

For y>=11/2, write f_y(t)=(1-t)(1-yt). On [0,1], |f_y(t)|<=y/4: its positive part <=1, its negative minimum has magnitude (y-1)^2/(4y)<y/4. Also t(1-t)<=1/4. For each fixed k<=3, differentiating the integral at most k times, and writing D_y^k as a finite linear combination of y^j times the j-th ordinary derivative, gives
|D_y^k S_s(y)| <= c_k (s+2)^(k+2)(y/4)^s,
|D_y^k T_s(y)| <= c'_k (s+2)^(k+2)y(y/4)^s.
If j>s the corresponding derivative is zero. Consequently the expected absolute contribution from Y>11/2 to any of these Euler moments is O_k((s+2)^(k+2) exp(-d/1000)), uniformly in the wedge. This tends to zero faster than every inverse power of d because s<=d/8. Unlike KQ's unsigned bound, this pays for the signed cancellation before bounding the tail.

On 1<=y<=11/2, the negative part of f_y has magnitude <=81/88<1; its positive part <=1-t. For any fixed ordinary derivative order j<=3, differentiating the integral gives the factor (s)_fall_j [t(1-t)]^j f_y^(s-j). On the positive part, integrate t^(j+1)(1-t)^s, multiply by (s+1)(s+2)(s)_fall_j, and obtain a bound <=(j+1)!. On the negative part the bound is O_j((s+2)^(j+2)(81/88)^(s-j)), uniformly bounded in s (zero derivative when s<j). Thus S_s, its derivatives up to order 3, T_s and their Euler moments up to order 3 have uniform bounds on this whole central interval. Together with the tail estimate the expected Euler moments are uniformly bounded.

## 3. Uniform macroscopic profile, with quantitative error order

For s>=1, uniformly in 1<=y<=11/2,
S_s(y)=(1+y)^(-2)+O(1/s).
Proof: put t=z/s. On t<=1/12, -log f_y(t)=(1+y)t+R, with 0<=R<=(1+y^2)t^2 (use -log(1-x)-x<=x^2 for 0<=x<=1/2). Hence the difference between f_y(z/s)^s and exp(-(1+y)z) is at most exp(-(1+y)z)(1+y^2)z^2/s. Integration against z and the factor (s+1)(s+2)/s^2 gives O(1/s). On t>=1/12 the positive contribution has magnitude bounded by (11/12)^s, negative by (81/88)^s; even after the prefactor these are O(1/s). The limiting integral is integral_0^infty z exp(-(1+y)z) dz=(1+y)^(-2).

Let lambda=s/d in [0,1/8]. The exact mean and variance of Y are
mu=a/b=(3d+s+4)/(d-s-2),
Var(Y)=a(a-b)/(b^2(b-1)).
Thus mu=(3+lambda)/(1-lambda)+O(1/d), 3<=mu<4 on the stated wedge, Var(Y)=O(1/d) uniformly. The central Taylor remainder for S_s or T_s at mu is bounded by a universal constant times (Y-mu)^2 using the uniform derivative bounds above. Since E[Y-mu]=0, the linear term cancels in the full expectation. Its tail contribution and the constant term on the tail are negligible: E[Y 1_(Y>11/2)]<=5(10/11)^m by the same inverse-moment bound with i=1, and probability is no larger. The tail of S_s and T_s was already controlled. Hence E[S_s(Y)]=S_s(mu)+O(1/d), and similarly for T_s. The L_d correction is O(1/d) by bounded expected Euler moments. In Abar, the constant coefficient w(0)=w_lambda+O(1/d), w_lambda=(lambda-1)(lambda+3)/(4(1+lambda)^2); the linear and quadratic coefficients are O(1/d) and O(1/d^2), respectively. This follows directly from expanding w(i); equivalently w(i)+3/4=[d(8s-1)+4s^2+7s+(8d+8)i-4i^2]/[4(d+s)(d+s+1)]. Euler moments through order 3 therefore give Abar=w_lambda(Vbar+Qbar)+O(1/d). Exact Ebar above has error O(1/s+1/d) relative to -(1-lambda)/(8(1+lambda)).

It follows that the normalized joint values differ uniformly from these rational functions by O(1/s+1/d):
V0=(lambda-1)^2/16,
Q0=(lambda-1)(lambda+3)/16,
A0=(lambda-1)^2(lambda+3)/(32(lambda+1)),
E0=(lambda-1)/(8(lambda+1)),
W0=(lambda-1)(lambda+1)/32,
Z0=(lambda-1)^3(lambda+3)/(64(lambda+1)).
Here Z is normalized by rd^2 and W by rd. In particular the endpoint contribution is essential to the simple W0 formula. JR's normalized C is
3(q0/d)(1+(2s+1)/d)^2 Wbar Qbar -32((3q0+d+1)/d) Zbar^2.
The coefficient limits are (3/2)(lambda-1)(1+2lambda)^2 and 16(1-3lambda). Substitution and elementary simplification establish the theorem:
C(q0,d)/(r^2 d^5) = Phi(lambda)+O(1/s+1/d),
Phi(x)=(x-1)^3(x+3) [52x^4+147x^3-63x^2+89x-9]/[1024(x+1)^2],
uniformly for all admissible s>=1, d>=8(s+4). Constants are absolute and the proof gives finite bounds, not optimized explicit thresholds. The limiting value at zero is 27/1024, matching KQ's iterated limit. No claim beyond this wedge.

## 4. Consequences: linear wedge and a new resonance strip

Let P(x)=52x^4+147x^3-63x^2+89x-9. P'(x)>=89-126/8>0 on [0,1/8]. P(0)=-9, P(1/8)=1475/1024>0. There is exactly one lambda_* in (0,1/8), simple; exact bisection below gives approx 0.107140924600. Phi is positive below it and negative above it. For any fixed 0<c<lambda_*, there exists d0(c) such that all admissible 0<=s<=c d, d>=d0(c), have C/r^2>0 except s=5 (negative for d>=188 by KQ). Proof: the profile is bounded away from zero on [0,c]; take s sufficiently large for the uniform error, then handle the finitely many small s by KP/KQ's fixed-s limits including the nonzero next term for s=5. For any fixed lambda_*<c'<1/8, there exists d1(c') with negative C/r^2 whenever c'd<=s and d>=8(s+4), d>=d1(c'). This is a linear-in-d support range, replacing KQ's logarithmic sufficient wedge, with a distinct macroscopic sign reversal.

Moreover every admissible zero of this formal fiber for sufficiently large d in d>=8(s+4) lies in a bounded-width strip |s-lambda_* d|<=K for an absolute K: outside a fixed neighborhood of lambda_*, the sign results (small s handled as above) exclude zero. Inside, s is proportional to d and the error is O(1/d); Phi has a simple zero so the mean value theorem gives |s/d-lambda_*|=O(1/d). No assertion of existence of any exact integer zero in this strip, nor of an explicit optimized K. Finite-d sign mismatch at d=1000,s=107 (see output) is a warning against using the limiting profile as an exact classifier inside the strip.

KO's N_s(d) is nonzero on the above sign regions; for p>d+s+2, the exact arithmetic implication for a positive-budget integer zero is still v_p(2q+d-s)<=v_p(N_s(d)) when p divides the coordinate. Thus linearly many formal observers are available, with the same KO prime scope. Uniform coefficient height and joint prime coverage remain open. This does not enlarge the original positive-q all-budget integer-exclusion range 3<=d<=3200. No formal Result, independent review, or Foundation admission.

## 5. Reproduction

The following exact Python program was executed. Two separate expressions, the KO short-support rational sum and the new beta/Euler evaluation, match exactly as tuples of normalized V,Q,A,E,C at 64 admissible points. All arithmetic except display of profile/errors is Fraction. First 49 checks cover d=257,513,1025 with even s<=32 satisfying d>=8(s+4); remaining 15 cover d=1000,4000,16000 and the five specified ratios with parity adjustment. The sign comparison is evidence, not the proof of the uniform asymptotics.

```python
from fractions import Fraction as F
from math import comb

def profile(l):
    p=52*l**4+147*l**3-63*l**2+89*l-9
    return (l-1)**3*(l+3)*p/(1024*(l+1)**2)

def short(d,s):
    assert d>=s+2 and (d+s)%2
    q=F(s-d,2); u=F(d+s,2); J=(d+s)*(d+s+1)
    V=Q=A=F(0); r=rho=F(1);prev=F(0)
    for i in range(s+2):
        if i:
            r*=F(s-i+1,s+i+2)
            rho*=F(3*d+s+6-2*i,s-d+2*i)
        a=(d-i+1)*(i+1)*rho*r;b=(d-i+1)*i*rho*prev
        V+=a;Q+=b;A+=F((u-d+i)*(u+d-i+2),J)*(a+b)
        prev=r
    E=F((u-d)*(2*d+3)*(s+2),2*(2*u+1)*(4*s+2))
    W=A+E;Z=q*A+Q+V
    C=3*q*(4*q+3*d+1)**2*W*Q-32*(3*q+d+1)*Z**2
    return V/d,Q/d,A/d,E/d,C/d**5

def beta(d,s):
    # direct beta-integral coefficient recurrence, followed by Euler moments
    aa=F(3*d+s+4,2);bb=F(d-s-2,2);Y=F(1);c=F(1)
    v=[F(0)]*4;z=[F(0)]*4
    for i in range(s+2):
        if i<=s:
            for k in range(4):v[k]+=c*Y*i**k
        if i:
            for k in range(4):z[k]-=prev*Y*i**k
        prev=c
        if i<=s:
            c*=-F((i+2)*(s-i),(i+1)*(s+i+3))
            Y*=F(aa-i,bb-i)
    V=v[0]+(v[0]-v[1])/d;Q=z[0]+(z[0]-z[1])/d
    T=[v[k]+z[k] for k in range(4)]
    a0=d*(8*s-1)+4*s*s+7*s;a1=8*d+8;a2=-4
    A=-F(3,4)*(V+Q)+sum(a*(T[k]+(T[k]-T[k+1])/d) for k,a in enumerate([a0,a1,a2]))/(4*(d+s)*(d+s+1))
    E=-F(s+2,4*(2*s+1))*F(d-s,d)*F(2*d+3,2*d)*F(d,d+s+1)
    q=F(s-d,2);Z=q*A/d+(Q+V)/d
    C=3*q/d*F(d+2*s+1,d)**2*(A+E)*Q-32*F(3*q+d+1,d)*Z**2
    return V,Q,A,E,C

def sign(x):return '+' if x>0 else '-' if x<0 else '0'

def quartic(l):return 52*l**4+147*l**3-63*l**2+89*l-9
lo=F(0);hi=F(1,8)
assert quartic(lo)<0<quartic(hi)
for _ in range(50):
    md=(lo+hi)/2
    if quartic(md)<0:lo=md
    else:hi=md
print('quartic root bracket:',lo,hi,format(float(lo),'.12f'),format(float(hi),'.12f'))
count=0
for d in (257,513,1025):
    for s in range(min(32,d//8-4)+1):
        if (d+s)%2 and d>=8*(s+4):
            assert short(d,s)==beta(d,s);count+=1
print('exact beta Euler vs short-support identities:',count)
# d fixed, s selected near four ratios and sign transition; enforce parity.
for d in (1000,4000,16000):
    for frac in (F(1,16),F(1,10),F(107,1000),F(11,100),F(3,25)):
        s=int(frac*d);s-=int((d+s)%2==0)
        assert d>=8*(s+4)
        a=short(d,s);b=beta(d,s);assert a==b;count+=1
        p=profile(F(s,d));err=abs(a[-1]-p)
        print('d=%d s=%d lambda=%.6f Cnorm=%.12g profile=%.12g err=%.6g sign=%s/%s'%(d,s,s/d,float(a[-1]),float(p),float(err),sign(a[-1]),sign(p)))
print('total exact identity checks:',count)
```

Actual output:
```text
quartic root bracket: 965039656210563/9007199254740992 241259914052641/2251799813685248 0.107140924600 0.107140924600
exact beta Euler vs short-support identities: 49
d=1000 s=61 lambda=0.061000 Cnorm=0.00841511445572 profile=0.00829133956943 err=0.000123775 sign=+/+
d=1000 s=99 lambda=0.099000 Cnorm=0.00112933069632 profile=0.00120747063196 err=7.81399e-05 sign=+/+
d=1000 s=107 lambda=0.107000 Cnorm=-7.71927721228e-05 profile=2.00819835083e-05 err=9.72748e-05 sign=-/+
d=1000 s=109 lambda=0.109000 Cnorm=-0.000363662266673 profile=-0.000262288636432 err=0.000101374 sign=-/-
d=1000 s=119 lambda=0.119000 Cnorm=-0.00171033582331 profile=-0.0015918287038 err=0.000118507 sign=-/-
d=4000 s=249 lambda=0.062250 Cnorm=0.00804528967961 profile=0.00801557963842 err=2.971e-05 sign=+/+
d=4000 s=399 lambda=0.099750 Cnorm=0.00107256898286 profile=0.00109211819214 err=1.95492e-05 sign=+/+
d=4000 s=427 lambda=0.106750 Cnorm=3.19951314252e-05 profile=5.57770057554e-05 err=2.37819e-05 sign=+/+
d=4000 s=439 lambda=0.109750 Cnorm=-0.000392064116257 profile=-0.000366727490176 err=2.53366e-05 sign=-/-
d=4000 s=479 lambda=0.119750 Cnorm=-0.0017158013698 profile=-0.00168620068422 err=2.96007e-05 sign=-/-
d=16000 s=999 lambda=0.062437 Cnorm=0.00798191462254 profile=0.00797449146242 err=7.42316e-06 sign=+/+
d=16000 s=1599 lambda=0.099937 Cnorm=0.00105852465482 profile=0.00106341300211 err=4.88835e-06 sign=+/+
d=16000 s=1711 lambda=0.106938 Cnorm=2.30518598969e-05 profile=2.89973867676e-05 err=5.94553e-06 sign=+/+
d=16000 s=1759 lambda=0.109937 Cnorm=-0.0003990483981 profile=-0.000392714587668 err=6.33381e-06 sign=-/-
d=16000 s=1919 lambda=0.119938 Cnorm=-0.00171707915911 profile=-0.00170968058475 err=7.39857e-06 sign=-/-
total exact identity checks: 64
```

## Next
Derive explicit first-order correction to Phi in the macroscopic resonance strip and integer separation or a uniform height bound for N_s when s grows; use signed transport as an analytic tool, retain full arithmetic observer for congruences. Evaluate union gains on actual positive-budget root neighbors d>3200. No exact zero asserted in the strip.
