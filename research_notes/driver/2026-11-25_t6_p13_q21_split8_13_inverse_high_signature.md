# T6 p13 q21 split(8,13): exact inverse high-signature exclusion
2026-11-25. Driver historical lane EM-DVR-DEBB5E, author-side mathematical contribution; not a decisive independent review. Reuse the exact T6 taskbook and the high-valuation cancellation at cd764082e3080198d5df0ecd3a3fcc3ee4a560b7, q22 note 013568fc822005bef9ebfd38a53d8c22bbb3a45b. Preserve onhour q11 and p17 q14 separate contributions.

## Statement
Under the T6 shape moment identities H0..H6, side mass <=2331, maximal prime 13, cancel equal atoms and the valuation >=2 layers by the previously verified lemma. Write d=13u, u=13q+r, 1<=r<=12, u 13-smooth, and residual mass w=13r-1. For a side of total Q, residual mass <=B(Q)=2331-169Q. Moment equality forces equality of the high residual signature G=(sum u^(-k) mod 13^k) for k=4,5,6, since lower valuations vanish after multiplying by 13^k. A configuration of Q8 is uniquely its positive-q multiset P and horizontal q0 multiset H, with w(P)+w(H)<=979. A Q13 target T has residual budget 134. Thus any match necessarily satisfies G(H)=G(T)-G(P) componentwise in the exact three residue groups.

Enumerate each positive multiset once in nondecreasing atom-index order, retaining repeats. Enumerate all horizontal multisets of cost <=979 (an intentional superset, since P costs positive mass). Index by exact 57-bit high key, retaining minimum mass for each key. Since each component is less than its allotted 15/19/23-bit lane, this packing is injective. The hash bitmap is only a necessary membership filter; all hits are checked by exact sorted-key binary search. If a key exists, minimum mass suffices for feasibility of this projected match; no match occurs even before the remaining mass restriction. Independently count full domains by unbounded integer coin DP and compare with the convolution of actual generated P and H cost histograms. Distinct Q imply different profiles; any collision must hit the index, so zero hits proves exclusion of the whole split and reverse sign.

## Executed result
Q13: P=1368, H=143, full=5775.
Q8: P=78410, H=19937556, full=37377606512.
All 19937556 horizontal high keys distinct (within this domain).
Exact inverse queries=452817750, bitmap hits=16514181, exact horizontal high hits=0, mass-valid=0.
g++ -O3 -std=c++17, wall 30.52 seconds, peak RSS 693376 KiB, exit 0. Independent DP and generated cost convolution agree for both Q. No claim of global T6 closure. q21 splits (9,12),(10,11) remain. The horizontal injectivity is an additional bounded statement (cost <=979), not a claim of global signature completeness.

## Reproduction (equivalent compact C++17)
```cpp
#include <bits/stdc++.h>
using namespace std;using U=uint64_t;
constexpr int M[3]={28561,371293,4826809};
struct S{array<int,3>x{};};struct A{int q,w;S s;};struct P{int w;S s;};
int B,Q;vector<A>a;vector<P>pos,hor;
bool smooth(int x){for(int p:{2,3,5,7,11,13})while(x%p==0)x/=p;return x==1;}
int inv(int a,int m){int64_t x=0,y=1,b=m;while(a){int t=b/a,z=b-t*a;b=a;a=z;int64_t u=x-t*y;x=y;y=u;}assert(b==1);return (x%m+m)%m;}
S add(S a,S b){for(int k=0;k<3;k++){a.x[k]+=b.x[k];if(a.x[k]>=M[k])a.x[k]-=M[k];}return a;}
S sub(S a,S b){for(int k=0;k<3;k++){a.x[k]-=b.x[k];if(a.x[k]<0)a.x[k]+=M[k];}return a;}
U key(S s){return U(s.x[0])|(U(s.x[1])<<15)|(U(s.x[2])<<34);}
U mix(U x){x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;x*=0x94d049bb133111ebULL;return x^(x>>31);}
void gen(int i,int q,int w,S s){if(!q){pos.push_back({w,s});return;}for(int j=i;j<(int)a.size();j++)if(a[j].q>0&&a[j].q<=q&&w+a[j].w<=B)gen(j,q-a[j].q,w+a[j].w,add(s,a[j].s));}
void hgen(int i,int w,S s){hor.push_back({w,s});for(int j=i;j<(int)a.size();j++)if(!a[j].q&&w+a[j].w<=B)hgen(j,w+a[j].w,add(s,a[j].s));}
U init(int q){Q=q;B=2331-169*q;a.clear();pos.clear();hor.clear();for(int i=q;i>=0;i--)for(int r=1;r<13;r++)if(smooth(13*i+r)){A t{i,13*r-1,{}};for(int k=0;k<3;k++){int v=inv(13*i+r,M[k]);int64_t z=1;for(int j=0;j<k+4;j++)z=z*v%M[k];t.s.x[k]=z;}a.push_back(t);}gen(0,Q,0,{});hgen(0,0,{});vector<vector<U>>dp(Q+1,vector<U>(B+1));dp[0][0]=1;for(auto&t:a)for(int q=t.q;q<=Q;q++)for(int w=t.w;w<=B;w++)dp[q][w]+=dp[q-t.q][w-t.w];U count=accumulate(dp[Q].begin(),dp[Q].end(),U(0));vector<U>hist(B+1);for(auto&h:hor)hist[h.w]++;partial_sum(hist.begin(),hist.end(),hist.begin());U total=0;for(auto&p:pos)total+=hist[B-p.w];assert(total==count);cout<<"Q "<<Q<<" P "<<pos.size()<<" H "<<hor.size()<<" DP "<<count<<endl;return count;}
struct K{U k;int w;bool operator<(const K&b)const{return k<b.k||(k==b.k&&w<b.w);}};
int main(){U n=init(13);vector<S> targets;for(auto&p:pos)for(auto&h:hor)if(p.w+h.w<=B)targets.push_back(add(p.s,h.s));assert(targets.size()==n);U count=init(8);vector<K>keys;keys.reserve(hor.size());constexpr U mask=(1ULL<<29)-1;vector<U>bitmap(1<<23);for(auto&h:hor){U k=key(h.s);keys.push_back({k,h.w});U b=mix(k)&mask;bitmap[b>>6]|=1ULL<<(b&63);}sort(keys.begin(),keys.end());size_t j=0;for(size_t i=0;i<keys.size();i++)if(i==0||keys[i].k!=keys[i-1].k)keys[j++]=keys[i];keys.resize(j);cout<<"unique horizontal high keys "<<j<<endl;U queries=0,bhits=0,khits=0,valid=0;for(auto&p:pos)for(auto&t:targets){queries++;auto k=key(sub(t,p.s));U b=mix(k)&mask;if(!(bitmap[b>>6]>>(b&63)&1))continue;bhits++;auto it=lower_bound(keys.begin(),keys.end(),K{k,0});if(it!=keys.end()&&it->k==k){khits++;if(it->w+p.w<=B){valid++;cout<<"mass-valid high-three hit "<<k<<" "<<it->w<<" "<<p.w<<endl;}}}assert(queries==pos.size()*targets.size());cout<<"queries "<<queries<<" bitmap hits "<<bhits<<" exact horizontal high hits "<<khits<<" mass-valid "<<valid<<endl;return valid?2:0;}
```

Next: q21 (9,12) and (10,11). Avoid assuming high-three injectivity for larger domains; preserve actual low-component or lower-prime completion obligations on any hit. No task/Result acceptance or new claim is asserted. Prior r556 and backlog r475 verified; onhour r145 listed, preserve active q11 scope.