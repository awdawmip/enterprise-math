#!/usr/bin/env python3
"""X6 Unit154: independent exact finite-box min-zero/partial-step certificate.
This is a standalone reconstruction of the declared mathematical interface;
it does not execute the frozen historical implementation or the R063 benchmark.
"""
from itertools import product
import json


def signature_refinement(radius):
    states = tuple(product(range(-radius, radius + 1), repeat=3))
    def obs(x):
        low = min(x)
        return tuple(a - low for a in x)
    def partition_from_signatures(sigs):
        canonical = {}
        return {s: canonical.setdefault(sigs[s], len(canonical)) for s in states}
    labels = partition_from_signatures({s: obs(s) for s in states})
    profile = [len(set(labels.values()))]
    for depth in range(1, radius + 2):
        sigs = {}
        for x in states:
            steps = []
            for i in range(3):
                for delta in (-1, 1):
                    y = list(x)
                    y[i] += delta
                    y = tuple(y)
                    steps.append((True, labels[y]) if y in labels else (False, None))
            sigs[x] = (labels[x], tuple(steps))
        labels = partition_from_signatures(sigs)
        profile.append(len(set(labels.values())))
    expected = [len(states) - (2 * (radius - depth)) ** 3
                for depth in range(radius + 1)]
    if profile[:radius + 1] != expected:
        raise ValueError((radius, "closed-form partition count mismatch", profile, expected))
    if profile[radius + 1] != len(states):
        raise ValueError((radius, "terminal partition unstable"))
    a, b = (-1, -1, -1), (0, 0, 0)
    if radius >= 1 and any(a[i] != b[i] - 1 for i in range(3)):
        raise ValueError("lower-bound witness invalid")
    return {"radius": radius, "states": len(states),
            "refinement_class_counts_h0_to_hR_plus_1": profile,
            "first_discrete_depth": radius,
            "lower_bound_pair": [list(a), list(b)]}


def main():
    results = [signature_refinement(r) for r in range(1, 6)]
    print(json.dumps({"schema": "X6_UNIT154_FINITE_PARTIAL_QUOTIENT_CERT_V1",
                      "frozen_model": "SIGNED_Z3_SLICE_FINITELY_TRUNCATED_CUBE",
                      "mode": "EXACT_INTEGER_STANDALONE_NOT_HISTORICAL_TEST_EXECUTION",
                      "results": results,
                      "verified": True,
                      "review": "AUTHOR_FINITE_EXECUTED_UNREVIEWED_NOT_ADMITTED"},
                     sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
