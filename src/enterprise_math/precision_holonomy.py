"""Exact transport laws for operation-scheduling defects in P018.

The functions here treat a path defect as an explicit non-negative integer state
change.  Coarsening transports that difference by quotienting the perturbed and
unperturbed states separately; no real-valued error model or limiting process is
used.
"""

from __future__ import annotations

from .precision import (
    collapse_refinement_defect,
    precision_ratio,
    scale_collapse_state,
)


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def defect_transport(modulus: int, base_state: int, defect: int) -> int:
    """Return the coarse-visible part of a non-negative fine-state defect."""
    _require_positive("modulus", modulus)
    _require_natural("base_state", base_state)
    _require_natural("defect", defect)
    return (base_state + defect) // modulus - base_state // modulus


def defect_transport_bulk_carry(modulus: int, base_state: int, defect: int) -> tuple[int, int, int]:
    """Return ``(transported, bulk, carry)`` for P018-T88.

    The exact identity is

        transported = defect // modulus
                    + ((base_state % modulus + defect % modulus) // modulus).
    """
    _require_positive("modulus", modulus)
    _require_natural("base_state", base_state)
    _require_natural("defect", defect)
    bulk = defect // modulus
    carry = (base_state % modulus + defect % modulus) // modulus
    transported = defect_transport(modulus, base_state, defect)
    if transported != bulk + carry:
        raise AssertionError("defect transport bulk/carry decomposition failed")
    if carry not in (0, 1):
        raise AssertionError("residual transport carry must be binary")
    return transported, bulk, carry


def staged_defect_transport(
    outer_modulus: int, inner_modulus: int, base_state: int, defect: int
) -> int:
    """Transport a defect through two quotient stages, inner then outer."""
    _require_positive("outer_modulus", outer_modulus)
    _require_positive("inner_modulus", inner_modulus)
    _require_natural("base_state", base_state)
    _require_natural("defect", defect)
    inner_base = base_state // inner_modulus
    inner_defect = defect_transport(inner_modulus, base_state, defect)
    return defect_transport(outer_modulus, inner_base, inner_defect)


def transport_is_coherent(
    outer_modulus: int, inner_modulus: int, base_state: int, defect: int
) -> bool:
    """Check P018-T89: staged transport equals direct product-modulus transport."""
    direct = defect_transport(outer_modulus * inner_modulus, base_state, defect)
    staged = staged_defect_transport(outer_modulus, inner_modulus, base_state, defect)
    return direct == staged


def collapse_holonomy_composition(
    n: int, power: int, coarse: int, middle: int, fine: int
) -> tuple[int, int, int, int]:
    """Return and verify the P018-T90 collapse-holonomy composition law.

    The tuple is ``(direct, lower, upper, transported_upper)`` and satisfies

        direct = lower + transported_upper.
    """
    _require_natural("n", n)
    _require_positive("power", power)
    precision_ratio(coarse, middle)
    precision_ratio(middle, fine)
    ratio = middle // coarse
    modulus = ratio**power

    lower = collapse_refinement_defect(n, power, coarse, middle)
    upper = collapse_refinement_defect(n, power, middle, fine)
    direct = collapse_refinement_defect(n, power, coarse, fine)
    middle_collapse = scale_collapse_state(n, power, middle)
    transported_upper = defect_transport(modulus, middle_collapse, upper)
    if direct != lower + transported_upper:
        raise AssertionError("collapse holonomy composition failed")
    return direct, lower, upper, transported_upper


def defect_is_invisible(modulus: int, base_state: int, defect: int) -> bool:
    """Return the exact P018-T91 zero-visibility condition."""
    _require_positive("modulus", modulus)
    _require_natural("base_state", base_state)
    _require_natural("defect", defect)
    threshold = modulus - base_state % modulus
    return defect < threshold


def strict_recovery_threshold(
    n: int, power: int, coarse: int, middle: int, fine: int
) -> tuple[bool, int, int]:
    """Return ``(strict, upper_holonomy, threshold)`` for P018-T92."""
    _require_natural("n", n)
    _require_positive("power", power)
    precision_ratio(coarse, middle)
    precision_ratio(middle, fine)
    modulus = (middle // coarse) ** power
    middle_collapse = scale_collapse_state(n, power, middle)
    upper = collapse_refinement_defect(n, power, middle, fine)
    threshold = modulus - middle_collapse % modulus
    strict = upper >= threshold

    direct, lower, _, transported = collapse_holonomy_composition(
        n, power, coarse, middle, fine
    )
    if strict != (direct > lower):
        raise AssertionError("strict recovery threshold criterion failed")
    if strict != (transported > 0):
        raise AssertionError("strict recovery transport criterion failed")
    return strict, upper, threshold
