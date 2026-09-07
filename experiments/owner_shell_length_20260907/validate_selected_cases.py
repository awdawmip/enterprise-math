"""Selected formula-boundary checks, not a shell scan or an all-N proof."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys

import shell_length as sl


def run():
    selected = []
    for b in (0, 1, 2, 17):
        for r in range(6):
            maximum = 2 * b + (r == 5)
            for t in sorted({0, min(1, maximum), maximum}):
                N = 6 * b * b + 2 * b * r + r + 2 * t
                assert sl.upper_length(N) == 6 * b + r
                endpoint, detail = sl.construct_endpoint(N)
                assert sl.verify_endpoint(N, endpoint)["valid"]
                assert detail["r"] == r and detail["t"] == t
                selected.append({"N": N, "b": b, "r": r, "t": t,
                                 "raw_endpoint": endpoint,
                                 "three_square_candidates": detail["candidates_checked"]})
    signed = sl.certificate(25, signs=(1, -1, 1, -1, 1, -1))
    assert signed["native_shortest_length"] == 11
    assert signed["construction"]["auxiliary_center_b"] != signed["native_common_depth"]
    assert len(signed["joint_twenty_slices"]) == 20
    assert signed["shortest_path_multiplicity"]["status"] == "COMPUTED_EXACT"
    assert sl.verify_endpoint(0, (0,) * 6)["valid"]
    assert sl.certificate(0)["shortest_path_multiplicity"]["count_decimal"] == "1"
    assert not sl.verify_endpoint(25, (0,) * 6)["valid"]
    assert not sl.verify_endpoint(True, (0,) * 6)["valid"]
    assert not sl.verify_endpoint(0, (False, 0, 0, 0, 0, 0))["valid"]
    consumed = []
    def unbounded_endpoint():
        while True:
            consumed.append(1)
            yield 0
    assert not sl.verify_endpoint(0, unbounded_endpoint())["valid"]
    assert consumed == []
    assert sl.construct_endpoint(0, signs=(-1,) * 6)[0] == (0,) * 6
    for invalid in (-1, True, 1.0, Fraction(1)):
        try:
            sl.construct_endpoint(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid N accepted")
    try:
        sl.construct_endpoint(25, search_budget=0)
    except sl.ResourceLimit:
        pass
    else:
        raise AssertionError("zero search budget was not enforced")
    assert sl.certificate(25, brc_event_budget=0)["shortest_path_multiplicity"]["status"] == "RESOURCE_LIMIT"
    large = sl.certificate(6_000_000, search_budget=0, brc_event_budget=6000)
    assert large["status"] == "ENDPOINT_VERIFIED"
    assert large["raw_signed_endpoint"] == (1000,) * 6
    if 0 < sys.get_int_max_str_digits() <= 4300:
        assert large["shortest_path_multiplicity"]["status"] == "RESOURCE_LIMIT"
        assert large["shortest_path_multiplicity"]["reason"] == "DECIMAL_CONVERSION_LIMIT"
    source = Path(sl.__file__)
    return {"schema": "owner_shell_length_selected_validation_v1", "status": "PASS",
            "scope": "Selected r/t boundary consumers only; all-N result is analytic, no prefix enumeration",
            "helper_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "validation_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "selected_case_count": len(selected), "selected_cases": selected,
            "signed_N25_endpoint": signed["raw_signed_endpoint"],
            "signed_N25_common_depth": signed["native_common_depth"],
            "signed_N25_auxiliary_b": signed["construction"]["auxiliary_center_b"],
            "signed_N25_shortest_path_count": signed["shortest_path_multiplicity"]["count_decimal"],
            "unbounded_endpoint_items_consumed": len(consumed),
            "zero_coordinate_signs_do_not_change_cell": True,
            "large_count_decimal_readout": large["shortest_path_multiplicity"],
            "interpreter_decimal_limit_unchanged": sys.get_int_max_str_digits(),
            "invalid_input_and_resource_boundaries": "PASS"}


if __name__ == "__main__":
    payload = run()
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": payload["status"], "selected_cases": payload["selected_case_count"],
                      "output_sha256": hashlib.sha256(output.read_bytes()).hexdigest()}))
