#!/usr/bin/env python3
"""Exact unsigned M3 Port-Euler fiber census for all subsets of doubled cube supports.
Each doubled support contributes an unordered multiset of two legal edge types.
The 12 forced edges keep fixed identities and arbitrary positive multiplicities.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
import json

missing = {(0, 1), (2, 3), (4, 5)}
ports = [p for p in combinations(range(6), 2) if p not in missing]
bit = {p: 1 << i for i, p in enumerate(ports)}
cube = list(product((0, 1), repeat=3))


def proj(t):
    i, j, k = t
    return (i, 2+j), (i, 4+k), (2+j, 4+k)


def xor_edge(a, b):
    return bit[a] ^ bit[b]


edge_types = []
for t in cube:
    a, b, c = proj(t)
    edge_types.append((xor_edge(a, b), xor_edge(a, c), xor_edge(b, c)))

forced_edges = []
for triple in combinations(range(6), 3):
    allowed = [p for p in combinations(triple, 2) if p not in missing]
    if len(allowed) == 2:
        forced_edges.append(xor_edge(*allowed))
assert len(forced_edges) == 12
F = {0}
for edge in forced_edges:
    F |= {x ^ edge for x in tuple(F)}
assert len(F) == 512

single = [[(e, 1 << typ) for typ, e in enumerate(options)]
          for options in edge_types]
double = [[(options[a] ^ options[b], (1 << a) | (1 << b))
           for a in range(3) for b in range(a, 3)]
          for options in edge_types]


def fiber(ups):
    # (12-bit boundary, 3-bit quotient edge-type set) -> number of distinct choices
    dp = {(0, 0): 1}
    for i in range(8):
        nxt = defaultdict(int)
        for (boundary, used), n in dp.items():
            for e, types in (double[i] if i in ups else single[i]):
                nxt[(boundary ^ e, used | types)] += n
        dp = nxt
    result = Counter()
    for (b, used), n in dp.items():
        if b in F and used.bit_count() >= 2:
            result[b] += n
    return result


def direct(ups):
    # Independent tuple enumeration for selected representatives.
    options = [list(combinations_with_replacement(range(3), 2)) if i in ups
               else [(j,) for j in range(3)] for i in range(8)]
    counts = Counter()
    for assignment in product(*options):
        parity = 0
        used = set()
        for i, picked in enumerate(assignment):
            for typ in picked:
                parity ^= edge_types[i][typ]
                used.add(typ)
        if parity in F and len(used) >= 2:
            counts[parity] += 1
    return counts


def combinations_with_replacement(values, r):
    from itertools import combinations_with_replacement as cwr
    return cwr(values, r)


# Independent exact check: direct tuples versus boundary/type DP on four cases.
for ups in [(), (0,), (0, 1), (0, 7)]:
    assert direct(frozenset(ups)) == fiber(frozenset(ups))

rows = []
for k in range(9):
    entries = []
    for inds in combinations(range(8), k):
        result = fiber(frozenset(inds))
        entries.append((inds, result))
        # Character/Fourier evaluation of the quotient's edge-type parity polynomial.
        n_expected = (2**k * (3**8 + 3) // 4 - 3) if k % 2 == 0 \
            else (2**k * (3**8 - 3) // 4)
        assert sum(result.values()) == n_expected
        assert len(result) == (465 if k == 0 else 495 if k == 1 else
                               508 if k == 2 else 512)
    mins = Counter(min(v.values()) for _, v in entries)
    maximum = max(max(v.values()) for _, v in entries)
    rows.append({"doubled_supports": k, "subsets": len(entries),
                 "reachable_boundaries": len(entries[0][1]),
                 "connected_realizations_per_subset": sum(entries[0][1].values()),
                 "minimum_positive_fiber_distribution": dict(sorted(mins.items())),
                 "max_fiber_over_all_subsets": maximum})
assert rows[0]["connected_realizations_per_subset"] == 1638
assert rows[8]["connected_realizations_per_subset"] == 420093
assert rows[8]["max_fiber_over_all_subsets"] == 7197
assert min(min(v.values()) for k in range(9)
           for inds in combinations(range(8), k)
           for v in [fiber(frozenset(inds))]) == 2

print(json.dumps({"schema": "R762KM_M3_UPGRADE_FIBERS_V1",
                  "port_order": ["".join(map(str, p)) for p in ports],
                  "cube_order": ["".join(map(str, (i, 2+j, 4+k))) for i, j, k in cube],
                  "edge_type_order": ["AB", "AC", "BC"],
                  "count_convention": "unordered edge multisets for doubled supports",
                  "forced_boundary_size": len(F),
                  "independent_direct_checks": [[], [0], [0, 1], [0, 7]],
                  "rows": rows, "all_assertions_passed": True},
                 ensure_ascii=False, indent=2))
