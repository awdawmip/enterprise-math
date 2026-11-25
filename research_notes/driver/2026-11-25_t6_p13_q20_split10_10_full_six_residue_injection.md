# T6 p13 q20(10,10): full finite six-residue injection

2026-11-25 · Existing Driver EM-DVR-DEBB5E · author-side computation, NOT_REVIEWED. Continue revision 569; no earlier search repeated.

## Proposition and proof

Use the same cancellation-normalized valuation-one p13 domain and mass cap 2331 on each side as the [q20(9,11) continuation](https://github.com/awdawmip/enterprise-math/blob/e9ec4c51cb05a52e0a97d9cfe47a699b6b31d0f5/research_notes/driver/2026-11-25_t6_p13_q20_split9_11_c651_810_hash_index.md). A once-13-divisible atom d=13u has u=13q+r, 1<=r<=12, u 13-smooth, and mass d-1=169q+13r-1. On each side Q=sum q=10; residual budget B=641. The remaining lower-prime denominators may be arbitrary 13-free denominators consistent with original budgets. Higher valuation/common cancellation assumptions retained.

Equality of full shape observers H0..H6 implies equality of inverse moments S1..S6 by the triangular binomial transform. Multiplying S_k equality by 13^k gives equality of R_k(U)=sum u^(-k) mod 13^k on both sides, since all 13-free terms vanish modulo 13^k. For Q=10 enumerate each multiset exactly once as vertical P and horizontal H using nondecreasing indices, repeating species allowed, residual weights <=641. Partition by R1(U)=b in 0..12. For each P only the horizontal bucket R1(H)=b-R1(P) mod13 is needed, including all H with w(H)<=641-w(P). Sort exact tuple (R4,R5,R6,R2,R3) for each b. The high field uses 15+19+23 bits with no overlap, the low field uses 8+12 bits with no overlap. The first component is implicit in b. Adjacent equal keys detect every collision, including collisions between different vertical or horizontal rosters. No approximate filter. Distinct rosters are emitted once, so all-zero collision counts prove injectivity on the full finite one-side domain. Thus the two multisets must be identical; opposite cancellation precludes nonempty equal sides with Q=10. In fact even the four residues 1,4,5,6 are injective, as every bucket has zero adjacent equal high keys. This excludes the exact q20(10,10) one-power subcase even with arbitrary 13-free completion. It does not close the historical missing raw logs of q20(9,11), lower layers, or global T6.

## Actual local computation

g++ -O3 -march=native -std=c++17 /tmp/q10.cpp -o /tmp/q10
Five successful /usr/bin/time -v runs: arguments 0 0, 1 3, 4 6, 7 9, 10 12. Each exit status 0. P=306988, H=729803, total=1328547997. Exact output rows:
```
bucket 0 profiles 102174220 high_adjacent_equal 0 six_adjacent_equal 0 six_pairs 0
bucket 1 profiles 102054983 high_adjacent_equal 0 six_adjacent_equal 0 six_pairs 0
bucket 2 profiles 102198697 high_adjacent_equal 0 six_adjacent_equal 0 six_pairs 0
bucket 3 profiles 102344921 high_adjacent_equal 0 six_adjacent_equal 0 six_pairs 0
bucket 4 profiles 102237785 high_adjacent_equal 0 six_adjacent_equal 0 six_pairs 0
bucket 5 profiles 102045276 high_adjacent_equal 0 six_adjacent_equal 0 six_pairs 0
bucket 6 profiles 102107566 high_adjacent_equal 0 six_adjacent_equal 0 six_pairs 0
bucket 7 profiles 102303330 high_adjacent_equal 0 six_adjacent_equal 0 six_pairs 0
bucket 8 profiles 102307284 high_adjacent_equal 0 six_adjacent_equal 0 six_pairs 0
bucket 9 profiles 102116344 high_adjacent_equal 0 six_adjacent_equal 0 six_pairs 0
bucket 10 profiles 102077575 high_adjacent_equal 0 six_adjacent_equal 0 six_pairs 0
bucket 11 profiles 102253437 high_adjacent_equal 0 six_adjacent_equal 0 six_pairs 0
bucket 12 profiles 102326579 high_adjacent_equal 0 six_adjacent_equal 0 six_pairs 0
```
Wall seconds 10.33,30.19,29.21,29.16,29.84 (sum 128.73); peak RSS 1634768 KiB. Independent ascending-integer Python univariate coin DP counts P=306988, H=729803, full=1328547997. Further NumPy int64 residue DP in reversed atom order independently reproduces each bucket count (all intermediate counts bounded by total within integer range).

## Reproduction source

```cpp
#include <bits/stdc++.h>
using namespace std;using U=uint64_t;using S=array<int,6>;constexpr int M[]={13,169,2197,28561,371293,4826809};
struct A{int q,w;S s;};struct R{int w;S s;};
S add(S x,const S&y){for(int k=0;k<6;k++){x[k]+=y[k];if(x[k]>=M[k])x[k]-=M[k];}return x;}
U key(const S&s){return U(s[3])|(U(s[4])<<15)|(U(s[5])<<34);}
uint32_t tail(const S&s){return uint32_t(s[1])|(uint32_t(s[2])<<8);}
bool smooth(int u){for(int p:{2,3,5,7,11,13})while(u%p==0)u/=p;return u==1;}
int inv(int a,int m){long x=0,y=1;int b=m;while(a){int t=b/a,z=b-t*a;b=a;a=z;long u=x-t*y;x=y;y=u;}assert(b==1);return (x%m+m)%m;}
constexpr int Q=10,B=2331-169*Q;vector<A>a;vector<R>P;array<vector<R>,13>H; U dp[Q+1][B+1][13]{},hp[B+1][13]{};
void pg(int i,int q,int w,S s){if(!q){P.push_back({w,s});return;}for(int j=i;j<(int)a.size();j++)if(a[j].q&&a[j].q<=q&&w+a[j].w<=B)pg(j,q-a[j].q,w+a[j].w,add(s,a[j].s));}
void hg(int i,int w,S s){H[s[0]].push_back({w,s});for(int j=i;j<(int)a.size();j++)if(!a[j].q&&w+a[j].w<=B)hg(j,w+a[j].w,add(s,a[j].s));}
struct K{U hi;uint32_t lo; bool operator<(const K&b)const{return hi<b.hi||(hi==b.hi&&lo<b.lo);}bool operator==(const K&b)const{return hi==b.hi&&lo==b.lo;}};
int main(int argc,char**argv){for(int u=1;u<13*(Q+1);u++){int q=u/13,r=u%13;if(!r||!smooth(u))continue;A t{q,13*r-1,{}};for(int k=0;k<6;k++){long v=inv(u,M[k]),z=1;assert(v*u%M[k]==1);for(int n=0;n<=k;n++)z=z*v%M[k];t.s[k]=z;}a.push_back(t);}pg(0,Q,0,{});hg(0,0,{});for(auto&h:H)sort(h.begin(),h.end(),[](auto&x,auto&y){return x.w<y.w;});
dp[0][0][0]=hp[0][0]=1;for(auto&t:a)if(t.q){for(int j=t.q;j<=Q;j++)for(int w=t.w;w<=B;w++)for(int s=0;s<13;s++)dp[j][w][s]+=dp[j-t.q][w-t.w][(s+13-t.s[0])%13];}else{for(int w=t.w;w<=B;w++)for(int s=0;s<13;s++)hp[w][s]+=hp[w-t.w][(s+13-t.s[0])%13];}
for(int w=1;w<=B;w++)for(int s=0;s<13;s++)hp[w][s]+=hp[w-1][s];U total=0;array<U,13>cnt{};for(int w=0;w<=B;w++)for(int s=0;s<13;s++)for(int h=0;h<13;h++)cnt[(s+h)%13]+=dp[Q][w][s]*hp[B-w][h];for(auto n:cnt)total+=n;cout<<"P "<<P.size()<<" H "<<accumulate(H.begin(),H.end(),U(0),[](U x,const auto&h){return x+h.size();})<<" total "<<total<<"\n";assert(total==1328547997ULL);for(int b=0;b<13;b++)cout<<"count "<<b<<" "<<cnt[b]<<"\n";cout<<flush;
int first=argc>1?atoi(argv[1]):0,last=argc>2?atoi(argv[2]):first;for(int b=first;b<=last;b++){vector<K>keys;keys.reserve(cnt[b]);for(auto&p:P){int s=(b+13-p.s[0])%13,c=B-p.w;for(auto&h:H[s]){if(h.w>c)break;auto t=add(p.s,h.s);assert(t[0]==b);keys.push_back({key(t),tail(t)});}}assert(keys.size()==cnt[b]);sort(keys.begin(),keys.end());U duplicates=0,pairs=0,hiDuplicates=0;size_t run=1;for(size_t i=1;i<keys.size();i++){if(keys[i].hi==keys[i-1].hi)hiDuplicates++;if(keys[i]==keys[i-1]){duplicates++;pairs+=run++;}else run=1;}cout<<"bucket "<<b<<" profiles "<<keys.size()<<" high_adjacent_equal "<<hiDuplicates<<" six_adjacent_equal "<<duplicates<<" six_pairs "<<pairs<<"\n"<<flush;
if(duplicates){for(size_t i=1;i<keys.size();i++)if(keys[i]==keys[i-1])cout<<"duplicate "<<keys[i].hi<<" "<<keys[i].lo<<"\n";cout<<flush;}}
}
```

Independent residue count:
```python
import numpy as np
Q=10;B=641
D=np.zeros((Q+1,B+1,13),dtype=np.int64);D[0,0,0]=1
H=np.zeros((B+1,13),dtype=np.int64);H[0,0]=1
for u in reversed(range(1,143)):
 q,r=divmod(u,13)
 if not r:continue
 t=u
 for p in (2,3,5,7,11,13):
  while t%p==0:t//=p
 if t!=1:continue
 w=13*r-1;s=pow(u,-1,13)
 if q:
  for j in range(q,Q+1):
   D[j,w:]+=np.roll(D[j-q,:B+1-w],s,axis=1)
 else:
  for i in range(w,B+1):H[i]+=np.roll(H[i-w],s)
H=H.cumsum(axis=0)
cnt=[sum(int(D[Q,w,s])*int(H[B-w,(b-s)%13]) for w in range(B+1) for s in range(13)) for b in range(13)]
print(cnt,sum(cnt))
```

New signed split complete at stated mathematical scope. q20(9,11) author history complete but 859902502 raw logs remain missing; q20 full evidence closure pending that limited recovery/verification. Native review, Result, Task, parent completion each zero. Preserve Driver author contribution, not independent review. Onhour other researcher is working q12 per backlog revision489; no overlap.
