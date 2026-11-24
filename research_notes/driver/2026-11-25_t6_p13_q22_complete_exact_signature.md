# T6: p13 q22 complete exact signature exclusion
2026-11-25. Historical Driver lane EM-DVR-DEBB5E; new author-side mathematical computation, not independent decisive review of own results. Frozen T6 scientific scope as in cd764082e3080198d5df0ecd3a3fcc3ee4a560b7 and task research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md. Preserve original author contributions, including EM-DIRECT-D03BC9, and the separate protected p17 q14 scope.

## Proposition and coverage
For a shape of exponents e_i >= 1 with side mass sum e_i <= 2331, retain denominators d=e+1. Equal H_0..H_6 imply equal reciprocal moments by the invertible binomial transform. Apply the p13 high-valuation cancellation proved at cd764082 (v>=2; three mixed congruences injective on the larger unsmoothed domain). At remaining valuation one write d=13u, u=13q+r, 1<=r<=12, u 13-smooth, q>=0. Let Q=sum q on a side. Residual cost w=13r-1, so sum w <=2331-169Q; Q<=13. Equality of reciprocal moments implies equal signatures F=(sum u^(-k) mod 13^k)_{k=1..6}. Lower valuation terms disappear on multiplication by 13^k and reduction mod 13^k.

For total q22, splits up to sign are precisely (9,13), (10,12), (11,11). Prior split(9,13) complete, cd764082, is reused. This turn proves the other two by exact injectivity/disjointness of even the high-three signature (k=4,5,6). Distinct full multisets are enumerated in nondecreasing atom order (atom order q descending, r ascending), retaining horizontal q=0 atoms and repetitions. Every profile decomposes uniquely into positive-q and horizontal profiles; sorting horizontal by residual cost allows exact budget cutoff. An independent unbounded integer coin DP counts the same domain: initialize D[0,0]=1; for each atom (q,w), update D[Q,c]+=D[Q-q,c-w] in ascending Q and c; sum D[Q,c] over c<=2331-169Q. Each atom w>0, so q=0 is valid in this recurrence.

High signature is packed injectively into a 57-bit unsigned integer with lanes 15,19,23 bits (each modulus below radix); low three components are mixed-radix packed into a uint32_t. A bitmap is only a necessary filter, not proof of equality; every hit is verified by exact sorted-key lookup. In symmetric split(11,11), injectivity means the entire valuation-one multisets must coincide; cancel them exactly, preserving the seven original identities. Such equal profiles do not constitute a maximal-p13 collision after common-atom cancellation. Lower-prime completion and other q remain open.

## Executed exact results
(11,11): P=246181, H=87579, DP and generated profiles both 100750914. Sorted all full keys; adjacent equal high keys=0, adjacent equal full keys=0, full collision groups=0. Wall 9.51 s, peak RSS 1588576 KiB, exit 0.
(10,12): Q12 P=58880, H=5989, full targets=2583672. Q10 P=306988, H=729803, DP total=1328547997. Initial monolithic attempt timed out; no coverage credited from it. Deterministic chunks, zero-based positive-profile index:
| range | exact queries | bitmap hits | high matches | full matches | wall s |
|---|---:|---:|---:|---:|---:|
|[0,8192)|212160726|2035188|0|0|10.98|
|[8192,29001)|200091499|1917116|0|0|10.07|
|[29001,68940)|250016677|2391656|0|0|12.56|
|[68940,101172)|250026106|2392393|0|0|12.04|
|[101172,195168)|250022917|2394633|0|0|12.27|
|[195168,306988)|166230072|1590883|0|0|8.47|
|total|1328547997|12721869|0|0|66.39|
All six successful executions exited normally; each range count checked with independent budget upper_bound, aggregate equals integer DP. Peak RSS 112004 KiB. Intervals partition all P indices. Thus no disjoint-profile high-three match exists in the entire q22 classification. The previous q23..26 and q10 results are retained; q>=27 is excluded by budget.

## Reproduction
C++17, g++ -O3. The following common generator and two main alternatives reproduce the actual computations; for (10,12) use chunk start and query cap arguments, with first prefix explicitly fixed to 8192 (the executed first binary used that fixed endpoint). The remaining ranges used the dynamic endpoint described in the code. The first main used a fixed-size DP array with the same recurrence; the common generator below uses the executed chunk's equivalent vector DP. Original local source hashes: symmetric c7892692fea3abf626809dd5283d36ff664d0e499e2e070294ba44b4f4322434; prefix 49c4c2fe1493231b2d2d4c4617c1fc2e9763261b6b53876000098cb7bec5d932; chunks 4b947c56fd0bdef77aaeb2c6328c7f098440b8eb96947df750cf91e33723821b.

```cpp
#include <bits/stdc++.h>
using namespace std; using U=uint64_t;
int Q=12,B=2331-169*Q; constexpr int M[6]={13,169,2197,28561,371293,4826809};
struct A{int q,w;array<int,6>s;}; vector<A>a;
struct P{int w;array<int,6>s;}; vector<P>pos,hor;
bool smooth(int x){for(int p:{2,3,5,7,11,13})while(x%p==0)x/=p;return x==1;}
int inv(int a,int m){int64_t x=0,y=1,b=m;while(a){int t=b/a,z=b-t*a;b=a;a=z;int64_t u=x-t*y;x=y;y=u;}assert(b==1);return (x%m+m)%m;}
array<int,6> add(const array<int,6>&x,const array<int,6>&y){array<int,6>z;for(int k=0;k<6;k++){z[k]=x[k]+y[k];if(z[k]>=M[k])z[k]-=M[k];}return z;}
void gen(int i,int q,int w,const array<int,6>&s){if(q==0){pos.push_back({w,s});return;}for(int j=i;j<(int)a.size();j++)if(a[j].q>0&&a[j].q<=q&&w+a[j].w<=B)gen(j,q-a[j].q,w+a[j].w,add(s,a[j].s));}
void hgen(int i,int w,const array<int,6>&s){hor.push_back({w,s});for(int j=i;j<(int)a.size();j++)if(a[j].q==0&&w+a[j].w<=B)hgen(j,w+a[j].w,add(s,a[j].s));}
struct Key{U h;uint32_t l;bool operator<(const Key&b)const{return h<b.h||(h==b.h&&l<b.l);}bool operator==(const Key&b)const{return h==b.h&&l==b.l;}};
Key key(const array<int,6>&s){return {U(s[3])|(U(s[4])<<15)|(U(s[5])<<34),uint32_t(s[0]+13*(s[1]+169*s[2]))};}
U mix(U x){x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;x*=0x94d049bb133111ebULL;return x^(x>>31);}
U init(int q){Q=q;B=2331-169*Q;a.clear();pos.clear();hor.clear();for(int q=Q;q>=0;q--)for(int r=1;r<13;r++)if(smooth(13*q+r)){A t{q,13*r-1,{}};for(int k=0;k<6;k++){int v=inv(13*q+r,M[k]);int64_t x=1;for(int j=0;j<=k;j++)x=x*v%M[k];t.s[k]=x;}a.push_back(t);}gen(0,Q,0,{});hgen(0,0,{});sort(hor.begin(),hor.end(),[](auto&x,auto&y){return x.w<y.w;});vector<vector<U>>dp(Q+1,vector<U>(B+1));dp[0][0]=1;for(auto&t:a)for(int q=t.q;q<=Q;q++)for(int w=t.w;w<=B;w++)dp[q][w]+=dp[q-t.q][w-t.w];U count=accumulate(dp[Q].begin(),dp[Q].end(),U(0));cout<<"Q "<<Q<<" P "<<pos.size()<<" H "<<hor.size()<<" DP "<<count<<endl;return count;}
int main(int argc,char**argv){
if(argc==1){
 U count=init(11);assert(count==100750914ULL);vector<Key>keys;keys.reserve(count);
 for(auto&p:pos)for(auto&h:hor){if(h.w+p.w>B)break;keys.push_back(key(add(p.s,h.s)));}
 assert(keys.size()==count);sort(keys.begin(),keys.end());U highadj=0,fulladj=0;
 for(size_t i=1;i<keys.size();i++){if(keys[i].h==keys[i-1].h)highadj++;if(keys[i]==keys[i-1])fulladj++;}
 cout<<"generated "<<keys.size()<<" adjacent high equal "<<highadj<<" adjacent full equal "<<fulladj<<endl;assert(highadj==0);return 0;
}
U n=init(12);assert(n==2583672);vector<Key>keys;keys.reserve(n);constexpr U mask=(1ULL<<28)-1;vector<U>bitmap(1<<22);
for(auto&p:pos)for(auto&h:hor){if(h.w+p.w>B)break;auto k=key(add(p.s,h.s));keys.push_back(k);U b=mix(k.h)&mask;bitmap[b>>6]|=1ULL<<(b&63);}
assert(keys.size()==n);sort(keys.begin(),keys.end());U expected=init(10),total=0,bhits=0,highhits=0,full=0;assert(expected==1328547997ULL);
size_t start=stoull(argv[1]),end=stoull(argv[2]);assert(start<=end&&end<=pos.size());
for(size_t i=start;i<end;i++){auto&p=pos[i];for(auto&h:hor){if(h.w+p.w>B)break;total++;auto k=key(add(p.s,h.s));U b=mix(k.h)&mask;if(!(bitmap[b>>6]>>(b&63)&1))continue;bhits++;auto it=lower_bound(keys.begin(),keys.end(),Key{k.h,0});for(;it!=keys.end()&&it->h==k.h;it++){highhits++;if(*it==k)full++;}}}
U check=0;for(size_t i=start;i<end;i++)check+=upper_bound(hor.begin(),hor.end(),B-pos[i].w,[](int b,const P&h){return b<h.w;})-hor.begin();
cout<<"range "<<start<<" "<<end<<" queries "<<total<<" bitmap hits "<<bhits<<" high matches "<<highhits<<" full matches "<<full<<endl;assert(total==check&&highhits==0);
}
```
Run without arguments for (11,11); run with the six explicit start/end pairs above for (10,12). Code is a consolidated equivalent reproduction, not claimed byte-identical to executed binaries.

## Coordination
Original dvr-20261125-0200-t6-current-read-v1 consumed once: SUCCEEDED, source snapshot 0fc72cdda05ca8d3d2d3da048b65476d4d16da6f, Issue240 1776 comments, as-of 2026-11-24T18:05:05Z; T6 parent HANDOFF_READY/NEEDS_DISPATCH, no live claim in that observed state, current next action is nonauthor review of p17 q14 frozen model, not this author's p13 work. Receipt is read evidence, not live write permission. Driver r555 verified. Onhour r142 q11 split(0,11) lengths4/5 complete and ongoing, preserve. Backlog r474 retains DCMP11 and no confirmed available worker, no reroll or claim. No new p13 frozen Result or independent acceptance established. No native protected write attempted, no change to schedule. Next author-side direction: q21 high-signature disjointness/injectivity, avoid active q11 research and preserve p17 independent reviewer scope.
