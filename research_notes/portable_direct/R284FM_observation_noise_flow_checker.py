#!/usr/bin/env python3
"""R284FM exact endpoint/noise cut checker. Standard-library only."""
from itertools import combinations

PAIRS = tuple(combinations(range(4), 2))
A, B = (2, 3, 6, 7), (1, 3, 4, 6)
AA = ((2, 3), (2, 6), (3, 7), (6, 7))
BB = ((1, 3), (1, 6), (3, 4), (4, 6))


def last_edge(values, phase):
    for offset in range(4):
        edge = (phase - 1 - offset) % 4
        if values[edge] != values[(edge + 1) % 4]:
            return edge
    raise AssertionError("constant coordinate should be excluded")


def cut_separates(codes, q, u):
    """Exact criterion for disjoint u-noisy stable phase readouts."""
    n = max(codes).bit_length()
    for i, j in PAIRS:
        edges = []
        for bit in range(n):
            vals = tuple((c >> bit) & 1 for c in codes)
            if vals[i] != vals[j]:
                edges.append((last_edge(vals, i), 4 + last_edge(vals, j)))
        if not any(
            sum(bool(mask & (1 << left)) and bool(mask & (1 << right))
                for left, right in edges) > q * mask.bit_count() + 2 * u
            for mask in range(1, 256)
        ):
            return False
    return True


def stable_states(codes, q):
    """BFS from pristine phase 0 across any number of complete publications."""
    n = max(codes).bit_length()
    reach = [set() for i in range(4)]
    reach[0].add(codes[0])
    dirty = True
    while dirty:
        dirty = False
        for i in range(4):
            j = (i + 1) % 4
            touched = codes[i] ^ codes[j]
            positions = [k for k in range(n) if (touched >> k) & 1]
            omitted = [sum(1 << k for k in group)
                       for r in range(min(q, len(positions)) + 1)
                       for group in combinations(positions, r)]
            for old in tuple(reach[i]):
                for miss in omitted:
                    # Only nominally changed positions are attempted.
                    new = (old & ~touched) | (old & miss) | (codes[j] & (touched ^ miss))
                    if new not in reach[j]:
                        reach[j].add(new)
                        dirty = True
    return reach


def direct_separates(codes, n, q, u):
    reach = stable_states(codes, q)
    masks = [sum(1 << k for k in ks)
             for r in range(u + 1)
             for ks in combinations(range(n), r)]
    readouts = [set(w ^ flip for w in states for flip in masks) for states in reach]
    return all(not (readouts[i] & readouts[j]) for i, j in PAIRS)


def compositions(total, count):
    if count == 1:
        yield (total,)
    else:
        for x in range(total + 1):
            for tail in compositions(total - x, count - 1):
                yield (x,) + tail


def diagonal_separates(x, modes, adj, q, u):
    return (any(x[k] >= 2*q + 2*u + 1 for k in modes)
            or any(x[k] + x[l] >= 3*q + 2*u + 1 for k, l in adj)
            or sum(x[k] for k in modes) >= 4*q + 2*u + 1)


def test():
    # Complete ordered four-code tuples, c0 normalized to 0, for n=3,4.
    samples = ((3, 0, 0), (3, 1, 0), (3, 0, 1),
               (4, 0, 0), (4, 1, 0), (4, 0, 1), (4, 1, 1))
    checks = 0
    for n, q, u in samples:
        count = 0
        for a, b, c in ((a, b, c)
                        for a in range(1, 1 << n)
                        for b in range(1, 1 << n) if b != a
                        for c in range(1, 1 << n) if c not in (a, b)):
            word = (0, a, b, c)
            assert cut_separates(word, q, u) == direct_separates(word, n, q, u), (n,q,u,word)
            count += 1
        checks += count
        print(f"all codes n={n} q={q} u={u}: {count} consistent")
    assert checks == 11550

    # Necessary four-phase lower bound, tested at n=4q+2u+1.
    histograms = 0
    for q in range(4):
        for u in range(2):
            n = 4*q + 2*u + 1
            checked = 0
            for vec in compositions(n, 7):
                x = (0,) + vec
                # The theorem's disjoint-diagonal witness, plus min distance.
                pair_distances = (
                    (1,3,5,7), (2,3,6,7), (4,5,6,7),
                    (1,2,5,6), (1,3,4,6), (2,3,4,5))
                if (all(sum(x[p] for p in D) >= 2*q + 2*u + 1 for D in pair_distances)
                    and diagonal_separates(x,A,AA,q,u)
                    and diagonal_separates(x,B,BB,q,u)):
                    raise AssertionError((q,u,n,vec))
                checked += 1
            histograms += checked
            print(f"bound n={n} q={q} u={u}: {checked} histograms; 0 candidates")
    print(f"PASS: {checks} explicit-code comparisons; {histograms} histogram checks")

if __name__ == '__main__':
    test()
