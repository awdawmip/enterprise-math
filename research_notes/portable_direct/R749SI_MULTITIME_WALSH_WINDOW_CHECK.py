#!/usr/bin/env python3
"""Exact finite tests for R749SI multi-time Walsh pullback and window-rank law.

The signed-Port transition is reconstructed from the 8 lifts of adjacent
unsigned two-axis supports; all arithmetic uses fractions.Fraction.
"""
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter
import json

AXES=range(6)
SUPPORTS=[frozenset(z) for z in combinations(AXES,2)]
EDGES=[(A,B) for A in SUPPORTS for B in SUPPORTS if len(A&B)==1]
assert len(EDGES)==120
NEXT={B:[C for C in SUPPORTS if len(B&C)==1] for B in SUPPORTS}
assert all(len(NEXT[B])==8 for B in SUPPORTS)

def states(edge):
    A,B=edge
    axes=tuple(sorted(A|B))
    return [dict(zip(axes,s)) for s in product((-1,1),repeat=3)]

def psi(state,subset):
    return __import__('math').prod(state[i] for i in subset)

def subset(edge,mask):
    axes=sorted(edge[0]|edge[1])
    return frozenset(a for i,a in enumerate(axes) if mask & (1<<i))

def law(A,B,C,x,p):
    assert C in NEXT[B]
    forced=(C==A^B)
    if p==1 and not forced:
        return None
    src=next(iter(A-B)); new=next(iter(C-B))
    assert len(B)==2
    out=[]
    if forced:
        assert src==new
        theta=8*p/(1+7*p)
        for sign,prob in ((x[src],(1+theta)/2),(-x[src],(1-theta)/2)):
            y={a:x[a] for a in B}; y[new]=sign
            if prob:out.append((y,prob))
    else:
        for sign in (-1,1):
            y={a:x[a] for a in B};y[new]=sign
            out.append((y,F(1,2)))
    assert sum((w for _,w in out),F(0))==1
    return out

def backward(edges,masks,p):
    # edges[t]=(support_t_left,support_t_right), masks[t] on the corresponding triple
    cur=frozenset();fact=F(1)
    for t in reversed(range(len(edges))):
        cur=cur^subset(edges[t],masks[t])
        if t==0:break
        A,B=edges[t-1]; C=edges[t][1]
        forced=(C==A^B)
        src=next(iter(A-B));new=next(iter(C-B))
        if forced:
            if new in cur:fact*=8*p/(1+7*p)
        elif new in cur:
            return F(0),frozenset()
        if not forced:
            cur=cur-{new}
        # for forced, new==src and copied B unchanged
    return fact,cur

def exact_paths(edges,x,p):
    outcomes=[([x],F(1))]
    for t in range(1,len(edges)):
        A,B=edges[t-1];C=edges[t][1]
        outcomes=[(path+[y],w*prob) for path,w in outcomes for y,prob in law(A,B,C,path[-1],p)]
    assert sum((w for _,w in outcomes),F(0))==1
    return outcomes

def check_word(edges,p):
    checks=0
    prior=states(edges[0]); paths=[exact_paths(edges,x,p) for x in prior]
    for masks in product(range(8),repeat=len(edges)):
        factor,source=backward(edges,masks,p)
        for x,paths_x in zip(prior,paths):
            lhs=sum((w*__import__('math').prod(psi(path[t],subset(edges[t],masks[t])) for t in range(len(edges))) for path,w in paths_x),F(0))
            rhs=factor*psi(x,source)
            assert lhs==rhs, (edges,p,masks,x,lhs,rhs)
            checks+=1
    return checks

def matrix(edges,p):
    left,right=states(edges[0]),states(edges[-1])
    d={tuple(sorted(v.items())):j for j,v in enumerate(right)}
    M=[]
    for x in left:
        row=[F(0)]*8
        for path,w in exact_paths(edges,x,p):row[d[tuple(sorted(path[-1].items()))]]+=w
        M.append(row)
    return M

def rank(A):
    b=[r[:] for r in A];j=0;n=len(b)
    for k in range(len(b[0])):
        pivot=next((t for t in range(j,n) if b[t][k]),None)
        if pivot is None:continue
        b[j],b[pivot]=b[pivot],b[j]
        inv=b[j][k]
        b[j]=[v/inv for v in b[j]]
        for t in range(j+1,n):
            if b[t][k]:
                f=b[t][k]
                b[t]=[v-f*w for v,w in zip(b[t],b[j])]
        j+=1
        if j==n:break
    return j

def surviving(edges,p):
    start=set(edges[0][0]|edges[0][1]);h={a:a for a in start}
    for t in range(1,len(edges)):
        A,B=edges[t-1];C=edges[t][1]
        old=next(iter(A-B));new=next(iter(C-B))
        if C==A^B:
            if p==0:h[old]=None
        else:
            h.pop(old);h[new]=None
    return len(set(v for v in h.values() if v is not None))

def main():
    metrics=Counter()
    for p in (F(0),F(1,2)):
        for A,B in EDGES:
            for C in NEXT[B]:
                edges=[(A,B),(B,C)]
                metrics['single_step_joint_equalities']+=check_word(edges,p)
        a,b=EDGES[0]
        for c in NEXT[b]:
            for d in NEXT[c]:
                e=[(a,b),(b,c),(c,d)]
                metrics['two_step_joint_equalities']+=check_word(e,p)
                for start in range(3):
                    R=rank(matrix(e[:start+1],p))
                    assert R==2**surviving(e[:start+1],p)
                    metrics['window_rank_checks']+=1
    # The p=1 boundary has only forced positive-probability observed paths.
    for A,B in EDGES:
        C=A^B
        metrics['boundary_p1_equalities']+=check_word([(A,B),(B,C)],F(1))
    # Nonforced innovations can be jointly detectable even when their marginal is fair.
    A=frozenset((0,1));B=frozenset((1,2));C=frozenset((2,3));D=frozenset((3,4))
    e=[(A,B),(B,C),(C,D)]
    fact,S=backward(e,[0,1<<sorted(B|C).index(3),1<<sorted(C|D).index(3)],F(1,2))
    assert fact==1 and not S
    result={'status':'PASS','model':'R749SF 120 unsigned directed supports / eight signed lifts','parameter_values':['0','1/2','1'],
            'single_step_joint_equalities':metrics['single_step_joint_equalities'],
            'two_step_joint_equalities':metrics['two_step_joint_equalities'],
            'boundary_p1_equalities':metrics['boundary_p1_equalities'],
            'window_rank_checks':metrics['window_rank_checks'],
            'fresh_same_sign_cross_time_expectation':'1',
            'native_event_permission':False}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
