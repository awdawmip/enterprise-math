#!/usr/bin/env python3
"""Exact R5 integer census of the 14-arc K4+high-pair sharp circuits.

Four sources (1,2,3,5); seven ratio numerators (2,10,15,20,25,30,38).
Target labels are distinguishable; F and G are the two interchangeable
copies of the high-high source pair. Standard library only.
"""
from itertools import combinations, permutations
from collections import Counter

SOURCES = (1, 2, 3, 5)
R = (2, 10, 15, 20, 25, 30, 38)


def coefficients(labels):
    """Return exact integer flows for A=pq,B=ph,C=pk,D=qh,E=qk,F=hk,G=hk."""
    a, b, c, d, e, f, g = (R[i] for i in labels)
    ua = (b - c) * (d - e)
    ub = (c - a) * (d - e)
    uc = (a - b) * (d - e)
    ud = -(b - c) * (e - a)
    ue = -(b - c) * (a - d)
    vf = (-ub) * (b - g) + (-ud) * (d - g)
    vg = (-ub) * (f - b) + (-ud) * (f - d)
    ue = -(b - c) * (a - d)
    delta = g - f
    return ua*delta, ub*delta, uc*delta, ud*delta, ue*delta, vf, vg


def source_conservation_holds(labels, coefficients_):
    A, B, C, D, E, F, G = labels
    ua, ub, uc, ud, ue, vf, vg = coefficients_
    rows = (
        ((A, ua), (B, ub), (C, uc)),
        ((A, -ua), (D, ud), (E, ue)),
        ((B, -ub), (D, -ud), (F, vf), (G, vg)),
        ((C, -uc), (E, -ue), (F, -vf), (G, -vg)),
    )
    return all(
        sum(v for _, v in row) == 0
        and sum(R[i]*v for i, v in row) == 0
        for row in rows
    )


def main():
    total = full = degenerate = 0
    zero_targets = Counter()
    for low in combinations(SOURCES, 2):
        per_total = per_full = per_degenerate = 0
        for labels in permutations(range(7)):
            if labels[5] > labels[6]:
                continue  # quotient F/G exchange, no double counting
            cf = coefficients(labels)
            assert all(cf[:5])
            assert source_conservation_holds(labels, cf), (low, labels)
            zeros = [i for i, v in zip(labels, cf) if v == 0]
            assert len(zeros) <= 1, (low, labels, zeros)
            per_total += 1
            if zeros:
                per_degenerate += 1
                zero_targets[zeros[0]] += 1
                assert zeros == [3], (low, labels, zeros)
            else:
                per_full += 1
        assert (per_total, per_full, per_degenerate) == (2520, 2472, 48)
        print("LOW", low, "ASSIGNMENTS", per_total,
              "FULL_SUPPORT_CIRCUITS", per_full, "DEGENERATE", per_degenerate)
        total += per_total
        full += per_full
        degenerate += per_degenerate
    assert (total, full, degenerate) == (15120, 14832, 288)
    assert dict(zero_targets) == {3: 288}
    assert coefficients((0,1,2,3,4,5,6)) == (200,-520,320,920,-720,250,150)
    assert coefficients((0,1,2,4,5,3,6)) == (450,-1170,720,2520,-2070,0,1350)
    print("TOTAL_14_ARC_K4_PLUS_HIGH_HIGH_ASSIGNMENTS", total)
    print("EXACT_FULL_SUPPORT_CIRCUITS", full)
    print("EXACT_ZERO_EDGE_DEGENERACIES", degenerate)
    print("ZERO_EDGE_TARGET_LABEL_COUNTS", sorted(zero_targets.items()))
    print("PASS_EXACT_SHARP_SUPPORT_CLASSIFICATION_14832_OF_15120")


if __name__ == "__main__":
    main()
