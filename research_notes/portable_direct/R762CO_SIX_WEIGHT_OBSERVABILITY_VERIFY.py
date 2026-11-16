#!/usr/bin/env python3
"""R762CO: exhaustive exact K4 triad N-BRC source-observer checker.
Edge order 01,02,03,12,13,23. Candidate exchanges only; no native
TRIADIC_CLOSURE_E event authorization is assumed. Standard library only.
"""
import itertools
import json
from collections import Counter

V=tuple(range(4))
EDGES=tuple(itertools.combinations(V,2))
STATES=tuple(sorted({min(s,tuple(i for i in range(6) if i not in s))
                     for s in itertools.combinations(range(6),3)}))
IDX={s:i for i,s in enumerate(STATES)}
STARS={frozenset(EDGES.index(tuple(sorted((v,x)))) for x in V if x!=v)
       for v in V}
TYPE=tuple('F' if frozenset(s) in STARS or
           frozenset(set(range(6))-set(s)) in STARS else 'P' for s in STATES)
assert len(STATES)==10 and TYPE.count('F')==4 and TYPE.count('P')==6

def canonical(s):
    a=tuple(sorted(s))
    return min(a,tuple(i for i in range(6) if i not in a))

def swaps(i):
    a=set(STATES[i]); b=set(range(6))-a
    return tuple((x,y,IDX[canonical((a-{x})|{y})])
                 for x in sorted(a) for y in sorted(b))
SWAPS=tuple(swaps(i) for i in range(10))
assert all(len({j for x,y,j in row})==9 and i not in {j for x,y,j in row}
           for i,row in enumerate(SWAPS))

def transfer(w):
    m=[[0]*10 for _ in range(10)]
    for i,row in enumerate(SWAPS):
        for x,y,j in row:m[i][j]+=w[x]*w[y]
    return m

def observe(m,h):
    f=[int(k=='F') for k in TYPE]
    p=[int(k=='P') for k in TYPE]
    seq=[(TYPE[i],) for i in range(10)]
    for t in range(h+1):
        seq=[seq[i]+(f[i],p[i]) for i in range(10)]
        f=[sum(m[i][j]*f[j] for j in range(10)) for i in range(10)]
        p=[sum(m[i][j]*p[j] for j in range(10)) for i in range(10)]
    return seq

def nclasses(m,h):return len(set(observe(m,h)))

def symmetries():
    r=[]
    for p in itertools.permutations(V):
        e=tuple(EDGES.index(tuple(sorted((p[a],p[b])))) for a,b in EDGES)
        s=tuple(IDX[canonical(e[i] for i in a)] for a in STATES)
        r.append((e,s))
    return r
G=symmetries()
assert len(G)==24
assert all(any(s[i]!=i for i,k in enumerate(TYPE) if k=='F')
           for e,s in G if e!=tuple(range(6)))
for w in itertools.product((1,2),repeat=6):
    assert any(e!=tuple(range(6)) and
               all(w[e[i]]==w[i] for i in range(6)) for e,s in G)
    assert nclasses(transfer(w),9)<10

hist={}; lastdepth={}; maxone={}
for B in (1,2,3,4):
    h=Counter();last=0;one=0
    for w in itertools.product(range(1,B+1),repeat=6):
        m=transfer(w)
        assert m==list(map(list,zip(*m)))
        counts=[nclasses(m,t) for t in range(10)]
        assert counts[2]==counts[9]
        h[counts[9]]+=1
        one=max(one,counts[1])
        last=max(last,max((t for t in range(1,10)
                           if counts[t]!=counts[t-1]),default=0))
        if B<=3:assert counts[1]<10
    hist[str(B)]={str(k):v for k,v in sorted(h.items())}
    lastdepth[str(B)]=last
    maxone[str(B)]=one

w2=(1,1,2,3,2,3)
w1=(1,1,1,2,3,4)
w1_three_values=(1,1,2,4,2,4)
assert [nclasses(transfer(w2),t) for t in range(3)]==[2,9,10]
assert [nclasses(transfer(w1),t) for t in range(2)]==[2,10]
assert len(set(w1_three_values))==3 and nclasses(transfer(w1_three_values),1)==10

def degrees(w):
    total=sum(w)
    return tuple(sum(w[x] for x in s)*(total-sum(w[x] for x in s))
                 for s in STATES)
for top in range(6,13):
    for mid in itertools.combinations(range(2,top),4):
        assert len(set(degrees((1,)+mid+(top,))))<10
wd=(1,2,3,5,8,13)
assert len(set(degrees(wd)))==10
assert [sum(row) for row in transfer(wd)]==list(degrees(wd))
assert len(set(frozenset(tuple(sorted((x,y))) for x,y,j in row)
               for row in SWAPS))==10

result={
  'schema':'R762CO_EXACT_CERTIFICATE_V1',
  'named_edges':[''.join(map(str,e)) for e in EDGES],
  'ordered_states':[[ ''.join(map(str,EDGES[j])) for j in s] for s in STATES],
  'domain':'positive-integer six-edge source multiplicity, 10 unnamed 3+3 partitions; conditional K4 candidate swaps',
  'class_histogram_h9':hist,
  'max_refinement_depth_B_le_4':lastdepth,
  'maximum_one_step_classes':maxone,
  'time_two_full_witness':{'weights':w2,'class_counts':[2,9,10],
                           'signature_table':[list(s) for s in observe(transfer(w2),2)]},
  'time_one_full_witness':{'weights':w1,'class_counts':[2,10],
                           'signature_table':[list(s) for s in observe(transfer(w1),1)]},
  'three_value_time_one_witness':{'weights':w1_three_values,'classes':10},
  'degree_only_witness':{'weights':wd,'degrees':degrees(wd),
                         'optimal_max_positive_integer_weight':13},
  'symmetry_certificate':'24 K4 group elements; all 64 two-colour patterns have nonidentity stabilizer moving F',
  'finite_coverage':'B=1,2,3,4: 4890 labelled input weight vectors at depths t=0..9; normalized sorted 6 distinct weights with max<=12',
  'all_horizon_certification':'Cayley-Hamilton order 10 for exact integer 10x10 transfer',
  'native_event_licence':'UNRESOLVED',
  'independent_review':'NOT_REVIEWED',
  'author_check':'PASSED'
}
print(json.dumps(result,indent=2,ensure_ascii=False))
