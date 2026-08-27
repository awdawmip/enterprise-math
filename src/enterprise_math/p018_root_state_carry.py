"""Exact boundary carries for quotient-root state counts.

There are two nested carry descriptions for the compressed denominator/root
atlas.

Binary horizon carry
--------------------
For positive ``n`` and root exponent ``r>=1`` let

    H = R_{r+1}(r*n - 1),
    D = floor(n/(H+1)^r),
    rho = n - D*(H+1)^r.

When ``H>=1`` all low roots ``1,...,H-1`` occur, and every high root above H is
a singleton.  Only the horizon root H may be absent.  It is present iff

    floor(n/H^r) >= D+1,

or equivalently

    n >= (D+1)H^r.

Writing ``Delta=(H+1)^r-H^r``, this is the exact one-bit carry test

    rho >= H^r - D*Delta.

Hence

    N_r(n) = D + H - 1 + kappa_r(n),   H>=1,

with ``kappa_r(n)`` binary.

Ternary state-count carry
-------------------------
The coarse denominator threshold D itself is confined to three adjacent values.
Put

    q = floor(H/r).

Then

    D in {q-1, q, q+1}

(with the obvious truncation at zero).  Moreover the exceptional lower case
``D=q-1`` necessarily has the horizon fiber present.  Combining this three-point
D-band with the binary horizon bit gives a single monotone ternary carry.
Define

    A = max(q*(H+1)^r, (q+1)*H^r),
    B = (q+1)*(H+1)^r,

and

    tau = 0,  n < A
          1,  A <= n < B
          2,  B <= n.

Then the exact number of distinct positive quotient-root states is

    N_r(n) = H + q - 1 + tau.

Thus the exact cardinality is determined by one ``(r+1)``-st integer root, the
small quotient ``H//r``, and two integer threshold comparisons.  For fixed r,
this sharpens the earlier Theta estimate to

    N_r(n) = (r+1) r^(-r/(r+1)) n^(1/(r+1)) + O(1),

where this asymptotic sentence is explanatory only; all executable logic below
is integer-only.
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
    """Return the exact binary boundary-carry data controlling the horizon root."""
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


def ternary_state_count_carry(n: int, root_exp: int) -> dict[str, int]:
    """Return the exact three-valued carry controlling the total state count.

    If ``H=R_{r+1}(r*n-1)`` and ``q=H//r``, the count is exactly

        H + q - 1 + tau,

    where ``tau`` is selected by the two thresholds returned here.
    """
    _require_int("n", n)
    _require_int("root_exp", root_exp)
    if n < 1 or root_exp < 1:
        raise ValueError("n and root_exp must be positive")

    horizon = state_coalescence_horizon(n, root_exp)
    q = horizon // root_exp
    root_power = horizon**root_exp
    next_root_power = (horizon + 1) ** root_exp

    lower_threshold = max(
        q * next_root_power,
        (q + 1) * root_power,
    )
    upper_threshold = (q + 1) * next_root_power

    if n < lower_threshold:
        carry = 0
    elif n < upper_threshold:
        carry = 1
    else:
        carry = 2

    exact_count = horizon + q - 1 + carry
    if exact_count < 1:
        raise AssertionError("positive quotient-root state count became nonpositive")

    binary = horizon_state_carry(n, root_exp)
    if exact_count != binary["distinct_root_count"]:
        raise AssertionError("ternary carry disagrees with exact binary carry count")

    d = int(binary["high_denominator_max"])
    if d < max(0, q - 1) or d > q + 1:
        raise AssertionError("high-denominator threshold escaped the three-point band")
    if q > 0 and d == q - 1 and not bool(binary["horizon_carry"]):
        raise AssertionError("lower D-band case lost its forced horizon carry")

    return {
        "n": n,
        "root_exp": root_exp,
        "horizon": horizon,
        "horizon_quotient": q,
        "high_denominator_max": d,
        "lower_threshold": lower_threshold,
        "upper_threshold": upper_threshold,
        "ternary_carry": carry,
        "distinct_root_count": exact_count,
    }


def ternary_state_count_band(n: int, root_exp: int) -> tuple[int, int, int]:
    """Return the three consecutive cardinalities allowed by the coarse horizon."""
    data = ternary_state_count_carry(n, root_exp)
    center = data["horizon"] + data["horizon_quotient"]
    return center - 1, center, center + 1
