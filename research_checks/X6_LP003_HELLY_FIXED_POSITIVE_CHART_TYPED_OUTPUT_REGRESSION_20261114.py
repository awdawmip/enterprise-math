#!/usr/bin/env python3
"""Optimization-safe regression for the Helly S12 chart/native-X6 interface.

Checks the unmodified current Helly producer in its canonical scripts location.
Only the explicitly typed local chart is accepted; no X6 Cell is fabricated.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def require(condition, description):
    if not condition:
        raise AssertionError(description)


def verify_typed_helly_producer(module):
    demos = module.check_enterprise_demos()
    chart = demos["fixed_sector_chart"]
    require(chart["globally_feasible"] is True, "S12 intersection is not feasible")
    require(chart["common_a_values"] == [5, 6, 7], "S12 a-values changed")
    require(chart["common_b_values"] == [3, 4], "S12 b-values changed")
    require(chart["coordinate_type"] == "FIXED_POSITIVE_S12_LOCAL_CHART",
            "local chart misidentified as native Cell")
    require(chart["sample_fixed_positive_chart_address"] == [5, 3, 0],
            "positive chart sample changed")
    require(chart["native_cell_address_status"] == (
        "UNSPECIFIED_REQUIRES_CELL_ANCHOR_AND_ORDERED_SIGNED_AXIS_EMBEDDING"),
        "native X6 provenance cannot be inferred from unlabelled S12 coordinates")
    require("sample_native_address" not in chart,
            "unlabelled chart incorrectly exported as native X6 address")

    # Distinct native embeddings of the same unlabelled local chart.
    x = (5, 3, 0, 0, 0, 0)
    y = (5, 0, 3, 0, 0, 0)
    require(x != y and sum((a - b) ** 2 for a, b in zip(x, y)) == 18,
            "non-unique signed native lift witness changed")

    support = demos["typed_boolean_brc_support"]
    require(support["globally_feasible"] is True, "support intersection changed")
    require(support["coordinatewise_common_values"] == ([1], [1], [0]),
            "support coordinate intersection changed")
    require(support["sample_support_mask"] == [1, 1, 0],
            "boolean BRC support mask changed")
    require(support["two_constraint_conflict_verified"] is True,
            "support obstruction no longer verified")

    # These checks are *evaluated* even with Python -O/-OO.
    require(module.check_interval_boxes()["helly2_violations"] == 0,
            "Helly-2 box check failed")
    require(module.check_unbounded_chain()["all_minimal_obstructions_verified"] is True,
            "minimal unsatisfiable chain check failed")
    require(module.check_carath_lower_bound()["all_lower_bounds_verified"] is True,
            "Caratheodory lower bound check failed")
    return True


def main():
    source = Path(__file__).resolve().parents[1] / "scripts" / "tool_discovery_helly_radon_certificate_calculus.py"
    spec = spec_from_file_location("typed_helly_source", source)
    require(spec is not None and spec.loader is not None,
            "current Helly producer cannot be loaded")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    verify_typed_helly_producer(module)
    print("PASS_X6_LP003_HELLY_TYPED_CHART_CONSUMER_REGRESSION")


if __name__ == "__main__":
    main()
