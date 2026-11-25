# R284IA — One-sided capacity payment and explicit onset 32000

2026-11-26. Author proof and exact sample replay; NOT_REVIEWED. Same auxiliary binary-tag safe-word total-count observer as HZ; no native physical attribution. Frozen scientific dependencies (all under research_notes/portable_direct/):
- HZ @ ae1ed992c6adf63e057ddb5c1729a405a654b2e8, R284HZ_ADJACENT_BOUNDARY_PAYMENT_EFFECTIVE_GLOBAL_ONSET_20261126.md
- HY @ 0164790b93645d9e15c65baa4d77260fcaa8e1c9, R284HY_CAPACITY_COUPLING_AND_SQRT_DOMAIN_20261125.md
- HQ @ b0572296445fe5355dd4807ac4d6073fe69e8144, R284HQ_EXACT_CURVATURE_BRANCH_BALANCE_20261125.md
- HP @ 3a29820d72c053c4a5a71e303244ce747a08be38, R284HP_EXACT_TILTED_PORT_COUPLING_20261125.md
- HO @ 35dc10f164c6a93ea5d65c4b5285304188fae549, R284HO_EXACT_FIXED_DEFICIT_POLYNOMIAL_STRIPS_20261125.md

Account main entry blobs matched immutable snapshot a3a0d0675c928ff77c17c81e360dba521c5e78db; current Source continuation entry matched 0a4c92589dca24fd3bb381a3fed3c0f9f291967a. Portable, method, global and Source P000, ACTIVE worldview, residual and BRC foundations read. Own registration recovered (original r1-20261124-0256-r284gd-session-v1 SUCCEEDED, open RESEARCHER, metadata only); RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E. LEASED inventory r1-20261126-0106-owner-read SUCCEEDED, as_of 2026-11-25T17:07:39.036859Z, source 0a4c92589dca24fd3bb381a3fed3c0f9f291967a, tasks=[], cursor null. Independent continuing science, no shared CLAIM or Result mutation.

**Theorem.** For all integers u>=32000 and 0<=q<u, K(q,u+1)>K(q,u); also K(q,u)>K(q+1,u) whenever q+1<u. For h=u-q>=25 both valid ratios exceed 1+1/[8(u+1)]. For h<=24 reuse HO's strict sign. This improves HZ's onset 4410000 by a factor 137.8125. Finite complement not yet closed.

## Exact definitions

M_n(k)=(k+1)/(n+1) binom(2n+2,n-k) on 0<=k<=n, zero elsewhere. C_(n,m)(g)=sum_k M_n(k)M_m(g-k). Put m=u+q, h=u-q, Q=C_(u,m)(h-1), V=C_(u,m)(h), A=C_(u-1,m)(h)+C_(u-1,m)(h-1), E=M_(m-1)(0)[M_(u-1)(h)+M_(u-1)(h+1)]. HY/HZ give b=V/Q, alpha=A/(Q+V), e=E/A, L=(3u+q+1)^2/(u+2q+1), H_q(x)=x/(1+qx)^2 and exact K=L H_q(alpha)(1+e)/(1+b). Subscripts R,O denote (q,u+1),(q+1,u). All observations concern the same true joint populations; E is not deleted.

## 1. Expand HZ boundary payment to h<=u/10

Assume u>=32000 and 25<=h<=u/10. Let a=u-1, w_z(k)=M_z(k)/M_z(0), rho_z(i)=(z-i)/(z+i+3), gamma_z=(z+2)/(4z+2), T_j=sum_k w_a(k)w_m(j-k), D_h=T_h+T_(h-1). Then e=gamma_m[w_a(h)+w_a(h+1)]/D_h.

Reuse HZ's branchwise inequality w_a(h-j)w_m(j)/w_a(h)>=(h-j+1)(j+1)/(h+1), which follows by monotonicity of rho in capacity and index. Summing gives T_h>=w_a(h)(h+2)(h+3)/6. HQ's r<=1 implies T_h/T_(h-1)<=(h+3)/h, hence D_h>=(9/5)T_h for h>=25. gamma_m<=4/15 and w_a(h+1)/w_a(h)<=5/4. Thus 0<e<=2/[(h+2)(h+3)]<2/h^2.

The actual consecutive boundary numerator/denominator inequalities in HZ hold throughout this wider band: the read numerator ratio at fixed capacities >=1-(2h+5)/u; gamma_(m+1)/gamma_m>=1-2/u^2; D_(h+1)/D_h<=1+3/h. Exact normalized capacity factor w_(z+1)(k)/w_z(k)=[1-k(k+2)/((z+1)(z+3))]^-1; the product of both factors at total degree <=h+1 is at most [1-(h+1)(h+3)/u^2]^-1. The numerator normalized weights increase under the capacity shifts. Therefore
e_R/e >= (1-2/u^2)(1-(2h+5)/u)(1-(h+1)(h+3)/u^2)/(1+3/h).
All factors positive. The deficit of the right hand side is <=3/h+3h/u: indeed (2+5/25)+(26/25)(28/25)/10+2/(25*32000)<3. For omit, gamma decreases, the denominator increases under the m-expansion, and the old numerator reverse ratio is <=[1-(2h+3)/u]^-1. Therefore e_O/e <=(1+3/(h-1))/(1-(2h+3)/u). The excess of this is <=4/h+3h/u because denominator>=1-212/1000, (25/8)/(1-212/1000)<4 and (53/25)/(1-212/1000)<3. Consequently both adverse boundary differences e-e_R,e_O-e are <=P=8/h^3+6/(uh); both comparison factors (1+e_R)/(1+e),(1+e)/(1+e_O) are >=1-P. This proves the HZ bound in a ten-times-wider direct band.

## 2. One-sided alpha transport (new)

HY's exact joint law with k+l+z=h, z in {0,1}, masses M_u(k)M_m(l), gives alpha=E[v_u(k)], with v_u(k)=c_u-k(k+2)/[2u(2u+1)], c_u=1/4+3/(8u+4). On the read step compose h+1, u+1, m+1. The first two operations move k by 0 or +1; the last moves k by 0 or -1. In particular k_R>=k-1, stronger for the required *upper* change than the symmetric |k_R-k|<=2 used by HY. c_(u+1)<c_u. With k<=h and denominator-reciprocal difference <=1/u^3 (HY),
alpha_R-alpha <=(2h+1)/(2u(2u+1))+h(h+2)/u^3.
This also holds for k=0 (no downward move is possible). The omit coupling gives alpha_O>=alpha. For all three locations alpha>=1/5, since v>=1/4-(h+1)(h+3)/(4u^2)>1/5. Hence when h<=u/20 the read alpha ratio is <=1+1/(7u), and in the full h<=u/10 band it is <=1+1/(3u). For example for s=h/u<=s0, the coefficient of 1/u in the relative change is bounded by 5[(2s0+1/32000)/4+s0^2+2s0/32000]. Both constant comparisons are exact rationals.

HP's mixed transport at g=h-1 bounds each capacity increment multiplier for b by 1+(2h+1)/[(u-h+1)(u+h+3)], with the same bound for the larger m and later increment. The unnormalized convolution is log-concave (HY), so advancing h after the capacity increments cannot increase b. For s0=1/20 each increment <=1+1/(9u), for s0=1/10 each <=1+5/(24u), using (2s0+1/32000)/(1-s0^2). Thus b_R/b<=1+1/(4u) in the narrower band and <=1+3/(7u) in the wider band. The omit b_O>=b by HY/HP. As q>=9u/10, H_q is decreasing in the relevant alpha range. HY gives L_R/L>1+1/(u+1), L/L_O>1 and H_q(alpha)/H_(q+1)(alpha_O)>1+1/(u+1), since alpha>=1/5. The read H factor is >=1/(1+alpha relative bound increment) as in HY. The combined unfavorable b/alpha multiplier denominator is <=1+(2/5)/u for h<=u/20 and <=1+(4/5)/u in h<=u/10.

## 3. Three complementary surplus regions

I: 4h^2<=u. Then h<=u/20 since u>=32000. Instead of relying on HQ's narrow signed band, use HQ's uniform absolute bound |r_g-r_(g+1)|<2/(u+3) with r_g>=9/10 at the needed indices and capacities (Polya minimum >=(u-h)/(u+h+4)). A neighboring normalized ratio in either direction is <=1+20/(9u). Together with the b capacity factor <=1+1/(4u), the adverse multiplier in the read direction is <=1+5/(2u). As b=(h+3)r_(h-1)/h, obtain
b_R/b <= (1-3/[(h+1)(h+3)])(1+5/(2u)) <= 1-3/(2h^2).
Indeed 3h^2/[(h+1)(h+3)]>=1875/728 and (5/2)h^2/u<=5/8. For omit, capacity increase helps, so
b_O/b >= (1+3/[(h-1)(h+3)])/(1+20/(9u)) >= 1+3/(2h^2),
using 3h^2/[(h-1)(h+3)]>=25/9 and (20/9)h^2/u<=5/9. Thus both comparison b factors >=1+1/(2h^2) (b>=1/2). Also P<=19/(2h^3), and (1+1/(2h^2))(1-19/(2h^3))>1 for h>=25. This pays the boundary loss in full, leaving geometric surplus and at most the read alpha multiplier denominator 1+1/(7u).

II: 4h^2>u, h<=u/20. Here P<76/u^(3/2)<9/(20u). Combined b/alpha denominator <=1+2/(5u), so both K comparisons exceed
(1+1/(u+1))(1-9/(20u))/(1+2/(5u)) > 1+1/[8(u+1)].

III: u/20<h<=u/10. Here uP<64000/u^2+120/u<1/100. Combined b/alpha denominator <=1+4/(5u), so the analogous bound with P coefficient 1/100 and denominator coefficient 4/5 again exceeds 1+1/[8(u+1)].

For the final rational comparisons, with coefficients B,P0, cross multiplying the desired strict inequality gives (7/8-P0-B)u-2P0-9B/8>0. Use (B,P0)=(1/7,0),(2/5,9/20),(4/5,1/100), respectively. All three slopes positive and values at 32000 positive. In I the combined b-boundary factor is strictly >1; the inequality with P0=0 is therefore justified. Omit uses a no-worse bound than read in all three regions.

## 4. Global stitch

For h>u/10, h^2/u>u/100. HY Proof 2 (weighted signed-tail payment) requires u>=64, h>=36, h^2>=16q and h^2/u>=(625/36) ln(1600(u+1)). The first three hold for u>=32000,h>u/10. For the last, at 32000, 1600(32001)<2^26 and ln2<7/10, so the right side <(625/36)*26*7/10<320. The difference u/100-(625/36)ln(1600(u+1)) is increasing thereafter. HY supplies the strict 1/[8(u+1)] margin. HO covers h<=24. This closes all deficits for u>=32000, with the exact same K and no change of observer. Dependencies are author proofs, not independently reviewed.

## Executed exact sample and constant checks (Python 3)

The following is the locally executed code after correcting the omit constant from an overly large 3 to the valid lower bound 25/9. All signs use integer or rational arithmetic, decimals only for display. The samples are not an exhaustive proof of the finite complement.

```python
from fractions import Fraction as F
from math import prod, isqrt

def ports(n,H):
    D=prod(n+i+3 for i in range(H)); a=[D]
    for k in range(H):
        v,r=divmod(a[-1]*(k+2)*(n-k),(k+1)*(n+k+3))
        assert r==0
        a.append(v)
    return a,D

def factors(u,q):
    h=u-q; m=u+q; H=h+1
    p,P=ports(u,H); a,A=ports(u-1,H); b,B=ports(m,H)
    def C(x,y,g): return sum(x[k]*y[g-k] for k in range(g+1))
    Q=C(p,b,h-1); V=C(p,b,h); W=C(a,b,h)+C(a,b,h-1)
    gamma=lambda n:F(n+2,4*n+2)
    e=gamma(m)*F((a[h]+a[h+1])*B,W)
    alpha=gamma(u)*F(W*P,(Q+V)*A)
    beta=F(V,Q)
    L=F((3*u+q+1)**2,u+2*q+1)
    K=L*alpha*(1+e)/((1+beta)*(1+q*alpha)**2)
    return e,alpha,beta,K

U=32000
# Uniform bounds for u>=U, using 1/u<=1/U and h/u<=s.
assert F(2)+F(5,25)+F(26,25)*F(28,25)/10+F(2,25*U)<3
assert F(25,8)/(1-F(212,1000))<4
assert F(53,25)/(1-F(212,1000))<3
assert F(625,36)*26*F(7,10)<320
assert 1600*(U+1)<2**26
assert F(625,36)/(U+1)<F(1,100)
assert 76**2*400 <81*U # 76/sqrt(U)<9/20
assert F(64000,U**2)+F(120,U)<F(1,100)
for s,c,bound,acost,total in [(F(1,20),F(1,9),F(1,4),F(1,7),F(2,5)),(F(1,10),F(5,24),F(3,7),F(1,3),F(4,5))]:
    assert (2*s+F(1,U))/(1-s*s)<c
    assert 2*c+c*c/U<bound
    assert 5*((2*s+F(1,U))/4+s*s+2*s/U)<acost
    assert bound+acost+bound*acost/U<total
    assert F(1,4)-(s+F(1,U))*(s+F(3,U))/4>F(1,5)
assert (1-F(1,20))/(1+F(1,20)+F(4,U))>F(9,10)
assert F(1,4)+F(20,9)+F(1,4)*F(20,9)/U<F(5,2)
assert F(3*25**2,26*28)-F(5,8)>F(3,2)
assert (F(25,9)-F(5,9))/(1+F(20,9*U))>F(3,2)
assert F(25,2)>F(19,2)+F(19,4*25**2)
# For each (B,P), (1+1/(u+1))(1-P/u)/(1+B/u)>1+1/(8(u+1)).
# Difference after positive cross multiplication: (7/8-P-B)*u-2P-9B/8.
for B,P in [(F(2,5),F(9,20)),(F(4,5),F(1,100)),(F(1,7),F(0))]:
    assert (F(7,8)-P-B)*U-2*P-F(9,8)*B>0
N=0; mins={}
for u in [32000,64000,140000]:
    z=isqrt(u//4)
    H={25,64,z,z+1,2*z}
    if u==32000: H|={u//20,u//20+1,u//10}
    for h in sorted(H):
        q=u-h
        e,a,b,K=factors(u,q); er,ar,br,Kr=factors(u+1,q); eo,ao,bo,Ko=factors(u,q+1)
        P=F(8,h**3)+F(6,u*h)
        assert 0<=e<F(2,h*h) and e-er<=P and eo-e<=P
        assert ao>=a and bo>=b and min(a,ar,ao)>=F(1,5)
        if 20*h<=u:
            assert ar/a<=1+F(1,7*u) and br/b<=1+F(1,4*u)
        else:
            assert ar/a<=1+F(1,3*u) and br/b<=1+F(3,7*u)
        if 4*h*h<=u:
            regime='small'
            assert br/b<=1-F(3,2*h*h) and bo/b>=1+F(3,2*h*h)
            assert min((1+b)/(1+br),(1+bo)/(1+b))>=1+F(1,2*h*h)
        elif 20*h<=u:
            regime='medium'; assert P<F(9,20*u)
        else:
            regime='wide'; assert P<F(1,100*u)
        rr=(Kr/K-1)*(u+1); oo=(K/Ko-1)*(u+1)
        assert min(rr,oo)>F(1,8)
        mins[regime]=min(mins.get(regime,min(rr,oo)),rr,oo)
        print(u,h,regime,float(rr),float(oo),flush=True); N+=1
print('cases',N,'comparisons',2*N,'minimum_scaled_gap', {k:float(v) for k,v in mins.items()})
```

Actual stdout (all assertions passed):
```
32000 25 small 66.55514977714692 72.62704783950156
32000 64 small 12.555527949703587 13.89943810325355
32000 89 small 7.371689802799436 8.507800854236173
32000 90 medium 7.247003614029967 8.379034377748177
32000 178 medium 3.048919674203052 4.0802072333120165
32000 1600 medium 1.520524433363727 2.652329302817375
32000 1601 wide 1.5205114087924063 2.6524032569583884
32000 3200 wide 1.5170382667272877 2.79614783694756
64000 25 small 131.48944715440305 142.627757964079
64000 64 small 23.502806904568036 25.18237689094475
64000 126 small 7.4418666071941955 8.53934041987581
64000 127 medium 7.351663728051149 8.447047354580992
64000 252 medium 3.0557961815266084 4.078005377865669
140000 25 small 285.70778074776496 308.880590669989
140000 64 small 49.496982646275086 51.97854792696428
140000 187 small 7.467597631767478 8.533691430325353
140000 188 medium 7.405972317449512 8.47110223041234
140000 374 medium 3.0533338527212353 4.068351526163627
cases 18 comparisons 36 minimum_scaled_gap {'small': 7.371689802799436, 'medium': 1.520524433363727, 'wide': 1.5170382667272877}
```

## Next

Use asymmetric transport and split actual b/alpha costs more finely, or build fast exact sign certificates for the still uncovered finite complement u<32000. Avoid enumerating the whole old triangular domain. HO, HV, HW, HX, HY retain their exact proven scopes. A stronger next direction is to use the actual L surplus (rather than the coarse 1/u) and a sharper nonnegative one-sided alpha expectation; then the direct band might reach h/u>1/10 and meet the signed baseline at a smaller budget. Independent review and strict Activity observation audit pending.
