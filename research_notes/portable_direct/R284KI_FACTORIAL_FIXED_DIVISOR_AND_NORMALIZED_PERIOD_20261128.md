# R284KI — Factorial fixed divisors and normalized integer-valued period sieve

2026-11-28. Author proof, local C++ and Python exact computations; NOT_REVIEWED. Auxiliary arithmetic of R284, not native spatial transfer. Own recovery r1-20261128-1300-own-recovery confirms original open RESEARCHER session r1-20261124-0256-r284gd-session-v1, no formal own runs; EM-DIRECT-0C386E / TASK_RESEARCH / RA-B82240E8488EF5A1DA5186C4. LEASED inventory original request r1-20261128-1300-owner-read SUCCEEDED after an intermediate unknown read outcome; as-of 2026-11-28T05:00:46.220069Z, no LEASED entries, Source 2235136cdaa2b2a695d651dabb87486bf017215d (head changed by completion). No shared task/claim mutation. Global canonical entries verified at immutable main 977a8f098dd687b5682b54c1c656aaf32ab60002. P000 V4/V5, ACTIVE worldview, joint observer/residual contracts, portable and current method read; scientific inputs unchanged.

Frozen science: KH dce843c8122f19c67b790b9ed8c639ccba8b511e:research_notes/portable_direct/R284KH_COMPOSITE_POWER_JETS_AND_HERMITE_BLOCK_20261128.md; KG 0c5c18b5e6725fcdebad3c12b9ebec33659ba12f:research_notes/portable_direct/R284KG_SEXTIC_POLE_FIBER_AND_PRIMITIVE_COMPOSITE_SIEVE_20261128.md; JR 88211c0912397b00536b6c4d6427cab29d4499f2:research_notes/portable_direct/R284JR_GLOBAL_BUDGET_POLYNOMIAL_AND_INTEGER_ROOT_EXCLUSION_20261127.md; KD 544d7a97fa075fe62848ae1cf27acdb9bdc7df19:research_notes/portable_direct/R284KD_FINITE_BRIDGE_AND_MODULAR_FALLBACK_20261128.md (unique root and certified root bracket as used in KG/KH). No independent review of these inputs claimed.

## 1. Uniform factorial fixed divisor (proof)

Use JR's exact cleared observations with u=q+d, n=2q+d, l=d-k, S_v(k)=product_{i<k}(v-i) product_{k<=i<d}(v+i+3). For all integer v, including negative v (generalized integral binomial coefficients),
S_v(k)=k!(d-k)! binom(v,k) binom(v+d+2,d-k).
Let t_k=(k+1)!(d-k)!, 0<=k<=d, and put
    g_d = gcd_{0<=k<d} t_k = (d+2)!/lcm(1,2,...,d+2).
This is a new scalar fixed-divisor normalization for R284, not a claim of a new general binomial LCM identity. The identity follows by setting m=d+2, n0=m-1. For a prime p, a=floor(log_p m), b=v_p(m), the maximum v_p(binom(n0,r)) is a-b: Legendre's formula counts terms where r mod p^j > n0 mod p^j; for j<=b or j>a there are none, and r=p^a-1 attains all j=b+1,...,a (if a=b all valuations are zero). Thus gcd of r!(n0-r)! for 1<=r<=n0-1 has p-valuation v_p(m!)-a. Endpoints r=0,n0 do not change the gcd. In the zero-carry case no attaining interior index is required. Also t_d=(d+1)! is a multiple of g_d.

The a_k branch integer weights after binomial extraction are t_k*t_l; the b_k branch weights are t_k^2 for l>=1. The endpoint U[d]D_n has weight (d!)^2. Consequently every individual branch summand, including the endpoint, is divisible in value by g_d^2 at every integer q. In fact g_d^2 is the exact gcd of these factorial weights, since the b_k weights include every t_k^2 with k<d. It is not asserted to be the exact fixed divisor of any whole sum. The signed joint sums v,b,a and Wn,Qn,Zn from JR are all divisible by g_d^2, so
    g_d^4 | P_d(q) for all q in Z.
This is a fixed divisor of values, not necessarily a coefficient content divisor; keep P, all removed factors, and the original sign/zero equivalence on legal positive q. It is valid for smooth composite coordinates as well as prime ones. For example d=3001 gives v_2(g)=2983, v_3(g)=1492, v_5(g)=744, hence baseline exponents 11932,5968,2976. No factorial-scale integer needs to be constructed for the modular evaluator.

## 2. Exact remaining fixed divisor and a short period after normalization

For any integer-valued rational polynomial T of degree <=N, Newton expansion T(q)=sum_{i=0}^N Delta^i T(0) binom(q,i) has integer coefficients in this basis. Thus the gcd of all integer values equals gcd(T(0),...,T(N)): one direction immediate, other follows from integer differences and integral generalized binomial values. Apply to T=P_d/g_d^4, N=4d+9 (JR). Write delta_d=gcd(T(Z)), a positive integer since P is nonzero. For each p the exact remaining fixed divisor exponent e_p=v_p(delta_d) is the minimum valuation over the N+1 consecutive inputs, with zero values treated as infinite. It can be computed from P/p^(4 v_p(g_d)) mod p^s if a residue achieves valuation <s; if all vanish the answer is only >=s. Dividing by the remaining fixed divisor produces another integer-valued polynomial. For a single prime it suffices to divide by p^(4 v_p(g_d)+e_p), retaining p-units. This is an exact zero-preserving normalization on integer inputs, with full carrier retained.

Period theorem: for any integer-valued polynomial F of degree <=N and s>=1, F(q+p^(s+floor(log_p N)))=F(q) mod p^s, for all q in Z. Proof via Newton and Vandermonde: for T0=p^(s+floor(log_p N)), v_p(binom(T0,i))>=s for 1<=i<=N, from i*binom(T0,i)=T0*binom(T0-1,i-1). Hence every shifted binomial difference vanishes mod p^s. This period does not depend on the size of the removed fixed divisor. Applying the period to the normalized polynomial, not to the unnormalized numerator before division, is essential.

Whole-composite version: for h>0, L_N=lcm(1,...,N), the gcd of binom(h,i), 1<=i<=N, equals h/gcd(h,L_N). The lower bound follows from the same identity. For each p|h, choose i=p^min(v_p(h),floor(log_p N)); binom(h-1,i-1) is a p-unit by the digit/carry formula (or product valuation), proving equality. Thus F(q+h)-F(q) is divisible by h/gcd(h,L_N); more generally a Newton truncation at degree t-1 leaves a multiple of gcd_{t<=i<=N} binom(h,i). This is a normalized whole-composite necessary root test, with no prime-independence assumption. It differs from KH's ordinary integer-coefficient power jets: denominators of the binomial basis must be paid; one cannot divide an integer-coefficient jet by a fixed divisor and still assume its coefficients integral. No extra sieve advantage from the whole-composite Newton truncation has yet been executed on R284.

## 3. Actual exact results

Local Python exact prefix/suffix integer implementation computed the complete delta_d (gcd after removing g_d^4) for d=81..120, using q=0..4d+9, all 40 completed. The columns are d, v2(delta), v3(delta), v5(delta), v7(delta), v11(delta):
81 29 10 6 8 4
82 19 8 7 6 4
83 23 12 4 4 4
84 22 12 4 6 4
85 29 9 8 8 4
86 17 11 8 8 0
87 23 14 8 8 0
88 21 6 6 8 2
89 31 10 6 6 2
90 21 10 8 4 2
91 27 8 8 6 4
92 26 16 8 8 4
93 31 16 6 8 4
94 15 13 6 8 4
95 21 15 8 8 4
96 17 18 8 2 4
97 27 10 8 0 0
98 18 14 2 2 0
99 21 14 4 4 2
100 22 11 4 4 2
101 29 16 6 4 2
102 17 18 6 4 4
103 23 13 4 2 4
104 20 15 4 0 4
105 31 18 6 4 4
106 21 6 6 6 4
107 25 12 7 6 4
108 26 10 4 6 0
109 33 8 4 6 0
110 17 12 8 4 2
111 23 14 8 2 2
112 19 11 8 4 2
113 29 13 6 6 4
114 20 16 6 7 4
115 27 8 8 6 4
116 24 12 8 6 4
117 33 14 8 4 4
118 19 10 6 2 4
119 25 17 6 5 0
120 22 18 8 8 0
Raw complete integer gcd output SHA256 f10688df3f6f7854b393a8ff5fd3e8c4d03a42c9643c2b70101dc445043c4e82, reproduced by Python below. Example delta_81=2056834688146869651808125140519121244351867578731858905549627970225495156239816823144448000000. A sample q=1..40 would not prove the fixed divisor and for some d gave too-high minima; full degree+1 inputs are required.

New domain d=3001, q from ceil(4d^2/5) to floor(4d^2/3) as carried in KG/KH. C++ normalized period sieve executed:
d=3001 initial=4803201
p=2 g=2983 extra=51 period=16384 zero_classes=16380 remaining=4802028
p=3 g=1492 extra=13 period=19683 zero_classes=19671 remaining=4799102
p=5 g=744 extra=10 period=15625 zero_classes=15605 remaining=4792958
The original run timed out during p=7; no result for that prime claimed. For the three completed primes the exact total fixed-divisor exponents of P are 11983,5981,2986. Their period sieve excludes 10243 of 4803201 bracket budgets cumulatively, with no independence assumption. No claim of disjointness with KG's earlier exclusions, no new all-budget d closure. The low exclusion rate is an informative negative result: removing the entire fixed divisor of values at a prime still leaves large sets of normalized zero classes. Use variable structural factors or different observers, not just more globally normalized small-prime tests.

Independent crosscheck: exact Python carrier vs C++ valuation/unit recurrence for 15 distinct (d,q) in {81,120,3001} x {0,1,17,100,10000}, each at p=2,3,5 and s=54,33,23 respectively; all 45 exact residues matched. Local output SHA256 e553dfee1b82778309475d8762882af18b3dfcc65f8f53849a3dc6705bc044fe. The evaluator uses nonnegative q only (all linear factors positive, no zero factor valuation ambiguity); theorem extends to all integer q by integer-valued representation. With fixed small p^s<2^54 (or equal for p=2), signed sums fit int64; odd-prime products use signed __int128; power-of-2 products use uint64 wrap and mask, which preserves the low bits exactly. No floating-point decisions. Costs O(d) modular operations per evaluation, plus factor-stripping divisions; N+1 samples and each complete period require O(d^2) such operations at fixed p, not a general bit-complexity guarantee.

## 4. Reproduction (executed local code)

Python exact fixed divisor (source SHA256 4797a31c1491975f4ce4d91c8a22b5ab2ba34165d467d565e02fe3f6c1e73a3e):
```python
from math import factorial,gcd,lcm

def carrier(d,q):
    u=q+d;n=2*q+d
    def S(v):
        tail=[1]*(d+1)
        for k in range(d-1,-1,-1):tail[k]=tail[k+1]*(v+k+3)
        pre=1
        for k in range(d+1):
            tail[k]*=pre;pre*=v-k
        return tail
    U,N=S(u),S(n);v=b=a=0
    for k in range(d+1):
        l=d-k;A=(k+1)*(l+1)*U[k]*N[l];B=(k+1)*l*U[k]*N[l-1] if l else 0
        v+=A;b+=B;a+=(u-k)*(u+k+2)*(A+B)
    J=2*u*(2*u+1);L=4*n+2;W=L*a+u*U[d]*N[0]*q*(2*d+3)*(n+2);Q=J*L*b;Z=L*(q*a+J*(b+v));return 3*q*(4*q+3*d+1)**2*W*Q-32*(3*q+d+1)*Z**2

def val(x,p):
    if not x:return 999999
    k=0
    while x%p==0:x//=p;k+=1
    return k

def fixed(d):
    B=(factorial(d+2)//lcm(*range(1,d+3)))**4
    D=0; n=4*d+9
    for q in range(n+1):
        P=carrier(d,q);a,r=divmod(P,B);assert r==0
        D=gcd(D,a)
        if D==1:break
    return D

if __name__=='__main__':
    for d in range(81,121):
        f=fixed(d);print(d, f, *(val(f,p) for p in [2,3,5,7,11]),flush=True)
```

C++ source (original local SHA256 17eb8c889483a05a03d02c6f63bca431c3720d14917553edddf204fc222dc3af; replay g++ -O3 -std=c++17 r284ki_sieve.cpp -o r284ki_sieve; ./r284ki_sieve 3001 3001; p=7 may take longer than the original budget):
```cpp
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using I=int64_t;
struct Pair{int v; I u;};
struct Eval {
 int d,p,s,g; I mod,period; std::vector<I> pw; std::vector<Pair> U,N,tail,weights; 
 Eval(int d_,int p_,int s_):d(d_),p(p_),s(s_),g(0),mod(1),period(1),pw(s+1),U(d+1),N(d+1),tail(d+1),weights(d+2){
  pw[0]=1;for(int i=1;i<=s;i++)pw[i]=pw[i-1]*p;mod=pw[s];
  I m=d+2;while(m){m/=p;g+=m;}for(I a=p;a<=d+2;a*=p)g--;
  period=mod;for(I a=p;a<=d;a*=p){if(period>INT64_MAX/p){period=0;break;}period*=p;}
  for(int k=1;k<=d+1;k++)weights[k]=split(k);
 }
 I mul(I a,I b)const{if(p==2)return (I)((uint64_t(a)*uint64_t(b))&uint64_t(mod-1));return (I)((__int128(a)*b)%mod);}
 Pair split(I x)const{assert(x>0);int v=0;while(x%p==0){x/=p;v++;}return {v,x%mod};}
 Pair prod(Pair a,Pair b)const{return {a.v+b.v,mul(a.u,b.u)};}
 void branch(I v,std::vector<Pair>& out){tail[d]={0,1};for(int k=d-1;k>=0;k--)tail[k]=prod(tail[k+1],split(v+k+3));Pair pre={0,1};for(int k=0;k<=d;k++){out[k]=prod(pre,tail[k]);if(k<d)pre=prod(pre,split(v-k));}}
 I norm(Pair a)const{int e=a.v-2*g;assert(e>=0);return e>=s?0:mul(a.u,pw[e]);}
 I operator()(I q){I u=q+d,n=2*q+d;branch(u,U);branch(n,N);I v=0,b=0,a=0;
  for(int k=0;k<=d;k++){int l=d-k;I A=norm(prod(prod(U[k],N[l]),prod(weights[k+1],weights[l+1]))),B=l?norm(prod(prod(U[k],N[l-1]),prod(weights[k+1],weights[l]))):0;
   v=(v+A)%mod;b=(b+B)%mod;a=(a+mul(mul((u-k)%mod,(u+k+2)%mod),(A+B)%mod))%mod;}
  I J=mul(2*u%mod,(2*u+1)%mod),L=(4*n+2)%mod;
  I ep=norm(prod(U[d],N[0]));for(I x:{u,q, I(2*d+3),n+2})ep=mul(ep,x%mod);
  I W=(mul(L,a)+ep)%mod,Q=mul(mul(J,L),b),Z=mul(L,(mul(q%mod,a)+mul(J,(b+v)%mod))%mod),F=(4*q+3*d+1)%mod;
  I r=(mul(mul(mul(3*q%mod,mul(F,F)),W),Q)-mul(mul(32%mod,(3*q+d+1)%mod),mul(Z,Z)))%mod;return (r+mod)%mod;
 }
};
int main(int argc,char**argv){int lo=argc>1?atoi(argv[1]):3001,hi=argc>2?atoi(argv[2]):3003;for(int d=lo;d<=hi;d++){I low=(4LL*d*d+4)/5,high=4LL*d*d/3;std::vector<I> cand;for(I q=low;q<=high;q++)cand.push_back(q);std::cout<<"d="<<d<<" initial="<<cand.size()<<std::endl;for(int p:{2,3,5,7}){int s=p==2?54:p==3?33:p==5?23:19;Eval e(d,p,s);int min=s;for(int q=0;q<=4*d+9;q++){I x=e(q);int v=0;while(v<s&&x%p==0){v++;x/=p;}min=std::min(min,v);}if(min==s){std::cout<<"saturated p="<<p<<std::endl;continue;}Eval z(d,p,min+1);I period=p;for(I a=p;a<=4*d+9;a*=p)period*=p;std::vector<char> pass(period);I count=0;for(I q=0;q<period;q++){pass[q]=(z(q)==0);count+=pass[q];}auto end=std::remove_if(cand.begin(),cand.end(),[&](I q){return !pass[q%period];});cand.erase(end,cand.end());std::cout<<"p="<<p<<" g="<<e.g<<" extra="<<min<<" period="<<period<<" zero_classes="<<count<<" remaining="<<cand.size()<<std::endl;if(cand.empty())break;}}}
```

Crosscheck driver (compile including the above file under the indicated filename):
```cpp
#define main old_main
#include "r284ki_sieve.cpp"
#undef main
int main(){for(int d:{81,120,3001})for(int q:{0,1,17,100,10000})for(int p:{2,3,5}){int s=p==2?54:p==3?33:23;Eval e(d,p,s);std::cout<<d<<' '<<q<<' '<<p<<' '<<s<<' '<<e.g<<' '<<e(q)<<'\n';}}
```
Read its output rows d,q,p,s,g,r in Python; assert divmod(carrier(d,q),p**(4*g))[1]==0 and (carrier(d,q)//p**(4*g))%(p**s)==r. Actual 45/45 matched.

## Next

Normalize KG's H rather than raw P at each integer q, paying the variable valuations of every removed factor (not just scalar fixed divisors), then seek a useful normalized modular exclusion on smooth composite fibers. Combine with KH power jets only with exact division or sufficient valuation payment. Use KD's root-location observer to reduce candidate load if global sieve is not efficient. The current data disfavor brute-force small-prime period expansion alone; do not repeat the already completed p=2,3,5 scans or claim the interrupted p=7 scan. KD finite exclusion d=3..3000, JY/JZ subpower sparsity and KG/KH constraints retain prior scope. All-parameter integer exclusion open.
