#!/usr/bin/env python3
"""Exact six-axis triadic C12-root source-fiber certificate (author check).
Independent finite implementation of the cited frozen signed-permutation convention.
No original native benchmark, current downstream script, or other owner's PR is run.
"""
import json
from collections import Counter, defaultdict
from itertools import combinations

N=6
IDENTITY=tuple(range(1,N+1))
def require(p, msg):
    if not p: raise ValueError(msg)
def unit(i,sign=1):
    return tuple(sign if r==i else 0 for r in range(N))
def plus(a,b): return tuple(x+y for x,y in zip(a,b))
def signed_q(S):
    i,j,k=S
    q=list(IDENTITY)
    q[i],q[j],q[k]=-(j+1),-(k+1),-(i+1)
    return tuple(q)
def compose(g,h):
    return tuple((1 if x>0 else -1)*g[abs(x)-1] for x in h)
def power(g,n):
    p=IDENTITY
    for _ in range(n):p=compose(g,p)
    return p
def act(g,z):
    out=[0]*N
    for i,c in enumerate(z):
        if c:
            image=g[i]
            out[abs(image)-1]+=(1 if image>0 else -1)*c
    return tuple(out)

fibers=defaultdict(list)
nexts=defaultdict(set)
for i,j,k in combinations(range(N),3):
    q=signed_q((i,j,k))
    require(power(q,6)==IDENTITY, 'Q^6')
    for orientation,op in (('+',q),('-',power(q,5))):
        orb=[unit(i)]
        for _ in range(5):orb.append(act(op,orb[-1]))
        require(len(set(orb))==6, 'macro C6')
        require(act(op,orb[-1])==orb[0], 'orbit closed')
        micro=[]
        for s in range(6):micro.extend((orb[s],plus(orb[s],orb[(s+1)%6])))
        require(len(set(micro))==12, 'outer C12')
        root=micro[3]
        predicted=(plus(unit(k),unit(j,-1)) if orientation=='+' else plus(unit(j),unit(k,-1)))
        require(root==predicted, 'root formula')
        require(sum(abs(x) for x in root)==2, 'BRC shortest T')
        require(sum(x*x for x in root)==2, 'native square G')
        successor=act(op,root)
        predicted_succ=(plus(unit(k),unit(i,-1)) if orientation=='+' else plus(unit(j),unit(i,-1)))
        require(successor==predicted_succ, 'frame-selected successor')
        fibers[root].append({'triad':[i+1,j+1,k+1], 'orientation':orientation})
        nexts[root].add(successor)

h=Counter(len(v) for v in fibers.values())
nh=Counter(len(v) for v in nexts.values())
require(len(fibers)==20 and sum(map(len,fibers.values()))==40, 'fibers count')
require(h=={1:8,2:6,3:4,4:2}, 'fiber histogram')
require(nh==h, 'distinct next states')
ambiguous=sum(len(v)>1 for v in fibers.values())
require(ambiguous==12, 'ambiguity count')
root=plus(unit(4),unit(2,-1))
example=fibers[root]
require(example==[{'triad':[1,3,5], 'orientation':'+'},{'triad':[2,3,5], 'orientation':'+'}], 'example inputs')
example_outputs=sorted([list(x) for x in nexts[root]])
require(example_outputs==sorted([list(plus(unit(4),unit(0,-1))),list(plus(unit(4),unit(1,-1)))]), 'example next')
result={'schema':'X6_UNIT76_FRAME_FIBER_CERTIFICATE_V1',
 'source_scope':'Frozen P000 V5 signed six-axis Cell; separately current 2026-09-06 triad code exact source',
 'triads':20,'oriented_source_readouts':40,'distinct_signed_root_cells':20,
 'root_fiber_size_histogram':{str(k):v for k,v in sorted(h.items())},
 'root_successor_output_histogram':{str(k):v for k,v in sorted(nh.items())},
 'nonfactorizing_root_cells':ambiguous,
 'example_root':list(root),'example_source_triads':example,
 'example_successors':example_outputs,
 'universal_formulas':'R_+(i,j,k)=e_k-e_j; R_-(i,j,k)=e_j-e_k; Q(R_+)=e_k-e_i; Q^-1(R_-)=e_j-e_i',
 'status':'AUTHOR_EXACT_FINITE_EXECUTED_UNREVIEWED_NOT_ADMITTED'}
print(json.dumps(result,ensure_ascii=False,sort_keys=True,separators=(',',':')))
