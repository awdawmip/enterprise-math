# R284IB — Asymmetric capacity payment, geometric surplus, and onset 7300

2026-11-26. Author proof and exact computation; NOT_REVIEWED. Same auxiliary binary-tag safe-word total-count observer; no native physical attribution. Frozen dependencies, all under research_notes/portable_direct/: IA @ bcf3cc5f2338301fca81835ccaf7a549b76357cb R284IA_ONE_SIDED_CAPACITY_PAYMENT_AND_32000_ONSET_20261126.md; HZ @ ae1ed992c6adf63e057ddb5c1729a405a654b2e8 R284HZ_ADJACENT_BOUNDARY_PAYMENT_EFFECTIVE_GLOBAL_ONSET_20261126.md; HY @ 0164790b93645d9e15c65baa4d77260fcaa8e1c9 R284HY_CAPACITY_COUPLING_AND_SQRT_DOMAIN_20261125.md; HQ @ b0572296445fe5355dd4807ac4d6073fe69e8144 R284HQ_EXACT_CURVATURE_BRANCH_BALANCE_20261125.md; HP @ 3a29820d72c053c4a5a71e303244ce747a08be38 R284HP_EXACT_TILTED_PORT_COUPLING_20261125.md; HO @ 35dc10f164c6a93ea5d65c4b5285304188fae549 R284HO_EXACT_FIXED_DEFICIT_POLYNOMIAL_STRIPS_20261125.md. All read. Global main entry blobs matched 1374a634fcecfc9c5458b070e571ebfacbd38336; EM continuation entry matched dbe291d50bd5a8c8a94f20927f6b76ee20f8ddc3. P000 V5, ACTIVE worldview, joint preservation, portable and method rules read. Original own registration r1-20261124-0256-r284gd-session-v1 SUCCEEDED, RA-B82240E8488EF5A1DA5186C4 / EM-DIRECT-0C386E; metadata not private session possession. Owner inventory request r1-20261126-0202-owner-read RUNNING at last prepublication observation. Independent same research line; no shared CLAIM or Result mutation.

**Theorem.** For integers u>=7300 and 0<=q<u, K(q,u+1)>K(q,u); for q+1<u, K(q,u)>K(q+1,u). For deficit h=u-q>=25 both valid ratios exceed 1+1/[100(u+1)]. HO supplies strict signs for h<=24. IA onset 32000 reduced by factor 32000/7300. Finite complement remains open.

## Definitions

M_n(k)=(k+1)/(n+1) binom(2n+2,n-k) on 0<=k<=n, zero otherwise. C_(n,m)(g)=sum_k M_n(k)M_m(g-k). m=u+q, h=u-q, Q=C_(u,m)(h-1), V=C_(u,m)(h), A=C_(u-1,m)(h)+C_(u-1,m)(h-1), E=M_(m-1)(0)[M_(u-1)(h)+M_(u-1)(h+1)]. K=L H_q(alpha)(1+e)/(1+b), where L=(3u+q+1)^2/(u+2q+1), H_q(x)=x/(1+qx)^2, alpha=A/(Q+V), b=V/Q, e=E/A. R,O are read (q,u+1) and omit (q+1,u).

## 1. Boundary transport up to h/u=1/5

Take U=7300, u>=U, 25<=h<=u/5. The exact HZ/IA normalized branch estimates require only support h+2<=u-1, gamma_m<=4/15, h>=25, positive denominators in the displayed ratio bounds; all hold. In detail w_z(k)=M_z(k)/M_z(0), gamma_z=(z+2)/(4z+2), a=u-1, T_j=sum w_a(k)w_m(j-k), D_h=T_h+T_(h-1). The branchwise comparison of rho products gives T_h>=w_a(h)(h+2)(h+3)/6; HQ r<=1 gives D_h>=9T_h/5, and w_a(h+1)/w_a(h)<=5/4. Thus e<2/h^2. Applying exactly the adjacent normalized branch ratios from HZ, independently of HZ's final onset, yields
e_R/e >= (1-2/u^2)(1-(2h+5)/u)(1-(h+1)(h+3)/u^2)/(1+3/h),
e_O/e <= (1+3/(h-1))/(1-(2h+3)/u).
These follow from the normalized capacity multiplier [1-k(k+2)/((z+1)(z+3))]^-1 and actual degree sum <=h+1, and D_(h+1)/D_h<=1+3/h, D_h/D_(h-1)<=1+3/(h-1). All factors positive. Read deficit <=3/h+3h/u because 2+5/25+(26/25)(28/25)/5+2/(25U)<3. Omit excess <=6/h+4h/u, using denominator>=.576, (25/8)/.576<6 and (53/25)/.576<4. For h<=u/10 use denominator>=.788 and bounds 4/h+3h/u as IA. Therefore both adverse changes are <=P, with
P=8/h^3+6/(uh) if h<=u/10,
P=12/h^3+8/(uh) otherwise.
Both boundary comparison factors >=1-P. Nonzero E retained.

## 2. One-sided transport and asymmetric capacity charges

The IA/HY joint law k+l+z=h, z in {0,1}, gives alpha=E[v_u(k)], v_u(k)=1/4+3/(8u+4)-k(k+2)/[2u(2u+1)]. On the read step k_R>=k-1, and alpha_R-alpha <=(2h+1)/[2u(2u+1)]+h(h+2)/u^3 as IA. Omit alpha_O>=alpha. For h<=s u, all three alpha >=a_s=1/4-(s+1/U)(s+3/U)/4>1/5 for s<=1/5; hence
u*(alpha_R/alpha-1) <=[(2s+1/U)/4+s^2+2s/U]/a_s.
For s=1/5 this is <585/1000. In the narrower bands use 1/5 as lower bound: s=1/20 gives <1/7 and s=1/10 gives <1/3, exactly as IA but with U=7300.

For b, HP mixed transport charges each capacity at g=h-1 by 1+(2h+1)/[(n-h+1)(n+h+3)]. The two capacities are u and m=2u-h, not both u. At s=1/5 the two increments are <=1+c1/u,1+c2/u, with c1=(2s+1/U)/(1-s^2), c2=(2s+1/U)/((2-s)^2-s^2). Log-concavity under advancing h gives b_R/b<=their product <=1+543/(1000u). Omit b_O>=b. In the smaller bands the old symmetric bounds 1+1/(4u),1+3/(7u) apply for s=1/20,1/10, respectively: the individual charges <=1+1/(9u),1+5/(24u). Their products satisfy these bounds at U=7300. q>=4u/5, alpha>=1/5; H_q decreases, so read H factor is >=1/max(1,alpha_R/alpha), and omit H ratio >1+1/(u+1) by HY. Combined unfavorable b/alpha read denominator <=1+B/u, with B=2/5,4/5,113/100 in the three nested bands. This last bound uses actual unequal capacities, not a symmetric worst case.

## 3. Strengthened exact geometric surplus

HY L_R/L>1+1/(u+1) and L/L_O>1. In h<=u/5, stronger L_R/L>1+7/[6(u+1)]. Set A0=3u+q+1, B0=u+2q+1. The exact cross difference is
6(u+1)(A0+3)^2 B0 - (6(u+1)+7) A0^2(B0+1).
Substitute u=5h+x,q=u-h. The polynomial has 9 nonzero coefficients, all positive (minimum 44), verified by exact symbolic expansion. This gives the strengthened lower bound without differentiation or asymptotic error.

## 4. Four direct regions

I: 2h^2<=u. Then h<=u/20 since u>=U. HQ absolute curvature |r_(g+1)-r_g|<2/(u+3), and Pólya minimum >=(u-h)/(u+h+4)>9/10 for the indices involved. Thus adverse neighboring normalized ratio <=1+20/(9u). Combining with the capacity bound gives read adverse multiplier <=1+5/(2u). With b=(h+3)r_(h-1)/h:
b_R/b <=(1-3/[(h+1)(h+3)])(1+5/(2u)) <=1-5/(4h^2),
b_O/b >=(1+3/[(h-1)(h+3)])/(1+20/(9u)) >=1+5/(4h^2).
The first uses 3h^2/[(h+1)(h+3)]>=1875/728 and (5/2)h^2/u<=5/4; the second uses 3h^2/[(h-1)(h+3)]>=25/9 and (20/9)h^2/u<=10/9. Since b>=9/10, each comparison b factor >=1+1/(2h^2), from (9/19)(5/4)>1/2. Also P<=11/h^3, and (1+1/(2h^2))(1-11/h^3)>1 for h>=25. The b factor pays the boundary factor completely. Remaining read alpha denominator <=1+1/(7u); omit is favorable.

II: 2h^2>u and h<=u/20. Then uP<22 sqrt(2)/sqrt(u)<37/100, and B=2/5.

III: u/20<h<=u/10. Then uP<64000/u^2+120/u<1/50, B=4/5.

IV: u/10<h<=u/5. Then uP<12000/u^2+80/u<12/1000, B=113/100. Use the stronger geometric surplus 7/[6(u+1)] for read. Omit needs no adverse b/alpha payment and has H surplus >1+1/(u+1).

For each read lower bound (1+A/(u+1))(1-P0/u)/(1+B/u)>1+J/(u+1) with J=1/100, cross multiplication gives (A-P0-B-J)u-P0(1+A)-B(1+J)>0. Use (A,P0,B)=(1,0,1/7),(1,37/100,2/5),(1,1/50,4/5),(7/6,12/1000,113/100). Each slope and value at U are strictly positive. Omit is at least as favorable in I-III; in IV use (1,12/1000,0). This proves the direct band.

## 5. Global stitch

For h>u/5, h^2/u>u/25. HY Proof 2 suffices if u>=64,h>=36,h^2>=16q, h^2/u>=(625/36) ln(1600(u+1)). At U=7300, 1600(U+1)<2^24 and ln2<7/10, hence RHS<(625/36)*24*7/10=875/3<292=U/25. The difference u/25-(625/36)ln(1600(u+1)) increases thereafter. The other conditions hold since h>u/5 and U>=400. HY gives the stronger 1/[8(u+1)] margin. HO covers h<=24. End of proof.

## Exact computation and reproduction

Local Python arbitrary integers/Fraction and SymPy, exact signs; decimal display only. Analytic checks and 19 complete sample positions (38 neighbor comparisons) printed before timeout on the final larger sample (32000,6400), which is NOT counted. Minimum observed scaled gap 1.5170400769146706 (32000,3201 read). No completed assertion failed. Scope: u=7300,10000 with h={25,floor sqrt(u/2),that+1,u//20,u//20+1,u//10,u//10+1,u//5}; u=32000 with h=126,127,3201. The script below reproduces completed scope and the analytic constants; no exhaustive finite complement claim.

```python
from fractions import Fraction as F
from math import prod,isqrt
import sympy as S
U=7300
for s,den,co1,co2 in [(F(1,10),F(788,1000),4,3),(F(1,5),F(576,1000),6,4)]:
    assert 1-(2+F(3,25))*s>=den
    assert F(25,8)/den<co1 and F(53,25)/den<co2
    assert 2+F(5,25)+F(26,25)*F(28,25)*s+F(2,25*U)<3
for s,c,bound,acost,total in [(F(1,20),F(1,9),F(1,4),F(1,7),F(2,5)),(F(1,10),F(5,24),F(3,7),F(1,3),F(4,5))]:
    assert (2*s+F(1,U))/(1-s*s)<c
    assert 2*c+c*c/U<bound
    assert 5*((2*s+F(1,U))/4+s*s+2*s/U)<acost
    assert bound+acost+bound*acost/U<total
    assert F(1,4)-(s+F(1,U))*(s+F(3,U))/4>F(1,5)
assert (1-F(1,20))/(1+F(1,20)+F(4,U))>F(9,10)
assert F(1,4)+F(20,9)+F(1,4)*F(20,9)/U<F(5,2)
assert F(3*25**2,26*28)-F(5,4)>F(5,4)
assert (F(25,9)-F(10,9))/(1+F(20,9*U))>F(5,4)
assert F(9,19)*F(5,4)>F(1,2)
assert F(25,2)>11+F(11,2*25**2)
assert U>=200
assert 22**2*2 < F(37,100)**2*U
assert F(64000,U**2)+F(120,U)<F(1,50)
s=F(1,5)
c1=(2*s+F(1,U))/(1-s*s)
c2=(2*s+F(1,U))/((2-s)**2-s*s)
assert c1+c2+c1*c2/U<F(543,1000)
amin=F(1,4)-(s+F(1,U))*(s+F(3,U))/4
assert amin>F(1,5)
assert ((2*s+F(1,U))/4+s*s+2*s/U)/amin<F(585,1000)
assert F(543,1000)+F(585,1000)+F(543,1000)*F(585,1000)/U<F(113,100)
assert F(12000,U**2)+F(80,U)<F(12,1000)
x,h=S.symbols('x h');u=5*h+x;q=u-h
A=3*u+q+1;B=u+2*q+1
poly=S.Poly(S.expand(6*(u+1)*(A+3)**2*B-(6*(u+1)+7)*A**2*(B+1)),x,h)
assert all(c>0 for c in poly.coeffs())
print('L certificate:',len(poly.terms()),'terms; min coefficient',min(poly.coeffs()))
for A,P,B,J in [(F(1),F(0),F(1,7),F(1,100)),(F(1),F(37,100),F(2,5),F(1,100)),(F(1),F(1,50),F(4,5),F(1,100)),(F(7,6),F(12,1000),F(113,100),F(1,100))]:
    assert A-P-B-J>0 and (A-P-B-J)*U-P*(1+A)-B*(1+J)>0
assert (1-F(12,1000)-F(1,100))*U-2*F(12,1000)>0
assert 1600*(U+1)<2**24
assert F(625,36)*24*F(7,10)<F(U,25)
assert F(625,36)/(U+1)<F(1,25)
assert U>=36*5 and U>=16*25
print('all analytic constant comparisons passed')
def ports(n,H):
    D=prod(n+i+3 for i in range(H));a=[D]
    for k in range(H):
        v,r=divmod(a[-1]*(k+2)*(n-k),(k+1)*(n+k+3));assert r==0;a.append(v)
    return a,D
def factors(u,q):
    h=u-q;m=u+q;H=h+1
    p,P=ports(u,H);a,A=ports(u-1,H);b,B=ports(m,H)
    def C(x,y,g):return sum(x[k]*y[g-k] for k in range(g+1))
    Q=C(p,b,h-1);V=C(p,b,h);W=C(a,b,h)+C(a,b,h-1)
    gamma=lambda n:F(n+2,4*n+2)
    e=gamma(m)*F((a[h]+a[h+1])*B,W)
    alpha=gamma(u)*F(W*P,(Q+V)*A);beta=F(V,Q)
    L=F((3*u+q+1)**2,u+2*q+1)
    K=L*alpha*(1+e)/((1+beta)*(1+q*alpha)**2)
    return e,alpha,beta,K
for u in [U,10000,32000]:
    z=isqrt(u//2)
    for h in sorted({25,z,z+1,u//20,u//20+1,u//10,u//10+1,u//5} if u!=32000 else {z,z+1,3201}):
        q=u-h;e,a,b,K=factors(u,q);er,ar,br,Kr=factors(u+1,q);eo,ao,bo,Ko=factors(u,q+1)
        p=F(8,h**3)+F(6,u*h) if 10*h<=u else F(12,h**3)+F(8,u*h)
        assert 0<=e<F(2,h*h) and e-er<=p and eo-e<=p
        assert ao>=a and bo>=b and min(a,ar,ao)>F(1,5)
        if 2*h*h<=u:
            assert br/b<=1-F(5,4*h*h) and bo/b>=1+F(5,4*h*h)
        if 10*h>u:
            assert ar/a<=1+F(585,1000*u) and br/b<=1+F(543,1000*u)
        rr=(Kr/K-1)*(u+1);oo=(K/Ko-1)*(u+1)
        assert min(rr,oo)>F(1,100)
        print(u,h,float(rr),float(oo),flush=True)
```

Actual stdout before timeout:
```
L certificate: 9 terms; min coefficient 44
all analytic constant comparisons passed
7300 25 16.431974808016598 18.59903278565463
7300 60 4.423493077645962 5.538563778566978
7300 61 4.333924103867784 5.444957801905862
7300 365 1.5740335906751368 2.705793788196131
7300 366 1.5736455189717578 2.705782310183572
7300 730 1.5284847727336566 2.806959210405818
7300 731 1.5284596233907852 2.8073605380024484
7300 1460 1.5276239978340844 3.1574744583122163
10000 25 21.911568930873486 24.50389650011475
10000 70 4.470008422007738 5.57001138165101
10000 71 4.391330415322814 5.488280734895959
10000 500 1.5542463748969455 2.6859431636402284
10000 501 1.5540508669027224 2.686024134286476
10000 1000 1.5243744503815442 2.8030602164294867
10000 1001 1.5243649798979515 2.8033622255474904
10000 2000 1.5266380161011686 3.1567969972912264
32000 126 4.511412511858203 5.568025783105056
32000 127 4.466042818721181 5.521672099322554
32000 3201 1.5170400769146706 2.7962470413099587
```

Next: use actual geometric surplus and asymmetry to refine the capacity charge by coupled branch expectation (rather than maximum k=h); alternatively exploit the now much smaller finite complement with certified fixed-point interval recurrence plus exact fallback. Prior strips and wedge regions remain applicable. Independent review and strict activity observation audit remain pending.
