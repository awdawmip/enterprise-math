"""Exact orientation selector for the P025 projective capacity maximum.

Write

    U(n) = n*S(n) = sum_{p|n} v_p(n) * n/p.

For a primitive relation a+b=c the cyclic projective terms satisfy

    rho_c >= rho_b  iff  U(a)+U(c) >= U(b),
    rho_c >= rho_a  iff  U(b)+U(c) >= U(a).

Hence a side orientation can beat c only by violating one triangle inequality
in the raw derivative masses.  At most one side can do so.  If neither side is
superdominant, c is a maximizer; equality gives the exact tie cases.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_projective_capacity_condition import projective_capacity_condition_state
from .abc_support import abc_support_state, prime_factorization


@dataclass(frozen=True)
class ProjectiveOrientationState:
    abc: tuple[int, int, int]
    derivative_masses: tuple[int, int, int]
    triangle_defects: tuple[int, int]
    predicted_maximizers: tuple[int, ...]
    exact_maximizers: tuple[int, ...]


def raw_derivative_mass(n: int) -> int:
    """Return ``U(n)=sum v_p(n)*n/p`` exactly; define U(1)=0."""
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 0
    return sum(exponent * (n // prime) for prime, exponent in prime_factorization(n))


def projective_orientation_state(a: int, b: int, c: int) -> ProjectiveOrientationState:
    """Classify the exact cyclic maximizers from derivative-mass triangle defects.

    Orientation indices are ``0=a, 1=b, 2=c``.  The projective state's stored
    cyclic defect order is ``c,b,a``, so the exact comparison is reordered here.
    """
    abc_support_state(a, b, c)
    Ua, Ub, Uc = (raw_derivative_mass(n) for n in (a, b, c))

    # Positive defect means that side violates the triangle inequality and is
    # the unique projective maximizer.
    defect_a = Ua - Ub - Uc
    defect_b = Ub - Ua - Uc
    if defect_a > 0:
        predicted = (0,)
    elif defect_b > 0:
        predicted = (1,)
    else:
        predicted_list = [2]
        if defect_a == 0:
            predicted_list.append(0)
        if defect_b == 0:
            predicted_list.append(1)
        predicted = tuple(sorted(predicted_list))

    state = projective_capacity_condition_state(a, b, c)
    # stored order is rho_c,rho_b,rho_a
    by_orientation = (
        state.cyclic_weighted_defects[2],
        state.cyclic_weighted_defects[1],
        state.cyclic_weighted_defects[0],
    )
    maximum = max(by_orientation)
    exact = tuple(i for i, value in enumerate(by_orientation) if value == maximum)
    if predicted != exact:
        raise AssertionError(
            f"derivative-mass orientation law failed: predicted {predicted}, exact {exact}"
        )

    return ProjectiveOrientationState(
        abc=(a, b, c),
        derivative_masses=(Ua, Ub, Uc),
        triangle_defects=(defect_a, defect_b),
        predicted_maximizers=predicted,
        exact_maximizers=exact,
    )
