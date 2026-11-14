#!/usr/bin/env python3
"""Guard the live Helly demo against promoting an S12 chart witness to native X6 Cell identity.

Uses the actual current source module. This is a consumer-interface regression, not
an additional Helly theorem or a replacement for native signed-X6 benchmarks.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def main():
    source = Path(__file__).resolve().parents[1] / "scripts" / "tool_discovery_helly_radon_certificate_calculus.py"
    spec = spec_from_file_location("typed_helly_source", source)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    demos = module.check_enterprise_demos()
    chart = demos["fixed_sector_chart"]
    assert chart["globally_feasible"] is True
    assert chart["common_a_values"] == [5, 6, 7]
    assert chart["common_b_values"] == [3, 4]
    assert chart["coordinate_type"] == "FIXED_POSITIVE_S12_LOCAL_CHART"
    assert chart["sample_fixed_positive_chart_address"] == [5, 3, 0]
    assert chart["native_cell_address_status"] == (
        "UNSPECIFIED_REQUIRES_CELL_ANCHOR_AND_ORDERED_SIGNED_AXIS_EMBEDDING"
    )
    assert "sample_native_address" not in chart

    # Signed X6 native coordinates require an anchor and a declared ordered axis embedding.
    # One unlabelled chart triple admits more than one native lift, so neither is inferred.
    x = (5, 3, 0, 0, 0, 0)
    y = (5, 0, 3, 0, 0, 0)
    assert x != y and sum((a - b) ** 2 for a, b in zip(x, y)) == 18

    support = demos["typed_boolean_brc_support"]
    assert support["globally_feasible"] is True
    assert support["coordinatewise_common_values"] == ([1], [1], [0])
    assert support["sample_support_mask"] == [1, 1, 0]
    assert support["two_constraint_conflict_verified"] is True

    # Preserve the producer's existing finite mathematical predicates.
    assert module.check_interval_boxes()["helly2_violations"] == 0
    assert module.check_unbounded_chain()["all_minimal_obstructions_verified"] is True
    assert module.check_carath_lower_bound()["all_lower_bounds_verified"] is True
    print("PASS_X6_LP003_HELLY_TYPED_CHART_CONSUMER_REGRESSION")


if __name__ == "__main__":
    main()
