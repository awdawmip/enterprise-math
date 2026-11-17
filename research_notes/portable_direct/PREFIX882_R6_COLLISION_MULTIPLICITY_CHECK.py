#!/usr/bin/env python3
"""PREFIX-882: exact collision-pair multiplicity for named XOR observations.
Python >=3.9, standard library only. All arithmetic is exact integers.
"""
import json
from collections import defaultdict

def deltas(p):
    return [0] + [s * (1 << i) for i in range(p) for s in (1, -1)]

def count_witnesses(p, a, d, e):
    """Number of valid starting states u for (u,u+d), (u+a,u+a+e).
    a >= 0, d/e are zero or signed binary single-bit changes.
    """
    assert p >= 1 and 0 <= a < (1 << p)
    assert d in deltas(p) and e in deltas(p)
    n = 1 << p
    L = max(0, -a, -d, -a-e)
    U = min(n-1, n-1-a, n-1-d, n-1-a-e)
    if L > U:
        return 0
    states = {(0, 0, 0): 1}
    for i in range(p):
        ai, li, ui = (a >> i) & 1, (L >> i) & 1, (U >> i) & 1
        next_states = defaultdict(int)
        for (carry, borrow_l, borrow_u), count in states.items():
            for xi in (0, 1):
                sm = xi + ai + carry
                yi = sm & 1
                if d != 0 and abs(d) == (1 << i) and xi != (0 if d > 0 else 1):
                    continue
                if e != 0 and abs(e) == (1 << i) and yi != (0 if e > 0 else 1):
                    continue
                state = (sm >> 1,
                         int(xi - li - borrow_l < 0),
                         int(ui - xi - borrow_u < 0))
                next_states[state] += count
        states = next_states
    return sum(count for (carry, bl, bu), count in states.items()
               if bl == 0 and bu == 0)

def count_direct(p, a, d, e):
    n = 1 << p
    return sum(
        0 <= u+d < n and 0 <= u+a < n and 0 <= u+a+e < n
        and (d == 0 or u+d == (u ^ abs(d)))
        and (e == 0 or u+a+e == ((u+a) ^ abs(e)))
        for u in range(n)
    )

def collision_pair_count(p, q1, q2):
    n, ds = 1 << p, deltas(p)
    cross = same_start = 0
    for a in range(q1, n, q1):
        for d in ds:
            for e in ds:
                if (a + e - d) % q2 == 0:
                    cross += count_witnesses(p, a, d, e)
    for j, d in enumerate(ds):
        for e in ds[j+1:]:
            if (e-d) % q2 == 0:
                same_start += count_witnesses(p, 0, d, e)
    return cross + same_start, cross, same_start

def direct_pair_count(p, q1, q2):
    n = 1 << p
    fiber = defaultdict(int)
    for u in range(n):
        for index in (-1, *range(p)):
            v = u if index == -1 else u ^ (1 << index)
            fiber[(u % q1, v % q2)] += 1
    return sum(m * (m-1) // 2 for m in fiber.values())

def bit_zero_prefix(t, h):
    assert t >= 0 and h > 0 and h & (h-1) == 0
    return (t // (2*h)) * h + min(h, t % (2*h))

def main():
    tests = []
    for p in range(1, 7):
        ds, checked = deltas(p), 0
        for a in range(1 << p):
            for d in ds:
                for e in ds:
                    observed = count_witnesses(p, a, d, e)
                    expected = count_direct(p, a, d, e)
                    assert observed == expected, (p, a, d, e, observed, expected)
                    checked += 1
        tests.append({"p": p, "parameter_tuples": checked, "mismatches": 0})
    pair_tests = []
    for p, bound in ((3, 9), (4, 15), (5, 17), (6, 13)):
        checked, nonzero = 0, 0
        for q1 in range(1, bound + 1, 2):
            for q2 in range(1, bound + 1, 2):
                dp, _, _ = collision_pair_count(p, q1, q2)
                brute = direct_pair_count(p, q1, q2)
                assert dp == brute, (p, q1, q2, dp, brute)
                checked += 1
                nonzero += dp > 0
        pair_tests.append({"p": p, "odd_modulus_max": bound,
                           "pairs_checked": checked, "nonzero_collisions": nonzero,
                           "mismatches": 0})
    n, q1, q2 = 1 << 32, (1 << 19)-1, (1 << 19)-3
    family, total = [], 0
    for j in range(14):
        k = 1 << j
        a, b = k*q1, k*q2
        h = a-b
        assert a < n and h == 1 << (j+1)
        exact_count = bit_zero_prefix(n-a, h)
        dp_count = count_witnesses(32, a, h, 0)
        assert dp_count == exact_count
        family.append({"k": k, "a": a, "b": b,
                       "difference": h, "number_of_collision_pairs": exact_count})
        total += exact_count
    assert total == 25770082303
    print(json.dumps({
        "schema": "PREFIX882_R6_COLLISION_MULTIPLICITY_V1",
        "exact_count_dp_tests": tests,
        "unordered_pair_crosschecks": pair_tests,
        "p32_example": {
            "p": 32, "q1": q1, "q2": q2,
            "event_count": 33*n,
            "disjoint_power_of_two_multiplier_families": family,
            "certified_collision_pairs_lower_bound": total,
            "mean_alternative_events_lower_bound_numerator": 2*total,
            "mean_alternative_events_lower_bound_denominator": 33*n
        },
        "status": "ALL_EXACT_ASSERTIONS_PASSED"
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
