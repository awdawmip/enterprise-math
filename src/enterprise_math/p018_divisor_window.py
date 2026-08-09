"""WIP P018 discovery: quotient-window separation for general divisors.

For a square basin k^2 < n < (k+1)^2 and divisor d>=2, the possible integer
quotients n//d lie in

    W_d(k) = [floor(k^2/d)+1, floor(k(k+2)/d)].

This module records an elementary sufficient separation criterion for two such
windows. It is discovery-stage evidence, not a canonical theorem module.
"""

from __future__ import annotations


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def divisor_quotient_window(k: int, divisor: int) -> tuple[int, int]:
    """Return the exact quotient window for 2<=divisor<=k."""
    _require_int("k", k)
    _require_int("divisor", divisor)
    if k < 2:
        raise ValueError("k must be at least 2")
    if divisor < 2 or divisor > k:
        raise ValueError("require 2 <= divisor <= k")
    return (k * k) // divisor + 1, (k * (k + 2)) // divisor


def divisor_window_separation(k: int, left: int, right: int) -> dict[str, object]:
    """Check the sufficient criterion 2*left <= k*(right-left).

    If 2d <= k(e-d), then d(k+2)<=ek and therefore

        floor(k(k+2)/e) <= floor(k^2/d),

    so W_e(k) lies strictly below W_d(k).
    """
    _require_int("k", k)
    _require_int("left", left)
    _require_int("right", right)
    if not (2 <= left < right <= k):
        raise ValueError("require 2 <= left < right <= k")
    margin = k * (right - left) - 2 * left
    if margin < 0:
        raise ValueError("the sufficient separation criterion is not satisfied")
    left_window = divisor_quotient_window(k, left)
    right_window = divisor_quotient_window(k, right)
    if right_window[1] >= left_window[0]:
        raise AssertionError("criterion held but quotient windows were not separated")
    return {
        "k": k,
        "left": left,
        "right": right,
        "criterion_margin": margin,
        "left_window": left_window,
        "right_window": right_window,
        "integer_gap": left_window[0] - right_window[1] - 1,
    }


def same_parity_divisor_windows(k: int) -> dict[str, object]:
    """Executable candidate corollary: same-parity divisor windows are disjoint."""
    _require_int("k", k)
    if k < 3:
        raise ValueError("k must be at least 3")
    divisors = list(range(2, k + 1))
    checked: list[tuple[int, int]] = []
    for i, left in enumerate(divisors):
        for right in divisors[i + 1 :]:
            if (right - left) % 2:
                continue
            divisor_window_separation(k, left, right)
            checked.append((left, right))
    return {"k": k, "checked_pairs": tuple(checked), "pair_count": len(checked)}
