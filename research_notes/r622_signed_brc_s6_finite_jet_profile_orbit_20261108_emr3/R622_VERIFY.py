#!/usr/bin/env python3
"""Exact finite-jet S6 orbit and grade-boundary verifier for frozen R462 signed BRC.

Python standard library only; arbitrary-precision integers; no floating point.
The verifier reconstructs the twelve K_i from the frozen binomial formula,
then enumerates all 720 S6 orientations at every truncation degree d=0..11.
"""
from __future__ import annotations
from itertools import permutations, product
from math import comb, factorial
import argparse
import hashlib
import json
from pathlib import Path

SCIENCE_COMMIT = "18783e01e3646c72b7aab3b16d3f565e83e6446f"
K_BLOB = "7fa7a762f758b30c6090468ac43487daa34abad8"

def C(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0

def add(a: list[int], b: list[int]) -> list[int]:
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out

def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out

def frozen_K(i: int) -> list[int]:
    """R462 theta=0 K_i, coefficients in ascending t-degree."""
    d = [
        -C(4, i) + C(2, i - 1),
        C(5, i - 1) - C(5, i - 2),
        C(7, i - 2),
        -C(9, i - 3),
    ]
    out = [0]
    for j, x in enumerate(d, 1):
        n = i + 1 - j
        if n >= 0:
            out = add(out, [-x * C(n, k) for k in range(n + 1)])
    return [0] * (i - 1) + out

def jet(p: list[int], d: int) -> tuple[int, ...]:
    return tuple((p + [0] * (d + 1 - len(p)))[: d + 1])

def axis_profiles(K: list[list[int]], d: int):
    return tuple(
        (jet(K[2 * j], d), jet(K[2 * j + 1], d))
        for j in range(6)
    )

def orient_profile(P, pi):
    """pi maps a base axis to its spatial axis."""
    out = [None] * 6
    for base in range(6):
        out[pi[base]] = P[base]
    return tuple(out)

def orient_grade(pi):
    """Per-spatial-axis (positive,negative) R621 level increments."""
    out = [None] * 6
    for base in range(6):
        out[pi[base]] = (2 * base + 1, 2 * base + 2)
    return tuple(out)

def run():
    K = [frozen_K(i) for i in range(1, 13)]
    valuations = [next(i for i, c in enumerate(p) if c) for p in K]
    leaders = [K[i][valuations[i]] for i in range(12)]
    assert valuations == list(range(12))
    assert leaders == [2, -1, -8, -11, 6, 53, 106, 119, 83, 36, 9, 1]
    assert K[0] == [2, 3]
    assert K[1] == [0, -1, 4, 4]
    assert K[2][2] == -8

    perms = list(permutations(range(6)))
    steps = list(product(range(6), range(2)))
    assert len(perms) == factorial(6) == 720
    assert len(steps) == 12

    rows = []
    safe1 = 0
    safe2 = 0
    grade_witnesses = []

    for d in range(12):
        P = axis_profiles(K, d)
        zero = ((0,) * (d + 1), (0,) * (d + 1))
        k = sum(1 for p in P if p != zero)
        assert k == min(6, d // 2 + 1)

        multiplicities = {}
        for p in P:
            multiplicities[p] = multiplicities.get(p, 0) + 1

        orbit = {orient_profile(P, pi) for pi in perms}
        formula = factorial(6)
        for multiplicity in multiplicities.values():
            formula //= factorial(multiplicity)
        expected = factorial(6) // factorial(6 - k)
        assert len(orbit) == formula == expected

        classes = {}
        for pi in perms:
            classes.setdefault(orient_profile(P, pi), []).append(pi)

        # Exact future-append descent: equivalent orientations give identical
        # truncated K factors for every spatial signed step and every two-step
        # product. The ring projection is multiplicative, so this extends by
        # induction to arbitrary finite K-appended suffixes.
        for members in classes.values():
            rep = members[0]
            rep_base_at_spatial = [rep.index(x) for x in range(6)]
            for pi in members:
                cur_base_at_spatial = [pi.index(x) for x in range(6)]
                for spatial_axis, sign in steps:
                    i_rep = 2 * rep_base_at_spatial[spatial_axis] + sign
                    i_cur = 2 * cur_base_at_spatial[spatial_axis] + sign
                    assert jet(K[i_rep], d) == jet(K[i_cur], d)
                    safe1 += 1
                for (x1, s1), (x2, s2) in product(steps, repeat=2):
                    ir1 = 2 * rep_base_at_spatial[x1] + s1
                    ir2 = 2 * rep_base_at_spatial[x2] + s2
                    ic1 = 2 * cur_base_at_spatial[x1] + s1
                    ic2 = 2 * cur_base_at_spatial[x2] + s2
                    assert jet(mul(K[ir1], K[ir2]), d) == jet(mul(K[ic1], K[ic2]), d)
                    safe2 += 1

        grade_orbit = {
            (orient_profile(P, pi), orient_grade(pi))
            for pi in perms
        }
        assert len(grade_orbit) == 720

        # For d<=7 at least two axis profiles are zero. Swapping those hidden
        # base axes leaves the coefficient-only profile unchanged but changes
        # the one-step R621 grade q_pi(+e_x).
        if d <= 7:
            hidden = k  # zero-based first hidden base axis
            pi = list(range(6))
            pi[hidden], pi[hidden + 1] = pi[hidden + 1], pi[hidden]
            pi = tuple(pi)
            identity = tuple(range(6))
            assert orient_profile(P, identity) == orient_profile(P, pi)
            spatial_axis = hidden
            q_identity = orient_grade(identity)[spatial_axis][0]
            q_swapped = orient_grade(pi)[spatial_axis][0]
            assert q_identity != q_swapped
            grade_witnesses.append({
                "d": d,
                "hidden_base_axes_1based": [hidden + 1, hidden + 2],
                "spatial_axis_1based": spatial_axis + 1,
                "positive_grade_identity": q_identity,
                "positive_grade_swapped": q_swapped,
            })

        rows.append({
            "d": d,
            "visible_nonzero_axis_profiles": k,
            "profile_multiplicities": sorted(multiplicities.values(), reverse=True),
            "orbit_states": expected,
            "fixed_width_bits": (expected - 1).bit_length(),
            "stabilizer_states": factorial(6 - k),
            "grade_augmented_states": len(grade_orbit),
        })

    evidence = {
        "schema": "EM_R622_S6_TRUNCATED_PROFILE_ORBIT_EXACT_V1",
        "science_pin": {
            "commit": SCIENCE_COMMIT,
            "k_blob": K_BLOB,
            "theta": "0",
            "B0_coefficients_low_to_high": [1, 1],
        },
        "source_formula": "R462 frozen K binomial formula reconstructed independently from the pinned source blob",
        "K_t_valuations": valuations,
        "K_leading_coefficients": leaders,
        "K_polynomials_sha256": hashlib.sha256(json.dumps(K, separators=(",", ":")).encode("utf-8")).hexdigest(),
        "orientation_count": 720,
        "truncation_degrees_checked": list(range(12)),
        "orbit_rows": rows,
        "coefficient_only_single_append_factor_checks": safe1,
        "coefficient_only_two_append_product_checks": safe2,
        "grade_augmented_state_count_each_degree": 720,
        "grade_separation_witnesses_d0_to_d7": grade_witnesses,
        "pass": "R622_TRUNCATED_S6_PROFILE_ORBIT_AND_GRADE_BOUNDARY_PASS",
    }
    return evidence

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="R622_EVIDENCE.json")
    args = parser.parse_args()
    evidence = run()
    payload = json.dumps(evidence, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    Path(args.out).write_text(payload, encoding="utf-8")
    print(evidence["pass"])
    print("single_append_factor_checks", evidence["coefficient_only_single_append_factor_checks"])
    print("two_append_product_checks", evidence["coefficient_only_two_append_product_checks"])
    print("sha256", hashlib.sha256(payload.encode("utf-8")).hexdigest())

if __name__ == "__main__":
    main()
