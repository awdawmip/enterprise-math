#!/usr/bin/env python3
"""R711.3: exact triangle closure of all six-vertex triple licenses."""
from itertools import combinations
from collections import Counter
from json import dump

V=tuple(range(6))
E=tuple(combinations(V,2)); T=tuple(combinations(V,3))
index={e:i for i,e in enumerate(E)}
triangle_edges=tuple(sum(1<<index[e] for e in combinations(t,2)) for t in T)
graph_triangles=[sum(1<<i for i,m in enumerate(triangle_edges) if (g&m)==m)
                 for g in range(1<<15)]
assert len(set(graph_triangles))==6115

def shadow(h):
    e=0
    while h:
        bit=h&-h
        e |= triangle_edges[bit.bit_length()-1]
        h ^= bit
    return e

def closure(h):
    return graph_triangles[shadow(h)]

def defect(h):
    c=closure(h)
    assert h|c==c
    assert closure(c)==c
    return (c^h).bit_count()

counts=Counter()
for h in range(1<<20):
    counts[defect(h)]+=1

assert sum(counts.values())==1<<20
assert counts[0]==6115

pasch=((0,1,2),(0,3,4),(1,3,5),(2,4,5))
mask=sum(1<<T.index(t) for t in pasch)
assert defect(mask)==4
missing=[list(t) for i,t in enumerate(T) if (closure(mask)^mask)>>i&1]
assert missing==[[0,1,3],[0,2,4],[1,2,5],[3,4,5]]

report={'schema':'EM_R711_SIX_AXIS_CLOSURE_V1','candidate_support_maps':1<<20,
        'graph_generated_maps':counts[0],
        'non_graph_generated_maps':(1<<20)-counts[0],
        'independent_graph_image_count':len(set(graph_triangles)),
        'closure_defect_distribution':dict(sorted(counts.items())),
        'pasch_missing_triads':missing,
        'status':'EXACT_ENUMERATION_PASS',
        'scope':'Six labeled indices; arbitrary Boolean 3-uniform support maps; no native V29/V39 admission'}
print('R711_PAIRWISE_TRIANGLE_SHADOW_CLOSURE_EXACT_PASS',
      1<<20,counts[0],len(set(graph_triangles)),counts[0],max(counts))
