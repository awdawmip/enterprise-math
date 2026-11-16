"""R762CH K4 STAR four-triad all-pair provenance check, exact integers."""
from itertools import combinations, permutations
from math import comb
import json
V=range(4)
E=list(combinations(V,2))
assert len(E)==6
stars={v:frozenset(e for e in E if v in e) for v in V}
star_pairs=set()
for s in stars.values():star_pairs |= set(combinations(sorted(s),2))
all_pairs=set(combinations(E,2))
hidden=all_pairs-star_pairs
assert len(star_pairs)==12 and len(hidden)==3
assert hidden=={(E[0],E[-1]),(E[1],E[4]),(E[2],E[3])}
for p in permutations(V):
    def move(e): return tuple(sorted(p[x] for x in e))
    assert {tuple(sorted((move(a),move(b)))) for a,b in star_pairs}==star_pairs
    assert {tuple(sorted((move(a),move(b)))) for a,b in hidden}==hidden
for q in range(2,11):
    assert q**12*q**3==q**15
    assert sum(comb(q,k) for k in range(q+1))**15==2**(15*q)
print(json.dumps({
 'K4_edge_axis_labels':[''.join(map(str,e)) for e in E],
 'four_STAR_triples':{str(v):[''.join(map(str,e)) for e in sorted(s)] for v,s in stars.items()},
 'visible_pairs':len(star_pairs),
 'dormant_pairs':['/'.join(''.join(map(str,e)) for e in pair) for pair in sorted(hidden)],
 'q3':{'star_classes':3**12,'star_bits':(3**12-1).bit_length(),'all_classes':3**15,
       'all_bits':(3**15-1).bit_length(),'hidden_fiber':3**3,
       'conditional_repair_bits':(3**3-1).bit_length(),
       'joint_bit_difference':(3**15-1).bit_length()-(3**12-1).bit_length()},
 'S4_permutations_checked':24,'q_range_checked':list(range(2,11)),
 'evidence_scope':'K4 EDGE-STAR CHART AND DECLARED STAR-PAIR DIAGNOSTIC OBSERVER; NATIVE EVENT LICENSING UNVERIFIED',
 'review':'NOT_REVIEWED'
},indent=2))
