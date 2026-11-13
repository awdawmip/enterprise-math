#!/usr/bin/env python3
"""R762L exact S6-equivariant signed-triad admissibility and pair-fiber classification.
Pure candidate incidence, not physical TRIADIC_CLOSURE_E admission or V29/V39 dynamics.
"""
import itertools
import json
from collections import Counter, defaultdict

AXES = range(6)
PORTS = [(i,s) for i in AXES for s in (-1,1)]
TRIADS = [tuple((a,s) for a,s in zip(ax,sgn))
          for ax in itertools.combinations(AXES,3)
          for sgn in itertools.product((-1,1),repeat=3)]
VISIBLES = [tuple((a,s) for a,s in zip(ax,sgn))
            for ax in itertools.combinations(AXES,2)
            for sgn in itertools.product((-1,1),repeat=2)]
PERMS = list(itertools.permutations(AXES))

def neg(t):
    return sum(s==-1 for a,s in t)

def orientation_image(t, chi, pi):
    order = [t[0],t[1],t[2]] if chi == 0 else [t[0],t[2],t[1]]
    image = [(pi[a],s) for a,s in order]
    sorted_image = tuple(sorted(image))
    index = [sorted_image.index(x) for x in image]
    inv = sum(index[i]>index[j] for i in range(3) for j in range(i+1,3))
    return sorted_image, inv%2

assert len(TRIADS)==160 and len(VISIBLES)==60 and len(PERMS)==720
assert Counter(map(neg,TRIADS))=={0:20,1:60,2:60,3:20}
for k in range(4):
    sample = next(t for t in TRIADS if neg(t)==k)
    orbit = {tuple(sorted((pi[a],s) for a,s in sample)) for pi in PERMS}
    assert orbit=={t for t in TRIADS if neg(t)==k}
for t in TRIADS:
    repeated = next((p,q) for p,q in itertools.combinations(t,2) if p[1]==q[1])
    i,j = repeated[0][0],repeated[1][0]
    pi=list(AXES); pi[i],pi[j]=pi[j],pi[i]
    assert orientation_image(t,0,pi)==(t,1)
    assert orientation_image(t,1,pi)==(t,0)

branches=defaultdict(list)
for t in TRIADS:
    for hidden in t:
        visible=tuple(p for p in t if p!=hidden)
        for chi in (0,1):
            branches[visible].append((neg(t), hidden[1],chi))
assert len(branches)==60
assert all(len(b)==16 for b in branches.values())

class_data=[]
collisions=defaultdict(list)
for bits in itertools.product((0,1),repeat=4):
    K=[i for i in range(4) if bits[i]]
    for r in range(3):
        matches=[v for v in VISIBLES if neg(v)==r]
        for v in matches:
            observed=[(hidden_sign,chi) for k,hidden_sign,chi in branches[v] if bits[k]]
            positive=sum(s==1 for s,chi in observed)
            negative=sum(s==-1 for s,chi in observed)
            assert positive==8*bits[r]
            assert negative==8*bits[r+1]
    totals=tuple(8*(bits[r]+bits[r+1]) for r in range(3))
    refined=tuple((8*bits[r],8*bits[r+1]) for r in range(3))
    class_data.append({'admitted_negative_counts':K,
                       'pair_total_by_visible_negative_count':list(totals),
                       'by_hidden_sign':list(map(list,refined))})
    collisions[totals].append(K)
assert len(class_data)==16
assert len(collisions)==15
ambiguous={','.join(map(str,k)):v for k,v in collisions.items() if len(v)>1}
assert ambiguous=={'8,8,8':[[1,3],[0,2]]}
assert len({tuple(tuple(p) for p in c['by_hidden_sign']) for c in class_data})==16

record={'schema':'R762L_S6_TRIAD_ADMISSIBILITY_CENSUS_V1',
        'science':'candidate signed three-distinct-axis incidence, S6 covariance, no physical event claim',
        'axis_permutations_checked':len(PERMS),
        'oriented_triads':2*len(TRIADS),
        'unoriented_triads':len(TRIADS),
        'visible_pairs':len(VISIBLES),
        'S6_orbit_sizes_by_negative_count':dict(Counter(map(neg,TRIADS))),
        'all_160_supports_have_chirality_reversing_S6_stabilizer':True,
        'S6_invariant_boolean_admission_laws':16,
        'pair_total_signatures':15,
        'only_pair_total_collision':ambiguous,
        'refined_hidden_sign_signatures':16,
        'classes':class_data,
        'all_checks':'PASS'}
print(json.dumps(record,ensure_ascii=False,indent=2))
