# R284HZ: adjacent boundary payment and effective all-deficit onset

2026-11-26; author proof, NOT_REVIEWED. Auxiliary binary-tag safe-word total-count observer, not native physical attribution. Frozen sources: HY@0164790b93645d9e15c65baa4d77260fcaa8e1c9 (R284HY_CAPACITY_COUPLING_AND_SQRT_DOMAIN_20261125.md), HQ@b0572296445fe5355dd4807ac4d6073fe69e8144 (R284HQ_EXACT_CURVATURE_BRANCH_BALANCE_20261125.md), HO@35dc10f164c6a93ea5d65c4b5285304188fae549 (R284HO_EXACT_FIXED_DEFICIT_POLYNOMIAL_STRIPS_20261125.md), all in research_notes/portable_direct/. Global entry blobs verified at main b0e74257cef73da1ae1f61e687a5520a6a56f109; current EM continuation, portable, method, P000 V5, Heartbeat, joint preservation, residual fidelity and ACTIVE worldview read. Own session MCP-8cd6c4fa26b9459d923ff73ba0082220 recovery confirms original registration SUCCEEDED, open RESEARCHER, RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E. LEASED inventory r1-20261126-0000-owner-read SUCCEEDED, as_of 2026-11-25T16:01:23.394789Z, Source 9ecbd97e2c2163a1b0f469615bc07e3d587706c5, tasks=[], cursor null. No shared CLAIM/Result or P000 mutation.

**Theorem.** For all integers u>=4,410,000, 0<=q<u, K(q,u+1)>K(q,u), and K(q,u)>K(q+1,u) when q+1<u. For d=u-q>=16 both valid ratios exceed 1+1/[8(u+1)]; in the direct band 16<=d<=u/100 they exceed 1+1/[4(u+1)]. For d<16 use HO's strict sign only. This replaces unknown effective onset with a finite complement; it does not prove that complement.

## Exact adjacent boundary payment

Set h=d, a=u-1, m=u+q. Let M_z(k)=(k+1)/(z+1) binom(2z+2,z-k), zero outside 0<=k<=z. w_z(k)=M_z(k)/M_z(0)=(k+1) prod_{i<k}(z-i)/(z+i+3), gamma_z=M_(z-1)(0)/M_z(0)=(z+2)/(4z+2). Put T_j=sum_k w_a(k)w_m(j-k), D_h=T_h+T_(h-1). HY's exact boundary e=E/A=gamma_m[w_a(h)+w_a(h+1)]/D_h. Denote e_R=e(q,u+1), e_O=e(q+1,u). For u>=4410000, 16<=h<=u/100, prove
0<=e<2/h^2; e-e_R<=P; e_O-e<=P, where P=8/h^3+6/(uh).

Write rho_z(i)=(z-i)/(z+i+3). As a<=m and rho decreases in i and increases in z, prod_{i=h-j}^{h-1}rho_a(i)<=prod_{i=0}^{j-1}rho_m(i) for 0<=j<=h. Hence w_a(h-j)w_m(j)/w_a(h)>=(h-j+1)(j+1)/(h+1). Sum actual joint branches: T_h>=w_a(h)(h+2)(h+3)/6. HQ's positive Polya transport yields normalized ratio r_g<=1 (expectation of a convex combination of rho factors), so T_h/T_(h-1)<=(h+3)/h and D_h>=(9/5)T_h for h>=16. Also gamma_m<=4/15 and w_a(h+1)/w_a(h)<=(h+2)/(h+1)<=5/4. The numerator <=(3/5)w_a(h). Thus e<=2/[(h+2)(h+3)]<2/h^2.

Read step h->h+1 then a,m each +1: numerator's two-weight ratio before expansion >= minimum of consecutive w ratios >=1-(2h+5)/u. Capacity increases normalized w, and gamma_(m+1)/gamma_m=1-3/[(m+2)(2m+3)]>=1-2/u^2. At fixed capacities D_(h+1)/D_h<=1+3/h. The exact capacity factor w_(z+1)(k)/w_z(k)=[1-k(k+2)/((z+1)(z+3))]^-1 applies branchwise. Since a+1=u and k+l<=h+1, the product of both capacity factors <=[1-(h+1)(h+3)/u^2]^-1, by k(k+2)+l(l+2)<=(h+1)(h+3). Therefore
e_R/e >= (1-2/u^2)(1-(2h+5)/u)(1-(h+1)(h+3)/u^2)/(1+3/h).
All factors positive. Using 1/(1+x)>=1-x and the product inequality, e-e_R<=e*[3/h+(2h+5)/u+(h+1)(h+3)/u^2+2/u^2]<=e*(3/h+3h/u), since h>=16, h/u<=1/100 imply (2+5/16)+(1+1/16)(1+3/16)/100+2/(uh)<3. This gives 6/h^3+6/(uh).

Omit step h->h-1, m+1: gamma decreases, denominator increases under m expansion, and numerator ratio at fixed capacities <=[1-(2h+3)/u]^-1 by the two successive w ratio bounds. Also D_h/D_(h-1)<=1+3/(h-1). Thus e_O/e <= (1+3/(h-1))/(1-(2h+3)/u). Its excess over 1 is <=4/h+3h/u: denominator>=1-(2+3/16)/100, and 3h/(h-1)<=16/5. Multiply by e<2/h^2. In both K comparisons the boundary factor >=1-P, namely (1+e_R)/(1+e), (1+e)/(1+e_O). Exact joint branches and nonzero E retained.

## Two complementary surpluses

HY factorization K=L/(1+b)*H_q(alpha)*(1+e), H_q(x)=x/(1+qx)^2, b=C_(u,m)(h)/C_(u,m)(h-1), alpha=A/(Q+V), L=(3u+q+1)^2/(u+2q+1). HY Proof 3's non-e estimates use only u>=4410000, h<=u/100 (not h^2>=441u): L_R/L>1+1/(u+1), L/L_O>1, b_R/b<=1+1/(16u), b_O>=b, alpha>=1/5, alpha_R/alpha<=1+1/(12u), alpha_O>=alpha. Exact capacity coupling gives the last two. Since q>=99u/100, H_q is decreasing, H_q(alpha_R)/H_q(alpha)>=1/(1+1/(12u)), H_q(alpha)/H_(q+1)(alpha_O)>1+1/(u+1).

Case I: 20h^2<=u. Then 16(h+1)^2<=20h^2 for h>=16. HQ's balanced-port positive curvature applies at old and new capacities; b=(h+3)r_(h-1)/h. Read: capacity increments first, then h+1: b_R/b<=(1-3/[(h+1)(h+3)])(1+1/(16u))<=1-2/h^2 because 3h^2/[(h+1)(h+3)]>=768/323>2+1/320. Omit: h-1 then capacity increase, b_O/b>=1+3/[(h-1)(h+3)]>=1+2/h^2. Pólya representation gives b>=r_(h-1)>=(u-h+1)/(u+h+2)>1/2. Both b factors >=1+2/(3h^2). P<9/h^3, and (1+2/(3h^2))(1-P)>1 for h>=16 (2h/3>9+6/h^2). Thus combinatorial curvature pays the full boundary loss, leaving geometric and alpha surplus. Both ratios >1+1/[4(u+1)].

Case II: 20h^2>u. Then h>sqrt(220500)>469, P<166/(uh)<1/(2u). General b/alpha denominator product <=1+1/(6u). Read ratio > (1+1/(u+1))(1-1/(2u))/(1+1/(6u)) >1+1/[4(u+1)]; cross multiplication gives u/12-29/24>0 after common denominator u(u+1). Omit has no unfavorable b/alpha beyond P and satisfies the same bound.

Stitch: if h>u/100, h^2>u^2/10000>=441u, so HY applies. If 16<=h<=u/100 use Cases I/II; if h<16 use HO. Thus explicit onset for all valid deficits. Previous author proof dependencies retain NOT_REVIEWED status.

## Executed exact sample

Use HO's common denominator rather than forming huge binomial counts; exact arithmetic, decimal display only. Executed code:

```python
from fractions import Fraction as F
from math import prod,isqrt
def ports(n,H):
    D=prod(n+i+3 for i in range(H)); a=[D]
    for k in range(H):
        v,r=divmod(a[-1]*(k+2)*(n-k),(k+1)*(n+k+3))
        assert r==0
        a.append(v)
    return a,D
def factors(u,q):
    h=u-q;m=u+q;H=h+1
    p,P=ports(u,H);a,A=ports(u-1,H);b,B=ports(m,H)
    def C(x,y,g):return sum(x[k]*y[g-k] for k in range(g+1))
    Q=C(p,b,h-1);V=C(p,b,h)
    C0=C(a,b,h)+C(a,b,h-1)
    gamma=lambda n:F(n+2,4*n+2)
    e=gamma(m)*F((a[h]+a[h+1])*B,C0)
    alpha=gamma(u)*F(C0*P,(Q+V)*A)
    beta=F(V,Q)
    L=F((3*u+q+1)**2,u+2*q+1)
    K=L*alpha*(1+e)/((1+beta)*(1+q*alpha)**2)
    return e,alpha,beta,K
N=0;maxcost=F(0);minread=None;minomit=None
for u in [4410000,10000000,100000000]:
    z=isqrt(u//20)
    for h in sorted({16,25,64,128,256} if u==100000000 else {16,25,64,128,256,z,z+1,2*z}):
        q=u-h
        e,a,b,K=factors(u,q);er,ar,br,Kr=factors(u+1,q);eo,ao,bo,Ko=factors(u,q+1)
        P=F(8,h**3)+F(6,u*h)
        assert e<F(2,h*h)
        assert e-er<=P and eo-e<=P
        assert (1+er)/(1+e)>=1-P and (1+e)/(1+eo)>=1-P
        assert ar/a<=1+F(1,12*u) and ao>=a and br/b<=1+F(1,16*u) and bo>=b
        if 20*h*h<=u:
            assert br/b<=1-F(2,h*h) and bo/b>=1+F(2,h*h)
            assert min((1+b)/(1+br),(1+bo)/(1+b))>=1+F(2,3*h*h)
        else:
            assert P<F(1,2*u)
        rr=(Kr/K-1)*(u+1);oo=(K/Ko-1)*(u+1)
        assert min(rr,oo)>F(1,4)
        maxcost=max(maxcost,(e-er)/P,(eo-e)/P)
        minread=rr if minread is None else min(minread,rr)
        minomit=oo if minomit is None else min(minomit,oo)
        N+=1
        print(u,h,'small' if 20*h*h<=u else 'large',float(rr),float(oo),float((e-er)/P),float((eo-e)/P),flush=True)
print('cases',N,'comparisons',2*N,'max_fraction_paid',float(maxcost),'min_scaled_read',float(minread),'min_scaled_omit',float(minomit))
```

Completed output summary: cases 21 comparisons 42 max_fraction_paid 0.3704630769686529 min_scaled_read 9.084208045223356 min_scaled_omit 10.09516428770374. All exact assertions passed. Earlier attempts including larger h at u=10^8 timed out and are not counted. The proof, not sampling, establishes the unbounded result.

Next: reduce the explicit onset by enlarging the direct band, tightening payments and exploiting proven HV/HW/HX/HY/HO regions before a finite certificate. Do not repeat unknown-onset proofs. Finite complement below 4,410,000 remains open except already proved regions; no independent review.
