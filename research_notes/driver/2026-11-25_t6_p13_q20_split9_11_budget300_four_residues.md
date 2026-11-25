# T6 p13 q20 split(9,11): budget 0..300, four exact residues
2026-11-25; Driver lane own scientific contribution, not independent decisive review or a frozen Result.

Scope: same H0..H6 shape observer, both original mass budgets <=2331, maximal prime 13, higher valuation/common atom cancellation as in the preceding q20(8,12) note at 3d75222684d0e92cda6dbdf5200384e3e1e75b91. Each surviving valuation-one atom d=13(13q+r), 1<=r<=12, has 13-smooth u=13q+r and mass 169q+13r-1. Multiplying the k-th moment equality by 13^k gives the necessary residue sum equality mod 13^k. In this run use k=4,5,6 AND k=1; the fourth component is exact, not a probabilistic filter. This reduces possible high-three collisions without excluding any true solution. Pack components in disjoint 15,19,23,4 bit slots (61 bits). Unsigned hash bitmap only prefilters: exact equal keys necessarily set the same bit, followed by exact binary search in the prefix bucket. No floating point.

For Q9 B=810 and Q11 B=472, enumerate positive vertical multiset P, horizontal multiset H separately in nondecreasing atom indices (repeats permitted). Cost of residual atoms is 13r-1; H sorted by cost, hc[c] from independent coin DP includes every tie at cost<=c. c=B-w(P). All Q11 targets are enumerated; Q9 restricts c=0..300 only. Positive configuration counts and full profiles checked against independent DP. Four disjoint P-index residue classes partition the chosen Q9 band. Q9 full domain 8,963,595,909; Q11 full domain 100,750,914. Q9 0..300 has 129,729,694 configurations; zero exact four-residue matches. Remaining c=301..810 includes 8,833,866,215 configurations. q20(9,11) remains OPEN; (10,10) remains OPEN. The q20(7,13),(8,12) prior results are retained.

Actual run, g++ -O3 -march=native -std=c++17 -pthread q.cpp -o q; /usr/bin/time -v ./q 0 300:
```
Q=9 full=8963595909 P=186647 H=5612
band=0..300 expected=129729694 P=98340
Q=11 full=100750914 P=246181 H=87579
targets unique=100750914
group 2 P=24530 profiles=32231535 filter=2888391 hits=0
group 0 P=24584 profiles=32657101 filter=2927215 hits=0
group 3 P=24600 profiles=32444999 filter=2907071 hits=0
group 1 P=24626 profiles=32396059 filter=2898790 hits=0
TOTAL 129729694 filter=11621467 hits=0
Elapsed wall 25.86s; peak RSS 949028 KiB; exit status 0.
```
Independent DP count-only runs also establish c=0..400 757267116, c=401..450 675010922, c=451..500 1155169353, c=0..500 2587447391; these are planning counts only, not completed exclusions. No performance improvement against a same-input benchmark is asserted.

Executed C++ source:
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

Next: continue disjoint c bands from 301; use exact four-residue test. If a real match appears, decode both multiset rosters, test all six residue components and lower-prime/H0 completion; do not call a necessary-residue match a solution. The prior q10 and q21..26 exclusions and budget cap q>=27 are retained. No claim, Result admission, independent review or mother closure is asserted.
