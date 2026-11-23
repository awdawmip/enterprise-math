#!/usr/bin/env python3
"""R284GC: all-q first-edge obstruction, exact integer Hall/BFS certificate.

No scipy or LP solver. Covers all seven-pattern stable families by R284GA
and proves every non-F0..F10 family has a q-uniform forbidden-prefix cut.
"""
from collections import deque
from itertools import combinations, product

PAIRS = tuple(combinations(range(4), 2))
ADJ = {(0, 1), (0, 3), (1, 2), (2, 3)}
BITS = {p: (0, p & 1, (p >> 1) & 1, (p >> 2) & 1)
        for p in range(1, 8)}
LAST = {(p, i): next(e for e in ((i - 1 - t) % 4 for t in range(4))
                      if BITS[p][e] != BITS[p][(e + 1) % 4])
        for p in range(1, 8) for i in range(4)}
DIST, CUTS = {}, {}
for i, j in PAIRS:
    edges = [(p, LAST[p, i], 4 + LAST[p, j]) for p in range(1, 8)
             if BITS[p][i] != BITS[p][j]]
    DIST[i, j] = tuple(p for p, _, _ in edges)
    masks = {}
    for v in range(1, 256):
        m = tuple(p for p, a, b in edges
                  if (v >> a) & 1 and (v >> b) & 1)
        if m:
            masks[m] = min(masks.get(m, 9), v.bit_count())
    CUTS[i, j] = tuple(masks.items())


def compositions(n, count):
    if count == 1:
        yield (n,)
    else:
        for j in range(n + 1):
            for tail in compositions(n - j, count - 1):
                yield (j,) + tail


def stable_templates(k):
    """R284GA's q-independent two-heavy predicate, complete after R284GB."""
    ans = []
    for G in combinations((3, 5, 6), 2):
        for w in compositions(k - 4, 7):
            z = list(w)
            z[G[0] - 1] += 2
            z[G[1] - 1] += 2
            if any(sum(z[p - 1] for p in DIST[pair]) <
                   (5 if pair in ADJ else 3)
                   for pair in PAIRS if len(set(DIST[pair]) & set(G)) == 1):
                continue
            if any(not any(
                    len(set(mask) & set(G)) == 2 or
                    (len(set(mask) & set(G)) == 1 and vertices == 2 and
                     sum(z[p - 1] for p in mask) >= 3)
                    for mask, vertices in CUTS[pair]) for pair in PAIRS):
                continue
            ans.append((G, tuple(z)))
    return ans


def hall_uniform(G, z, q0, source, target, other, successful):
    """Prove distance(prefix, stable-other)<=2 for every integer q>=q0.

    In the exact R284FT flow network, each unit of mismatch has an eligible
    subset of the eight last-update omission-budget vertices. Weighted Hall:
    deficiency=max_U(sum_{eligibility subset U} demand-q*|U|,0).
    With x_p(q)=2q*[p in G]+z_p, every subset expression is affine in q.
    Hence checking its slope<=0 and its value at q0<=2 proves all-q.
    """
    demands = []
    for p in range(1, 8):
        a = 2 * (p in G)
        b = z[p - 1] - successful.get(p, 0)
        if BITS[p][source] != BITS[p][other]:
            assert a * q0 + b >= 0
            e = (1 << LAST[p, source]) | (1 << (4 + LAST[p, other]))
            demands.append((e, a, b))
        fixed = successful.get(p, 0)
        if fixed and BITS[p][target] != BITS[p][other]:
            e = 1 << (4 + LAST[p, other])
            demands.append((e, 0, fixed))
    for U in range(256):
        slope = -U.bit_count()
        intercept = 0
        for eligible, a, b in demands:
            if U & eligible == eligible:
                slope += a
                intercept += b
        if slope > 0 or q0 * slope + intercept > 2:
            return False
    return True


def uniform_bad_prefix(G, z, q0, types, attempts):
    source, target = 0, 1
    for misses in product(*(range(min(q0, t) + 1) for t in attempts)):
        if sum(misses) > q0:
            continue
        succ = {p: a - m for p, a, m in zip(types, attempts, misses)}
        for third in (2, 3):
            if hall_uniform(G, z, q0, source, target, third, succ):
                return ('THIRD', third, misses)
        if sum(succ.values()) <= 2 and hall_uniform(
                G, z, q0, source, target, target, succ):
            return ('ROLLBACK', target, misses)
    return None


def uniform_first_edge_excluded(G, z, q0=5):
    """Explore an over-approximation of uniformly safe count prefixes.

    At q>q0, a monotone update path can exit the q0 count box only by
    reaching an old maximum in a growing type. Prohibit such a reachable
    boundary; non-growing types have unchanged maxima. Therefore this is
    a finite all-q obstruction, not extrapolation of a finite q sample.
    """
    x0 = {p: 2 * q0 * (p in G) + z[p - 1] for p in range(1, 8)}
    types = tuple(p for p in range(1, 8)
                  if x0[p] and BITS[p][0] != BITS[p][1])
    finish = tuple(x0[p] for p in types)
    start = (0,) * len(types)
    frontier = deque([start])
    safe_reachable = {start}
    bad_witnesses = {}
    while frontier:
        state = frontier.popleft()
        if state == finish or any(state[i] == finish[i] and p in G
                                  for i, p in enumerate(types)):
            return False, len(safe_reachable), bad_witnesses
        for i, p in enumerate(types):
            if state[i] == finish[i]:
                continue
            nxt = state[:i] + (state[i] + 1,) + state[i + 1:]
            if nxt in safe_reachable or nxt in bad_witnesses:
                continue
            witness = uniform_bad_prefix(G, z, q0, types, nxt)
            if witness is not None:
                bad_witnesses[nxt] = witness
            else:
                safe_reachable.add(nxt)
                frontier.append(nxt)
    return True, len(safe_reachable), bad_witnesses


def frontier_families(q):
    A, B = 2 * q + 5, 2 * q + 3
    return {
        (0, 0, 0, 0, A, B, 0),
        (0, 0, 0, 0, A, B, 1),
        (0, 0, 0, 0, A, B + 1, 0),
        (0, 0, 0, 0, A + 1, B, 0),
        (0, 0, 0, 1, A - 1, B, 1),
        (0, 0, 0, 1, A, B, 0),
        (0, 0, 1, 0, A - 1, B, 1),
        (0, 0, 1, 0, A, B, 0),
        (0, 1, 0, 0, A - 1, B, 1),
        (0, 1, 0, 0, A, B, 0),
        (1, 0, 0, 0, A, B, 0),
    }


def main():
    leftovers = set()
    for k, expected, excluded_expected in ((8, 7, 6), (9, 66, 56)):
        families = stable_templates(k)
        assert len(families) == expected
        excluded = 0
        witnesses, max_safe_nodes = 0, 0
        for G, z in families:
            x0 = tuple(10 * (p in G) + z[p - 1] for p in range(1, 8))
            blocked, n, bad = uniform_first_edge_excluded(G, z)
            if blocked:
                excluded += 1
                witnesses += len(bad)
                max_safe_nodes = max(max_safe_nodes, n)
            else:
                leftovers.add(x0)
        assert excluded == excluded_expected, (k, excluded)
        print('k=%d stable=%d uniformly_excluded=%d residual=%d '
              'witness_nodes=%d max_safe_nodes=%d' %
              (k, expected, excluded, expected - excluded,
               witnesses, max_safe_nodes))
    assert leftovers == frontier_families(5), (
        'unexpected survivors', leftovers ^ frontier_families(5))
    print('PASS: for every integer q>=5 first-edge survivors are contained '
          'in exactly R284FW F0-F10 (11 parameterized families)')
    print('With R284GB, R284GA, R284FW, R284FP and R284FE: '
          'n_min(q,1)=4q+10 for all integers q>=5')
    print('Existing R284FS/FT/FU cover q=2,3,4 separately')


if __name__ == '__main__':
    main()
