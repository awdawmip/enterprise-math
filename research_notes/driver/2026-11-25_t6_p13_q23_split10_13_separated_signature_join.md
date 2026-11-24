# T6 p13 valuation-one q23 split(10,13): complete separated signature join
2026-11-25. Continuation of Driver lane historical EM-DVR-DEBB5E author-side work, revision553. Scientific source d84bd940cfb093cdc60e569f15cad58772a51dca; prior note 4574db5e11603f8600cb7f6f18c7d0d18597232e. Preserve original authors including EM-DIRECT-D03BC9. This is author-side computation, not independent acceptance of own work.

## Result
Under the previous note's upstream high-valuation cancellation and maximum prime 13 hypothesis, for valuation-one atoms d=13(13q+r), 1<=r<=12, 13-smooth u=13q+r, cost d-1=169q+13r-1, each side cap2331, equality of the six reciprocal moments forces equality of F=(sum u^(-k) mod 13^k)_{k=1..6}. The mixed radix key is injective on this tuple (less than 13^21). Q=sum q. Q<=13. Previous note excluded q23 split(11,12) and all q24..26; q>=27 is impossible by cap. This note excludes the remaining q23 split(10,13), up to sign. Thus all q23..26 are excluded under the stated reduction.

## Exact separated enumeration
Separate a nondecreasing positive-q multiset P from its q=0 multiset H. Each profile has a unique decomposition even with repeated atoms. Enumerate H once, sorted by residual cost; all costs <=641. For each P of Q=10 and residual cost w<=641, combine precisely the prefix of H with cost<=641-w. The same representation builds the Q13 target set with cap134. Suffix minimum-cost DP for positive q only drops impossible completions. The three low components are a necessary filter and the full six components are compared exactly for every survivor. No common-support filter, no probability, no rounding, no lower-prime completion assumption beyond the original necessary congruences. Same-signature Q13 duplicates are zero, as before.

Independent JS unbounded coin DP and convolution:
positive Q10 profiles=306988; horizontal profiles cost<=641=729803; sum over residual cost c of positive_count[c]*horizontal_prefix[641-c]=1328547997. Counts are exact as all intermediate counts here are below 2^53. The executed C++ count is the same. Q13 target count=5775; low-three matching Q10 profiles=1328729; full matches=0. Executed g++ -O3 -std=c++17, return code0, elapsed 11.569 seconds wall including enumeration and join (compile excluded). Progress totals at positive counts 50000,100000,150000,200000,250000,300000: 597598665,908459978,1043185625,1186024137,1284231335,1325325688. Final 1328547997. Prior interrupted full DFS is not reused as evidence. No q11..22 or global T6 closure is claimed. Next possible route: use this separated join with cost-sliced signature target sets and cancellation disjointness, or audit the upstream valuation reduction.

## Executed C++17 reproduction
```cpp
#include <bits/stdc++.h>
using namespace std; using I=uint64_t; using U=__uint128_t;
constexpr int B=2331; constexpr int M[6]={13,169,2197,28561,371293,4826809};
struct Atom{int q,r,w;array<int,6>s;};vector<Atom>a; int npos;
int inv(int a,int m){int64_t x=0,y=1,b=m;while(a){int t=b/a,z=b-t*a;b=a;a=z;int64_t u=x-t*y;x=y;y=u;}assert(b==1);return (x%m+m)%m;}
bool smooth(int a){for(int p:{2,3,5,7,11,13})while(a%p==0)a/=p;return a==1;}
void init(){for(int q=13;q>=0;q--)for(int r=1;r<13;r++)if(smooth(13*q+r)){Atom t{q,r,13*r-1,{}};for(int j=0;j<6;j++){int v=inv(13*q+r,M[j]);int64_t x=1;for(int k=0;k<=j;k++)x=x*v%M[j];t.s[j]=x;}a.push_back(t);if(q)npos++;}assert(a.size()==78);}
struct Profile{array<int,6>s;int w;};
vector<Profile> h, pos;
vector<array<int,14>> mn;
array<int,6> add(const array<int,6>&x,const array<int,6>&y){array<int,6>z;for(int j=0;j<6;j++){int v=x[j]+y[j];z[j]=v>=M[j]?v-M[j]:v;}return z;}
void horizontal(int i,int c,int w,const array<int,6>&s){h.push_back({s,w});for(int j=i;j<(int)a.size();j++)if(a[j].w<=c)horizontal(j,c-a[j].w,w+a[j].w,add(s,a[j].s));}
void positive(int i,int q,int c,int w,const array<int,6>&s){if(q==0){pos.push_back({s,w});return;}for(int j=i;j<npos;j++)if(a[j].q<=q&&a[j].w<=c&&mn[j][q-a[j].q]<=c-a[j].w)positive(j,q-a[j].q,c-a[j].w,w+a[j].w,add(s,a[j].s));}
U key(const array<int,6>&s){U k=0;for(int j=5;j>=0;j--)k=k*M[j]+s[j];return k;}
int low(const array<int,6>&s){return s[0]+13*(s[1]+169*s[2]);}
int main(){init();mn.resize(npos+1);mn[npos].fill(100000);mn[npos][0]=0;for(int i=npos-1;i>=0;i--){mn[i][0]=0;for(int q=1;q<=13;q++){mn[i][q]=mn[i+1][q];if(q>=a[i].q)mn[i][q]=min(mn[i][q],a[i].w+mn[i][q-a[i].q]);}}
horizontal(npos,641,0,{});sort(h.begin(),h.end(),[](auto&x,auto&y){return x.w<y.w;});
array<size_t,642> lim{};size_t z=0;for(int c=0;c<=641;c++){while(z<h.size()&&h[z].w<=c)z++;lim[c]=z;}
positive(0,13,134,0,{});vector<U> keys;vector<uint8_t> filter(4826809);for(auto&p:pos)for(size_t i=0;i<lim[134-p.w];i++){auto s=add(p.s,h[i].s);keys.push_back(key(s));filter[low(s)]=1;}sort(keys.begin(),keys.end());assert(keys.size()==5775);assert(adjacent_find(keys.begin(),keys.end())==keys.end());cerr<<"Q13 "<<keys.size()<<endl;
pos.clear();positive(0,10,641,0,{});cerr<<"pos "<<pos.size()<<" hor "<<h.size()<<endl;
I total=0,lowhits=0,full=0;int done=0;
for(auto&p:pos){size_t n=lim[641-p.w];total+=n;int x=p.s[0],y=p.s[1],z=p.s[2];for(size_t i=0;i<n;i++){auto&v=h[i].s;int x1=x+v[0],y1=y+v[1],z1=z+v[2];if(x1>=13)x1-=13;if(y1>=169)y1-=169;if(z1>=2197)z1-=2197;if(filter[x1+13*(y1+169*z1)]){lowhits++;auto s=add(p.s,v);if(binary_search(keys.begin(),keys.end(),key(s)))full++;}}if(++done%50000==0)cerr<<"progress "<<done<<" "<<total<<" "<<lowhits<<" "<<full<<endl;}
cout<<"complete "<<total<<" low "<<lowhits<<" full "<<full<<endl;assert(total==1328547997ULL);
}
```
## Control
Current gateway status succeeded. Original own recovery request dvr-20261124-2000-own-recovery-metadata-v1 read returned CONTROL_REQUEST_NOT_FOUND; no replay. Driver r553 authenticated; backlog r472 preserves DCMP11 selection and dependency evidence with no available worker confirmed; onhour r138 reports 127/127 author family records and aggregation pending. Do not repeat their work. Formal T6 protected p17 q14 scope remains separate; no native review, Result, formal Task or mother-objective completion from this author-side unit.
