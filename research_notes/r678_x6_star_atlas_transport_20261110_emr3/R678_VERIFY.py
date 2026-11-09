#!/usr/bin/env python3
"""R678: classify K4 STAR atlas support frames within signed X6; exact S6 enumeration."""
from itertools import permutations
from collections import deque
import json
from pathlib import Path
AXES=tuple(range(6))
STARS=((0,2,5),(0,3,4),(1,2,4),(1,3,5))
CANON=tuple(sorted(STARS))

def p_sign(p):
    return sum(p[i]>p[j] for i in AXES for j in range(i+1,6))%2

def atlas_image(p,atlas=CANON):
    return tuple(sorted(tuple(sorted(p[i] for i in triple)) for triple in atlas))

def signed_c6_perm(triple):
    i,j,k=triple
    p=list(AXES);p[i],p[j],p[k]=j,k,i
    return tuple(p)

images_even=set(); images_odd=set();stabilizers=[]
for p in permutations(AXES):
    t=atlas_image(p)
    (images_even if not p_sign(p) else images_odd).add(t)
    if t==CANON:stabilizers.append(p)
assert len(images_even)==len(images_odd)==15
assert not images_even.intersection(images_odd)
assert len(images_even.union(images_odd))==30
assert len(stabilizers)==24 and all(p_sign(p)==0 for p in stabilizers)
assert 24*30==720

G=[signed_c6_perm(x) for x in STARS]
assert all(p_sign(x)==0 for x in G)
assert any(atlas_image(x)!=CANON for x in G)
S={CANON};q=deque([CANON])
while q:
    curr=q.popleft()
    for g in G:
        nxt=atlas_image(g,curr)
        if nxt not in S:S.add(nxt);q.append(nxt)
assert S==images_even and len(S)==15

g0=signed_c6_perm(STARS[0]);off=atlas_image(g0)
assert (2,3,4) in off and (2,3,4) not in CANON
assert len(stabilizers)*(1<<6)==1536
assert 23040//1536==15
assert 46080//1536==30

out={
 'schema':'EM_R678_ATLAS_ORBIT_EXACT_CERT_V1','status':'PASS',
 'verified':'R678_SIGNED_C6_STAR_ATLAS_15_30_FRAME_PASS',
 'star_atlas_zero_based':[list(t) for t in CANON],
 'all_label_permutations_checked':720,
 'underlying_even_axis_permutations':360,'underlying_odd_axis_permutations':360,
 'atlas_stabilizer_unsigned_order':24,
 'atlas_stabilizer_signed_order':1536,
 'atlas_even_frame_orbit':15,'atlas_odd_frame_orbit':15,
 'atlas_full_signed_frame_orbit':30,
 'local_four_c6_reach_even_frames':15,
 'local_generator_1_image_zero_based':[list(x) for x in off],
 'future_observer_scope':'current four unlabeled STAR supports, arbitrary signed-permutation actions, readout after each action',
 'source_frozen_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
 'remaining_question':'transport local C6 chirality, native outer microtrace and BRC path provenance across moving frames'
}
p=Path(__file__).with_name('R678_EVIDENCE.json')
p.write_text(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
print(out['verified'],'even',len(images_even),'odd',len(images_odd),'aut',len(stabilizers),'support_group',len(S))
