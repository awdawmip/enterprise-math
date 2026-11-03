#!/usr/bin/env python3
"""PREFIX-462: exact positive-path BRC occupation/endpoint fiber certificate.
Combinatorial verification only, using Python standard library exact integers.
Frozen science model: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
"""
from collections import Counter
from math import comb, factorial, prod

WEIGHTS = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)  # one-sided +e1 and 5 signed pairs


def compositions(total, count):
    if count == 1:
        yield (total,)
        return
    for a in range(total + 1):
        for rest in compositions(total - a, count - 1):
            yield (a,) + rest


def endpoint(occupancy):
    return (occupancy[0],) + tuple(occupancy[1 + 2 * i] - occupancy[2 + 2 * i] for i in range(5))


def canonical_form(occupancy):
    s, *y = endpoint(occupancy)
    pair_counts = [min(occupancy[1 + 2 * i], occupancy[2 + 2 * i]) for i in range(5)]
    p = sum(pair_counts)
    out = [s]
    for i, yi in enumerate(y):
        h = p if i == 0 else 0
        out.extend((max(yi, 0) + h, max(-yi, 0) + h))
    return tuple(out)


def support_closed(m):
    return sum(comb(4, j) * comb(m - j + 6, 6) for j in range(min(4, m) + 1))


def multinomial_weight(counts):
    m = sum(counts)
    integer = factorial(m) // prod(factorial(c) for c in counts)
    return integer * prod(w ** c for w, c in zip(WEIGHTS, counts))


def dp_weighted(m):
    # direct ordered-path propagation; independent of occupation multinomial method
    dp = {(0, 0, 0, 0, 0, 0): 1}
    steps = [(1, 0, 0, 0, 0, 0)]
    for i in range(1, 6):
        p, n = [0] * 6, [0] * 6
        p[i], n[i] = 1, -1
        steps.extend((tuple(p), tuple(n)))
    for _ in range(m):
        ndp = Counter()
        for x, v in dp.items():
            for st, w in zip(steps, WEIGHTS):
                ndp[tuple(a+b for a, b in zip(x, st))] += v*w
        dp = ndp
    return dict(dp)


def check():
    print('PREFIX462_TORIC_CERTIFICATE_V1')
    for m in range(0, 9):
        occ_count = 0
        support = Counter()
        fiber_sets = {}
        for c in compositions(m, 11):
            occ_count += 1
            e = endpoint(c)
            support[e] += 1
            cf = canonical_form(c)
            assert endpoint(cf) == e
            assert sum(cf) == m
            assert all(min(cf[1+2*i], cf[2+2*i]) == 0 for i in range(1, 5))
            if e in fiber_sets:
                assert fiber_sets[e] == cf
            else:
                fiber_sets[e] = cf
        assert occ_count == comb(m + 10, 10)
        assert len(support) == support_closed(m)
        assert sum(support.values()) == occ_count
        for (s, *ys), k in support.items():
            p = (m - s - sum(abs(y) for y in ys)) // 2
            assert (m-s-sum(abs(y) for y in ys)) % 2 == 0
            assert k == comb(p + 4, 4)
        print(f'm={m} occupation_vectors={occ_count} distinct_endpoints={len(support)} fiber_formula=PASS canonical_exchange=PASS')

        if m <= 6:
            # independently verify occupation multinomials against ordered weighted BRC DP
            agg = Counter()
            for c in compositions(m, 11):
                agg[endpoint(c)] += multinomial_weight(c)
            dp = dp_weighted(m)
            assert dict(agg) == dp
            assert sum(agg.values()) == sum(WEIGHTS) ** m
            print(f'  weighted_path_mass=PASS total_mass={sum(WEIGHTS)**m} support={len(dp)}')

    # The exact two-letter witness: two opposite pairs, same native endpoint.
    w2 = 2 * WEIGHTS[1] * WEIGHTS[2]
    w3 = 2 * WEIGHTS[3] * WEIGHTS[4]
    assert w2 == 30 and w3 == 154 and w2 != w3
    print(f'm=2 two_ordered_word_pair_masses pair_e2={w2} pair_e3={w3} endpoint=(0,0,0,0,0,0)')
    print('ALL_CHECKS_PASS')


if __name__ == '__main__':
    check()
