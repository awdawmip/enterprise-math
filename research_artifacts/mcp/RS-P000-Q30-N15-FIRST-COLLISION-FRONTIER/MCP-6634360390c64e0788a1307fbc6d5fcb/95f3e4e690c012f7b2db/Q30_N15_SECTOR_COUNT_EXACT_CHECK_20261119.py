#!/usr/bin/env python3
"""Exact fixed-degree labeled simple-graph sector targets for Q30 n=15.
No graph enumeration, no 1-WL packet calculation, no collision conclusion.
"""
from functools import lru_cache
from math import comb, factorial
import json

@lru_cache(None)
def all_graphs(n0, n1, n2, n3):
    counts = [n0, n1, n2, n3]
    if n1 + n2 + n3 == 0:
        return 1
    if sum(k * counts[k] for k in range(4)) % 2:
        return 0
    d = max(k for k in range(4) if counts[k])
    counts[d] -= 1
    if d > sum(counts[1:]):
        return 0
    total = 0
    for a in range(min(d, counts[1]) + 1):
        for b in range(min(d - a, counts[2]) + 1):
            c = d - a - b
            if c < 0 or c > counts[3]:
                continue
            nxt = (counts[0] + a, counts[1] - a + b,
                   counts[2] - b + c, counts[3] - c)
            total += (comb(counts[1], a) * comb(counts[2], b)
                      * comb(counts[3], c) * all_graphs(*nxt))
    return total

@lru_cache(None)
def connected(r, s):
    # r distinct specified cubic labels, s specified degree-two labels.
    if r == 0:
        return factorial(s - 1) // 2 if s >= 3 else 0
    if r % 2:
        return 0
    total = all_graphs(0, 0, s, r)
    # Unique component containing the first cubic vertex.
    for rr in range(2, r + 1, 2):
        for ss in range(s + 1):
            if (rr, ss) == (r, s) or rr + ss < 4:
                continue
            total -= (comb(r - 1, rr - 1) * comb(s, ss)
                      * connected(rr, ss) * all_graphs(0, 0, s - ss, r - rr))
    return total

N14 = {2: 12414124800, 4: 38690265600, 6: 120607023600,
       8: 393165964800, 10: 1358543793600,
       12: 4991840330400, 14: 19491385914000}

def main():
    for r, expected in N14.items():
        assert connected(r, 14 - r) == expected, (r, connected(r, 14-r))
    sectors = [{"r": r, "s": 15 - r,
                "connected_fixed_degree_labels": connected(r, 15 - r),
                "all_fixed_degree_labels": all_graphs(0, 0, 15 - r, r)}
               for r in range(2, 15, 2)]
    obj = {"schema": "Q30_N15_FIXED_DEGREE_SECTOR_TARGETS_V1",
           "scope": "connected labeled simple (degree 3)^r (degree 2)^s with fixed degree-class labels, n=15",
           "role": "independent orbit-coverage count targets; NOT enumeration/1-WL/collision proof",
           "n14_regression": "7/7 match prior exact sector totals",
           "sectors": sectors,
           "sector_fixed_label_sum": sum(x["connected_fixed_degree_labels"] for x in sectors),
           "all_labeled_degree_assignments_total":
           sum(comb(15, x["r"]) * x["connected_fixed_degree_labels"] for x in sectors)}
    print(json.dumps(obj, indent=2))

if __name__ == "__main__":
    main()
