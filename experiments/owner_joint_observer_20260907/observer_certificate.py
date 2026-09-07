"""Noncanonical X6 raw-observer adapter reusing the exact BRC histogram carrier.

This experiment proves only its finite certificates. It does not establish the
separate seven-support uniqueness theorem or register a new tool family.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path
import sys
from typing import Iterable, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from enterprise_math.brc_histogram import WeightHistogram
from enterprise_math.operation_quotient import operation_descends, stable_family_partition


@dataclass(frozen=True)
class Branch:
    label: str
    coordinate: tuple[int, ...]
    weight: Fraction = Fraction(1)

    def __post_init__(self) -> None:
        if not isinstance(self.label, str) or not self.label:
            raise ValueError("branch label must be a nonempty string")
        coordinate = tuple(self.coordinate)
        if len(coordinate) != 6 or any(type(x) is not int for x in coordinate):
            raise ValueError("coordinate must contain six signed integers")
        if isinstance(self.weight, bool) or not isinstance(self.weight, (int, Fraction)):
            raise TypeError("weight must be an int or Fraction")
        if self.weight <= 0:
            raise ValueError("branch weight must be positive")
        object.__setattr__(self, "coordinate", coordinate)
        object.__setattr__(self, "weight", Fraction(self.weight))


def _axes(axes: Sequence[int]) -> tuple[int, ...]:
    result = tuple(axes)
    if not result or len(set(result)) != len(result):
        raise ValueError("axes must be nonempty and distinct")
    if any(type(axis) is not int or not 0 <= axis < 6 for axis in result):
        raise ValueError("axis indices must be integers from 0 to 5")
    return result


def _branches(branches: Iterable[Branch]) -> tuple[Branch, ...]:
    result = tuple(branches)
    if not all(isinstance(branch, Branch) for branch in result):
        raise TypeError("expected Branch values")
    if len({branch.label for branch in result}) != len(result):
        raise ValueError("branch labels must be unique within a population")
    return result


def fiber_histograms(
    branches: Iterable[Branch], axes: Sequence[int]
) -> dict[tuple[int, ...], WeightHistogram]:
    """Observe raw signed X6 fibers without modifying the source branches."""
    selected = _axes(axes)
    buckets: dict[tuple[int, ...], list[Fraction]] = {}
    for branch in _branches(branches):
        key = tuple(branch.coordinate[axis] for axis in selected)
        buckets.setdefault(key, []).append(branch.weight)
    return {key: WeightHistogram.from_weights(weights) for key, weights in sorted(buckets.items())}


def raw_marginal_table(
    branches: Iterable[Branch], axes: Sequence[int]
) -> dict[tuple[int, ...], Fraction]:
    return {key: histogram.total_mass for key, histogram in fiber_histograms(branches, axes).items()}


def all_three_axis_tables(
    branches: Iterable[Branch],
) -> dict[tuple[int, ...], dict[tuple[int, ...], Fraction]]:
    population = _branches(branches)
    return {axes: raw_marginal_table(population, axes) for axes in combinations(range(6), 3)}


def parity_branches(parity: int) -> tuple[Branch, ...]:
    """Eight unit branches in a four-axis cube inside native signed X6."""
    if type(parity) is not int or parity not in (0, 1):
        raise ValueError("parity must be 0 or 1")
    return tuple(
        Branch(f"p{parity}:{''.join(map(str, bits))}", tuple(bits) + (0, 0), Fraction(1))
        for bits in product((0, 1), repeat=4)
        if sum(bits) % 2 == parity
    )


def cylinder_filter(
    branches: Iterable[Branch], axes: Sequence[int], address: Sequence[int]
) -> tuple[Branch, ...]:
    selected = _axes(axes)
    target = tuple(address)
    if len(selected) != len(target) or any(type(value) is not int for value in target):
        raise ValueError("cylinder address must have one integer for each selected axis")
    return tuple(
        branch for branch in _branches(branches)
        if tuple(branch.coordinate[axis] for axis in selected) == target
    )


def _q(value: Fraction) -> str:
    return str(value)


def _histogram_record(histogram: WeightHistogram) -> dict:
    return {
        "weight_histogram": [[_q(weight), count] for weight, count in histogram.entries],
        "CWM": {"C": histogram.count, "W": _q(histogram.total_mass), "M": _q(histogram.dominant_mass)},
        "dominant_degeneracy": histogram.dominant_degeneracy,
        "prime_valuation_terms": [
            {"valuation": [list(term) for term in valuation], "count": count}
            for valuation, count in histogram.prime_valuation_terms()
        ],
    }


def _branch_records(branches: Iterable[Branch]) -> list[dict]:
    return [{"label": b.label, "coordinate": list(b.coordinate), "weight": _q(b.weight)} for b in branches]


def parity_certificate() -> dict:
    even, odd = parity_branches(0), parity_branches(1)
    comparisons = []
    zero = WeightHistogram.from_weights(())
    for axes in combinations(range(6), 3):
        left, right = fiber_histograms(even, axes), fiber_histograms(odd, axes)
        fibers = []
        for address in sorted(set(left) | set(right)):
            left_hist, right_hist = left.get(address, zero), right.get(address, zero)
            fibers.append({
                "address": list(address),
                "left": _histogram_record(left_hist),
                "right": _histogram_record(right_hist),
                "histogram_equal": left_hist == right_hist,
                "left_source_labels": [b.label for b in cylinder_filter(even, axes, address)],
                "right_source_labels": [b.label for b in cylinder_filter(odd, axes, address)],
            })
        comparisons.append({"axes_zero_based": list(axes), "histograms_equal": left == right, "fibers": fibers})

    four_axes = (0, 1, 2, 3)
    left4, right4 = raw_marginal_table(even, four_axes), raw_marginal_table(odd, four_axes)
    four_differences = [
        {"address": list(key), "left_mass": _q(left4.get(key, Fraction(0))),
         "right_mass": _q(right4.get(key, Fraction(0)))}
        for key in sorted(set(left4) | set(right4)) if left4.get(key, 0) != right4.get(key, 0)
    ]
    cylinder = (0, 0, 0, 0)
    selected_even, selected_odd = cylinder_filter(even, four_axes, cylinder), cylinder_filter(odd, four_axes, cylinder)
    selected_left = WeightHistogram.from_weights(b.weight for b in selected_even)
    selected_right = WeightHistogram.from_weights(b.weight for b in selected_odd)
    populations = {"even": even, "odd": odd, "origin": selected_even, "empty": selected_odd}
    initial_partition = {
        name: tuple(
            (axes, tuple((address, histogram.entries) for address, histogram in fiber_histograms(population, axes).items()))
            for axes in combinations(range(6), 3)
        )
        for name, population in populations.items()
    }
    operation = {"even": "origin", "odd": "empty", "origin": "origin", "empty": "empty"}
    descends = operation_descends(populations, operation, initial_partition)
    repaired = stable_family_partition(populations, {"four_axis_cylinder": operation}, initial_partition)
    # This is a signed OBSERVER of two positive BRC populations, not signed BRC mass.
    joint_left = sum(((-1) ** sum(b.coordinate[:4])) * b.weight for b in even)
    joint_right = sum(((-1) ** sum(b.coordinate[:4])) * b.weight for b in odd)
    assert len(even) == len(odd) == 8
    assert len(comparisons) == 20 and all(row["histograms_equal"] for row in comparisons)
    assert len(four_differences) == 16
    assert (selected_left.total_mass, selected_right.total_mass) == (Fraction(1), Fraction(0))
    assert (joint_left, joint_right) == (Fraction(8), Fraction(-8))
    assert not descends and len(set(initial_partition.values())) == 3 and len(set(repaired.values())) == 4
    return {
        "schema": "OWNER_X6_JOINT_OBSERVER_FINITE_CERTIFICATE_V1",
        "status": "NONCANONICAL_EXPERIMENT_EXACT_FINITE_CHECK",
        "source_snapshot": "ef1893382",
        "foundation": "X6 affine Cell torsor Z^6; raw signed coordinate observers; chosen Cell origin retained",
        "reuse": {
            "method": "t0.weighted_brc_histogram", "state": "REUSE_EXECUTED",
            "implementation": "src/enterprise_math/brc_histogram.py",
            "calls": ["WeightHistogram.from_weights", "count", "total_mass", "dominant_mass", "dominant_degeneracy", "prime_valuation_terms"],
        },
        "claim_boundary": "Finite 8-vs-8 collision certificate only; no seven-support uniqueness proof, global observer equivalence, theorem promotion or new tool family.",
        "observer_scope": "All 20 raw three-axis fiber histograms, including CWM and exact weight valuations. Source labels remain in attached provenance and are not asserted equal.",
        "left_population": _branch_records(even), "right_population": _branch_records(odd),
        "three_axis_comparisons": comparisons,
        "all_three_axis_histograms_equal": all(row["histograms_equal"] for row in comparisons),
        "four_axis_difference": {"axes_zero_based": list(four_axes), "different_addresses": four_differences},
        "joint_observer": {"formula": "sum_x mass(x) * (-1)^(x0+x1+x2+x3)", "left": _q(joint_left), "right": _q(joint_right)},
        "future_operation_failure": {
            "operation": "retain only the four-axis cylinder x0=x1=x2=x3=0, then read total mass",
            "horizon": 1, "left": _histogram_record(selected_left), "right": _histogram_record(selected_right),
            "conclusion": "The three-axis histogram observer does not support this future operation; retain a joint coordinate or the original population.",
        },
        "T6_exact_reuse": {
            "method": "quotient.operation_family_closure", "state": "REUSE_EXECUTED",
            "implementation": "src/enterprise_math/operation_quotient.py",
            "calls": ["operation_descends", "stable_family_partition"],
            "declared_finite_population_states": list(populations),
            "operation": operation, "initial_class_count": len(set(initial_partition.values())),
            "operation_descends": descends, "coarsest_stable_refinement": repaired,
            "repaired_class_count": len(set(repaired.values())),
            "scope": "Only this four-state carrier and repetitions of the declared idempotent cylinder filter; no unrestricted X6 minimality claim.",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("parity_certificate.json"))
    args = parser.parse_args()
    certificate = parity_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"output": str(args.output.resolve()), "three_axis_tables": 20,
                      "equal_histograms": certificate["all_three_axis_histograms_equal"],
                      "four_axis_differences": 16, "future_cylinder_mass": ["1", "0"]}, indent=2))


if __name__ == "__main__":
    main()
