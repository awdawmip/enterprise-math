# EC49FYP — maximal optional holes and uniform five/six-hole obstructions

2026-11-24; independent portable continuation of Research-4 historical provenance EM-DIRECT-23537B (current private binding unconfirmed). Frozen input BRC16943, exact 50 masks from [FYO](https://github.com/awdawmip/enterprise-math/blob/3f81ac0627e5e9eb696d3fda4940557219d20345/research_notes/portable_direct/EC49FYO_ZERO_PREFIX_RESIDUAL_OBSTRUCTION.md). Auxiliary Boolean observer W(U,H)(t,j)=1[t in U]1[j not in H], m>h, |H|<=h, distinct nonempty supports, deterministic exact identification, unit-cost probes. No new native X6 attribution or foundation change.

## Theorem and proof

For this frozen family, Q_5(m)>=m+7 for m>=6 and Q_6(m)>=m+8 for m>=7. Together with FYM's parent-dependent upper bound c_h<=2h this gives 7<=c_5<=10 and 8<=c_6<=12. FYO's cases h=3,4 are reproduced. The proof applies to arbitrary m, not extrapolation.

Use the FYO prefix residual inequality. For a prefix of d distinct zero probes, with column masks M_j, define mandatory hole set J(U)={j:M_j intersects U}; a low-hole target exists iff |J(U)|<=h-1 for some U. For such U, optional holes are columns disjoint from U. Write b=|J(U)|. For every admissible H containing J(U), its prefix excess lower bound is d-b+tau_U(N), where N is the union of masks of live touched columns and tau_U(N) is the least number of extra rows hitting every strict-superset difference not already hit by N. Optional holes contribute no mandatory-in-support query credit. Tau is antitone in N: a larger previously hit set can never increase the remaining minimum. Thus increasing H by an optional hole weakly increases the bound, and it is sufficient to enumerate optional hole sets of maximum allowed size min(h-1-b,k-b), where k is touched column count. This maximization is exact for the FYO low-hole bound, not a quotient of the full observer state. No discarded optional subset can have a stronger bound than one of its maximal extensions. This reduction is valid for arbitrary finite support families under the stated observer model.

As in FYO, enumerate canonical sorted column-mask multisets with arbitrary fresh columns, keeping prefixes with a compatible low-hole target and no target whose excess exceeds c. Every compatible low-hole target requires a further probe: changing a live column to a hole preserves the all-zero history. Count successors with no such target separately as escapes, never as contradictions. Repeated physical probes may be removed without increasing worst depth. At depth d=c+h, every compatible low-hole target already incurs excess >=d-(h-1)=c+1, so no survivors are possible there. A finite search ending with no survivors AND zero escapes at every layer rules out all depth m+c trees for all m>h. Arbitrarily many fresh columns enlarge the prefix domain; actual finite-m prefixes are contained. The enumeration below closes both (h,c)=(5,6),(6,7). It does not close (3,5), which has 935 distinct escape prefixes at depth 8. A high-hole continuation or constructive search is needed there.

## Executed exact C++17 verifier

Compile g++ -O3 -std=c++17 fyp.cpp -o fyp; run ./fyp h c. Each row is h,c,depth,distinct successors tested,survivors,distinct escapes. Integer popcounts, unions and finite enumeration only. Largest depth 11 here; no shift exceeds 11. The 1024 row-mask universe is exhaustive. Actual local execution code:

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;
const int F[]={23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005};
int pc[1024], tau[50][1024];
using S=vector<int>;
struct Hash{size_t operator()(S const& a)const{size_t h=0;for(int x:a)h=h*1031+x;return h;}};
int bound(S const&a,int h,int c,int d){bool exists=false;for(int i=0;i<50;i++){int u=F[i],must=0;S b;for(int x:a){if(x&u)must++;else b.push_back(x);}if(must>=h)continue;exists=true;int extra=d-must;if(extra>c)return 1;int keep=max(0,(int)b.size()-(h-1-must)); // tau monotone: enough to use maximum optional holes
int n=b.size();for(int mask=0;mask<(1<<n);mask++){if(__builtin_popcount((unsigned)mask)!=keep)continue;int z=0;for(int j=0;j<n;j++)if(mask>>j&1)z|=b[j];if(extra+tau[i][z]>c)return 1;}}
return exists?0:-1;}
int main(int argc,char**argv){for(int x=0;x<1024;x++)pc[x]=__builtin_popcount((unsigned)x);for(int i=0;i<50;i++){vector<int> ds;for(int v:F)if(v!=F[i]&&(v&F[i])==F[i])ds.push_back(v^F[i]);for(int z=0;z<1024;z++){int best=10;for(int t=0;t<1024;t++){if(pc[t]>=best)continue;bool ok=true;for(int d:ds)if(!(d&(z|t))){ok=false;break;}if(ok)best=pc[t];}tau[i][z]=best;}}
int h=atoi(argv[1]),c=atoi(argv[2]);unordered_set<S,Hash> layer;layer.insert(S{});for(int d=1;d<=c+h;d++){unordered_set<S,Hash> seen,next;long long escape=0;for(auto const&a:layer)for(int j=0;j<=(int)a.size();j++){if(j>0&&j<(int)a.size()&&a[j]==a[j-1])continue;for(int t=0;t<10;t++){int bit=1<<t;S q=a;if(j==(int)a.size())q.push_back(bit);else{if(a[j]&bit)continue;q[j]|=bit;}sort(q.begin(),q.end());if(!seen.insert(q).second)continue;int v=bound(q,h,c,d);if(v<0)escape++;else if(v==0)next.insert(q);}}cout<<h<<","<<c<<","<<d<<","<<seen.size()<<","<<next.size()<<","<<escape<<endl;layer.swap(next);if(layer.empty())break;}}
```

Actual output:
```csv
3,4,1,10,10,0
3,4,2,100,24,0
3,4,3,388,37,0
3,4,4,989,30,0
3,4,5,947,9,0
3,4,6,414,2,0
3,4,7,128,0,0
4,5,1,10,10,0
4,5,2,100,100,0
4,5,3,790,388,0
4,5,4,3813,322,0
4,5,5,7563,406,0
4,5,6,11487,168,0
4,5,7,7522,19,0
4,5,8,1128,10,0
4,5,9,723,0,0
5,6,1,10,10,0
5,6,2,100,100,0
5,6,3,790,790,0
5,6,4,5635,3813,0
5,6,5,29376,4943,0
5,6,6,71506,3529,0
5,6,7,89454,1845,0
5,6,8,67765,575,0
5,6,9,30362,8,0
5,6,10,560,6,0
5,6,11,487,0,0
6,7,1,10,10,0
6,7,2,100,100,0
6,7,3,790,790,0
6,7,4,5635,5635,0
6,7,5,36604,29376,0
6,7,6,195457,62033,0
6,7,7,590515,34632,0
6,7,8,679002,22376,0
6,7,9,636537,5549,0
6,7,10,255550,1118,0
6,7,11,64419,0,0
3,5,1,10,10,0
3,5,2,100,100,0
3,5,3,790,495,0
3,5,4,4835,1438,0
3,5,5,19536,2691,0
3,5,6,53492,3066,0
3,5,7,83319,4056,0
3,5,8,144693,0,935
```

## Next and status

Try a finite three-hole m+5 decision tree, or study the 935 escape prefixes using full-h-hole state certificates (the m mandatory probe argument does not hold unchanged when |H|=h). General h+2 lower bound remains a conjecture beyond h=6. The maximal optional-hole reduction is an exact adversarial-bound quotient and should be reused instead of enumerating every subset. No formal task/Result/Review or shared claim: exact lookup r4-20261124-1030-ec49as-task-read-v1 SUCCEEDED, Source 51168b3c14924f02c7c299b581c9b55395ba8f49, NO_CANONICAL_PUBLICATION_DIRECTORY (limited directory observation only). Historical identity provenance preserved, current private writer binding unconfirmed. AUTHOR_PROVED / EXACT_FINITE_INTEGER_ENUMERATION / PARENT_DEPENDENT / NOT_REVIEWED.
