#!/usr/bin/env python3
"""Exact finite checks for the moving-cutoff tail geometry.

The structural assertions use integers and ``Fraction`` only.  They show that
the cutoff tail is not geometrically local at the current scale: every tail
endpoint is transported to a strictly lower triangular scale.
"""

from __future__ import annotations

from fractions import Fraction


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def prime_power_base(n: int) -> int | None:
    if n < 2:
        return None
    for p in range(2, n + 1):
        if not is_prime(p):
            continue
        q = p
        while q < n:
            q *= p
        if q == n:
            return p
    return None


def prime_powers(limit: int) -> list[int]:
    return [n for n in range(2, limit + 1) if prime_power_base(n) is not None]


def weight(a: int) -> Fraction:
    p = prime_power_base(a)
    assert p is not None
    return Fraction(p, a)


def q(a: int, n: int) -> int:
    return n // a


def field(n: int) -> Fraction:
    return Fraction(
        ((43 * n * n + 17 * n + 3) % 131) - 65,
        ((31 * n + 13) % 37) + 1,
    )


def defect(a: int, n: int) -> Fraction:
    return field(n) + field(q(a, n))


def residual(actions: list[int], n: int) -> Fraction:
    return sum((weight(c) * defect(c, n) for c in actions), Fraction(0, 1))


def check_tail_landing(max_y: int = 180) -> None:
    for y in range(2, max_y + 1):
        n = y * y
        for a in prime_powers(y):
            m = q(a, n)
            assert m >= y
            for c in prime_powers(m):
                if c <= y:
                    continue
                endpoint = q(c, m)
                assert endpoint == q(a * c, n)
                assert endpoint <= (y - 1) // a, (y, a, c, endpoint)
                assert endpoint < y
                if a >= 2:
                    assert endpoint <= (y - 1) // 2


def check_residual_cutoff_decomposition(max_y: int = 120) -> None:
    for y in range(2, max_y + 1):
        n = y * y
        global_actions = prime_powers(y)
        for a in global_actions:
            m = q(a, n)
            full_actions = prime_powers(m)
            tail_actions = [c for c in full_actions if c > y]
            assert residual(full_actions, m) == (
                residual(global_actions, m) + residual(tail_actions, m)
            )

            tail_vertex_mass = sum(
                (weight(c) for c in tail_actions), Fraction(0, 1)
            )
            tail_endpoint_sum = sum(
                (weight(c) * field(q(c, m)) for c in tail_actions),
                Fraction(0, 1),
            )
            assert residual(tail_actions, m) == (
                tail_vertex_mass * field(m) + tail_endpoint_sum
            )


def check_pair_tail_difference(max_y: int = 80) -> None:
    for y in range(3, max_y + 1):
        n = y * y
        actions = prime_powers(y)
        for a in actions:
            for b in actions:
                ma = q(a, n)
                mb = q(b, n)
                tail_a = [c for c in prime_powers(ma) if c > y]
                tail_b = [c for c in prime_powers(mb) if c > y]
                lhs = residual(actions, ma) - residual(actions, mb)
                rhs = (
                    residual(prime_powers(ma), ma)
                    - residual(prime_powers(mb), mb)
                    - residual(tail_a, ma)
                    + residual(tail_b, mb)
                )
                assert lhs == rhs


def main() -> None:
    check_tail_landing()
    check_residual_cutoff_decomposition()
    check_pair_tail_difference()
    print("moving-cutoff tail checks: PASS")


if __name__ == "__main__":
    main()
