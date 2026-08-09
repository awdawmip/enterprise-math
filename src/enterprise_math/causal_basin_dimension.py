"""P008 completion basins as exact one-dimension-lower growth objects.

Let V(k) be a strictly increasing integer observation of complete causal/LEGO
structural levels.  The P008 right-adjoint root sends an amount n to the largest
k with V(k)<=n, so the k-th collapse basin is exactly the integer interval

    V(k) <= n < V(k+1)

and has width Delta V(k)=V(k+1)-V(k).

If V has finite-difference growth degree p, the basin-width sequence has degree
p-1.  For the free m-slot allocation family H_m(c), the identity is stronger:

    H_m(c+1)-H_m(c) = H_(m-1)(c+1).

Thus the entire collapse basin width is itself the cardinality of a complete
LEGO fiber with one fewer hidden placement freedom.  For A_p graph balls the
same difference is the graph sphere/shell count.  This connects P008 collapse,
P019 shell/basin ideas and the causal dimension ladder without invoking
calculus.
"""

from __future__ import annotations

from .causal_capacity_dimension import sampled_polynomial_difference_degree
from .lattice_geometry import a_ball_count, a_coordinator_shell_count
from .lego_partition_fiber import hidden_allocation_multiplicity


def basin_widths(complete_growth: tuple[int, ...]) -> tuple[int, ...]:
    if not isinstance(complete_growth, tuple) or len(complete_growth) < 2:
        raise ValueError("complete_growth must contain at least two levels")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in complete_growth
    ):
        raise ValueError("complete-growth values must be non-negative integers")
    if any(left >= right for left, right in zip(complete_growth, complete_growth[1:])):
        raise ValueError("complete_growth must be strictly increasing")
    return tuple(
        complete_growth[index + 1] - complete_growth[index]
        for index in range(len(complete_growth) - 1)
    )


def basin_growth_degree(complete_growth: tuple[int, ...]) -> int | None:
    """Finite-sample difference degree of the P008 basin-width sequence."""
    return sampled_polynomial_difference_degree(basin_widths(complete_growth))


def free_lego_basin_width(slot_count: int, total: int) -> int:
    """H_m(c+1)-H_m(c), equal to H_(m-1)(c+1) for m>=2."""
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 2:
        raise ValueError("slot_count must be at least two")
    if isinstance(total, bool) or not isinstance(total, int) or total < 0:
        raise ValueError("total must be a non-negative integer")
    direct = (
        hidden_allocation_multiplicity(slot_count, total + 1)
        - hidden_allocation_multiplicity(slot_count, total)
    )
    lower = hidden_allocation_multiplicity(slot_count - 1, total + 1)
    if direct != lower:
        raise AssertionError("free LEGO basin failed exact dimension-lowering identity")
    return direct


def a_p_ball_basin_width(p: int, radius: int) -> int:
    """V_p(r)-V_p(r-1)=A_p coordinator shell at radius r for r>=1."""
    if isinstance(p, bool) or not isinstance(p, int) or p <= 0:
        raise ValueError("p must be a positive integer")
    if isinstance(radius, bool) or not isinstance(radius, int) or radius <= 0:
        raise ValueError("radius must be a positive integer")
    direct = a_ball_count(p, radius) - a_ball_count(p, radius - 1)
    shell = a_coordinator_shell_count(p, radius)
    if direct != shell:
        raise AssertionError("A_p ball basin width did not equal coordinator shell")
    return direct


def expected_dimension_lowering(
    complete_growth: tuple[int, ...],
    expected_complete_degree: int,
) -> bool:
    """Finite exact audit that first difference lowers polynomial degree by one."""
    if expected_complete_degree <= 0:
        raise ValueError("expected_complete_degree must be positive")
    complete_degree = sampled_polynomial_difference_degree(complete_growth)
    width_degree = basin_growth_degree(complete_growth)
    return (
        complete_degree == expected_complete_degree
        and width_degree == expected_complete_degree - 1
    )
