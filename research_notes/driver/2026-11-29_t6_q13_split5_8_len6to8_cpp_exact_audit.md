# T6 q13 split(5,8) lengths 6–8: exact interval audit in C++

Driver EM-DVR-DEBB5E; original custody and contribution history retained. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca. Reuses saturated kernel and dual interval theorem of cd13961f1ad5ca95a5e1431216f0017e57f00825 and partial ledger 9102add32110bb674f45dc10c240c68a5a5a195f. Basis U from 0bf185c700fe5a46b5e7ad1b49f7441c1a2ee7be:research_checks/T6_P13_Q13_SPLIT0_13_AUTHOR_EXACT_CERT_20261126.json. Relaxed high domain, common atoms retained, both mass budgets 2331, six mixed congruences. First JavaScript execution timed out; target path read returned 404, no successful computation attributed to that run. A separate local Python exact rational setup and compiled C++17 exhaustive search completed all 28 remaining pairs. Shared nonblind context; not clean independent decisive review of Driver-authored method.

## Exact coverage and arithmetic
All partitions of 5 crossed with partitions of 8 of lengths 6,7,8; 7 x 4 = 28. For each high atom (q,r), cost 169q+13r-1, r=1..12, contribution t_k=(13q+r)^(-k) mod 13^k, k=1..6. Enumerate nondecreasing r within each equal q block, prune only if cumulative positive cost exceeds 2331. Low weight w_r=13r-1. Verify H_{kr}=r^(-k) mod 13^k, each row of U in kernel and |det U|=13^21. Solve Hx=t by successive mod-13 digit lifts (at digit j=0..5 use first 6-j columns and last 6-j rows, invert mod 13, add 13^j times digit solution); verify each lift. Let B=13^6, D=B U^-1; exact integer D. For every atom cache xD mod B. Let g_{ri}=(U^-1)_{ri}/w_r; l_i=min(0,min_r g), h_i=max(0,max_r g). Width bound max_i 2453(h_i-l_i)=498515831/736645312<1, exact checked using Python Fraction and SymPy. In order of increasing widths precompute L_i=ceil(B[(2331-mp)l_i-(2331-mn)h_i]), H_i=floor(B[(2331-mp)h_i-(2331-mn)l_i]); verify L_i<=0<=H_i and H_i-L_i<B. For each pair of masses group positives by mp, sorted by first residue coordinate; for each negative, enumerate positives in circular inclusive interval [c-H_0,c-L_0] mod B by binary search; keep duplicate residue entries. Test each other coordinate with exact integer arithmetic. For a surviving residue c, take c if c<=H_i, else c-B; verify interval; restore original coordinate order and u=zU/B; assert each division exact. Check all six congruences against independently accumulated high atom t values, and signed budgets. Reject ledger sums asserted for every row. C++ int arithmetic residue sums <2B; products in recovery and congruences use signed 64-bit; z_i bounded by B, |U_ij|<=356, so numerator <=12*B*356 <2^35; low u and congruence products safely within signed 64-bit. The exhaustive enumeration is not based on smoothness or deletion of common atoms.

## Executed output
Columns pp,np,raw,search,index_pass,box_survivors,valid,min_max_budget_excess. Pattern digits denote high q parts. Row minimum excess is only over recovered box survivors, not over every congruence solution. All 28 rows completed with zero valid.
```csv
11111,11111111,330142176,321786192,70268268,736,0,1515
11111,1111112,648700416,647901072,149113242,919,0,1499
11111,111113,228953088,228953088,55693087,314,0,1490
11111,111122,465060960,465060960,113123034,1132,0,648
1112,11111111,330142176,321786192,74528092,477,0,1715
1112,1111112,648700416,647901072,157593057,1981,0,664
1112,111113,228953088,228953088,58678896,698,0,1189
1112,111122,465060960,465060960,119218042,1727,0,741
113,11111111,70744752,68954184,16871498,177,0,1622
113,1111112,139007232,138835944,35603609,582,0,1524
113,111113,49061376,49061376,13221754,428,0,1120
113,111122,99655920,99655920,26855794,563,0,1287
122,11111111,70744752,68954184,16870198,182,0,1174
122,1111112,139007232,138835944,35616789,463,0,1353
122,111113,49061376,49061376,13224607,353,0,1011
122,111122,99655920,99655920,26841685,595,0,819
14,11111111,10883808,10608336,2735455,60,0,2198
14,1111112,21385728,21359376,5756043,180,0,1949
14,111113,7547904,7547904,2132529,69,0,1843
14,111122,15331680,15331680,4331627,134,0,1304
23,11111111,10883808,10608336,2734380,39,0,1893
23,1111112,21385728,21359376,5759619,146,0,1280
23,111113,7547904,7547904,2133880,73,0,1733
23,111122,15331680,15331680,4330378,154,0,1827
5,11111111,906984,884028,239449,4,0,2247
5,1111112,1782144,1779948,503220,24,0,2230
5,111113,628992,628992,185926,4,0,3534
5,111122,1277640,1277640,378458,24,0,1644
TOTAL,28,4177545840,4154682672,1014542616,12238,0
```
Minimum observed excess 648. Combined with prior 126-pattern ledger, split(5,8) all 154 patterns complete, raw 5,685,631,380, budget-feasible 5,662,768,212, index passes 1,424,467,616, recovered 23,496, zero valid. Global alternate-solver coverage 720/885. Remaining split(6,7) 165, H0, observation-envelope implication, lower-prime completion, global T6=2332 remain open. Native Reference still only 566 patterns as of original successful pass; no Result acceptance or Task/mother completion.

## Reproduce
The previous saved JS audit function in f5acfbd9481996599feed33fa9bb8e86cac7f5a5:research_notes/driver/2026-11-28_t6_q13_split5_8_len5_pos5_modular_interval_join.md supplies exact equivalent executable logic and all rational setup, use all 7 positive partitions (remove filter p.length===5) and change negative filter to p.length>=6; use pinned U. Run in a local Node process rather than the timed-out bounded tool, or implement the exact C++ loops below. The actual run used Python Fraction/SymPy setup as described above, generated integer input for C++ (B; W; order; U; H; each q,r coordinates and t; counts and lists of possible mp,mn; bounds for each mass pair), then g++ -O3 -std=c++17 audit.cpp -o audit; ./audit < input.txt. Positive mass list = {169*5+13*r-l: 1<=l<=5, l<=r<=12*l, mass<=2331}; negative list analogously 8 and l=6..8. Coordinate arrays in sorted width order; original H and U unchanged. Full C++ search implementation follows.
```cpp
#include <bits/stdc++.h>
using namespace std; using ll=long long; using V=array<int,12>; using T=array<int,6>;
int B,W[12],ord[12],U[12][12],H[6][12],P[6]; V cs[9][13]; T ts[9][13]; struct Box{V lo,hi;}; Box bx[2332][2332];
struct R{int m;V v;T t;};
vector<vector<int>> parts(int n,int lo=1){if(!n)return {{}};vector<vector<int>> a;for(int q=lo;q<=n;q++)for(auto p:parts(n-q,q)){p.insert(p.begin(),q);a.push_back(p);}return a;}
ll raw(vector<int> p){ll a=1;for(int q=1;q<=8;q++){int k=count(p.begin(),p.end(),q);ll c=1;for(int j=1;j<=k;j++)c=c*(11+j)/j;a*=c;}return a;}
vector<R> roster(vector<int> p){vector<R> a;function<void(int,int,R)> go=[&](int i,int prev,R z){if(i==(int)p.size()){a.push_back(z);return;}int q=p[i];for(int r=i&&p[i-1]==q?prev:1;r<=12;r++){R x=z;x.m+=169*q+13*r-1;if(x.m>2331)break;for(int j=0;j<12;j++)x.v[j]=(x.v[j]+cs[q][r][j])%B;for(int j=0;j<6;j++)x.t[j]=(x.t[j]+ts[q][r][j])%P[j];go(i+1,r,x);}};go(0,1,R{});return a;}
int main(){cin>>B;for(int i=0,p=1;i<6;i++)P[i]=p*=13;for(int &x:W)cin>>x;for(int &x:ord)cin>>x;for(auto &r:U)for(int &x:r)cin>>x;for(auto &r:H)for(int &x:r)cin>>x;for(int q=1;q<=8;q++)for(int r=1;r<=12;r++){for(int &x:cs[q][r])cin>>x;for(int &x:ts[q][r])cin>>x;}int m,n;cin>>m>>n;vector<int> ms(m),ns(n);for(int &x:ms)cin>>x;for(int &x:ns)cin>>x;for(int x:ms)for(int y:ns){for(int &v:bx[x][y].lo)cin>>v;for(int &v:bx[x][y].hi)cin>>v;}
ll total[5]={};int rows=0;for(auto pp:parts(5)){auto pos=roster(pp);map<int,vector<R>> groups;for(auto p:pos)groups[p.m].push_back(p);for(auto &[m,g]:groups)sort(g.begin(),g.end(),[](auto&a,auto&b){return a.v[0]<b.v[0];});for(auto np:parts(8)){if(np.size()<6)continue;auto neg=roster(np);ll rawc=raw(pp)*raw(np),search=(ll)pos.size()*neg.size(),passes=0,surv=0,valid=0;ll rej[12]={};ll minex=LLONG_MAX;for(auto &n:neg)for(auto &[m,g]:groups){auto &b=bx[m][n.m];int L=(n.v[0]-b.hi[0]+B)%B,R=(n.v[0]-b.lo[0]+B)%B;auto lb=[&](int x){return lower_bound(g.begin(),g.end(),x,[](auto &a,int x){return a.v[0]<x;})-g.begin();};pair<int,int> ranges[2];int nr;if(L<=R){ranges[0]={lb(L),lb(R+1)};nr=1;}else{ranges[0]={0,lb(R+1)};ranges[1]={lb(L),g.size()};nr=2;}ll npass=0;for(int k=0;k<nr;k++){auto [l,h]=ranges[k];npass+=h-l;for(int i=l;i<h;i++){auto&p=g[i];int j=1;for(;j<12;j++){int c=n.v[j]-p.v[j];if(c<0)c+=B;if(c>b.hi[j]&&c-B<b.lo[j])break;}if(j<12){rej[j]++;continue;}surv++;ll z[12],u[12];for(j=0;j<12;j++){int c=n.v[j]-p.v[j];if(c<0)c+=B;z[ord[j]]=c<=b.hi[j]?c:c-B;assert(z[ord[j]]>=b.lo[j]&&z[ord[j]]<=b.hi[j]);}ll mp=p.m,mn=n.m;for(j=0;j<12;j++){ll x=0;for(int k=0;k<12;k++)x+=z[k]*U[k][j];assert(x%B==0);u[j]=x/B;if(u[j]>0)mp+=u[j]*W[j];else mn-=u[j]*W[j];}for(j=0;j<6;j++){ll x=p.t[j]-n.t[j];for(int k=0;k<12;k++)x+=u[k]*H[j][k];assert(x%P[j]==0);}ll ex=max(mp,mn)-2331;minex=min(minex,ex);if(ex<=0)valid++;}}passes+=npass;rej[0]+=g.size()-npass;}assert(accumulate(rej,rej+12,0LL)+surv==search&&passes==search-rej[0]);ll vals[]={rawc,search,passes,surv,valid};for(int j=0;j<5;j++)total[j]+=vals[j];rows++;for(int x:pp)cout<<x;cout<<',';for(int x:np)cout<<x;for(ll x:vals)cout<<','<<x;cout<<','<<minex;for(ll x:rej)cout<<','<<x;cout<<endl;}}
cout<<"TOTAL,"<<rows;for(ll x:total)cout<<','<<x;cout<<endl;}
```
