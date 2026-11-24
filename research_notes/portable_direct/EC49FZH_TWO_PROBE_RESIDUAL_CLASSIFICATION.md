# EC49FZH — Joint row/column certificate and exact two-probe residual classification

2026-11-25. Frozen BRC16943 auxiliary Boolean observer, 50 supports and physical column labels, as in FZG at bf04c9dd1d7120fd7c0d6741c789f43e27318176:research_notes/portable_direct/EC49FZG_TIGHT_DEFICIT_MASK_RIGIDITY.md (blob 2df26166059e5d7dd7ea075962a4218b77213a94). Reuse its static classification and last-positive branch result. Model W(r,j)=1[r in U]1[j not in H], |H|<=h<m. Auxiliary discrete observer, not native X6 attribution.

## New analytic result: exact restricted certificate cost
For any compatible labeled state set X and x=(U,H) in X, let J consist of j such that (U,H xor {j}) is also in X. Write a=|J\H|, b=|J intersect H|. Let V range over supports V!=U with (V,H) in X. Choose row sets P subset U, N subset complement U, subject to
(P intersect (U\V)) union (N intersect (V\U)) nonempty for every V.
Then the minimum number of probes that, on the path for x, distinguish x from all its single-column toggle neighbors AND all same-H support competitors is exactly

C(x) = b + min_{P,N feasible} [ max(a,|P|) + |N| ].

In particular, every recovering decision tree has remaining worst-case depth >= max_{x in X} C(x).

Proof: Every toggle neighbor requires a probe at its column with row in U. Mandatory missing columns consume b distinct negative probes, none of which separates same-H competitors. The a mandatory live columns require a positive probe each. Let P be the positive rows observed in live columns and N the negative rows observed there. Same-H competitors differ only on live columns, exactly on U xor V, so the displayed covering condition is necessary. At least max(a,|P|) positive and |N| negative live-column probes are required. Conversely, assign the P rows to mandatory live columns when possible, then to arbitrary live columns (one exists since h<m); if a>|P| fill the remaining mandatory live columns with arbitrary rows of nonempty U. Observe each N row in a live column, and one U row in each mandatory hole. This realizes the bound and separates precisely the specified competitors (possibly more). This is a certificate on the true-state path, not a decision tree construction or an exact depth formula for X. If U is empty the model needs separate treatment; all frozen supports are nonempty.

Useful special case: if a strict superset V of U is compatible at the same H, at least one extra live negative probe is necessary beyond |J|. If two such supersets have disjoint V\U, at least two extra probes are necessary. More generally their row transversal number is a lower bound on |N|. This is valid on arbitrary transcripts. It strengthens FZG mandatory-column pruning without erasing labels. A query-equivalence class may be merged only when its Boolean response vector is identical on the whole branch, hence on all descendant subsets.

For h=14,m=25,d=33, last-positive branch budget k=12, the following four FZG exclusions now have short analytic witnesses (no tree search needed). The witness x=(673,H) has 12 toggle neighbors and a compatible (697,H), a strict superset with 697 xor 673=24, requiring a thirteenth query. Column bit numbering starts at zero, with masks in the sorted multiset below.
last mask,row,H decimal:
1,0,29487310
3,0,29487247
192,7,29454543
512,9,25293007
These are simplified proofs of known last-probe exclusions, not four new exclusions.

## New exact finite result: penultimate-positive branches
The four surviving final probe types are (3,1),(192,6),(320,6),(320,8). Remove that bit from a representative physical column of the full zero-prefix inventory. Enumerate every inequivalent preceding probe (mask,row) of the resulting inventory, remove its bit, and constrain that probe to positive. Its remaining depth budget is m-h+2=13. The last probe is NOT imposed as a constraint in this positive branch. All columns with the same current mask are equivalent by physical-label permutation for the branch. There are 58 ordered types. Exact decision recursion, using mandatory-column pruning and the strict-superset residual lower bounds above, resolves all 58: 29 feasible and 29 impossible. All 4624 labeled states across the 29 feasible branches replayed successfully (sum with multiplicity across branches). All 29 negative results exhausted the search; 12 initial node-cap outcomes were rerun with a larger cap and resolved. There is no unresolved type at depth two.

Final type | possible penultimate types (current mask,row) | yes/no
(3,1): (1,0),(3,0),(4,2),(144,7),(320,6),(320,8) | 6/8
(192,6): (1,0),(3,0),(4,2),(8,3),(128,7),(144,7),(192,7),(256,8),(320,8) | 9/6
(320,6): (3,1),(4,2),(8,3),(144,4),(144,7),(192,7),(256,8),(320,8) | 8/6
(320,8): (3,1),(64,6),(144,7),(192,6),(320,6),(512,9) | 6/9

Feasibility here means the positive branch alone is recoverable; the two suffix branches and all-zero branch have separate compatible histories. It does not settle M14, which remains 25<=M14<=27. For further reverse search, retain the actual labeled suffix as well as the two-probe types when their identities matter. FZF 35/82 closed exception count remains unchanged.

## Reproduction
Use Python 3 to generate input; compile the C++17 solver with g++ -O3 -std=c++17. The first run used cap=300000 and the 12 capped cases were repeated with cap=3000000; running the complete input with the larger cap gives the same statuses. All arithmetic is integer; bitsets preserve states. For each X, a nonconstant query partitions it into X intersect yes and its complement. If neither child exceeds binary capacity, recursively check both; k decreases. Negative memo entries are established by sound certificate pruning or exhaustive partition search, never by a cap. Positive memo entries store the chosen query and are replayed on every original state with actual observer evaluation. The input includes all admissible H by enumeration of additional holes on free columns, with the positive column live.

Save as input.py:
```python
from itertools import combinations
from sys import argv
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
MS=[s for s,n in [(1,4),(2,2),(3,2),(4,4),(8,1),(144,2),(192,2),(256,3),(320,2),(512,3)] for _ in range(n)]
def physical(p,h,pos=None):
 m=len(p);out=[]
 for u in F:
  if pos and (not(u>>pos[0]&1) or p[pos[1]]&u):continue
  req=sum(1<<j for j,s in enumerate(p) if s&u)
  if req.bit_count()>h:continue
  free=[j for j in range(m) if not req>>j&1 and (not pos or j!=pos[1])]
  for k in range(min(h-req.bit_count(),len(free))+1):
   for cc in combinations(free,k):out.append((u,req|sum(1<<j for j in cc)))
 return out
def probe_types(p):
 for j,s in enumerate(p):
  if s in p[:j]:continue
  for r in range(10):
   if s>>r&1:yield j,r
def generate():
 surv={(3,1),(192,6),(320,6),(320,8)}
 cases=[]
 for j,r in probe_types(MS):
  if (MS[j],r) not in surv:continue
  p=MS.copy();p[j]^=1<<r
  for l,s in probe_types(p):
   q=p.copy();q[l]^=1<<s;st=physical(q,14,(s,l))
   cases.append((MS[j],r,p[l],s,st))
 return sorted(cases,key=lambda x:len(x[4]))
if __name__=='__main__':
 cases=generate();assert len(cases)==58
 print(len(cases))
 for a,b,c,d,st in cases:
  print(a,b,c,d,len(st),25,13,int(argv[1]) if len(argv)>1 else 3000000)
  for u,h in st:print(u,h)
```

Save as search.cpp (executed algorithm):
```cpp
#include <bits/stdc++.h>
using namespace std;
constexpr int SZ=512;using B=bitset<SZ>;
struct Key{B x;int k;bool operator==(Key const&o)const{return k==o.k&&x==o.x;}};
struct Hash{size_t operator()(Key const&a)const{return hash<B>{}(a.x)^(a.k*0x9e3779b97f4a7c15ULL);}};
struct Query{B yes;vector<pair<int,int>> loc;};
struct S{int u,h;};
struct Solver{
 vector<S> st;int m,k,cap,calls=0;vector<Query> qs;vector<vector<pair<int,int>>> nei;vector<vector<pair<int,int>>> sup;unordered_map<Key,int,Hash> memo;
 Solver(vector<S> s,int mm,int kk,int cc):st(move(s)),m(mm),k(kk),cap(cc){
  if(st.size()>SZ)throw runtime_error("state limit");
  map<pair<int,int>,int> idx;for(int i=0;i<(int)st.size();i++)idx[{st[i].u,st[i].h}]=i;
  nei.resize(st.size());sup.resize(st.size());
  for(int i=0;i<(int)st.size();i++){auto [u,h]=st[i];for(int j=0;j<m;j++){auto it=idx.find({u,h^(1<<j)});if(it!=idx.end())nei[i].push_back({j,it->second});}for(int v=0;v<(int)st.size();v++)if(v!=i&&st[v].h==h&&(st[v].u&u)==u)sup[i].push_back({v,st[v].u^u});}
  unordered_map<B,int> ix;
  for(int r=0;r<10;r++)for(int j=0;j<m;j++){B q;for(int i=0;i<(int)st.size();i++)if(st[i].u>>r&1&&!(st[i].h>>j&1))q.set(i);if(q.none()||q.count()==st.size())continue;auto it=ix.find(q);if(it==ix.end()){ix[q]=qs.size();qs.push_back({q,{{r,j}}});}else qs[it->second].loc.push_back({r,j});}
 }
 int solve(B const&X,int k){int n=X.count();if(n<=1)return -2;if(!k||n>(1<<k))return -1;Key key{X,k};auto it=memo.find(key);if(it!=memo.end())return it->second;if(++calls>cap)throw 1;
  vector<pair<int,int>> tight;
  for(int i=X._Find_first();i<SZ;i=X._Find_next(i)){
   int J=0;for(auto [j,v]:nei[i])if(X[v])J|=1<<j;int a=__builtin_popcount((unsigned)J);if(a>k)return memo.emplace(key,-1).first->second;
   if(k-a<=1){int common=1023;bool has=false;for(auto [v,d]:sup[i])if(X[v]){has=true;common&=d;}if(has&&(a==k||!common))return memo.emplace(key,-1).first->second;}
   if(a==k)tight.push_back({st[i].u,J});
  }
  vector<pair<int,int>> opts;
  for(int q=0;q<(int)qs.size();q++){
   if(!tight.empty()){bool good=false;for(auto [r,j]:qs[q].loc){bool ok=true;for(auto [u,J]:tight)if(!(u>>r&1)||!(J>>j&1)){ok=false;break;}if(ok){good=true;break;}}if(!good)continue;}
   int c=(X&qs[q].yes).count();if(c&&c<n&&max(c,n-c)<=(1<<(k-1)))opts.push_back({max(c,n-c),q});
  }
  sort(opts.begin(),opts.end());
  for(auto [_,q]:opts){B a=X&qs[q].yes,b=X^a;if(a.count()<b.count())swap(a,b);if(solve(a,k-1)!=-1&&solve(b,k-1)!=-1)return memo.emplace(key,q).first->second;}
  return memo.emplace(key,-1).first->second;
 }
 int run(){B X;for(int i=0;i<(int)st.size();i++)X.set(i);int result;try{result=solve(X,k);}catch(int){return 0;}if(result==-1)return -1;for(int i=0;i<(int)st.size();i++){B Y=X;int rem=k;while(Y.count()>1){int q=memo.at(Key{Y,rem});assert(q>=0&&rem>0);auto [r,j]=qs[q].loc[0];bool yes=(st[i].u>>r&1)&&!(st[i].h>>j&1);B a=Y&qs[q].yes;Y=yes?a:Y^a;rem--;}assert(Y[i]);}return 1;}
};
int main(){int cases;cin>>cases;while(cases--){int a,b,c,d,n,m,k,cap;cin>>a>>b>>c>>d>>n>>m>>k>>cap;vector<S> st(n);for(auto&s:st)cin>>s.u>>s.h;Solver sol(st,m,k,cap);int v=sol.run();cout<<a<<","<<b<<","<<c<<","<<d<<","<<n<<","<<v<<","<<sol.calls<<endl;}}
```

For the four analytic witnesses, use physical() and probe_types() above. For each corresponding last type, remove its bit, enumerate states in its positive branch, and assert both (673,H),(697,H) and exactly 12 compatible single-column toggles of (673,H). For the general restricted certificate, enumerate all 1024 row masks S=P union N hitting every u xor v for same-H competitors and evaluate b+max(a,popcount(S&u))+popcount(S&~u).

## Actual calculation output, resolved status
Format last mask,row,penultimate mask,row,states,status,calls. Status 1=feasible and replayed; -1=exhausted impossible. Capped 12 initial outputs are replaced here by their actual second-run terminal outputs. Total resolved recursion calls 12,238,013 (excludes initial capped attempts).
```csv
320,8,192,6,50,1,49
320,8,320,6,65,1,64
192,6,320,8,73,1,72
320,6,320,8,73,1,72
320,8,64,6,89,1,88
320,6,256,8,97,1,7933
192,6,144,7,105,1,104
320,6,144,7,116,1,936
3,1,3,0,118,1,622
192,6,192,7,129,1,502
320,6,192,7,129,1,502
3,1,4,2,153,1,46854
192,6,256,8,165,1,38531
192,6,128,7,168,1,37573
3,1,1,0,169,1,34251
320,8,144,7,172,1,12723
3,1,144,7,183,1,19566
192,6,3,0,186,1,21389
320,8,3,0,186,-1,60528
192,6,512,9,187,-1,73639
320,6,3,1,195,1,125260
320,8,3,1,195,1,33651
3,1,512,9,197,-1,81613
320,8,512,9,197,1,20088
3,1,320,6,199,1,62196
3,1,320,8,207,1,14443
320,6,3,0,208,-1,81301
320,6,512,9,208,-1,199159
192,6,4,2,209,1,122134
320,6,4,2,210,1,139519
320,6,8,3,213,1,318402
320,8,144,4,220,-1,31857
320,8,4,2,221,-1,192764
320,6,144,4,231,1,78977
3,1,192,6,251,-1,86914
192,6,1,0,259,1,325433
192,6,3,1,262,-1,244061
192,6,8,3,269,1,645304
320,6,192,6,273,-1,103272
3,1,192,7,274,-1,22466
3,1,144,4,276,-1,117937
192,6,320,6,288,-1,304273
3,1,256,8,298,-1,611170
192,6,144,4,298,-1,159321
320,8,1,0,304,-1,259281
320,8,2,1,313,-1,143424
320,8,192,7,330,-1,66344
192,6,2,1,335,-1,817220
192,6,192,6,341,-1,149413
3,1,8,3,381,-1,757779
3,1,3,1,407,-1,617476
320,6,2,1,413,-1,1058681
320,6,1,0,426,-1,1451353
320,6,320,6,456,-1,1048829
3,1,2,1,458,-1,694078
320,8,8,3,460,-1,249361
320,8,320,8,487,-1,192855
320,8,256,8,511,-1,254406
```

Additional exploratory screens: the restricted certificate and simple residual/mandatory-column intersection tests at the roots of all 58 penultimate-positive branches did not exclude any of them. Likewise the root tests of the other 14 frozen FZG static inventories did not exclude any of their last-positive types. This explains why full recursive conditional state refinement is useful; these are scoped negative findings, not feasibility results.

## Control and continuation
Original own session registration r4-20261124-0240-ec49fyh-own-session-v1 read SUCCEEDED, EM-DIRECT-23537B, RA-2D7B4AD1AA5CD3F5D9EF1C76. Own recovery metadata confirms session not closed/custody not revoked; current private writer binding not established by metadata alone. Topic lookup r4-20261125-0430-ec49as-read-v1 SUCCEEDED at 44191b8e5c3e786cd12e45b37b4095ba5abe3818, NO_CANONICAL_PUBLICATION_DIRECTORY, native owner projection not evaluated. No shared CLAIM, formal Result or Review. Independent portable source publication. Continue the 29 surviving penultimate types to third-last, using support leaf budgets where sufficient and exact labeled recursion where necessary. Do not redo the 29 excluded types. AUTHOR_PROVED / EXACT_FINITE_BRANCH_CLASSIFICATION / PARENT_DEPENDENT / NOT_REVIEWED.
