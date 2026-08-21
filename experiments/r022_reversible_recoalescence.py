#!/usr/bin/env python3
"""R022 sixth-pass reversible recoalescence and deletion-horizon model."""
from __future__ import annotations

from collections import defaultdict
import json


def support_bit(n: int) -> int:
    return int(n > 0)


def add_one(n: int) -> int:
    return n + 1


def delete_one(n: int) -> int:
    return max(n - 1, 0)


def descends_through_support(op, max_n=12):
    groups = defaultdict(list)
    for n in range(max_n + 1):
        groups[support_bit(n)].append(n)
    for qv, states in groups.items():
        seen = {}
        for n in states:
            out = support_bit(op(n))
            seen.setdefault(out, []).append(n)
        if len(seen) > 1:
            keys = sorted(seen)
            return False, (seen[keys[0]][0], seen[keys[1]][0], qv, tuple(keys))
    return True, None


def future_signature(n: int, horizon: int):
    return tuple(support_bit(max(n - k, 0)) for k in range(horizon + 1))


def deletion_token(n: int, horizon: int) -> int:
    return min(n, horizon + 1)


def verify_deletion_token_coarsest(horizon: int, max_n=None):
    if max_n is None:
        max_n = horizon + 12
    states = range(max_n + 1)
    for a in states:
        for b in states:
            same_token = deletion_token(a, horizon) == deletion_token(b, horizon)
            same_future = future_signature(a, horizon) == future_signature(b, horizon)
            if same_token != same_future:
                return False, (a, b)
    classes = len({future_signature(n, horizon) for n in states})
    return True, classes


def induced_delete_token(token: int) -> int:
    return max(token - 1, 0)


def verify_stage_aware_transition(max_horizon=8, max_n=64):
    for horizon in range(1, max_horizon + 1):
        for residual in range(horizon, 0, -1):
            for n in range(max_n + 1):
                token = deletion_token(n, residual)
                expected = deletion_token(delete_one(n), residual - 1)
                actual = induced_delete_token(token)
                if expected != actual:
                    return False, (horizon, residual, n, token, expected, actual)
    return True, None


def horizon_extension_refinement(old_h: int, new_h: int, max_n=64):
    if new_h < old_h:
        raise ValueError("new horizon must extend old horizon")
    refinement = defaultdict(set)
    for n in range(max_n + 1):
        refinement[deletion_token(n, old_h)].add(deletion_token(n, new_h))
    return {k: tuple(sorted(v)) for k, v in sorted(refinement.items())}


def verify_saturated_class_refinement(old_h=2, new_h=5, max_n=64):
    ref = horizon_extension_refinement(old_h, new_h, max_n)
    nonsaturated_singletons = all(ref[t] == (t,) for t in range(old_h + 1))
    top = ref[old_h + 1]
    expected_top = tuple(range(old_h + 1, new_h + 2))
    return {
        "nonsaturated_classes_unchanged": nonsaturated_singletons,
        "old_saturated_class_refines_to": top,
        "expected_refinement": expected_top,
        "matches_expected": top == expected_top,
    }


def no_resurrection_extension_witness(old_h=2, new_h=3):
    a = old_h + 1
    b = old_h + 2
    return {
        "old_horizon": old_h,
        "new_horizon": new_h,
        "a": a,
        "b": b,
        "old_token_equal": deletion_token(a, old_h) == deletion_token(b, old_h),
        "new_token_equal": deletion_token(a, new_h) == deletion_token(b, new_h),
        "old_signatures_equal": future_signature(a, old_h) == future_signature(b, old_h),
        "new_signatures_equal": future_signature(a, new_h) == future_signature(b, new_h),
        "lesson": "without retained count/checkpoint, extending the future language cannot reconstruct the split",
    }


def run_all():
    add_ok, add_witness = descends_through_support(add_one)
    del_ok, del_witness = descends_through_support(delete_one)
    horizon_rows = []
    for h in range(0, 9):
        ok, classes = verify_deletion_token_coarsest(h)
        horizon_rows.append({
            "horizon": h,
            "coarsest_verified": ok,
            "future_classes": classes,
            "expected_classes": h + 2,
        })
    return {
        "support_quotient_operations": {
            "add_one_descends": add_ok,
            "add_one_counterexample": add_witness,
            "delete_one_descends": del_ok,
            "delete_one_counterexample": del_witness,
        },
        "deletion_horizon_token": {
            "formula": "tau_h(n)=min(n,h+1)",
            "rows": horizon_rows,
        },
        "stage_aware_transition": {
            "verified": verify_stage_aware_transition()[0],
            "rule": "tau_r(n) --delete--> max(tau_r(n)-1,0) at residual horizon r-1",
        },
        "horizon_extension": verify_saturated_class_refinement(),
        "no_resurrection_extension": no_resurrection_extension_witness(),
        "scope": {
            "observable": "Boolean support",
            "future_operation": "anonymous delete-one",
            "named_retraction_warning": "named/provenance-sensitive deletion generally requires stronger metadata",
        },
    }


def self_test():
    out = run_all()
    ops = out["support_quotient_operations"]
    assert ops["add_one_descends"] is True
    assert ops["delete_one_descends"] is False
    assert ops["delete_one_counterexample"][0:2] == (1, 2)

    for row in out["deletion_horizon_token"]["rows"]:
        assert row["coarsest_verified"] is True
        assert row["future_classes"] == row["expected_classes"]

    assert out["stage_aware_transition"]["verified"] is True

    ext = out["horizon_extension"]
    assert ext["nonsaturated_classes_unchanged"] is True
    assert ext["matches_expected"] is True

    nr = out["no_resurrection_extension"]
    assert nr["old_token_equal"] is True
    assert nr["new_token_equal"] is False
    assert nr["old_signatures_equal"] is True
    assert nr["new_signatures_equal"] is False


if __name__ == "__main__":
    self_test()
    print(json.dumps(run_all(), indent=2, sort_keys=True))
