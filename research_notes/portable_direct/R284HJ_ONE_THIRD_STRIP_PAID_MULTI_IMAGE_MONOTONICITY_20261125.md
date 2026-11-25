# R284HJ — One-third strip: paid additional reflection images and strict monotonicity

2026-11-25. Author proof with exact finite certificates, NOT_REVIEWED. Auxiliary binary-tag word-count observer only. Frozen HH f9b8351559e49b13fbe70faad67d87e1b84fa9b9:research_notes/portable_direct/R284HH_ALL_BUDGET_SIGN_CLASSIFICATION_20261125.md, HE 0e4f8d4318f145100959ca9ec3f41c0e219090d5:research_notes/portable_direct/R284HE_EXPONENTIAL_PORT_STRIP_AND_EVENTUAL_EXACT_ROUNDING_20261125.md and HA/HF pins as in HH. Concurrently published HI 02360937e02ffd533a6d8c5ff669d62441145aec:research_notes/portable_direct/R284HI_ALL_QUARTER_STRIP_STRICT_MONOTONICITY_20261125.md was read before publication; its quarter-strip result is not counted as new. P000 V5, ACTIVE worldview and joint observer preservation read. Own registration r1-20261124-0256-r284gd-session-v1 SUCCEEDED; recovery r1-20261125-0807-own-recovery confirmed same open session, no runs; EM-DIRECT-0C386E, RA-B82240E8488EF5A1DA5186C4. Owner read r1-20261125-0807-owner-read SUCCEEDED, snapshot 74b0fa4d1604c69bc8e6a76bea221d508f426f3c as of 2026-11-25T00:08:31.230303Z, no LEASED tasks. Independent research, no shared CLAIM.

## Result

For all integer u>=1, q>=0, K(q,u)>K(q+1,u) if 3(q+1)<=u, and K(q,u+1)>K(q,u) if 3q<=u. These extend HI's quarter-strip to one third of the budget. The proof below is conditional on the frozen exact path/corridor and moment-count identities. Outside this band and HB's fixed diagonal strips, global q monotonicity remains open.

## Paid extra reflection images

Retain HE corridor, orientations, cut and inventories, with a,b denoting post-cut totals. The four (a,b,x,t) are (H,3u,1,1),(H-1,3u,0,1),(H-1,3u+1,0,0),(H,3u+1,0,0), H=u+2q+1, weighted 1,q,1,1. The prefix cut is valid in the larger band (q<=u/3 and h>=2u); q=0 uses only the initial cut. The strip width W=b-a+x+t; write w=W+2 and n=a+b. The exact strengthened strip count R is the complete HE image sum:
R=sum over integer j of [C(n,a+jw)-C(n,a-x-1+jw)].
The j=0,1 terms alone give the four-term L of HE/HH. Now additional images can be nonzero; they are retained as a bounded signed residual, not treated as zero. For u>=48 and 3q<=u, a<=5u/3+1, b>=3u, p=a/n<=9/25, r=a/(b+1)<=9/16<3/5 and w>=u. For k>=0, C(n,a-k)/C(n,a)<= (3/5)^k, interpreting out-of-support binomials as zero. For j<=-1 both image indices are at most a-|j|w. For j>=2 use binomial symmetry; the indices become a-(j-1)w-x-t-2 and a-(j-1)w-t-1, both <=a-(j-1)w. Thus
|R-L|/C(n,a)<=4*(3/5)^w/(1-(3/5)^w)<=8*(3/5)^u.
This is valid even with actual extra images.

The original safe count O contains the full strip count R. Its two possible corner relaxations are those in HE: lower violation after a_total>e=A-2q, upper violation while a_total<q. The relevant forward/reverse segments have length >=u (e-r_cut>=u and A-q>=u) and contain more A than B. The same factorial expansion E[2^X]<=(1+p)^l gives probability <=((34/25)/sqrt(2))^l < (97/100)^l (compare squares). Union over both directions and lengths >=u: 0<=O-R<= (200/3)*(97/100)^u*C(n,a). These are separate residuals: omitted signed strip images and excluded positive corner mass.

The four-term L divided by C(n,a) is T=1-R_(x+1)-R_(t+1)+R_(x+t+2), R_k=product_(i=0..k-1)(a-i)/(b+i+1). For x=t=0, T=(1-r)^2-r*(1+r)/(b+2)>1/10 since r<=9/16 and b>=144. For x+t=1, T>=1-r-r^2>=31/256>1/10. For x=t=1, T>=1-2r^2>1/10. Therefore |O-L|<=750*(97/100)^u L. Positive prefix multiplicities preserve this bound for each of S,P,Q relative to the four-term sums S0,P0,Q0, even though the signs of their individual differences are not assumed.

Let eps=750*(97/100)^u. For eps<1,
K0*((1-eps)/(1+eps))^2 <= K <= K0*((1+eps)/(1-eps))^2.
No original path-level equality or other observer preservation is asserted.

## Quantitative surrogate gap on 3q<=u

Use HH's exact N,B expressions for the four-term quotient K0=N/B. In coordinates u=3q+x, x,q>=0, N and B respectively have 54 and 63 positive nonzero coefficients (minima 96,36). In the same coordinates let A=N B_q-N_q B, C=N_u B-N B_u, where derivatives here are at fixed original u or q respectively. Exact polynomial multiplication verifies (q+3)A-NB has 207 positive coefficients, minimum 46656; (u+1)C-NB has 204 positive coefficients, minimum 27648. Thus -partial_q log K0>1/(q+3), partial_u log K0>1/(u+1). Integration along the endpoint intervals (only rational surrogate is continuously extended) gives strict separation K0(q,u)/K0(q+1,u)>(q+4)/(q+3) and K0(q,u+1)/K0(q,u)>(u+2)/(u+1). For u>=490 both lower bounds are at least 1+1/(u+1) in the relevant strip.

Both real K endpoint comparisons pay at most ((1+eps)/(1-eps))^4 using eps at the smaller u. At u=490, eps=0.00024729256193623575 (display only), the exact rational payment gap is 0.0019802987425756213 < 1/491=0.002036659877800407. The exact test first succeeds at 490 among u>=48 with eps<1. Propagate: ((1+eps)/(1-eps))^4-1=8eps(1+eps^2)/(1-eps)^4; when eps shrinks by 97/100 this expression shrinks by at least that factor. Multiplication by u+1 still decreases for u>=490. The infinite tail follows.

## Exact finite complement and additional-image check

Computed every row u=1..490 with q=0..floor(u/3), using HA moments and GMP exact integer cross products. All q edges with u<490: 39772 comparisons, including 10004 outside HI's quarter strip. All u edges from u=1..489: 40261 comparisons, including 10004 outside HI. No failures. Extra image check u=48..120, floor(u/4)<q<=floor(u/3), all four orientations: 2056 checked; 1966 have nonzero extra image residual R-L. Every test satisfies 10L>=C(n,a) and |R-L|<=8*(3/5)^u*C(n,a). This specifically demonstrates why the old exact four-image identity must not be extrapolated.

## Reproduction: symbolic and image certificates

```python
import sympy as s
from fractions import Fraction as F
from math import comb
u,q,x=s.symbols('u q x');d=u-q
N=2*(3*u+4)**2*(q+2*u+1)*(q+3*u+1)**2*(2*d*d-5*q+2*u)*(2*d*d-7*q+4*u+3)
z=12*q**4*u+24*q**4-18*q**3*u**2-44*q**3*u-56*q**3-33*q*q*u*u-111*q*q*u-54*q*q+6*q*u**4-6*q*u**3-63*q*u*u-55*q*u-10*q+32*u**4+104*u**3+124*u*u+64*u+12
B=z*z
n=s.Poly(N.subs(u,3*q+x),x,q);b=s.Poly(B.subs(u,3*q+x),x,q)
a=n*(b.diff(q)-3*b.diff(x))-(n.diff(q)-3*n.diff(x))*b
c=n.diff(x)*b-n*b.diff(x)
for p in (n,b,s.Poly(q+3,x,q)*a-n*b,s.Poly(3*q+x+1,x,q)*c-n*b):
    assert min(p.coeffs())>0
    print(len(p.terms()),min(p.coeffs()))
for U in range(48,2000):
    e=750*F(97,100)**U
    if e<1 and ((1+e)/(1-e))**4<1+F(1,U+1):break
assert U==490
checks=nonzero=0
for U in range(48,121):
    for Q in range(U//4+1,U//3+1):
        H=U+2*Q+1
        for a,b,x,t in [(H,3*U,1,1),(H-1,3*U,0,1),(H-1,3*U+1,0,0),(H,3*U+1,0,0)]:
            n=a+b;w=b-a+x+t+2
            def c(j):return comb(n,j) if 0<=j<=n else 0
            L=c(a)-c(a-x-1)-c(a-t-1)+c(a-x-t-2)
            R=sum(c(a+j*w)-c(a-x-1+j*w) for j in range(-n//w-2,n//w+3));M=c(a)
            assert 10*L>=M and abs(R-L)<=8*F(3,5)**U*M
            nonzero+=R!=L;checks+=1
assert (checks,nonzero)==(2056,1966)
```

Executed finite complement: g++ -O3 r284hj_scan.cpp -lgmpxx -lgmp -o r284hj_scan && ./r284hj_scan
```cpp
#include <gmpxx.h>
#include <vector>
#include <iostream>
#include <cassert>
using Z=mpz_class;
std::vector<std::vector<Z>> M;
Z conv(const std::vector<Z>&a,const std::vector<Z>&b,int g){Z z=0;for(int k=std::max(0,g-int(b.size())+1);k<=std::min(g,int(a.size())-1);++k)mpz_addmul(z.get_mpz_t(),a[k].get_mpz_t(),b[g-k].get_mpz_t());return z;}
struct Ratio{Z n,b;};
Ratio ratio(int u,int q){int d=u-q,m=u+q;auto &A=M[u],&a=M[u-1],&B=M[m],&b=M[m-1];Z Q=conv(A,B,d-1),S=Q+conv(A,B,d)+q*(conv(a,B,d)+conv(a,B,d-1)),P=conv(a,b,d+1)+3*conv(a,b,d)+3*conv(a,b,d-1)+conv(a,b,d-2);return {P*Q*(3*u+q+1)*(3*u+q+1),S*S*(u+2*q+1)};}
int main(){M.resize(655);Z cat=1;for(int n=0;n<int(M.size());++n){auto &a=M[n];a.resize(n+1);a[0]=cat;for(int k=0;k<n;++k){a[k+1]=a[k]*(k+2)*(n-k);assert(mpz_divisible_ui_p(a[k+1].get_mpz_t(),(unsigned long)(k+1)*(n+k+3)));mpz_divexact_ui(a[k+1].get_mpz_t(),a[k+1].get_mpz_t(),(unsigned long)(k+1)*(n+k+3));}cat=cat*2*(2*n+3)/(n+3);}
std::vector<Ratio> prev;long qc=0,uc=0,qn=0,un=0;for(int u=1;u<=490;++u){std::vector<Ratio> row;for(int q=0;q<=u/3;++q){row.push_back(ratio(u,q));auto &a=row.back();if(u<490&&q){auto &b=row[q-1];assert(b.n*a.b>a.n*b.b);++qc;qn+=4*q>u;}if(q<int(prev.size())){auto &b=prev[q];assert(a.n*b.b>b.n*a.b);++uc;un+=4*q>u-1;}}prev=std::move(row);}std::cout<<qc<<" "<<uc<<" "<<qn<<" "<<un<<"\n";}
```
Output: 39772 40261 10004 10004. All strict comparisons passed.

## Next

Extend to fixed fractional bands closer to q=u by using an optimized sampling-without-replacement exponential bound (rather than fixed E[2^X]) and shifted polynomial derivative certificates; eventually the strip width and drift become small near q=u and the exponential-tail mechanism must connect to exact moment transport/diagonal estimates. Preserve the extra image and corner residual types separately. Global monotonicity remains the mother question; no repeat of the sign classification or HI quarter strip is needed.
