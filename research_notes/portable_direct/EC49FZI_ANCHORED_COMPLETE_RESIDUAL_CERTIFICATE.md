# EC49FZI — Anchored complete residual certificates and three-probe quotient

2026-11-25. Parent: f894becbadec26b083c1a3da5807b8391223c463:research_notes/portable_direct/EC49FZH_TWO_PROBE_RESIDUAL_CLASSIFICATION.md, blob caf141abd13734ddc5ba30af50a327741780b5bc. Same frozen BRC16943 auxiliary Boolean observer, 50 supports, physical column labels, W(r,j)=1[r in U]1[j not in H], |H|<=h<m. No native X6 attribution. Use FZH's 29 surviving two-probe suffix types; its excluded types are not reopened.

## 1. Exact complete true-state certificate after a positive anchor

Let X be any compatible state set after a known positive probe (r0,j0); thus r0 belongs to every U and j0 is live in every H. Fix x=(U,H) in X. Let T be a set of row features and L a set of column features. Require for each y=(V,K) != x in X that T intersects U xor V or L intersects H xor K. Then the exact minimum number of additional probes on the path for x sufficient to separate it from **all** other states in X is

C_full(x) = min over such (T,L) [ max(|T intersect U|, |L minus H|) + |T minus U| + |L intersect H| ].

Proof (lower bound): Each positive probe on x forces its row membership and its column liveness. Collect the rows and columns of the positive probes. Each negative probe has at least one zero feature on x; select one of its zero features. Every rival distinguished by that negative probe must have both features one, so the selected feature differs on that rival. Every rival distinguished by a positive probe differs on at least one of its two collected features. Hence the resulting T,L hit every rival difference. The number of distinct positive row features and positive column features is each at most the number of positive probes; the number of selected negative features is at most the number of negative probes. The objective is no larger than the probe count.

Upper bound: Realize the positive features by pairing arbitrary positive rows with positive columns, filling unequal lengths using the known anchor row or column. Each such probe is positive on x and implies both feature values on every state consistent with its answer. Observe each negative row via the anchor column and each negative column via the anchor row. These probes force their corresponding zero features. They identify x by the hitting condition and use exactly the displayed budget (or fewer if redundant; the lower bound gives equality at the optimum). Thus the minimum is exact. This also proves C_full(x) >= FZH's restricted certificate: the latter covers only same-H support competitors and same-U single-column neighbors. Mixed competitors generally require additional observations.

A concrete strict example: on two rows and two columns, X={(U={0,1}, H=empty), (U={0},H={1})}, common positive anchor (0,0). For x equal to the first state FZH's restricted certificate is 0, while C_full=1 because the mixed rival is excluded by e.g. probe (1,1).

This is a true-state-path certificate, not an exact adaptive worst-case depth formula. For any compatible branch depth k, max_x C_full(x)<=k is necessary. Negative-probe replacement is used only to prove true-state certificate cost, not to assert preservation of arbitrary two-child adaptive query behavior.

Exact computation: use one bit per row and one bit per physical column. For each rival form a nonempty difference mask E=(U xor V) union (H xor K shifted by row count). Choose a hitting set with the above monotone cost. Singleton masks force their bits; discard hit edges and supersets of retained edges (hitting a subset hits its superset). At each search node choose an uncovered edge and branch on adding one of its bits; prune cost above k. This is exhaustive since every solution extends at least one branch. Memoize only fully failed sets at a fixed k. Start k at the prior restricted certificate, and increase until feasible. Every reported exact cost was established by integer search.

## 2. Lossless quotient of three-probe residual branches

For a zero-prefix mask inventory p and a positive probe (r,j), first remove its row bit from p[j] (it is not constrained zero). The residual branch has a distinguished live column j, positive row r, and the remaining zero-prefix masks. Its key is (r,p[j],sorted multiset of p[l] for l != j). Equal keys induce a label permutation that fixes the distinguished column and carries all zero constraints and the positive constraint bijectively. It carries U unchanged, H by permutation, and every future probe by that permutation. Thus it preserves all adaptive decision-tree depths, not just counts or current readouts. Keep the ordered suffix paths in the fiber for future reverse extension; no claim of equivalence of suffix histories themselves.

From FZH's 29 surviving suffixes, 420 ordered three-probe types reduce to 348 distinct keys, with 50..1453 labeled states per key. Enumerate all 348 keys, no new sample or support family. There are 182416 labeled states summed across keys. Budget for the third-last-positive branch is m-h+3=14.

Exact complete certificate computation at the roots:
- all 182416 states evaluated; no root excluded by max C_full>14; largest C_full=14.
- 129054 state certificates strictly exceed the previous restricted FZH certificate; all 348 keys have at least one strict improvement.
- 855919 certificate search calls, including unsuccessful lower budgets.
- examples (key ID, state count, strict state count, first strict state index, old/new costs): (0,50,45,1,1,2); (1,76,61,1,1,2); (2,116,100,1,1,2); (4,129,94,0,0,1); (9,168,139,1,1,3). State index is zero-based in physical() order.

Exact adaptive decision recursion (FZH mandatory-column/superset pruning, larger bitset, same full branch replay):
- pass 1 cap=2000 calls per key: 47 feasible, 301 capped, 0 exhausted negative; 626048 calls; 10322 replayed states.
- pass 2 on capped keys only: cap=20000 for n<=300 else 5000. Combined latest terminal outcomes: 78 feasible, 270 capped/unresolved, 0 exhausted negative; 18934 replayed labeled states across feasible keys. Latest-per-key calls sum 1746387 (not cumulative across both passes). A cap is UNKNOWN, never an impossibility proof.
- feasible key IDs (zero-based, sorted as generator below): 0..43 inclusive,45..61 inclusive,68,70,71,72,73,74,76,79,80,81,83,89,90,91,132,143,145.
- lifting results back to ordered histories gives 97 feasible third-positive branches and 323 unresolved. By final suffix type, feasible/unresolved: (3,1) 18/66; (192,6) 27/107; (320,6) 30/83; (320,8) 22/67.
- All positive results replay actual W(r,j) on every input state. Feasible third-positive branch does not alone establish a complete prefix strategy.
- M14 remains 25<=M14<=27; FZF finite exception closure count 35/82 remains unchanged.

## 3. Reproduction (Python 3 and C++17)

Generate keys and exact states (save gen.py; output input.txt; IDs sorted by (n,key,paths,states), key unique):
```python
from itertools import combinations
import json,sys
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
MS=[s for s,n in [(1,4),(2,2),(3,2),(4,4),(8,1),(144,2),(192,2),(256,3),(320,2),(512,3)] for _ in range(n)]
SURV={(3,1):[(1,0),(3,0),(4,2),(144,7),(320,6),(320,8)],(192,6):[(1,0),(3,0),(4,2),(8,3),(128,7),(144,7),(192,7),(256,8),(320,8)],(320,6):[(3,1),(4,2),(8,3),(144,4),(144,7),(192,7),(256,8),(320,8)],(320,8):[(3,1),(64,6),(144,7),(192,6),(320,6),(512,9)]}
def physical(p,h,r,j):
 m=len(p);out=[]
 for u in F:
  if not(u>>r&1) or p[j]&u:continue
  req=sum(1<<i for i,s in enumerate(p) if s&u)
  if req.bit_count()>h:continue
  free=[i for i in range(m) if not req>>i&1 and i!=j]
  for k in range(min(h-req.bit_count(),len(free))+1):
   for cc in combinations(free,k):out.append((u,req|sum(1<<i for i in cc)))
 return out
def types(p):
 for j,s in enumerate(p):
  if s in p[:j]:continue
  for r in range(10):
   if s>>r&1:yield j,r
keys={}
for last,pen in SURV.items():
 p=MS.copy();p[p.index(last[0])]^=1<<last[1]
 for t in pen:
  q=p.copy();q[q.index(t[0])]^=1<<t[1]
  for j,r in types(q):
   z=q.copy();z[j]^=1<<r
   key=(r,z[j],tuple(sorted(z[:j]+z[j+1:])))
   keys.setdefault(key,[]).append((last,t,(q[j],r)))
cases=[]
for key,paths in keys.items():
 r,mask,other=key; st=physical([mask,*other],14,r,0);cases.append((len(st),key,paths,st))
cases.sort()
assert sum(len(x[2]) for x in cases)==420 and len(cases)==348
with open('cases.json','w') as f:json.dump([[n,key,paths] for n,key,paths,st in cases],f)
print(len(cases))
for i,(n,key,paths,st) in enumerate(cases):
 print(i,n,25,14,int(sys.argv[1]) if len(sys.argv)>1 else 2000)
 for u,h in st:print(u,h)
```

Complete certificate program cert.cpp (actual algorithm; output columns id,n,excluded-state-or-minus1,checked,maxexact,strict,first-strict-state,old,new,nodes):
```cpp
#include <bits/stdc++.h>
using namespace std; using W=uint64_t; int pc(W x){return __builtin_popcountll(x);}
struct Cert{W pr,pcoll,nr,nc; vector<W> edges; unordered_set<W> fail; long long nodes=0; int k;
 int cost(W x){return max(pc(x&pr),pc(x&pcoll))+pc(x&nr)+pc(x&nc);}
 bool go(W x){++nodes;if(cost(x)>k)return false;if(fail.count(x))return false;W e=0;int sz=100;for(W y:edges)if(!(y&x)&&pc(y)<sz){e=y;sz=pc(y);if(sz==1)break;}if(!e)return true;vector<pair<int,W>>v;while(e){W b=e&-e;e-=b;v.push_back({cost(x|b),b});}sort(v.begin(),v.end());for(auto[c,b]:v)if(c<=k&&go(x|b))return true;fail.insert(x);return false;}
};
int main(){int cases;cin>>cases;while(cases--){int id,n,m,k,cap;cin>>id>>n>>m>>k>>cap;vector<pair<int,int>>s(n);for(auto&[u,h]:s)cin>>u>>h;int found=-1,checked=0,maxexact=0,strict=0,ex=-1,exOld=-1,exNew=-1;long long nodes=0; W mask=(W(1)<<m)-1;
 for(int i=0;i<n;i++){auto[u,h]=s[i];Cert c{W(u),((~W(h))&mask)<<10,W(1023^u),W(h)<<10};W forced=0;vector<W>all;vector<int>sameH;int J=0;for(int j=0;j<n;j++)if(j!=i){auto[v,g]=s[j];W d=W(u^v)|(W(h^g)<<10);assert(d);all.push_back(d);if(pc(d)==1)forced|=d;if(g==h)sameH.push_back(u^v);if(v==u&&pc(h^g)==1)J|=h^g;}
 int a=pc(J&~h),b=pc(J&h),old=100;for(int r=0;r<1024;r++){int val=b+max(a,pc(r&u))+pc(r&(~u&1023));if(val>=old)continue;bool ok=true;for(int d:sameH)if(!(r&d)){ok=false;break;}if(ok)old=val;}
 if(old>k){found=i;break;}
 sort(all.begin(),all.end(),[](W a,W b){return make_pair(pc(a),a)<make_pair(pc(b),b);});for(W d:all)if(!(d&forced)){bool dominated=false;for(W e:c.edges)if((d&e)==e){dominated=true;break;}if(!dominated)c.edges.push_back(d);}
 int exact=old;for(;exact<=k;exact++){c.k=exact;c.fail.clear();if(c.go(forced))break;}nodes+=c.nodes;checked++;maxexact=max(maxexact,exact);if(exact>old){strict++;if(ex<0){ex=i;exOld=old;exNew=exact;}}if(exact>k){found=i;break;}
 }
 cout<<id<<","<<n<<","<<found<<","<<checked<<","<<maxexact<<","<<strict<<","<<ex<<","<<exOld<<","<<exNew<<","<<nodes<<endl;
}}
```

Adaptive solver: reuse the full FZH C++ algorithm from the pinned parent (identical recursive predicates, query-order sorting, positive replay and cap semantics). Change SZ=512 to SZ=1536; change main's input fields to id,n,m,k,cap and output to id,n,status,calls. The run here used the equivalent below, with pair<int,int> for states and separate qs/loc vectors. Compile both with g++ -O3 -std=c++17.
```cpp
#include <bits/stdc++.h>
using namespace std;
constexpr int SZ=1536;using B=bitset<SZ>;
struct Key{B x;int k;bool operator==(const Key&o)const{return k==o.k&&x==o.x;}};struct Hash{size_t operator()(const Key&a)const{return hash<B>{}(a.x)^(a.k*0x9e3779b97f4a7c15ULL);}};
struct Solver{vector<pair<int,int>>st;int m,k,cap,calls=0;vector<B>qs;vector<vector<pair<int,int>>>loc,nei,sup;unordered_map<Key,int,Hash>memo;
Solver(vector<pair<int,int>>s,int mm,int kk,int cc):st(move(s)),m(mm),k(kk),cap(cc){assert(st.size()<=SZ);map<pair<int,int>,int>idx;for(int i=0;i<(int)st.size();i++)idx[st[i]]=i;nei.resize(st.size());sup.resize(st.size());for(int i=0;i<(int)st.size();i++){auto[u,h]=st[i];for(int j=0;j<m;j++){auto it=idx.find({u,h^(1<<j)});if(it!=idx.end())nei[i].push_back({j,it->second});}for(int v=0;v<(int)st.size();v++)if(v!=i&&st[v].second==h&&(st[v].first&u)==u)sup[i].push_back({v,st[v].first^u});}unordered_map<B,int>ix;for(int r=0;r<10;r++)for(int j=0;j<m;j++){B q;for(int i=0;i<(int)st.size();i++)if(st[i].first>>r&1&&!(st[i].second>>j&1))q.set(i);if(q.none()||q.count()==st.size())continue;auto it=ix.find(q);if(it==ix.end()){ix[q]=qs.size();qs.push_back(q);loc.push_back({{r,j}});}else loc[it->second].push_back({r,j});}}
int solve(const B&X,int k){int n=X.count();if(n<=1)return -2;if(!k||n>(1<<k))return -1;Key key{X,k};auto it=memo.find(key);if(it!=memo.end())return it->second;if(++calls>cap)throw 1;vector<pair<int,int>>tight;for(int i=X._Find_first();i<SZ;i=X._Find_next(i)){int J=0;for(auto[j,v]:nei[i])if(X[v])J|=1<<j;int a=__builtin_popcount((unsigned)J);if(a>k)return memo.emplace(key,-1).first->second;if(k-a<=1){int common=1023;bool has=false;for(auto[v,d]:sup[i])if(X[v]){has=true;common&=d;}if(has&&(a==k||!common))return memo.emplace(key,-1).first->second;}if(a==k)tight.push_back({st[i].first,J});}
vector<pair<int,int>>opts;for(int q=0;q<(int)qs.size();q++){if(!tight.empty()){bool good=false;for(auto[r,j]:loc[q]){bool ok=true;for(auto[u,J]:tight)if(!(u>>r&1)||!(J>>j&1)){ok=false;break;}if(ok){good=true;break;}}if(!good)continue;}int c=(X&qs[q]).count();if(c&&c<n&&max(c,n-c)<=(1<<(k-1)))opts.push_back({max(c,n-c),q});}sort(opts.begin(),opts.end());for(auto[_,q]:opts){B a=X&qs[q],b=X^a;if(a.count()<b.count())swap(a,b);if(solve(a,k-1)!=-1&&solve(b,k-1)!=-1)return memo.emplace(key,q).first->second;}return memo.emplace(key,-1).first->second;}
int run(){B X;for(int i=0;i<(int)st.size();i++)X.set(i);int result;try{result=solve(X,k);}catch(int){return 0;}if(result==-1)return -1;for(int i=0;i<(int)st.size();i++){B Y=X;int rem=k;while(Y.count()>1){int q=memo.at(Key{Y,rem});assert(q>=0&&rem>0);auto[r,j]=loc[q][0];bool yes=(st[i].first>>r&1)&&!(st[i].second>>j&1);B a=Y&qs[q];Y=yes?a:Y^a;rem--;}assert(Y[i]);}return 1;}};
int main(){int cases;cin>>cases;while(cases--){int id,n,m,k,cap;cin>>id>>n>>m>>k>>cap;vector<pair<int,int>>s(n);for(auto&[u,h]:s)cin>>u>>h;Solver v(move(s),m,k,cap);int r=v.run();cout<<id<<","<<n<<","<<r<<","<<v.calls<<endl;}}
```

Run:
```sh
python gen.py 2000 > input.txt
g++ -O3 -std=c++17 cert.cpp -o cert
g++ -O3 -std=c++17 search.cpp -o search
./cert < input.txt > cert_results.csv
./search < input.txt > results.csv
```
Second pass input filter (actual):
```python
r={int(a):int(c) for a,b,c,d in map(lambda x:x.strip().split(','),open('results.csv'))}
f=open('input.txt');n=int(f.readline());cases=[]
for i in range(n):
 a=list(map(int,f.readline().split()));st=[f.readline() for _ in range(a[1])]
 if r[a[0]]==0:
  a[-1]=20000 if a[1]<=300 else 5000
  cases.append(' '.join(map(str,a))+'\n'+''.join(st))
with open('input2.txt','w') as g:g.write(str(len(cases))+'\n'+''.join(cases))
```
Then ./search < input2.txt > results2.csv. Replace pass-1 status by pass-2 status when present. The certificate algorithm runs independently of the adaptive solver. Root exact certificate costs can be used at descendants as well; this run did not yet implement that stronger prune inside adaptive recursion.

## 4. Continuation and authority

Original registration request r4-20261124-0240-ec49fyh-own-session-v1 reread SUCCEEDED. Historical own provenance EM-DIRECT-23537B, RA-2D7B4AD1AA5CD3F5D9EF1C76; current authenticated client identity verified, private writer binding not established. Exact topic lookup r4-20261125-0530-ec49as-read-v1 SUCCEEDED at 11593a52da7b6a1f828c7523d5c534bf507509bc: NO_CANONICAL_PUBLICATION_DIRECTORY, native owner view not evaluated, no formal CLAIM. Independent portable research; no claim or review asserted. Next: integrate complete certificate into adaptive recursion at promising tight nodes; retain and resume 270 unknown keys rather than re-solving the 78 feasible keys; alternatively extend feasible suffix fibers backward. Preserve M14 bounds and finite exception counts until a full proof. AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE_COST / PARTIAL_EXACT_BRANCH_REPLAY / PARENT_DEPENDENT / NOT_REVIEWED.
