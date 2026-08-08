"""Integer-only dimension-contraction tools for P019.

The core object is the balanced fiber-minimum power energy Psi_{m,s}(c): the
least possible sum of |a_i|**s over m integer slots with total c.  The square
case s=2 recovers the radial contraction model; s=1 recovers block-insensitive
relation cost up to the usual factor-of-two on zero-sum states.
"""

from __future__ import annotations


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def balanced_power_energy(block_size: int, power: int, total: int) -> int:
    """Minimum sum |a_i|**power for integer slots summing to total.

    If |total| = block_size*q + r, 0 <= r < block_size, a minimizer distributes
    the magnitude as evenly as possible: r slots have q+1 and the rest q.
    """
    _require_positive("block_size", block_size)
    _require_positive("power", power)
    _require_integer("total", total)
    magnitude = abs(total)
    q, r = divmod(magnitude, block_size)
    return (block_size - r) * q**power + r * (q + 1) ** power


def balanced_square_energy(block_size: int, total: int) -> int:
    """Square-energy specialization Psi_{m,2}."""
    return balanced_power_energy(block_size, 2, total)


def minimum_pair_collisions(block_size: int, units: int) -> int:
    """Minimum pair-collision count when units are balanced across slots."""
    _require_positive("block_size", block_size)
    if isinstance(units, bool) or not isinstance(units, int) or units < 0:
        raise ValueError("units must be a non-negative integer")
    q, r = divmod(units, block_size)
    return (block_size - r) * q * (q - 1) // 2 + r * q * (q + 1) // 2


def balanced_energy_increment(block_size: int, total: int) -> int:
    """Return Psi_{m,2}(total+1)-Psi_{m,2}(total)."""
    _require_positive("block_size", block_size)
    _require_integer("total", total)
    return 2 * (total // block_size) + 1


def min_plus_merge_power_energy(
    left_size: int, right_size: int, power: int, total: int
) -> int:
    """Closed result of min-plus convolution of two balanced power blocks."""
    _require_positive("left_size", left_size)
    _require_positive("right_size", right_size)
    _require_positive("power", power)
    _require_integer("total", total)
    return balanced_power_energy(left_size + right_size, power, total)


def min_plus_merge_energy(left_size: int, right_size: int, total: int) -> int:
    """Square-energy compatibility wrapper."""
    return min_plus_merge_power_energy(left_size, right_size, 2, total)


def partition_power_energy(
    block_sizes: tuple[int, ...], power: int, totals: tuple[int, ...]
) -> int:
    """Fiber-minimum power energy after contracting coordinates into blocks."""
    if not isinstance(block_sizes, tuple) or not block_sizes:
        raise ValueError("block_sizes must be a non-empty tuple")
    _require_positive("power", power)
    if not isinstance(totals, tuple) or len(totals) != len(block_sizes):
        raise ValueError("totals must be a tuple matching block_sizes")
    if sum(totals) != 0:
        raise ValueError("contracted totals must sum to zero")
    return sum(
        balanced_power_energy(block_size, power, total)
        for block_size, total in zip(block_sizes, totals)
    )


def partition_fiber_energy(block_sizes: tuple[int, ...], totals: tuple[int, ...]) -> int:
    """Square-energy compatibility wrapper for partition_power_energy."""
    return partition_power_energy(block_sizes, 2, totals)


def transfer_energy_increment(
    block_sizes: tuple[int, ...], totals: tuple[int, ...], receiver: int, donor: int
) -> int:
    """Square-energy increment for moving one integer unit donor -> receiver."""
    if receiver == donor:
        return 0
    if not (0 <= receiver < len(block_sizes) and 0 <= donor < len(block_sizes)):
        raise ValueError("receiver and donor must index block_sizes")
    partition_fiber_energy(block_sizes, totals)
    receiver_step = balanced_energy_increment(block_sizes[receiver], totals[receiver])
    donor_step = -balanced_energy_increment(block_sizes[donor], totals[donor] - 1)
    return receiver_step + donor_step
