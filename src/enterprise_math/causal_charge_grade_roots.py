"""Classical ADE primitive roots as minimum-grade events in causal charge kernels.

The root system is not primitive here.  Start with an integer displacement kernel
defined by conserved free/modular charges, then read the symmetric integer
second-order grade Q2(v)=sum_i v_i^2.  Primitive grade events are the nonzero
allowed displacements of minimum Q2.

Exact total conservation yields A roots at grade 2.  Total parity conservation
yields D roots at grade 2.  The scaled E8 finite charge code (all coordinates the
same parity and total divisible by four) has minimum nonzero grade 8; its grade-8
events are exactly the 112 two-coordinate +/-2 roots plus the 128 all-odd +/-1
roots.  E7/E6 are exact-charge sections of that same code.

The quadratic grade is used as an integer collision/dispersion observation, not
asserted here as primitive Euclidean ontology.
"""

from __future__ import annotations

from .causal_charge_kernel_geometry import (
    in_a_kernel,
    in_d_kernel,
    in_scaled_e8_charge_kernel,
)

Vector = tuple[int, ...]


def quadratic_grade(vector: Vector) -> int:
    if not vector or any(isinstance(value, bool) or not isinstance(value, int) for value in vector):
        raise ValueError("vector must be a non-empty integer tuple")
    return sum(value * value for value in vector)


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
    """Return the parity-sector reason and certified lower bound for a nonzero code vector."""
    if not in_scaled_e8_charge_kernel(vector):
        raise ValueError("vector must satisfy the scaled E8 finite charge code")
    if not any(vector):
        return "zero", 0
    parity = vector[0] % 2
    if parity == 1:
        # Eight odd coordinates each have square at least one.
        return "odd-sector-eight-nonzero-coordinates", 8
    # vector=2*z.  If sum z_i were odd then sum vector would be 2 mod 4, forbidden.
    # A nonzero integer z of squared grade one has exactly one +/-1 and odd sum;
    # therefore allowed z has squared grade at least two, so vector has grade >=8.
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
