"""R182: exact last-occurrence-order observer, affine lift, and packet checks.
Pure-Python reference; no third-party or native package dependency.
Run: python R182_last_occurrence_context_check.py
"""
from __future__ import annotations
from fractions import Fraction
from itertools import permutations, product
from math import factorial
from collections import defaultdict
import json


def states(k):
    return [()] + [p for r in range(1, k + 1) for p in permutations(range(k), r)]


def compose(a, b):
    blocked = set(b)
    return tuple(x for x in a if x not in blocked) + tuple(b)


def observe(word, k):
    result = ()
    for atom in word:
        if 0 <= atom < k:
            result = compose(result, (atom,))
    return result


def latest_in(state, subset):
    return next((x for x in reversed(state) if x in subset), None)


def affine(k):
    """Faithful regular-action simplex representation in Q^(N_k-1)."""
    S = states(k)
    at = {v: i for i, v in enumerate(S)}
    d = len(S) - 1

    def vertex(v):
        idx = at[v]
        return tuple(int(idx == j + 1) for j in range(d))

    def make(s):
        zero = vertex(compose((), s))
        columns = []
        for p in S[1:]:
            out = vertex(compose(p, s))
            columns.append(tuple(out[i] - zero[i] for i in range(d)))
        return tuple(tuple(columns[j][i] for j in range(d)) for i in range(d)), zero

    def apply(f, x):
        m, t = f
        return tuple(t[i] + sum(m[i][j] * x[j] for j in range(d)) for i in range(d))

    def then(f, g):
        m, t = f
        n, u = g
        mat = tuple(tuple(sum(n[i][l] * m[l][j] for l in range(d))
                          for j in range(d)) for i in range(d))
        return mat, apply(g, t)

    return S, vertex, make, apply, then


def packet(terms):
    d = defaultdict(int)
    for w, s, c in terms:
        assert w > 0 and c > 0
        d[(Fraction(w), tuple(s))] += c
    return tuple(sorted((Fraction(w), s, c) for (w, s), c in d.items()))


def serial(p, q):
    return packet((Fraction(w) * Fraction(v), compose(s, t), c * e)
                  for w, s, c in p for v, t, e in q)


def convert(p, k):
    return packet((w, observe(s, k), c) for w, s, c in p)


def run():
    checks = dict(state_compositions=0, subset_observers=0, separating_pairs=0,
                  band_identities=0, affine_compositions=0, packet_pairs=0,
                  complete_atom_words=0)
    stats = []
    for k in range(1, 6):
        S = states(k)
        N = sum(factorial(k) // factorial(j) for j in range(k + 1))
        assert N == len(S) == len(set(S))
        stats.append(dict(k=k, states=N, presence_states=2 ** k,
                          information_lower_bound_bits=(N - 1).bit_length(),
                          simplex_affine_dim=N - 1))
        for a in S:
            assert compose(a, a) == a
            for b in S:
                ab = compose(a, b)
                assert ab in S
                assert compose(compose(a, b), a) == compose(b, a)
                checks['state_compositions'] += 1
                checks['band_identities'] += 1
                for mask in range(1, 1 << k):
                    subset = {j for j in range(k) if mask & (1 << j)}
                    assert latest_in(ab, subset) == latest_in(a + b, subset)
                    checks['subset_observers'] += 1
        singleton_pair_queries = [(j,) for j in range(k)] + list(__import__('itertools').combinations(range(k), 2))
        for i, a in enumerate(S):
            for b in S[i + 1:]:
                assert any(latest_in(a, U) != latest_in(b, U)
                           for U in singleton_pair_queries)
                checks['separating_pairs'] += 1

    for wlen in range(0, 7):
        for w in product(range(4), repeat=wlen):
            s = observe(w, 3)
            for mask in range(1, 1 << 3):
                U = {j for j in range(3) if mask & (1 << j)}
                assert latest_in(s, U) == next((c for c in reversed(w) if c in U), None)
            checks['complete_atom_words'] += 1

    for k in (1, 2, 3):
        S, vertex, make, apply, then = affine(k)
        seq = list(product(S, S)) if k < 3 else list(product(S[:12], S[:12]))
        for a, b in seq:
            f, g = make(a), make(b)
            assert then(f, g) == make(compose(a, b))
            assert apply(f, vertex(())) == vertex(a)
            checks['affine_compositions'] += 1

    # Independent positive-rational packet benchmark, irrelevant IDs 3, 4,
    # exact multiplicities and coalescence of same (weight, effect).
    weights = [Fraction(1, 2), Fraction(2, 3), Fraction(5, 4)]
    base = [(weights[i % 3], (i % 5, (i + 1) % 5, i % 5), i % 4 + 1)
            for i in range(40)]
    for shift in range(80):
        p = base[shift % 20: shift % 20 + 8]
        q = base[(shift + 7) % 20: (shift + 7) % 20 + 7]
        left = convert(serial(p, q), 3)
        right = serial(convert(p, 3), convert(q, 3))
        assert left == right
        assert convert(p + q, 3) == packet(list(convert(p, 3)) + list(convert(q, 3)))
        checks['packet_pairs'] += 1
    return {"result":"R182_EXACT_REFERENCE_PASS",
            "frozen_scientific_input":"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
            "stats":stats,"checks":checks,
            "scope":"Exact finite examples k<=5; algebraic k>=1 theorem established by symbol proof. Reference implementation; not native enterprise_math import."}


if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, indent=2))
