#!/usr/bin/env python3
"""Exact finite stress checks for RS-ADDMUL-SUM-PRODUCT-OBSTRUCTION-STRESS-TEST.

This is a task-local research checker.  It reuses Enterprise Math's canonical
finite operation-family quotient test by currying binary ring operations into
families of unary translations.  It does not create a new general toolbox API.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from enterprise_math.operation_quotient import family_descends


def zn_translation_family(n: int) -> tuple[tuple[int, ...], dict[str, dict[int, int]]]:
    if n < 2:
        raise ValueError("n must be at least 2")
    domain = tuple(range(n))
    operations: dict[str, dict[int, int]] = {}
    for a in domain:
        operations[f"add:{a}"] = {x: (a + x) % n for x in domain}
        operations[f"mul:{a}"] = {x: (a * x) % n for x in domain}
    return domain, operations


def ring_table_failures(n: int, m: int, map_fn) -> dict[str, int]:
    add_failures = 0
    mul_failures = 0
    for a, b in product(range(n), repeat=2):
        if map_fn((a + b) % n) != (map_fn(a) + map_fn(b)) % m:
            add_failures += 1
        if map_fn((a * b) % n) != (map_fn(a) * map_fn(b)) % m:
            mul_failures += 1
    return {"add": add_failures, "mul": mul_failures}


def fiber_profile(values, map_fn) -> dict[str, int]:
    counts = Counter(map_fn(value) for value in values)
    return {
        "image_size": len(counts),
        "max_fiber": max(counts.values()) if counts else 0,
        "collisions": sum(count - 1 for count in counts.values()),
    }


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("v2 checker is restricted to positive integers")
    value = n
    exponent = 0
    while value % 2 == 0:
        exponent += 1
        value //= 2
    return exponent


def integer_sumset(values: set[int]) -> set[int]:
    return {a + b for a in values for b in values}


def integer_productset(values: set[int]) -> set[int]:
    return {a * b for a in values for b in values}


def main() -> None:
    domain8, operations8 = zn_translation_family(8)

    identity_partition = {x: x for x in domain8}
    parity_partition = {x: x % 2 for x in domain8}
    residue3_partition = {x: x % 3 for x in domain8}

    assert family_descends(domain8, operations8, identity_partition)
    assert family_descends(domain8, operations8, parity_partition)
    assert not family_descends(domain8, operations8, residue3_partition)

    parity_failures = ring_table_failures(8, 2, lambda x: x % 2)
    residue3_failures = ring_table_failures(8, 3, lambda x: x % 3)
    assert parity_failures == {"add": 0, "mul": 0}
    assert residue3_failures == {"add": 28, "mul": 25}

    # Same-law zero witness: x+0=x while x*0=0.  Any single target law used
    # exactly for both transports forces T(x)=T(0) for every x.
    forced_same_law_collisions = sum(
        int(((x + 0) % 8) != ((x * 0) % 8)) for x in domain8
    )
    assert forced_same_law_collisions == 7

    # p-adic valuation is a legitimate lossy bridge: multiplication transports
    # exactly to addition, while the addition skeleton min(v(a),v(b)) has
    # cancellation defects.
    valuation_mul_failures = 0
    valuation_min_failures = 0
    for a, b in product(range(1, 65), repeat=2):
        valuation_mul_failures += int(v2(a * b) != v2(a) + v2(b))
        valuation_min_failures += int(v2(a + b) != min(v2(a), v2(b)))
    assert valuation_mul_failures == 0
    assert valuation_min_failures == 1366
    assert v2(1 + 1) == 1 > min(v2(1), v2(1))

    # Exponential coordinate: addition -> multiplication is exact, but the same
    # target multiplication does not also transport source multiplication.
    exp_add_failures = 0
    exp_mul_failures = 0
    for a, b in product(range(9), repeat=2):
        ta, tb = 2**a, 2**b
        exp_add_failures += int(2 ** (a + b) != ta * tb)
        exp_mul_failures += int(2 ** (a * b) != ta * tb)
    assert exp_add_failures == 0
    assert exp_mul_failures == 79

    # Discrete logarithm in F_7^*: exact multiplication -> Z/6 addition.
    # Addition is not closed (six pairs sum to zero) and, where defined, does
    # not obey the same additive target law.
    p = 7
    primitive = 3
    log_table = {pow(primitive, e, p): e for e in range(p - 1)}
    assert len(log_table) == p - 1
    discrete_log_mul_failures = 0
    discrete_log_add_undefined = 0
    discrete_log_add_same_law_failures = 0
    for a, b in product(range(1, p), repeat=2):
        discrete_log_mul_failures += int(
            log_table[(a * b) % p]
            != (log_table[a] + log_table[b]) % (p - 1)
        )
        s = (a + b) % p
        if s == 0:
            discrete_log_add_undefined += 1
        else:
            discrete_log_add_same_law_failures += int(
                log_table[s]
                != (log_table[a] + log_table[b]) % (p - 1)
            )
    assert discrete_log_mul_failures == 0
    assert discrete_log_add_undefined == 6
    assert discrete_log_add_same_law_failures == 25

    # Exact set-growth distortion under a noninjective quotient.
    A = set(range(1, 13))
    sumset = integer_sumset(A)
    productset = integer_productset(A)
    assert len(A) == 12 and len(sumset) == 23 and len(productset) == 59
    sum_parity = fiber_profile(sumset, lambda n: n % 2)
    prod_parity = fiber_profile(productset, lambda n: n % 2)
    assert sum_parity == {"image_size": 2, "max_fiber": 12, "collisions": 21}
    assert prod_parity == {"image_size": 2, "max_fiber": 39, "collisions": 57}

    result = {
        "schema": "ADDMUL_BRIDGE_STRESS_CHECK_V1",
        "status": "PASS",
        "operation_quotient_reuse": {
            "identity_Z8": True,
            "parity_Z8_to_Z2": True,
            "residue3_Z8_to_Z3": False,
        },
        "finite_ring_table_failures": {
            "parity_Z8_to_Z2": parity_failures,
            "residue3_Z8_to_Z3": residue3_failures,
        },
        "elementary_obstruction": {
            "same_law_forced_nonzero_collisions_on_Z8": forced_same_law_collisions,
        },
        "pseudo_bridge_checks": {
            "v2": {
                "multiplication_transport_failures_1_to_64": valuation_mul_failures,
                "min_addition_skeleton_failures_1_to_64": valuation_min_failures,
            },
            "exp2": {
                "addition_to_multiplication_failures_0_to_8": exp_add_failures,
                "forced_source_multiplication_to_same_target_law_failures_0_to_8": exp_mul_failures,
            },
            "F7_discrete_log": {
                "multiplication_transport_failures": discrete_log_mul_failures,
                "addition_undefined_pairs": discrete_log_add_undefined,
                "addition_same_law_failures_where_defined": discrete_log_add_same_law_failures,
            },
        },
        "growth_packet": {
            "A_size": len(A),
            "A_plus_A_size": len(sumset),
            "A_times_A_size": len(productset),
            "parity_sum_image": sum_parity,
            "parity_product_image": prod_parity,
        },
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
