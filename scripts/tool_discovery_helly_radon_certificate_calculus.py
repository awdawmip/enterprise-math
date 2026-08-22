#!/usr/bin/env python3
"""Deterministic bounded checks for the Enterprise block finite-certificate calculus.

This script is evidence for finite examples only.  The structural theorems are proved
in the accompanying research note and do not depend on enumeration.
"""
from __future__ import annotations

from itertools import combinations, product
import hashlib
import json


def intervals(n: int):
    return [frozenset(range(lo, hi + 1)) for lo in range(n) for hi in range(lo, n)]


def intersects(family):
    if not family:
        return True
    common = set(family[0])
    for s in family[1:]:
        common.intersection_update(s)
    return bool(common)


def box_intersects(family):
    if not family:
        return True
    dim = len(family[0])
    return all(intersects([box[j] for box in family]) for j in range(dim))


def check_interval_boxes(domain_size: int = 3, dim: int = 2, max_family: int = 4):
    ints = intervals(domain_size)
    boxes = list(product(ints, repeat=dim))
    checked = 0
    pairwise_feasible = 0
    violations = []
    for k in range(2, max_family + 1):
        for fam in combinations(boxes, k):
            checked += 1
            all_pairs = all(box_intersects(pair) for pair in combinations(fam, 2))
            if all_pairs:
                pairwise_feasible += 1
                if not box_intersects(fam):
                    violations.append(fam)
                    break
        if violations:
            break
    sharp_left = (frozenset({0}), frozenset(range(domain_size)))
    sharp_right = (frozenset({domain_size - 1}), frozenset(range(domain_size)))
    return {
        "domain_size": domain_size,
        "dimension": dim,
        "box_count": len(boxes),
        "families_checked": checked,
        "pairwise_feasible_families": pairwise_feasible,
        "helly2_violations": len(violations),
        "sharp_two_constraint_obstruction": not box_intersects([sharp_left, sharp_right]),
    }


def sat_chain(n: int, omitted: int | None = None):
    # constraints: 0 = left endpoint; 1..n-1 = equalities; n = right endpoint
    def ok(bits):
        if omitted != 0 and bits[0] != 0:
            return False
        for i in range(n - 1):
            ci = i + 1
            if omitted != ci and bits[i] != bits[i + 1]:
                return False
        if omitted != n and bits[-1] != 1:
            return False
        return True

    return any(ok(bits) for bits in product((0, 1), repeat=n))


def check_unbounded_chain(n_min: int = 2, n_max: int = 10):
    rows = []
    for n in range(n_min, n_max + 1):
        whole_sat = sat_chain(n, None)
        deletion_sat = [sat_chain(n, omitted) for omitted in range(n + 1)]
        rows.append({
            "variables": n,
            "constraints": n + 1,
            "whole_infeasible": not whole_sat,
            "every_single_deletion_feasible": all(deletion_sat),
        })
    return {
        "range": [n_min, n_max],
        "all_minimal_obstructions_verified": all(
            r["whole_infeasible"] and r["every_single_deletion_feasible"] for r in rows
        ),
        "rows": rows,
    }


def subcube_hull(points):
    if not points:
        return None
    d = len(points[0])
    return tuple(frozenset(p[j] for p in points) for j in range(d))


def in_subcube(point, hull):
    return hull is not None and all(point[j] in hull[j] for j in range(len(point)))


def check_carath_lower_bound(d_min: int = 2, d_max: int = 8):
    rows = []
    for d in range(d_min, d_max + 1):
        x = (0,) * d
        S = [tuple(0 if j == i else 1 for j in range(d)) for i in range(d)]
        full = in_subcube(x, subcube_hull(S))
        every_deletion_fails = all(
            not in_subcube(x, subcube_hull(S[:i] + S[i + 1 :])) for i in range(d)
        )
        rows.append({
            "dimension": d,
            "witness_size": d,
            "target_in_full_hull": full,
            "target_lost_after_every_single_deletion": every_deletion_fails,
        })
    return {
        "range": [d_min, d_max],
        "all_lower_bounds_verified": all(
            r["target_in_full_hull"] and r["target_lost_after_every_single_deletion"]
            for r in rows
        ),
        "rows": rows,
    }


def check_enterprise_demos():
    # Fixed-sector S_12: address coordinates (a,b), interpreted as (a,b,0).
    chart_constraints = [
        (frozenset(range(2, 8)), frozenset(range(1, 7))),
        (frozenset(range(5, 10)), frozenset(range(0, 5))),
        (frozenset(range(4, 9)), frozenset(range(3, 10))),
    ]
    chart_common = (
        sorted(set.intersection(*(set(c[0]) for c in chart_constraints))),
        sorted(set.intersection(*(set(c[1]) for c in chart_constraints))),
    )

    # Typed Boolean-BRC support profile over three declared support atoms.
    # Coordinate admissible sets are {0}, {1}, or {0,1}.
    ANY = frozenset({0, 1})
    support_constraints = [
        (frozenset({1}), ANY, frozenset({0})),
        (ANY, frozenset({1}), ANY),
        (frozenset({1}), ANY, ANY),
    ]
    support_common = tuple(
        sorted(set.intersection(*(set(c[j]) for c in support_constraints))) for j in range(3)
    )
    conflict = support_constraints[0], (ANY, ANY, frozenset({1}))

    return {
        "fixed_sector_chart": {
            "globally_feasible": box_intersects(chart_constraints),
            "common_a_values": chart_common[0],
            "common_b_values": chart_common[1],
            "sample_native_address": [5, 3, 0],
        },
        "typed_boolean_brc_support": {
            "globally_feasible": box_intersects(support_constraints),
            "coordinatewise_common_values": support_common,
            "sample_support_mask": [1, 1, 0],
            "two_constraint_conflict_verified": not box_intersects(conflict),
        },
    }


def main():
    payload = {
        "schema": "ENTERPRISE_TDHR_BOUNDED_VERIFICATION_V1",
        "interval_box_helly2": check_interval_boxes(),
        "unbounded_relational_chain": check_unbounded_chain(),
        "subcube_carath_lower_bound": check_carath_lower_bound(),
        "enterprise_cross_domain_demos": check_enterprise_demos(),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
