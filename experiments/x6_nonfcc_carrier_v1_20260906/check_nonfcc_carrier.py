#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, permutations, product

# K4 edge labels and current FCC line representatives.
V={
    'AB':(1,1,0),
    'AC':(1,0,1),
    'AD':(0,1,-1),
    'BC':(0,1,1),
    'BD':(1,0,-1),
    'CD':(1,-1,0),
}
EDGES=tuple(V)

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def mul(s,a): return tuple(s*x for x in a)
def add3(a,b,c): return tuple(x+y+z for x,y,z in zip(a,b,c))

def graph_type(tri):
    deg={v:0 for v in 'ABCD'}
    for e in tri:
        deg[e[0]]+=1; deg[e[1]]+=1
    ds=sorted(deg.values(),reverse=True)
    if ds==[3,1,1,1]: return 'STAR'
    if ds==[2,2,2,0]: return 'FACE'
    if ds==[2,2,1,1]: return 'PATH'
    raise AssertionError(ds)

def good_signs(tri):
    out=[]
    for signs in product((-1,1),repeat=3):
        sv=[mul(s,V[e]) for s,e in zip(signs,tri)]
        pairs=[dot(sv[i],sv[j]) for i,j in combinations(range(3),2)]
        if pairs==[-1,-1,-1] and add3(*sv)==(0,0,0): out.append(signs)
    return tuple(out)

counts=Counter(); orientable=[]
for tri in combinations(EDGES,3):
    typ=graph_type(tri); gs=good_signs(tri)
    raw=[dot(V[a],V[b]) for a,b in combinations(tri,2)]
    prod=raw[0]*raw[1]*raw[2]
    counts[typ]+=1
    if typ=='STAR':
        assert prod==-1 and 0 not in raw and len(gs)==2
    elif typ=='FACE':
        assert prod==1 and 0 not in raw and len(gs)==0
    else:
        assert 0 in raw and len(gs)==0
    if gs: orientable.append((tri,gs))
assert counts==Counter({'PATH':12,'STAR':4,'FACE':4})
assert len(orientable)==4

# Native S6 is transitive on all 3-subsets; number of permutations mapping one
# fixed 3-subset to another is exactly 3!*3!=36.
ref=frozenset((0,1,2)); target=frozenset((0,3,5))
num=0
for p in permutations(range(6)):
    if frozenset(p[i] for i in target)==ref: num+=1
assert num==36

# Global Euclidean no-go: after the triangle sign condition globally gauges all
# pairwise correlations to -1/2, the all-ones Gram quadratic is negative.
n=6
# 1^T G 1 with diag 1, offdiag -1/2.
from fractions import Fraction
q=Fraction(n,1)+2*Fraction(n*(n-1)//2,1)*Fraction(-1,2)
assert q==Fraction(-9,1) and q<0

# Explicit FACE and PATH witnesses.
face=('AB','AC','BC')
assert [dot(V[a],V[b]) for a,b in combinations(face,2)]==[1,1,1]
path=('AB','AC','BD')
assert 0 in [dot(V[a],V[b]) for a,b in combinations(path,2)]

print('PASS_X6_NONFCC_CARRIER_V1')
print('S4_orbits',dict(counts))
print('current_FCC_120_charts',len(orientable))
print('nonSTAR_current_FCC_120_charts',0)
print('S6_maps_one_triple_to_reference',num)
print('global_six_line_Euclidean_all20_possible',False)
print('global_Gram_ones_quadratic',q)
