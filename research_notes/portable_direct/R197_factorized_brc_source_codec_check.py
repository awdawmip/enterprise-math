#!/usr/bin/env python3
"""R197: exact factorized BRC source-order histogram and dense-lift reference.

Independent reference implementation with integer/Fraction arithmetic only.
Actual enterprise_math.brc_transport package execution is NOT claimed here.
"""
from __future__ import annotations
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations
import json, math, random


def state_count(k):
    return sum(math.perm(k, r) for r in range(k + 1))


def states(k):
    yield ()
    for r in range(1, k + 1):
        yield from permutations(range(k), r)


def validate_word(s, k):
    if (not isinstance(s, tuple) or len(s) > k or len(set(s)) != len(s)
            or any(type(x) is not int or not 0 <= x < k for x in s)):
        raise ValueError('not a partial permutation of the declared sources')


def rank(s, k):
    validate_word(s, k)
    r, available, z = len(s), list(range(k)), sum(math.perm(k, j) for j in range(len(s)))
    for i, x in enumerate(s):
        at = available.index(x)
        z += at * math.perm(k - i - 1, r - i - 1)
        available.pop(at)
    return z


def unrank(z, k):
    if type(z) is not int or not 0 <= z < state_count(k):
        raise ValueError('source state code out of range')
    r = 0
    while z >= math.perm(k, r):
        z -= math.perm(k, r)
        r += 1
    available = list(range(k))
    result = []
    for i in range(r):
        q, z = divmod(z, math.perm(k-i-1, r-i-1))
        result.append(available.pop(q))
    return tuple(result)


def star(u, v):
    seen = set(v)
    return tuple(x for x in u if x not in seen) + v


def code_then(a, b, k):
    return rank(star(unrank(a, k), unrank(b, k)), k)


@dataclass(frozen=True, order=True)
class Affine:
    a: tuple
    b: tuple

    @property
    def dim(self):
        return len(self.b)

    @classmethod
    def eye(cls, n):
        return cls(tuple(tuple(F(i == j) for j in range(n)) for i in range(n)), (F(0),) * n)

    def then(self, later):
        n = self.dim
        assert later.dim == n
        m = tuple(tuple(sum((later.a[i][h] * self.a[h][j] for h in range(n)), F(0))
                  for j in range(n)) for i in range(n))
        v = tuple(sum((later.a[i][h]*self.b[h] for h in range(n)), F(0)) + later.b[i]
                  for i in range(n))
        return Affine(m, v)


def features(k):
    return tuple((i,) for i in range(k)) + tuple((i, j) for i in range(k) for j in range(i+1, k))


def reset(word, k):
    fs = features(k)
    status = [None] * len(fs)
    for symbol in word:
        for j, subset in enumerate(fs):
            if symbol in subset:
                status[j] = 0 if len(subset) == 1 or symbol == subset[0] else 1
    a = tuple(tuple(F(i == j and status[i] is None) for j in range(len(fs)))
              for i in range(len(fs)))
    b = tuple(F(x) if x is not None else F(0) for x in status)
    return Affine(a, b)


def direct_sum(a, b):
    n, d = a.dim, b.dim
    return Affine(tuple(row + (F(0),) * d for row in a.a) +
                  tuple((F(0),) * n + row for row in b.a), a.b + b.b)


def dense_lift(packet, k):
    out = defaultdict(int)
    for (weight, action, code), multiplicity in packet.items():
        out[(weight, direct_sum(action, reset(unrank(code, k), k)))] += multiplicity
    return dict(out)


def canonical(terms, k, n):
    out = defaultdict(int)
    for weight, a, count, word in terms:
        if type(count) is not int or count < 0 or F(weight) <= 0 or a.dim != n:
            raise ValueError('nonpositive weight, invalid multiplicity, or physical dimension')
        code = rank(tuple(word), k)
        if count:
            out[(F(weight), a, code)] += count
    return dict(out)


def alternatives(h, j):
    out = defaultdict(int, h)
    for key, count in j.items():
        out[key] += count
    return dict(out)


def product(h, j, k):
    out = defaultdict(int)
    for (w, a, s), c in h.items():
        for (v, b, t), d in j.items():
            out[(w*v, a.then(b), code_then(s, t, k))] += c*d
    return dict(out)


def dense_product(h, j):
    out = defaultdict(int)
    for (w, a), c in h.items():
        for (v, b), d in j.items():
            out[(w*v, a.then(b))] += c*d
    return dict(out)


def dense_alternatives(h, j):
    out = defaultdict(int, h)
    for key, count in j.items():
        out[key] += count
    return dict(out)


def run():
    result = {'schema': 'EM_R197_FACTORIZED_SOURCE_CODEC_EXACT_V1',
              'backend': 'independent_fraction_reference', 'status': 'PASS',
              'frozen_scientific_input': '43ec6098b1330ae86d0a7863be336c5d97f6ef34',
              'arithmetic': 'integer and Fraction, no floating point',
              'state_roundtrips': 0, 'all_ordered_compositions': 0,
              'dense_packet_pairs': 0, 'dense_packet_triplets': 0,
              'random_word_updates': 0, 'resource_rows': []}
    for k in range(1, 7):
        S = list(states(k))
        assert len(S) == state_count(k)
        assert {rank(s, k) for s in S} == set(range(state_count(k)))
        for s in S:
            assert unrank(rank(s, k), k) == s
        result['state_roundtrips'] += len(S)
        if k <= 5:
            for u in S:
                au = rank(u, k)
                for v in S:
                    assert unrank(code_then(au, rank(v, k), k), k) == star(u, v)
                    result['all_ordered_compositions'] += 1
        d = k*(k+1)//2
        result['resource_rows'].append({'k': k, 'states': state_count(k),
            'code_bits': (state_count(k)-1).bit_length(),
            'reset_dimension': d, 'dense_added_rational_slots_at_n2': 4*d + d*d+d})
    for k in range(1, 5):
        for n in range(1, 3):
            I = Affine.eye(n)
            shift = Affine(I.a, tuple(F(i+1, 2) for i in range(n)))
            scale = Affine(tuple(tuple(F(2 if i == j else 0) for j in range(n))
                                 for i in range(n)), tuple(F(-i, 3) for i in range(n)))
            u = tuple(range(min(k, 3)))
            v = tuple(reversed(range(min(k, 2))))
            H = canonical([(F(1,2), I, 2, u), (F(2,3), shift, 3, (0,))], k, n)
            J = canonical([(F(3,2), scale, 1, v), (F(1,2), I, 2, ())], k, n)
            K = canonical([(F(5,3), shift, 2, v), (F(1), scale, 1, u)], k, n)
            assert dense_lift(alternatives(H, J), k) == dense_alternatives(dense_lift(H, k), dense_lift(J, k))
            assert dense_lift(product(H, J, k), k) == dense_product(dense_lift(H, k), dense_lift(J, k))
            assert product(product(H,J,k),K,k) == product(H, product(J,K,k),k)
            assert dense_lift(product(product(H,J,k),K,k),k) == dense_product(dense_product(dense_lift(H,k),dense_lift(J,k)),dense_lift(K,k))
            result['dense_packet_pairs'] += 1
            result['dense_packet_triplets'] += 1
    rng = random.Random(197)
    for k in range(1, 7):
        for _ in range(50):
            word = tuple(rng.randrange(k) for i in range(100))
            state = ()
            code = 0
            for x in word:
                state = star(state, (x,))
                code = code_then(code, rank((x,), k), k)
                assert unrank(code, k) == state
                result['random_word_updates'] += 1
    for k in range(1, 7):
        for bad in [-1, state_count(k), True]:
            try:
                unrank(bad, k)
                raise AssertionError('bad source code accepted')
            except ValueError:
                pass
    return result


if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, indent=2))
