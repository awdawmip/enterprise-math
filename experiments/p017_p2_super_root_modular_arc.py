"""Finite verifier for the P017 super-root modular-arc carry law.

Research owner artifact only.  It checks P2-R17--P2-R21 from
`docs/P017_P2_CHEN_CARRY_BRIDGE_SUPPLEMENT_04_20260824.md`.
It is not an asymptotic proof and makes no all-K P2 claim.
"""

from __future__ import annotations

from cmath import exp
from math import floor, isqrt, pi, sqrt


def hit_count(k: int, m: int) -> int:
    if not (isinstance(k, int) and not isinstance(k, bool) and k >= 1):
        raise ValueError("k must be a positive integer")
    if not (isinstance(m, int) and not isinstance(m, bool) and m >= 1):
        raise ValueError("m must be a positive integer")
    return (k * k + 2 * k) // m - (k * k) // m


def odd_quotient_count(k: int, m: int) -> int:
    return hit_count(k, m) - hit_count(k, 2 * m)


def modular_arc_residue(k: int, m: int) -> int:
    if not (k < m <= k * k + 2 * k):
        raise ValueError("m must lie in the super-root basin range")
    return (k * k + m) % (2 * m)


def modular_arc_count(k: int, m: int) -> int:
    residue = modular_arc_residue(k, m)
    return int(residue >= 2 * (m - k))


def direct_odd_count(k: int, m: int) -> int:
    lower = k * k // m + 1
    upper = (k * k + 2 * k) // m
    return sum(quotient % 2 for quotient in range(lower, upper + 1))


def odd_excess_layer(k: int, m: int) -> tuple[int, int, int]:
    if m % 2 == 0:
        raise ValueError("m must be odd")
    a = m - k
    layer = a * a // (2 * m)
    corridor = a * a - 2 * layer * m
    return a, layer, corridor


def layer_root(k: int, layer: int) -> float:
    if layer < 0:
        raise ValueError("layer must be nonnegative")
    if layer == 0:
        return 0.0
    return layer + sqrt(layer * layer + 2 * layer * k)


def parity_ceil(value: float, required_parity: int) -> int:
    candidate = max(1, int(value))
    if candidate < value:
        candidate += 1
    if candidate % 2 != required_parity % 2:
        candidate += 1
    return candidate


def predicted_layer_miss(k: int, layer: int) -> int | None:
    required_parity = 1 - k
    if layer == 0:
        candidate = 1
    else:
        candidate = parity_ceil(layer_root(k, layer), required_parity)
    m = k + candidate
    corridor = candidate * candidate - 2 * layer * m
    if 0 <= corridor < 2 * candidate:
        return candidate
    return None


def miss_count_bound(k: int, additive_width: int) -> int:
    return 1 + additive_width * additive_width // (2 * (k + additive_width))


def l1_bound(k: int, additive_width: int) -> float:
    return (
        miss_count_bound(k, additive_width)
        + additive_width * (additive_width + 1) / (2 * k)
    )


def l2_bound(k: int, additive_width: int) -> float:
    return (
        miss_count_bound(k, additive_width)
        + additive_width
        * (additive_width + 1)
        * (2 * additive_width + 1)
        / (6 * k * k)
    )


def verify(limit_k: int = 180) -> None:
    for k in range(2, limit_k + 1):
        upper = k * k + 2 * k
        for m in range(k + 1, upper + 1):
            exact = odd_quotient_count(k, m)
            assert exact in (0, 1)
            assert exact == direct_odd_count(k, m)
            assert exact == modular_arc_count(k, m)

            if m % 2:
                a, layer, corridor = odd_excess_layer(k, m)
                assert modular_arc_residue(k, m) == a * a % (2 * m)
                assert exact == int(corridor >= 2 * a)

        # Every quadratic layer contains at most one odd miss, and the root
        # scheduler identifies it exactly.
        misses_by_layer: dict[int, list[int]] = {}
        for m in range(k + 1, upper + 1, 1):
            if m % 2 == 0:
                continue
            a, layer, corridor = odd_excess_layer(k, m)
            if corridor < 2 * a:
                misses_by_layer.setdefault(layer, []).append(a)
        assert all(len(values) <= 1 for values in misses_by_layer.values())
        for layer, values in misses_by_layer.items():
            assert predicted_layer_miss(k, layer) == values[0]

        # Deterministic near-root halo.
        for a in range(2, upper - k + 1):
            m = k + a
            if m % 2 and a * a < 2 * m:
                assert odd_quotient_count(k, m) == 1

        # Finite L1/L2 checks on several additive widths.
        widths = {
            1,
            2,
            max(1, isqrt(k)),
            max(1, 2 * isqrt(k)),
            max(1, k // 3),
            k,
        }
        for additive_width in sorted(widths):
            misses = 0
            l1 = 0.0
            l2 = 0.0
            for m in range(k + 1, k + additive_width + 1):
                if m % 2 == 0:
                    continue
                remainder = odd_quotient_count(k, m) - k / m
                misses += odd_quotient_count(k, m) == 0
                l1 += abs(remainder)
                l2 += remainder * remainder
            assert misses <= miss_count_bound(k, additive_width)
            assert l1 <= l1_bound(k, additive_width) + 1e-12
            assert l2 <= l2_bound(k, additive_width) + 1e-12


if __name__ == "__main__":
    verify()
    print("P017 super-root modular-arc verifier: PASS")
