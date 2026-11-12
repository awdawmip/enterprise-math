#!/usr/bin/env python3
"""Exact rooted closed X6 three-axis slice words: area-zero S3-frame anomalies.

Declared candidate transport: T_a = s*r**a (a=0,1,2), signed directions
share the same involutive T_a; later steps multiply on the left.
No floating point, stochastic sampling, or external dependencies.
"""
from collections import Counter
from itertools import combinations_with_replacement
import json

AXES = range(3)
PAIRS = ((0, 1), (0, 2), (1, 2))


def distinct_multiset_permutations(counts):
    """Exactly once per distinct word; signs are part of the token."""
    if all(v == 0 for v in counts.values()):
        yield ()
        return
    for token in sorted(counts):
        if counts[token]:
            counts[token] -= 1
            for rest in distinct_multiset_permutations(counts):
                yield (token,) + rest
            counts[token] += 1


def closed_words(number_of_pairs):
    """Every rooted, signed, zero-displacement word of length 2*k, once."""
    for selection in combinations_with_replacement(AXES, number_of_pairs):
        counts = {}
        for a in selection:
            counts[a, +1] = counts.get((a, +1), 0) + 1
            counts[a, -1] = counts.get((a, -1), 0) + 1
        yield from distinct_multiset_permutations(counts)


def observations(word):
    x = [0, 0, 0]
    A = [0, 0, 0]
    q = 0
    for j, (axis, sign) in enumerate(word):
        q += axis if j % 2 == 0 else -axis
        for t, (a, b) in enumerate(PAIRS):
            if axis == b:
                A[t] += x[a] * sign
        x[axis] += sign
    assert x == [0, 0, 0]
    return tuple(A), q % 3


def perm_comp(f, g):
    return tuple(f[g[k]] for k in range(3))


def perm_pow(p, exponent):
    ans = (0, 1, 2)
    for _ in range(exponent):
        ans = perm_comp(ans, p)
    return ans


r, s = (1, 2, 0), (1, 0, 2)
T = tuple(perm_comp(s, perm_pow(r, a)) for a in AXES)
assert perm_comp(s, perm_comp(r, s)) == perm_pow(r, 2)


def frame(word):
    ans = (0, 1, 2)
    for a, _ in word:
        ans = perm_comp(T[a], ans)
    return ans


def one_study(k):
    total = 0
    zero_area_q = Counter()
    nontrivial_axes = Counter()
    examples = {}
    for w in closed_words(k):
        A, q = observations(w)
        # Independent multiplication, not only a formula for the frame.
        assert frame(w) == perm_pow(r, q)
        total += 1
        if A == (0, 0, 0):
            zero_area_q[q] += 1
            if q:
                axes = tuple(sorted({a for a, _ in w}))
                nontrivial_axes[axes] += 1
                examples.setdefault(q, w)
    return {
        'length': 2*k,
        'all_closed_words': total,
        'zero_area_frame_counts': {str(q): zero_area_q[q] for q in range(3)},
        'zero_area_nontrivial_axes': {','.join(map(str, k)): v
                                      for k, v in sorted(nontrivial_axes.items())},
        'first_examples': {str(q): [[a, sign] for a, sign in w]
                           for q, w in sorted(examples.items())}
    }


S_plus = ((0,+1),(1,+1),(0,-1),(1,-1))
S_minus = ((0,+1),(1,-1),(0,-1),(1,+1))
W_hidden = S_plus + S_minus
W_trivial = ((0,+1),(0,-1))*4
assert observations(S_plus) == ((1,0,0),1)
assert observations(S_minus) == ((-1,0,0),1)
assert observations(W_hidden) == ((0,0,0),2)
assert observations(W_trivial) == ((0,0,0),0)
assert frame(W_hidden) == perm_pow(r,2)
assert frame(W_trivial) == (0,1,2)

results = [one_study(k) for k in range(1,5)]
assert [z['all_closed_words'] for z in results] == [6,90,1860,44730]
assert [z['zero_area_frame_counts'] for z in results] == [
    {'0':6,'1':0,'2':0}, {'0':66,'1':0,'2':0},
    {'0':876,'1':0,'2':0}, {'0':12882,'1':48,'2':48}]
assert results[3]['zero_area_nontrivial_axes'] == {'0,1':32,'0,2':32,'1,2':32}
print(json.dumps({
    'schema':'R758P5_ZERO_AREA_MINIMAL_EXACT_V1',
    'model':'rooted X6 three-axis signed-unit closed paths; candidate S3 involution transport',
    'length_classes':results,
    'minimal_length_zero_area_nonidentity':8,
    'equal_length_witness':{
        'hidden':[[a,sgn] for a,sgn in W_hidden],
        'trivial':[[a,sgn] for a,sgn in W_trivial],
        'same_A':[0,0,0], 'frame_hidden':'r^2','frame_trivial':'e'},
    'proof':'group normal-form + all balanced words of lengths 2,4,6,8 enumerated exactly',
    'status':'PASS'
},ensure_ascii=False,indent=2))
