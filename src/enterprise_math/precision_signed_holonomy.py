"""Signed path-defect transport for finite-precision operation schedules.

Base states may remain natural numbers while oriented differences between two
paths live in integers.  Python's ``//`` and ``%`` with a positive modulus use
the Euclidean/floor convention required here: the remainder is canonical in
``0 .. modulus-1`` even for negative inputs.
"""

from __future__ import annotations

from .core import collapse


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def signed_quotient(value: int, modulus: int) -> int:
    """Euclidean/floor quotient with positive ``modulus``."""
    _require_integer("value", value)
    _require_positive("modulus", modulus)
    return value // modulus


def signed_remainder(value: int, modulus: int) -> int:
    """Canonical remainder in ``0 .. modulus-1`` for signed ``value``."""
    _require_integer("value", value)
    _require_positive("modulus", modulus)
    return value % modulus


def signed_defect_transport(modulus: int, base_state: int, defect: int) -> int:
    """Transport an oriented integer defect through one quotient projection."""
    _require_positive("modulus", modulus)
    _require_integer("base_state", base_state)
    _require_integer("defect", defect)
    return signed_quotient(base_state + defect, modulus) - signed_quotient(
        base_state, modulus
    )


def signed_transport_bulk_carry(
    modulus: int, base_state: int, defect: int
) -> tuple[int, int, int]:
    """Return ``(transported, signed_bulk, canonical_carry)`` for P018-T94."""
    _require_positive("modulus", modulus)
    _require_integer("base_state", base_state)
    _require_integer("defect", defect)
    bulk = signed_quotient(defect, modulus)
    carry = (
        signed_remainder(base_state, modulus)
        + signed_remainder(defect, modulus)
    ) // modulus
    transported = signed_defect_transport(modulus, base_state, defect)
    if transported != bulk + carry:
        raise AssertionError("signed defect transport decomposition failed")
    if carry not in (0, 1):
        raise AssertionError("canonical residue carry must be binary")
    return transported, bulk, carry


def staged_signed_defect_transport(
    outer_modulus: int, inner_modulus: int, base_state: int, defect: int
) -> int:
    """Transport a signed defect through inner then outer quotient stages."""
    _require_positive("outer_modulus", outer_modulus)
    _require_positive("inner_modulus", inner_modulus)
    _require_integer("base_state", base_state)
    _require_integer("defect", defect)
    inner_base = signed_quotient(base_state, inner_modulus)
    inner_defect = signed_defect_transport(inner_modulus, base_state, defect)
    return signed_defect_transport(outer_modulus, inner_base, inner_defect)


def signed_transport_is_coherent(
    outer_modulus: int, inner_modulus: int, base_state: int, defect: int
) -> bool:
    """Check P018-T95: staged signed transport equals direct product transport."""
    direct = signed_defect_transport(
        outer_modulus * inner_modulus, base_state, defect
    )
    staged = staged_signed_defect_transport(
        outer_modulus, inner_modulus, base_state, defect
    )
    return direct == staged


def signed_defect_is_invisible(modulus: int, base_state: int, defect: int) -> bool:
    """Return the P018-T96 exact signed invisibility-window criterion."""
    _require_positive("modulus", modulus)
    _require_integer("base_state", base_state)
    _require_integer("defect", defect)
    residue = signed_remainder(base_state, modulus)
    return -residue <= defect < modulus - residue


def scheduling_holonomy(state: int, power: int, ratio: int) -> int:
    """P018-T93 oriented P009 collapse/project scheduling holonomy.

    Positive means ``project -> collapse`` ends above ``collapse -> project``;
    negative means it ends below it.
    """
    _require_natural("state", state)
    _require_positive("power", power)
    _require_positive("ratio", ratio)
    project_then_collapse = collapse(state // ratio, power)
    collapse_then_project = collapse(state, power) // ratio
    return project_then_collapse - collapse_then_project


def coarsened_scheduling_holonomy(
    state: int, power: int, first_ratio: int, second_ratio: int
) -> tuple[int, int]:
    """Return ``(direct_difference, transported_difference)`` for P018-T98."""
    _require_natural("state", state)
    _require_positive("power", power)
    _require_positive("first_ratio", first_ratio)
    _require_positive("second_ratio", second_ratio)
    first_path = collapse(state, power) // first_ratio
    second_path = collapse(state // first_ratio, power)
    defect = second_path - first_path
    direct = second_path // second_ratio - first_path // second_ratio
    transported = signed_defect_transport(second_ratio, first_path, defect)
    return direct, transported
