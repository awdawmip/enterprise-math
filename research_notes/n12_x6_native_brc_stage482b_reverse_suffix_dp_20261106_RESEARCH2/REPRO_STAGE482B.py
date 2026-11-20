"""Stage480-B | Exact 2-Q-POP suffix BRC on a typed native X6 3-direction observer.
Scientific source pin: Stage477-B (Global bf84bd7c61a2444b59b1da96be57df0e9ae47e53;
EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419). Independent exact integer implementation.
"""
from itertools import product
from functools import lru_cache
from collections import defaultdict, Counter
from math import factorial
import json
A = 'ABC'
PAIRS = tuple(x+y for x in A for y in A)
IX={z:i for i,z in enumerate(PAIRS)}
ZERO=(0,)*9

def E(x,y):
    z=[0]*9;z[IX[x+y]]=1;return tuple(z)
def add(*x):return tuple(map(sum,zip(*x)))
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def edges(s):
    c=[0]*9
    for x,y in zip(s,s[1:]):c[IX[x+y]]+=1
    return tuple(c)
def baseline(m):return (m-1,)+(0,)*8
def theta(m,w,h):
    return add(baseline(m),E('A',w[0]),edges(w),E(w[-1],'A'),E('A',h[0]),edges(h),E(h[-1],'A'))
def det2(z):
    if len(z)==0:return 1
    if len(z)==1:return z[0][0]
    if len(z)==2:return z[0][0]*z[1][1]-z[0][1]*z[1][0]
    raise AssertionError('3x3 minor maximum')
@lru_cache(None)
def N(l,s,t,e):
    """Directed Euler word count; counts original words, not labelled edges."""
    if l<1 or len(e)!=9 or min(e)<0 or sum(e)!=l-1:return 0
    if l==1:return int(s==t and e==ZERO)
    o=[sum(e[i*3:i*3+3]) for i in range(3)]
    inn=[sum(e[3*j+i] for j in range(3)) for i in range(3)]
    si=A.index(s);ti=A.index(t)
    if any(o[i]-inn[i]!=(i==si)-(i==ti) for i in range(3)):return 0
    active=[i for i in range(3) if o[i]+inn[i] or i==si or i==ti]
    rest=[i for i in active if i!=ti]
    if any(o[i]==0 for i in rest):return 0
    L=[[o[i]-e[3*i+i] if i==j else -e[3*i+j] for j in rest] for i in rest]
    tau=det2(L)
    if tau<=0:return 0
    v=tau*factorial(o[ti]);den=1
    for i in rest:v*=factorial(o[i]-1)
    for x in e:den*=factorial(x)
    assert v%den==0
    return v//den
@lru_cache(None)
def N_recur(s,t,e):
    if min(e)<0:return 0
    if sum(e)==0:return int(s==t)
    v=0
    for x in A:
        pos=IX[s+x]
        if e[pos]:
            z=list(e);z[pos]-=1
            v+=N_recur(x,t,tuple(z))
    return v

def compositions(bnd,tot,p=()):
    if len(p)==8:
        if 0<=tot<=bnd[8]:yield p+(tot,)
        return
    for x in range(min(tot,bnd[len(p)])+1):
        yield from compositions(bnd,tot-x,p+(x,))



# Stage482-B reverse residual Euler-BRC suffix automaton.
# For this 3-letter native X6 observer; future APPEND remains 12 signed directions.
from collections import defaultdict
from itertools import product

def B(k,w):
    m=2*k+2
    return add(baseline(m),E('A',w[0]),edges(w),E(w[-1],'A'))

@lru_cache(None)
def support(R,u,r):
    assert 0<=r<=u and min(R)>=0 and sum(R)==u+1
    dp={('A',R):1}; transitions=0
    for _ in range(r):
        next_dp=defaultdict(int)
        for (last,e),paths in dp.items():
            for x in A:
                j=IX[x+last]
                if e[j]:
                    rem=list(e);rem[j]-=1
                    next_dp[(x,tuple(rem))]+=paths
                    transitions+=1
        dp=dict(next_dp)
    q=mass=0
    for (last,e),paths in dp.items():
        count=N(u-r+2,'A',last,e)
        if count:
            q+=paths
            mass+=paths*count
    assert mass==N(u+2,'A','A',R)
    return q,mass,len(dp),transitions

@lru_cache(None)
def z_prefix_count(R,u,r,prefix):
    assert len(prefix)<=r
    dp={('A',R):1}
    for _ in range(r-len(prefix)):
        nxt=defaultdict(int)
        for (last,e),paths in dp.items():
            for x in A:
                j=IX[x+last]
                if e[j]:
                    rem=list(e);rem[j]-=1
                    nxt[(x,tuple(rem))]+=paths
        dp=dict(nxt)
    ans=0
    for (last,e),paths in dp.items():
        rem=list(e);c=last
        for x in reversed(prefix):
            j=IX[x+c]
            if not rem[j]:break
            rem[j]-=1;c=x
        else:
            if N(u-r+2,'A',c,tuple(rem))>0:ans+=paths
    return ans

def z_rank(R,u,r,z):
    if len(z)!=r or z_prefix_count(R,u,r,z)!=1:
        raise ValueError('unsupported suffix')
    out=0;pre=''
    for x in z:
        for y in A:
            if y==x:break
            out+=z_prefix_count(R,u,r,pre+y)
        pre+=x
    return out

def z_unrank(R,u,r,index):
    if not 0<=index<support(R,u,r)[0]:raise ValueError('outside support')
    pre=''
    for _ in range(r):
        for x in A:
            n=z_prefix_count(R,u,r,pre+x)
            if index>=n:index-=n
            else:pre+=x;break
        else:raise AssertionError('missing suffix branch')
    return pre

@lru_cache(None)
def types(k,u,r,T):
    m=2*k+2; room=sub(T,baseline(m))
    if min(room)<0:return ()
    out=[]
    for ew in compositions(room,k-1):
        for s in A:
            for t in A:
                nw=N(k,s,t,ew)
                if not nw:continue
                residual=sub(T,add(baseline(m),E('A',s),ew,E(t,'A')))
                if min(residual)<0:continue
                q,mass,states,steps=support(residual,u,r)
                if q:out.append((s,t,ew,residual,nw,q,mass,states,steps))
    return tuple(out)

def fiber(k,u,r,T):
    typ=types(k,u,r,T)
    return dict(classes=sum(v[4]*v[5] for v in typ),
                population=sum(v[4]*v[6] for v in typ),
                surviving_types=len(typ),
                terminal_states=sum(v[7] for v in typ),
                transitions=sum(v[8] for v in typ))

@lru_cache(None)
def w_prefix_count(k,u,r,T,pre):
    ans=0;used=edges(pre)
    for s,t,ew,R,nw,q,mass,states,steps in types(k,u,r,T):
        if pre:
            if pre[0]!=s:continue
            rem=sub(ew,used)
            if min(rem)<0:continue
            n=N(k-len(pre)+1,pre[-1],t,rem)
        else:n=nw
        ans+=n*q
    return ans

def key_rank(k,u,r,T,w,z):
    if len(w)!=k:raise ValueError('W length')
    pre='';out=0
    for x in w:
        for y in A:
            if x==y:break
            out+=w_prefix_count(k,u,r,T,pre+y)
        pre+=x
    R=sub(T,B(k,w))
    if min(R)<0:raise ValueError('invalid W')
    return out+z_rank(R,u,r,z)

def key_unrank(k,u,r,T,index):
    if not 0<=index<w_prefix_count(k,u,r,T,''):raise ValueError('outside support')
    pre=''
    for _ in range(k):
        for x in A:
            n=w_prefix_count(k,u,r,T,pre+x)
            if index>=n:index-=n
            else:pre+=x;break
        else:raise AssertionError('missing W')
    return pre,z_unrank(sub(T,B(k,pre)),u,r,index)

def brute(k,u,r,T):
    hist=Counter()
    for w0 in product(A,repeat=k):
        w=''.join(w0)
        for h0 in product(A,repeat=u):
            h=''.join(h0)
            if theta(2*k+2,w,h)==T:
                hist[(w,h[-r:] if r else '')]+=1
    return hist

def verify():
    cases=0;keys=0
    for k,u in ((1,1),(1,2),(2,2),(2,3),(3,3)):
        ts={theta(2*k+2,''.join(w),''.join(h))
            for w in product(A,repeat=k) for h in product(A,repeat=u)}
        for T in ts:
            for r in range(u+1):
                g=brute(k,u,r,T); f=fiber(k,u,r,T)
                assert (f['classes'],f['population'])==(len(g),sum(g.values()))
                cases+=1;keys+=len(g)
    k,u=3,8
    T=theta(2*k+2,'ABC','ABACBCAA')
    focus=[]
    total_rank=0
    for r in range(4,9):
        f=fiber(k,u,r,T); g=brute(k,u,r,T)
        assert (f['classes'],f['population'])==(len(g),sum(g.values()))
        ordered=sorted(g)
        assert w_prefix_count(k,u,r,T,'')==len(ordered)
        for i,key in enumerate(ordered):
            assert key_rank(k,u,r,T,*key)==i
            assert key_unrank(k,u,r,T,i)==key
            total_rank+=1
        focus.append(dict(h=r,**f))
    return dict(status='ASSERTIONS_PASSED',small_fiber_r_cases=cases,
                small_keys_checked=keys,full_key_rank_checks=total_rank,
                theta=T,focus=focus)

if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
