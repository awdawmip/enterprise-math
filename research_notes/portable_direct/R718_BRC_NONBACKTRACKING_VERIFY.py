#!/usr/bin/env python3
"""R718: cyclic non-backtracking path-formal BRC/S3 histogram, exact integers."""
import json
from collections import defaultdict
from itertools import permutations

STATES = tuple(permutations(range(6), 3))
INDEX = {s: i for i, s in enumerate(STATES)}
MASK = tuple(sum(1 << x for x in s) for s in STATES)
ROOT = INDEX[(0, 1, 2)]
ROOT_MASK = MASK[ROOT]
NEIGH = tuple(tuple(INDEX[s[:j] + (x,) + s[j + 1:]]
                    for j in range(3) for x in range(6) if x not in s)
              for s in STATES)
PERMS = tuple(permutations(range(3)))


def holonomy(i):
    return tuple(STATES[i].index(x) for x in range(3))


def histogram_dp(length):
    """Fixed root, all source-labelled ordered-slot lifts, cyclic NB at root."""
    result = defaultdict(int)
    if length < 2:
        return result
    for first in NEIGH[ROOT]:
        current = {(ROOT, first): 1}
        for step in range(2, length + 1):
            after = defaultdict(int)
            for (prev, pos), ways in current.items():
                for nxt in NEIGH[pos]:
                    if MASK[nxt] == MASK[prev]:
                        continue  # no immediate reversal of an unordered triad edge
                    if step == length:
                        if MASK[nxt] != ROOT_MASK:
                            continue
                        if MASK[pos] == MASK[first]:
                            continue  # cyclic seam at the root
                    after[(pos, nxt)] += ways
            current = after
        for (_, final), ways in current.items():
            result[holonomy(final)] += ways
    return result


def histogram_dfs(length):
    """Independent literal path enumeration, used for lengths <= 6."""
    result = defaultdict(int)
    def visit(path):
        pos = path[-1]
        steps = len(path) - 1
        if steps == length:
            if MASK[pos] == ROOT_MASK and MASK[path[-2]] != MASK[path[1]]:
                result[holonomy(pos)] += 1
            return
        for nxt in NEIGH[pos]:
            if len(path) >= 2 and MASK[nxt] == MASK[path[-2]]:
                continue
            if steps + 1 == length and MASK[nxt] != ROOT_MASK:
                continue
            visit(path + [nxt])
    visit([ROOT])
    return result


def main():
    assert len(STATES) == 120
    assert all(len(n) == 9 for n in NEIGH)
    hist = {m: histogram_dp(m) for m in range(1, 17)}
    expected = {
        3: (18, 6, 0),
        4: (54, 48, 9),
        5: (360, 252, 198),
        6: (2934, 2064, 2133),
    }
    transpositions = ((1, 0, 2), (0, 2, 1), (2, 1, 0))
    cycles = ((1, 2, 0), (2, 0, 1))
    for m in (3, 4, 5, 6):
        d = hist[m]
        assert tuple(d.get(p, 0) for p in transpositions) == (expected[m][1],) * 3
        assert tuple(d.get(p, 0) for p in cycles) == (expected[m][2],) * 2
        assert d.get((0, 1, 2), 0) == expected[m][0]
        assert dict(histogram_dfs(m)) == dict(d)
    assert sum(hist[2].values()) == 0
    for m in range(4, 17):
        assert set(hist[m]) == set(PERMS)
    result = {
        "schema": "R718_CYCLIC_NONBACKTRACKING_BRC_V1",
        "native_source_pin": "a72226e2430ffa4786321ac86e7f0c599d5f0389",
        "root": [0, 1, 2],
        "constraint": "unordered-triad immediate reversals prohibited, including root seam",
        "histogram": {str(m): {"".join(map(str, p)): hist[m].get(p, 0) for p in PERMS}
                      for m in range(1, 17)},
        "checks": ["120 ordered slot states", "nine one-slot neighbours per state",
                   "exact DP through length 16", "independent exhaustive DFS at m=3..6",
                   "six observed holonomies for all m=4..16"],
        "status": "R718_BRC_CYCLIC_NB_SIX_STATE_PASS",
    }
    print(json.dumps(result, sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
