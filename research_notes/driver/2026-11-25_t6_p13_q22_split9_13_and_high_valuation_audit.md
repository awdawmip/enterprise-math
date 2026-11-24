# T6: q22 split(9,13) inverse signature join and high-valuation cancellation audit
2026-11-25. Driver lane historical EM-DVR-DEBB5E. New author-side finite q22 computation and exact upstream lemma audit, not independent decisive acceptance of own result. Frozen scientific Source d84bd940cfb093cdc60e569f15cad58772a51dca; original task research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md. Preserve EM-DIRECT-D03BC9 and previous contributors. Prior q23..26 result 8f46d8d21bc4c1aa7582dd9172ed0082b5c767d2, q10 independent six-split synthesis d4b2a7149f7c33ff4e9b0c0d2a762dc59de9b6e8; neither replayed.

## 1. Upstream high-valuation cancellation
For each side, exponent e_i=d_i-1>=1 and mass <=2331. Equality of H_0..H_6 implies reciprocal moment equalities by the binomial invertible triangular transform, since e_i/(e_i+1)=1-1/d_i. Fix p=11 or 13 and highest remaining valuation v>=2. Since d_i<=2332, v<=3. For every d=p^v u with p not dividing u, retain all integer u in [1,floor(2332/p^v)] with p not dividing u (even nonsmooth u allowed). Multiply kth reciprocal identity by p^(vk) and reduce modulo p^k in the localization at p. Every lower-valuation term vanishes. Consequently the maximal-valuation profiles have identical three-component signature (sum u^-k mod p^k) for k=1,2,3. Costs are p^v u-1. Enumerate nondecreasing multisets with each side cost <=2331. Exact integer computation returned:
| p | v | units | profiles | distinct first 1 | distinct first 2 | distinct first 3 |
|---|---:|---:|---:|---:|---:|---:|
|11|3|1|2|2|2|2|
|11|2|18|2020|11|1038|2020|
|13|3|1|2|2|2|2|
|13|2|12|372|13|315|372|
This is injectivity on the larger unsmoothed domain, using only the first three mixed congruences. Identical signatures force identical multisets, so equal denominators at the maximal valuation can be removed, preserving all seven exact H equalities and not increasing masses. Descend v=3 then 2. This supplies a standalone exact proof of the high-valuation cancellation premise for p13 as used by the earlier q10 and q23..26 reductions, and for p11 for future use. It does not close valuation-one or lower-prime/H0 completion. No protected p17 q14 work performed.

Executed Python enumeration (the same recurrence used for the above counts; extra assertion makes the criterion explicit):
```python
for p in (11,13):
    for v in (2,3):
        units=[u for u in range(1,2332//p**v+1) if u%p]
        def gen(i,c,t):
            yield t
            for j in range(i,len(units)):
                u=units[j]; w=p**v*u-1
                if w<=c: yield from gen(j,c-w,t+(u,))
        profiles=list(gen(0,2331,()))
        signatures=[tuple(sum(pow(u,-k,p**k) for u in x)%p**k
                          for k in range(1,4)) for x in profiles]
        sizes=[len({s[:k] for s in signatures}) for k in range(1,4)]
        print(p,v,len(units),len(profiles),sizes)
        assert sizes[-1]==len(profiles)
```

## 2. q22 split(9,13) inverse signature join
At p13 valuation one, d=13(13q+r), 1<=r<=12, 13-smooth u=13q+r, q>=0; cost=169q+13r-1. Define F(U)=(sum u^-k mod 13^k) for k=1..6. Equality requires F(A)=F(B). For Q=sum q=9, separate uniquely the positive-q multiset P and horizontal H with sum q=0. For Q=13 build the full exact target roster T. Budgets for residual cost are 810 and 134 respectively. Instead of scanning all Q9 configurations, query the horizontal signature index with F(T)-F(P) componentwise mod 13^k. All positive, horizontal and target profiles are nondecreasing full labeled multisets; suffix minimum cost pruning only removes impossible completions.

Independent unbounded integer coin DP by q and residual cost gives Q9 P=186647, H(cap810)=4298444, and complete Q9=8963595909. Q13 P=1368, H(cap134)=143, complete=5775. Exact C++ join returned complete Q9 count 8963595909; 1077886425 P/T queries; 17132355 bitmap hits; exact equality of high three components (k=4,5,6): zero; full six matches: zero. Time 27.46 s wall, peak RSS 231392 KiB, g++ -O3 -std=c++17, normal exit. The high-three packing is injective (15+19+23 bits; each modulus below its lane radix); bitmap hash is only a necessary prefilter, every bitmap hit is verified by exact sorted-key lookup, and all equal high keys would be checked on the other three components and mass. There were no high-key matches even before those remaining checks. Thus split(9,13) excluded up to sign, without any common-support pruning or probability assumption. The q22 other splits (10,12) and (11,11) remain open. q10 and q23..26 retain their proven local scopes.

### Executed C++17 reproduction
```cpp
#include <bits/stdc++.h>
using namespace std;using U=uint64_t;
constexpr int M[6]={13,169,2197,28561,371293,4826809};
struct A{int q,w;array<int,6>s;};vector<A>a;int np;vector<array<int,14>>mn;
struct P{array<int,6>s;int w;};vector<P>pos,hor,target;
int inv(int a,int m){int64_t x=0,y=1,b=m;while(a){int t=b/a,z=b-t*a;b=a;a=z;int64_t u=x-t*y;x=y;y=u;}assert(b==1);return (x%m+m)%m;}
bool smooth(int x){for(int p:{2,3,5,7,11,13})while(x%p==0)x/=p;return x==1;}
array<int,6> add(const array<int,6>&x,const array<int,6>&y){array<int,6>z;for(int k=0;k<6;k++){z[k]=x[k]+y[k];if(z[k]>=M[k])z[k]-=M[k];}return z;}
void hgen(int i,int c,int w,const array<int,6>&s){hor.push_back({s,w});for(int j=i;j<(int)a.size();j++)if(a[j].w<=c)hgen(j,c-a[j].w,w+a[j].w,add(s,a[j].s));}
void pgen(int i,int q,int c,int w,const array<int,6>&s){if(!q){pos.push_back({s,w});return;}for(int j=i;j<np;j++)if(a[j].q<=q&&a[j].w<=c&&mn[j][q-a[j].q]<=c-a[j].w)pgen(j,q-a[j].q,c-a[j].w,w+a[j].w,add(s,a[j].s));}
void init(){for(int q=13;q>=0;q--)for(int r=1;r<13;r++)if(smooth(13*q+r)){A t{q,13*r-1,{}};for(int k=0;k<6;k++){int v=inv(13*q+r,M[k]);int64_t x=1;for(int j=0;j<=k;j++)x=x*v%M[k];t.s[k]=x;}a.push_back(t);if(q)np++;}assert(a.size()==78);mn.resize(np+1);mn[np].fill(100000);mn[np][0]=0;for(int i=np-1;i>=0;i--){mn[i][0]=0;for(int q=1;q<=13;q++){mn[i][q]=mn[i+1][q];if(q>=a[i].q)mn[i][q]=min(mn[i][q],a[i].w+mn[i][q-a[i].q]);}}}
U hi(int x,int y,int z){return U(x)|(U(y)<<15)|(U(z)<<34);}
U hi(const array<int,6>&s){return hi(s[3],s[4],s[5]);}
uint32_t lo(const array<int,6>&s){return s[0]+13*(s[1]+169*s[2]);}
int sub(int x,int y,int m){int d=x-y;return d<0?d+m:d;}
U mix(U x){x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;x^=x>>27;x*=0x94d049bb133111ebULL;return x^(x>>31);}
struct E{U h;uint32_t l,w;};
int main(){init();hgen(np,134,0,{});pgen(0,13,134,0,{});for(auto&p:pos)for(auto&h:hor)if(p.w+h.w<=134)target.push_back({add(p.s,h.s),p.w+h.w});assert(target.size()==5775);pos.clear();hor.clear();hgen(np,810,0,{});pgen(0,9,810,0,{});assert(hor.size()==4298444&&pos.size()==186647);vector<E>tab;tab.reserve(hor.size());vector<U>filter(1<<22);constexpr U mask=(1ULL<<28)-1;vector<U>hist(811);for(auto&h:hor){U x=hi(h.s);tab.push_back({x,lo(h.s),uint32_t(h.w)});U b=mix(x)&mask;filter[b>>6]|=1ULL<<(b&63);hist[h.w]++;}partial_sum(hist.begin(),hist.end(),hist.begin());sort(tab.begin(),tab.end(),[](auto&x,auto&y){return x.h<y.h;});hor.clear();hor.shrink_to_fit();U total=0,pairs=0,filterhits=0,highhits=0,full=0,done=0;for(auto&p:pos){total+=hist[810-p.w];for(auto&t:target){U x=hi(sub(t.s[3],p.s[3],M[3]),sub(t.s[4],p.s[4],M[4]),sub(t.s[5],p.s[5],M[5]));U b=mix(x)&mask;pairs++;if(!(filter[b>>6]>>(b&63)&1))continue;filterhits++;auto it=lower_bound(tab.begin(),tab.end(),x,[](const E&e,U v){return e.h<v;});if(it==tab.end()||it->h!=x)continue;array<int,6>z{};for(int k=0;k<3;k++)z[k]=sub(t.s[k],p.s[k],M[k]);uint32_t l=lo(z);for(;it!=tab.end()&&it->h==x;it++){highhits++;if(it->l==l&&it->w+p.w<=810){full++;cerr<<"MATCH "<<done<<"\n";}}}if(++done%25000==0)cerr<<done<<" "<<pairs<<" "<<filterhits<<" "<<highhits<<" "<<full<<endl;}cout<<"complete profiles "<<total<<" pairs "<<pairs<<" filterhits "<<filterhits<<" highhits "<<highhits<<" full "<<full<<endl;assert(total==8963595909ULL);}
```

## 3. Coordination
Authenticated Driver checkpoint r554 was read. Own custody profile d25-sites-permanent-driver-start-20261110-v1 status valid, not revoked/expired, underlying session open, public session matches historical DA-2C461358FCCA215C8753 Source record. This is recovery metadata, not fresh execution authorization. Original dvr-20261124-2000-own-recovery-metadata-v1 returned CONTROL_REQUEST_NOT_FOUND; no replay. New current read dvr-20261125-0200-t6-current-read-v1 queued; consume only original receipt. Onhour r140 author synthesis 5dfc3f657b1eee674f1a7ca46b739608b47719fa: 127 q10 families, 319619196 raw, 153219924 common cancellation, 3569827 over cap, 162829445 searches, 223 witnesses, zero valid. Consumed as author evidence distinct from Driver independent smooth-domain searches. Onhour q11 length1..3 certificate 7f1297166b6d384cf169a1990e33c06703595f13 and r140 preserve ongoing q11 work. Backlog r473 retains DCMP11 selection and dependencies, no confirmed available worker. No claim, protected native review, Result acceptance, formal Task or mother completion. Preserve author-side contribution of this note and distinct p17 q14 protected scope.
