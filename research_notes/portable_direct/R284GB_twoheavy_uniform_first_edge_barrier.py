#!/usr/bin/env python3
"""R284GB: uniform first-edge residual obstruction for the two-heavy sector.

Proves a finite q=5 barrier with the R284FT exact integral min-cut dual.
The all-q step is a mathematical omission-slot matching lift in the note.
No external dependencies.
"""
from itertools import combinations, product
from collections import defaultdict

PAIRS = tuple(combinations(range(4), 2))
ADJ = {(0, 1), (0, 3), (1, 2), (2, 3)}
BITS = {p: (0, p & 1, (p >> 1) & 1, (p >> 2) & 1) for p in range(1, 8)}
LAST = {(p, i): next(e for e in ((i - 1 - t) % 4 for t in range(4))
                      if BITS[p][e] != BITS[p][(e + 1) % 4])
        for p in range(1, 8) for i in range(4)}
DIST, CUT = {}, {}
for i, j in PAIRS:
    edges = [(p, LAST[p, i], 4 + LAST[p, j])
             for p in range(1, 8) if BITS[p][i] != BITS[p][j]]
    DIST[i, j] = tuple(p for p, _, _ in edges)
    masks = {}
    for U in range(1, 256):
        mask = tuple(p for p, a, b in edges if (U >> a) & 1 and (U >> b) & 1)
        if mask:
            masks[mask] = min(U.bit_count(), masks.get(mask, 9))
    CUT[i, j] = tuple(masks.items())


def compositions(total, n):
    if n == 1:
        yield (total,)
    else:
        for a in range(total + 1):
            for rem in compositions(total - a, n - 1):
                yield (a,) + rem


def stable_twoheavy(G, z):
    for pair in PAIRS:
        h = len(set(DIST[pair]) & set(G))
        if h == 1 and sum(z[p - 1] for p in DIST[pair]) < (5 if pair in ADJ else 3):
            return False
        if not any((len(set(mask) & set(G)) == 2) or
                   (len(set(mask) & set(G)) == 1 and size == 2 and
                    sum(z[p - 1] for p in mask) >= 3)
                   for mask, size in CUT[pair]):
            return False
    return True


def stable_direct(x, q):
    for pair in PAIRS:
        if sum(x[p - 1] for p in DIST[pair]) < 2*q + (5 if pair in ADJ else 3):
            return False
        if not any(sum(x[p - 1] for p in mask) >= q*size + 3
                   for mask, size in CUT[pair]):
            return False
    return True


def liftable(G, i, j):
    """Match two differing new coordinates of each heavy type to omitted-write slots.

    Each of the eight slots (four last-write groups for each comparison history)
    has additional omission capacity exactly one on passing q to q+1.
    """
    choices = [(LAST[p, i], 4 + LAST[p, j])
               for p in G if BITS[p][i] != BITS[p][j] for _ in range(2)]
    def matching(t, used):
        if t == len(choices):
            return True
        return any(not (used >> b) & 1 and matching(t + 1, used | (1 << b))
                   for b in choices[t])
    return matching(0, 0)


def prefix_distance(x, q, i, target, j, success):
    """Exactly D-maxflow, by 256-subset min-cut (R284FT).

    Free bits carry two omission-source edges; successfully written bits that
    differ from stable j carry only the right-history omission-source edge.
    """
    needs = []
    for p in range(1, 8):
        s = success.get(p, 0)
        free = x[p - 1] - s
        if free and BITS[p][i] != BITS[p][j]:
            needs.append(((1 << LAST[p, i]) | (1 << (4 + LAST[p, j])), free))
        if s and BITS[p][target] != BITS[p][j]:
            needs.append((1 << (4 + LAST[p, j]), s))
    return max(sum(v for bits, v in needs if bits & U == bits) - q*U.bit_count()
               for U in range(256))


def first_witness(x, q, G, attempted, types):
    """An already-defined third phase, or premature next phase at <=2 writes."""
    permitted = [j for j in (1, 2, 3) if liftable(G, 0, j)]
    for missed in product(*(range(min(q, t) + 1) for t in attempted)):
        if sum(missed) > q:
            continue
        success = {p: t - m for p, t, m in zip(types, attempted, missed)}
        for j in permitted:
            if j == 1 and sum(success.values()) > 2:
                continue
            if prefix_distance(x, q, 0, 1, j, success) <= 2:
                return (j, missed)
    return None


def capped_first_edge(x, q, G):
    types = tuple(p for p in range(1, 8) if x[p - 1] and BITS[p][0] != BITS[p][1])
    cap = tuple(min(x[p - 1], 8) if p in G else x[p - 1] for p in types)
    heavy_updated = tuple(types.index(p) for p in G if p in types)
    assert heavy_updated
    start = (0,) * len(types)
    safe, frontier, bad = {start}, [start], {}
    while frontier:
        node = frontier.pop()
        for h in range(len(types)):
            if node[h] >= cap[h]:
                continue
            nxt = node[:h] + (node[h] + 1,) + node[h + 1:]
            if nxt in safe or nxt in bad:
                continue
            witness = first_witness(x, q, G, nxt, types)
            if witness is not None:
                bad[nxt] = witness
            else:
                safe.add(nxt)
                frontier.append(nxt)
    escape = any(any(s[h] == cap[h] for h in heavy_updated) for s in safe)
    return escape, len(safe), len(bad), types, cap


def all_families(q):
    A, B = 2*q + 5, 2*q + 3
    return [(0,0,0,0,A,B,0), (0,0,0,0,A,B,1),
            (0,0,0,0,A,B+1,0), (0,0,0,0,A+1,B,0),
            (0,0,0,1,A-1,B,1), (0,0,0,1,A,B,0),
            (0,0,1,0,A-1,B,1), (0,0,1,0,A,B,0),
            (0,0,1,0,A-1,B,1), (0,0,1,0,A,B,0),
            (1,0,0,0,A,B,0)]


def main():
    counts = defaultdict(int)
    stable_cases = []
    first_edge_possible = []
    total_safe = total_bad = 0
    for k in (8, 9):
        for G in combinations((3, 5, 6), 2):
            for w in compositions(k-4, 7):
                z = list(w)
                for p in G: z[p-1] += 2
                if not stable_twoheavy(G, z):
                    continue
                counts[(k, G)] += 1
                x = tuple(z[p-1] + 10*(p in G) for p in range(1, 8))
                assert stable_direct(x, 5)
                stable_cases.append((k, G, x))
                escape, s, b, types, cap = capped_first_edge(x, 5, G)
                total_safe += s; total_bad += b
                if escape:
                    first_edge_possible.append((k, G, x))
        print(f'width=4q+{k}: stable={sum(counts[k,G] for G in combinations((3,5,6),2))} '
              f'capped_edge_survivors={sum(item[0] == k for item in first_edge_possible)}')
    assert [counts[(8,G)] for G in combinations((3,5,6),2)] == [3,1,3]
    assert [counts[(9,G)] for G in combinations((3,5,6),2)] == [28,10,28]
    assert len(stable_cases) == 73 and len(first_edge_possible) == 11
    assert {x for _, _, x in first_edge_possible} == set(all_families(5))
    assert all(liftable(G,0,j) for G in combinations((3,5,6),2)
               for j in (1,2,3) if not ((G==(3,5) and j==1)
                                      or (G==(5,6) and j==3)))
    assert not liftable((3,5),0,1) and not liftable((5,6),0,3)
    # The same fixed finite test box preserves all obstructions after lifting.
    for q in (6, 7, 11):
        for k, G, x in stable_cases:
            y = tuple(x[p-1] + 2*(q-5)*(p in G) for p in range(1,8))
            assert stable_direct(y,q)
            if x not in all_families(5):
                assert capped_first_edge(y,q,G)[0] is False, (q,k,G,y)
    print('PASS stable=7+66, first-edge candidate families=1+10, '
          f'obstructed=62, base_safe_nodes={total_safe}, '
          f'base_bad_nodes={total_bad}')
    print('PASS q=6,7,11 lifted obstacle regressions; all-q from omission-slot lemma')


if __name__ == '__main__':
    main()
