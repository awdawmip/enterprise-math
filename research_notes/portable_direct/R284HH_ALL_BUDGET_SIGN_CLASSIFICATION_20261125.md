# R284HH — All-budget sign classification via paid quarter-strip and exact finite complement

2026-11-25. Author proof plus exhaustive exact certificate, NOT_REVIEWED. Same auxiliary binary-tag word-count observer; no native physical attribution. Frozen sources: HG 6c0b1f5a2300f7c6e3194bbd7b572979d7585bad:research_notes/portable_direct/R284HG_COMPLETE_PRE_ONSET_EXCEPTION_CLASSIFICATION_20261125.md; HF b9fda453ef76999e8ec9cbc776e69f715025819a; HE 0e4f8d4318f145100959ca9ec3f41c0e219090d5; HC 36e96070fd5f44cabe0713c9047fb751232f69bc and their HA/GU/GX pins. Preserve all hypotheses; conditional on their author-proved exact count, corridor and HC envelope identities. Current control/behavior entries checked at GK b38517756e62267f0636ff520cbb38e4971a6ed3 and EM 97ac35b8d8c97f62135d07c6d4ae2b8e8fc41d12; P000 V5 and ACTIVE worldview unchanged. Own registration r1-20261124-0256-r284gd-session-v1 SUCCEEDED, own recovery r1-20261125-0705-own-recovery confirmed open/no runs, EM-DIRECT-0C386E / RA-B82240E8488EF5A1DA5186C4. Owner read r1-20261125-0702-owner-read SUCCEEDED, inventory as of 2026-11-24T23:03:23Z at Source 3fd386d8822fcc76867596b702c824aedb11edd6, returned zero LEASED tasks; no live authority asserted (head changed during read). No shared CLAIM.

## Results

For every integer u>=1 and 0<=q<u, K(q,u) is never 1; there is a unique integer cutoff q_max(u)>=0 such that K>1 exactly when q<=q_max(u), and K<1 exactly when q>q_max(u). The latter set is empty at u=1. This proves global uniqueness of the sign transition, not strict monotonicity of K in the entire parameter domain. For u>=10000 use HG; the new finite complement exhaustively certifies all 49,995,000 pairs with 1<=u<=9999, of which only 15,290 need original exact S,P,Q counts. No ties, reversals or budgets without a positive point. The highest budget needing any full count in this certificate is 1151. For 1152<=u<10000, binary search in 0<=q<=floor(u/4) on the sign of the fixed-degree F=N-B exactly finds q_max; no original counts or tie fallback needed there. For u>=10000 use HG's one integer square root and at most three polynomial tests. All counts and comparisons were done with GMP integers; no floating-point decisions.

For f(u)=(isqrt(324*u+121887)-169)//3, all 9999 small budgets are overpredicted, with corrections 2..60 (maximum 60). Combined with HG, the total number of exceptional budgets over ALL positive integers is 599125 = 589126+9999; c=1:583054, c=2:7396, c=3:2915, c>=4:5760. Last exception and permanent onset remain HF's 2522581650951 and 2522581650952. No inference of independent mathematical acceptance.

## Proof: quarter-strip residual payment

Extend HE's exact four-image strip count from q<=u/8 to q<=u/4, integer u>=22. Its three orientations have remaining inventories (a,b,x,t)=(H,3u,1,1),(H-1,3u,0,1),(H-1,3u+1,0,0),(H,3u+1,0,0) with multiplicities 1,q,1,1 respectively; H=u+2q+1. Prefix cut immediately after q-th B is safe because r<=t and b<=q<=h (HE's h is at least 2u). The q=0 term with multiplicity q vanishes. For all four orientations W=b-a+x+t. From 4q<=u, W+2>a and 2(W+2)>b+x+1 by direct substitution. For the HE infinite reflection sum, j<0 is therefore outside the binomial support, and j>=2 likewise; j=0,1 produce exactly L(a,b;x,t). This slightly weaker sufficient image condition replaces HF's W+2>a+x+1.

For a uniform shuffle of the remaining inventory, p=a/(a+b)<=17/50 since a<=3u/2+1, b>=3u and u>=22. The original corridor differs from the strengthened one only by the two corner relaxations as in HE: lower violation after total a>e=A-2q, upper violation while total a<q. Each such segment has length >=u in its respective forward/reversed direction and contains more A than B. For length l, the without-replacement factorial expansion gives E[2^X]<=(1+p)^l; Markov gives (67/(50 sqrt(2)))^l < (19/20)^l (compare squares). The union of all lengths l>=u and both directions costs at most 40*(19/20)^u times the unconstrained shuffle count.

The strip fraction T=1-R_(x+1)-R_(t+1)+R_(x+t+2), R_j=product (a-i)/(b+i+1), is >=1/5. In fact r=R_1<=51/100, and R_2=r^2-r*(1+r)/(b+2). For x=t=0, T=(1-r)^2-r*(1+r)/(b+2) >= (49/100)^2-(51/100)*(151/100)/68 >1/5. For x+t=1, T>=1-r-r^2>1/5; for x=t=1, T>=1-2r^2>1/5. All inventories are positive and large enough for these R_j. Thus each original count differs from its strip count by a nonnegative relative residual at most epsilon(u)=200*(19/20)^u, also after the positive cut multiplicities are summed. Hence exactly

K0/(1+epsilon)^2 <= K <= K0*(1+epsilon)^2,   22<=u, 0<=4q<=u.

This is an observer-specific residual payment. It keeps the underlying branch provenance and does not identify the original path families with the compressed strip for other observations.

## Monotone rational certificate and finite exhaustive complement

Use exactly HF's N,B, F=N-B derived from HE's strip formulas. At u=4q+x, x,q>=0, the derivative numerators N_u B-N B_u and N B_q-N_q B have 187 and 189 strictly positive nonzero coefficients; both are nonzero on each axis. The square-root polynomial of B has 20 strictly positive coefficients there including a positive constant. Exact SymPy calculation below. Therefore K0=N/B strictly decreases with q in the quarter-strip; no assumption of continuous original K. Let D=20^u and C=200*19^u. For each u>=22 define robust-positive when N*D^2>B*(D+C)^2 and robust-negative when N*(D+C)^2<B*D^2. The positive set is an initial interval, the negative set a terminal interval in q<=floor(u/4). Binary-search their endpoints with exact integers, evaluate the intervening undecided q by HA's exact positive moment convolution. Every certified interval is paid by the displayed inequality, no probabilistic numerical tolerance.

For the complement q>floor(u/4), use HC's exact envelope. Let r=(u+2)/(2(2u+1)), t=(m+2)/(2(2m+1)), rho=[6u(u+2)-d(2d+7)]/[12u(2u+1)], b=t(1+3r), W=(J+1)^2/H. HC proves P/S<=b/(1+q*rho), Q/S<=1/(1+q*rho). For u>=2, b decreases, rho increases and W decreases with q; HC also proves Q/S strictly decreases. Consequently either of b*W/(1+q*rho)^2<1 or b*W*(Q/S)/(1+q*rho)<1 certifies the entire suffix starting at that q. The second uses the actual Q/S from a computed exact count at that anchor. Iterate complement q in ascending order until a suffix certificate succeeds, testing remaining points by exact moments. For u<22 use only exact counts and these suffix bounds (u=1 exact only). Every row visits its signed blocks in order, tests for a positive point after a negative, and checks coverage. This is a finite proof certificate over the whole complement, not extrapolation from a sampled window.

## Executed exact reproduction

The following C++17/GMP program was compiled and run with g++ -O3 -std=c++17 r284hh_scan.cpp -lgmpxx -lgmp -o r284hh_scan; ./r284hh_scan 9999. The initial Catalan recurrence is M_n(0)=Catalan_(n+1); all subsequent moment divisions are exact by HA. The source expressions N,B are the factored/expanded HF rational quotient. No floating-point arithmetic.

```cpp
#include <gmpxx.h>
#include <vector>
#include <iostream>
#include <cassert>
#include <map>
#include <algorithm>
using Z=mpz_class;
std::vector<Z> cat;
Z powz(unsigned a,unsigned n){Z z;mpz_ui_pow_ui(z.get_mpz_t(),a,n);return z;}
struct Ratio{Z n,b;};
Ratio surrogate(int U,int Q){Z u=U,q=Q,d=u-q;
 Z N=2*(3*u+4)*(3*u+4)*(q+2*u+1)*(q+3*u+1)*(q+3*u+1)*(2*d*d-5*q+2*u)*(2*d*d-7*q+4*u+3);
 Z z=12*q*q*q*q*u+24*q*q*q*q-18*q*q*q*u*u-44*q*q*q*u-56*q*q*q-33*q*q*u*u-111*q*q*u-54*q*q+6*q*u*u*u*u-6*q*u*u*u-63*q*u*u-55*q*u-10*q+32*u*u*u*u+104*u*u*u+124*u*u+64*u+12;
 return {N,z*z};}
std::vector<Z> moments(int n,int g){std::vector<Z> v(g+1);v[0]=cat[n];for(int k=0;k<g&&k<n;++k){v[k+1]=v[k]*(k+2)*(n-k);mpz_divexact_ui(v[k+1].get_mpz_t(),v[k+1].get_mpz_t(),(unsigned long)(k+1)*(n+k+3));}return v;}
Z conv(const std::vector<Z>&a,const std::vector<Z>&b,int g){Z v=0;for(int k=0;k<=g;++k)mpz_addmul(v.get_mpz_t(),a[k].get_mpz_t(),b[g-k].get_mpz_t());return v;}
struct Counts{Z S,P,Q;};
Counts counts(int u,int q){int d=u-q,m=u+q,g=d+1;auto A=moments(u,g),a=moments(u-1,g),B=moments(m,g),b=moments(m-1,g);Z Q=conv(A,B,d-1);Z S=Q+conv(A,B,d)+q*(conv(a,B,d)+conv(a,B,d-1));Z P=conv(a,b,d+1)+3*conv(a,b,d)+3*conv(a,b,d-1)+conv(a,b,d-2);return {S,P,Q};}
int exactsign(int u,int q,const Counts&c){Z f=c.P*c.Q*(3*u+q+1)*(3*u+q+1)-c.S*c.S*(u+2*q+1);return sgn(f);}
bool suffix(int U,int Q,const Counts* c=nullptr){if(U<2)return false;Z u=U,q=Q,d=u-q,m=u+q;Z a=u+2,b=2*(2*u+1),tn=m+2,td=2*(2*m+1),rn=6*u*(u+2)-d*(2*d+7),rd=12*u*(2*u+1);Z bn=tn*(b+3*a),bd=td*b,fn=rd+q*rn,J=3*u+q+1,H=u+2*q+1;
 if(c)return bn*rd*J*J*c->Q<bd*fn*H*c->S;
 return bn*rd*rd*J*J<bd*fn*fn*H;}
int main(int argc,char**argv){int maxu=argc>1?atoi(argv[1]):9999;cat.resize(2*maxu+1);cat[0]=1;for(int n=0;n<2*maxu;++n){cat[n+1]=cat[n]*2*(2*n+3);mpz_divexact_ui(cat[n+1].get_mpz_t(),cat[n+1].get_mpz_t(),n+3);}
 long long exact=0,paidpos=0,paidneg=0,suffixneg=0,all=0,ties=0,reversals=0,missingpos=0;int maxexactu=0,maxq=0;std::map<int,int> hist;std::vector<int> boundary(maxu+1);
 for(int u=1;u<=maxu;++u){int lo=0,hi=-1;int last=-1;bool seenNeg=false,hasPos=false;
  auto add=[&](int q,int sign){if(sign==0)++ties;if(sign>0){if(seenNeg)++reversals;last=q;hasPos=true;}if(sign<0)seenNeg=true;};
  if(u>=22){int cap=u/4;Z den=powz(20,u),num=200*powz(19,u);Z dn=den*den,up=(den+num)*(den+num);
   auto robust=[&](int q){auto v=surrogate(u,q);if(v.n*dn>v.b*up)return 1;if(v.n*up<v.b*dn)return -1;return 0;};
   int a=-1,b=cap+1;while(b-a>1){int m=(a+b)/2;if(robust(m)==1)a=m;else b=m;}lo=b;paidpos+=lo;
   a=-1;b=cap+1;while(b-a>1){int m=(a+b)/2;if(robust(m)==-1)b=m;else a=m;}hi=b;paidneg+=cap+1-hi;
   assert(lo<=hi);if(lo>0)add(lo-1,1);
   for(int q=lo;q<hi;++q){auto c=counts(u,q);add(q,exactsign(u,q,c));++exact;maxexactu=u;}
   if(hi<=cap)add(hi,-1);
   lo=cap+1;
  }
  for(int q=lo;q<u;++q){if(suffix(u,q)){suffixneg+=u-q;add(q,-1);break;}auto c=counts(u,q);++exact;maxexactu=u;int sign=exactsign(u,q,c);add(q,sign);if(suffix(u,q,&c)){assert(sign<0);suffixneg+=u-q-1;break;}}
  if(!hasPos)++missingpos;boundary[u]=last;maxq=std::max(maxq,last);all+=u;
  Z a=324*Z(u)+121887,root;mpz_sqrt(root.get_mpz_t(),a.get_mpz_t());int f=(root.get_si()-169)/3;
  ++hist[f-last];
  if(u%1000==0||u==maxu)std::cerr<<"u "<<u<<" exact "<<exact<<" pos "<<paidpos<<" neg "<<paidneg<<" suffix "<<suffixneg<<" ties "<<ties<<" reversals "<<reversals<<" qmax "<<last<<"\n";
 }
 assert(exact+paidpos+paidneg+suffixneg==all);std::cout<<"coverage "<<all<<" exact "<<exact<<" paidpos "<<paidpos<<" paidneg "<<paidneg<<" suffixneg "<<suffixneg<<" ties "<<ties<<" reversals "<<reversals<<" missingpos "<<missingpos<<" maxexactu "<<maxexactu<<" maxq "<<maxq<<"\n";
 for(auto [d,n]:hist)std::cout<<"correction "<<d<<" count "<<n<<"\n";
 for(int u:{1,2,3,4,8,16,32,64,128,256,512,1000,2000,4096,8192,9999})if(u<=maxu)std::cout<<"boundary "<<u<<" "<<boundary[u]<<"\n";
 assert(!ties&&!reversals&&!missingpos);
}
```

Actual output summary:
coverage 49995000 exact 15290 paidpos 3573356 paidneg 8930561 suffixneg 37475793 ties 0 reversals 0 missingpos 0 maxexactu 1151 maxq 552
Correction distribution: c=2:1417; c=3:2822; c=4..60:5760 in total (each individual count is printed by the reproduction). No c=0,1 or c>60.
Selected boundary (u:qmax): 1:0,2:0,3:1,4:2,8:5,16:9,32:16,64:27,128:43,256:67,512:103,1000:153,2000:228,4096:340,8192:496,9999:552. All 9999 budgets have correction>=2; c2=1417, c3=2822, c>=4=5760.

Independent exact SymPy/Fraction check (executed, outputs 187,189,20 and 5457 orientation checks):
```python
import sympy as s
from math import comb
from fractions import Fraction as F
u,q,x=s.symbols('u q x');H=u+2*q+1;D=H+3*u;J=3*u+q
def T(a,b,x,t):
    def R(k):return s.prod((a-j)/(b+j+1) for j in range(k))
    return 1-R(x+1)-R(t+1)+R(x+t+2)
S=T(H,3*u,1,1)+q*H/D*T(H-1,3*u,0,1);P=H/(3*u+1)*T(H-1,3*u+1,0,0);Q=(D+1)/(3*u+1)*T(H,3*u+1,0,0)
N,B=map(s.expand,s.fraction(s.factor(P*Q*(J+1)**2/(S*S*H))))
for G in (s.diff(N,u)*B-N*s.diff(B,u),N*s.diff(B,q)-s.diff(N,q)*B):
    p=s.Poly(G.subs(u,4*q+x),x,q);assert all(c>0 for c in p.coeffs());assert p.eval(q,0).as_expr()!=0 and p.eval(x,0).as_expr()!=0;print(len(p.terms()))
base=s.factor(B).base
p=s.Poly(base.subs(u,4*q+x),x,q);assert all(c>0 for c in p.coeffs());print(len(p.terms()))
def moments(n,g):
    a=[comb(2*n+2,n)//(n+1)]
    for k in range(g):a.append(a[-1]*(k+2)*(n-k)//((k+1)*(n+k+3)) if k<n else 0)
    return a
def counts(u,q):
    d=u-q;m=u+q;g=d+1
    A,a,B,b=(moments(n,g) for n in (u,u-1,m,m-1))
    def C(a,b,g):return sum(a[k]*b[g-k] for k in range(g+1)) if g>=0 else 0
    Q=C(A,B,d-1);S=Q+C(A,B,d)+q*(C(a,B,d)+C(a,B,d-1));P=sum(comb(3,j)*C(a,b,d+1-j) for j in range(4));return S,P,Q
def strip(a,b,x,t):
    def c(j):return comb(a+b,j) if 0<=j<=a+b else 0
    W=b-a+x+t;assert W+2>a and 2*(W+2)>b+x+1
    return c(a)-c(a-x-1)-c(a-t-1)+c(a-x-t-2)
def strip_counts(u,q):
    H=u+2*q+1;return strip(H,3*u,1,1)+q*strip(H-1,3*u,0,1),strip(H-1,3*u+1,0,0),strip(H,3*u+1,0,0)
check=0
for U in range(22,121):
    eps=200*F(19,20)**U
    for Q in range(U//4+1):
        for full,short in zip(counts(U,Q),strip_counts(U,Q)):
            assert 0<short<=full and F(full-short,short)<=eps;check+=1
print(check)
```

## Next
Global sign-transition classification now complete at author-proof scope conditional on frozen dependencies. Do not repeat the 49,995,000-point proof or trillion-scale HG classification. The distinct global strict-monotonicity question remains open outside the proved strips; seek a joint moment-ratio inequality controlling P/S increases (HC counterexample rules out separate monotonicity globally). Quarter-strip derivative certificates permit an improved exact adjacent-comparison payment on unbounded u with explicit integer threshold; derive sharper payments using pointwise derivative gaps. Independently review the frozen dependencies and full certificate as appropriate; no formal Task/Result admission or review claimed.
