"""R201 native BRC integration probe. Run with PYTHONPATH=src in enterprise-math.
This module imports the real pinned API; no silent simulation or fallback.
"""
from fractions import Fraction as Q
from itertools import product
from enterprise_math.brc_transport import Affine, EffectHistogram


def observer_generator(a, k, L, labels, x):
    b = a.bit_length()  # ceil(log2(a+1))
    d = k + k * (k - 1) // 2
    D = d + b * L
    if D < 1:
        raise ValueError("native Affine requires positive dimension")
    A = [[Q(i == j) for j in range(D)] for i in range(D)]
    t = [Q(0)] * D

    def constant(row, val):
        A[row] = [Q(0)] * D
        t[row] = Q(val)

    label = labels[x]
    if label >= 0:
        constant(label, 1)
        r = k
        for i in range(k):
            for j in range(i + 1, k):
                if i == label:
                    constant(r, 1)
                elif j == label:
                    constant(r, 0)
                r += 1
    for slot in range(L):
        for bit in range(b):
            r = d + slot * b + bit
            if slot == L - 1:
                constant(r, ((x + 1) >> bit) & 1)
            else:
                A[r] = [Q(0)] * D
                A[r][d + (slot + 1) * b + bit] = Q(1)
                t[r] = Q(0)
    return Affine(tuple(tuple(row) for row in A), tuple(t))


def word_action(a, k, L, labels, word):
    D = k + k * (k - 1) // 2 + a.bit_length() * L
    T = Affine.identity(D)
    for x in word:
        T = T.then(observer_generator(a, k, L, labels, x))
    return T


def observable(labels, L, word):
    source = ()
    for x in word:
        i = labels[x]
        if i >= 0:
            source = tuple(j for j in source if j != i) + (i,)
    return source, tuple(word[-L:]) if L else ()


def block_lift(physical, observer):
    n, d = physical.dim, observer.dim
    rows = []
    for row in physical.a:
        rows.append(tuple(row) + (Q(0),) * d)
    for row in observer.a:
        rows.append((Q(0),) * n + tuple(row))
    return Affine(tuple(rows), tuple(physical.b) + tuple(observer.b))


def run():
    a, k, L, labels = 3, 2, 2, (-1, 0, 1)
    seen = {}
    checks = 0
    for length in range(6):
        for w in product(range(a), repeat=length):
            act = word_action(a, k, L, labels, w)
            key = observable(labels, L, w)
            if key in seen:
                assert act == seen[key]
            else:
                seen[key] = act
            checks += 1

    B = Affine(((Q(1), Q(0)), (Q(0), Q(1))), (Q(1, 2), Q(0)))
    C = Affine(((Q(1), Q(0)), (Q(0), Q(1))), (Q(0), Q(3, 4)))
    f = word_action(a, k, L, labels, (1, 0))
    g = word_action(a, k, L, labels, (2,))
    left = block_lift(B, f)
    right = block_lift(C, g)
    assert left.then(right) == block_lift(B.then(C), f.then(g))
    assert f.then(g) == word_action(a, k, L, labels, (1, 0, 2))

    dim = left.dim
    H = EffectHistogram.from_terms(dim, ((Q(2, 3), left, 2), (Q(5, 7), right, 1)))
    G = EffectHistogram.from_terms(dim, ((Q(3, 5), right, 3),))
    expected = EffectHistogram.from_terms(dim,
        ((u * v, pa.then(pb), ca * cb)
         for u, pa, ca in H.entries for v, pb, cb in G.entries))
    assert H.then(G) == expected
    assert H.alternatives(G) == EffectHistogram.from_terms(dim, H.entries + G.entries)
    return {"status": "PASS", "backend": "NATIVE_ENTERPRISE_MATH_BRC_TRANSPORT",
            "words_checked": checks, "observer_classes": len(seen),
            "positive_rational_histogram": True}


if __name__ == "__main__":
    import json
    print(json.dumps(run(), sort_keys=True))
