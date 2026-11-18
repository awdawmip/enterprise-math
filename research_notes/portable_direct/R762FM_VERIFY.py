#!/usr/bin/env python3
"""Finite checker for a typed X6 signed-triad incidence *candidate*.

Exact integer, enumerative, no external libraries. This is a discrete branch-incidence
calculation, not evidence that the native TRIADIC_CLOSURE_E law has been adopted.
"""
from itertools import combinations, product
import json

AXES = tuple(range(1, 7))
SIGNS = (-1, 1)

def charges(signs):
    q = 1
    for s in signs:
        q *= s
    return q

def closed(signs, orientation):
    return charges(signs) == orientation

def generators():
    # Six sign-flips and five adjacent permutations generate W6.
    for i in AXES:
        yield ("flip", i)
    for i in range(1, 6):
        yield ("swap", i)

def transform_axes_signs(axes, signs, orientation, gen):
    axes2 = list(axes)
    signs2 = list(signs)
    o2 = orientation
    if gen[0] == "flip":
        j = gen[1]
        for idx, a in enumerate(axes):
            if a == j:
                signs2[idx] = -signs2[idx]
                o2 = -o2
    else:
        j = gen[1]
        axes2 = [j + 1 if a == j else j if a == j + 1 else a for a in axes]
    pairs = sorted(zip(axes2, signs2))
    return tuple(a for a, s in pairs), tuple(s for a, s in pairs), o2

def fan(axes, signs):
    # c=0 denotes a selected chart anchor, not a distinguished native origin.
    return tuple(tuple(s if j == a else 0 for j in AXES) for a, s in zip(axes, signs))

def transform_vector(v, gen):
    if gen[0] == "flip":
        return tuple(-x if i == gen[1] else x for i, x in enumerate(v, 1))
    i = gen[1]
    out = list(v)
    out[i-1], out[i] = out[i], out[i-1]
    return tuple(out)

def partitions_of_six():
    # Unordered partitions into two unordered triples: choose the triple of 1.
    ans = []
    for x, y in combinations(AXES[1:], 2):
        a = frozenset((1, x, y))
        b = frozenset(set(AXES) - a)
        ans.append((a, b))
    return ans

def run():
    gens = list(generators())
    total = closed_count = covariance_checks = 0
    witness = None
    for axes in combinations(AXES, 3):
        for signs in product(SIGNS, repeat=3):
            for o in SIGNS:
                total += 1
                accept = closed(signs, o)
                closed_count += int(accept)
                F = set(fan(axes, signs))
                assert len(F) == 3 and all(sum(abs(x) for x in v) == 1 for v in F)
                for g in gens:
                    a2, s2, o2 = transform_axes_signs(axes, signs, o, g)
                    assert closed(s2, o2) == accept
                    assert set(fan(a2, s2)) == {transform_vector(v, g) for v in F}
                    covariance_checks += 1
                if axes == (1, 2, 3) and signs == (1, 1, 1) and o == -1:
                    witness = {"axes": list(axes), "signs": list(signs), "orientation": o,
                               "closed": accept, "flipped_orientation_closed": closed(signs, 1)}
    assert total == 320 and closed_count == 160 and covariance_checks == 3520
    patterns = set(product(SIGNS, repeat=3))
    seen = {(1, 1, 1)}
    frontier = list(seen)
    while frontier:
        s = frontier.pop()
        for j in range(3):
            t = tuple(-v if k == j else v for k, v in enumerate(s))
            if t not in seen:
                seen.add(t)
                frontier.append(t)
    assert seen == patterns
    pair_lifts = []
    for k in AXES[2:]:
        for o in SIGNS:
            s3 = o
            pair_lifts.append({"third_axis": k, "third_sign": s3, "orientation": o})
            assert closed((1, 1, s3), o)
    assert len(pair_lifts) == 8
    P = partitions_of_six()
    assert len(P) == 10
    signatures = {tuple(sorted(a - {1})) for a, b in P}
    assert len(signatures) == 10
    assert {a | b for a, b in P} == {frozenset(AXES)}
    assert all(len(a & b) == 0 and len(a) == len(b) == 3 for a, b in P)
    assert 2**3 < len(P) <= 2**4
    return {
        "schema": "EM_R762FM_SIGNED_TRIAD_COVARIANT_INCIDENCE_V1",
        "date": "2026-11-19",
        "scoped_model": "candidate W6-covariant signed X6 triad-incidence fan; not a native license",
        "axes": 6,
        "native_signed_directions": 12,
        "axis_triples": 20,
        "sign_patterns_per_triple": 8,
        "orientation_tags": 2,
        "total_tagged_candidates": total,
        "closed_tagged_candidates": closed_count,
        "generator_count": len(gens),
        "closure_and_fan_covariance_checks": covariance_checks,
        "single_triple_sign_flip_orbit_size": len(seen),
        "two_visible_plus_legs_with_orientation_unknown_lifts": len(pair_lifts),
        "two_visible_plus_legs_with_orientation_fixed_lifts": 4,
        "unlabeled_two_triad_partitions_of_six_distinct_axes": len(P),
        "distinct_future_partner_pair_signatures": len(signatures),
        "min_fixed_bits_for_pairing_under_all_partner_queries": 4,
        "example_nonclosed_tagged_incidence": witness,
        "arithmetic": "finite exact integer enumeration; pure labelled-branch combinatorics",
        "proof_status": "author_proved_plus_full_finite_checker; not independently reviewed",
        "native_signed_event_status": "candidate construction only; actual TRIADIC_CLOSURE_E admission open",
        "checks": "PASS"
    }

if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2, sort_keys=True))
