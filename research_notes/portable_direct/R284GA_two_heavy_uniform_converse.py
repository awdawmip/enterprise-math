#!/usr/bin/env python3
"""R284GA: q-independent two-heavy stable-cut criterion, exact integer census.

The universal-q result uses a written cut-inequality proof; these finite
offset enumerations and finite-q regressions check its implementation.
"""
from itertools import combinations

PAIRS = tuple(combinations(range(4), 2))
ADJACENT = {(0, 1), (0, 3), (1, 2), (2, 3)}
BITS = {p: (0, p & 1, (p >> 1) & 1, (p >> 2) & 1)
        for p in range(1, 8)}
LAST = {}
for p in range(1, 8):
    for i in range(4):
        LAST[p, i] = next(e for e in ((i - 1 - t) % 4 for t in range(4))
                          if BITS[p][e] != BITS[p][(e + 1) % 4])

DIST, CUTS = {}, {}
for i, j in PAIRS:
    edges = [(p, LAST[p, i], 4 + LAST[p, j])
             for p in range(1, 8) if BITS[p][i] != BITS[p][j]]
    DIST[i, j] = tuple(p for p, _, _ in edges)
    minimal_vertices = {}
    for vertices in range(1, 256):
        mask = tuple(p for p, source, target in edges
                     if vertices & (1 << source) and vertices & (1 << target))
        if mask:
            minimal_vertices[mask] = min(
                minimal_vertices.get(mask, 9), vertices.bit_count())
    CUTS[i, j] = tuple(minimal_vertices.items())
    assert all(2 <= size <= 4 for _, size in CUTS[i, j])


def compositions(total, count):
    if count == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for tail in compositions(total - first, count - 1):
                yield (first,) + tail


def cases(k):
    """Offsets x_p=2q*1_{p in G}+z_p; z>=0; sum(z)=k; z_G>=2."""
    for G in combinations((3, 5, 6), 2):
        for offset in compositions(k - 4, 7):
            z = list(offset)
            z[G[0] - 1] += 2
            z[G[1] - 1] += 2
            yield G, tuple(z)


def symbolic(G, z):
    """q-independent necessary distance and exact stable-cut criterion (q>=5)."""
    for pair in PAIRS:
        changed = DIST[pair]
        h = len(set(changed) & set(G))
        assert h >= 1
        c = 5 if pair in ADJACENT else 3
        if h == 1 and sum(z[p - 1] for p in changed) < c:
            return False
        if not any(
            (len(set(mask) & set(G)) == 1 and vertices == 2
             and sum(z[p - 1] for p in mask) >= 3)
            or (len(set(mask) & set(G)) == 2)
            for mask, vertices in CUTS[pair]
        ):
            return False
    return True


def direct(G, z, q):
    x = tuple(z[p - 1] + 2 * q * (p in G) for p in range(1, 8))
    if any(sum(x[p - 1] for p in DIST[pair]) <
           2 * q + (5 if pair in ADJACENT else 3)
           for pair in PAIRS):
        return False
    return all(any(sum(x[p - 1] for p in mask) >= q * vertices + 3
                   for mask, vertices in CUTS[pair]) for pair in PAIRS)


def main():
    for k, expected, face, group_counts in (
        (8, 7, 7, {(3, 5): 3, (3, 6): 1, (5, 6): 3}),
        (9, 66, 18, {(3, 5): 28, (3, 6): 10, (5, 6): 28}),
    ):
        all_cases = tuple(cases(k))
        assert len(all_cases) == (630 if k == 8 else 1386)
        selected = {item for item in all_cases if symbolic(*item)}
        assert len(selected) == expected, (k, len(selected))
        assert sum(not any(z[p - 1] for p in (1, 2, 4, 7))
                   for G, z in selected) == face
        assert {g: sum(G == g for G, z in selected)
                for g in combinations((3, 5, 6), 2)} == group_counts
        for q in (5, 6, 7, 11, 64, 1000):
            assert all(symbolic(G, z) == direct(G, z, q)
                       for G, z in all_cases), (k, q)
        print(f'k={k} all_offsets={len(all_cases)} stable={expected} '
              f'three_pattern={face} mixed={expected-face} '
              f'group_counts={group_counts}')
    print('PASS: q-independent two-heavy converse for all q>=5; '
          '2016 exact offsets and 12096 direct-q regression checks')


if __name__ == '__main__':
    main()
