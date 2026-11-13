#!/usr/bin/env python3
"""Stage486-B independent, exact source-population and boundary test."""
from itertools import product
from collections import Counter, defaultdict
from functools import lru_cache
import json

D='ABCDEFGHIJKL' # signed X6 directions, +E1..+E6,-E1..-E6
BASE='ABG'
V={'A':(1,0),'B':(0,1),'G':(-1,0)}
def edges(w):return Counter(zip(w,w[1:]))
def esig(w):return tuple(edges(w).get(x,0) for x in product(BASE,repeat=2))
def disp(w):return tuple(sum(V[x][j] for x in w) for j in range(2))
def observer(p,q):return (disp(p),disp(q),esig(p),esig(q),sum(a==b for a,b in zip(p,q)))
def minus(e,f):
    e=e.copy()
    for x,n in f.items():
        e[x]-=n
        if e[x]<0:return None
        if not e[x]:del e[x]
    return e
def norm(e):return tuple(sorted((a,b,v) for (a,b),v in e.items() if v))
@lru_cache(None)
def N(n,s,t,counts):
    if sum(v for _,_,v in counts)!=n-1:return 0
    if n==1:return int(s==t and not counts)
    e={(a,b):v for a,b,v in counts}
    return sum(N(n-1,b,t,norm(minus(e,Counter({(s,b):1}))))
               for (a,b),v in e.items() if a==s and v>0)
def count(n,s,t,e):return N(n,s,t,norm(e)) if e is not None else 0
def key(t,w,H,k,u,h):
    L=max(k+1,h-k-u-1);r=min(h,u)
    return (t[-L:],w,H[-r:] if r else '')
def population(K,eP,eQ,s,k,u,h):
    sig,w,S=K;L=len(sig);r=len(S);m=2*k+2
    p=count(m-L+1,s,sig[0],minus(eP,edges(sig)))
    fixed=eP+Counter({(sig[-1],w[0]):1})+edges(w)+Counter({(w[-1],'A'):1})
    R=minus(eQ,fixed)
    if R is None:return 0
    if not r:return p*count(u+2,'A','A',R)
    return p*count(u-r+2,'A',S[0],minus(R,edges(S+'A')))
def run(k,u):
    m=2*k+2;n=m+k+u+2
    fibers=defaultdict(list)
    for chars in product(BASE,repeat=m+k+u):
        t=''.join(chars[:m]);w=''.join(chars[m:m+k]);H=''.join(chars[m+k:]);q=t+w+'A'+H+'A'
        fibers[observer(t,q)].append((t,w,H))
    result={}
    for h in range(n):
        total=0
        for entries in fibers.values():
            classes=Counter(key(t,w,H,k,u,h) for t,w,H in entries)
            t,w,H=entries[0];eP=edges(t);eQ=edges(t+w+'A'+H+'A')
            for K,num in classes.items():assert population(K,eP,eQ,t[0],k,u,h)==num
            assert sum(classes.values())==len(entries)
            total+=len(classes)
        result[str(h)]=total
    return {'raw':sum(len(v) for v in fibers.values()),'fibers':len(fibers),'classes':result}
if __name__=='__main__':
    a=run(1,2);b=run(2,2)
    t1='AABAAA';t2='ABAAAA';w='AB';H='AB'
    q1=t1+w+'A'+H+'A';q2=t2+w+'A'+H+'A'
    assert observer(t1,q1)==observer(t2,q2)
    assert key(t1,w,H,2,2,8)==key(t2,w,H,2,2,8)
    assert key(t1,w,H,2,2,9)!=key(t2,w,H,2,2,9)
    assert esig(q1[:-8])==esig(q2[:-8]) and esig(q1[:-9])!=esig(q2[:-9])
    output={'k1u2':a,'k2u2':b,'strict_witness':{'T1':t1,'T2':t2,'W':w,'H':H,'Q_POP_divergence':9},
            'exact_integer_population':'PASS','status':'PASS'}
    print(json.dumps(output,sort_keys=True))
