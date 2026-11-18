#!/usr/bin/env python3
"""Finite signed-X6 seven-operation, nine-history BRC observer model.
Frozen mathematical input is from EC49ET; operation order and provenance retained.
Contains an exhaustive complete p-fiber generator without external project imports.
"""
from functools import lru_cache
from collections import defaultdict

OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
     'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
STATES=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')
BASE=('ce','de','ec','ed')


def path(w):return tuple(s for a in w for s in OPS[a])
def poscount(w):
    x=path(w);return tuple(x.count(j) for j in range(1,7))
def displacement(w):
    x=path(w);return tuple(x.count(j)-x.count(-j) for j in range(1,7))
def signature(w):
    out=[]
    for event,prev in STATES:
        for step in path(w):
            if prev==1 and step==2:
                event={'N':'A','B':'BA'}.get(event,event)
            elif prev==2 and step==1:
                event={'N':'B','A':'AB'}.get(event,event)
            prev=step
        out.append(BUCKETS.index(event))
    return tuple(out)

T4=frozenset(signature(w) for w in BASE)
T2=frozenset(signature(w) for w in ('feg','gef'))
P0=poscount('ce')
PAID_BASE={t[:i] for w in BASE for t in [path(w)] for i in range(1,len(t)+1)}
assert len(T4)==4 and len(T2)==2 and T4.isdisjoint(T2) and len(PAID_BASE)==28

@lru_cache(None)
def words(h,p):
    """All ordered returning words of length h with complete positive-step p.

    From net +2 E1: b=0, e=a+1.  Put r=c+d=p1+p2-1-h,
    then a=e-1, f=p1-r-2e, g=p2-r. Exhaustive multiset
    permutations for c=0..r; no rank or signature pruning here.
    """
    p1,p2,e,*rest=p
    if any(rest):return tuple()
    r=p1+p2-h-1; a=e-1; f=p1-r-2*e;g=p2-r
    if min(r,a,f,g)<0:return tuple()
    out=[]
    def rec(counts,w):
        if len(w)==h:out.append(w);return
        for token in 'acdefg':
            if counts[token]>0:
                counts[token]-=1;rec(counts,w+token);counts[token]+=1
    for nc in range(r+1):
        rec(dict(a=a,c=nc,d=r-nc,e=e,f=f,g=g),'')
    return tuple(out)

@lru_cache(None)
def T4_fibers(h):
    """Finite complete h-horizon p domain admitting all T4 signatures.
    The bounds p1<=2h, p2<=h, e<=ceil((h+1)/2) follow
    directly from the primitive token strings and returning equation.
    """
    out={}
    for e in range(1,(h+2)//2+1):
        for p1 in range(0,2*h+1):
            for p2 in range(0,h+1):
                p=(p1,p2,e,0,0,0)
                w=words(h,p)
                if w and T4.issubset({signature(x) for x in w}):out[p]=w
    return out


def rank_mod(signatures,prime=1000003):
    pivots={};rank=0
    for sig in signatures:
        for bucket in range(5):
            v=[int(x==bucket) for x in sig]
            for i in range(9):
                if not v[i]:continue
                if i in pivots:
                    mul=v[i]
                    for j in range(i,9):v[j]=(v[j]-mul*pivots[i][j])%prime
                else:
                    inv=pow(v[i],-1,prime)
                    pivots[i]=[(x*inv)%prime for x in v]
                    rank+=1;break
    return rank
