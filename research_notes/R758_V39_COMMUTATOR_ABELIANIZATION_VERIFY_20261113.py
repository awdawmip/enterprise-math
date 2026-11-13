#!/usr/bin/env python3
"""R758 exact observer/abelianization check for the V39 three based-loop macro packets."""
from itertools import combinations, permutations, product
from collections import Counter
from fractions import Fraction
import json

S3 = tuple(permutations(range(3)))
e = (0, 1, 2)

def mul(x, y):
    """Composition x after y."""
    return tuple(x[y[i]] for i in range(3))

def inv(x):
    return tuple(x.index(i) for i in range(3))

def end(order, labels):
    h = e
    for p in order:  # V39 packet order P;Q has h(Q) o h(P)
        h = mul(labels[p], h)
    return h

def is_normal(H):
    if e not in H or any(mul(inv(a), b) not in H for a, b in product(H, repeat=2)):
        return False
    return all(mul(mul(g,h), inv(g)) in H for g,h in product(S3,H))

normals = []
for size in range(1, 7):
    for indices in combinations(range(6), size):
        H = frozenset(S3[i] for i in indices)
        if is_normal(H):
            normals.append((len(H), sorted(','.join(map(str,p)) for p in H)))
assert sorted(n for n, _ in normals) == [1, 3, 6]

three_cycles = {(1,2,0), (2,0,1)}
A3 = frozenset({e, *three_cycles})
assert any(set(x) == {','.join(map(str,p)) for p in A3} for n,x in normals if n==3)

freq = Counter(); pairs = Counter(); patterns = Counter()
for a,b in product(S3, repeat=2):
    c = mul(inv(a), inv(b))
    H = {'A':a, 'B':b, 'C':c}
    out = {''.join(p):end(p,H) for p in permutations('ABC')}
    assert all(out[o] == e for o in ('ABC', 'BCA', 'CAB'))
    assert all(v in A3 for v in out.values())
    commute = mul(a,b) == mul(b,a)
    pairs['commuting' if commute else 'noncommuting'] += 1
    rev = Counter(out[s] for s in ('ACB','BAC','CBA'))
    if commute:
        assert rev == Counter({e:3})
        assert len(set(out.values())) == 1
    else:
        assert set(rev) == three_cycles and sorted(rev.values()) == [1,2]
        assert len(set(out.values())) == 3
        patterns[tuple(sorted(rev.values()))] += 1
    freq.update(out.values())
assert pairs == Counter({'commuting':18, 'noncommuting':18})
assert freq == Counter({e:162,(1,2,0):27,(2,0,1):27})
assert patterns == Counter({(1,2):18})

# Source-labelled fixed bow-tie (R757): A,B transpositions, C their inverse product
A = (0,2,1)
B = (1,0,2)
C = mul(inv(A),inv(B))
labels = {'A':A,'B':B,'C':C}
fixed = {''.join(p):list(end(p,labels)) for p in permutations('ABC')}
assert Counter(map(tuple, fixed.values())) == Counter({e:3,(1,2,0):2,(2,0,1):1})

probabilities = {','.join(map(str,k)):{'num':v,'den':216} for k,v in sorted(freq.items())}
assert Fraction(freq[e],216) == Fraction(3,4)
assert all(Fraction(freq[x],216) == Fraction(1,8) for x in three_cycles)
expected_prefix_bits = Fraction(3,4)*1 + Fraction(1,8)*2 + Fraction(1,8)*2
assert expected_prefix_bits == Fraction(5,4)

result = {
    'schema':'R758_V39_ABELIANIZATION_EXACT_V1',
    'model':'V39 completed based loop macros A,B,C=B^-1;A^-1; uniform pair/schedule only for optional ensemble',
    'source':'R757 @ ed0b15b4ba948a21150969478d8a6941db76b11f',
    'task_science_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
    'S3_pair_count':len(S3)**2,
    'S3_schedules_per_pair':6,
    'normal_subgroups':[{'size':n,'elements':elems} for n,elems in normals],
    'pair_classes':dict(pairs),
    'noncomm_reverse_fiber_patterns':{','.join(map(str,k)):v for k,v in patterns.items()},
    'uniform_pair_schedule_endpoint_counts':{','.join(map(str,k)):v for k,v in sorted(freq.items())},
    'uniform_pair_schedule_probabilities':probabilities,
    'huffman_optimal_mean_bit_length':{'numerator':expected_prefix_bits.numerator,'denominator':expected_prefix_bits.denominator},
    'R757_fixed_source_fibers':fixed,
    'theorems':{
        'all_endpoint_in_derived_group':True,
        'all_homomorphisms_to_abelian_groups_annihilate_endpoint':True,
        'S3_proper_group_quotients_cannot_detect_nontrivial_3cycle':True,
        'S3_noncommuting_reverse_multiplicity_2_1':True
    },
    'validation':'PASS',
    'arithmetic':'permutation tuples and exact fractions, no floating point'
}
print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
