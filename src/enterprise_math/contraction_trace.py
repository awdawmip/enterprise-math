"""Finite witness and trace kernels for P019 dimension contraction.

This module separates three layers:

1. balanced minimum values, which are associative under min-plus block merge;
2. full two-block fiber witness relations, which are integer intervals;
3. directed boundary representatives, whose repeated selection can depend on the
   ordered contraction history.

No floating point values or true division are used.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb, factorial

from .core import integer_nth_root
from .dimension_contraction import balanced_power_energy


Block = tuple[int, ...]
MergeStep = tuple[Block, Block]


@dataclass(frozen=True)
class BoundaryTraceStep:
    receiver: Block
    donor: Block
    total: int
    slack_before: int
    receiver_total: int
    donor_total: int
    consumed_excess: int
    slack_after: int
    next_gap: int


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def balanced_minimizer_count(block_size: int, power: int, total: int) -> int:
    """Number of labeled slot-level minimizers for Psi_(m,s)(total).

    For power > 1 the minimizer is balanced: if |total| = m*q+r, exactly r
    labeled slots carry magnitude q+1 and the remaining slots carry q. For
    power = 1 every sign-consistent weak composition is minimizing.
    """
    _require_positive("block_size", block_size)
    _require_positive("power", power)
    _require_integer("total", total)
    magnitude = abs(total)
    if power == 1:
        if magnitude == 0:
            return 1
        return comb(magnitude + block_size - 1, block_size - 1)
    _, remainder = divmod(magnitude, block_size)
    return comb(block_size, remainder)


def two_block_argmin_profile(
    left_size: int, right_size: int, power: int, total: int
) -> tuple[tuple[int, int], ...]:
    """Return (left_total, labeled multiplicity) for every min-plus minimizer.

    For power > 1 the profile is the hypergeometric remainder-allocation
    profile. For power = 1 it is the weak-composition profile.
    """
    _require_positive("left_size", left_size)
    _require_positive("right_size", right_size)
    _require_positive("power", power)
    _require_integer("total", total)

    if power == 1:
        values = range(0, total + 1) if total >= 0 else range(total, 1)
        result = []
        for left_total in values:
            right_total = total - left_total
            left_count = balanced_minimizer_count(left_size, 1, left_total)
            right_count = balanced_minimizer_count(right_size, 1, right_total)
            result.append((left_total, left_count * right_count))
        return tuple(result)

    total_size = left_size + right_size
    magnitude = abs(total)
    q, remainder = divmod(magnitude, total_size)
    low = max(0, remainder - right_size)
    high = min(left_size, remainder)
    sign = 1 if total >= 0 else -1
    result = []
    for left_remainder in range(low, high + 1):
        left_magnitude = left_size * q + left_remainder
        right_remainder = remainder - left_remainder
        multiplicity = comb(left_size, left_remainder) * comb(
            right_size, right_remainder
        )
        result.append((sign * left_magnitude, multiplicity))
    return tuple(result)


def fiber_excess_energy(
    left_size: int, right_size: int, power: int, total: int, left_total: int
) -> int:
    """Energy above the merged fiber minimum for one two-block split."""
    _require_positive("left_size", left_size)
    _require_positive("right_size", right_size)
    _require_positive("power", power)
    _require_integer("total", total)
    _require_integer("left_total", left_total)
    split = balanced_power_energy(left_size, power, left_total) + balanced_power_energy(
        right_size, power, total - left_total
    )
    merged = balanced_power_energy(left_size + right_size, power, total)
    return split - merged


def fiber_witness_interval(
    left_size: int, right_size: int, power: int, total: int, slack: int
) -> tuple[int, int]:
    """Compressed full witness relation for one contraction fiber.

    Returns the integer interval [L,U] of left totals whose split energy is at
    most merged_minimum + slack. Discrete convexity guarantees that the full
    feasible set is exactly this interval.
    """
    _require_positive("left_size", left_size)
    _require_positive("right_size", right_size)
    _require_positive("power", power)
    _require_integer("total", total)
    _require_natural("slack", slack)

    profile = two_block_argmin_profile(left_size, right_size, power, total)
    left = min(value for value, _ in profile)
    right = max(value for value, _ in profile)

    while fiber_excess_energy(left_size, right_size, power, total, left - 1) <= slack:
        left -= 1
    while fiber_excess_energy(left_size, right_size, power, total, right + 1) <= slack:
        right += 1
    return left, right


def fiber_witness_multiplicity(
    left_size: int, right_size: int, power: int, total: int, slack: int
) -> int:
    """Number of feasible block-total witnesses in the compressed fiber relation."""
    left, right = fiber_witness_interval(left_size, right_size, power, total, slack)
    return right - left + 1


def directed_boundary_split(
    receiver_size: int, donor_size: int, power: int, total: int, slack: int
) -> tuple[int, int]:
    """Unique right-end boundary representative for donor -> receiver transfer."""
    _, receiver_total = fiber_witness_interval(
        receiver_size, donor_size, power, total, slack
    )
    return receiver_total, total - receiver_total


def directed_boundary_decomposition(
    receiver_size: int, donor_size: int, power: int, total: int, slack: int
) -> tuple[int, int, int, int, int]:
    """Return boundary split plus exact consumed/slack remainder decomposition.

    Returns `(receiver_total, donor_total, consumed_excess, remainder, next_gap)`.
    The remainder satisfies `0 <= remainder < next_gap`.
    """
    receiver_total, donor_total = directed_boundary_split(
        receiver_size, donor_size, power, total, slack
    )
    consumed = fiber_excess_energy(
        receiver_size, donor_size, power, total, receiver_total
    )
    remainder = slack - consumed
    next_excess = fiber_excess_energy(
        receiver_size, donor_size, power, total, receiver_total + 1
    )
    next_gap = next_excess - consumed
    if not (0 <= remainder < next_gap):
        raise AssertionError("directed boundary remainder must lie inside the next basin")
    return receiver_total, donor_total, consumed, remainder, next_gap


def square_residue_correction(block_size: int, total: int) -> int:
    """Bounded remainder epsilon_m(c) in m*Psi_(m,2)(c)=c^2+epsilon."""
    _require_positive("block_size", block_size)
    _require_integer("total", total)
    remainder = abs(total) % block_size
    return remainder * (block_size - remainder)


def square_split_imbalance(
    left_size: int, right_size: int, left_total: int, right_total: int
) -> int:
    """Cross-multiplied deviation from proportional block allocation."""
    _require_positive("left_size", left_size)
    _require_positive("right_size", right_size)
    _require_integer("left_total", left_total)
    _require_integer("right_total", right_total)
    return right_size * left_total - left_size * right_total


def square_split_from_imbalance(
    left_size: int, right_size: int, total: int, imbalance: int
) -> tuple[int, int]:
    """Recover an exact two-block split from parent total and imbalance tag.

    A valid tag satisfies `(left_size*total + imbalance) % (left_size+right_size)=0`.
    """
    _require_positive("left_size", left_size)
    _require_positive("right_size", right_size)
    _require_integer("total", total)
    _require_integer("imbalance", imbalance)
    total_size = left_size + right_size
    numerator = left_size * total + imbalance
    if numerator % total_size != 0:
        raise ValueError("imbalance tag is incompatible with block sizes and total")
    left_total = numerator // total_size
    right_total = total - left_total
    return left_total, right_total


def square_minimum_imbalance_profile(
    left_size: int, right_size: int, total: int
) -> tuple[tuple[int, int], ...]:
    """Return `(imbalance, multiplicity)` for every square-energy minimizer.

    The profile depends on the parent remainder (and sign), not on the bulk
    quotient of `|total|` by the merged block size.
    """
    profile = two_block_argmin_profile(left_size, right_size, 2, total)
    return tuple(
        (
            square_split_imbalance(
                left_size, right_size, left_total, total - left_total
            ),
            multiplicity,
        )
        for left_total, multiplicity in profile
    )


def square_scaled_excess_identity(
    left_size: int, right_size: int, left_total: int, right_total: int
) -> tuple[int, int]:
    """Return both sides of the exact scaled square-excess identity."""
    _require_positive("left_size", left_size)
    _require_positive("right_size", right_size)
    _require_integer("left_total", left_total)
    _require_integer("right_total", right_total)
    total_size = left_size + right_size
    total = left_total + right_total
    excess = fiber_excess_energy(left_size, right_size, 2, total, left_total)
    left_side = left_size * right_size * total_size * excess
    imbalance = square_split_imbalance(
        left_size, right_size, left_total, right_total
    )
    right_side = (
        imbalance * imbalance
        + right_size
        * total_size
        * square_residue_correction(left_size, left_total)
        + left_size
        * total_size
        * square_residue_correction(right_size, right_total)
        - left_size
        * right_size
        * square_residue_correction(total_size, total)
    )
    return left_side, right_side


def square_imbalance_bound(
    left_size: int, right_size: int, total: int, slack: int
) -> int:
    """Integer bound for |(m+n)*left_total-m*total| at given square slack."""
    _require_positive("left_size", left_size)
    _require_positive("right_size", right_size)
    _require_integer("total", total)
    _require_natural("slack", slack)
    total_size = left_size + right_size
    bound_square = (
        left_size
        * right_size
        * (
            total_size * slack
            + square_residue_correction(total_size, total)
        )
    )
    return integer_nth_root(bound_square, 2)


def _normalize_block(block: Block) -> Block:
    if not isinstance(block, tuple) or not block:
        raise ValueError("each block must be a non-empty tuple")
    if any(isinstance(index, bool) or not isinstance(index, int) or index < 0 for index in block):
        raise ValueError("block indices must be non-negative integers")
    if len(set(block)) != len(block):
        raise ValueError("block indices must be unique")
    return tuple(sorted(block))


def reverse_boundary_witness_with_trace(
    slot_count: int,
    power: int,
    threshold: int,
    history: tuple[MergeStep, ...],
) -> tuple[tuple[int, ...], tuple[BoundaryTraceStep, ...]]:
    """Replay an oriented history and expose the exact slack-remainder cascade."""
    _require_positive("slot_count", slot_count)
    _require_positive("power", power)
    _require_natural("threshold", threshold)
    if len(history) != slot_count - 1:
        raise ValueError("a complete history must contain slot_count-1 merges")

    normalized = tuple(
        (_normalize_block(receiver), _normalize_block(donor))
        for receiver, donor in history
    )
    full = tuple(range(slot_count))
    totals: dict[Block, int] = {full: 0}
    trace: list[BoundaryTraceStep] = []

    for receiver, donor in reversed(normalized):
        if set(receiver) & set(donor):
            raise ValueError("merged blocks must be disjoint")
        merged = tuple(sorted(receiver + donor))
        if merged not in totals:
            raise ValueError("history is not a valid ordered contraction chain")

        total = totals.pop(merged)
        other_energy = sum(
            balanced_power_energy(len(block), power, value)
            for block, value in totals.items()
        )
        merged_minimum = balanced_power_energy(len(merged), power, total)
        slack = threshold - other_energy - merged_minimum
        if slack < 0:
            raise ValueError("threshold is inconsistent with the current coarse state")

        receiver_total, donor_total, consumed, remainder, next_gap = (
            directed_boundary_decomposition(
                len(receiver), len(donor), power, total, slack
            )
        )
        totals[receiver] = receiver_total
        totals[donor] = donor_total
        trace.append(
            BoundaryTraceStep(
                receiver=receiver,
                donor=donor,
                total=total,
                slack_before=slack,
                receiver_total=receiver_total,
                donor_total=donor_total,
                consumed_excess=consumed,
                slack_after=remainder,
                next_gap=next_gap,
            )
        )

    expected = {tuple((index,)) for index in range(slot_count)}
    if set(totals) != expected:
        raise ValueError("history did not refine to the singleton partition")
    witness = tuple(totals[(index,)] for index in range(slot_count))
    return witness, tuple(trace)


def reverse_boundary_witness(
    slot_count: int,
    power: int,
    threshold: int,
    history: tuple[MergeStep, ...],
) -> tuple[int, ...]:
    """Replay an oriented contraction history as exact right-boundary lifts."""
    witness, _ = reverse_boundary_witness_with_trace(
        slot_count, power, threshold, history
    )
    return witness


def unoriented_partition_chain_count(slot_count: int) -> int:
    """Number of maximal chains from singletons to one block in Pi_N."""
    _require_positive("slot_count", slot_count)
    if slot_count == 1:
        return 1
    return factorial(slot_count) * factorial(slot_count - 1) // (2 ** (slot_count - 1))


def oriented_contraction_history_count(slot_count: int) -> int:
    """Number of complete merge histories when each merge has receiver/donor order."""
    _require_positive("slot_count", slot_count)
    return factorial(slot_count) * factorial(slot_count - 1)
