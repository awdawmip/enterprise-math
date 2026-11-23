#!/usr/bin/env python3
"""R153: exact rational continuum certificate, frozen R121/R122 Port-10 observer."""
from fractions import Fraction as Q
from itertools import product

PORT = 10
CAPS = ((0, 156), (0, 312), (1, 136), (0, 196), (1, 20), (1, 176))
PIECES = ((Q(0), Q(20), (3, 1, 136)),
          (Q(20), Q(292), (1, 0, 52)),
          (Q(292), Q(528), (6, 1, 20)))
U, V = (4, -4, 1), (6, -1, 0)
A, C, K, H = (1, 0, 0), (5, -4, 1), (5, -1, 0), (9, -5, 1)


def population():
    out = {}
    for x, y, z in product(range(-PORT, PORT+1), repeat=3):
        v = (x, y, z)
        if v == (0, 0, 0):
            continue
        pos = sum(max(n, 0) for n in v)
        neg = sum(max(-n, 0) for n in v)
        if max(pos, neg) > PORT or next(n for n in v if n) < 0:
            continue
        h = (0, x+3*y+6*z, 3*x+12*y+30*z, 7*x+39*y+126*z)
        gaps = tuple(abs(h[j]-h[i]) for i, j in
                     ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)))
        out[v] = gaps
    assert len(out) == 1935
    return out


def score(gaps, d):
    return max(Q(g, a*d+b) for g, (a, b) in zip(gaps, CAPS))


def expected_set(d):
    s = {U, V}
    if d > 188:
        s.update((A, C, K, H))
    if d >= 421:
        s.remove(U)
    if d >= 448:
        s.remove(V)
    return s


def roots_of_ratio(gaps, candidate, factor, lo, hi):
    """All zeros of g/(aD+b) - factor*p/(kD+t) in (lo,hi)."""
    p, k, t = candidate
    out = set()
    for g, (a, b) in zip(gaps, CAPS):
        m = Q(g*k)-factor*p*a
        c = Q(g*t)-factor*p*b
        if m:
            r = -c/m
            if lo < r < hi:
                out.add(r)
    return out


def main():
    vectors = population()
    checked = 0
    root_counts = []
    for lo, hi, candidate in PIECES:
        critical = {lo, hi}
        for gaps in vectors.values():
            critical.update(roots_of_ratio(gaps, candidate, Q(1), lo, hi))
            critical.update(roots_of_ratio(gaps, candidate, Q(3, 2), lo, hi))
        critical = sorted(critical)
        root_counts.append(len(critical))
        probes = critical + [(u+v)/2 for u, v in zip(critical, critical[1:])]
        for d in probes:
            p, k, t = candidate
            target_eta = Q(p, k*d+t)
            values = {v: score(g, d) for v, g in vectors.items()}
            assert min(values.values()) == target_eta, ('optimizer', d)
            actual = {v for v, f in values.items() if 2*f < 3*target_eta}
            assert actual == expected_set(d), ('near-set', d, actual)
            checked += 1
    # The only possible changes of each comparison's truth value occur
    # at these exact rational zeros. The endpoint/midpoint checks therefore
    # cover every real D in each interval, including strict equalities.
    print('R153 EXACT B=20, 0<D<=528 CONTINUUM CERTIFICATE PASS')
    print('complete_integer_directions', len(vectors),
          'critical_points_by_eta_piece', root_counts,
          'exact_full_population_probes', checked)
    print('eta switch D=20,292; near-set changes D=188,421,448')


if __name__ == '__main__':
    main()
