#!/usr/bin/env python3
"""Stage489-B independent exact verifier of the edit-lift finite witnesses."""
from collections import Counter, defaultdict
from itertools import product
from functools import lru_cache
import json

D='ABCDEFGHIJKL'  # +E1..+E6, -E1..-E6
v={a:tuple((1 if i==j else 0)*sgn for i in range(6))
   for j in range(6) for a,sgn in ((D[j],1),(D[j+6],-1))}

def obs(p,q):
    def movement(w):return tuple(sum(v[c][i] for c in w) for i in range(6))
    def edges(w):
        C=Counter(zip(w,w[1:])); return tuple(C[(x,y)] for x in D for y in D)
    return len(p),len(q),movement(p),movement(q),edges(p),edges(q),sum(x==y for x,y in zip(p,q))

def edit(w,j,z):return w[:j-1]+z+w[j:]

def explore(p,a,b,j,limits):
    todo=[(p,a,b,0,0,0,0,0)]; seen=set(todo); count=0
    while todo:
        p,a,b,up,ua,vp,va,us=todo.pop();count+=1
        assert obs(p,a)==obs(p,b),('unequal observation',p,a,b,up,ua,vp,va,us)
        cand=[]
        if up<limits[0] and len(p)>1:cand.append((p[:-1],a,b,up+1,ua,vp,va,us))
        if ua<limits[1]:
            cand.extend((p+z,a,b,up,ua+1,vp,va,us) for z in D)
        if vp<limits[2] and len(a)>1 and len(b)>1:
            cand.append((p,a[:-1],b[:-1],up,ua,vp+1,va,us))
        if va<limits[3]:
            cand.extend((p,a+z,b+z,up,ua,vp,va+1,us) for z in D)
        if us<limits[4] and j<=len(a) and j<=len(b):
            cand.extend((p,edit(a,j,z),edit(b,j,z),up,ua,vp,va,us+1) for z in D)
        for s in cand:
            if s not in seen:seen.add(s);todo.append(s)
    return count

def euler_rec(d):
    word=''.join(D[i] for i in range(d));
    @lru_cache(None)
    def f(at,e):
        if not any(e):return int(at==0)
        return sum(f(z,e[:at*d+z]+(e[at*d+z]-1,)+e[at*d+z+1:])
                   for z in range(d) if e[at*d+z])
    population=f(0,(1,)*(d*d))
    return population,f.cache_info().currsize

def main():
    T='ABGABA';W='GH';j=10;u=6
    fibers=defaultdict(list)
    for h in product('ABGH',repeat=u):
        H=''.join(h);q=T+W+'A'+H+'A';fibers[obs(T,q)].append((H,q))
    h1,h2='AAAABA','AAABAA'
    q1=T+W+'A'+h1+'A';q2=T+W+'A'+h2+'A'
    assert obs(T,q1)==obs(T,q2)
    assert q1[j-2:j+1]==q2[j-2:j+1]=='AAA' and h1[-1]==h2[-1]
    states=explore(T,q1,q2,j,(1,1,1,1,1))
    s1=T+W+'A'+'AB'+'A';s2=T+W+'A'+'BA'+'A'
    assert obs(T,s1)==obs(T,s2)
    assert obs(T,edit(s1,j,'A'))!=obs(T,edit(s2,j,'A'))
    sigs={}
    for tri in product('ABGH',repeat=3):
        w=''.join(tri);o=obs('B',w)
        sig=tuple((tuple(x-y for x,y in zip(obs('B',edit(w,2,z))[2],o[2])),
                   tuple(x-y for x,y in zip(obs('B',edit(w,2,z))[5],o[5]))) for z in D)
        assert sig not in sigs or sigs[sig]==w
        sigs[sig]=w
    assert len(sigs)==64
    e2=euler_rec(2);e3=euler_rec(3)
    assert e2==(2,10) and e3==(72,146)
    print(json.dumps({'H_words':4**u,'fibers':len(fibers),'states':states,
      'strict_edit':'Q_SET(10,A)','triple_signatures':len(sigs),
      'Euler_d2':e2,'Euler_d3':e3},sort_keys=True))

if __name__=='__main__':main()
