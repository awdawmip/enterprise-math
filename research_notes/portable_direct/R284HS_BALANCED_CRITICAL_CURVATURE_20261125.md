# R284HS - Uniform critical-window curvature for balanced joint ports

2026-11-25. Author proof, exact finite checks, NOT_REVIEWED. Auxiliary binary-tag safe-word total-count observer; not native physical attribution, no modification of P000 and no new full-K monotonicity theorem. Frozen sources: ee9230b632b0e33e4d160856ba551ec906610750:research_notes/portable_direct/R284HR_BALANCED_PORT_CONCENTRATION_CURVATURE_20261125.md; b0572296445fe5355dd4807ac4d6073fe69e8144:research_notes/portable_direct/R284HQ_EXACT_CURVATURE_BRANCH_BALANCE_20261125.md. Current account entries verified at 2f8b828c1ee152e9d4a25be297525ce439a28377, continuation entry at a63d0008fc9cc8803a0147c29af70fd686b1b80f. P000 V5, ACTIVE worldview, joint preservation, residual and portable rules read. Own original session recovery r1-20261125-1705-own-recovery returned open RESEARCHER session MCP-8cd6c4fa26b9459d923ff73ba0082220, registration r1-20261124-0256-r284gd-session-v1 SUCCEEDED, managed custody not revoked. RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E. Recovery is metadata, not claim. Current LEASED inventory r1-20261125-1705-owner-inventory-read was RUNNING at last observation before writing; no assertion of empty inventory. No shared CLAIM or Task/Result state mutation.

## Theorem

Reuse HQ/HR definitions: M_n(k)=(k+1)/(n+1) binom(2n+2,n-k) on 0<=k<=n and zero otherwise; C_g=sum_k M_n(k)M_m(g-k); A_g=C_g/[M_n(0)M_m(0)binom(g+3,3)], r_g=A_(g+1)/A_g. Put t=min(n,m), rho=max(n,m)/t in [1,2], h=t^(-1/2), lambda=g h. For each fixed 0<a<b<infinity, uniformly over rho in [1,2] and lambda in [a,b],
    t(r_g-r_(g+1)) = - (log Z_rho)''(lambda) + O_(a,b)(t^(-1/2)),
    Z_rho(lambda)=6 integral_0^1 s(1-s) exp[-lambda^2 c(s)] ds,
    c(s)=s^2+(1-s)^2/rho.
For every rho in [1,2] and every lambda>=0, the limiting curvature is bounded below by 23/150 (in particular >3/20). Hence on each such compact critical window the discrete curvature exceeds 1/(8t) for sufficiently large t. Combining frozen HQ's small-deficit and HR's moderate-deficit theorems, there exists t0 such that for all t>=t0, rho in [1,2], 0<=g<=t/2,
    r_g-r_(g+1)>1/(200t).
This closes the asymptotic scale gap for the balanced-port curvature, not the finite effective onset, g>t/2, or the mixed full K ratio. No numerical value of t0 is claimed.

## Proof of limiting curvature bound

Complete the square: c(s)=c0+A(s-s0)^2, c0=1/(1+rho), A=1+1/rho, s0=1/(1+rho). Then c0>=1/3, A<=2 and s0 in [1/3,1/2]. Write z=s-s0, Q=A z^2 and use expectation under the positive joint density proportional to s(1-s) exp[-lambda^2 Q]. The exact differentiation identity is
    (log Z)''=-2c0-2 E Q+4 lambda^2 Var(Q).
The variance is a retained joint-distribution contribution, not independent-port replacement.

Lemma (one-dimensional variance payment). For this density p=e^(-V)/normalizer and smooth f on [0,1],
    Var(f)<= E[(f')^2/V''],  V''=2A lambda^2+1/s^2+1/(1-s)^2>=2A lambda^2+8.
For completeness, define u(s)=p(s)^(-1) integral_0^s (f-E f)p. Since p vanishes linearly at both endpoints and the numerator has total integral zero, u=O(s) and O(1-s) at the respective endpoints; u' is bounded there. Thus u'-V'u=f-E f. Integration by parts gives E[(u'-V'u)^2]=E[(u')^2+V''u^2] and Var(f)=-E[f'u]. Cauchy-Schwarz with V'' then proves the lemma, with the zero variance case immediate. All endpoint terms vanish (including V'p u^2). Apply it to Q to get
    4 lambda^2 Var(Q) <= 8 [2A lambda^2/(2A lambda^2+8)] E Q.
Also E Q decreases with lambda^2, because its derivative is -Var(Q). At lambda=0, direct beta(2,2) moments give E Q=(3/10)(1+1/rho)-1/(1+rho)<=7/60. The final inequality is equivalent to 11rho^2-31rho+18<=0, true on [1,2].
For lambda^2<=8 the bracket is <=4/5; hence (log Z)''<=-2/3+(22/5)(7/60)=-23/150.

For lambda>0 an additional exact integration by parts gives
    2 lambda^2 E Q = 1+E[z (1-2s)/(s(1-s))].
The product inside the expectation is positive only between s0 and 1/2. There |z|<=1/6 and |(1-2s)/(s(1-s))|<=3/2, so it is pointwise <=1/4 everywhere. Therefore E Q<=5/(8 lambda^2).
For lambda^2>=8 the variance lemma gives (log Z)''<=-2/3+6 E Q<=-2/3+30/64=-19/96. This proves the asserted uniform positive limiting curvature. It also gives a reusable local variance payment avoiding full support range bounds.

## Controlled discrete-to-continuous comparison

Use the exact joint port weight (k+1)(g-k+1) w_n(k)w_m(g-k), where w_n(k)=product_{i=0}^{k-1}(n-i)/(n+i+3). Here we can exchange n,m and take n=t,m=rho t. For alpha in [1,2], x=k h in a fixed bounded interval, expand each log(1-i/(alpha t))-log(1+(i+3)/(alpha t)) through cubic order. Since k=O(1/h), the sum of fourth-order remainders is uniformly O(h^3). The finite sums of powers yield
    log w_(alpha t)(k)=-x^2/alpha-2xh/alpha
       +h^2[3x^2/(2alpha^2)-x^4/(6alpha^3)] + O(h^3).
This includes k=0 and the endpoints. The quadratic log term sums (3i+9/2)/(alpha^2 t^2); the leading cubic term sums -2i^3/(3alpha^3 t^3). Terms omitted from these finite sums are O(h^3). This expansion is for the auxiliary count observer, not a native physical propagator.

For y=lambda-x, put B0=exp(-x^2-y^2/rho), U=-2x-2y/rho, V=3x^2/2-x^4/6+3y^2/(2rho^2)-y^4/(6rho^3). Then
    w_t(k)w_(rho t)(g-k)= B0[1+hU+h^2(V+U^2/2)+O(h^3)].
Multiply by (x+h)(y+h), and call the coefficient functions F0,F1,F2. Each is smooth jointly in x,lambda,rho, and all needed derivatives are bounded on the compact window. Exactly,
    A_g = [h sum_(k=0)^g (x+h)(y+h) w_t(k)w_(rho t)(g-k)] /
          [(lambda+h)(lambda+2h)(lambda+3h)/6].
Apply the endpoint-including trapezoidal Euler-Maclaurin expansion to F0 through h^2, to F1 through h, and to F2 at integral order. For smooth bounded derivatives on these compact sets, the summed remainder is O(h^3); explicitly the F0 corrections are h(F0(0)+F0(lambda))/2 and h^2(F0'(lambda)-F0'(0))/12, where primes here differentiate x at fixed lambda. The F1 endpoint correction and F2 integral likewise are smooth functions of (lambda,rho). The denominator has positive leading term lambda^3/6 on the compact window. Thus
    A_g=Z_rho(lambda)+h P1(lambda,rho)+h^2 P2(lambda,rho)+O_(a,b)(h^3),
with smooth P1,P2. The leading term follows by x=lambda s. Uniform positive minimum of Z on the compact set permits taking logs:
    log A_g=log Z_rho(lambda)+h L1(lambda,rho)+h^2 L2(lambda,rho)+O_(a,b)(h^3),
where L1,L2 are smooth and their needed derivatives uniformly bounded. The same expansion holds at g+1,g+2 by enlarging the compact window. Second forward difference of log A_g is h^2(log Z)''+O(h^3): the h L1 term contributes O(h^3), the h^2 L2 term O(h^4), and the remaining three errors are O(h^3) even without differentiability. Also r_g=1+O(h). Since r_(g+1)/r_g=exp(second forward difference), the claimed discrete limit follows. This explicitly pays the errors after the two-step operation, rather than using independent first-order endpoint bounds.

Finally take compact window [1/8,257]. If g<sqrt(t)/8 and t>=256, HQ applies since g+2<=sqrt(t)/4. If g>256sqrt(t) and g<=t/2, HR applies with >1/(64t). The compact window covers the rest once its asymptotic threshold is met. The three strict bounds yield the final all-scale eventual result on 0<=g<=t/2.

## Executed finite evidence

Python exact arbitrary-size integers and Fraction; no floating-point decision. Sample 81 exact curvature comparisons across t=64,256,1024,4096, m=t,3t/2,2t, g=floor(lambda sqrt(t)) for lambda=1/8,1/4,1/2,1,2,4,8 and g<=t/2. These are samples, not exhaustive proof of the continuum inequality or effective onset.

```python
from math import comb,isqrt
from fractions import Fraction as F
from functools import lru_cache
@lru_cache(None)
def ports(n,g):
    a=[comb(2*n+2,n)//(n+1)]
    for k in range(g):
        if k>=n: a.append(0); continue
        z,r=divmod(a[-1]*(k+2)*(n-k),(k+1)*(n+k+3)); assert r==0
        a.append(z)
    return a
def check(t,m,g):
    a,b=ports(t,g+2),ports(m,g+2)
    c=[sum(a[k]*b[j-k] for k in range(j+1)) for j in (g,g+1,g+2)]
    r=F(c[1]*(g+1),c[0]*(g+4)); rn=F(c[2]*(g+2),c[1]*(g+5))
    return t*(r-rn)
rows=[]
for t in (64,256,1024,4096):
    for m in (t,3*t//2,2*t):
        for l in (F(1,8),F(1,4),F(1,2),F(1),F(2),F(4),F(8)):
            g=int(l*isqrt(t))
            if g>t//2: continue
            v=check(t,m,g); assert v>F(3,20)
            rows.append((t,m,g,v))
print('exact cases',len(rows))
print('min scaled',min(float(r[3]) for r in rows))
print('minimum at',[(t,m,g) for t,m,g,v in rows if v==min(x[3] for x in rows)])
print('selected t=4096,m=8192:',[(g,round(float(v),9)) for t,m,g,v in rows if t==4096 and m==8192])
assert F(2,3)-F(22,5)*F(7,60)==F(23,150)>F(3,20)
assert F(2,3)-6*F(5,64)==F(19,96)>F(3,20)
print('analytic margins',F(23,150),F(19,96))
```
Actual output:
```
exact cases 81
min scaled 0.4416647747223739
minimum at [(64, 128, 32)]
selected t=4096,m=8192: [(8, 0.894259077), (16, 0.886213516), (32, 0.860957576), (64, 0.785640978), (128, 0.647923581), (256, 0.607004049), (512, 0.600735441)]
analytic margins 23/150 19/96
```

## Next

The small, critical and moderate scales for balanced-port curvature are now analytically connected for sufficiently large t. Seek a direct discrete analogue of the variance payment, or extend the local concentration bound to g>t/2 and to the exact shifted port ratios in full K. Effective finite onset and the full K propagation remain open. Do not repeat critical asymptotics or previous full K eventual coverage. Independent review and strict activity observation audit remain outstanding.
