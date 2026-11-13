#!/usr/bin/env python3
"""R761 exact finite test: S6-covariant oriented-positive-port triad candidate.

Local provenance-label permutation on six native-axis ports, not an
admitted native P000 force transport or classical vector force balance.
"""
from itertools import combinations, permutations
from collections import deque, defaultdict
from math import factorial
import json

AXES = tuple(range(6))
E = AXES

def rotate_repr(t):
    a,b,c=t
    return min((a,b,c),(b,c,a),(c,a,b))

def all_oriented_triples():
    return sorted({rotate_repr(t) for s in combinations(AXES,3) for t in permutations(s)})

def invert(p):
    return tuple(p.index(i) for i in AXES)

def multiply(p,q):
    return tuple(p[q[i]] for i in AXES)

def update_perm(t):
    a,b,c=t
    v=list(E)
    v[a]=c; v[b]=a; v[c]=b
    return tuple(v)

def transport(t,sigma):
    return rotate_repr(tuple(sigma[i] for i in t))

def conjugate(p,sigma):
    return multiply(multiply(sigma,p),invert(sigma))

def parity(p):
    return sum(p[i]>p[j] for i in AXES for j in range(i+1,6)) % 2

def closure(gens):
    steps=tuple(gens)+tuple(invert(g) for g in gens)
    seen={E}; queue=deque([E]); layers={E:0}
    while queue:
        p=queue.popleft()
        for g in steps:
            h=multiply(p,g)
            if h not in seen:
                seen.add(h)
                layers[h]=layers[p]+1
                queue.append(h)
    return seen, layers

def verify():
    oriented=all_oriented_triples()
    assert len(oriented)==40
    support=sorted({frozenset(t) for t in oriented})
    assert len(support)==20
    each=defaultdict(list)
    for t in oriented: each[frozenset(t)].append(t)
    assert all(len(each[s])==2 for s in support)
    gen={t:update_perm(t) for t in oriented}
    for s,ts in each.items():
        a,b=ts
        assert gen[a]!=gen[b]
        assert gen[a]==invert(gen[b])
        assert multiply(multiply(gen[a],gen[a]),gen[a])==E
        assert parity(gen[a])==0
    for sigma in permutations(AXES):
        for t,g in gen.items():
            t2=transport(t,sigma)
            assert gen[t2]==conjugate(g,sigma), (sigma,t)
    for s in support:
        stabilizer=[p for p in permutations(AXES) if {p[i] for i in s}==set(s)]
        assert len(stabilizer)==36
        equivariant_local=[p for p in permutations(AXES)
                          if all(p[i]==i for i in AXES if i not in s)
                          and all(conjugate(p,h)==p for h in stabilizer)]
        assert equivariant_local==[E], (s,equivariant_local)
    orbit,depth=closure(tuple(gen.values()))
    assert len(orbit)==factorial(6)//2==360
    assert all(parity(p)==0 for p in orbit)
    for pair in combinations(AXES,2):
        cand=[t for t in oriented if set(pair).issubset(t)]
        assert len(cand)==8
    a=update_perm((0,1,2)); b=update_perm((0,1,3))
    small,_=closure([a,b])
    assert len(small)==12
    assert all(all(p[i]==i for i in (4,5)) for p in small)
    plus=gen[rotate_repr((0,1,2))]
    minus=gen[rotate_repr((0,2,1))]
    assert plus==(2,0,1,3,4,5)
    assert minus==(1,2,0,3,4,5)
    return {
      "schema":"EM_R761_ORIENTED_TRIAD_CANDIDATE_EXACT_V1",
      "native_axis_count":6,
      "unordered_supports":len(support),
      "oriented_supports":len(oriented),
      "full_s6_relabelings_checked":factorial(6),
      "equivariance_checks":factorial(6)*len(oriented),
      "support_stabilizers_checked":len(support),
      "support_stabilizer_size":36,
      "centralizer_local_candidates_per_support":1,
      "positive_equal_quantum_triads_per_visible_pair":4,
      "oriented_triads_per_visible_pair":8,
      "two_overlapping_triads_group_order":len(small),
      "all_triads_generated_port_group_order":len(orbit),
      "all_triads_generated_port_group_max_word_depth":max(depth.values()),
      "opposite_orientation_first_output":list(plus),
      "opposite_orientation_second_output":list(minus),
      "result":"PASS",
      "scope":"Positive-port equal-quantum local candidate; S6 axis reindexings; distinct provenance labels; not a P000-native physical transport or V29/V39 theorem"
    }

if __name__=='__main__':
    print(json.dumps(verify(),sort_keys=True,indent=2))
