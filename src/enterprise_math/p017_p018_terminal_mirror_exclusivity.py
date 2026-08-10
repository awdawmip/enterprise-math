"""Mirror-side exclusivity for the even-J terminal full-core shell.

Let

    J = J_perp(k) > 0

be even, so the near-primorial terminal odd order is m=J-1.  The terminal core
compression shows that every remaining low-core residual row has a complete
transverse core C satisfying

    C <= k-1,
    omega(rad(C)) = J,

and contributes exactly one residual bit.

For one anchor-surviving mirror pair M-r,M+r the transverse prime supports of
the two sides are disjoint.  Hence if *both* sides were terminal low-core rows,
the product of their complete cores would contain 2J distinct transverse odd
primes.  Writing P_perp(k,2J) for the minimum possible product of 2J such
primes gives

    C_- C_+ >= P_perp(k,2J).

But low-core terminality also gives

    C_- C_+ <= (k-1)^2.

Therefore whenever fewer than 2J transverse primes exist, or

    P_perp(k,2J) > (k-1)^2,

each mirror radius carries at most one terminal low-core residual bit.

This is a finite support-product obstruction.  It does not prove that terminal
residual rows are absent and does not prove Legendre; it lowers their natural
carrier from signed states to mirror radii on the stated scale regime.
"""

from __future__ import annotations

from .p017_mirror import mirror_center, mirror_pair, mirror_transverse_supports
from .p017_p018_near_primorial_precision import near_primorial_adaptive_order
from .p017_p018_terminal_core_compression import terminal_core_point_majorant
from .p017_p018_transverse_primorial import transverse_odd_primorial


def terminal_mirror_exclusivity_criterion(k: int) -> dict[str, object]:
    """Return the exact P_perp(k,2J) mirror-exclusivity condition."""
    data = near_primorial_adaptive_order(k)
    j = int(data["transverse_primorial_depth"])
    if j <= 0 or j % 2:
        raise ValueError("terminal mirror exclusivity is the positive even-J shell")

    barrier = transverse_odd_primorial(k, 2 * j)
    complete = bool(barrier["complete"])
    product = int(barrier["product"])
    ceiling = (k - 1) * (k - 1)
    exclusive = (not complete) or product > ceiling
    return {
        "k": k,
        "transverse_primorial_depth": j,
        "terminal_order": int(data["adaptive_odd_order"]),
        "required_distinct_primes_for_two_low_sides": 2 * j,
        "two_side_minimum_transverse_primes": tuple(barrier["transverse_primes"]),
        "two_side_minimum_transverse_product": product,
        "two_side_prefix_complete": complete,
        "low_core_product_ceiling": ceiling,
        "mirror_low_terminal_exclusive": exclusive,
    }


def terminal_mirror_pair_classification(k: int, radius: int) -> dict[str, object]:
    """Classify low-terminal residual bits on the two sides of one mirror pair."""
    criterion = terminal_mirror_exclusivity_criterion(k)
    if isinstance(radius, bool) or not isinstance(radius, int) or not (1 <= radius < k):
        raise ValueError("radius must satisfy 1<=r<k")

    lower, upper = mirror_pair(k, radius)
    lower_support, upper_support = mirror_transverse_supports(k, radius)
    lower_data = terminal_core_point_majorant(k, lower, tuple(lower_support))
    upper_data = terminal_core_point_majorant(k, upper, tuple(upper_support))
    low_sides = tuple(
        side
        for side, row in (("lower", lower_data), ("upper", upper_data))
        if bool(row["low_terminal_full_core_row"])
    )

    if bool(criterion["mirror_low_terminal_exclusive"]) and len(low_sides) > 1:
        lower_core = int(lower_data["complete_transverse_core"])
        upper_core = int(upper_data["complete_transverse_core"])
        if lower_core * upper_core <= int(criterion["low_core_product_ceiling"]):
            raise AssertionError("two terminal low-core mirror sides violated the transverse primorial barrier")

    return {
        **criterion,
        "radius": radius,
        "center": mirror_center(k),
        "lower_state": lower,
        "upper_state": upper,
        "lower_support": tuple(lower_support),
        "upper_support": tuple(upper_support),
        "lower_terminal": lower_data,
        "upper_terminal": upper_data,
        "low_terminal_sides": low_sides,
        "low_terminal_bit_count": len(low_sides),
    }


def terminal_low_rows_are_radius_injective(k: int) -> dict[str, object]:
    """Verify the exclusivity criterion across all surviving mirror radii."""
    criterion = terminal_mirror_exclusivity_criterion(k)
    if not bool(criterion["mirror_low_terminal_exclusive"]):
        raise ValueError("scale does not satisfy the mirror-exclusivity criterion")

    low_rows: list[tuple[int, str, int]] = []
    for radius in range(1, k):
        from math import gcd

        if gcd(radius, int(mirror_center(k))) != 1:
            continue
        data = terminal_mirror_pair_classification(k, radius)
        if int(data["low_terminal_bit_count"]) > 1:
            raise AssertionError("one radius carried two terminal low-core bits")
        for side in data["low_terminal_sides"]:
            state = int(data["lower_state"] if side == "lower" else data["upper_state"])
            low_rows.append((radius, side, state))

    radii = tuple(radius for radius, _side, _state in low_rows)
    if len(radii) != len(set(radii)):
        raise AssertionError("terminal low-core rows are not injective on mirror radius")
    return {
        **criterion,
        "terminal_low_rows": tuple(low_rows),
        "terminal_low_row_count": len(low_rows),
        "terminal_low_radius_count": len(set(radii)),
        "one_low_bit_per_radius": True,
    }
