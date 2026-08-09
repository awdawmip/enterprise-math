"""Single-bit horizon carry for exact quotient-root state counts.

The compressed denominator/root atlas has a deterministic coarse count plus one
boundary bit.  For positive ``n`` and root exponent ``r>=1`` let

    H = R_{r+1}(r*n - 1),
    D = floor(n/(H+1)^r),
    rho = n - D*(H+1)^r.

When ``H>=1`` all low roots ``1,...,H-1`` occur, and every high root above H is
a singleton.  Only the horizon root H may be absent.  It is present iff

    floor(n/H^r) >= D+1

or equivalently

    n >= (D+1)H^r.

Writing ``Delta=(H+1)^r-H^r`` and using the coarse block decomposition of n,
this is the exact carry test

    rho >= H^r - D*Delta.

If the right-hand side is nonpositive, the carry is automatically one.  Thus

    N_r(n) = D + H - 1 + kappa_r(n),   H>=1,

with ``kappa_r(n)`` a genuine one-bit boundary carry.  The exceptional H=0
case has ``N_r(n)=D``.

This module is integer-only and intentionally separates the project-specific
carry packaging from the classical floor/root order facts used to prove it.
"""

from __future__ import annotations

from .p018_root_state_decomposition import (
    exact_distinct_root_state_count,
    horizon_fiber_present,
    state_coalescence_horizon,
)


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def horizon_state_carry(n: int, root_exp: int) -> dict[str, int | bool]:
    """Return the exact boundary-carry data controlling the horizon root."""
    _require_int("n", n)
    _require_int("root_exp", root_exp)
    if n < 1 or root_exp < 1:
        raise ValueError("n and root_exp must be positive")

    horizon = state_coalescence_horizon(n, root_exp)
    step_power = (horizon + 1) ** root_exp
    high_denominator_max = n // step_power
    block_base = high_denominator_max * step_power
    remainder = n - block_base

    if horizon == 0:
        carry = False
        root_power = 0
        power_increment = step_power
        raw_threshold = 0
        effective_threshold = 0
    else:
        root_power = horizon**root_exp
        power_increment = step_power - root_power
        raw_threshold = root_power - high_denominator_max * power_increment
        effective_threshold = max(0, raw_threshold)
        carry = remainder >= effective_threshold
        direct = n >= (high_denominator_max + 1) * root_power
        if carry != direct:
            raise AssertionError("remainder carry and direct horizon test disagree")
        if carry != horizon_fiber_present(n, root_exp):
            raise AssertionError("horizon carry disagrees with exact root fiber")

    closed = exact_distinct_root_state_count(n, root_exp)
    expected_count = (
        high_denominator_max
        if horizon == 0
        else high_denominator_max + horizon - 1 + int(carry)
    )
    if expected_count != closed["distinct_root_count"]:
        raise AssertionError("horizon carry failed to reconstruct exact state count")

    return {
        "n": n,
        "root_exp": root_exp,
        "horizon": horizon,
        "high_denominator_max": high_denominator_max,
        "block_base": block_base,
        "remainder": remainder,
        "root_power": root_power,
        "next_root_power": step_power,
        "power_increment": power_increment,
        "raw_carry_threshold": raw_threshold,
        "effective_carry_threshold": effective_threshold,
        "horizon_carry": carry,
        "distinct_root_count": expected_count,
    }
