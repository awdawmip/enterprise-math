#!/usr/bin/env python3
"""R677: finite signed-axis C6 group closure and exact typed signed BRC fibers.
Run: python research_notes/r677_signed_c6_star_group_20261110_emr3/R677_VERIFY.py
Uses frozen Source native signed_brc.py; no trigonometric numerical evolution.
"""
from __future__ import annotations
import sys, json
from collections import deque
from itertools import combinations, product, permutations
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'experiments/x6_signed_native_spatial_v16_20260905'))
from signed_brc import shortest_event_count, shortest_path_multiplicity, endpoint_multiplicity, spatial_norm_squared

N=6
STARS=((0,2,5),(0,3,4),(1,2,4),(1,3,5))
IDENT=tuple(range(2*N))
SIX_IDENT=tuple(range(N))

def signed_c6(triple):
    i,j,k=triple
    assert len(set(triple))==3
    mapping=list(range(12))
    for src,dst in ((i,j),(j,k),(k,i+6)):
        mapping[src]=dst
        mapping[src+6]=(dst+6)%12
    return tuple(mapping)

def compose(p,q):
    return tuple(p[q[x]] for x in range(len(p)))

def power(g,n):
    h=tuple(range(len(g)))
    for _ in range(n): h=compose(g,h)
    return h

def gen_perm(triple):
    i,j,k=triple
    p=list(range(6))
    p[i],p[j],p[k]=j,k,i
    return tuple(p)

def closure(generators,idn):
    G={idn};q=deque([idn])
    while q:
        h=q.popleft()
        for g in generators:
            gh=compose(g,h)
            if gh not in G:G.add(gh);q.append(gh)
    return G

def subset_orbit(gens,seed):
    S={tuple(sorted(seed))};q=deque(S)
    while q:
        t=q.popleft()
        for p in gens:
            k=tuple(sorted(p[x] for x in t))
            if k not in S:S.add(k);q.append(k)
    return S

def vector_action(g,z):
    out=[0]*6
    for i,a in enumerate(z):
        j=g[i];out[j%6]=(-1 if j>=6 else 1)*a
    return tuple(out)

for t in STARS:
    g=signed_c6(t)
    assert power(g,6)==IDENT and power(g,3)!=IDENT
    assert frozenset(i for i in range(N) if power(g,3)[i]==i+6)==frozenset(t)
    for i in range(6):assert g[i+6]==(g[i]+6)%12

rows=[]
for k in range(1,5):
    for idx in combinations(range(4),k):
        triples=[STARS[i] for i in idx]
        signed=[signed_c6(t) for t in triples]
        perms=[gen_perm(t) for t in triples]
        perm_group=closure(perms,SIX_IDENT)
        group=closure(signed,IDENT)
        support=set().union(*map(set,triples))
        orbit=subset_orbit(perms,triples[0])
        if k==1:
            assert len(group)==6 and len(perm_group)==3 and len(orbit)==1
        elif k==2:
            assert len(support)==5 and len(group)==1920 and len(perm_group)==60
            assert orbit==set(combinations(sorted(support),3))
        else:
            assert len(support)==6 and len(group)==23040 and len(perm_group)==360
            assert orbit==set(combinations(range(6),3))
        assert all(sum(p[i]>p[j] for i in range(6) for j in range(i+1,6))%2==0 for p in perm_group)
        rows.append({'star_subset':list(idx),'generators':k,'axes_touched':len(support),'underlying_permutations':len(perm_group),'signed_group_order':len(group),'triple_orbit':len(orbit)})

G3=closure([signed_c6(t) for t in STARS[:3]],IDENT)
assert all(signed_c6(t) in G3 for t in combinations(range(6),3))
odd=list(range(12))
odd[0],odd[1]=odd[1],odd[0]
odd[6],odd[7]=odd[7],odd[6]
Gplus=closure([signed_c6(t) for t in STARS[:3]]+[tuple(odd)],IDENT)
assert len(Gplus)==46080

checked=0
for z in product((-1,0,1),repeat=6):
    for g in [signed_c6(t) for t in STARS[:3]]:
        z1=vector_action(g,z)
        assert shortest_event_count(z1)==shortest_event_count(z)
        assert spatial_norm_squared(z1)==spatial_norm_squared(z)
        assert shortest_path_multiplicity(z1)==shortest_path_multiplicity(z)
        assert endpoint_multiplicity(6,z1)==endpoint_multiplicity(6,z)
        checked+=1

z=(1,-2,1,0,0,0)
steps=[0,7,7,2]  # +E1, -E2, -E2, +E3; 0-based signed axis letters
words=set(permutations(steps))
assert len(words)==12 and len(words)==shortest_path_multiplicity(z)
for g in [signed_c6(t) for t in STARS]:
    mapped={tuple(g[x] for x in w) for w in words}
    assert len(mapped)==12 and shortest_path_multiplicity(vector_action(g,z))==12

result={
 'schema':'EM_R677_EXACT_FINITE_EVIDENCE_V1','status':'PASS',
 'verified':'R677_THREE_STAR_SIGNED_C6_BRC_EXACT_PASS',
 'star_triples_zero_based':[list(s) for s in STARS],
 'star_subset_census':rows,
 'four_star_order':23040,'three_star_order':23040,'two_star_order':1920,'one_star_order':6,
 'full_signed_even_axis_group_order':23040,'odd_axis_swap_extension_order':46080,
 'full_20_triads_generators_all_in_three_star_group':True,
 'typed_brc_signed_vectors_checked':checked,'example_z':list(z),
 'example_shortest_brc_multiplicity':12,
 'source_kernel':'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py @ frozen a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'computation':'Python stdlib exact permutation+integer BFS, Source typed signed_brc'
}
out=Path(__file__).with_name('R677_EVIDENCE.json')
out.write_text(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf-8')
print(result['verified'])
print('census',[(r['star_subset'],r['signed_group_order']) for r in rows])
print('BRC checks',checked)
print('evidence',out)
