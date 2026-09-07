"""Validate the existing shell consumer's BRC arithmetic migration.

The frozen v1 outputs and original input/resource regression remain provenance.
This checker adds exact trace reconstruction and confirms the governed call path
does not execute the historical direct-division multiplicity routines.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys

import shell_length as sl
import validate_selected_cases as original_validation


def _integer(value):
    if type(value) is int:
        return value
    if (type(value) is dict and set(value) == {"encoding", "value"}
            and value["encoding"] == "hex" and type(value["value"]) is str):
        return int(value["value"], 16)
    raise AssertionError("trace value is not an exact integer encoding")


def verify_trace(record):
    assert type(record) is dict and set(record) == {"purpose", "trace"}
    assert type(record["purpose"]) is str and record["purpose"]
    fields = record["trace"]
    kind = fields.get("evaluation_kind")
    if kind == "BRC_DIVISION_EVALUATION":
        names = {"numerator", "denominator", "quotient", "remainder", "collapsed_numerator"}
        assert set(fields) == names | {"evaluation_kind"}
        v = {name: _integer(fields[name]) for name in names}
        assert v["numerator"] >= 0 and v["denominator"] > 0
        assert v["quotient"] >= 0 and 0 <= v["remainder"] < v["denominator"]
        assert v["collapsed_numerator"] == v["denominator"] * v["quotient"]
        assert v["numerator"] == v["collapsed_numerator"] + v["remainder"]
    elif kind == "BRC_ROOT_EVALUATION":
        names = {"radicand", "degree", "root_index", "collapsed_radicand", "remainder", "next_power"}
        assert set(fields) == names | {"evaluation_kind"}
        v = {name: _integer(fields[name]) for name in names}
        assert v["degree"] == 2 and v["radicand"] >= 0 and v["root_index"] >= 0
        assert v["collapsed_radicand"] == v["root_index"] ** v["degree"]
        assert v["next_power"] == (v["root_index"] + 1) ** v["degree"]
        assert v["collapsed_radicand"] <= v["radicand"] < v["next_power"]
        assert v["radicand"] == v["collapsed_radicand"] + v["remainder"]
    else:
        raise AssertionError("unknown arithmetic evaluation kind")
    return kind


def _json_shape(value):
    return json.loads(json.dumps(value))


def _sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    original_limit = sys.get_int_max_str_digits()
    baseline_path = Path(__file__).with_name("validate_selected_cases.json")
    frozen = json.loads(baseline_path.read_text(encoding="utf-8"))
    selected = original_validation.run()
    for field in ("selected_case_count", "selected_cases", "signed_N25_endpoint",
                  "signed_N25_common_depth", "signed_N25_auxiliary_b",
                  "signed_N25_shortest_path_count", "unbounded_endpoint_items_consumed",
                  "zero_coordinate_signs_do_not_change_cell"):
        assert _json_shape(selected[field]) == frozen[field], field

    def no_legacy_division(*args, **kwargs):
        raise AssertionError("governed certificate called a historical direct-division routine")

    old_shortest = sl.signed_brc.shortest_path_multiplicity
    old_general = sl.signed_brc.endpoint_multiplicity
    sl.signed_brc.shortest_path_multiplicity = no_legacy_division
    sl.signed_brc.endpoint_multiplicity = no_legacy_division
    trace_count = 0
    kinds = set()
    try:
        for case in selected["selected_cases"]:
            ledger = []
            endpoint, construction = sl.construct_endpoint(case["N"], arithmetic_trace=ledger)
            assert endpoint == tuple(case["raw_endpoint"])
            assert "arithmetic_trace" not in construction
            for record in ledger:
                kinds.add(verify_trace(record))
            trace_count += len(ledger)
        signed = sl.certificate(25, signs=(1, -1, 1, -1, 1, -1))
        zero = sl.certificate(0)
        skipped = sl.certificate(25, brc_event_budget=0)
        large = sl.certificate(6_000_000, search_budget=0, brc_event_budget=6000)
        for payload in (signed, zero, skipped, large):
            assert payload["schema"] == "owner_shell_length_endpoint_v2"
            assert "arithmetic_trace" not in payload["construction"]
            assert "arithmetic_trace" not in payload["verification"]
            for record in payload["arithmetic_trace"]:
                kinds.add(verify_trace(record))
            trace_count += len(payload["arithmetic_trace"])
            json.dumps(payload)
        assert signed["shortest_path_multiplicity"]["count_decimal"] == frozen["signed_N25_shortest_path_count"]
        assert zero["shortest_path_multiplicity"]["count_decimal"] == "1"
        assert skipped["shortest_path_multiplicity"]["reason"] == "EVENT_BUDGET"
        assert not any(r["purpose"] == "signed BRC shortest-word multiplicity"
                       for r in skipped["arithmetic_trace"])
        if 0 < original_limit <= 4300:
            assert large["shortest_path_multiplicity"]["reason"] == "DECIMAL_CONVERSION_LIMIT"
        assert any(type(v) is dict and v.get("encoding") == "hex"
                   for r in large["arithmetic_trace"] for v in r["trace"].values())
        balanced = 1 << 256
        huge = sl.upper_length_evaluation(6 * balanced * balanced)
        assert huge["upper_length"] == 6 * balanced
        for record in huge["arithmetic_trace"]:
            kinds.add(verify_trace(record))
        trace_count += len(huge["arithmetic_trace"])
        assert kinds == {"BRC_DIVISION_EVALUATION", "BRC_ROOT_EVALUATION"}
        for kind in sorted(kinds):
            original = next(r for r in signed["arithmetic_trace"] if r["trace"]["evaluation_kind"] == kind)
            tampered = deepcopy(original)
            key = "remainder"
            tampered["trace"][key] = _integer(tampered["trace"][key]) + 1
            try:
                verify_trace(tampered)
            except AssertionError:
                pass
            else:
                raise AssertionError("tampered collapse trace accepted")
    finally:
        sl.signed_brc.shortest_path_multiplicity = old_shortest
        sl.signed_brc.endpoint_multiplicity = old_general
    assert sys.get_int_max_str_digits() == original_limit
    return {
        "schema": "owner_shell_length_brc_migration_validation_v1",
        "status": "PASS",
        "scope": "Same 61 selected formula/input/resource cases plus exact BRC traces; no all-N proof claim from tests.",
        "helper_sha256": _sha(Path(sl.__file__)),
        "validation_sha256": _sha(Path(__file__)),
        "frozen_v1_validation_sha256": _sha(baseline_path),
        "original_validation_source_sha256": _sha(Path(original_validation.__file__)),
        "selected_case_count": selected["selected_case_count"],
        "frozen_selected_outputs_equal": True,
        "trace_count_verified": trace_count,
        "trace_kinds": sorted(kinds),
        "tampered_trace_rejected": True,
        "governed_legacy_multiplicity_calls": 0,
        "exact_large_trace_json_serialization": "PASS",
        "interpreter_decimal_limit_unchanged": original_limit,
        "large_count_readout_status": large["shortest_path_multiplicity"]["status"],
        "source_dependencies": {
            str(path.relative_to(sl.ROOT)).replace("\\", "/"): _sha(path)
            for path in (sl.NATIVE.joinpath("signed_brc.py"), sl.NATIVE.joinpath("x6_signed.py"),
                         sl.ROOT.joinpath("src/enterprise_math/exact_arithmetic.py"))
        },
        "legacy_boundary": "Unmodified original regression imports Fraction only to reject noninteger input. Original signed BRC multiplicity routines are not used by the governed v2 certificate; pure-integer coordinate/norm/length contracts remain reused.",
    }


if __name__ == "__main__":
    payload = run()
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": payload["status"], "selected_cases": payload["selected_case_count"],
                      "verified_traces": payload["trace_count_verified"], "output_sha256": _sha(output)}))
