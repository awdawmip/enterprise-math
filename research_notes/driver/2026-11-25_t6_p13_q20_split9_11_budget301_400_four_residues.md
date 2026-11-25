# T6 p13 q20 split(9,11): exact four-residue continuation, budgets 301..400

2026-11-25; existing Driver lane, own scientific contribution. Retain the prior definitions, p13 valuation-one domain, both mass caps 2331, high-valuation/common cancellation and H0..H6 observer. Previous immutable source: 0c62b01b9034cd71d5d6142c0490bd753fa2301e:research_notes/driver/2026-11-25_t6_p13_q20_split9_11_budget300_four_residues.md.

The same exact C++ algorithm was executed locally for c=301..400 only (not redoing 0..300). Here c=810-w(P), w(P) is residual positive-vertical multiset weight, H has residual mass <=c. Q11 target side is complete. The necessary residues k=4,5,6,1 use exact disjoint bit fields, hash bitmap only filters and every survivor undergoes exact comparison. Coin DP counts the full multiset domain independently of the recursive enumeration; modulo-four P-index classes partition the band. No matches.

Actual output: g++ -O3 -march=native -std=c++17 -pthread q.cpp -o q; /usr/bin/time -v ./q 301 400
```
Q=9 full=8963595909 P=186647 H=30227
band=301..400 expected=627537422 P=40917
Q=11 full=100750914 P=246181 H=87579
targets unique=100750914
group 0 P=10175 profiles=156341634 filter=14003845 hits=0
group 3 P=10181 profiles=154893588 filter=13874018 hits=0
group 2 P=10315 profiles=158308701 filter=14180129 hits=0
group 1 P=10246 profiles=157993499 filter=14142405 hits=0
TOTAL 627537422 filter=56200397 hits=0
Elapsed wall 24.96s; user 59.59s; system 0.64s; peak RSS 950612 KiB; exit status 0.
```
Cumulative budgets 0..400: 757267116 profiles; 8206328793 remain (401..810). q20(9,11) and (10,10) remain open. No new Result, Review, Task completion or mother closure. Prior q20(7,13),(8,12) retained. Next 401 onward.

Reproduction source (same as prior):
```cpp
#include <bits/stdc++.h>
using namespace std; using U=uint64_t; using S=array<int,4>; constexpr int M[]={28561,371293,4826809,13};
struct A{int q,w;S s;};struct R{int w;S s;};
S add(S x,S y){for(int k=0;k<4;k++){x[k]+=y[k];if(x[k]>=M[k])x[k]-=M[k];}return x;}
U key(S s){return U(s[0])|(U(s[1])<<15)|(U(s[2])<<34)|(U(s[3])<<57);}
bool smooth(int n){for(int d:{2,3,5,7,11,13})while(n%d==0)n/=d;return n==1;}
int inv(int a,int m){long x=0,y=1;int b=m;while(a){int t=b/a,z=b-t*a;b=a;a=z;long u=x-t*y;x=y;y=u;}assert(b==1);return (x%m+m)%m;}
struct D{int Q,B;vector<A>a;vector<R>p,h;vector<U>hc,pd;U full=0;
void pg(int i,int q,int w,S s){if(!q){p.push_back({w,s});return;}for(int j=i;j<(int)a.size();j++)if(a[j].q&&a[j].q<=q&&w+a[j].w<=B)pg(j,q-a[j].q,w+a[j].w,add(s,a[j].s));}
void hg(int i,int w,S s,int cap){h.push_back({w,s});for(int j=i;j<(int)a.size();j++)if(!a[j].q&&w+a[j].w<=cap)hg(j,w+a[j].w,add(s,a[j].s),cap);}
D(int q,int cap):Q(q),B(2331-169*q){for(int j=Q;j>=0;j--)for(int r=1;r<=12;r++)if(smooth(13*j+r)){A t{j,13*r-1,{}};for(int k=0;k<4;k++){long v=inv(13*j+r,M[k]),z=1;for(int n=0;n<(k==3?1:k+4);n++)z=z*v%M[k];t.s[k]=z;}a.push_back(t);}pg(0,Q,0,{});hg(0,0,{},cap);sort(h.begin(),h.end(),[](auto&x,auto&y){return x.w<y.w;});hc.assign(B+1,0);hc[0]=1;for(auto&t:a)if(!t.q)for(int w=t.w;w<=B;w++)hc[w]+=hc[w-t.w];partial_sum(hc.begin(),hc.end(),hc.begin());assert(h.size()==hc[cap]);vector<vector<U>>dp(Q+1,vector<U>(B+1));dp[0][0]=1;for(auto&t:a)if(t.q)for(int j=t.q;j<=Q;j++)for(int w=t.w;w<=B;w++)dp[j][w]+=dp[j-t.q][w-t.w];pd=dp[Q];assert(accumulate(pd.begin(),pd.end(),U(0))==p.size());for(int w=0;w<=B;w++)full+=pd[w]*hc[B-w];cerr<<"Q="<<Q<<" full="<<full<<" P="<<p.size()<<" H="<<h.size()<<endl;}};
U hash64(U k){k^=k>>30;k*=0xbf58476d1ce4e5b9ULL;k^=k>>27;k*=0x94d049bb133111ebULL;return k^(k>>31);}
int main(int argc,char**argv){int lo=atoi(argv[1]),hi=atoi(argv[2]);D d(9,hi);assert(d.full==8963595909ULL);U expect=0,np=0;for(int w=0;w<=d.B;w++)if(d.B-w>=lo&&d.B-w<=hi){expect+=d.pd[w]*d.hc[d.B-w];np+=d.pd[w];}cerr<<"band="<<lo<<".."<<hi<<" expected="<<expect<<" P="<<np<<endl;if(argc>3)return 0;D t(11,472);assert(t.full==100750914);vector<U>keys;keys.reserve(t.full);constexpr int bits=30;vector<U>bm(1ULL<<(bits-6));for(auto &x:t.p)for(size_t j=0;j<t.hc[t.B-x.w];j++){U k=key(add(x.s,t.h[j].s));keys.push_back(k);U b=hash64(k)>>(64-bits);bm[b>>6]|=1ULL<<(b&63);}assert(keys.size()==t.full);sort(keys.begin(),keys.end());keys.erase(unique(keys.begin(),keys.end()),keys.end());cerr<<"targets unique="<<keys.size()<<endl;constexpr int prefix=22,shift=61-prefix;vector<uint32_t>ix((1<<prefix)+1);size_t off=0;for(size_t i=0;i<ix.size();i++){while(off<keys.size()&&(keys[off]>>shift)<i)off++;ix[i]=off;}assert(off==keys.size());U total=0,ps=0,bh=0,hit=0;mutex mu;vector<thread>workers;for(int z=0;z<4;z++)workers.emplace_back([&,z]{U n=0,pn=0,bh0=0,hit0=0;for(size_t i=z;i<d.p.size();i+=4){auto &x=d.p[i];int c=d.B-x.w;if(c<lo||c>hi)continue;pn++;size_t cnt=d.hc[c];n+=cnt;for(size_t j=0;j<cnt;j++){U k=key(add(x.s,d.h[j].s));U b=hash64(k)>>(64-bits);if(!(bm[b>>6]>>(b&63)&1))continue;bh0++;auto pr=k>>shift;if(binary_search(keys.begin()+ix[pr],keys.begin()+ix[pr+1],k)){hit0++;lock_guard<mutex>l(mu);cout<<"HIT "<<k<<" P "<<i<<" H "<<j<<endl;}}}lock_guard<mutex>l(mu);total+=n;ps+=pn;bh+=bh0;hit+=hit0;cout<<"group "<<z<<" P="<<pn<<" profiles="<<n<<" filter="<<bh0<<" hits="<<hit0<<endl;});for(auto&x:workers)x.join();assert(total==expect&&ps==np);cout<<"TOTAL "<<total<<" filter="<<bh<<" hits="<<hit<<endl;return hit?2:0;}
```
