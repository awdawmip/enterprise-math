#!/usr/bin/env python3
"""PREFIX-888: exact named-XOR axis-collision multiplicity and source-gap spectrum.

All counts use arbitrary-precision Python integers. No external dependencies.
Run: python3 PREFIX888_R6_AXIS_SPECTRUM.py > PREFIX888_R6_AXIS_SPECTRUM_RESULTS.json
"""
import json
from collections import Counter


def axis_count(p, q):
    """Number of distinct unordered legal trajectories sharing one exact endpoint
    and their other endpoint modulo odd q; also valid with time reversed."""
    assert p >= 1 and q >= 1 and q % 2 == 1
    n = 1 << p
    if q == 1:
        return n * p * (p + 1) // 2
    return (n // 2) * sum(
        (p - h) for h in range(1, p)
        if pow(2, h, q) in (1, q - 1)
    )


def gap_spectrum(p, q):
    """Exact counts by gap h=i-j between two different named source bits."""
    assert p >= 1 and q > 1 and q % 2 == 1
    n = 1 << p
    return {str(h): (n // 2) * (p - h)
            for h in range(1, p)
            if pow(2, h, q) in (1, q - 1)}


def directly_count_one_port(p, q):
    """Independent full enumeration of ordered XOR transitions per endpoint."""
    n = 1 << p
    total = 0
    for y in range(n):
        incoming = [y] + [y ^ (1 << i) for i in range(p)]
        counts = Counter(x % q for x in incoming)
        total += sum(c * (c - 1) // 2 for c in counts.values())
    return total


def directly_check_two_ports(p, q1, q2):
    """Cross-check full two-port spectrum and disjoint axis lower bound."""
    n = 1 << p
    fibers = Counter()
    for x in range(n):
        fibers[(x % q1, x % q2)] += 1
        for i in range(p):
            fibers[(x % q1, (x ^ (1 << i)) % q2)] += 1
    full = sum(c * (c - 1) // 2 for c in fibers.values())
    v = directly_count_one_port(p, q1)
    h = directly_count_one_port(p, q2)
    assert full >= v + h
    assert v == axis_count(p, q1)
    assert h == axis_count(p, q2)
    return full, v, h


def scan(p, lower, upper):
    assert lower % 2 == 1 and upper % 2 == 1 and lower <= upper
    m = (upper - lower) // 2 + 1
    positive_count = 0
    sum_one_port = 0
    maximum = -1
    max_moduli = []
    for q in range(lower, upper + 1, 2):
        a = axis_count(p, q)
        sum_one_port += a
        if a:
            positive_count += 1
        if a > maximum:
            maximum, max_moduli = a, [q]
        elif a == maximum:
            max_moduli.append(q)
    return {
        "lower_odd": lower, "upper_odd": upper, "moduli": m,
        "forcing_moduli": positive_count,
        "forcing_ordered_modulus_pairs": 2 * m * positive_count - positive_count ** 2,
        "sum_single_port_axis_pairs": sum_one_port,
        "total_axis_collision_pairs_across_all_ordered_port_choices": 2 * m * sum_one_port,
        "max_single_port_axis_pairs": maximum,
        "max_moduli": max_moduli
    }


def main():
    one_port_checks = 0
    for p in range(1, 9):
        for q in range(1, min(1 << p, 35), 2):
            assert axis_count(p, q) == directly_count_one_port(p, q)
            one_port_checks += 1

    two_port_checks = 0
    for p in range(1, 7):
        for q1 in range(1, min(1 << p, 25), 2):
            for q2 in range(1, min(1 << p, 25), 2):
                directly_check_two_ports(p, q1, q2)
                two_port_checks += 1

    p = 32
    full = scan(p, 1, (1 << 19) - 1)
    high = scan(p, (1 << 18) + 1, (1 << 19) - 1)
    assert one_port_checks == 82 and two_port_checks == 373
    assert (full["forcing_moduli"], high["forcing_moduli"]) == (385, 24)
    assert (full["forcing_ordered_modulus_pairs"],
            high["forcing_ordered_modulus_pairs"]) == (201702655, 6290880)
    assert (full["sum_single_port_axis_pairs"],
            high["sum_single_port_axis_pairs"]) == (
                15386720337920, 287762808832)
    assert (full["total_axis_collision_pairs_across_all_ordered_port_choices"],
            high["total_axis_collision_pairs_across_all_ordered_port_choices"]) == (
                8067072832527400960, 75435293758455808)
    result = {
        "schema": "PREFIX888_R6_EXACT_NAMED_XOR_AXIS_SPECTRUM_V1",
        "p": p, "n": 1 << p, "frozen_scientific_pin":
            "f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "full_19_bit_upper_bound_domain": full,
        "exact_19_bit_width_domain": high,
        "single_port_examples": {
            str(q): axis_count(p, q)
            for q in (1, 3, 5, 262145, 349525, 524285, 524287)
        },
        "validation": {
            "direct_one_port_cases": one_port_checks,
            "direct_complete_two_port_cases": two_port_checks,
            "disagreements": 0,
            "arithmetic": "exact integers only",
            "external_deps": []
        },
        "classification":
            "AUTHOR_PROVED / FINITE_EXACT_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED"
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
