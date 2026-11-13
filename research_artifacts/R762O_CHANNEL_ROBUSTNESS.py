#!/usr/bin/env python3
"""R762O: exact Q3 BRC pair-observer channel distance and sharp edge-budget census."""
from itertools import product
from collections import Counter
import json

Q = list(product((0, 1), repeat=3))
I = {s:i for i,s in enumerate(Q)}
E = [(I[s], I[tuple(x ^ (i == j) for i,x in enumerate(s))])
     for s in Q for j in range(3) if s[j] == 0]
assert len(Q) == 8 and len(E) == 12
LAWS = [tuple((n >> i) & 1 for i in range(8)) for n in range(256)]

def selected(mask):
    return [edge for j,edge in enumerate(E) if (mask >> j) & 1]

def degrees(mask):
    d = [0] * 8
    for u,v in selected(mask):
        d[u] += 1
        d[v] += 1
    return d

def edge_connectivity(mask):
    edges = selected(mask)
    # Up to complement, all nontrivial cuts are represented by 1 <= S < 128.
    return min(sum(((S >> u) & 1) != ((S >> v) & 1) for u,v in edges)
               for S in range(1,128))

def output(a,edges,weighted):
    return tuple(4*(a[u] + 2*a[v] if weighted else a[u] + a[v])
                 for u,v in edges)

def signature_distance(mask,weighted):
    es=selected(mask)
    signatures = set(output(a,es,weighted) for a in LAWS)
    pairs=list(signatures)
    distance = min((sum(x!=y for x,y in zip(p,q))
                    for i,p in enumerate(pairs) for q in pairs[i+1:]),default=0)
    return len(signatures),distance

qualified={x:[] for x in ('U1','U2','U3','W1','W2','W3')}
for mask in range(4096):
    lam=edge_connectivity(mask)
    mindeg=min(degrees(mask))
    for r in (1,2,3):
        if lam >= r: qualified['U'+str(r)].append(mask)
        if mindeg >= r: qualified['W'+str(r)].append(mask)

result = {
    'schema':'R762O_BRC_CHANNEL_ROBUSTNESS_EVIDENCE_V1',
    'parent_task':'RS-X6-TRIADIC-CLOSURE-DYNAMICS',
    'publication_id':'TP2-8B7E13C5904A2D6F1142',
    'frozen_science':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
    'predecessor':'R762N PR #2310 @ d73517ebad637d29e8fb541492ee0c09e4c95a4c',
    'model':'Boolean candidate signed X6 triad incidence on Q3; not native event admission',
    'cube_vertices':8,'cube_edges':12,'edge_subsets_tested':4096,
    'cut_subsets_per_mask':127,'candidate_laws':256,
    'observer_units':'4 times raw positive BRC branch counts',
    'thresholds':{}
}
for key,masks in qualified.items():
    count=min(m.bit_count() for m in masks)
    opts=[m for m in masks if m.bit_count()==count]
    sample=opts[0]
    n,d=signature_distance(sample,key[0]=='W')
    assert n==(256 if key[0]=='W' else 255)
    assert d==int(key[-1])
    result['thresholds'][key]={
       'minimum_channels':count,'extremizers':len(opts),
       'witness_edge_indices':[i for i in range(12) if (sample>>i)&1],
       'observed_signatures':n,'brute_hamming_distance':d,
       'witness_min_degree':min(degrees(sample)),
       'witness_edge_connectivity':edge_connectivity(sample)}
expected={'U1':(7,384),'U2':(8,6),'U3':(12,1),
          'W1':(4,9),'W2':(8,9),'W3':(12,1)}
for k,(size,number) in expected.items():
    v=result['thresholds'][k]
    assert (v['minimum_channels'],v['extremizers'])==(size,number)
print(json.dumps(result,indent=2,ensure_ascii=False))
