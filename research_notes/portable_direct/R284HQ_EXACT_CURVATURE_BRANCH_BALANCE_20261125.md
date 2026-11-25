# R284HQ — Exact two-step joint curvature balance, half-size uniform bound and signed band

2026-11-25. Author proof and exact calculation, NOT_REVIEWED. Auxiliary binary-tag safe-word total-count observer only; no native physical attribution or P000 change. Frozen dependency: 3a29820d72c053c4a5a71e303244ce747a08be38:research_notes/portable_direct/R284HP_EXACT_TILTED_PORT_COUPLING_20261125.md (exact tilted coupling); ee8f08bb614ff06cb63f6e2567d14ead674e42ff:research_notes/portable_direct/R284HM_SUBCRITICAL_POLYA_PORT_TRANSPORT_20261125.md (Pólya transport and K identity); 35dc10f164c6a93ea5d65c4b5285304188fae549:research_notes/portable_direct/R284HO_EXACT_FIXED_DEFICIT_POLYNOMIAL_STRIPS_20261125.md. Current account entries verified at 5bd13fb99f2ad27ae1f15c56a5b5927286e0c7d0; project entry blobs verified at 8951962a0ccdd09b9a8f8d83aea518149140443e. P000 Source V5, ACTIVE worldview and joint preservation/residual contracts read. Own session recovery: original registration r1-20261124-0256-r284gd-session-v1 SUCCEEDED, role RESEARCHER, session open, managed custody not revoked; recovery is metadata only, not CLAIM or execution authorization. Own RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E. New LEASED inventory r1-20261125-1504-owner-inventory-read observed QUEUED with EVENT_READ_CONTROL_BUSY / CURRENT_CONTROL_FOLLOW_RETRY; no assertion of empty owner inventory. Continue only the existing independent line; no shared claim, Task state or Result mutation.

## Definitions and theorem

For nonnegative n,m, let M_n(k)=(k+1)/(n+1) binom(2n+2,n-k) on 0<=k<=n, zero elsewhere. C_g=sum_k M_n(k)M_m(g-k), c_g=binom(g+3,3), A_g=C_g/[M_n(0)M_m(0)c_g], r_g=A_(g+1)/A_g (r_(n+m)=0). Define mu_g(k)=M_n(k)M_m(g-k)/C_g on its positive support. All comparisons below have 0<=g<n+m, t=min(n,m), T=max(n,m).

1. **Improved uniform curvature payment:** |r_g-r_(g+1)| < 2/(t+3), halving HP's constant 4, over the whole original support, including capacity boundaries.
2. **Exact signed branch balance:** on mu_g put l=g-k, p=(k+2)/(g+4), x=rho_n(k), y=rho_m(l), rho_z(j)=(z-j)/(z+j+3) for 0<=j<=z and zero beyond support. Write X=p x+(1-p)y, delta_x=x-rho_n(k+1), delta_y=y-rho_m(l+1). Then
   r_g(r_g-r_(g+1)) = D - Var_mu_g(X) - J,
   D=E_mu_g[p (k+3)/(g+5) x delta_x+(1-p)(l+3)/(g+5) y delta_y],
   J=E_mu_g[p(1-p)(x-y)^2/(g+5)].
   D,J and the variance are nonnegative. This is an exact two-step identity, not an absolute approximation.
3. **Effective positive curvature band:** for t>0, T<=2t and 16(g+2)^2<=t, r_g-r_(g+1)>1/(200t). More generally, when g<t let L=(t-g)/(t+g+3), H=T/(T+3), delta=(2t+3)/[(T+g+3)(T+g+4)]. Then
   r_g(r_g-r_(g+1)) >= L delta/2 - (1+1/(g+5))(H-L)^2/4.
   Positive RHS suffices for strict decrease.
4. **Unrestricted sign is false:** at n=0, m>=10, g=0, r_1>r_0; at n=1 the same strict reversal holds exactly for m>=81 (m>=0 and g=0 valid). Thus an unrestricted relative log-concavity assumption on A_g cannot replace the joint payment. The capacity ratios in K's unshifted ports are balanced; these counterexamples are to a general port lemma, not counterexamples to K monotonicity.

## Proof

(1) Use frozen HP's exact coupling: a draw (k,l) from mu_g and (k',l') from mu_(g+1) can be coupled so exactly one coordinate grows by one. Let b_z(j)=1-rho_z(j) and a=p b_n(k)+(1-p)b_m(l); the HM identity gives r_g=1-E a. For a step growing k, write p'=(k+3)/(g+5). Then p'-p=(1-p')/(g+4) and
   a'-a=p'[b_n(k+1)-b_n(k)]+(p'-p)[b_n(k)-b_m(l)].
The step is allowed only when k<n, so 0<b_n(k+1)-b_n(k)=(2n+3)/[(n+k+3)(n+k+4)]<2/(n+3). Also b_z(j)<=(2j+3)/(z+3). Hence
   a'-a < [2p'+(1-p')(2k+3)/(g+4)]/(n+3) < 2/(n+3),
   a'-a >= -(1-p')(2l+3)/[(g+4)(m+3)] > -2/(m+3).
Swap the two ports for the other step. Taking expectation preserves strict bounds since the finite support carries positive mass. This establishes the constant 2 without requiring a scale restriction or absolute endpoint payment.

(2) The Pólya step under mu_g before acceptance chooses k-growth with p and l-growth with 1-p. Along two consecutive steps the branch acceptance weights multiply (zero means the path hits a capacity boundary). The expectation of the product under the unweighted two-step transition after mu_g is A_(g+2)/A_g=r_g r_(g+1); this follows from the same Pólya reweighting as HM or by summing the ordered word weights. The two same-color probabilities are p(k+3)/(g+5)=p²+p(1-p)/(g+5) and (1-p)(l+3)/(g+5)=(1-p)²+p(1-p)/(g+5); the total probability of the two mixed orders is 2p(1-p)(g+4)/(g+5). The conditional expectation of the product therefore equals
   p(k+3)/(g+5) x(x-delta_x)+(1-p)(l+3)/(g+5) y(y-delta_y)+2p(1-p)(g+4)/(g+5) xy
   = X²+p(1-p)(x-y)²/(g+5) - [p(k+3)/(g+5)x delta_x+(1-p)(l+3)/(g+5)y delta_y].
At a saturated port x=0 or y=0, the corresponding factor makes the same-color term zero, and the beyond-support convention is consistent. Taking expectation and using r_g=E X gives the claimed exact identity. No independence of the two coordinates, deletion of joint support or signed cancellation of raw positive branch mass is assumed. D is the expected loss from repeated use of a port, the variance pays the heterogeneity of current joint allocation, J pays the reinforcement correlation of the two steps.

(3) If g<t, every x,y lies in [L,H]; every delta_x,delta_y is >=delta by the exact one-step formula. The two same-color probabilities sum to p²+(1-p)²+2p(1-p)/(g+5)>=1/2. Thus D>=L delta/2. Since X lies in [L,H], Var(X)<=(H-L)^2/4 (from E[(X-L)(H-X)]>=0 and completing the square). Since p(1-p)<=1/4, J<=(H-L)^2/[4(g+5)]. This proves the rational sign criterion.

For the simpler effective band t>=16(g+2)^2 implies t>=64, g<=t/4, and T<=2t. Then L>=1/2, and T+g+4<=5t/2; delta>8/(25t). Consequently D>2/(25t). Also H-L <=1-L=(2g+3)/(t+g+3)<(2g+3)/(t+3), and (2g+3)^2<t/4. So Var(X)+J < (6/5)(t/4)/(4t²)=3/(40t). Subtracting proves r_g(r_g-r_(g+1))>1/(200t); 0<r_g<=1 gives part 3. This is an explicit sign on a growing portion of the subcritical band, for the auxiliary port observer, not a proof of global K monotonicity.

(4) At g=0, let a=n/(n+3), b=m/(m+3), c=n(n-1)/[(n+3)(n+4)], e=m(m-1)/[(m+3)(m+4)]. Directly r_0=(a+b)/2, r_1=(3c+4ab+3e)/[5(a+b)] for n+m>0. When n=0 and m>=1, r_0=m/[2(m+3)], r_1=3(m-1)/[5(m+4)]. Thus r_1>r_0 iff m²-8m-18>0, exactly m>=10. At n=0,m=10 the signed curvature is -1/910. For n=1,
   r_0-r_1=-3(m³-78m²-183m-60)/[40(m+3)(m+4)(5m+3)].
For 0<=m<=78 the numerator cubic is negative, and its values at 79,80 are negative. Writing m=81+j, j>=0, the cubic is j³+165j²+6864j+4800>0. This gives the exact threshold 81 and the witness n=1,m=81: r_0=17/28, r_1=351/578, difference -1/8092. The counterexample has both ports positive-capacity.

## Executed evidence (Python 3, exact integers and rational fractions)

The following reproduces the complete 15,000 identity/absolute-bound checks, the sign counterexamples, and 54 signed-band sample checks. Finite checks do not prove the unbounded results; proofs above do.

```python
from math import comb,isqrt
from fractions import Fraction as F
from functools import lru_cache
@lru_cache(None)
def M(n):
    return [(k+1)*comb(2*n+2,n-k)//(n+1) for k in range(n+1)]
def C(n,m,g):
    if g<0:return 0
    a,b=M(n),M(m)
    return sum(a[k]*b[g-k] for k in range(max(0,g-m),min(n,g)+1))
def r(n,m,g):
    return F(C(n,m,g+1)*(g+1),C(n,m,g)*(g+4))
def rho(n,k):return F(n-k,n+k+3) if k<=n else F(0)
def check(n,m,g):
    a,b=M(n),M(m); Z=C(n,m,g); rr=r(n,m,g); rn=r(n,m,g+1)
    E=E2=D=J=F(0)
    for k in range(max(0,g-m),min(n,g)+1):
        l=g-k; w=F(a[k]*b[l],Z);p=F(k+2,g+4)
        x,y=rho(n,k),rho(m,l);v=p*x+(1-p)*y
        E+=w*v;E2+=w*v*v
        D+=w*(p*F(k+3,g+5)*x*(x-rho(n,k+1))+(1-p)*F(l+3,g+5)*y*(y-rho(m,l+1)))
        J+=w*p*(1-p)*(x-y)**2/(g+5)
    assert E==rr and rr*(rr-rn)==D-(E2-E*E)-J
    assert abs(rr-rn)<F(2,min(n,m)+3)
    return rr-rn
N=0;neg=0;mx=F(0);witness=None
for n in range(25):
 for m in range(25):
  for g in range(n+m):
   z=check(n,m,g);N+=1;neg+=z<0
   v=(min(n,m)+3)*abs(z)
   if v>mx:mx=v;witness=(n,m,g)
print('identity_and_bound',N,'negative_curvature',neg,'max_scaled',mx,'witness',witness)
for n,m in [(0,10),(1,80),(1,81),(1,100)]:
 print('counterexample_test',n,m,r(n,m,0),r(n,m,1),check(n,m,0))
B=0;minsc=None
for t in [64,100,144,256,400,1024]:
 for m in [t,t+t//2,2*t]:
  for g in range(max(0,isqrt(t)//4-1)):
   assert 16*(g+2)**2<=t
   z=check(t,m,g);assert z>F(1,200*t);B+=1
   minsc=min(t*z,minsc) if minsc is not None else t*z
print('positive_band_samples',B,'min_scaled_approx',float(minsc))
```
Actual output:
```
identity_and_bound 15000 negative_curvature 44 max_scaled 153/140 witness (24, 24, 0)
counterexample_test 0 10 5/13 27/70 -1/910
counterexample_test 1 80 403/664 1712/2821 95/1873144
counterexample_test 1 81 17/28 351/578 -1/8092
counterexample_test 1 100 503/824 4010/6539 -15123/5388136
positive_band_samples 54 min_scaled_approx 0.8350621812472121
```

## Next

The exact two-step identity isolates the obstruction: a uniform bound on Var_mu_g(X)+J relative to D is needed in balanced ports beyond the proven small-deficit band. Study variance using the tilted conditional law and its discrete score/curvature; compare directly with D rather than paying independent full residual ranges. The ratio T/t<=2 is relevant to unshifted n=u,m=u+q in K, with shifted ports requiring their own domain checks. HO's all-budget fixed-deficit proof and HN's eventual full-scale K monotonicity remain intact; global K sign still lacks effective closure. Do not repeat the asymptotic coverage or mistake the counterexamples for K counterexamples. Independent review and strict Activity observation audit remain pending.
