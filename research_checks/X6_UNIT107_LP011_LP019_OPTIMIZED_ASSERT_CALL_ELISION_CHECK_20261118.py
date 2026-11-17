#!/usr/bin/env python3
"""Author-side optimization call-elision witness for two pinned X6 callsites.

This runs the exact Python assert/counter CONTROL-FLOW pattern extracted from
current research_checks files, not those files or the frozen R063 benchmark.
Original source blobs:
 LP011_TYPED_DOMINANT_CONSUMER: cf2c11d47a4abf5a462c4c96540a125f0f942a8d
 LP019_SIGNED_THICKNESS_AND_BRC_FIBERS: 24664a814c83b471febaabb4a1c0b0ae0c59d571
"""
import hashlib
import json


def require(condition, description):
    if not condition:
        raise AssertionError(description)


def sample(source, expected):
    observations = []
    for optimization in (0, 1, 2):
        namespace = {"N": expected}
        exec(compile(source, "x6_unit107_controlflow", "exec", optimize=optimization), namespace)
        reported = namespace["reported"]
        actual = namespace["called"]
        require(reported == expected, f"reported length changed at -O{optimization}")
        require(actual == (expected if optimization == 0 else 0),
                f"actual call count inconsistent at -O{optimization}")
        observations.append({"optimization": optimization, "reported": reported, "actual_calls": actual})
    return observations


def main():
    # Both original programs invoke the imported Source API only in `assert`:
    # LP011 source lines 102-108, LP019 source lines 110-117.
    # `reported` models imported_module_calls and six_comparisons, respectively.
    source = '''\nreported=0\ncalled=0\ndef native(i):\n    global called\n    called += 1\n    return i\nfor i in range(N):\n    assert native(i)==i\n    reported += 1\n'''
    rows = {
        "LP011_3_axis_cube_-7_to_7": sample(source, 15 ** 3),
        "LP019_6_axis_endpoint_DP_lengths_0_to_6": sample(source, sum((1, 12, 73, 304, 985, 2668, 6321))),
    }
    result = {
        "schema": "X6_UNIT107_PYTHON_OPTIMIZED_ASSERT_NATIVE_CALL_ELISION_V1",
        "scope": "synthetic exact Python control-flow reproduction; original modules not executed",
        "original_source_blobs": {
            "LP011": "cf2c11d47a4abf5a462c4c96540a125f0f942a8d",
            "LP019": "24664a814c83b471febaabb4a1c0b0ae0c59d571"
        },
        "witnesses": rows,
        "original_R063_Helly_benchmarks_executed": False,
        "project_review_admission": False,
    }
    canonical = json.dumps(result, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    result["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(result, sort_keys=True, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
