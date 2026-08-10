"""Fractionless count-ray and defect tools for R004.

Rational probabilities and normalized fractions are treated as external views of
finite count data.  Internally this module keeps non-negative integer count
vectors, integer cross defects, Bell excess/slack, seed-transfer counts, and
record/crossover count words.

Projective count rays, denominator clearing, determinant/cross-product ratio
comparison, Bell inequalities, and finite combinatorial counting are prior
mathematics.  The R004-specific role is to make them the native interface for
its current physical toys so division is not a primitive operation.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from itertools import combinations
from math import comb, gcd

Setting = tuple[int, int]
Outcome = tuple[int, int]
SETTINGS: tuple[Setting, ...] = ((0, 0), (0, 1), (1, 0), (1, 1))
OUTCOMES: tuple[Outcome, ...] = ((-1, -1), (-1, 1), (1, -1), (1, 1))


def _counts(values: Sequence[int], name: str = "counts") -> tuple[int, ...]:
    row = tuple(values)
    if not row:
        raise ValueError(f"{name} must be nonempty")
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in row):
        raise ValueError(f"{name} must be non-negative integers")
    if sum(row) <= 0:
        raise ValueError(f"{name} must have positive total mass")
    return row


def primitive_count_vector(values: Sequence[int]) -> tuple[int, ...]:
    """Unique gcd-normalized integer representative of a rational count ray."""
    row = _counts(values)
    common = 0
    for value in row:
        common = gcd(common, value)
    if common <= 0:
        raise AssertionError("positive count mass must have a positive gcd")
    return tuple(value // common for value in row)


def count_ray_equal(left: Sequence[int], right: Sequence[int]) -> bool:
    """Equality of normalized rational distributions without division."""
    a = _counts(left, "left")
    b = _counts(right, "right")
    if len(a) != len(b):
        raise ValueError("count rays must have equal width")
    total_a = sum(a)
    total_b = sum(b)
    return all(x * total_b == y * total_a for x, y in zip(a, b))


def cross_defect(
    left_part: int,
    left_total: int,
    right_part: int,
    right_total: int,
) -> int:
    """Signed determinant comparing two normalized parts.

    The sign of ``left_part/left_total - right_part/right_total`` is the sign of
    this integer, but no fraction is constructed.
    """
    for value, name in (
        (left_part, "left_part"),
        (right_part, "right_part"),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"{name} must be a non-negative integer")
    for value, name in (
        (left_total, "left_total"),
        (right_total, "right_total"),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
    if left_part > left_total or right_part > right_total:
        raise ValueError("part count cannot exceed total count")
    return left_part * right_total - right_part * left_total


def seed_transfer_defect(left: Sequence[int], right: Sequence[int]) -> int:
    """Minimum atom count that must be reassigned between equal-mass rows.

    This is the total positive excess, equal to half the L1 distance for rows of
    equal total mass, but is computed directly without division.
    """
    a = _counts(left, "left")
    b = _counts(right, "right")
    if len(a) != len(b):
        raise ValueError("rows must have equal width")
    if sum(a) != sum(b):
        raise ValueError("transfer defect requires equal total mass")
    positive = sum(max(x - y, 0) for x, y in zip(a, b))
    negative = sum(max(y - x, 0) for x, y in zip(a, b))
    if positive != negative:
        raise AssertionError("equal-total rows must balance positive and negative transfer")
    return positive


def max_seed_transfer_defect(rows: Mapping[Setting, Sequence[int]]) -> int:
    if set(rows) != set(SETTINGS):
        raise ValueError("one latent count row is required per CHSH setting")
    normalized = {setting: _counts(rows[setting]) for setting in SETTINGS}
    totals = {sum(row) for row in normalized.values()}
    if len(totals) != 1:
        raise ValueError("all setting rows must have equal total mass")
    return max(
        seed_transfer_defect(normalized[left], normalized[right])
        for left, right in combinations(SETTINGS, 2)
    )


def binary_correlation_numerator(counts: Mapping[Outcome, int]) -> tuple[int, int]:
    if set(counts) != set(OUTCOMES):
        raise ValueError("all four binary outcomes are required")
    row = _counts(tuple(counts[outcome] for outcome in OUTCOMES))
    total = sum(row)
    numerator = sum(a * b * counts[(a, b)] for a, b in OUTCOMES)
    return numerator, total


def chsh_count_word(tables: Mapping[Setting, Mapping[Outcome, int]]) -> tuple[int, int]:
    """Return exact CHSH numerator and common setting mass."""
    if set(tables) != set(SETTINGS):
        raise ValueError("all four CHSH setting tables are required")
    correlations: dict[Setting, int] = {}
    totals: set[int] = set()
    for setting in SETTINGS:
        numerator, total = binary_correlation_numerator(tables[setting])
        correlations[setting] = numerator
        totals.add(total)
    if len(totals) != 1:
        raise ValueError("all CHSH setting tables must have equal total mass")
    total = next(iter(totals))
    numerator = (
        correlations[(0, 0)]
        + correlations[(0, 1)]
        + correlations[(1, 0)]
        - correlations[(1, 1)]
    )
    return numerator, total


def bell_excess(numerator: int, total: int) -> int:
    if isinstance(numerator, bool) or not isinstance(numerator, int):
        raise ValueError("numerator must be an integer")
    if isinstance(total, bool) or not isinstance(total, int) or total <= 0:
        raise ValueError("total must be a positive integer")
    return abs(numerator) - 2 * total


def relaxed_bell_slack(numerator: int, total: int, transfer_defect: int) -> int:
    """Integer slack for ``BellExcess <= 6 * seed_transfer_defect``."""
    if isinstance(transfer_defect, bool) or not isinstance(transfer_defect, int) or transfer_defect < 0:
        raise ValueError("transfer_defect must be a non-negative integer")
    return 6 * transfer_defect - bell_excess(numerator, total)


def r004_bell_target_count_tables() -> dict[Setting, dict[Outcome, int]]:
    """Twenty-atom target stored directly as count data, with no Fraction object."""
    return {
        (0, 0): {(-1, -1): 2, (-1, 1): 8, (1, -1): 8, (1, 1): 2},
        (0, 1): {(-1, -1): 2, (-1, 1): 8, (1, -1): 8, (1, 1): 2},
        (1, 0): {(-1, -1): 1, (-1, 1): 9, (1, -1): 9, (1, 1): 1},
        (1, 1): {(-1, -1): 9, (-1, 1): 1, (1, -1): 1, (1, 1): 9},
    }


def r004_sharp_setting_weight_rows() -> dict[Setting, tuple[int, ...]]:
    """Existing 60-atom setting-dependent local witness in integer form."""
    sparse: dict[Setting, dict[int, int]] = {
        (0, 0): {2: 10, 3: 7, 5: 6, 7: 7, 8: 7, 10: 6, 12: 7, 13: 10},
        (0, 1): {2: 6, 3: 7, 5: 10, 7: 7, 8: 7, 10: 10, 12: 7, 13: 6},
        (1, 0): {2: 10, 3: 7, 5: 10, 7: 3, 8: 3, 10: 10, 12: 7, 13: 10},
        (1, 1): {2: 10, 3: 3, 5: 10, 7: 7, 8: 7, 10: 10, 12: 3, 13: 10},
    }
    return {
        setting: tuple(row.get(index, 0) for index in range(16))
        for setting, row in sparse.items()
    }


def threshold_record_count_word(separation: int, resolution: int) -> tuple[int, int]:
    """Return ``(record_agreement, record_separation)`` with sum = resolution."""
    if isinstance(separation, bool) or not isinstance(separation, int) or separation < 0:
        raise ValueError("separation must be a non-negative integer")
    if isinstance(resolution, bool) or not isinstance(resolution, int) or resolution <= 0:
        raise ValueError("resolution must be a positive integer")
    separated = min(separation, resolution)
    return resolution - separated, separated


def threshold_count_margin(
    agreement: int,
    total: int,
    required_numerator: int,
    required_denominator: int,
) -> int:
    """Cross-multiplied margin against an external rational threshold word.

    Nonnegative means ``agreement/total`` reaches the external threshold; the
    internal calculation remains the integer ``required_denominator*agreement -
    required_numerator*total``.
    """
    for value, name in ((agreement, "agreement"), (required_numerator, "required_numerator")):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"{name} must be a non-negative integer")
    for value, name in ((total, "total"), (required_denominator, "required_denominator")):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
    if agreement > total or required_numerator > required_denominator:
        raise ValueError("normalized part cannot exceed its total")
    return required_denominator * agreement - required_numerator * total


def path_crossover_count_word(vertex_count: int, record_resolution: int) -> tuple[int, int]:
    """Return ``(zero_overlap_pairs, overlapping_pairs)`` for path P_N."""
    if isinstance(vertex_count, bool) or not isinstance(vertex_count, int) or vertex_count <= 0:
        raise ValueError("vertex_count must be a positive integer")
    if isinstance(record_resolution, bool) or not isinstance(record_resolution, int) or record_resolution <= 0:
        raise ValueError("record_resolution must be a positive integer")
    total = comb(vertex_count, 2)
    zero = 0 if vertex_count <= record_resolution else comb(vertex_count - record_resolution + 1, 2)
    return zero, total - zero


def path_crossover_growth_cross_defect(vertex_count: int, record_resolution: int) -> int:
    """Integer proof that the normalized zero-overlap share is nondecreasing.

    If Z_N/T_N is the conventional normalized view, this returns
    ``Z_(N+1)*T_N - Z_N*T_(N+1)`` directly.  No quotient is formed.
    """
    if vertex_count < 2:
        raise ValueError("vertex_count must be at least two")
    zero, overlap = path_crossover_count_word(vertex_count, record_resolution)
    next_zero, next_overlap = path_crossover_count_word(vertex_count + 1, record_resolution)
    total = zero + overlap
    next_total = next_zero + next_overlap
    return next_zero * total - zero * next_total
