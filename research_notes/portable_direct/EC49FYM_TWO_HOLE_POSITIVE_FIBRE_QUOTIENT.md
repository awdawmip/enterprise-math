# EC49FYM — exact positive-fibre quotient and two-hole minimax improvements

2026-11-24. Portable continuation of EC49FYL at immutable 5cbfe43ccd041b7b7fc458586d4384a0de074246, research_notes/portable_direct/EC49FYL_DENSE_HOLE_ADAPTIVE_EXACT_LAW.md. Frozen auxiliary BRC16943 support family (list below); unit noiseless Boolean physical queries, at most h holes, m>h. No native X6/heartbeat attribution. Prior own registration receipt r4-20261124-0240-ec49fyh-own-session-v1 SUCCEEDED, EM-DIRECT-23537B, RA-2D7B4AD1AA5CD3F5D9EF1C76. Current exact topic receipt r4-20261124-0730-ec49as-current-task-v1 SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY at bdc3cf2a82e18426c91ff71c40f0b1c4ed8c31ba; directory observation only, no formal CLAIM or shared owner transition.

## Exact quotient for arbitrary hole budget

Let F be the 50 nonempty support masks. Raw state (U,Z) gives reading W(t,j)=1[t in U]1[j notin Z], |Z|<=h. After any prefix let A be supports compatible with the positive columns' full row transcripts, and for each of the n columns not yet observed positive let L_j subset F be supports compatible with its zero observations if that column is live. A column with a positive has a known live label; its future queries depend only on U, independent of which known-live column is selected. Retain the physical label list for execution and recovery.

For U in A, put k(U)=number of j with U notin L_j. Exactly these k columns are forced holes; among the remaining n-k columns, every choice of up to h-k additional holes is possible, independently conditional on U. Thus trim A to k<=h, intersect all L_j with A, and canonicalize the unordered multiset of L_j. This representation retains all joint hole choices and their multiplicity, not just the marginal possible live sets. Exact cardinality:
N(A,L)=sum_{U in A} sum_{i=0}^{min(h-k(U),n-k(U))} binom(n-k(U),i).

Transitions: a probe in a known-live column intersects A with the row mask R_t on 1, and its complement on 0. A probe in unconfirmed j on 0 replaces L_j by L_j minus R_t. On 1 intersect A with L_j intersect R_t, remove j from the unconfirmed list, retain its known-live physical label. Normalize after each update. These rules follow directly by restricting the complete raw state relation, hence by induction preserve all future Boolean observations. Permuting unconfirmed columns (and known-live labels) is a bijective relabeling of possible states, preserving all physical probe actions up to permutation. The minimax value is therefore exactly preserved by sorting L; use a retained label map when replaying a strategy. A constant probe can be omitted. Identical or complementary canonical child pairs are equivalent for feasibility, even when their label maps differ.

For h=2, if a_i is the number of supports with exactly i forced holes (i=0,1,2), then N=a_0(1+n+binom(n,2))+a_1*n+a_2. Compute the a_i via three bit-sliced threshold accumulators G_1,G_2,G_3, where G_i tracks supports forced into at least i holes. Trim G_3; no floating arithmetic.

## Additional admissible residual lower bound

Fix a compatible support U and take its target state with exactly its k forced holes, all other columns live. If k<h then each of its n-k unconfirmed live columns requires a future positive read: otherwise turning that column into an additional hole yields a competing state with the identical path. For any strict superset V in A compatible as live in every target live unconfirmed column (the already known-live constraints are in A), the state (V, same target hole set) also survives. Distinguishing these strict supersets requires additional negative probes in live columns, hitting every V minus U. Positive probes cannot distinguish these supersets. Therefore remaining depth is at least n-k plus the transversal number of these residual differences. This is a valid necessary condition for any prefix and arbitrary h; the implementation uses only U=101,788,833, and tests the small remaining transversal budget by exact enumeration. When k>=h it omits this bound, rather than transferring a claim outside its scope.

## Results

Exact search with canonical positive-fibre quotient, h=2. Every state count is exact. Recursive feasibility enumerates every nonconstant splitting row and column orbit whose two child sizes fit 2^(d-1), except equivalent canonical child pairs; complete failure proves impossibility. Memo bounds preserve both proven upper and lower depths. No time-limited search is called impossible.

Executed C++17 (g++ -O3):
```
7 2 11 1450 0 calls 58367 memo 23952
8 2 12 1850 1 calls 6629433 memo 1031718
verified 1850 12 20558
9 2 12 2300 0 calls 664064 memo 201211
```
The 8-column tree was replayed with each of 1850 original labeled (U,Z) inputs, retaining the column permutation and checking actual query answers, support compatibility, forced holes and known-live labels, terminating in an exact singleton within 12 queries. Mean depth 20558/1850. A separate m=9 depth13 search was interrupted, and is unnecessary: by the already-proved extension inequality Q_2(9)<=Q_2(8)+1=13. Thus, using FYL's prior depth12 upper for m=7 and depth11 impossibility for m=8:
Q_2(7)=12, Q_2(8)=12, Q_2(9)=13.
The stabilized residual constant now satisfies c_2 in {3,4}; for every m>=8, Q_2(m)<=m+4. The remaining question is whether any m>=10 admits depth m+3; a finite negative at m=9 does not exclude a later drop.

Further general consequence: scan one column by rows (1,2,0) as in FYL; a positive branch identifies U within six total queries then reads each other column once, costing <=m+5. A hole branch costs three queries and reduces (h,m) to (h-1,m-1), giving Q_h(m)<=max(m+5,3+Q_{h-1}(m-1)) for h>=1 and m>h. For the stabilized constants, c_h<=max(5,2+c_{h-1}). With c_1=3 and the new c_2<=4, induction gives c_h<=2h for h>=2, improving FYL's 2h+4. This is a derived asymptotic upper bound, not a determination of every c_h.

## Executed search implementation

Save as ec49.cpp; g++ -O3 -std=c++17 ec49.cpp -o ec49; run ./ec49 7 11, ./ec49 8 12, ./ec49 9 12. Implementation is for h=2 and m<=10, not the arbitrary-h code. All support and residual calculations are exact unsigned integer bit operations. The program below is the executed algorithm and replay.

```cpp
#include <bits/stdc++.h>
using namespace std;using U=uint64_t;const U ALL=(1ULL<<50)-1;int m,h;U R[10];int F[]={23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005};
struct S{U a;array<U,10> l{};int n;bool operator==(S const&b)const{return a==b.a&&n==b.n&&l==b.l;}bool operator<(S const&b)const{return tie(a,n,l)<tie(b.a,b.n,b.l);}};
struct Hash{size_t operator()(S const&s)const{U x=s.a+0x9e3779b97f4a7c15ULL+s.n;for(int j=0;j<s.n;j++){x^=s.l[j]+0x9e3779b97f4a7c15ULL+(x<<6)+(x>>2);}return x;}};
int norm(S &s){U g1=0,g2=0,g3=0;for(int j=0;j<s.n;j++){U b=s.a&~s.l[j];g3|=g2&b;g2|=g1&b;g1|=b;}s.a&=~g3;for(int j=0;j<s.n;j++)s.l[j]&=s.a;sort(s.l.begin(),s.l.begin()+s.n);for(int j=s.n;j<10;j++)s.l[j]=0;return __builtin_popcountll(s.a&~g1)*(1+s.n+s.n*(s.n-1)/2)+__builtin_popcountll(s.a&g1&~g2)*s.n+__builtin_popcountll(s.a&g2);}
struct Entry{int lo=0,hi=99,j=-2,t=-1;};unordered_map<S,Entry,Hash> mem;long long calls=0;int rootj=-2,roott=-1;auto start=chrono::steady_clock::now();
struct Opt{int score,j,t,nx,ny;S x,y;};
bool bound(S const&s,int d){for(int u: {101,788,833}){int i=find(F,F+50,u)-F;U b=1ULL<<i;if(!(s.a&b))continue;int k=0;for(int j=0;j<s.n;j++)k+=!(s.l[j]&b);if(k>=h)continue;int live=s.n-k;if(live>d)return false;vector<int> dif;for(int v=0;v<50;v++){if(!(s.a>>v&1)||F[v]==u||(F[v]&u)!=u)continue;bool ok=true;for(int j=0;j<s.n;j++)if((s.l[j]&b)&&!(s.l[j]>>v&1)){ok=false;break;}if(ok)dif.push_back(F[v]^u);}if(dif.empty())continue;int extra=d-live;if(extra>=3)continue;bool possible=false;for(int t=0;t<1024;t++)if(__builtin_popcount((unsigned)t)<=extra){bool ok=true;for(int v:dif)if(!(t&v)){ok=false;break;}if(ok){possible=true;break;}}if(!possible)return false;}return true;}
bool solve(S const&s,int n,int d){calls++;if(n<=1)return true;if(d<=0||n>(1<<d))return false;auto it=mem.find(s);if(it!=mem.end()){if(it->second.lo>d)return false;if(it->second.hi<=d)return true;}if(!bound(s,d))return false;if(calls%1000000==0)cerr<<calls<<" mem "<<mem.size()<<" sec "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<endl;vector<Opt> opts;int cap=1<<(d-1);for(int j=-1;j<s.n;j++){if(j==-1&&s.n==m)continue;if(j>0&&s.l[j]==s.l[j-1])continue;U l=j<0?s.a:s.l[j];for(int t=0;t<10;t++){U p=l&R[t];if(!p)continue;S x=s,y=s;if(j<0){x.a&=~R[t];y.a&=R[t];}else{x.l[j]&=~R[t];y.a=p;for(int k=j;k+1<y.n;k++)y.l[k]=y.l[k+1];y.n--;};int nx=norm(x),ny=norm(y);if(!nx||!ny||max(nx,ny)>cap)continue;bool dupe=false;for(auto&o:opts)if((o.x==x&&o.y==y)||(o.x==y&&o.y==x)){dupe=true;break;}if(!dupe)opts.push_back({max(nx,ny),j,t,nx,ny,x,y});}}
sort(opts.begin(),opts.end(),[](auto&a,auto&b){return tie(a.score,a.j,a.t)<tie(b.score,b.j,b.t);});for(auto&o:opts){bool ok=o.nx>=o.ny?(solve(o.x,o.nx,d-1)&&solve(o.y,o.ny,d-1)):(solve(o.y,o.ny,d-1)&&solve(o.x,o.nx,d-1));if(ok){auto&e=mem[s];e.hi=d;e.j=o.j;e.t=o.t;return true;}}auto&e=mem[s];e.lo=max(e.lo,d+1);return false;}
int main(int argc,char**argv){m=atoi(argv[1]);h=2;int d=atoi(argv[2]);for(int t=0;t<10;t++)for(int i=0;i<50;i++)if(F[i]>>t&1)R[t]|=1ULL<<i;S s{ALL,{},m};for(int j=0;j<m;j++)s.l[j]=ALL;int n=norm(s);bool ok=solve(s,n,d);cout<<m<<" "<<h<<" "<<d<<" "<<n<<" "<<ok<<" calls "<<calls<<" memo "<<mem.size()<<endl;
if(ok){int mx=0,total=0,count=0;for(int i=0;i<50;i++)for(int z=0;z<(1<<m);z++)if(__builtin_popcount((unsigned)z)<=h){S a=s;vector<pair<U,int>> cols;for(int j=0;j<m;j++)cols.push_back({ALL,j});vector<int> pos;int k=0,nn=n;while(nn>1){auto e=mem.at(a);int j=e.j,t=e.t;int label=j<0?pos[0]:cols[j].second;bool bit=(F[i]>>t&1)&&!(z>>label&1);if(j<0){if(bit)a.a&=R[t];else a.a&=~R[t];}else if(bit){a.a=cols[j].first&R[t];pos.push_back(label);cols.erase(cols.begin()+j);}else cols[j].first&=~R[t];a.n=cols.size();for(int q=0;q<a.n;q++)a.l[q]=cols[q].first;nn=norm(a);for(auto&c:cols)c.first&=a.a;sort(cols.begin(),cols.end());assert(a.a>>i&1);int forced=0;for(auto c:cols){if(!(c.first>>i&1)){forced++;assert(z>>c.second&1);}}assert(forced<=h);for(int p:pos)assert(!(z>>p&1));k++;assert(k<=d);}assert(__builtin_popcountll(a.a)==1);mx=max(mx,k);total+=k;count++;}cout<<"verified "<<count<<" "<<mx<<" "<<total<<endl;}}
```

Status: AUTHOR_PROVED / EXACT_FINITE_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED. Replay shares normalization code with search; independent raw-state verifier and compact tree certificate remain worthwhile follow-ups. Next: search m>=10 at depth m+3 or prove a uniform obstruction, with memory-aware search; preserve 7,8,9 solved cases. No need to rerun interrupted m=9 depth13. No change to P000, frozen support inputs, task status, or research cadence.
