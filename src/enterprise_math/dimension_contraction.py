"""Integer-only dimension-contraction tools for P019.

The core object is the balanced fiber-minimum square energy psi_m(c): the
least possible sum of squares of m integer coordinates with total c.
"""

from __future__ import annotations


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def balanced_square_energy(block_size: int, total: int) -> int:
    """Minimum sum of squares of block_size integers whose sum is total.

    If |total| = block_size*q + r with 0 <= r < block_size, the minimizer has
    r coordinates of magnitude q+1 and the remaining coordinates of magnitude
    q, all with the sign of total.
    """
    _require_positive("block_size", block_size)
    _require_integer("total", total)
    magnitude = abs(total)
    q, r = divmod(magnitude, block_size)
    return (block_size - r) * q * q + r * (q + 1) * (q + 1)


def minimum_pair_collisions(block_size: int, units: int) -> int:
    """Minimum pair-collision count when units are balanced across slots."""
    _require_positive("block_size", block_size)
    if isinstance(units, bool) or not isinstance(units, int) or units < 0:
        raise ValueError("units must be a non-negative integer")
    q, r = divmod(units, block_size)
    return (block_size - r) * q * (q - 1) // 2 + r * q * (q + 1) // 2


def balanced_energy_increment(block_size: int, total: int) -> int:
    """Return psi_m(total+1)-psi_m(total) as an exact odd integer."""
    _require_positive("block_size", block_size)
    _require_integer("total", total)
    return 2 * (total // block_size) + 1


def min_plus_merge_energy(left_size: int, right_size: int, total: int) -> int:
    """Min-plus convolution of two balanced square-energy blocks.

    The search interval is finite because a minimizer is attained by a split
    nearest the proportional allocation. We expose the direct closed result;
    tests verify it against bounded exhaustive min-plus convolution.
    """
    _require_positive("left_size", left_size)
    _require_positive("right_size", right_size)
    _require_integer("total", total)
    return balanced_square_energy(left_size + right_size, total)


def partition_fiber_energy(block_sizes: tuple[int, ...], totals: tuple[int, ...]) -> int:
    """Fiber-minimum square energy after contracting coordinates into blocks."""
    if not isinstance(block_sizes, tuple) or not block_sizes:
        raise ValueError("block_sizes must be a non-empty tuple")
    if not isinstance(totals, tuple) or len(totals) != len(block_sizes):
        raise ValueError("totals must be a tuple matching block_sizes")
    if sum(totals) != 0:
        raise ValueError("contracted totals must sum to zero")
    return sum(
        balanced_square_energy(block_size, total)
        for block_size, total in zip(block_sizes, totals)
    )


def transfer_energy_increment(
    block_sizes: tuple[int, ...], totals: tuple[int, ...], receiver: int, donor: int
) -> int:
    """Energy increment for moving one integer unit from donor to receiver."""
    if receiver == donor:
        return 0
    if not (0 <= receiver < len(block_sizes) and 0 <= donor < len(block_sizes)):
        raise ValueError("receiver and donor must index block_sizes")
    partition_fiber_energy(block_sizes, totals)
    receiver_step = balanced_energy_increment(block_sizes[receiver], totals[receiver])
    donor_step = -balanced_energy_increment(block_sizes[donor], totals[donor] - 1)
    return receiver_step + donor_step
