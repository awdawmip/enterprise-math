#!/usr/bin/env python3
"""Exact finite checks for a conditional, S6-equivariant P000 triad-channel BRC lift.
The all-length claims are proved in the accompanying mathematical note.
No classical physical/phase computation is performed.
"""
from itertools import permutations, product, combinations
import json

ID=(0,1,2)
CARRIERS={
 'A': {
  'P':(0,2,1), 'Q':(1,0,2),
  'returns': {'I':('012','014','013','012'), 'P':('012','023','013','012'), 'Q':('012','023','123','012')}
 },
 'B': {
  'P':(0,2,1), 'Q':(2,1,0),
  'returns': {'I':('012','123','124','012'), 'P':('012','023','013','012'), 'Q':('012','123','013','012')}
 }
}

def mul(a,b):
    # Composition a o b, so a[b[i]] is image of slot i.
    return tuple(a[b[i]] for i in range(len(b)))

def power(a,k):
    v=tuple(range(len(a)))
    for _ in range(k):v=mul(v,a)
    return v

def update(letter,counts,k):
    c,a,b=counts
    if letter=='I':return (c+1,a,b),k
    if letter=='P':return (c,a+1,b),k
    if letter=='Q':
        b+=1
        epsilon_new=(a+b)%2
        k=(k+(1 if epsilon_new==0 else -1))%3
        return (c,a,b),k
    raise ValueError(letter)

def witness(letters,p,q):
    counts=(0,0,0);k=0;h=ID
    r=mul(p,q)
    for t in letters:
        counts,k=update(t,counts,k)
        h=mul(h,{'I':ID,'P':p,'Q':q}[t])
        eps=(counts[1]+counts[2])%2
        assert h==mul(power(r,k),power(p,eps)),(letters,h,counts,k)
    return counts,k,h

def seam_legal(u,v):
    # A return has triple root x>y>z>x; no backtracking at seam z!=y_next.
    return u[-2]!=v[1]

def is_arc(a,b):
    return len(set(a)&set(b))==2 and a!=b

results={}
for name,data in CARRIERS.items():
    p,q=data['P'],data['Q']
    assert p!=q and mul(p,p)==ID and mul(q,q)==ID
    r=mul(p,q)
    assert power(r,3)==ID and power(r,1)!=ID
    ret=data['returns']
    for word in ret.values():
        assert word[0]==word[-1]=='012'
        assert all(is_arc(word[i],word[i+1]) for i in range(3))
        assert all(word[i-1]!=word[(i+1)%3] for i in range(3))
    assert all(seam_legal(ret[x],ret[y]) for x in 'IPQ' for y in 'IPQ')
    checked=0
    for n in range(9):
        for word in product('IPQ',repeat=n):
            witness(word,p,q)
            checked+=1
    fibers={}
    for word in ('PPQQ','PQPQ','QPQP'):
        c,k,h=witness(word,p,q)
        fibers[word]={'counts':c,'k':k,'holonomy':''.join(map(str,h))}
    assert len({v['holonomy'] for v in fibers.values()})==3
    assert len({tuple(v['counts']) for v in fibers.values()})==1
    frame=(0,2,5)
    samples=tuple(product('IPQ',repeat=4))
    frames_considered=0
    for rotation in permutations(range(6)):
        rot_frame=tuple(rotation[j] for j in frame)
        for w in samples:
            _,_,h=witness(w,p,q)
            left=tuple(rotation[frame[h[i]]] for i in range(3))
            right=tuple(rot_frame[h[i]] for i in range(3))
            assert left==right
            assert set(frame[h[i]] for i in range(3))==set(frame)
        frames_considered+=1
    results[name]={
      'all_words_tested_length_0_to_8':checked,
      'S6_rotations_tested':frames_considered,
      'word_lengths_for_S6_check':4,
      'equivariance_cases':frames_considered*len(samples),
      'seam_pairs_checked':9,
      'same_ledger_distinct_holonomy':fibers,
      'three_state_residue_modulus':3,
      'conditional_native_triad_assumed':'one canonical equal-quantum TRIADIC_CLOSURE_E at chosen Cell',
      'native_V29_PASS_event_realization':'not checked; proposed coupling remains open'
    }

labels=frozenset(range(6))
parts={frozenset((frozenset(t),labels-frozenset(t)))
       for t in combinations(range(6),3)}
assert len(parts)==10
representative=next(iter(parts))
orbit={frozenset(frozenset(rot[i] for i in block) for block in representative)
       for rot in permutations(range(6))}
assert orbit==parts
stabilizer=sum(1 for rot in permutations(range(6))
               if frozenset(frozenset(rot[i] for i in block) for block in representative)==representative)
assert stabilizer==72
assert 720//stabilizer==len(parts)
assert not any(all(frozenset(frozenset(rot[i] for i in block) for block in pt)==pt
                       for rot in permutations(range(6))) for pt in parts)

results['six_quantum_two_triad_decomposition']={
 'axis_labels':6,'unordered_partitions':len(parts),'S6_orbit_size':len(orbit),
 'stabilizer_order':stabilizer,'canonical_selection_without_extra_mark':False,
 'minimal_fixed_width_branch_bits':4,
 'status':'structural decompositions conditional on six simultaneous canonical triads; global six-force stability not asserted'
}
print(json.dumps({'status':'PASS','model':'conditional P000-X6 S6-equivariant BRC triad channel','carriers':results},indent=2,ensure_ascii=False))
