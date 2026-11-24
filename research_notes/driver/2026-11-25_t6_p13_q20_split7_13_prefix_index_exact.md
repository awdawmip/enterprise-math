# T6 p13 q20 split(7,13): exact high-three signature exclusion
2026-11-25. Continuing historical Driver lane EM-DVR-DEBB5E (r559); author-side computation, not a new independent decisive review or accepted Result.

## Statement and proof
Under the T6 H0..H6 identities, maximal prime 13 and side mass <=2331, cancel identical atoms and higher valuation layers using the previous verified lemma (cd764082e3080198d5df0ecd3a3fcc3ee4a560b7). For v13(d)=1 write d=13u, u=13q+r, 1<=r<=12, u 13-smooth. Each cost d-1=169q+w, w=13r-1. For a side with total Q the residual budget is B=2331-169Q. Multiplication of the kth moment identity by 13^k and reduction modulo 13^k eliminates lower-valuation atoms; hence equality of G=(sum u^(-k) mod 13^k) for k=4,5,6 is necessary.

For Q7, B=1148; Q13, B=134. Split profiles uniquely into positive-q multiset P and q0 multiset H. Nondecreasing atom indices enumerate each multiset once with repetitions. Generate every Q13 target T with both parts fitting B. For every Q7 positive part P and Q13 target T query the exact key G(T)-G(P) in the horizontal index. Use all H costing <=1148, an intentional superset; since there are zero exact matches even in this superset, no mass-valid match is possible. Reverse signs follow by symmetry.

The 15/19/23-bit fields contain each exact component separately. The bitmap only excludes absent hash bits; collisions in the hash cause extra exact comparisons, never omissions. Sorted keys with prefix h=key>>37 give half-open bounds idx[h], idx[h+1], then exact binary search. The four positive-index residue classes mod4 exhaust all P exactly once. Independent unbounded coin DP with nondecreasing atom types counts all legal full profiles, and the generated positive/horizontal cost convolution agrees. Horizontal index has no duplicate keys in this larger domain; therefore G is injective on q0 multisets costing <=1148, a new bounded conclusion.

## Executed results
First attempt timed out after generating and sorting the horizontal keys; no whole-split result attributed to it. Second attempt uses prefix bounds and 4 worker groups; it exited normally.
Q13: P=1368 H=143 DP=5775
Q7: P=28657 H=77253253 DP=106764960310
unique horizontal keys=77253253
group 0 queries=41377875 bitmap hits=2870434 exact hits=0
group 1 queries=41372100 bitmap hits=2874530 exact hits=0
group 2 queries=41372100 bitmap hits=2871794 exact hits=0
group 3 queries=41372100 bitmap hits=2873458 exact hits=0
total queries=165494175 bitmap hits=11490216 exact horizontal high hits=0
GNU time: elapsed 22.78s, user 30.80s, peak RSS 745132 KiB, exit 0. This is the successful computation's runtime, not total work including the first interrupted attempt.
Remaining q20: (8,12),(9,11),(10,10); other q/lower prime/H0 open. Preserve onhour q11 and p17 q14 distinct scopes.

## Reproduction
Compile with g++ -O3 -std=c++17 -pthread.
```cpp
#include <bits/stdc++.h>
using namespace std;using U=uint64_t;
constexpr int M[3]={28561,371293,4826809};
struct S{array<int,3>x{};};struct A{int q,w;S s;};struct P{int w;S s;};
int B,Q;vector<A>a;vector<P>pos;vector<U>hist;
bool smooth(int x){for(int p:{2,3,5,7,11,13})while(x%p==0)x/=p;return x==1;}
int inv(int a,int m){int64_t x=0,y=1,b=m;while(a){int t=b/a,z=b-t*a;b=a;a=z;int64_t u=x-t*y;x=y;y=u;}assert(b==1);return (x%m+m)%m;}
S add(S a,S b){for(int k=0;k<3;k++){a.x[k]+=b.x[k];if(a.x[k]>=M[k])a.x[k]-=M[k];}return a;}
S sub(S a,S b){for(int k=0;k<3;k++){a.x[k]-=b.x[k];if(a.x[k]<0)a.x[k]+=M[k];}return a;}
U key(S s){return U(s.x[0])|(U(s.x[1])<<15)|(U(s.x[2])<<34);}
U mix(U x){x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;x*=0x94d049bb133111ebULL;return x^(x>>31);}
void gen(int i,int q,int w,S s){if(!q){pos.push_back({w,s});return;}for(int j=i;j<(int)a.size();j++)if(a[j].q>0&&a[j].q<=q&&w+a[j].w<=B)gen(j,q-a[j].q,w+a[j].w,add(s,a[j].s));}
template<typename F>void hgen(int i,int w,S s,F& f){f(w,s);for(int j=i;j<(int)a.size();j++)if(!a[j].q&&w+a[j].w<=B)hgen(j,w+a[j].w,add(s,a[j].s),f);}
U init(int q){Q=q;B=2331-169*q;a.clear();pos.clear();hist.assign(B+1,0);for(int i=q;i>=0;i--)for(int r=1;r<13;r++)if(smooth(13*i+r)){A t{i,13*r-1,{}};for(int k=0;k<3;k++){int v=inv(13*i+r,M[k]);int64_t z=1;for(int j=0;j<k+4;j++)z=z*v%M[k];t.s.x[k]=z;}a.push_back(t);}gen(0,Q,0,{});vector<vector<U>>dp(Q+1,vector<U>(B+1));dp[0][0]=1;for(auto&t:a)for(int q=t.q;q<=Q;q++)for(int w=t.w;w<=B;w++)dp[q][w]+=dp[q-t.q][w-t.w];return accumulate(dp[Q].begin(),dp[Q].end(),U(0));}
void verify(U n){partial_sum(hist.begin(),hist.end(),hist.begin());U total=0;for(auto&p:pos)total+=hist[B-p.w];assert(total==n);cout<<"Q "<<Q<<" P "<<pos.size()<<" H "<<hist.back()<<" DP "<<n<<endl;}
int main(){U n=init(13);vector<P>h;auto f=[&](int w,S s){hist[w]++;h.push_back({w,s});};hgen(0,0,{},f);verify(n);vector<S> targets;for(auto&p:pos)for(auto&t:h)if(p.w+t.w<=B)targets.push_back(add(p.s,t.s));assert(targets.size()==n);U count=init(7);vector<U>keys;keys.reserve(77253253);constexpr U mask=(1ULL<<30)-1;vector<U>bitmap(1<<24);auto g=[&](int w,S s){hist[w]++;U k=key(s);keys.push_back(k);U b=mix(k)&mask;bitmap[b>>6]|=1ULL<<(b&63);};hgen(0,0,{},g);verify(count);sort(keys.begin(),keys.end());keys.erase(unique(keys.begin(),keys.end()),keys.end());cout<<"unique horizontal keys "<<keys.size()<<endl;
vector<size_t> idx((1<<20)+1);size_t off=0;for(size_t i=0;i<idx.size();i++){while(off<keys.size()&&(keys[off]>>37)<i)off++;idx[i]=off;}U queries=0,bhits=0,khits=0;mutex mu;vector<thread> workers;for(int z=0;z<4;z++)workers.emplace_back([&,z]{U q=0,bh=0,kh=0;for(size_t i=z;i<pos.size();i+=4){auto&p=pos[i];for(auto&t:targets){q++;auto k=key(sub(t,p.s));U b=mix(k)&mask;if(!(bitmap[b>>6]>>(b&63)&1))continue;bh++;auto h=k>>37;if(binary_search(keys.begin()+idx[h],keys.begin()+idx[h+1],k)){kh++;lock_guard<mutex> l(mu);cout<<"high-three hit "<<k<<" Pmass "<<p.w<<endl;}}}lock_guard<mutex> l(mu);queries+=q;bhits+=bh;khits+=kh;cout<<"group "<<z<<" queries "<<q<<" bitmap hits "<<bh<<" exact hits "<<kh<<endl;});for(auto& t:workers)t.join();assert(queries==pos.size()*targets.size());cout<<"queries "<<queries<<" bitmap hits "<<bhits<<" exact horizontal high hits "<<khits<<endl;return khits?2:0;}
```
