"""Exact escape enumeration and saturation residual feasibility replay.
Run python3 EC49FYQ_ESCAPE_PREFIX_VERIFY.py; requires g++ C++17.
"""
import pathlib, subprocess, tempfile
from functools import lru_cache
from collections import Counter
F=[23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005]
src=r'''
#include <algorithm>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;
const int F[]={23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005};
int tau[50][1024];
using S=vector<int>;
struct Hash{size_t operator()(S const&a)const{size_t h=0;for(int x:a)h=h*1031+x;return h;}};
int bound(S const&a,int h,int c,int d){bool exists=false;for(int i=0;i<50;i++){int u=F[i],must=0;S b;for(int x:a){if(x&u)must++;else b.push_back(x);}if(must>=h)continue;exists=true;int extra=d-must;if(extra>c)return 1;int keep=max(0,(int)b.size()-(h-1-must));int n=b.size();for(int mask=0;mask<(1<<n);mask++){if(__builtin_popcount((unsigned)mask)!=keep)continue;int z=0;for(int j=0;j<n;j++)if(mask>>j&1)z|=b[j];if(extra+tau[i][z]>c)return 1;}}return exists?0:-1;}
int main(){for(int i=0;i<50;i++){vector<int> ds;for(int v:F)if(v!=F[i]&&(v&F[i])==F[i])ds.push_back(v^F[i]);for(int z=1023;z>=0;z--){bool ok=true;for(int d:ds)if(!(d&z)){ok=false;break;}if(ok)tau[i][z]=0;else{int b=99;for(int t=0;t<10;t++)if(!(z>>t&1))b=min(b,1+tau[i][z|1<<t]);tau[i][z]=b;}}}
int h=3,c=5;unordered_set<S,Hash> layer;layer.insert(S{});for(int d=1;d<=c+h;d++){unordered_set<S,Hash> seen,next;int escape=0;for(auto const&a:layer)for(int j=0;j<=(int)a.size();j++){if(j>0&&j<(int)a.size()&&a[j]==a[j-1])continue;for(int t=0;t<10;t++){int bit=1<<t;S q=a;if(j==(int)a.size())q.push_back(bit);else{if(a[j]&bit)continue;q[j]|=bit;}sort(q.begin(),q.end());if(!seen.insert(q).second)continue;int v=bound(q,h,c,d);if(v<0){escape++;cout<<d;for(int x:q)cout<<","<<x;cout<<"\n";}else if(v==0)next.insert(q);}}cerr<<d<<","<<seen.size()<<","<<next.size()<<","<<escape<<"\n";layer.swap(next);if(layer.empty())break;}}
'''
with tempfile.TemporaryDirectory() as tmp:
    p=pathlib.Path(tmp)/'escape.cpp'
    exe=pathlib.Path(tmp)/'escape'
    p.write_text(src)
    subprocess.run(['g++','-O3','-std=c++17',str(p),'-o',str(exe)],check=True)
    a=subprocess.run([str(exe)],capture_output=True,text=True,check=True)
print(a.stderr)
esc=[tuple(map(int,l.split(',')))[1:] for l in a.stdout.splitlines()]
assert len(esc)==935
def depth_masks(q, fresh):
    cand=[u for u in F if sum(bool(u&x) for x in q)==3]
    masks=[]
    for j in range(len(q)+fresh):
        for t in range(10):
            p=sum(1<<i for i,u in enumerate(cand) if (j==len(q) or not(q[j]&u)) and u>>t&1)
            if p and p!=(1<<len(cand))-1:masks.append(p)
    masks=list(set(masks))
    @lru_cache(None)
    def solve(s,d):
        n=s.bit_count()
        if n<=1:return True
        if n>1<<d or d==0:return False
        cap=1<<(d-1)
        options=set()
        for p in masks:
            x=s&p;y=s^x
            if x and y and max(x.bit_count(),y.bit_count())<=cap:
                options.add((x,y) if x<y else (y,x))
        for x,y in sorted(options,key=lambda p:max(p[0].bit_count(),p[1].bit_count())):
            if solve(x,d-1) and solve(y,d-1):return True
        return False
    if not cand:return 0,0
    d=(len(cand)-1).bit_length()
    while not solve((1<<len(cand))-1,d):d+=1
    return len(cand),d
hist=Counter()
for q in esc:
    k=len(q)
    n,d=depth_masks(q,1)
    n0,d0=depth_masks(q,0) if k>3 else (n,None)
    hist[(k,n,d0,d)]+=1
by=Counter()
for (k,n,d0,d1),v in hist.items():
    for m in range(4,10):
        if k<=m:
            by[(m,'compatible_prefixes')]+=v
            if (d0 if k==m else d1)<=m-3:
                by[(m,'completable')]+=v
print([(m,by[m,'compatible_prefixes'],by[m,'completable']) for m in range(4,10)])
print('depth hist',Counter({d:sum(v for (k,n,d0,d1),v in hist.items() if d1==d) for d in range(6)}))
print('max candidate count',max(x[1] for x in hist))
