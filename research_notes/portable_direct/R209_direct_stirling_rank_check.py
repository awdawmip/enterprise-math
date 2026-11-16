#!/usr/bin/env python3
"""R209: exact uniform-direction paired-event quotient count and table-free codec.
Standard library only. Tests specified finite domains, not native BRC integration.
"""
from itertools import permutations, product
from math import ceil
from functools import lru_cache
import json, sys

def falling(k,r):
    v=1
    for i in range(r):
        v*=k-i
    return v

@lru_cache(None)
def stirling(n,r):
    tab=[[0]*(r+1) for _ in range(n+1)]
    tab[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,r)+1):
            tab[i][j]=tab[i-1][j-1]+j*tab[i-1][j]
    return tab[n][r]

@lru_cache(None)
def C(r,L):
    return sum(stirling(L+1,j+1) for j in range(min(r,L)+1))

@lru_cache(None)
def count(m,k,L):
    a=m*(k+1)
    return sum(a**ell for ell in range(L))+m**L*sum(falling(k,r)*C(r,L) for r in range(k+1))

def state(word,L):
    s=()
    for d,p in word:
        if p!=0:
            s=tuple(t for t in s if t!=p)+(p,)
    return s,tuple(word[-L:]) if L else ()

def perm_rank(s,k):
    rem=list(range(1,k+1));r=len(s);n=0
    for i,x in enumerate(s):
        z=rem.index(x)
        n+=z*falling(k-i-1,r-i-1)
        rem.pop(z)
    return n

def perm_unrank(n,k,r):
    out=[];rem=list(range(1,k+1))
    for i in range(r):
        block=falling(k-i-1,r-i-1)
        q,n=divmod(n,block)
        out.append(rem.pop(q))
    return tuple(out)

@lru_cache(None)
def suffix_dp(L,j):
    f=[[0]*(j+1) for _ in range(L+1)]
    f[0][j]=1
    for t in range(1,L+1):
        for h in range(j+1):
            f[t][h]=(1+h)*f[t-1][h]+(f[t-1][h+1] if h<j else 0)
    return f

def allowed(s,j,h):
    names=set(s[-i] for i in range(1,h+1))
    if h<j:
        names.add(s[-h-1])
    return sorted((0,*names))

def update_h(x,s,j,h):
    return h+1 if h<j and x==s[-h-1] else h

def prov_rank(s,L,pword):
    j=len(set(pword)-{0})
    if j>len(s) or j>L:raise ValueError('invalid j')
    rev=pword[::-1]
    f=suffix_dp(L,j)
    idx=sum(stirling(L+1,v+1) for v in range(j))
    h=0
    for pos,x in enumerate(rev):
        if x not in allowed(s,j,h):raise ValueError('invalid last-occurrence order')
        t=L-pos-1
        for candidate in allowed(s,j,h):
            if candidate>=x:break
            idx+=f[t][update_h(candidate,s,j,h)]
        h=update_h(x,s,j,h)
    if h!=j:raise ValueError('missing label')
    return idx

def prov_unrank(s,L,z):
    r=len(s)
    for j in range(min(r,L)+1):
        block=stirling(L+1,j+1)
        if z<block:break
        z-=block
    else:raise ValueError('provenance code out of range')
    f=suffix_dp(L,j)
    h=0;rev=[]
    for pos in range(L):
        t=L-pos-1
        for x in allowed(s,j,h):
            n=f[t][update_h(x,s,j,h)]
            if z>=n:
                z-=n
                continue
            rev.append(x)
            h=update_h(x,s,j,h)
            break
        else:raise AssertionError('no branch')
    assert z==0 and h==j
    return tuple(rev[::-1])

def digit_rank(seq,base):
    ans=0
    for d in seq:ans=ans*base+d
    return ans

def digit_unrank(z,base,n):
    out=[0]*n
    for i in range(n-1,-1,-1):
        z,out[i]=divmod(z,base)
    assert z==0
    return tuple(out)

def rank(st,m,k,L):
    s,tail=st;a=m*(k+1)
    if len(tail)<L:
        assert s==state(tail,L)[0]
        ell=len(tail)
        return sum(a**u for u in range(ell))+digit_rank(
            [d*(k+1)+p for d,p in tail],a)
    short=sum(a**u for u in range(L))
    r=len(s)
    off=short+m**L*sum(falling(k,u)*C(u,L) for u in range(r))
    off+=perm_rank(s,k)*m**L*C(r,L)
    dirs=tuple(d for d,p in tail)
    ps=tuple(p for d,p in tail)
    return off+prov_rank(s,L,ps)*m**L+digit_rank(dirs,m)

def unrank(z,m,k,L):
    total=count(m,k,L)
    if not(0<=z<total):raise ValueError('rank out of range')
    a=m*(k+1)
    for ell in range(L):
        block=a**ell
        if z<block:
            digits=digit_unrank(z,a,ell)
            tail=tuple(divmod(v,k+1) for v in digits)
            return state(tail,L)
        z-=block
    for r in range(k+1):
        each=m**L*C(r,L)
        block=falling(k,r)*each
        if z<block:break
        z-=block
    else:raise AssertionError('source block missing')
    pr,z=divmod(z,each)
    s=perm_unrank(pr,k,r)
    pv,z=divmod(z,m**L)
    directions=digit_unrank(z,m,L)
    prov=prov_unrank(s,L,pv)
    return s,tuple(zip(directions,prov))

def compose(left,right,L):
    s1,t1=left;s2,t2=right
    s=tuple(v for v in s1 if v not in s2)+s2
    tail=(t1+t2)[-L:] if L else ()
    return s,tail

def run():
    summary={"schema":"R209_DIRECT_STIRLING_RANK_UNRANK_V1","status":"PASS",
             "check_type":"exact Python int; exhaustive where described",
             "models":[],"parameter_models":0,"roundtrips":0,"word_image_checks":0,
             "suffix_fibre_checks":0,"append_checks":0,"state_composition_checks":0}
    for m,k,L in product((1,2,3),(0,1,2),(0,1,2)):
        n=count(m,k,L)
        images=set()
        alpha=tuple(product(range(m),range(k+1)))
        for ln in range(k+L+1):
            for word in product(alpha,repeat=ln):
                st=state(word,L)
                images.add(st)
                idx=rank(st,m,k,L)
                assert unrank(idx,m,k,L)==st,(m,k,L,word,idx)
                summary["word_image_checks"]+=1
        assert len(images)==n,(m,k,L,n,len(images))
        visited=set()
        for i in range(n):
            s=unrank(i,m,k,L)
            assert rank(s,m,k,L)==i
            visited.add(s)
            summary["roundtrips"]+=1
        assert len(visited)==n and visited==images
        witnesses={}
        for ln in range(k+L+1):
            for word in product(alpha,repeat=ln):
                witnesses.setdefault(state(word,L),word)
        for i,(st,w) in enumerate(witnesses.items()):
            if i>=128:break
            for a in alpha:
                st2=state(w+(a,),L)
                assert compose(st,state((a,),L),L)==st2
                assert unrank(rank(st2,m,k,L),m,k,L)==st2
                summary["append_checks"]+=1
        reps=list(witnesses.items())[:min(12,n)]
        for st,w in reps:
            for other,v in reps:
                assert compose(st,other,L)==state(w+v,L),(m,k,L,w,v,st,other)
                summary["state_composition_checks"]+=1
        summary["models"].append({"m":m,"k":k,"L":L,"count":n,"complete":True})
        summary["parameter_models"]+=1
    for k in range(4):
        for L in range(5):
            for r in range(k+1):
                s=tuple(range(1,r+1));seen=set()
                for pv in product(range(k+1),repeat=L):
                    x=tuple((0,p) for p in pv)
                    last=state(x,L)[0]
                    if not last or (len(last)<=r and s[-len(last):]==last):
                        seen.add(pv)
                assert len(seen)==C(r,L),(k,L,r,len(seen),C(r,L))
                summary["suffix_fibre_checks"]+=1
    m,k,L=12,6,2
    n=count(m,k,L)
    assert n==1407685
    for idx in [0,1,84,85,10000,n//2,n-2,n-1]:
        assert rank(unrank(idx,m,k,L),m,k,L)==idx
        summary["roundtrips"]+=1
    summary["x6_case"]={"m":12,"k":6,"L":2,"state_count":n,
        "minimum_fixed_bits":(n-1).bit_length(),
        "full_tail_fibre":m**L*C(k,L),"stirling_fibre_C":C(k,L)}
    summary["depths"]=[{"L":L,"states":count(12,6,L),
        "fixed_bits":(count(12,6,L)-1).bit_length()} for L in range(6)]
    summary["large_rank_roundtrips"]=0
    for L in range(1,6):
        n=count(12,6,L)
        for i in [0,1,2,n//7,n//3,n//2,n*5//7,n-3,n-2,n-1]:
            assert rank(unrank(i,12,6,L),12,6,L)==i
            summary["large_rank_roundtrips"]+=1
    return summary

if __name__=="__main__":
    print(json.dumps(run(),sort_keys=True,indent=2))
