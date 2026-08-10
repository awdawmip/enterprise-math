"""Exact finite Bell/CHSH obstruction for R004 latent-completion research.

The module is deliberately integer/rational-first.  It does not claim Bell,
CHSH, or relaxed-measurement-independence mathematics as Enterprise Math
inventions.  R004 uses those established boundaries to answer a narrower
question left open by its finite response-table no-go: which explicit
restrictions make a pre-sampled finite completion fail, and how much relaxation
is required to restore one for one exact rational target?
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from typing import Mapping, Sequence

Setting = tuple[int, int]
ResponseTable = tuple[int, int, int, int]
SETTINGS: tuple[Setting, ...] = ((0, 0), (0, 1), (1, 0), (1, 1))


def _sign(value: int, name: str = "outcome") -> None:
    if isinstance(value, bool) or value not in (-1, 1):
        raise ValueError(f"{name} must be -1 or 1")


def local_response_tables() -> tuple[ResponseTable, ...]:
    """All deterministic setting-local binary response tables.

    A table is ``(A_0,A_1,B_0,B_1)``.  Alice's response therefore depends only
    on her local setting and the already-selected table; Bob's response depends
    only on his local setting and the same table.
    """
    return tuple(product((-1, 1), repeat=4))


def deterministic_chsh(table: ResponseTable) -> int:
    if len(table) != 4:
        raise ValueError("response table must have four local outcomes")
    a0, a1, b0, b1 = table
    for value in table:
        _sign(value)
    return a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1


def _weight_row(weights: Sequence[int]) -> tuple[int, ...]:
    row = tuple(weights)
    if len(row) != len(local_response_tables()):
        raise ValueError("one non-negative integer weight is required per table")
    if any(
        isinstance(weight, bool) or not isinstance(weight, int) or weight < 0
        for weight in row
    ):
        raise ValueError("weights must be non-negative integers")
    if sum(row) <= 0:
        raise ValueError("at least one latent seed atom is required")
    return row


def weighted_local_chsh(weights: Sequence[int]) -> tuple[int, int]:
    """Return the exact CHSH numerator and common seed weight.

    The same weights are used for all four setting pairs, encoding measurement-
    setting independence.  Every valid local mixture obeys
    ``abs(numerator)<=2*total``.
    """
    tables = local_response_tables()
    row = _weight_row(weights)
    total = sum(row)
    numerator = sum(
        weight * deterministic_chsh(table)
        for weight, table in zip(row, tables)
    )
    return numerator, total


def local_chsh_bound_holds(weights: Sequence[int]) -> bool:
    numerator, total = weighted_local_chsh(weights)
    return abs(numerator) <= 2 * total


def weighted_local_correlations(weights: Sequence[int]) -> dict[Setting, Fraction]:
    tables = local_response_tables()
    row = _weight_row(weights)
    total = sum(row)
    correlations: dict[Setting, Fraction] = {}
    for x, y in SETTINGS:
        value = 0
        for weight, table in zip(row, tables):
            a0, a1, b0, b1 = table
            a = (a0, a1)[x]
            b = (b0, b1)[y]
            value += weight * a * b
        correlations[(x, y)] = Fraction(value, total)
    return correlations


def local_joint_counts_for_setting(
    weights: Sequence[int], setting: Setting
) -> dict[tuple[int, int], int]:
    if setting not in SETTINGS:
        raise ValueError("unknown CHSH setting")
    row = _weight_row(weights)
    x, y = setting
    output = {outcome: 0 for outcome in product((-1, 1), repeat=2)}
    for weight, table in zip(row, local_response_tables()):
        a0, a1, b0, b1 = table
        output[((a0, a1)[x], (b0, b1)[y])] += weight
    return output


def chsh_value(correlations: Mapping[Setting, Fraction]) -> Fraction:
    if set(correlations) != set(SETTINGS):
        raise ValueError("exactly four CHSH setting correlations are required")
    if any(not isinstance(value, Fraction) for value in correlations.values()):
        raise ValueError("correlations must be exact Fractions")
    return (
        correlations[(0, 0)]
        + correlations[(0, 1)]
        + correlations[(1, 0)]
        - correlations[(1, 1)]
    )


def _setting_weight_rows(
    weights_by_setting: Mapping[Setting, Sequence[int]],
) -> tuple[dict[Setting, tuple[int, ...]], int]:
    if set(weights_by_setting) != set(SETTINGS):
        raise ValueError("one weight row is required for every CHSH setting")
    rows = {setting: _weight_row(weights_by_setting[setting]) for setting in SETTINGS}
    totals = {sum(row) for row in rows.values()}
    if len(totals) != 1:
        raise ValueError("all setting-dependent rows must have the same total weight")
    return rows, next(iter(totals))


def setting_dependent_local_correlations(
    weights_by_setting: Mapping[Setting, Sequence[int]],
) -> dict[Setting, Fraction]:
    rows, total = _setting_weight_rows(weights_by_setting)
    tables = local_response_tables()
    output: dict[Setting, Fraction] = {}
    for setting in SETTINGS:
        x, y = setting
        numerator = 0
        for weight, table in zip(rows[setting], tables):
            a0, a1, b0, b1 = table
            numerator += weight * (a0, a1)[x] * (b0, b1)[y]
        output[setting] = Fraction(numerator, total)
    return output


def setting_dependent_chsh_numerator(
    weights_by_setting: Mapping[Setting, Sequence[int]],
) -> tuple[int, int]:
    rows, total = _setting_weight_rows(weights_by_setting)
    correlations = setting_dependent_local_correlations(rows)
    value = chsh_value(correlations) * total
    if value.denominator != 1:
        raise AssertionError("integer setting weights must give an integer CHSH numerator")
    return value.numerator, total


def max_l1_setting_distance(
    weights_by_setting: Mapping[Setting, Sequence[int]],
) -> int:
    rows, _ = _setting_weight_rows(weights_by_setting)
    return max(
        sum(abs(left - right) for left, right in zip(rows[s], rows[t]))
        for s, t in combinations(SETTINGS, 2)
    )


def maximum_setting_total_variation(
    weights_by_setting: Mapping[Setting, Sequence[int]],
) -> Fraction:
    rows, total = _setting_weight_rows(weights_by_setting)
    del rows
    return Fraction(max_l1_setting_distance(weights_by_setting), 2 * total)


def relaxed_measurement_dependence_bound_holds(
    weights_by_setting: Mapping[Setting, Sequence[int]],
) -> bool:
    """Finite relaxed CHSH bound ``|N| <= 2W + 3D``.

    ``D`` is the maximum L1 distance between any two equal-total setting weight
    rows.  Taking the `(0,0)` row as a reference gives an ordinary local CHSH
    numerator bounded by `2W`; each of the other three setting rows can change
    one binary correlation numerator by at most `D`.  Hence the displayed
    integer inequality.  In total-variation units `M=D/(2W)`, this is
    ``|S|<=2+6M``.
    """
    numerator, total = setting_dependent_chsh_numerator(weights_by_setting)
    distance = max_l1_setting_distance(weights_by_setting)
    return abs(numerator) <= 2 * total + 3 * distance


def _rational_unit_vector(x: int, y: int, denominator: int) -> tuple[int, int, int]:
    if isinstance(denominator, bool) or not isinstance(denominator, int) or denominator <= 0:
        raise ValueError("denominator must be positive")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in (x, y)):
        raise ValueError("vector coordinates must be integers")
    if x * x + y * y != denominator * denominator:
        raise ValueError("coordinates must form an exact rational unit vector")
    return x, y, denominator


def _dot(left: tuple[int, int, int], right: tuple[int, int, int]) -> Fraction:
    lx, ly, ld = left
    rx, ry, rd = right
    return Fraction(lx * rx + ly * ry, ld * rd)


def rational_singlet_correlations() -> dict[Setting, Fraction]:
    """One exact rational CHSH-violating singlet correlation table."""
    alice = (
        _rational_unit_vector(1, 0, 1),
        _rational_unit_vector(0, 1, 1),
    )
    bob = (
        _rational_unit_vector(3, 4, 5),
        _rational_unit_vector(3, -4, 5),
    )
    return {
        (x, y): -_dot(alice[x], bob[y])
        for x, y in SETTINGS
    }


def rational_singlet_joint_counts() -> dict[Setting, dict[tuple[int, int], int]]:
    """Exact 20-atom joint counts for the rational singlet target."""
    correlations = rational_singlet_correlations()
    output: dict[Setting, dict[tuple[int, int], int]] = {}
    for setting, correlation in correlations.items():
        counts: dict[tuple[int, int], int] = {}
        for a, b in product((-1, 1), repeat=2):
            probability = Fraction(1 + a * b * correlation, 4)
            count = probability * 20
            if count.denominator != 1:
                raise AssertionError("selected rational target must clear at denominator 20")
            counts[(a, b)] = count.numerator
        output[setting] = counts
    return output


def correlation_from_joint_counts(counts: Mapping[tuple[int, int], int]) -> Fraction:
    required = {(-1, -1), (-1, 1), (1, -1), (1, 1)}
    if set(counts) != required:
        raise ValueError("all four binary joint outcomes are required")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in counts.values()
    ):
        raise ValueError("joint counts must be non-negative integers")
    total = sum(counts.values())
    if total <= 0:
        raise ValueError("joint table must be nonempty")
    numerator = sum(a * b * counts[(a, b)] for a, b in required)
    return Fraction(numerator, total)


def rational_target_sharp_measurement_dependent_weights() -> dict[Setting, tuple[int, ...]]:
    """Explicit denominator-60 local model saturating M=2/15.

    The response functions remain setting-local, but the latent distribution is
    allowed to depend on the joint setting.  Each row has total weight 60.  All
    six pairwise L1 distances are 16, hence all pairwise total-variation
    distances are `16/(2*60)=2/15`.  The observed joint counts are exactly three
    times the twenty-atom rational singlet tables.
    """
    rows: dict[Setting, dict[int, int]] = {
        (0, 0): {2: 10, 3: 7, 5: 6, 7: 7, 8: 7, 10: 6, 12: 7, 13: 10},
        (0, 1): {2: 6, 3: 7, 5: 10, 7: 7, 8: 7, 10: 10, 12: 7, 13: 6},
        (1, 0): {2: 10, 3: 7, 5: 10, 7: 3, 8: 3, 10: 10, 12: 7, 13: 10},
        (1, 1): {2: 10, 3: 3, 5: 10, 7: 7, 8: 7, 10: 10, 12: 3, 13: 10},
    }
    return {
        setting: tuple(row.get(index, 0) for index in range(16))
        for setting, row in rows.items()
    }


def rational_target_measurement_dependence_minimum() -> Fraction:
    """Return the proved sharp max-TV cost `2/15` for the selected target.

    Lower bound: `|S|<=2+6M` and `|S|=14/5` imply `M>=2/15`.
    Upper bound: ``rational_target_sharp_measurement_dependent_weights`` has
    max pairwise TV exactly `2/15` and reproduces every target joint table.
    """
    target = rational_singlet_joint_counts()
    witness = rational_target_sharp_measurement_dependent_weights()
    for setting in SETTINGS:
        observed = local_joint_counts_for_setting(witness[setting], setting)
        if observed != {outcome: 3 * count for outcome, count in target[setting].items()}:
            raise AssertionError("sharp witness must reproduce the rational target")
    cost = maximum_setting_total_variation(witness)
    if cost != Fraction(2, 15):
        raise AssertionError("sharp witness must attain total-variation cost 2/15")
    return cost
