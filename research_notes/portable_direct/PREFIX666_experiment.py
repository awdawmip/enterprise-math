from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
import time
N,DEN=189,2**18
Q=F(19,128)
@lru_cache(None)
def inside(n,k,a):return 40*(n+1)*comb(n,k)*a**k*(DEN-a)**(n-k)>DEN**n
@lru_cache(None)
def wide(n,k):
    if k>n//2:return wide(n,n-k)
    mid=k*DEN//n
    assert inside(n,k,mid)
    if k==0:ll=lh=0
    else:
        lo,hi=0,mid
        while hi-lo>1:
            md=(lo+hi)//2
            if inside(n,k,md):hi=md
            else:lo=md
        ll,lh=lo,hi
    lo,hi=mid,DEN
    while hi-lo>1:
        md=(lo+hi)//2
        if inside(n,k,md):lo=md
        else:hi=md
    rl,rh=lo,hi
    if 4*(rl-lh)>DEN:return True
    if 4*(rh-ll)<DEN:return False
    raise ValueError((n,k))

def build():
    st={0:1}; rows=[st.copy()]
    for n in range(1,N+1):
        nx=defaultdict(int)
        for k,v in st.items(): nx[k]+=v;nx[k+1]+=v
        st={k:v for k,v in nx.items() if wide(n,k)}
        rows.append(st.copy())
    assert not rows[-1]
    return rows

def eval_az(rows,z):
    t=[]
    for m in range(N):
        t.append(sum((F(v)*z**k*(1-z)**(m-k) for k,v in rows[m].items()),F()))
    a=[];b=[]
    for n in range(N):
        aa,bb=F(1),F(n+1)
        for m in range(N):
            if not t[m]:continue
            w=F(comb(n+m,n),2**(n+m+1))*t[m]
            aa-=w;bb-=F(n+m+1,2)*w
        a.append(aa);b.append(bb)
    return a,b,t

def moments_at(rows,a,b,t,p):
    s=[];sp=[];spp=[]
    for n in range(N):
        fn=[F(rows[n].get(k,0),comb(n,k)) for k in range(n+1)]
        s.append(sum((F(rows[n].get(k,0))*p**k*(1-p)**(n-k) for k in rows[n]),F()))
        sp.append(n*sum((comb(n-1,k)*(fn[k+1]-fn[k])*p**k*(1-p)**(n-1-k) for k in range(n)),F()) if n>=1 else F())
        spp.append(n*(n-1)*sum((comb(n-2,k)*(fn[k+2]-2*fn[k+1]+fn[k])*p**k*(1-p)**(n-2-k) for k in range(n-1)),F()) if n>=2 else F())
    mu=sum((a[n]*s[n] for n in range(N)),sum(t,F()))
    h=sum((b[n]*s[n] for n in range(N)),sum(((m+1)*t[m] for m in range(N)),F()))
    mup=sum((a[n]*sp[n] for n in range(N)),F())
    mupp=sum((a[n]*spp[n] for n in range(N)),F())
    hpp=sum((b[n]*spp[n] for n in range(N)),F())
    wpp=2*hpp-2*mup*mup-2*mu*mupp
    return mu,mup,mupp,hpp,wpp
if __name__=='__main__':
    a0=time.monotonic();rows=build();print('build',time.monotonic()-a0,'state',sum(len(x) for x in rows));
    a,b,t=eval_az(rows,Q);print('ab',time.monotonic()-a0)
    for p in (F(0),F(1,4096),F(1,2048),F(1,1024)):
        now=time.monotonic(); vals=moments_at(rows,a,b,t,p);print(str(p),*[round(float(x),6) for x in vals],"seconds",round(time.monotonic()-now,2))
