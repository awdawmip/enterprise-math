# T6 p13 q20 split(8,12): complete exact budget join
2026-11-25. Driver lane, own scientific contribution; author-side computation, not independent decisive review or frozen Result.

## Scope and result
Retain the exact T6 H0..H6 shape observer, both masses <=2331, maximal prime 13 and previously proved higher valuation/common atom cancellation. For v13(d)=1, d=13u, u=13q+r, 1<=r<=12, u 13-smooth. Each atom costs 169q+13r-1. Multiplying kth reciprocal-moment identity by 13^k and reducing modulo 13^k eliminates lower valuation atoms. Therefore equality of G(U)=(sum u^(-k) mod 13^k) for k=4,5,6 is necessary. On Q8 vs Q12, no legal pair has equal G. This closes the signed split, not q20 or the mother objective. The original partial 0..600 source is https://github.com/awdawmip/enterprise-math/blob/30b5752c0acea7971ae8901908c465d048630fe9/research_notes/driver/2026-11-25_t6_p13_q20_split8_12_budget600_partial.md .

## Exact enumeration
Use the prior nondecreasing multiset enumeration and independent coin DP. For Q8 B=979, c=B-w(P); for Q12 B=303. Every P and H is unique as an atom-index multiset, with repeats retained, H ordered by cost. For each P, the first hc[c] horizontal records are exactly those with cost <=c (including all equal-cost ties). The four P-index classes modulo 4 exhaust the domain. All Q12 targets (2,583,672, distinct) are indexed. The hash bitmap is only a necessary test, with unsigned 32-bit multiplication/addition modulo 2^32; equal G has equal hash so no false negative. The exact 57-bit packed key remains unchanged and exact binary search within the prefix interval decides hits. No floating point. Actual group counts and positive-roster counts agree with the independent DP assertions. Previous timed-out 601..700 attempt had no completed group and is not credited; the new two disjoint bands cover it.

| c | P | H (cap upper endpoint) | actual profiles | bitmap survivors | exact hits | elapsed s | peak RSS KiB |
|---|---:|---:|---:|---:|---:|---:|---:|
|601..620|2917|566167|1499564840|111130885|0|5.12|54424|
|621..700|10070|1393138|9207124640|682417249|0|33.52|83608|
|701..750|3466|2352719|6471808476|479508779|0|24.36|127388|
|751..800|1938|3886294|5789616214|429104318|0|21.67|127384|
|801..979|1483|19937556|8557628382|634073685|0|34.49|586160|
All five exits 0. Each target initialization: P=58880, H=5989, full=2583672, unique targets=2583672; each Q8 full DP=37377606512. Newly covered 31525742552, survivors 2336234916, exact hits 0. New elapsed sum 119.16s (separate invocations, not benchmark against earlier different bands). Prior 0..600 count 5851863960 plus this new 31525742552 = 37377606512, exact Q8 total. Whole split(8,12) excluded.

Actual group output (group, P, full, bitmap, exact):
```
601..620:
3 726 373510318 27681305 0
0 746 381773902 28286385 0
2 722 372297681 27593926 0
1 723 371982939 27569269 0
621..700:
3 2493 2266049637 167878821 0
0 2502 2284778671 169272604 0
1 2514 2308076026 171233393 0
2 2561 2348220306 174032431 0
701..750:
1 860 1604697035 118897150 0
2 850 1591123456 117922406 0
3 865 1620426454 120060586 0
0 891 1655561531 122628637 0
751..800:
1 484 1437442746 106569030 0
3 470 1416207906 104984394 0
2 480 1426607177 105675118 0
0 504 1509358385 111875776 0
801..979:
1 358 2042354743 151326795 0
3 357 2077623802 153940786 0
2 381 2182566412 161694520 0
0 387 2255083425 167111584 0
```

## Executed reproduction source
Compile g++ -O3 -march=native -std=c++17 -pthread; run with 601 620, 621 700, 701 750, 751 800, 801 979. This is the actual algorithm executed; prior source contains original 0..600 implementation. 
```cpp
#include <bits/stdc++.h>
using namespace std;using U=uint64_t;using S=array<int,3>;constexpr int M[]={28561,371293,4826809};struct A{int q,w;S s;};struct P{int w;S s;};vector<A>a;vector<P>p,h;int B;
S add(S x,S y){for(int k=0;k<3;k++){x[k]+=y[k];if(x[k]>=M[k])x[k]-=M[k];}return x;}
U key(S s){return U(s[0])|(U(s[1])<<15)|(U(s[2])<<34);}
uint32_t hash32(S s){return uint32_t(s[0])*0x9e3779b1u+uint32_t(s[1])*0x85ebca6bu+uint32_t(s[2])*0xc2b2ae35u;}
bool smooth(int n){for(int d:{2,3,5,7,11,13})while(n%d==0)n/=d;return n==1;}
int inv(int a,int m){long x=0,y=1;int b=m;while(a){int t=b/a,z=b-t*a;b=a;a=z;long u=x-t*y;x=y;y=u;}assert(b==1);return (x%m+m)%m;}
void gen(int i,int q,int w,S s){if(!q){p.push_back({w,s});return;}for(int j=i;j<(int)a.size();j++)if(a[j].q>0&&a[j].q<=q&&w+a[j].w<=B)gen(j,q-a[j].q,w+a[j].w,add(s,a[j].s));}
void hg(int i,int w,S s,int cap){h.push_back({w,s});for(int j=i;j<(int)a.size();j++)if(!a[j].q&&w+a[j].w<=cap)hg(j,w+a[j].w,add(s,a[j].s),cap);}
vector<U> init(int Q,bool positive){B=2331-169*Q;a.clear();p.clear();h.clear();for(int q=Q;q>=0;q--)for(int r=1;r<13;r++)if(smooth(13*q+r)){A t{q,13*r-1,{}};for(int k=0;k<3;k++){long z=1,v=inv(13*q+r,M[k]);for(int j=0;j<k+4;j++)z=z*v%M[k];t.s[k]=z;}a.push_back(t);}gen(0,Q,0,{});vector<vector<U>>dp(Q+1,vector<U>(B+1));dp[0][0]=1;for(auto&t:a)if(!positive||t.q)for(int q=t.q;q<=Q;q++)for(int w=t.w;w<=B;w++)dp[q][w]+=dp[q-t.q][w-t.w];return dp[Q];}
int main(int argc,char**argv){int lo=atoi(argv[1]),hi=atoi(argv[2]);auto d=init(12,false);hg(0,0,{},B);vector<U>keys;constexpr int bits=25;vector<U>bm(1<<(bits-6));for(auto&x:p)for(auto&y:h)if(x.w+y.w<=B){S s=add(x.s,y.s);keys.push_back(key(s));uint32_t b=hash32(s)>>(32-bits);bm[b>>6]|=1ULL<<(b&63);}assert(keys.size()==accumulate(d.begin(),d.end(),U(0)));cout<<"Q12 P="<<p.size()<<" H="<<h.size()<<" full="<<keys.size()<<endl;sort(keys.begin(),keys.end());keys.erase(unique(keys.begin(),keys.end()),keys.end());cout<<"unique targets="<<keys.size()<<endl;vector<size_t>ix((1<<18)+1);size_t off=0;for(size_t i=0;i<ix.size();i++){while(off<keys.size()&&(keys[off]>>39)<i)off++;ix[i]=off;}
auto pd=init(8,true);hg(0,0,{},hi);sort(h.begin(),h.end(),[](auto&x,auto&y){return x.w<y.w;});vector<U>hc(B+1);hc[0]=1;for(auto&t:a)if(!t.q)for(int w=t.w;w<=B;w++)hc[w]+=hc[w-t.w];partial_sum(hc.begin(),hc.end(),hc.begin());assert(h.size()==hc[hi]);U expect=0,pn=0,full=0;for(int w=0;w<=B;w++){full+=pd[w]*hc[B-w];if(B-w>=lo&&B-w<=hi){expect+=pd[w]*hc[B-w];pn+=pd[w];}}cout<<"Q8 full DP="<<full<<" budget ["<<lo<<","<<hi<<"] P="<<pn<<" H="<<h.size()<<" expected="<<expect<<endl;
U total=0,bhits=0,hits=0,npos=0;mutex mu;vector<thread>workers;for(int z=0;z<4;z++)workers.emplace_back([&,z]{U n=0,bh=0,kh=0,np=0;for(size_t i=z;i<p.size();i+=4){auto&x=p[i];int cap=B-x.w;if(cap<lo||cap>hi)continue;np++;size_t count=hc[cap];n+=count;for(size_t j=0;j<count;j++){auto&y=h[j];S s=add(x.s,y.s);uint32_t b=hash32(s)>>(32-bits);if(!(bm[b>>6]>>(b&63)&1))continue;bh++;U k=key(s);auto pref=k>>39;if(binary_search(keys.begin()+ix[pref],keys.begin()+ix[pref+1],k)){kh++;lock_guard<mutex>l(mu);cout<<"HIT key="<<k<<" Pindex="<<i<<" Pcost="<<x.w<<" Hcost="<<y.w<<endl;}}}lock_guard<mutex>l(mu);total+=n;bhits+=bh;hits+=kh;npos+=np;cout<<"group "<<z<<" P="<<np<<" full="<<n<<" bitmap="<<bh<<" exact="<<kh<<endl;});for(auto&t:workers)t.join();assert(total==expect&&npos==pn);cout<<"TOTAL "<<total<<" bitmap="<<bhits<<" exact="<<hits<<endl;return hits?2:0;}
```

## Continuation
q20 remaining (9,11),(10,10); q20(7,13) and (8,12) closed at stated scope. Preserve earlier q10, q21..26, q>=27 budget cap and p13/p11 higher valuation cancellation. Other q and primes/H0 remain open. Any future high-three collision must be decoded and checked against the full six residues, true side mass, common atoms and lower-prime completion; do not discard it as a mere hash hit. 
