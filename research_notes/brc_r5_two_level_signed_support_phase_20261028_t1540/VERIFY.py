#!/usr/bin/env python3
"""Exact standalone R5 22-history signed-support phase certificate."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
ZERO,ONE=F(0),F(1)
RATIOS=(F(1,2),ONE,F(3,2))
ROWS={"A":(F(1,4),F(1,2),F(1,4)),"B":(F(1,8),F(3,4),F(1,8))}
def build():
    nodes={}
    for tag in ("A","B"):
        root=(tag,)
        nodes[root]=(1,ONE,F(1,2),[])
        for i,(qprob,ratio) in enumerate(zip(ROWS[tag],RATIOS)):
            h=(tag,i)
            nodes[h]=(2,ratio,F(1,2)*qprob,[])
            nodes[root][3].append(h)
            if i==1:
                cond,final=ROWS[tag],RATIOS
            else:
                cond,final=(F(1,2),F(1,2)),(ratio*F(3,4),ratio*F(5,4))
            for j,(qc,s) in enumerate(zip(cond,final)):
                child=(tag,i,j)
                nodes[child]=(3,s,nodes[h][2]*qc,[])
                nodes[h][3].append(child)
    assert len(nodes)==22
    leaves=[v for v in nodes.values() if v[0]==3]
    assert len(leaves)==14
    assert sum(q for _,r,q,_ in leaves)==1
    assert sum(r*q for _,r,q,_ in leaves)==1
    for t,r,q,children in nodes.values():
        assert q>0 and r>0
        if children:
            assert sum(nodes[ch][2] for ch in children)==q
            assert sum(nodes[ch][1]*nodes[ch][2] for ch in children)==q*r
    return nodes
NODES=build()
FIBERS=((1,ONE),(2,F(1,2)),(2,ONE),(2,F(3,2)))
def full_bellman(lam):
    a,b,c,d=map(F,lam)
    vals={}
    for h in sorted(NODES,key=lambda k:-len(k)):
        t,r,q,children=NODES[h]
        opts=[b*q,a*r*q]
        if children:
            opts.append(q*(c*r+d)+sum(vals[ch] for ch in children))
        vals[h]=min(opts)
    return c+d+sum(vals[(tag,)] for tag in ("A","B"))
def lr_exhaustive_81(lam):
    a,b,c,d=map(F,lam)
    best=None
    count=0
    for choices in product(("P","Q","C"),repeat=4):
        acts=dict(zip(FIBERS,choices))
        def rec(h):
            t,r,q,children=NODES[h]
            if t==3:return min(b*q,a*r*q)
            move=acts[(t,r)]
            if move=="P":return b*q
            if move=="Q":return a*r*q
            return q*(c*r+d)+sum(rec(ch) for ch in children)
        value=c+d+sum(rec((tag,)) for tag in ("A","B"))
        if best is None or value<best:
            best=value
        count+=1
    assert count==81
    return best
def gap(w):
    w=F(w)
    assert F(17,2)<=w<=12
    if w<=F(26,3) or w>=F(46,5):return ZERO
    if w<=F(170,19):return (9*w-78)/16
    return (46-5*w)/8
def witness():
    acts={}
    for h,(t,r,q,children) in NODES.items():
        if t==1:acts[h]="C" if h==("A",) else "P"
        elif t==2:acts[h]="Q" if r<1 else ("C" if r>1 else "P")
        else:acts[h]="Q" if r<1 else "P"
    ep=eq=tp=tq=ZERO
    reach={("A",):F(1,2),("B",):F(1,2)}
    for t in (1,2,3):
        nxt=defaultdict(lambda:ZERO)
        for h,w in reach.items():
            _,r,q,children=NODES[h]
            move=acts[h]
            if move!="C":
                ep+=w*r*(move=="Q")
                eq+=w*(move=="P")
                tp+=t*w*r
                tq+=t*w
            else:
                for ch in children:
                    nxt[ch]+=w*NODES[ch][2]/q
        reach=nxt
    assert not reach
    return ep,eq,tp,tq
if __name__=="__main__":
    for w in (F(17,2),F(26,3),F(35,4),F(170,19),F(9),F(46,5),F(12)):
        lam=(4,4,-8,w)
        f=full_bellman(lam)
        l=lr_exhaustive_81(lam)
        assert l-f==gap(w)
        print(f"w={w}: full={f}, LR={l}, gap={l-f}")
    O=witness()
    assert O==(F(1,16),F(7,8),F(27,16),F(13,8))
    assert sum(a*b for a,b in zip((4,4,-8,9),O))==F(39,8)
    assert full_bellman((4,4,-8,9))==F(39,8)
    assert lr_exhaustive_81((4,4,-8,9))==F(5)
    assert gap(F(170,19))==F(3,19)
    peak=(38,38,-76,85)
    assert full_bellman(peak)==F(91,2)
    assert lr_exhaustive_81(peak)==F(47)
    assert sum(a*b for a,b in zip(peak,O))==F(91,2)
    assert F(3,2)/sum(abs(a) for a in peak)==F(1,158)
    print("witness O=(1/16,7/8,27/16,13/8); signed support (4,4,-8,9): 39/8 < 5")
    print("peak direction (38,38,-76,85): signed support gap=3/2; L-infinity distance >=1/158")
    print("complete LR deterministic early-fiber search=81 policies; full raw-history Bellman exact")
    print("PASS_EXACT_R5_TWO_LEVEL_SUPPORT_PHASE")
