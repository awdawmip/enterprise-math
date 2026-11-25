# R284HX — Parabolic baseline certificate and logarithmic-deficit residual payment

2026-11-25. Author proof, NOT_REVIEWED. Auxiliary binary-tag safe-word total-count observer, same scope as R284HW; no native physical attribution. Frozen scientific source: awdawmip/enterprise-math@8c3bad026fc69c3a685218fc4677433a48310256:research_notes/portable_direct/R284HW_UNIFORM_WEDGE_RESIDUAL_PAYMENT_20261125.md and HT@d9a5329739c288770a164382c7b8b1992d886c65:research_notes/portable_direct/R284HT_TERMINAL_PORT_EXACT_REDUCTION_20261125.md. HW/HU exact K reduction and HT signed extension reused without changing their scientific pins. Global main entry blobs verified together at 9ceb05fcf1c89be43302f996708069266ad5da31. Current portable/continuation, research method, P000 V5, ACTIVE worldview and joint preservation read. Own original registration and open session verified by recovery r1-20261125-2155-own-recovery, RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E. Recovery is metadata, not shared CLAIM authority. Owner inventory r1-20261125-2155-owner-read SUCCEEDED, as_of 2026-11-25T13:57:23.234657Z, Source 422fb1f6e3d95e7b3675edcf9c749bc51156d737, LEASED filter returned no tasks. No shared CLAIM or Result mutation.

## Results

Let d=u-q. For real q>=0, d>=30, d^2>=16q, both rational baseline ratios K0(q,u+1)/K0(q,u) and K0(q,u)/K0(q+1,u) exceed 1+1/[4(u+1)]. Here K0 is the explicitly defined rational function below. For the true integer count indicator K, if u>=64, 0<=q<u and

d^2 >= 100 u ln(u+1),

then both true ratios exceed 1+1/[8(u+1)]. All comparisons are valid since d>=30. This provides an explicit sublinear boundary, complementing the linear HW wedge and the prior eventual scale results; it is not full integer-domain closure.

## Proof 1 — exact two-variable parabolic coefficient certificate

Use M_n(k)=(k+1)/(n+1) binom(2n+2,n-k) for 0<=k<=n, zero otherwise; C_ab(g)=sum_k M_a(k)M_b(g-k). At a location (U,Qp), let m=U+Qp, h=U-Qp; Q=C_(U,m)(h-1), V=C_(U,m)(h), A=C_(U-1,m)(h)+C_(U-1,m)(h-1), E=M_(m-1)(0)[M_(U-1)(h)+M_(U-1)(h+1)]. K=(A+E)Q(3U+Qp+1)^2/[(Q+V+Qp A)^2(U+2Qp+1)].

HT: R_ab(g)=binom(S,j) f(S,g), S=2(a+b+2), j=a+b-g, f(S,g)=[4(g+2)^2-S]/[S(S-1)]. C=R+nonnegative truncated signed mass. Define K0 replacing Q,V,A by corresponding R counts and E by zero. In the rational function use S=4u+2q+4, j=u+2q+1, Q0=f(S,d-1), V0=j/(S-j+1)f(S,d), A0=j(j-1)/[S(S-1)]f(S-2,d)+j(S-j)/[S(S-1)]f(S-2,d-1). The shared binomial cancels in K0=A0 Q0 (3u+q+1)^2/[(Q0+V0+q A0)^2(u+2q+1)]. These rational baseline factors are positive in the claimed parabolic region and at the two neighbor points: the largest S is <=6q+4d+8 <=(3/8)d^2+4d+8 <4d^2 for d>=30, and every g+2>=d. Other factors are positive.

Write each H=K0(next)/K0(current)-1 in the desired orientation as N/D in the exact reduced rational form from the script (omit uses current/next). For p=D and p=4(u+1)N-D, express p(q+d,q)=sum a_ij q^i d^j with L=degree_q p. Substitute d=30+x, q=d^2 z/[16(1+z)], x,z>=0. Multiplication by [16(1+z)]^L yields the polynomial

sum a_ij 16^(L-i) z^i (1+z)^(L-i) (30+x)^(j+2i).

All nonzero coefficients are positive, including the constant and the x^0 z^L coefficient, by the exact finite integer expansion below. Thus p>0 for d>=30 and 0<=q<d^2/16; at q=d^2/16 the z^L coefficient is exactly 16^L p(q+d,q), a polynomial in x with nonnegative coefficients and positive constant, establishing the closed boundary as well. This certificate uses neither sampled parameter signs nor floating point. It proves the claimed baseline margin.

## Proof 2 — pay the actual joint residual through the square-root-logarithmic band

Assume u>=64 and d^2>=100u ln(u+1). In particular d>=30, d^2>=16q, d^2>=7u. For each of (U,Qp)=(u,q),(u+1,q),(u,q+1), consider the four convolution terms entering Q,V,A. In each term g+2>=d, S<=7u, j<=3u+1<=25u/8. Both class sizes 2N,2M (N=a+1, M=b+1) in HT satisfy min(N,M)/(N+M)>=u/(3u+3)>=3/10. The signed count is positive and f(S,g)>=3d^2/(49u^2)>d^2/(17u^2).

The HT joint hypergeometric signed extension uses v=(1-J/N)(1-(j-J)/M); omitted nonzero terms have one negative factor and absolute weight <=1, and the signed mass is retained as C-R. The distance of either class mean to its zero layer is at least (3/10)(g+2)>=(3/10)d. For a hypergeometric sample count X with sample size j, HT proves Pr(X-EX>=b)<=exp(-2b^2/j) by the factorial-moment bound E(1+z)^X <=(1+p z)^j for z>=0 and the centered Bernoulli mgf estimate. For b>=d/4, this is <=exp(-d^2/(25u)); if j=0 the tail is zero. Hence 0<=C/R-1<=34u^2/d^2 exp(-d^2/(25u)).

For the separate E: if h>U-1, E=0. Otherwise M_(U-1)(h+1)<=M_(U-1)(h), since the port ratio is (k+2)(U-1-k)/[(k+1)(U-1+k+3)] and 2k^2+6k+3>U-1 at k=h>=d-1 (using d^2>=7u). Also M_(m-1)(0)<=M_m(0) by the Catalan consecutive ratio. Therefore E<=2 M_(U-1)(h) M_m(0). In C_(U-1,m)(h) the boundary branch has second-class sample count M-1. Its distance above the mean is at least (3/10)d-1>=d/4. Each signed factor on this valid branch is in [0,1]. Its weight is at most binom(S,j) times the same tail, and the signed count R_(U-1,m)(h) is a positive summand of the signed A. Consequently E/A_signed<=34u^2/d^2 exp(-d^2/(25u)).

Put delta=34u^2/d^2 exp(-d^2/(25u)). This bound is common to the three locations, so their true-to-baseline K ratios lie between (1+delta)^(-2) and (1+2delta)(1+delta) by HW (the same positive A appears in numerator and denominator, and E is retained as a paid correction). The hypothesis implies delta<=34u/(u+1)^4<1/[100(u+1)] because (u+1)^3>3400u for u>=64. The latter holds at 64 and the ratio (u+1)^3/u increases. For delta<=0.1, (1+delta)^3(1+2delta)<=1+6delta. The true ratios thus exceed (1+1/[4(u+1)])/(1+6/[100(u+1)])>1+1/[8(u+1)] by positive cross multiplication. This proves the theorem. More generally the same payment works wherever d>=30, u>=64, d^2>=16q, d^2>=7u and the explicit delta<1/[100(u+1)]. No residual deletion for other observers is asserted.

## Executed exact replay

Python/SymPy with exact integers and fractions. Decimal output only for display. The dictionary expansion computes the four full transformed polynomials; the endpoint condition is checked independently at x=0. Sample selection uses the exact sufficient condition d^2>=70u*bit_length(u+1), since ln2<7/10 by the positive exponential series. All actual signs, residual sandwiches and reference comparisons are exact. Script:

```python
from math import comb,isqrt
from fractions import Fraction as F
from functools import lru_cache
import sympy as s
u,q,d,x,z=s.symbols('u q d x z'); S=4*u+2*q+4; j=u+2*q+1; dd=u-q
f=lambda S,g:(4*(g+2)**2-S)/(S*(S-1))
Q=f(S,dd-1);V=j/(S-j+1)*f(S,dd);A=j*(j-1)/(S*(S-1))*f(S-2,dd)+j*(S-j)/(S*(S-1))*f(S-2,dd-1)
K=s.factor(A*Q*(3*u+q+1)**2/((Q+V+q*A)**2*(u+2*q+1)))
C0=16; shift=30; count=0
for name,a,b in [('read',K.subs(u,u+1),K),('omit',K,K.subs(q,q+1))]:
 N,D=s.fraction(s.factor(a/b-1))
 for label,e in [('D',D),('margin',4*(u+1)*N-D)]:
  p=s.Poly(e.subs(u,q+d),q,d); L=p.degree(q); co={}
  for (i,j),a in p.terms():
   for k in range(L-i+1):
    key=(i+k,j+2*i);co[key]=co.get(key,0)+int(a)*C0**(L-i)*comb(L-i,k)
  out={}
  for (i,j),a in co.items():
   for k in range(j+1):
    key=(i,k);out[key]=out.get(key,0)+a*comb(j,k)*shift**(j-k)
  vs=[a for a in out.values() if a]
  assert min(vs)>0 and out[(0,0)]>0 and out[(L,0)]>0
  assert s.expand(e.subs({u:F(30)+F(900,16),q:F(900,16)}))>0
  count+=len(vs)
  print(name,label,'L',L,'terms',len(vs),'min',min(vs),'endpoint_constant',out[(L,0)],flush=True)
print('total positive coefficients',count,flush=True)
assert F(1)+F(7,10)+F(7,10)**2/2+F(7,10)**3/6>2
@lru_cache(maxsize=12)
def ports(n):
 a=[comb(2*n+2,n)//(n+1)]
 for k in range(n):
  v,r=divmod(a[-1]*(k+2)*(n-k),(k+1)*(n+k+3));assert r==0;a.append(v)
 return a
def C(n,m,g):
 a,b=ports(n),ports(m)
 return sum(a[k]*b[g-k] for k in range(max(0,g-m),min(n,g)+1))
def R(n,m,g):
 S=2*(n+m+2); j=n+m-g
 return F(comb(S,j)*(4*(g+2)**2-S),S*(S-1))
def pair(U,Qp,base_u):
 m=U+Qp;d=U-Qp
 a,b=C(U,m,d-1),C(U,m,d); c=C(U-1,m,d)+C(U-1,m,d-1)
 aa,bb=R(U,m,d-1),R(U,m,d);cc=R(U-1,m,d)+R(U-1,m,d-1)
 E=ports(m-1)[0]*sum(ports(U-1)[k] for k in (d,d+1) if k<U)
 h=F(1,100*(base_u+1))
 assert all(0<=v/w-1<h for v,w in ((a,aa),(b,bb),(c,cc))) and 0<=E/cc<h
 fac=F((3*U+Qp+1)**2,U+2*Qp+1)
 true=fac*F((c+E)*a,(a+b+Qp*c)**2); ref=fac*cc*aa/(aa+bb+Qp*cc)**2
 assert ref==F(str(K.subs({u:U,q:Qp})))
 assert (1+h)**-2<=true/ref<=(1+2*h)*(1+h)
 return true,ref
count=0; new=0; mn=None
for U in (1024,2048,4096,8192):
 D0=1+isqrt(70*U*(U+1).bit_length())
 for D in sorted({D0, (D0+U)//2, U}):
  if D>U:continue
  assert D*D>=70*U*(U+1).bit_length()
  Qp=U-D
  a,a0=pair(U,Qp,U);b,b0=pair(U+1,Qp,U);c,c0=pair(U,Qp+1,U)
  assert b0/a0-1>F(1,4*(U+1)) and a0/c0-1>F(1,4*(U+1))
  assert b/a-1>F(1,8*(U+1)) and a/c-1>F(1,8*(U+1))
  v=min(b/a-1,a/c-1)*(U+1);mn=v if mn is None else min(v,mn)
  count+=2;new+=2*(U<2*Qp+10)
  print('sample',U,Qp,D,'scaled gaps',float((b/a-1)*(U+1)),float((a/c-1)*(U+1)),flush=True)
print('comparisons',count,'outside HW',new,'min',float(mn),flush=True)
```

Actual output summary: read D L=15, 427 terms, min 24749176752; read margin L=15, 427 terms, min 131985799920; omit D L=13, 330 terms, min 2749908528; omit margin L=13, 332 terms, min 25664722992. Total 1516 positive coefficients, all endpoint constants positive. 24 exact true/baseline neighbor comparisons, 4 outside HW; all assertions passed. Minimum observed scaled true gap 1.0000813812438833 at u=8192,q=0. Near new sample boundary:
|u|q|d|scaled read gap|scaled omit gap|
|--:|--:|--:|--:|--:|
|1024|136|888|1.2696367024|16.6522460333|
|2048|736|1312|1.4706964075|6.8483325018|
|4096|2165|1931|1.5202553321|4.7619021740|
|8192|5358|2834|1.5301677629|3.8662620325|
Finite samples support the actual scope only; proof is the coefficient certificate plus residual inequality.

## Next

The parabolic baseline certificate already reaches d>=4 sqrt(q) with d>=30. The bottleneck is the independent absolute tail payment in the critical strip, not polynomial sign complexity. Seek signed relative *adjacent* tail transmission (rather than separately paying entire residual at each point), exploiting HP exact coupling and HU shared A, to replace the logarithmic gap by an effective constant multiple of sqrt(u). The small fixed-deficit and finite middle regions retain their existing separate status. Independent mathematical review and strict Activity observation audit pending.
