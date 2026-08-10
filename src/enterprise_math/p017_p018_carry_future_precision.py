"""Task-relative future precision for the P017×P018 carry refinement monoid.

The channel monoid from p017_p018_carry_refinement_channel gives an exact P023
style future-language question: how much of a parent quotient progression

    (N,y0),   y_t=y0-2t

must be retained to recover declared future odd refinements?

Size-only finite language
-------------------------
For an odd refinement d, the child size is

    N_d=floor(N/d)+1_{tau_d < N mod d},
    tau_d = y0 * 2^(-1) mod d.

Thus N_d depends only on N and y0 mod d.  For a finite set D of total refinement
products, all requested child sizes factor through

    (N, y0 mod L),
    L=lcm(D).

Because the refinement action is multiplicative,

    R_d2 o R_d1 = R_(d1*d2),

the same statement covers a finite compositional language: if every total
product that may be queried belongs to a finite set M, then
`(N,y0 mod lcm(M))` is sufficient.  Intermediate fiber lists are not required.

Exact-origin boundary
---------------------
The exact nonempty child quotient origin is

    y0_d=(y0-2 tau_d)/d.

Adding a multiple of L to y0 preserves all size channels for d|L but generally
changes y0_d by a nonzero multiple of L/d.  Hence a bounded residue state is not
universally sufficient when the future language observes exact descendant
origins rather than sizes alone.

Singleton universal-language boundary
--------------------------------------
For N=1 and positive odd y0,

    N_d=1 iff d|y0.

Therefore:

* visibility of all odd-prime refinements recovers rad(y0);
* visibility of all odd prime-power refinements recovers every v_p(y0);
* visibility of all positive odd refinements recovers the complete divisor set
  and hence y0 itself.

So the high-product singleton regime does not admit a nontrivial universal
collapse for the all-divisor future language.  Precision is genuinely
**task-relative**: bounded size-only futures admit a finite congruence quotient,
while the universal divisor language is information-complete.

This is an exact P017/P018 -> P023 future-sufficiency specialization.  It is not
a Legendre proof; for the Legendre route it is chiefly a negative boundary on
claims that the refinement monoid alone removes the terminal factorization
information.
"""

from __future__ import annotations

from math import lcm

from .p017_p018_carry_refinement_channel import refine_channel_state


def _normalize_refinements(refinements: tuple[int, ...]) -> tuple[int, ...]:
    if not refinements:
        raise ValueError("refinements must be nonempty")
    normalized = tuple(sorted(set(int(d) for d in refinements)))
    for d in normalized:
        if d < 1 or d % 2 == 0:
            raise ValueError("refinements must be positive odd integers")
    return normalized


def size_future_signature(
    fiber_size: int,
    first_quotient: int | None,
    refinements: tuple[int, ...],
) -> dict[str, object]:
    """Return all declared child sizes and their finite congruence precision."""
    normalized = _normalize_refinements(refinements)
    modulus = lcm(*normalized)
    rows: list[dict[str, int]] = []
    for d in normalized:
        data = refine_channel_state(fiber_size, first_quotient, d)
        rows.append({"refinement": d, "child_fiber_size": int(data["child_fiber_size"])})
    residue = None if first_quotient is None else first_quotient % modulus
    return {
        "fiber_size": fiber_size,
        "refinements": normalized,
        "future_precision_modulus": modulus,
        "first_quotient_residue": residue,
        "child_size_rows": tuple(rows),
        "finite_size_language_factors_through_residue": True,
    }


def verify_size_future_residue_sufficiency(
    fiber_size: int,
    first_quotient: int,
    refinements: tuple[int, ...],
    residue_shift_multiplier: int,
) -> dict[str, object]:
    """Check y0 and y0+tL have identical finite child-size signatures."""
    normalized = _normalize_refinements(refinements)
    modulus = lcm(*normalized)
    shifted = first_quotient + residue_shift_multiplier * modulus
    if shifted % 2 == 0:
        # L is odd, so parity flips when the multiplier is odd.  Use 2L to stay
        # inside the odd quotient-state class.
        shifted += modulus
    first = size_future_signature(fiber_size, first_quotient, normalized)
    second = size_future_signature(fiber_size, shifted, normalized)
    if first["child_size_rows"] != second["child_size_rows"]:
        raise AssertionError("finite size future failed congruence sufficiency")
    return {
        "fiber_size": fiber_size,
        "first_quotient": first_quotient,
        "shifted_first_quotient": shifted,
        "future_precision_modulus": modulus,
        "first_signature": first,
        "shifted_signature": second,
        "same_size_future_signature": True,
    }


def singleton_divisor_future_signature(
    first_quotient: int,
    refinements: tuple[int, ...],
) -> dict[str, object]:
    """Return the exact divisor visibility signature for a singleton channel."""
    if isinstance(first_quotient, bool) or not isinstance(first_quotient, int) or first_quotient <= 0 or first_quotient % 2 == 0:
        raise ValueError("first_quotient must be a positive odd integer")
    normalized = _normalize_refinements(refinements)
    rows = tuple(
        {
            "refinement": d,
            "visible": int(refine_channel_state(1, first_quotient, d)["child_fiber_size"]) == 1,
            "divides_first_quotient": first_quotient % d == 0,
        }
        for d in normalized
    )
    if any(bool(row["visible"]) != bool(row["divides_first_quotient"]) for row in rows):
        raise AssertionError("singleton future visibility is not exact divisibility")
    return {
        "fiber_size": 1,
        "first_quotient": first_quotient,
        "rows": rows,
        "singleton_visibility_equals_divisibility": True,
    }


def full_singleton_divisor_recovery(first_quotient: int) -> dict[str, object]:
    """Verify the all-positive-odd divisor future recovers y0 exactly."""
    if isinstance(first_quotient, bool) or not isinstance(first_quotient, int) or first_quotient <= 0 or first_quotient % 2 == 0:
        raise ValueError("first_quotient must be a positive odd integer")
    divisors = tuple(d for d in range(1, first_quotient + 1, 2) if first_quotient % d == 0)
    data = singleton_divisor_future_signature(first_quotient, divisors)
    visible = tuple(int(row["refinement"]) for row in data["rows"] if bool(row["visible"]))
    recovered = max(visible)
    if recovered != first_quotient:
        raise AssertionError("complete singleton divisor future failed to recover quotient")
    return {
        **data,
        "visible_divisors": visible,
        "recovered_first_quotient": recovered,
        "universal_divisor_future_is_information_complete": True,
    }
