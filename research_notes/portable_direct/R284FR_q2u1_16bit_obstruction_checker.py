#!/usr/bin/env python3
"""Exact no-16-bit certificate for four-phase reset-free omission/noisy reads.

Four nominal fixed words, q=2 omissions per update, u=1 transient bit flip
per read; all past omissions can persist. Independent of chosen coordinate
order. Tests a necessary condition; no semantic decoding is assumed.
"""
from itertools import combinations, product
from collections import deque
from functools import lru_cache
from math import comb

N, Q, U = 16, 2, 1
PAIRS = ((0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (1, 3))
PAT = {}
for p in range(1, 8):
    bit = (0, p & 1, (p >> 1) & 1, (p >> 2) & 1)
    change_edges = {e for e in range(4) if bit[e] != bit[(e + 1) % 4]}
    latest = tuple(next((i - 1 - t) % 4 for t in range(4)
                        if (i - 1 - t) % 4 in change_edges)
                   for i in range(4))
    PAT[p] = (bit, latest)


def compositions(n, m):
    for cuts in combinations(range(n + m - 1), m - 1):
        prev = -1
        x = []
        for cut in cuts:
            x.append(cut - prev - 1)
            prev = cut
        yield tuple(x + [n + m - 2 - prev])


def cutsets(i, j):
    # For each vertex subset, record multiedge types with BOTH endpoints in it.
    edges = [(p, PAT[p][1][i], 4 + PAT[p][1][j])
             for p in range(1, 8) if PAT[p][0][i] != PAT[p][0][j]]
    thresholds = {}
    for vertices in range(1, 256):
        typemask = sum(1 << (p - 1) for p, a, b in edges
                       if vertices & (1 << a) and vertices & (1 << b))
        if typemask:
            thresholds[typemask] = min(thresholds.get(typemask, 100),
                                       Q * vertices.bit_count() + 2 * U + 1)
    return [(tuple(k for k in range(7) if mask >> k & 1), threshold)
            for mask, threshold in thresholds.items()]


def endpoint_candidates():
    distances = [tuple(p - 1 for p in range(1, 8)
                       if PAT[p][0][i] != PAT[p][0][j]) for i, j in PAIRS]
    thresholds = [2 * Q + 4 * U + 1] * 4 + [2 * (Q + U) + 1] * 2
    graphs = [cutsets(i, j) for i, j in PAIRS]
    distance_survivors = 0
    endpoint_survivors = []
    for x in compositions(N, 7):
        if any(sum(x[p] for p in ps) < threshold
               for ps, threshold in zip(distances, thresholds)):
            continue
        distance_survivors += 1
        if all(any(sum(x[p] for p in ps) >= threshold for ps, threshold in graph)
               for graph in graphs):
            endpoint_survivors.append(x)
    assert comb(N + 6, 6) == 74613
    assert distance_survivors == 1270, distance_survivors
    assert len(endpoint_survivors) == 36, len(endpoint_survivors)
    return endpoint_survivors


def words_and_phases(x):
    word = [0] * 4
    positions = {p: [] for p in range(1, 8)}
    bit_idx = 0
    for p in range(1, 8):
        for _ in range(x[p - 1]):
            positions[p].append(bit_idx)
            for i in range(1, 4):
                if (p >> (i - 1)) & 1:
                    word[i] |= 1 << bit_idx
            bit_idx += 1
    stable = []
    for phase in range(4):
        groups = {e: [] for e in range(4)}
        for p, pos in positions.items():
            groups[PAT[p][1][phase]].extend(pos)
        masks = [[sum(1 << k for k in chosen)
                  for count in range(min(Q, len(group)) + 1)
                  for chosen in combinations(group, count)]
                 for group in groups.values()]
        states = [word[phase] ^ (a | b | c | d)
                  for a, b, c, d in product(*masks)]
        assert len(states) == len(set(states))
        stable.append(states)
    return word, positions, stable


def forced_read_masks(stable):
    # phase j is FORCED at physical prefix w if d(w,S_j)<=2u: there is
    # an observed word y within 1 flip of w and within 1 flip of S_j.
    force = bytearray(1 << N)
    for phase, states in enumerate(stable):
        for s in states:
            force[s] |= 1 << phase
            for a in range(N):
                v = s ^ (1 << a)
                force[v] |= 1 << phase
                for b in range(a + 1, N):
                    force[v ^ (1 << b)] |= 1 << phase
    return force


def has_locally_safe_order(edge, words, positions, stable, force):
    target = (edge + 1) % 4
    types = [p for p in range(1, 8) if positions[p]
             and PAT[p][0][edge] != PAT[p][0][target]]
    initial = (0,) * len(types)
    final = tuple(len(positions[p]) for p in types)
    valid_phase_bits = (1 << edge) | (1 << target)

    @lru_cache(None)
    def locally_safe(prefix):
        # Symmetry: only the count of attempted coordinates of each type matters.
        attempted = [k for p, t in zip(types, prefix) for k in positions[p][:t]]
        omissions = [0] + [1 << k for k in attempted] + [
            (1 << a) | (1 << b) for a, b in combinations(attempted, 2)]
        for miss in omissions:
            successful_mask = sum(1 << k for k in attempted) ^ miss
            target_bits = words[target] & successful_mask
            for source in stable[edge]:
                physical = (source & ~successful_mask) | target_bits
                f = force[physical]
                if (f & ~valid_phase_bits) or (f & (1 << edge) and f & (1 << target)):
                    return False
        return True

    queue = deque([initial]); seen = {initial}
    while queue:
        prefix = queue.popleft()
        if prefix == final:
            return True
        for i, p in enumerate(types):
            if prefix[i] == len(positions[p]):
                continue
            nxt = list(prefix)
            nxt[i] += 1
            nxt = tuple(nxt)
            if nxt not in seen and locally_safe(nxt):
                seen.add(nxt)
                queue.append(nxt)
    return False


def main():
    survivors = endpoint_candidates()
    first_edge_safe = []
    for x in survivors:
        words, positions, stable = words_and_phases(x)
        force = forced_read_masks(stable)
        if has_locally_safe_order(0, words, positions, stable, force):
            first_edge_safe.append(x)
            assert not has_locally_safe_order(1, words, positions, stable, force), x
    assert first_edge_safe == [(0, 0, 0, 0, 9, 7, 0)], first_edge_safe
    print('n=16: 74613 complete coordinate-pattern histograms')
    print('n=16: 1270 pass all six necessary distance bounds')
    print('n=16: 36 pass all six exact endpoint observer cuts')
    print('n=16: 35 fail edge 0->1 local-prefix condition')
    print('n=16: unique edge-0 survivor fails edge 1->2')
    print('CONCLUSION: no correct 16-bit four-phase protocol for (q,u)=(2,1)')
    print('Combined with R284FQ n>=16 and R284FE n<=18: 17 <= n_min <= 18')

if __name__ == '__main__':
    main()
