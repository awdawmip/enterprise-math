# R284KK — Signed finite moment boundary transfer, even-deficiency septic fiber, and exact fixed-point all-budget extension

2026-11-28. Author written proof and executed local Python/C++ checks; NOT_REVIEWED. Auxiliary arithmetic of the R284 observer, not native spatial transfer. Own registration recovered by r1-20261128-1502-own-recovery; original session_start r1-20261124-0256-r284gd-session-v1; EM-DIRECT-0C386E / TASK_RESEARCH / RA-B82240E8488EF5A1DA5186C4; no formal own runs. Owner inventory r1-20261128-1502-owner-read SUCCEEDED, as-of 2026-11-28T07:03:06.304291Z, 547 total, empty LEASED filter; source 2dc6782f370efc130fc54ebc8e5568c9c7733ccc (current at admission, head changed by completion). No shared Task/CLAIM mutation. Global entry immutable main 7310e87bb381cb46571fb6856330d6fe70eb225e, both entry blobs verified; global P000 V4 projection verified by canonical blob; Source V5 foundation projection, ACTIVE worldview, joint/residual contracts, portable research and current method consulted.

Frozen inputs: JR 88211c0912397b00536b6c4d6427cab29d4499f2:research_notes/portable_direct/R284JR_GLOBAL_BUDGET_POLYNOMIAL_AND_INTEGER_ROOT_EXCLUSION_20261127.md; KD 544d7a97fa075fe62848ae1cf27acdb9bdc7df19:research_notes/portable_direct/R284KD_FINITE_BRIDGE_AND_MODULAR_FALLBACK_20261128.md; KG 0c5c18b5e6725fcdebad3c12b9ebec33659ba12f:research_notes/portable_direct/R284KG_SEXTIC_POLE_FIBER_AND_PRIMITIVE_COMPOSITE_SIEVE_20261128.md; KI 206cb02a626169e6dc075566a80666bb2bfe763e:research_notes/portable_direct/R284KI_FACTORIAL_FIXED_DIVISOR_AND_NORMALIZED_PERIOD_20261128.md; KJ 66fbb96d3b010ce81f5b32fc543bfd4fb3dbb59f:research_notes/portable_direct/R284KJ_ADJACENT_OUTER_FIBERS_AND_JOINT_SMOOTH_SIEVE_20261128.md; JO 81cc0f06a4cf0209733a50284362f9bb1e8aded9:research_notes/portable_direct/R284JO_FULL_JOINT_BLOCK_TRANSFER_20261127.md treats all offsets r>=3 including r=d, so the n=-2 fiber itself is not claimed new; the increment is its explicit low-degree signed-moment compression and resulting fixed septic observer, plus the executed new intersection and exact fixed-point finite closure.

## 1. Finite signed moment transfer with the exact boundary

Use JR's R_v(k)=product_{i<k}(v-i)/(v+i+3), u=q+d, n=2q+d, l=d-k, V=sum (k+1)(l+1)R_u(k)R_n(l), Q=sum (k+1)l R_u(k)R_n(l-1) (zero at l=0), A=sum (u-k)(u+k+2)/(2u(2u+1)) times the sum of the two weights, E=R_u(d) q(2d+3)(n+2)/(2(2u+1)(4n+2)), W=A+E, Z=qA+Q+V. C=3q(4q+3d+1)^2 WQ-32(3q+d+1)Z^2. These rational formulas are defined on the formal fiber n=-2: set m=(d-2)/2, q0=-m-2, u=m, d=2m+2; all denominators nonzero for d>=3. E vanishes identically because n+2=0. R_{-2}(l)=(-1)^l(l+1). This is a formal observer evaluation, not a legal negative physical budget.

Put w_k=(-1)^k R_m(k), T_k=(m+k+2)w_k and B=T_{d+1}=(d-m)w_d. Retain the signed factorial moments M_r=sum_{k=0}^d k^{fall r} w_k. Since (m+k+3)w_{k+1}=(k-m)w_k, direct subtraction gives
 T_{k+1}(k+1)^{fall r}-T_k k^{fall r}
 =-(d-r)k^{fall r}w_k + r(r-1-m)k^{fall(r-1)}w_k
for r>=1; for r=0 the difference is -d w_k. Sum including BOTH endpoints:
 M_0=(m+2-B)/d,
 M_r=[r(r-1-m)M_{r-1}-B(d+1)^{fall r}]/(d-r), 1<=r<=4, d>=5.
For r>=1 the initial falling factorial is zero. This is a finite, exact reduction for the declared four observations; it does not discard B, which is generally nonzero for odd d. At d=3,4 evaluate the original finite sums or use moments only below the singular denominator.

Define the linear evaluator L(k^{fall r})=M_r, and sigma=(-1)^d. Then
 V=sigma L((k+1)(d-k+1)^2),
 Q=-sigma L((k+1)(d-k)^2),
 A=sigma L((m-k)(m+k+2)(k+1)(2(d-k)+1))/(2m(2m+1)).
The last identity uses the joint cancellation of the l-dependent square terms in V+Q before applying the A weight. Z=q0 A+V+Q. Thus all original C observations are exactly recovered from the four-step moment transfer and the single boundary B. For odd d one must retain B; computing it from the original product costs O(d) rational multiplications, and no unconditional sublinear full evaluation is claimed. For even d>=6, m is a positive integer >=2, and R_m(d)=0, so B=0 and the transfer is constant-size rational arithmetic. This is a signed joint observation compression on this specific fiber only, not a global elimination of branch data.

## 2. Explicit septic observer for even d>=6

Let d=2m+2, integer m>=2. Substituting B=0 in the recurrence (or iterating M_r/M_0=r(r-1-m)/(d-r)) and evaluating the polynomial weights gives
 V=(m+2)(8m^3+28m^2+15m-17)/(2(2m-1)(2m+1)),
 Q=-(m+2)(8m^3+20m^2+5m-10)/(2(2m-1)(2m+1)),
 A=(m+1)(m+2)(4m+7)/(4(2m-1)(2m+1)),
 Z=-(m+2)(4m+7)(m^2-m+4)/(4(2m-1)(2m+1)).
Since E=0, q0=-m-2, 4q0+3d+1=2m-1 and 3q0+d+1=-m-3, insertion yields
 C(q0,d)=(m+2)^2(4m+7) F(m)/[8(2m-1)^2(2m+1)^2],
 F(m)=96m^7+496m^6+644m^5+4m^4+1015m^3+1751m^2+2356m+5316.
All coefficients positive and sum 11678<4^7, so for m>=2, 0<F(m)<(4m+7)^7. Note the boundary exception d=4: the r=4 moment recurrence is singular, and direct evaluation gives C=34631/4, not the displayed septic formula. It is explicitly excluded from the septic theorem (already covered by JR).

The cleared integer carrier P_d=D^2 C of JR has D=2u(2u+1)(4n+2)D_u D_n, D_v=product_{i=0}^{d-1}(v+i+3). Here D_m product factors <=3m+4 and D_{-2}=d!, and all other D factors have prime support <=4m+7=2d+3. Because q0 is integer, any legal integer root q must satisfy the whole-composite divisibility
 h=q+m+2 | P_d(-m-2).
For any prime p>2d+3 dividing h, D(q0) is a unit and all factors outside F(m) are p-units. Therefore
 v_p(h)<=v_p(F(m))
 is a necessary condition for an integer root. If p does not divide F(m), C(q,d) is a p-unit (P_d and D are both units by congruence), so nonzero. The product of seven distinct primes >2d+3 exceeds F(m), so at most SIX exceptional large primes occur per even d. In KD's bracket h<(2d+3)^2, hence at most one such prime per h, and the number of surviving budgets with a large prime factor in h is O(d) (at most six progressions, each <= 8d^2/[15(2d+4)]+1). Smooth h remains open in the general unbounded problem.

In KJ's coordinates u=q+d, u+1, 2u+1, the new h=u-m obeys u-h=m, u+1-h=m+1, 2u+1-2h=2m+1. Thus no prime >2d+3 can be common to h and any of those three coordinates. This is a joint arithmetic condition, not a statistical independence assumption; small-prime overlap and whole composite constraints are retained.

## 3. Executed exact checks and joint sieve

Python Fraction compared V,Q,A,Z independently via the original R_m product and the moment recurrence for every d=5..300 (296 cases). The explicit septic formula matched C for every even d=6..300 (148 cases); positivity and bound also passed. Original d=4 formula trial failed, then the true singular boundary was identified and scoped out as above; this is a mathematical endpoint correction, not a hidden computation failure.

The C++ integer sieve repeats KJ's necessary three-coordinate tests on the 50 even d in 3002..3100 and then tests h. Exact domain q=ceil(4d^2/5)..floor(4d^2/3). Ascending prime sieve gives largest prime factors; at these thresholds no coordinate contains two large factors. Horner mod p is exact within signed 64-bit, with p<=2*(4*3100^2/3+3100)+1. No floating-point or independence assumptions in the sieve.
Totals: initial 248251592; KG 87413408; KG+u+1 29436568; KJ three-coordinate 7432099; of these 4809814 have eligible large prime factor in h; all four survivors 2622438; new strict exclusions 4809661. This removes 4809661 of KJ's even-d survivors; 153 eligible exceptions remain. The odd d were not tested by this septic criterion. These are benchmark counts over the broad bracket; section 4 separately closes all d in this finite interval by exact real-root localization. No claimed unbounded closure.

## 4. Exact integer fixed-point sign certification (all d=3001..3100)

Reuse KD's proof of one simple real zero and the sign pattern for all d>=81, and JR's C=0 necessary condition. New implementation evaluates the ORIGINAL rational observer using exact integers rather than binary64 error estimates: T=2^96. Each prefix ratio R_v(k) is enclosed by integers [L_k,U_k]/T, beginning [T,T]. On multiplication by positive rational a/b use floor(L_k*a/b), ceil(U_k*a/b). Thus induction gives rigorous outward enclosure, with no roundoff assumptions. At legal q all weights and denominators are nonnegative/positive (u-k>=q>0). Multiply two prefix intervals to obtain denominator T^2, form V,Q,A by additions and outward weighted divisions; E is rescaled from T to T^2. W and Z then also have denominator T^2. The two positive products in C have denominator T^4; subtraction uses lower(first)-upper(second) and upper(first)-lower(second). Every operation is exact integer arithmetic; any ambiguous interval is not a sign certificate. An ordinary floating evaluation only proposes adjacent candidate endpoints. The final assertions depend exclusively on the exact strict signs, hence correctness is independent of the proposal's accuracy.

For every integer d=3001..3100 the executed code found adjacent integers l_d,l_d+1 with strictly C(l_d,d)>0 and C(l_d+1,d)<0. All endpoints are legal; uniqueness proves no legal integer zero anywhere, including outside the proposed bracket. The fixed-point code used 96 fractional bits, with exact outward payment; no ambiguous case in these 200 sign checks. The all-budget exclusion theorem from JR+KD therefore extends to 3<=d<=3100, q>=64, d^2<=4q, with no q upper bound. The extension relies on KD's earlier author-proved uniqueness, not a new independent proof of that theorem. Local exact stdout includes the integer lower/upper sign bounds in T^4 units; its SHA256 is 4ce47d8a66bdd85b79704d90c75f811c132c37903ceb1d5a10d696986dc483ed. All 100 lower endpoints (in order d=3001..3100; upper=lower+1) are:
9596431 9602832 9609235 9615640 9622048 9628457 9634869 9641283 9647698 9654116 9660537 9666959 9673383 9679810 9686239 9692670 9699103 9705538 9711975 9718414 9724856 9731299 9737745 9744193 9750643 9757095 9763550 9770006 9776465 9782925 9789388 9795853 9802320 9808790 9815261 9821735 9828210 9834688 9841168 9847650 9854134 9860621 9867109 9873600 9880092 9886587 9893084 9899583 9906085 9912588 9919094 9925601 9932111 9938623 9945137 9951653 9958172 9964692 9971215 9977739 9984266 9990795 9997327 10003860 10010395 10016933 10023472 10030014 10036558 10043104 10049653 10056203 10062755 10069310 10075867 10082426 10088987 10095550 10102115 10108683 10115252 10121824 10128398 10134974 10141552 10148132 10154714 10161299 10167885 10174474 10181065 10187658 10194253 10200851 10207450 10214052 10220655 10227261 10233869 10240479

## 5. Reproducibility

The following three code blocks are the actual executed local scripts; each embedded script SHA256 was matched against its local file digest. Python 3; compile C++ with g++ -O3 -std=c++17 scan.cpp -o scan. Run python check.py, ./scan > scan.txt, python root.py > root.txt. The full scan output is embedded below and its SHA256 matches the local output. Root raw margins regenerate exactly by the provided code; the hash and all brackets are recorded above. Local root.txt is additionally available in the working bundle if needed. No hosted CI or formalization performed.

check.py SHA256 a274ed62a50701196489ba82dc08f7e3fef6ef8104738a444a73c464eb8bfe1c
```python
from fractions import Fraction as F
from math import prod

def direct(d):
    m=F(d-2,2);q=-m-2;n=-2
    U=[F(1)]
    for k in range(d):U.append(U[-1]*(m-k)/(m+k+3))
    V=Q=A=F(0)
    for k in range(d+1):
        l=d-k
        a=(k+1)*(l+1)**2*U[k]*(-1)**l
        b=(k+1)*l*l*U[k]*(-1)**(l-1) if l else 0
        V+=a;Q+=b;A+=(m-k)*(m+k+2)*(a+b)/(2*m*(2*m+1))
    Z=q*A+Q+V
    C=3*q*(4*q+3*d+1)**2*A*Q-32*(3*q+d+1)*Z*Z
    return U,V,Q,A,Z,C

def moments(d,U):
    m=F(d-2,2); B=(d-m)*(-1)**d*U[d]; M=[(m+2-B)/d]
    for r in range(1,5):M.append((r*(r-1-m)*M[-1]-B*prod(d+1-i for i in range(r)))/(d-r))
    # Polynomial weights expressed by forward differences, in falling factorial basis.
    def avg(f,n):
        a=[f(k) for k in range(n+1)];out=F(0);fac=1
        for r in range(n+1):
            out+=a[0]*M[r]/fac
            a=[y-x for x,y in zip(a,a[1:])];fac*=r+1
        return (-1)**d*out
    V=avg(lambda k:(k+1)*(d-k+1)**2,3)
    Q=-avg(lambda k:(k+1)*(d-k)**2,3)
    A=avg(lambda k:(m-k)*(m+k+2)*(k+1)*(2*(d-k)+1),4)/(2*m*(2*m+1))
    Z=(-m-2)*A+Q+V
    return V,Q,A,Z

def f(m):return ((((((96*m+496)*m+644)*m+4)*m+1015)*m+1751)*m+2356)*m+5316
for d in range(4,301):
    U,V,Q,A,Z,C=direct(d)
    if d>=5: assert moments(d,U)==(V,Q,A,Z),d
    if d%2==0 and d>=6:
        m=(d-2)//2
        assert C==F((m+2)**2*(4*m+7)*f(m),8*(2*m-1)**2*(2*m+1)**2),d
        assert C>0 and 0<f(m)<(4*m+7)**7,d
print('finite moment identities d=5..300: 296; even septics d=6..300: 148; all pass')
```
scan.cpp SHA256 a3911cbb9d8e83cb672846c329bda97e51c6c663cd53a9a67f569a7f3e89763c
```cpp
#include <vector>
#include <iostream>
#include <cstdint>
#include <cassert>
using namespace std;
using I=int64_t;
int main(){const int lo=3002,hi=3100,M=2*(4*hi*hi/3+hi)+1;vector<int> lp(M+1);for(int p=2;p<=M;p++)if(!lp[p])for(int i=p;i<=M;i+=p)lp[i]=p;
I total=0,s0=0,s1=0,s2=0,s3=0,eligible=0,ex=0;
for(int d=lo;d<=hi;d+=2){int m=(d-2)/2,a=(4*d*d+4)/5,b=4*d*d/3;I c0=0,c1=0,c2=0,c3=0,e=0;
for(int q=a;q<=b;q++){int u=q+d,p=lp[u];bool ok0=p<=2*d+2;if(!ok0){I f=64;for(int c:{-61,13,61,-29,0,16})f=(f*d+c)%p;ok0=f==0;}if(!ok0)continue;c0++;
if(lp[u+1]>2*d+3)continue;c1++;int p2=lp[2*u+1];if(p2>2*d+3&&(4*d+1)%p2)continue;c2++;
int p3=lp[q+m+2];bool ok3=p3<=2*d+3;if(!ok3){e++;I f=96;for(int c:{496,644,4,1015,1751,2356,5316})f=(f*m+c)%p3;ok3=f==0;}c3+=ok3;}
cout<<d<<' '<<b-a+1<<' '<<c0<<' '<<c1<<' '<<c2<<' '<<e<<' '<<c3<<'\n';total+=b-a+1;s0+=c0;s1+=c1;s2+=c2;s3+=c3;eligible+=e;ex+=c2-c3;}
cout<<"total "<<total<<' '<<s0<<' '<<s1<<' '<<s2<<' '<<eligible<<' '<<s3<<" excluded "<<ex<<'\n';}
```
root.py SHA256 4dd77aa9e8ca59537b17e02e6f44977309f4a7692b04bfeb0816be8f870d24a0
```python
# Exact outward fixed-point interval proof on the original JR rational carrier.
# No floating point is used to certify a sign. All legal evaluated factors positive.
from math import isqrt
T=1<<96

def ceildiv(a,b): return -(-a//b)
def mul(x,y): return (x[0]*y[0],x[1]*y[1])
def scale(x,a,b=1): return (x[0]*a//b,ceildiv(x[1]*a,b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def pref(n,d):
    r=[(T,T)]
    for i in range(d):r.append(scale(r[-1],n-i,n+i+3))
    return r

def sign(q,d):
    u=q+d;n=2*q+d;J=2*u*(2*u+1);L=4*n+2
    U,N=pref(u,d),pref(n,d);V=Q=A=(0,0)
    # V,Q,A use denominator T^2; E is rescaled exactly from T.
    for k in range(d+1):
        l=d-k;a=scale(mul(U[k],N[l]),(k+1)*(l+1))
        b=scale(mul(U[k],N[l-1]),(k+1)*l) if l else (0,0)
        V=add(V,a);Q=add(Q,b);A=add(A,scale(add(a,b),(u-k)*(u+k+2),J))
    E=scale(U[d],T*q*(2*d+3)*(n+2),2*(2*u+1)*L)
    W=add(A,E);Z=add(scale(A,q),add(V,Q))
    P=scale(mul(W,Q),3*q*(4*q+3*d+1)**2)
    M=scale(mul(Z,Z),32*(3*q+d+1))
    lo,hi=P[0]-M[1],P[1]-M[0]
    return (1 if lo>0 else -1 if hi<0 else 0),lo,hi

def fast(q,d):
    u=q+d;n=2*q+d;J=2*u*(2*u+1);L=4*n+2
    def r(v):
        a=[1.]
        for i in range(d):a.append(a[-1]*(v-i)/(v+i+3))
        return a
    U,N=r(u),r(n);V=Q=A=0.
    for k in range(d+1):
        l=d-k;a=(k+1)*(l+1)*U[k]*N[l];b=(k+1)*l*U[k]*N[l-1] if l else 0.
        V+=a;Q+=b;A+=(u-k)*(u+k+2)*(a+b)/J
    E=U[d]*q*(2*d+3)*(n+2)/(2*(2*u+1)*L);Z=q*A+Q+V
    return 3*q*(4*q+3*d+1)**2*(A+E)*Q-32*(3*q+d+1)*Z*Z

for d in range(3001,3101):
    lo=4*d*d//5;hi=(4*d*d+2)//3
    while hi-lo>1:
        mid=(hi+lo)//2
        if fast(mid,d)>0:lo=mid
        else:hi=mid
    a,al,ah=sign(lo,d);b,bl,bh=sign(hi,d)
    assert a==1 and b==-1 and hi==lo+1,(d,lo,hi,a,b)
    # margin bounds in integer units of T^4; signs entirely exact.
    print(d,lo,hi,al,bh)
print('PASS d=3001..3100 count=100 exact outward fixed-point consecutive brackets')
```
scan.txt SHA256 88dc13459e30debbb5fe549b2035a21acf4f2c5a5edddea058d4a992a0f2fbf5
```text
3002 4806402 1691980 569755 143870 93709 50161
3004 4812809 1694646 570773 144126 91799 52327
3006 4819220 1697357 571590 144296 94770 49526
3008 4825634 1699615 572262 144433 93282 51155
3010 4832054 1701079 572572 144510 90731 53779
3012 4838477 1702916 573045 144570 94339 50231
3014 4844905 1705874 574206 144897 94416 50481
3016 4851337 1707500 574583 144943 91124 53833
3018 4857773 1710519 575704 145289 93654 51635
3020 4864214 1712068 576380 145468 96484 48984
3022 4870658 1715408 577673 145902 94655 51247
3024 4877108 1717422 578224 146049 96040 50009
3026 4883561 1720131 579311 146309 91660 54649
3028 4890018 1722024 579817 146427 96776 49651
3030 4896481 1723933 580363 146438 95458 51005
3032 4902946 1725802 581166 146670 94864 51808
3034 4909417 1728501 581963 146846 95814 51032
3036 4915892 1731190 583034 147164 94370 52794
3038 4922370 1733105 583833 147392 95142 52250
3040 4928854 1735815 584615 147639 93970 53669
3042 4935341 1737732 585115 147698 94950 52748
3044 4941833 1740500 586456 148203 96576 51627
3046 4948329 1743119 587230 148352 95539 52813
3048 4954829 1745013 587763 148432 97641 50791
3050 4961334 1747722 588846 148748 97205 51560
3052 4967842 1749658 589360 148805 95304 53501
3054 4974356 1751512 589854 148890 97083 51829
3056 4980873 1754245 590892 149168 95910 53258
3058 4987394 1756152 591338 149237 97190 52051
3060 4993921 1759149 592550 149697 93452 56246
3062 5000450 1761249 593198 149741 98241 51500
3064 5006985 1762702 593834 149980 99667 50313
3066 5013524 1766334 595169 150370 96856 53514
3068 5020066 1768178 595628 150417 98138 52279
3070 5026614 1770079 596392 150675 95621 55057
3072 5033165 1772806 597184 150826 97699 53127
3074 5039721 1775295 598158 151117 97342 53775
3076 5046281 1777466 598767 151218 97626 53592
3078 5052845 1779404 599270 151313 98724 52589
3080 5059414 1781310 600093 151560 96672 54913
3082 5065986 1784071 600863 151788 94537 57251
3084 5072564 1785976 601302 151776 100391 51385
3086 5079145 1788717 602432 152119 100442 51677
3088 5085730 1790649 602909 152239 98928 53311
3090 5092321 1792600 603496 152334 99757 52585
3092 5098914 1794493 604038 152463 99250 53213
3094 5105513 1797041 604728 152602 98966 53651
3096 5112116 1798347 604973 152568 96592 55976
3098 5118722 1801119 606381 153064 100066 53006
3100 5125334 1803885 607480 153461 100392 53074
total 248251592 87413408 29436568 7432099 4809814 2622438 excluded 4809661
```

## Next

Investigate the odd-d boundary B=(d-m)(-1)^d R_m(d) as an exact valuation coordinate and whether it yields a bounded-degree or otherwise small-height exception restriction. Generalize the finite signed-moment transfer to other special second-branch values only where the joint weights remain polynomial in k; do not repeat JO's general evaluator as a new result. The even septic gives a new independent large-prime witness but the smooth composite intersection remains a genuine unbounded obstacle. Combine normalized whole-composite constraints with localized integer candidates, preserving every removed factor and its valuation. Full all-budget finite closure 3..3100; all d>=81 unique real root; unbounded integer non-equality open. No formal Task, Result, Review, or native transfer asserted.
