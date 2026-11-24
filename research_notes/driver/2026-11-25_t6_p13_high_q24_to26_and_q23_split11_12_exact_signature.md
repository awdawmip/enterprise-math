# T6 p13: high vertical-order signature exclusion, q24–26 and q23 split(11,12)
2026-11-25, Driver lane EM-DVR-DEBB5E. New author-side exact computation, not independent review of own result or native acceptance. Frozen scientific source d84bd940cfb093cdc60e569f15cad58772a51dca, original H0..H6 and independent side mass caps 2331. Preserve original authors including EM-DIRECT-D03BC9 and prior q10 audit d4b2a7149f7c33ff4e9b0c0d2a762dc59de9b6e8. No re-execution of q10 signed split audit.

## Proposition and proof reduction
Conditional on maximum remaining denominator prime 13 and cancellation of denominators divisible by 13^2 (upstream reduction not reproved here), the remaining 13-layer atoms are d=13u, u=13q+r, q>=0, 1<=r<=12, u 13-smooth. Each occurrence costs d-1=169q+13r-1. After cancellation of common named atoms, let Q_A,Q_B be sums of q on each side. Each Q<=13 since 169*14>2331; both sum to at most 26. For k=1..6 the original H0..H6 equalities imply equality of reciprocal moments via the invertible triangular binomial relation. After multiplying the kth reciprocal identity by 13^k and reducing in the localization at 13, non-13 denominators vanish and the necessary signature of the full valuation-one profile is F=(sum u^{-k} mod 13^k)_{k=1..6}. We retain horizontal q=0 atoms, multiplicities, and all actual denominators. Lower-prime completion and H0 are not assumed away; a necessary-signature contradiction suffices in the stated scope.

For a fixed Q enumerate all nondecreasing multisets from the 78 admissible (q,r) atoms with q<=13 and sum q=Q and residual cost sum(13r-1)<=2331-169Q. All contributions positive in cost; enumerate including empty horizontal part and all repetitions. Suffix minimum-cost DP prunes only impossible q completion. Separate unbounded coin DP counts every multiset by q and residual cost; it matches all completed DFS counts. Signature key uses mixed radix 13^1,...,13^6; largest key <13^21<2^128. Each modular multiplication uses int64 (13^12<2^63). Low three components are a lossless necessary prefilter; all surviving lookups compare full keys.

## Executed results
|Q|profiles enumerated|independent DP|DFS nodes|
|---|---:|---:|---:|
|13|5775|5775|6914|
|12|2583672|2583672|2611639|
|11|100750914|100750914|100831156|

|split|low-three matches (query profiles)|full match or duplicate|
|---|---:|---:|
|13,13|not used|0 adjacent equal keys|
|12,13|2066|0|
|12,12|not used|0 adjacent equal keys|
|11,13|97885|0|
|11,12|33312848|0|

Same-Q injectivity forces identical entire valuation-one profiles, hence an empty 13-layer after named cancellation. Different-Q disjoint signatures exclude equality even without the disjoint-support filter. Thus q26 (13,13), q25 (12,13), q24 (11,13 and 12,12) fully excluded up to sign, and q23 split(11,12) excluded. q>=27 impossible under both caps. q23 split(10,13) remains open: independent DP count 1328547997 profiles at Q=10, but attempted full DFS did not complete before the tool timeout; no output or partial negative result is claimed. The first C++ run covering q24–26 completed in 2.74 seconds with peak RSS 72108 KiB; second run returned complete q11/12 result before timeout in the subsequent q10/13 traversal. Independent JS execution also matched Q13/Q12 counts and the 2066 low-three matches/zero full matches. No new p13 global, other-q, upstream or T6 mother closure. Current Task read dvr-20261125-0000-t6-current-read-v1 SUCCEEDED, HANDOFF_READY/NEEDS_DISPATCH, no active owner; its formal p17 q14 reviewer preflight is distinct and not taken over. The new high-order computation is portable scientific work, not a native claim or formal review.

## Reproduction (C++17)
Compile g++ -O3 -std=c++17 -Wall -Wextra. The following is the executed completed-domain code, with the interrupted Q10 traversal omitted. 
```cpp
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
using U=__uint128_t; using I=uint64_t;
constexpr int P=13,B=2331,QMAX=13; constexpr array<int,6> M={13,169,2197,28561,371293,4826809};
struct Atom{int q,r,w;array<int,6>s;}; vector<Atom> atoms;
int inv(int a,int m){int64_t x=0,y=1,b=m;while(a){int t=b/a;int z=b-t*a;b=a;a=z;int64_t u=x-t*y;x=y;y=u;}assert(b==1);return (x%m+m)%m;}
bool smooth(int a){for(int p:{2,3,5,7,11,13})while(a%p==0)a/=p;return a==1;}
int modadd(int a,int b,int m){int s=a+b;return s>=m?s-m:s;}
U key(const array<int,6>&s){U k=0;for(int j=5;j>=0;j--)k=k*M[j]+s[j];return k;}
int low(const array<int,6>&s){return s[0]+13*(s[1]+169*s[2]);}
vector<array<int,14>> mn;
void init(){for(int q=13;q>=0;q--)for(int r=1;r<13;r++)if(smooth(13*q+r)){Atom a{q,r,13*r-1,{}};for(int j=0;j<6;j++){int v=inv(13*q+r,M[j]);int64_t t=1;for(int k=0;k<=j;k++)t=t*v%M[j];a.s[j]=t;}atoms.push_back(a);}assert(atoms.size()==78);int n=atoms.size();mn.resize(n+1);mn[n].fill(100000);mn[n][0]=0;for(int i=n-1;i>=0;i--){mn[i][0]=0;for(int q=1;q<=13;q++){mn[i][q]=mn[i+1][q];int a=atoms[i].q;if(a&&q>=a)mn[i][q]=min(mn[i][q],atoms[i].w+mn[i][q-a]);}}}
I dpcount(int Q){int C=B-169*Q;vector<vector<I>>dp(Q+1,vector<I>(C+1));dp[0][0]=1;for(auto&a:atoms)for(int q=a.q;q<=Q;q++)for(int c=a.w;c<=C;c++)dp[q][c]+=dp[q-a.q][c-a.w];I n=0;for(I k:dp[Q])n+=k;return n;}
template<class F>void dfs(int i,int q,int c,const array<int,6>&s,I& count,I&nodes,F& consume){nodes++;if(q==0){count++;consume(s);}for(int j=i;j<(int)atoms.size();j++){const auto&a=atoms[j];if(a.q>q||a.w>c||mn[j][q-a.q]>c-a.w)continue;array<int,6>t;for(int k=0;k<6;k++)t[k]=modadd(s[k],a.s[k],M[k]);dfs(j,q-a.q,c-a.w,t,count,nodes,consume);}}
template<class F>void run(int Q,F consume){I count=0,nodes=0;dfs(0,Q,B-169*Q,{},count,nodes,consume);I expected=dpcount(Q);assert(count==expected);cout<<"Q="<<Q<<" profiles="<<count<<" DP="<<expected<<" nodes="<<nodes<<endl;}
I dup(vector<U>& v){sort(v.begin(),v.end());I d=0;for(size_t i=1;i<v.size();i++)d+=v[i]==v[i-1];return d;}
int main(){init();vector<U>v13,v12;vector<uint8_t>filter(4826809),filter12(4826809);run(13,[&](const auto&s){v13.push_back(key(s));filter[low(s)]=1;});I d13=dup(v13);cout<<"13/13 adjacent_duplicate="<<d13<<endl;I c1213=0,f1213=0;run(12,[&](const auto&s){U k=key(s);v12.push_back(k);filter12[low(s)]=1;if(filter[low(s)]){f1213++;c1213+=binary_search(v13.begin(),v13.end(),k);}});I d12=dup(v12);cout<<"12/13 low3_matches="<<f1213<<" full_matches="<<c1213<<"; 12/12 adjacent_duplicate="<<d12<<endl;I c1113=0,f1113=0,c1112=0,f1112=0;run(11,[&](const auto&s){if(filter[low(s)]){f1113++;c1113+=binary_search(v13.begin(),v13.end(),key(s));}if(filter12[low(s)]){f1112++;c1112+=binary_search(v12.begin(),v12.end(),key(s));}});cout<<"11/13 low3_matches="<<f1113<<" full_matches="<<c1113<<endl;cout<<"11/12 low3_matches="<<f1112<<" full_matches="<<c1112<<endl;}
```
