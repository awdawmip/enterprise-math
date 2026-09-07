"""Typed X6 joint-histogram consumer, not a new BRC family or general solver.

All twenty raw three-axis tables share one chart. Missing fibers mean zero.
Exact weights are positive rationals; their branch counts remain integers.
Only the uniform binary six-axis family is classified here. A general input
is UNCLASSIFIED even if its mass relaxation happens to have a rational answer.
"""
from __future__ import annotations

from collections.abc import Iterable, Mapping
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import sys

from observer_certificate import Branch, fiber_histograms
from enterprise_math.brc_histogram import WeightHistogram, histogram_recoalesce

EXPERIMENTS = Path(__file__).resolve().parents[1]
if str(EXPERIMENTS) not in sys.path:
    sys.path.insert(0, str(EXPERIMENTS))
from owner_branch_scout_20260907 import binary_x6_strength3_generators


AXES = tuple(combinations(range(6), 3))
ZERO = WeightHistogram.from_weights(())


def stratify_histogram_tables(tables: Mapping) -> dict:
    """Validate and defensively copy tables; split counts by exact weight.

    The returned integer layers state M n_q=c_q with n_q in N_0. This function
    checks format and equal per-weight totals, not global realizability.
    """
    if not isinstance(tables, Mapping):
        raise TypeError("tables must be a mapping of all 20 sorted axis triples")
    if any(not isinstance(axes, tuple) or len(axes) != 3
           or any(type(axis) is not int for axis in axes) or axes not in AXES
           for axes in tables):
        raise ValueError("axis labels must be sorted triples of distinct integer axes 0..5")
    if set(tables) != set(AXES):
        raise ValueError("exactly the 20 sorted raw three-axis tables are required")
    copied = {}
    weights = set()
    for axes in AXES:
        if not isinstance(tables[axes], Mapping):
            raise TypeError("each raw fiber table must be a mapping")
        table = {}
        for address, histogram in tables[axes].items():
            if not isinstance(address, tuple) or len(address) != 3 or any(type(x) is not int for x in address):
                raise ValueError("raw fiber addresses must be triples of signed integers")
            if not isinstance(histogram, WeightHistogram):
                raise TypeError("each fiber value must be a WeightHistogram, not total mass")
            # Freeze both container levels and rerun the base validation.
            # Do not coerce numeric values: bool/float data must stay invalid.
            # This also removes subclasses that change readout properties.
            exact = WeightHistogram(tuple(tuple(entry) for entry in histogram.entries))
            if not exact.is_zero:
                table[address] = exact
                weights.update(weight for weight, _ in exact.entries)
        copied[axes] = dict(sorted(table.items()))
    weights = tuple(sorted(weights))
    layers = {weight: {axes: {} for axes in AXES} for weight in weights}
    for axes, table in copied.items():
        for address, histogram in table.items():
            for weight, count in histogram.entries:
                layers[weight][axes][address] = count
    totals = {}
    for weight, layer in layers.items():
        observed_totals = {sum(table.values()) for table in layer.values()}
        if len(observed_totals) != 1:
            raise ValueError(f"marginal branch-count totals disagree for exact weight {weight}")
        totals[weight] = observed_totals.pop()
    return {"tables": copied, "weights": weights, "count_layers": layers,
            "branch_totals": totals, "coefficient_domain": "NONNEGATIVE_INTEGERS",
            "global_realizability": "NOT_CHECKED"}


def verify_histogram_realization(tables: Mapping, branches: Iterable[Branch]) -> dict:
    """Recompute every full histogram and return all fiber/weight comparisons.

    Generated labels distinguish witness occurrences only; this check does not
    assert recovery of erased source identities. Unlisted fibers are zero.
    """
    strata = stratify_histogram_tables(tables)
    population = tuple(branches)
    if not all(isinstance(branch, Branch) for branch in population):
        raise TypeError("a realization must contain Branch objects")
    # Revalidate and freeze each record before computing any observations.
    population = tuple(Branch(branch.label, branch.coordinate, branch.weight) for branch in population)
    if len({branch.label for branch in population}) != len(population):
        raise ValueError("realization branch labels must be unique")
    comparisons = []
    actual_tables = {}
    for axes in AXES:
        expected = strata["tables"][axes]
        actual = fiber_histograms(population, axes)
        actual_tables[axes] = actual
        for address in sorted(set(expected) | set(actual)):
            left, right = expected.get(address, ZERO), actual.get(address, ZERO)
            left_counts, right_counts = dict(left.entries), dict(right.entries)
            weight_comparisons = tuple(
                {"weight": weight, "expected_count": left_counts.get(weight, 0),
                 "actual_count": right_counts.get(weight, 0),
                 "equal": left_counts.get(weight, 0) == right_counts.get(weight, 0)}
                for weight in sorted(set(left_counts) | set(right_counts))
            )
            comparisons.append({
                "axes": axes, "address": address, "expected_histogram": left,
                "actual_histogram": right, "histogram_equal": left == right,
                "expected_mass": left.total_mass, "actual_mass": right.total_mass,
                "mass_equal": left.total_mass == right.total_mass,
                "weight_comparisons": weight_comparisons,
            })
    mismatches = tuple(row for row in comparisons if not row["histogram_equal"])
    return {"valid": not mismatches,
            "status": "VERIFIED_EXACT_HISTOGRAM_REALIZATION" if not mismatches else "HISTOGRAM_MISMATCH",
            "branch_count": len(population), "checked_axis_tables": AXES,
            "comparisons": tuple(comparisons), "mismatches": mismatches,
            "all_mass_tables_match": all(row["mass_equal"] for row in comparisons),
            "actual_tables": actual_tables, "unlisted_fibers_are_zero": True}


def _uniform_binary_signature(strata: dict):
    tables = strata["tables"]
    if not strata["weights"]:
        return None, ZERO
    levels = [set() for _ in range(6)]
    for axes, table in tables.items():
        for address in table:
            for axis, value in zip(axes, address):
                levels[axis].add(value)
    if any(len(values) != 2 for values in levels):
        return None
    levels = tuple(tuple(sorted(values)) for values in levels)
    common = next(iter(tables[AXES[0]].values()))
    for axes, table in tables.items():
        expected_addresses = set(product(*(levels[axis] for axis in axes)))
        if set(table) != expected_addresses or any(histogram != common for histogram in table.values()):
            return None
    return levels, common


def _rao_certificate(levels, weight):
    supports = ((),) + tuple((axis,) for axis in range(6)) + tuple((0, axis) for axis in range(1, 6))
    return {"kind": "BINARY_X6_STRENGTH3_RAO", "weight": weight,
            "axis_levels": levels, "per_fiber_count": 1, "branch_rows": 8,
            "character_supports": supports, "gram_rank": 12,
            "contradiction": "12 mutually orthogonal nonzero character columns cannot fit in 8 branch rows"}


def verify_rao_obstruction(tables: Mapping, certificate: Mapping) -> bool:
    """Independently bind the finite Rao rank obstruction to original tables."""
    strata = stratify_histogram_tables(tables)
    signature = _uniform_binary_signature(strata)
    if signature is None or not strata["weights"] or not isinstance(certificate, Mapping):
        return False
    levels, common = signature
    weight = certificate.get("weight")
    if isinstance(weight, bool) or not isinstance(weight, Fraction):
        return False
    if any(type(certificate.get(field)) is not int for field in ("per_fiber_count", "branch_rows", "gram_rank")):
        return False
    certified_levels = certificate.get("axis_levels")
    if (not isinstance(certified_levels, tuple) or len(certified_levels) != 6
        or any(not isinstance(pair, tuple) or len(pair) != 2
               or any(type(value) is not int for value in pair) for pair in certified_levels)):
        return False
    certified_supports = certificate.get("character_supports")
    if (not isinstance(certified_supports, tuple)
        or any(not isinstance(support, tuple) or any(type(axis) is not int for axis in support)
               for support in certified_supports)):
        return False
    if dict(common.entries).get(weight) != 1 or dict(certificate) != _rao_certificate(levels, weight):
        return False
    supports = tuple(frozenset(support) for support in certificate["character_supports"])
    # Uniform triples force every nonempty <=3-axis character sum to vanish.
    # Products cancel repeated axes; these selected supports never need degree 4.
    if len(set(supports)) != 12 or not all(1 <= len(a ^ b) <= 3 for a, b in combinations(supports, 2)):
        return False
    return strata["branch_totals"][weight] == 8 and len(supports) > 8


def realize_uniform_binary_histograms(tables: Mapping, *, max_branches: int = 10000) -> dict:
    """Classify/construct common-histogram binary X6 tables, weight by weight.

    For each exact weight, the allowed uniform multiplicities are 0 or >=2.
    Count 1 gives a Rao certificate. Other inputs return UNCLASSIFIED, with no
    integer inference from a rational mass solution. A witness budget limits
    materialization only and is explicitly separate from mathematical status.
    """
    strata = stratify_histogram_tables(tables)
    if type(max_branches) is not int or max_branches < 0:
        raise ValueError("max_branches must be a nonnegative integer")
    signature = _uniform_binary_signature(strata)
    if signature is None:
        return {"status": "UNCLASSIFIED", "reason": "outside the common-histogram binary X6 family",
                "strata": strata}
    levels, common = signature
    for weight, multiplicity in common.entries:
        if multiplicity == 1:
            certificate = _rao_certificate(levels, weight)
            if not verify_rao_obstruction(tables, certificate):
                raise ArithmeticError("constructed Rao certificate did not verify")
            return {"status": "INFEASIBLE_BY_RAO", "certificate": certificate,
                    "certificate_verified": True, "strata": strata}
    count = 8 * common.count
    if count > max_branches:
        return {"status": "WITNESS_BUDGET_EXCEEDED", "mathematical_status": "UNIFORM_FAMILY_REALIZABLE",
                "required_branches": count, "strata": strata}
    population = []
    if common.entries:
        index_two, index_three = binary_x6_strength3_generators()
        for weight, multiplicity in common.entries:
            b = multiplicity % 2
            a = (multiplicity - 3 * b) // 2
            # Actual reuse of the BRC alternative/recoalescence operation.
            composed = histogram_recoalesce(WeightHistogram.from_counts({weight: 2 * a}),
                                            WeightHistogram.from_counts({weight: 3 * b}))
            if composed != WeightHistogram.from_counts({weight: multiplicity}):
                raise ArithmeticError("BRC uniform multiplicity composition failed")
            for row in index_two * a + index_three * b:
                coordinate = tuple(levels[axis][bit] for axis, bit in enumerate(row))
                population.append(Branch(f"histogram-witness:{len(population)}", coordinate, weight))
    population = tuple(population)
    verification = verify_histogram_realization(tables, population)
    if not verification["valid"]:
        raise ArithmeticError("constructed realization failed complete histogram verification")
    return {"status": "REALIZED", "branches": population, "verification": verification,
            "axis_levels": levels, "strata": strata,
            "source_identity_status": "GENERATED_WITNESS_LABELS_NOT_RECOVERED_SOURCE_LABELS"}
