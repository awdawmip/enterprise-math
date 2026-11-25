# T6 p13 q20 split(8,12): exact partial budget-band exclusion
2026-11-25, continuing Driver lane checkpoint r560. Author-side calculation; not independent decisive review or a frozen Result.

## Claim
Use the same T6 H0..H6, maximal prime 13, higher valuation/common-atom cancellation and side mass <=2331 as the prior r560 note at 0115ed0663271e57d726f352dc84300186156cb7. At v13(d)=1 put d=13u, u=13q+r, 1<=r<=12, u 13-smooth. For side Q, B=2331-169Q, residual cost w=13r-1. A complete profile splits uniquely into positive-q P and q0 H; define c=B-w(P). For Q8 vs Q12 the entire band 0<=c<=600 has no matching high-three signature G=(sum u^(-k) mod 13^k) for k=4,5,6. Multiplying the kth original moment identity by 13^k and reducing modulo 13^k shows G equality is necessary after higher valuation cancellation.

Generate nondecreasing atom-index multisets, with repeated indices allowed. On Q12 (B=303) build the complete set of signatures. On Q8 (B=979) generate every P whose c belongs to the band, and every H with cost <=c, via sorted horizontal prefix. The key packs 15/19/23 bits without overlap. The 2^27-bit hash bitmap is a necessary membership filter only; exact sorted key comparison in the prefix interval decides each hit. Positive-index classes modulo 4 partition P. Independent unbounded coin DP for positive and horizontal atoms gives exact band count sum_w P_8(w) H(979-w) over c in the band. Assertions compare actual enumeration and DP. No floating point enters the test.

## Executed results
Q12: P=58880 H=5989 full=2583672; unique targets=2583672. Q8 total DP=37377606512.
| c band | P | H (cap upper endpoint) | exact Q8 profiles | bitmap hits | exact G hits | wall sec | max RSS KiB |
|---|---:|---:|---:|---:|---:|---:|---:|
|0..500|40610|128402|1322231747|25214135|0|8.14|45460|
|501..600|17926|452163|4529632213|86364966|0|25.85|56728|
Both exits 0, coverage assertions passed. Combined 5851863960 profiles, 111579101 bitmap survivors, zero exact matches. 601..700 attempted: Q8 P=12987, H=1393138, expected DP 10706689480; process call timed out after initial count, no completed group log obtained. That band is NOT credited. Remaining c=601..979: 31525742552 profiles; split(8,12) remains open. Also remaining q20 splits (9,11),(10,10). Preserve independent q11 / p17 q14 scopes.

## Reproduction
Compile g++ -O3 -std=c++17 -pthread; run with arguments 0 500, 501 600. For remaining use smaller disjoint bands and save complete group logs. The actual source follows.
```cpp
#include <bits/stdc++.h>
using namespace std;using U=uint64_t;using S=array<int,3>;constexpr int M[]={28561,371293,4826809};struct A{int q,w;S s;};struct P{int w;S s;};vector<A>a;vector<P>p,h;int B;
S add(S x,S y){for(int k=0;k<3;k++){x[k]+=y[k];if(x[k]>=M[k])x[k]-=M[k];}return x;}
U key(S s){return U(s[0])|(U(s[1])<<15)|(U(s[2])<<34);}
U mix(U x){x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;x*=0x94d049bb133111ebULL;return x^(x>>31);}
bool smooth(int n){for(int d:{2,3,5,7,11,13})while(n%d==0)n/=d;return n==1;}
int inv(int a,int m){long x=0,y=1;int b=m;while(a){int t=b/a,z=b-t*a;b=a;a=z;long u=x-t*y;x=y;y=u;}assert(b==1);return (x%m+m)%m;}
void gen(int i,int q,int w,S s){if(!q){p.push_back({w,s});return;}for(int j=i;j<(int)a.size();j++)if(a[j].q>0&&a[j].q<=q&&w+a[j].w<=B)gen(j,q-a[j].q,w+a[j].w,add(s,a[j].s));}
void hg(int i,int w,S s,int cap){h.push_back({w,s});for(int j=i;j<(int)a.size();j++)if(!a[j].q&&w+a[j].w<=cap)hg(j,w+a[j].w,add(s,a[j].s),cap);}
vector<U> init(int Q,bool positive){B=2331-169*Q;a.clear();p.clear();h.clear();for(int q=Q;q>=0;q--)for(int r=1;r<13;r++)if(smooth(13*q+r)){A t{q,13*r-1,{}};for(int k=0;k<3;k++){long z=1,v=inv(13*q+r,M[k]);for(int j=0;j<k+4;j++)z=z*v%M[k];t.s[k]=z;}a.push_back(t);}gen(0,Q,0,{});vector<vector<U>>dp(Q+1,vector<U>(B+1));dp[0][0]=1;for(auto&t:a)if(!positive||t.q)for(int q=t.q;q<=Q;q++)for(int w=t.w;w<=B;w++)dp[q][w]+=dp[q-t.q][w-t.w];return dp[Q];}
int main(int argc,char**argv){int lo=atoi(argv[1]),hi=atoi(argv[2]);auto d=init(12,false);hg(0,0,{},B);vector<U>keys;for(auto&x:p)for(auto&y:h)if(x.w+y.w<=B)keys.push_back(key(add(x.s,y.s)));assert(keys.size()==accumulate(d.begin(),d.end(),U(0)));cout<<"Q12 P="<<p.size()<<" H="<<h.size()<<" full="<<keys.size()<<endl;sort(keys.begin(),keys.end());keys.erase(unique(keys.begin(),keys.end()),keys.end());cout<<"unique targets="<<keys.size()<<endl;constexpr U mask=(1ULL<<27)-1;vector<U>bm(1<<21);for(U k:keys){U b=mix(k)&mask;bm[b>>6]|=1ULL<<(b&63);}vector<size_t>ix((1<<18)+1);size_t off=0;for(size_t i=0;i<ix.size();i++){while(off<keys.size()&&(keys[off]>>39)<i)off++;ix[i]=off;}
auto pd=init(8,true);hg(0,0,{},hi);sort(h.begin(),h.end(),[](auto&x,auto&y){return x.w<y.w;});vector<U>hc(B+1);hc[0]=1;for(auto&t:a)if(!t.q)for(int w=t.w;w<=B;w++)hc[w]+=hc[w-t.w];partial_sum(hc.begin(),hc.end(),hc.begin());assert(h.size()==hc[hi]);U expect=0,pn=0,full=0;for(int w=0;w<=B;w++){full+=pd[w]*hc[B-w];if(B-w>=lo&&B-w<=hi){expect+=pd[w]*hc[B-w];pn+=pd[w];}}cout<<"Q8 full DP="<<full<<" budget ["<<lo<<","<<hi<<"] P="<<pn<<" H="<<h.size()<<" expected="<<expect<<endl;
U total=0,bhits=0,hits=0,npos=0;mutex mu;vector<thread>workers;for(int z=0;z<4;z++)workers.emplace_back([&,z]{U n=0,bh=0,kh=0,np=0;for(size_t i=z;i<p.size();i+=4){auto&x=p[i];int cap=B-x.w;if(cap<lo||cap>hi)continue;np++;for(auto&y:h){if(y.w>cap)break;n++;U k=key(add(x.s,y.s)),b=mix(k)&mask;if(!(bm[b>>6]>>(b&63)&1))continue;bh++;auto pref=k>>39;if(binary_search(keys.begin()+ix[pref],keys.begin()+ix[pref+1],k)){kh++;lock_guard<mutex>l(mu);cout<<"HIT key="<<k<<" Pindex="<<i<<" Pcost="<<x.w<<" Hcost="<<y.w<<endl;}}}lock_guard<mutex>l(mu);total+=n;bhits+=bh;hits+=kh;npos+=np;cout<<"group "<<z<<" P="<<np<<" full="<<n<<" bitmap="<<bh<<" exact="<<kh<<endl;});for(auto&t:workers)t.join();assert(total==expect&&npos==pn);cout<<"TOTAL "<<total<<" bitmap="<<bhits<<" exact="<<hits<<endl;return hits?2:0;}
```
