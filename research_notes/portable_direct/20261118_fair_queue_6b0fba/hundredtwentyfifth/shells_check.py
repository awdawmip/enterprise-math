"""Exact checks for hyperplane seeds in the signed coordinate unit-step graph."""
import heapq
import json
from collections import Counter
from itertools import combinations, product
from math import comb, gcd


def bound_data(a):
    steps = [s * g for g in a for s in (1, -1)]
    A = max(steps)
    assert gcd(*a) == 1
    ds = sorted({A, *(A - g for g in steps)} - {0})
    labels = [None] * A
    labels[0] = (0, 0)
    queue = [(0, 0, 0)]
    while queue:
        dist, length, i = heapq.heappop(queue)
        if labels[i] != (dist, length):
            continue
        for d in ds:
            j = (i + d) % A
            cand = (dist + d, length + 1)
            if labels[j] is None or cand < labels[j]:
                labels[j] = cand
                heapq.heappush(queue, (*cand, j))
    delta, ell = map(list, zip(*(labels[-j % A] for j in range(A))))
    first = [A * m - d for d, m in zip(delta, ell)]
    H = max(0, 1 + max(first) - A)
    return steps, A, delta, ell, first, H


def bfs(steps, limit):
    hist = {0: (0, 1)}
    shells = [[0]]
    for r in range(1, limit + 1):
        front = Counter()
        for n in shells[-1]:
            for step in steps:
                y = n + step
                if y not in hist:
                    front[y] += hist[n][1]
        shells.append(sorted(front))
        hist.update((n, (r, ways)) for n, ways in front.items())
    return hist, shells


def word_polys(steps, delta):
    A = max(steps)
    pos = Counter(A - g for g in steps if g != A)
    highest = max(delta)
    monomials = {0: 1}
    polys = [[] for _ in delta]
    while monomials:
        for coeffs, d in zip(polys, delta):
            coeffs.append(monomials.get(d, 0))
        nxt = Counter()
        for x, coeff in monomials.items():
            for y, mult in pos.items():
                if x + y <= highest:
                    nxt[x + y] += coeff * mult
        monomials = nxt
    for row in polys:
        while row and not row[-1]:
            row.pop()
    return polys


def front_report(a):
    steps, A, delta, ell, first, H = bound_data(a)
    # Grow until every finite exceptional height is explicitly known.
    r = 4 * A + 3
    dist, levels = bfs(steps, r)
    finite = range(H + A)
    assert all(n in dist for n in finite)
    bound = max(1 + max(dist[n][0] for n in finite),
                (H + A + max(delta) + A - 1) // A)
    if r < bound + 3:
        dist, levels = bfs(steps, bound + 3)
    jumps = {g: [(g + delta[(j + g) % A] - delta[j]) // A
                 for j in range(A)] for g in sorted(set(steps))}
    named = {}
    for g in jumps:
        assert sum(jumps[g]) == g
        c = Counter(jumps[g])
        named[g] = (c[1] + c[-1], 2 * c[0], c[1] + c[-1])
    polys = word_polys(steps, delta)
    u = steps.count(A)
    assert all(next(m for m, q in enumerate(row) if q) == l
               and len(row) <= A for row, l in zip(polys, ell))
    genus = (2 * sum(delta) - A*(A-1)) // (2*A)
    ball_size = 0
    # A cost-A deficit means a wait only in this ball test, never a named edge.
    max_deficit = 2 * A * bound
    positive = {A, *(A-g for g in steps)} - {0}
    coin = [0] + [max_deficit+1] * max_deficit
    for c in range(1, max_deficit+1):
        coin[c] = min((1+coin[c-w] for w in positive if w <= c),
                      default=max_deficit+1)
    early_edges = []
    unstable = []
    for m in range(0, 2 * A * A + 1):
        actual = dist[m][0]
        r0 = (m + delta[m % A]) // A
        assert (actual == r0) == (m >= first[m % A])
        if actual != r0:
            unstable.append(m)
    assert 1 + max(unstable, default=-1) == H
    pop_exceptions, dir_exceptions, sample = [], [], {}
    for r, shell in enumerate(levels[:-1]):
        ball_size += len(shell)
        if len(shell) != 2 * A:
            pop_exceptions.append(r)
        edge = {g: tuple(sum(dist[n+g][0] - r == s for n in shell)
                         for s in (-1, 0, 1)) for g in jumps}
        assert all(edge[g] == edge[-g] for g in jumps)
        if r <= bound:
            for n in range(-r*A, r*A+1):
                assert (coin[r*A-n] <= r) == (dist[n][0] <= r)
        if r < bound:
            early_edges.append({"distance":r, "size":len(shell),
                                "in_flat_out_by_abs_height":{str(g):edge[g]
                                 for g in sorted(set(map(abs, steps)))}})
        if edge != named:
            dir_exceptions.append(r)
        if r in {0, 1, 2, 3, 4, 5, bound, bound+1}:
            sample[r] = [len(shell), sum(dist[n][1] for n in shell),
                         list(edge[a[0]])]
        if r >= bound:
            assert edge == named
            assert ball_size == 2 * A * r + 1 - 2 * genus
            pos_n = [A * r - d for d in delta]
            assert set(shell) == set(pos_n) | {-v for v in pos_n}
            for n, row in zip(pos_n, polys):
                expected = sum(q * comb(r, i) * u ** (r-i)
                               for i, q in enumerate(row) if i <= r)
                assert dist[n][1] == expected == dist[-n][1]
                assert all(dist[n+g][0] - r == jumps[g][n % A] for g in jumps)
    return dict(axes=a, delta=delta, minimal_length=ell, thresholds=first,
                first_uniform_height=H, exceptional_nonnegative_heights=unstable,
                all_formulae_safe_radius=bound,
                exact_first_persistent_cardinality_radius=1+max(pop_exceptions, default=-1),
                exact_first_persistent_named_edge_radius=1+max(dir_exceptions, default=-1),
                positive_jump={str(g): jumps[g] for g in sorted(set(a))},
                eventual_named_edges_in_flat_out=[list(named[g]) for g in steps],
                all_early_named_edge_rows=early_edges,
                semigroup_genus=genus, word_polynomial_degree=max(map(len, polys))-1,
                word_exponential_base=u, word_polynomials_in_binomial_basis=polys,
                radius_sample_size_words_first_plus_axis_in_flat_out=sample)


def native_words(a):
    # Displacements are literal six-component vectors; no quotient step graph used.
    names = tuple((i, s) for i in range(6) for s in (-1, 1))
    steps = [s * a[i] for i, s in names]
    dist, levels = bfs(steps, 4)
    accum = {}
    for r in range(5):
        count = Counter()
        for word in product(names, repeat=r):
            dx = [0] * 6
            for i, s in word:
                dx[i] += s
            count[sum(x * y for x, y in zip(a, dx))] += 1
        for n, value in count.items():
            accum.setdefault(n, (r, value))
        assert all(accum[n] == dist[n] for n in levels[r])
    return {"axes": a, "words_by_length": [12**j for j in range(5)],
            "numbers_of_first_height_endpoints": [len(f) for f in levels]}


def check_family():
    total = 0
    max_H = {}
    all_equality = {}
    for A in range(1, 11):
        hs = []
        extremals = []
        for count in range(min(A-1, 5)+1):
            for small in combinations(range(1, A), count):
                a = small + (A,)
                if gcd(*a) != 1:
                    continue
                steps, _, d, _, first, H = bound_data(a)
                radius = 3 * A + 2
                dist, _ = bfs(set(steps), radius)
                for n in range(A*A+1):
                    assert (dist[n][0] == (n + d[n % A]) // A) == (n >= first[n % A])
                deg = max(map(len, word_polys(steps, d))) - 1
                if A >= 2:
                    sharp_degree = A-1 in a or (A % 2 == 1 and A-2 in a and all(v % 2 for v in a))
                    assert (deg == A-1) == sharp_degree
                assert H <= (A-1) * (A-2)
                if A >= 3:
                    assert (H == (A-1)*(A-2)) == (a == (A-1, A))
                if H == (A-1)*(A-2):
                    extremals.append(a)
                hs.append(H)
                total += 1
        max_H[A] = max(hs)
        all_equality[A] = extremals
    for A in range(2, 65):
        for a in ((A, A-1, 0, 0, 0, 0), (-A, A, 1-A, 0, 0, 0)):
            _, _, d, ell, _, H = bound_data(a)
            assert d == ell == [(-j) % A for j in range(A)]
            assert H == (A-1)*(A-2)
    return dict(six_axis_distinct_magnitude_sets=total,
                highest_height_threshold_by_A=max_H, exact_extremizers=all_equality,
                signed_duplicate_extremal_examples_through_A=64)


def main():
    examples = [(3,5,0,0,0,0), (5,12,0,0,0,0), (7,6,0,0,0,0),
                (7,-7,6,0,0,0), (1,-2,3,-4,5,-7), (1,1,1,1,1,1)]
    result = {"coordinate_order":"axis-major, + then - in named edge arrays",
              "edges":"[inward,flat,outward] per translation orbit of the starting vertex",
              "cost":"standard library integer checks; no physical runtime extrapolation",
              "finite_magnitude_test":check_family(),
              "coordinate_words":[native_words(a) for a in examples],
              "examples":[front_report(a) for a in examples]}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
