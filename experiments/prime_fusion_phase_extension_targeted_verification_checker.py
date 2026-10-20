#!/usr/bin/env python3
"""Independent exact-integer audit for the Prime Fusion phase extension.

This program uses only Python's standard library.  It checks the polynomial
identities symbolically and then pressure-tests the retained modular claims.
Finite enumeration is evidence for, not a replacement for, the proofs in the
frozen research return.
"""

from __future__ import annotations

import argparse
import json
from math import gcd, isqrt
from pathlib import Path
from typing import Callable


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index, coefficient in enumerate(left):
        out[index] += coefficient
    for index, coefficient in enumerate(right):
        out[index] += coefficient
    return trim(out)


def poly_scale(poly: list[int], scalar: int) -> list[int]:
    return trim([scalar * coefficient for coefficient in poly])


def poly_mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def poly_derivative(poly: list[int]) -> list[int]:
    return trim([index * poly[index] for index in range(1, len(poly))])


def determinant_bareiss(matrix: list[list[int]]) -> int:
    """Exact determinant by fraction-free Gaussian elimination."""

    if not matrix:
        return 1
    work = [row[:] for row in matrix]
    size = len(work)
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        pivot_row = next(
            (row for row in range(pivot_index, size) if work[row][pivot_index]),
            None,
        )
        if pivot_row is None:
            return 0
        if pivot_row != pivot_index:
            work[pivot_index], work[pivot_row] = (
                work[pivot_row],
                work[pivot_index],
            )
            sign = -sign
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                )
                if pivot_index:
                    assert numerator % previous == 0
                    numerator //= previous
                work[row][column] = numerator
        for row in range(pivot_index + 1, size):
            work[row][pivot_index] = 0
        previous = pivot
    return sign * work[-1][-1]


def resultant(left: list[int], right: list[int]) -> int:
    """Resultant of low-to-high coefficient polynomials."""

    left = trim(left[:])
    right = trim(right[:])
    degree_left = len(left) - 1
    degree_right = len(right) - 1
    left_high = list(reversed(left))
    right_high = list(reversed(right))
    size = degree_left + degree_right
    matrix: list[list[int]] = []
    for shift in range(degree_right):
        matrix.append(
            [0] * shift + left_high + [0] * (size - shift - len(left_high))
        )
    for shift in range(degree_left):
        matrix.append(
            [0] * shift + right_high + [0] * (size - shift - len(right_high))
        )
    return determinant_bareiss(matrix)


def laurent_add(
    left: dict[int, int], right: dict[int, int]
) -> dict[int, int]:
    out = dict(left)
    for exponent, coefficient in right.items():
        out[exponent] = out.get(exponent, 0) + coefficient
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}


def laurent_mul(
    left: dict[int, int], right: dict[int, int]
) -> dict[int, int]:
    out: dict[int, int] = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = left_exponent + right_exponent
            out[exponent] = (
                out.get(exponent, 0) + left_coefficient * right_coefficient
            )
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def f_value(value: int) -> int:
    return value * value + 1


def g_value(value: int) -> int:
    return value * value + value + 1


def big_f_value(value: int) -> int:
    return f_value(value) * g_value(value)


def roots_mod(function: Callable[[int], int], modulus: int) -> list[int]:
    if modulus == 1:
        return [0]
    return [value for value in range(modulus) if function(value) % modulus == 0]


def crt_pair(left: int, left_modulus: int, right: int, right_modulus: int) -> int:
    assert gcd(left_modulus, right_modulus) == 1
    if right_modulus == 1:
        return left % left_modulus
    correction = ((right - left) * pow(left_modulus, -1, right_modulus)) % right_modulus
    return (left + left_modulus * correction) % (left_modulus * right_modulus)


def multiplicative_order(value: int, modulus: int, limit: int = 24) -> int:
    if modulus == 1:
        return 1
    assert gcd(value, modulus) == 1
    accumulator = 1
    for order in range(1, limit + 1):
        accumulator = (accumulator * value) % modulus
        if accumulator == 1:
            return order
    raise AssertionError((value, modulus, limit))


def pointed_cell(a: int, b: int) -> dict[str, int]:
    assert a > 0 and b > 0 and gcd(a, b) == 1
    n_channel = a * a + b * b
    c_channel = a * a - a * b + b * b
    assert gcd(n_channel, c_channel) == 1
    modulus = n_channel * c_channel
    assert gcd(b, modulus) == 1
    residue = (-a * pow(b, -1, modulus)) % modulus
    return {
        "a": a,
        "b": b,
        "N": n_channel,
        "C": c_channel,
        "H": modulus,
        "r": residue,
    }


def idempotent_from_root(residue: int, modulus: int) -> int:
    inverse = pow(residue, -1, modulus)
    return (-(residue + inverse)) % modulus


def shared_positive_pairs(n_channel: int, c_channel: int) -> set[tuple[int, int]]:
    pairs: set[tuple[int, int]] = set()
    limit = isqrt(n_channel)
    for left in range(1, limit + 1):
        for right in range(1, limit + 1):
            if (
                left * left + right * right == n_channel
                and left * left - left * right + right * right == c_channel
            ):
                pairs.add((left, right))
    return pairs


def audit_symbolic_identities() -> dict[str, object]:
    f_poly = [1, 0, 1]
    g_poly = [1, 1, 1]
    fused = poly_mul(f_poly, g_poly)
    bezout = poly_add(poly_mul([1, 1], f_poly), poly_scale(poly_mul([0, 1], g_poly), -1))
    assert bezout == [1]
    res_fg = resultant(f_poly, g_poly)
    assert res_fg == 1
    fused_degree = len(fused) - 1
    disc_fused = (
        (-1) ** (fused_degree * (fused_degree - 1) // 2)
        * resultant(fused, poly_derivative(fused))
        // fused[-1]
    )
    assert fused == [1, 1, 2, 1, 1]
    assert disc_fused == 12

    t = {1: 1, -1: 1}
    trace_side = laurent_add(laurent_mul(t, t), t)
    divided_fused = {-2: 1, -1: 1, 0: 2, 1: 1, 2: 1}
    assert trace_side == divided_fused
    return {
        "bezout_identity": "(X+1)(X^2+1)-X(X^2+X+1)=1",
        "fused_coefficients_low_to_high": fused,
        "resultant_f_g": res_fg,
        "discriminant_fused": disc_fused,
        "laurent_identity": "X^-2 F(X)=(X+X^-1)^2+(X+X^-1)",
        "status": "PASS",
    }


def audit_all_small_moduli(max_modulus: int) -> dict[str, object]:
    root_count = 0
    moduli_with_roots = 0
    nonsquarefree_examples: list[dict[str, object]] = []
    for modulus in range(2, max_modulus + 1):
        roots = roots_mod(big_f_value, modulus)
        if roots:
            moduli_with_roots += 1
        for residue in roots:
            root_count += 1
            assert gcd(residue, modulus) == 1
            inverse_formula = (-(residue**3 + residue**2 + 2 * residue + 1)) % modulus
            assert residue * inverse_formula % modulus == 1 % modulus
            e = idempotent_from_root(residue, modulus)
            assert (e * e - e) % modulus == 0
            assert (e - (residue + 1) * f_value(residue)) % modulus == 0
            assert (e - 1 - residue * g_value(residue)) % modulus == 0
            left_factor = gcd(e, modulus)
            right_factor = gcd(e - 1, modulus)
            assert gcd(left_factor, right_factor) == 1
            assert left_factor * right_factor == modulus
        square_divisor = next(
            (prime for prime in range(2, isqrt(modulus) + 1) if modulus % (prime * prime) == 0),
            None,
        )
        if roots and square_divisor is not None and len(nonsquarefree_examples) < 8:
            nonsquarefree_examples.append(
                {"H": modulus, "roots": roots, "square_divisor": square_divisor}
            )
    return {
        "range": [2, max_modulus],
        "moduli_with_roots": moduli_with_roots,
        "roots_checked": root_count,
        "nonsquarefree_examples": nonsquarefree_examples,
        "status": "PASS",
    }


def audit_cells(cell_bound: int, root_modulus_cap: int) -> dict[str, object]:
    primitive_count = 0
    dual_prime_count = 0
    exhaustive_root_cells = 0
    composite_order12_count = 0
    composite_orbit_incomplete: list[dict[str, object]] = []
    dual_full_root_extras: list[dict[str, object]] = []

    for a in range(1, cell_bound + 1):
        for b in range(1, cell_bound + 1):
            if gcd(a, b) != 1:
                continue
            primitive_count += 1
            cell = pointed_cell(a, b)
            n_channel = cell["N"]
            c_channel = cell["C"]
            modulus = cell["H"]
            residue = cell["r"]
            assert big_f_value(residue) % modulus == 0

            # V6 pointed factor recovery, including the C=1 degeneracy.
            e = idempotent_from_root(residue, modulus)
            assert gcd(e, modulus) == n_channel
            assert gcd(e - 1, modulus) == c_channel

            # Swap keeps the channels and inverts the marked residue.
            swapped = pointed_cell(b, a)
            assert swapped["N"] == n_channel and swapped["C"] == c_channel
            assert swapped["r"] == pow(residue, -1, modulus)

            # The local sixth-power congruences require no primality.
            sixth = pow(residue, 6, modulus)
            assert (sixth + 1) % n_channel == 0
            assert (sixth - 1) % c_channel == 0
            plus_gcd = gcd(modulus, sixth + 1)
            minus_gcd = gcd(modulus, sixth - 1)
            assert plus_gcd == n_channel * gcd(c_channel, 2)
            assert minus_gcd == c_channel * gcd(n_channel, 2)
            assert c_channel % 2 == 1

            if n_channel > 2 and c_channel > 3:
                assert multiplicative_order(residue % n_channel, n_channel) == 4
                assert multiplicative_order(residue % c_channel, c_channel) == 3
                assert multiplicative_order(residue, modulus) == 12
                if not (is_prime(n_channel) and is_prime(c_channel)):
                    composite_order12_count += 1

            # Directly enumerate every root only when the full modulus is manageable.
            if a <= b and modulus <= root_modulus_cap:
                exhaustive_root_cells += 1
                f_roots = roots_mod(f_value, n_channel)
                g_roots = roots_mod(g_value, c_channel)
                mixed_by_crt = {
                    crt_pair(left, n_channel, right, c_channel)
                    for left in f_roots
                    for right in g_roots
                }
                mixed_by_scan = {
                    value
                    for value in range(modulus)
                    if f_value(value) % n_channel == 0
                    and g_value(value) % c_channel == 0
                }
                assert mixed_by_crt == mixed_by_scan
                assert all(big_f_value(value) % modulus == 0 for value in mixed_by_scan)
                full_roots = set(roots_mod(big_f_value, modulus))
                assert mixed_by_scan <= full_roots

                if n_channel > 2 and c_channel > 3:
                    orbit = {pow(residue, exponent, modulus) for exponent in (1, 5, 7, 11)}
                    assert len(orbit) == 4
                    assert orbit <= mixed_by_scan
                    if len(f_roots) == 2 and len(g_roots) == 2:
                        assert orbit == mixed_by_scan
                    elif not (is_prime(n_channel) and is_prime(c_channel)):
                        composite_orbit_incomplete.append(
                            {
                                "a": a,
                                "b": b,
                                "N": n_channel,
                                "C": c_channel,
                                "H": modulus,
                                "orbit_cardinality": len(orbit),
                                "mixed_locus_cardinality": len(mixed_by_scan),
                            }
                        )

            if is_prime(n_channel) and is_prime(c_channel) and n_channel > 3 and c_channel > 3:
                dual_prime_count += 1
                assert multiplicative_order(residue % n_channel, n_channel) == 4
                assert multiplicative_order(residue % c_channel, c_channel) == 3
                assert multiplicative_order(residue, modulus) == 12
                orbit = {pow(residue, exponent, modulus) for exponent in (1, 5, 7, 11)}
                assert len(orbit) == 4
                expected_local_f = {residue % n_channel, pow(residue, -1, n_channel)}
                expected_local_g = {residue % c_channel, pow(residue, -1, c_channel)}
                assert len(expected_local_f) == 2 and len(expected_local_g) == 2
                mixed_by_crt = {
                    crt_pair(left, n_channel, right, c_channel)
                    for left in expected_local_f
                    for right in expected_local_g
                }
                assert orbit == mixed_by_crt
                assert shared_positive_pairs(n_channel, c_channel) == {(a, b), (b, a)}
                assert {residue, pow(residue, -1, modulus)} == {
                    pow(residue, 1, modulus),
                    pow(residue, 11, modulus),
                }
                other_pair = {pow(residue, 5, modulus), pow(residue, 7, modulus)}
                assert other_pair.isdisjoint({residue, pow(residue, -1, modulus)})
                for phase in orbit:
                    assert pow(phase, 6, n_channel) == n_channel - 1
                    assert pow(phase, 6, c_channel) == 1
                    assert gcd(modulus, pow(phase, 6, modulus) + 1) == n_channel
                    assert gcd(modulus, pow(phase, 6, modulus) - 1) == c_channel

                if a <= b and modulus <= root_modulus_cap:
                    full_roots = set(roots_mod(big_f_value, modulus))
                    extras = sorted(full_roots - orbit)
                    if extras:
                        dual_full_root_extras.append(
                            {
                                "a": a,
                                "b": b,
                                "p": n_channel,
                                "q": c_channel,
                                "H": modulus,
                                "r": residue,
                                "mixed_roots": sorted(orbit),
                                "extra_F_roots": extras,
                                "full_F_root_count": len(full_roots),
                            }
                        )

    # Exact named pressure controls.
    smallest_dual_scope = pointed_cell(2, 3)
    assert smallest_dual_scope == {"a": 2, "b": 3, "N": 13, "C": 7, "H": 91, "r": 60}
    mixed_91 = sorted(pow(60, exponent, 91) for exponent in (1, 5, 7, 11))
    full_91 = roots_mod(big_f_value, 91)
    assert mixed_91 == [18, 44, 60, 86]
    assert full_91 == [9, 16, 18, 44, 60, 74, 81, 86]

    parity_control = pointed_cell(1, 3)
    sixth_70 = pow(parity_control["r"], 6, parity_control["H"])
    assert parity_control == {"a": 1, "b": 3, "N": 10, "C": 7, "H": 70, "r": 23}
    assert gcd(70, sixth_70 + 1) == 10
    assert gcd(70, sixth_70 - 1) == 14

    composite_orbit_control = pointed_cell(4, 7)
    f_roots_65 = roots_mod(f_value, 65)
    g_roots_37 = roots_mod(g_value, 37)
    mixed_2405 = {
        crt_pair(left, 65, right, 37)
        for left in f_roots_65
        for right in g_roots_37
    }
    orbit_2405 = {
        pow(composite_orbit_control["r"], exponent, 2405)
        for exponent in (1, 5, 7, 11)
    }
    assert len(f_roots_65) == 4 and len(g_roots_37) == 2
    assert len(mixed_2405) == 8 and len(orbit_2405) == 4
    assert orbit_2405 < mixed_2405

    degenerate = pointed_cell(1, 1)
    degenerate_e = idempotent_from_root(degenerate["r"], degenerate["H"])
    degenerate_sixth = pow(degenerate["r"], 6, degenerate["H"])
    assert degenerate == {"a": 1, "b": 1, "N": 2, "C": 1, "H": 2, "r": 1}
    assert gcd(degenerate_e, 2) == 2 and gcd(degenerate_e - 1, 2) == 1
    assert gcd(2, degenerate_sixth - 1) == 2  # Not C=1.

    nonsquarefree = pointed_cell(3, 4)
    assert nonsquarefree["N"] == 25 and nonsquarefree["C"] == 13
    assert roots_mod(big_f_value, nonsquarefree["H"])

    return {
        "cell_range": {"a": [1, cell_bound], "b": [1, cell_bound]},
        "primitive_cells_checked": primitive_count,
        "dual_prime_cells_checked_ordered": dual_prime_count,
        "composite_cells_with_order_12_checked_ordered": composite_order12_count,
        "full_root_enumeration": {
            "H_cap": root_modulus_cap,
            "unordered_cells_checked": exhaustive_root_cells,
        },
        "V10_scope_counterexample": {
            "cell": [2, 3],
            "p": 13,
            "q": 7,
            "H": 91,
            "r": 60,
            "channel_oriented_mixed_roots": mixed_91,
            "full_F_roots": full_91,
            "extra_F_roots": sorted(set(full_91) - set(mixed_91)),
        },
        "dual_prime_full_root_extra_examples": dual_full_root_extras[:12],
        "composite_orbit_control": {
            "cell": [4, 7],
            "N": 65,
            "C": 37,
            "H": 2405,
            "local_f_root_count": len(f_roots_65),
            "local_g_root_count": len(g_roots_37),
            "power_orbit_count": len(orbit_2405),
            "mixed_locus_count": len(mixed_2405),
        },
        "additional_composite_orbit_incomplete_examples": composite_orbit_incomplete[:12],
        "V11_even_composite_control": {
            "cell": [1, 3],
            "N": 10,
            "C": 7,
            "H": 70,
            "r": parity_control["r"],
            "r6": sixth_70,
            "gcd_H_r6_plus_1": gcd(70, sixth_70 + 1),
            "gcd_H_r6_minus_1": gcd(70, sixth_70 - 1),
        },
        "degenerate_control": {
            "cell": [1, 1],
            "N": 2,
            "C": 1,
            "H": 2,
            "V6_recovery": [gcd(degenerate_e, 2), gcd(degenerate_e - 1, 2)],
            "V11_minus_gcd": gcd(2, degenerate_sixth - 1),
        },
        "nonsquarefree_control": {
            "cell": [3, 4],
            "N": nonsquarefree["N"],
            "C": nonsquarefree["C"],
            "H": nonsquarefree["H"],
        },
        "status": "PASS",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell-bound", type=int, default=80)
    parser.add_argument("--root-modulus-cap", type=int, default=5000)
    parser.add_argument("--universal-modulus", type=int, default=400)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    assert arguments.cell_bound >= 7
    assert arguments.root_modulus_cap >= 2405
    assert arguments.universal_modulus >= 2

    result = {
        "schema": "PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_CHECK_V1",
        "parameters": {
            "cell_bound": arguments.cell_bound,
            "root_modulus_cap": arguments.root_modulus_cap,
            "universal_modulus": arguments.universal_modulus,
        },
        "symbolic_exact_checks": audit_symbolic_identities(),
        "all_F_roots_small_moduli": audit_all_small_moduli(arguments.universal_modulus),
        "cell_audit": audit_cells(arguments.cell_bound, arguments.root_modulus_cap),
        "final_status": "PASS",
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if arguments.output is not None:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(rendered, encoding="utf-8", newline="\n")
    print(rendered, end="")


if __name__ == "__main__":
    main()
