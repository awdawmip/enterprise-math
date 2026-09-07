"""Compact reproducible witnesses for three distinct X6/BRC input contracts."""
from __future__ import annotations

from dataclasses import asdict, is_dataclass
from fractions import Fraction
from itertools import product
import json
from pathlib import Path

from histogram_realization import (
    AXES, WeightHistogram, realize_uniform_binary_histograms,
    verify_histogram_realization, verify_rao_obstruction,
)
from noisy_recovery import fit_budgeted_noise
from observer_certificate import Branch, all_three_axis_tables
from exact_feasibility import verify_certificate


def json_value(value):
    if isinstance(value, Fraction):
        return str(value)
    if is_dataclass(value):
        return json_value(asdict(value))
    if isinstance(value, dict):
        return {key: json_value(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [json_value(item) for item in value]
    return value


def uniform_tables(histogram):
    return {axes: {address: histogram for address in product((0, 1), repeat=3)} for axes in AXES}


def run():
    unit = uniform_tables(WeightHistogram.from_counts({1: 1}))
    obstruction = realize_uniform_binary_histograms(unit)
    assert obstruction["status"] == "INFEASIBLE_BY_RAO"
    assert verify_rao_obstruction(unit, obstruction["certificate"])
    relaxed = tuple(Branch(f"mass-only:{i}", point, Fraction(1, 8))
                    for i, point in enumerate(product((0, 1), repeat=6)))
    rejected = verify_histogram_realization(unit, relaxed)
    assert rejected["all_mass_tables_match"] and not rejected["valid"]

    common = WeightHistogram.from_counts({Fraction(2, 3): 2, Fraction(7, 11): 3})
    mixed = realize_uniform_binary_histograms(uniform_tables(common))
    assert mixed["status"] == "REALIZED" and mixed["verification"]["valid"]
    assert len(mixed["branches"]) == 40

    origin = (0,) * 6
    noise = all_three_axis_tables((Branch("truth-example", origin, Fraction(1)),))
    noise[AXES[0]][(9, 8, 7)] = Fraction(-1, 10)
    fit = fit_budgeted_noise(noise, [origin], residual_budget=Fraction(1, 10),
                            truth_noise_budget=Fraction(1, 10))
    assert fit["distribution"] == ((origin, Fraction(1)),)
    assert fit["actual_stacked_l1_residual"] == Fraction(1, 10)
    assert fit["conditional_l1_bound"] == Fraction(111, 100)
    assert verify_certificate(fit["compiled_matrix"], fit["compiled_rhs"], fit["certificate"])
    return {
        "status": "PASS",
        "scope": "reproducible finite examples; no Foundation promotion or general integer solver",
        "uniform_unit_histogram": {
            "input": "every address of all20 binary raw triple tables has histogram 1[1]",
            "rao_certificate": obstruction["certificate"],
            "mass_only_relaxation": "64 binary X6 Cells each carry mass 1/8",
            "mass_relaxation_passes": rejected["all_mass_tables_match"],
            "histogram_relaxation_passes": rejected["valid"],
            "mismatching_fibers": len(rejected["mismatches"]),
        },
        "uniform_mixed_histogram": {
            "common_fiber_histogram": common.entries,
            "witness_branches": mixed["branches"],
            "checked_fibers": len(mixed["verification"]["comparisons"]),
            "all_histograms_match": mixed["verification"]["valid"],
        },
        "budgeted_noise_fit": {
            "input": "unit origin raw marginals plus -1/10 at axes012 address(9,8,7)",
            "declared_carrier": [origin],
            "distribution": fit["distribution"],
            "actual_residual": fit["actual_stacked_l1_residual"],
            "conditional_l1_bound": fit["conditional_l1_bound"],
            "conditional_assumptions": fit["conditional_l1_bound_assumptions"],
            "compiled_matrix": fit["compiled_matrix"],
            "compiled_rhs": fit["compiled_rhs"],
            "observation_rows": fit["observation_rows"],
            "certificate": fit["certificate"],
        },
    }


if __name__ == "__main__":
    output = Path(__file__).with_suffix(".json")
    payload = json_value(run())
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8", newline="\n")
    print(json.dumps({"status": payload["status"], "output": str(output)}))
