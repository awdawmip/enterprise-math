"""Classical ADE primitive roots as minimum-grade events in causal charge kernels.

The root system is not primitive here. Start with an integer displacement kernel
defined by conserved free/modular charges, then choose an observation grade.
Two grades must not be conflated:

- transfer mass counts how many indivisible unit transfers a zero-total event
  actually moves;
- Q2(v)=sum_i v_i^2 is a symmetric integer second-order grade.

For A roots both notions select the same one-unit events. Exceptional E sections
can place events of different transfer mass on one Q2 shell, showing that
traditional equal root length is not automatically equal causal primitive cost.
"""

from __future__ import annotations

from .causal_charge_kernel_geometry import in_a_kernel, in_d_kernel, in_scaled_e8_charge_kernel

Vector = tuple[int, ...]


def quadratic_grade(vector: Vector) -> int:
    if not vector or any(isinstance(value, bool) or not isinstance(value, int) for value in vector):
        raise ValueError("vector must be a non-empty integer tuple")
    return sum(value * value for value in vector)


def absolute_event_mass(vector: Vector) -> int:
    if not vector or any(isinstance(value, bool) or not isinstance(value, int) for value in vector):
        raise ValueError("vector must be a non-empty integer tuple")
    return sum(abs(value) for value in vector)


def conserved_transfer_mass(vector: Vector) -> int:
    """Number of indivisible units moved by a zero-total displacement."""
    if not in_a_kernel(vector):
        raise ValueError("transfer mass requires exact total conservation")
    positive = sum(value for value in vector if value > 0)
    negative = -sum(value for value in vector if value < 0)
    if positive != negative:
        raise AssertionError("zero total must balance positive and negative transfer mass")
    return positive


def is_a_minimum_grade_move(vector: Vector) -> bool:
    return in_a_kernel(vector) and quadratic_grade(vector) == 2


def is_d_minimum_grade_move(vector: Vector) -> bool:
    return in_d_kernel(vector) and quadratic_grade(vector) == 2


def a_minimum_grade() -> int:
    return 2


def d_minimum_grade() -> int:
    return 2


def scaled_e8_minimum_grade() -> int:
    return 8


def is_scaled_e8_minimum_grade_move(vector: Vector) -> bool:
    return in_scaled_e8_charge_kernel(vector) and quadratic_grade(vector) == 8


def scaled_e8_grade_lower_bound_reason(vector: Vector) -> tuple[str, int]:
    if not in_scaled_e8_charge_kernel(vector):
        raise ValueError("vector must satisfy the scaled E8 finite charge code")
    if not any(vector):
        return "zero", 0
    parity = vector[0] % 2
    if parity == 1:
        return "odd-sector-eight-nonzero-coordinates", 8
    return "even-sector-parity-forces-two-units", 8


def e7_exact_charge(vector: Vector) -> int:
    if len(vector) != 8:
        raise ValueError("E7 section uses eight scaled E8 slots")
    return sum(vector)


def e6_second_exact_charge(vector: Vector) -> int:
    if len(vector) != 8:
        raise ValueError("E6 section uses eight scaled E8 slots")
    selector = (1, 1, 1, 1, 1, 1, -3, -3)
    return sum(value * weight for value, weight in zip(vector, selector))


def is_e7_minimum_grade_move(vector: Vector) -> bool:
    return is_scaled_e8_minimum_grade_move(vector) and e7_exact_charge(vector) == 0


def is_e6_minimum_grade_move(vector: Vector) -> bool:
    return is_e7_minimum_grade_move(vector) and e6_second_exact_charge(vector) == 0


def transfer_mass_histogram(vectors: tuple[Vector, ...]) -> dict[int, int]:
    histogram: dict[int, int] = {}
    for vector in vectors:
        mass = conserved_transfer_mass(vector)
        histogram[mass] = histogram.get(mass, 0) + 1
    return dict(sorted(histogram.items()))


def support_size_histogram(vectors: tuple[Vector, ...]) -> dict[int, int]:
    histogram: dict[int, int] = {}
    for vector in vectors:
        support = sum(value != 0 for value in vector)
        histogram[support] = histogram.get(support, 0) + 1
    return dict(sorted(histogram.items()))
