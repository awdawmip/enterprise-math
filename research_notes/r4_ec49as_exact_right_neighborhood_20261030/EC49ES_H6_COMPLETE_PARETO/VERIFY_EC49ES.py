#!/usr/bin/env python3
"""EC49ES H=6 S=4, exact bounded native-X6 prefix-trie DP.

A bound discards only partial forests whose already incurred nonnegative native-edge
cost exceeds the global known feasible bound. Every completion has >= partial cost.
This proves all-case minimum against one supplied feasible construction; minima
within the bound are computed exactly. Baseline h2 is fixed at 28 edges.
"""
import os,sys,time,json
from concurrent.futures import ProcessPoolExecutor
from itertools import product
from collections import Counter,defaultdict
from VERIFY_EC49ER import *

FIBERS=None
T4=frozenset(signature(w) for w in BASE)
P0=poscount('ce')
PAID_BASE_FROZEN=PAID_BASE

class SimpleNode:
    __slots__=('kids','terminal')
    def __init__(self):self.kids={};self.terminal=0

def bounded_opt(fs, ps, bound, track=False):
    """return exact E when <=bound; else None. Bound covers entire E including 28 base."""
    root=SimpleNode()
    colors={}
    for h,p in zip(range(3,7),ps):
        words=fs[h][p]
        req=T4 # every selected fiber has unique exact minimal 4 signature basis
        for t in req:colors[(h,t)]=len(colors)
        for w in words:
            s=signature(w)
            if s not in req:continue
            node=root
            for step in path(w):node=node.kids.setdefault(step,SimpleNode())
            node.terminal |= (1<<colors[(h,s)])
    limit=bound-28
    stats=[0,0]
    def rec(n,prefix):
        stats[0]+=1
        cur={0:0}
        for step,ch in n.kids.items():
            sub=rec(ch,prefix+(step,))
            if not sub or not cur:return {}
            new={}
            for m1,c1 in cur.items():
                for m2,c2 in sub.items():
                    c=c1+c2
                    if c>limit: continue
                    k=m1|m2
                    if c<new.get(k,limit+1):new[k]=c
            cur=new
            if not cur:return {}
        if prefix:
            edgecost=int(prefix not in PAID_BASE_FROZEN)
            sel={0:0}
            for m,c0 in cur.items():
                mask=m|n.terminal
                if not mask:continue
                cost=c0+edgecost
                if cost<=limit and cost<sel.get(mask,limit+1):sel[mask]=cost
            cur=sel
        if len(cur)>stats[1]:stats[1]=len(cur)
        return cur
    res=rec(root,())
    allmask=(1<<len(colors))-1
    return {'E':res.get(allmask,limit+1)+28 if allmask in res else None, 'nodes':stats[0],'max_states':stats[1]}

def init_worker():
    global FIBERS
    FIBERS=fibers()

def worker(chunk, bound):
    global FIBERS
    if FIBERS is None:FIBERS=fibers()
    minE=bound+1
    best=None
    within=0;nodes=0;maxstates=0
    for ps in chunk:
        r=bounded_opt(FIBERS,ps,bound)
        nodes+=r['nodes'];maxstates=max(maxstates,r['max_states'])
        if r['E'] is not None:
            within+=1
            if r['E']<minE: minE=r['E'];best=ps
    return {'minE':minE,'best':best,'within':within,'nodes':nodes,'maxstates':maxstates,'cases':len(chunk)}
