#!/usr/bin/env python3
"""Exact finite checks for a typed signed-X6 two-axis PathSqrt fibre extension.

Historical R063 sector semantics remain unchanged. These tests concern one
ordered pair of signed native axes with four other relative components zero.
No native two-dimensional plane or additional spatial axes are introduced.
"""
from math import comb, isqrt


def positive_sector(r):
    out = []
    for a in range(r + 1):
        b2 = r * r - a * a
        b = isqrt(b2)
        if b * b == b2:
            out.append((a, b))
    return out


def signed_shell_independent(r):
    out = set()
    for x in range(-r, r + 1):
        y2 = r * r - x * x
        y = isqrt(y2)
        if y * y == y2:
            out.add((x, y))
            out.add((x, -y))
    return out


def weight(a, b):
    return (2 if a else 1) * (2 if b else 1)


def check(r):
    sector = positive_sector(r)
    shell = signed_shell_independent(r)
    asserted_shell = {
        (sx * a, sy * b)
        for a, b in sector
        for sx in (-1, 1)
        for sy in (-1, 1)
    }
    assert shell == asserted_shell
    assert len(shell) == sum(weight(a, b) for a, b in sector)
    path_count = sum(comb(abs(x) + abs(y), abs(x)) for x, y in shell)
    weighted_count = sum(weight(a, b) * comb(a + b, a) for a, b in sector)
    assert path_count == weighted_count
    # Two factorized test observables: unsigned sector; signed endpoint.
    unsigned_obs = sum((abs(x) + 2 * abs(y)) * comb(abs(x) + abs(y), abs(x)) for x, y in shell)
    unsigned_grouped = sum(weight(a, b) * (a + 2 * b) * comb(a + b, a) for a, b in sector)
    assert unsigned_obs == unsigned_grouped
    signed_obs = sum((x - y) * comb(abs(x) + abs(y), abs(x)) for x, y in shell)
    assert signed_obs == 0  # sign reflection symmetry, verified independently
    return len(sector), len(shell), path_count


def main():
    for r in range(1, 129):
        check(r)
    assert positive_sector(50) == [
        (0, 50), (14, 48), (30, 40), (40, 30), (48, 14), (50, 0)
    ]
    original = sum(comb(a + b, a) for a, b in positive_sector(50))
    sector_count, endpoint_count, signed_count = check(50)
    assert (sector_count, endpoint_count) == (6, 20)
    assert original == 110695538274255714208
    assert signed_count == 442782153097022856828
    negative_x = sum(
        comb(abs(x) + abs(y), abs(x))
        for x, y in signed_shell_independent(50) if x < 0
    )
    assert negative_x == 221391076548511428413
    assert signed_count - sector_count == 442782153097022856822
    assert signed_count - endpoint_count == 442782153097022856808
    assert endpoint_count - sector_count == 14
    print({
        'radii': 128, 'r50_positive_trace_fibers': sector_count,
        'r50_signed_endpoint_fibers': endpoint_count,
        'r50_positive_paths': original, 'r50_signed_paths': signed_count,
        'r50_negative_x_paths': negative_x,
        'r50_unsigned_trace_defect': signed_count - sector_count,
        'r50_signed_trace_defect': signed_count - endpoint_count,
        'status': 'EXACT_INTEGER_CHECKS_PASS',
    })


if __name__ == '__main__':
    main()
