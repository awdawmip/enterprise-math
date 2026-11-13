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


@lru_cache(None)
def mass3(s,t,ew,T,u,m,z):
    """Count hidden words H whose exact last min(3,u) symbols are z."""
    k=(m-2)//2
    r=min(3,u)
    if len(z)!=r:raise ValueError('wrong suffix length')
    common=add(baseline(m),E('A',s),ew,E(t,'A'))
    L=u-r
    if L==0:
        return int(T==add(common,E('A',z[0]),edges(z),E(z[-1],'A')))
    remain=sub(T,add(common,edges(z),E(z[-1],'A')))
    if min(remain)<0:return 0
    ans=0
    for p in A:
        for q in A:
            delta=sub(remain,add(E('A',p),E(q,z[0])))
            if min(delta)>=0:ans+=N(L,p,q,delta)
    return ans

@lru_cache(None)
def suffixes3(s,t,ew,T,k,u):
    m=2*k+2
    return tuple(''.join(x) for x in product(A,repeat=min(3,u))
                 if mass3(s,t,ew,T,u,m,''.join(x))>0)

@lru_cache(None)
def summary3(k,u,T):
    m=2*k+2
    room=sub(T,baseline(m))
    if min(room)<0:return (0,0,0)
    classes=population=types=0
    for ew in compositions(room,k-1):
        for s in A:
            for t in A:
                nw=N(k,s,t,ew)
                if nw==0:continue
                for z in suffixes3(s,t,ew,T,k,u):
                    classes+=nw
                    population+=nw*mass3(s,t,ew,T,u,m,z)
                    types+=1
    return classes,population,types

@lru_cache(None)
def prefix3(pre,k,u,T):
    if not pre:return summary3(k,u,T)[0]
    if len(pre)==k:return len(suffixes3(pre[0],pre[-1],edges(pre),T,k,u))
    m=2*k+2
    ep=edges(pre)
    room=sub(T,add(baseline(m),ep))
    if min(room)<0:return 0
    ans=0
    for g in compositions(room,k-len(pre)):
        for t in A:
            nw=N(k-len(pre)+1,pre[-1],t,g)
            if nw:
                ans+=nw*len(suffixes3(pre[0],t,add(ep,g),T,k,u))
    return ans

def rank3(k,u,T,w,z):
    supports=suffixes3(w[0],w[-1],edges(w),T,k,u)
    if z not in supports:raise ValueError('unsupported')
    result=0;pre=''
    for x in w:
        for y in A:
            if x==y:break
            result+=prefix3(pre+y,k,u,T)
        pre+=x
    return result+supports.index(z)

def unrank3(k,u,T,r):
    if not 0<=r<summary3(k,u,T)[0]:raise ValueError('rank outside support')
    pre=''
    for _ in range(k):
        for x in A:
            n=prefix3(pre+x,k,u,T)
            if r>=n:r-=n
            else:pre+=x;break
        else:raise AssertionError('missing child')
    return pre,suffixes3(pre[0],pre[-1],edges(pre),T,k,u)[r]

def check():
    # All 3^(k+u) original histories for k=1..3,u=1..4,
    # grouped by the full initial directed-adjacency fibre.
    small=[]
    for k in (1,2,3):
        for u in (1,2,3,4):
            m=2*k+2;fs=defaultdict(list)
            for wp in product(A,repeat=k):
                w=''.join(wp)
                for hp in product(A,repeat=u):
                    h=''.join(hp)
                    T=theta(m,w,h)
                    fs[T].append((w,h))
            ranks=0;checks=0
            for T,items in fs.items():
                grouped=Counter((w,h[-min(3,u):]) for w,h in items)
                assert summary3(k,u,T)[:2]==(len(grouped),len(items))
                for (w,z),count in grouped.items():
                    assert mass3(w[0],w[-1],edges(w),T,u,m,z)==count
                    checks+=1
                if k<=2 or len(grouped)<=18:
                    for i,key in enumerate(sorted(grouped)):
                        assert rank3(k,u,T,*key)==i
                        assert unrank3(k,u,T,i)==key
                        ranks+=1
            small.append(dict(k=k,u=u,fibers=len(fs),histories=3**(k+u),class_checks=checks,rank_checks=ranks))
    T=(28,5,1,3,1,4,3,2,1)
    medium=summary3(12,9,T)
    assert medium==(366818,1763560,5078),medium
    return dict(status='ALL_ASSERTIONS_PASSED',small=small,
                totals={key:sum(a[key] for a in small) for key in ('fibers','histories','class_checks','rank_checks')},
                medium=dict(k=12,u=9,theta=T,classes_qpop3=medium[0],population=medium[1],
                            supported_types=medium[2],classes_qpop2=207318))

if __name__=='__main__':
    print(json.dumps(check(),indent=2))
