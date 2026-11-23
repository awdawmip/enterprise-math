#!/usr/bin/env python3
"""R284FO: finite crosscheck of the four-epoch lower bound n >= 4q+5u+2.

Self-contained exact integer arithmetic. Enumerates all seven nonconstant
four-phase column-pattern histograms at n=4q+5u+1. A surviving histogram
would meet all four necessary write-prefix distances and the exact opposite-
phase endpoint flow cuts of R284FM. None should survive in the tested range.
This is a finite crosscheck; the all-parameter theorem uses a written proof.
"""
from itertools import combinations
from math import comb
import json

# p encodes the three bits c1,c2,c3 with c0=0; a column is a four-bit history.
PAT = {}
for p in range(1, 8):
    bits = (0, p & 1, (p >> 1) & 1, (p >> 2) & 1)
    changed_edges = {i for i in range(4) if bits[i] != bits[(i - 1) % 4]}
    last = tuple(next((i - t) % 4 for t in range(4)
                      if (i - t) % 4 in changed_edges) for i in range(4))
    PAT[p] = (bits, last)


def weak_compositions(total, parts):
    """All ordered nonnegative integer tuples summing to total, exactly once."""
    for divs in combinations(range(total + parts - 1), parts - 1):
        prev = -1
        ans = []
        for d in divs:
            ans.append(d - prev - 1)
            prev = d
        ans.append(total + parts - 2 - prev)
        yield tuple(ans)


def subset_cuts(i, j, q, u):
    """For every cut U return (pattern mask, minimal required multiplicity)."""
    edges = [(p, PAT[p][1][i], 4 + PAT[p][1][j])
             for p in range(1, 8) if PAT[p][0][i] != PAT[p][0][j]]
    min_vertices = {}
    for vertex_mask in range(1, 256):
        column_mask = 0
        for p, left, right in edges:
            if (vertex_mask & (1 << left)) and (vertex_mask & (1 << right)):
                column_mask |= 1 << (p - 1)
        if column_mask:
            cardinality = vertex_mask.bit_count()
            min_vertices[column_mask] = min(
                cardinality, min_vertices.get(column_mask, 99))
    return [(tuple(t for t in range(7) if m & (1 << t)),
             q * vertex_count + 2 * u + 1)
            for m, vertex_count in min_vertices.items()]


def verify(q, u):
    n = 4 * q + 5 * u + 1
    adjacent = [(0, 1), (1, 2), (2, 3), (3, 0)]
    opposite = [(0, 2), (1, 3)]
    a = 2 * q + 4 * u + 1  # R284FH write-prefix necessary distance
    b = 2 * (q + u) + 1   # stable noisy ball necessary distance
    requirements = [(
        tuple(p - 1 for p in range(1, 8) if PAT[p][0][i] != PAT[p][0][j]),
        a if (i, j) in adjacent else b)
        for i, j in adjacent + opposite]
    cut_reqs = [subset_cuts(i, j, q, u) for i, j in opposite]
    total = passed_distance = passed_both_cuts = 0
    for x in weak_compositions(n, 7):
        total += 1
        if not all(sum(x[k] for k in ps) >= threshold
                   for ps, threshold in requirements):
            continue
        passed_distance += 1
        if all(any(sum(x[k] for k in ps) >= threshold for ps, threshold in cuts)
               for cuts in cut_reqs):
            passed_both_cuts += 1
    assert total == comb(n + 6, 6), (n, total)
    assert passed_both_cuts == 0, (q, u, passed_both_cuts)
    return {"q": q, "u": u, "boundary_n": n,
            "histograms": total, "meet_six_distances": passed_distance,
            "meet_both_exact_opposite_cuts": passed_both_cuts}


def main():
    cases = [verify(q, u) for q in range(5) for u in range(3)]
    print(json.dumps({"claim": "n_min(q,u)>=4q+5u+2",
                      "checks": cases,
                      "total_histograms": sum(v["histograms"] for v in cases),
                      "total_distance_survivors": sum(v["meet_six_distances"] for v in cases),
                      "all_boundary_candidates_excluded": True}, indent=2))


if __name__ == "__main__":
    main()
