"""Exact quotient transport of square-collapse basins.

The core result is finite and integer-only: dividing every state in one square
basin by an integer d>=2 can move the square-root index to only two adjacent
values, and the new root index is strictly below the original basin index.
"""

from __future__ import annotations

from .core import integer_nth_root


def _require_nat(name: str, value: int, *, minimum: int = 0) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")


def square_basin_quotient_transport(k: int, divisor: int, n: int) -> dict[str, int]:
    """Transport one state from the k-th square basin through floor division.

    Preconditions:
        k >= 1,
        divisor >= 2,
        k^2 <= n < (k+1)^2.

    If j=R_2(floor(k^2/divisor)), then the returned quotient root is exactly
    j or j+1, and j<k.
    """
    _require_nat("k", k, minimum=1)
    _require_nat("divisor", divisor, minimum=2)
    _require_nat("n", n)
    lower = k * k
    upper_exclusive = (k + 1) * (k + 1)
    if not lower <= n < upper_exclusive:
        raise ValueError("n must lie in the canonical square basin [k^2,(k+1)^2)")

    base_quotient = lower // divisor
    base_root = integer_nth_root(base_quotient, 2)
    quotient = n // divisor
    quotient_root = integer_nth_root(quotient, 2)

    if base_root >= k:
        raise AssertionError("quotient root scale did not strictly descend")
    if quotient_root not in (base_root, base_root + 1):
        raise AssertionError("square basin divided into more than two root-index basins")

    return {
        "k": k,
        "divisor": divisor,
        "n": n,
        "base_quotient": base_quotient,
        "base_root": base_root,
        "quotient": quotient,
        "quotient_root": quotient_root,
    }


def square_basin_quotient_window(k: int, divisor: int) -> dict[str, int]:
    """Return the complete quotient image of [k^2,(k+1)^2) under floor division."""
    _require_nat("k", k, minimum=1)
    _require_nat("divisor", divisor, minimum=2)

    q_min = (k * k) // divisor
    q_max = (((k + 1) * (k + 1)) - 1) // divisor
    base_root = integer_nth_root(q_min, 2)
    max_root = integer_nth_root(q_max, 2)

    if base_root >= k:
        raise AssertionError("quotient window did not strictly descend in root scale")
    if max_root not in (base_root, base_root + 1):
        raise AssertionError("quotient window meets more than two square-root indices")

    return {
        "k": k,
        "divisor": divisor,
        "q_min": q_min,
        "q_max": q_max,
        "base_root": base_root,
        "max_root": max_root,
    }


def open_divisible_cofactor_window(k: int, divisor: int) -> dict[str, int]:
    """Return the quotient window for divisible states strictly inside the square basin.

    This is the P017 specialization when ``divisor`` is the chosen least prime:

        floor(k^2/d)+1 <= q <= floor(((k+1)^2-1)/d).

    Every such q satisfies j^2 < q < (j+2)^2 for
    j=R_2(floor(k^2/d)).
    """
    data = square_basin_quotient_window(k, divisor)
    q_min_open = (k * k) // divisor + 1
    q_max = data["q_max"]
    base_root = data["base_root"]

    if q_min_open <= q_max:
        if not base_root * base_root < q_min_open:
            raise AssertionError("open cofactor window did not leave the lower square boundary")
        if not q_max < (base_root + 2) * (base_root + 2):
            raise AssertionError("open cofactor window crossed a third square basin")

    return {
        **data,
        "q_min_open": q_min_open,
        "nonempty": int(q_min_open <= q_max),
    }
