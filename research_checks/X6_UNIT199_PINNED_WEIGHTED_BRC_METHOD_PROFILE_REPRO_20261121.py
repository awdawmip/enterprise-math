#!/usr/bin/env python3
"""Reproduce Unit199's focused method comparison; not the R063 benchmark.

Run from the enterprise-math checkout. The reused Unit198 reader verifies
the historical signed_brc.py Git-blob SHA before importing the actual function.
Timing medians vary by host; exact values and case coverage are deterministic.
"""
from __future__ import annotations

import gc
import hashlib
import importlib.util
import json
from fractions import Fraction
from math import comb
from pathlib import Path
import statistics
import time
import sys

ROOT = Path(__file__).resolve().parents[1]
UNIT198 = ROOT / "research_checks" / "X6_UNIT198_PINNED_WEIGHTED_BRC_COEFFICIENT_DP_CHECK_20261121.py"

def load_unit198():
    spec = importlib.util.spec_from_file_location("x6_unit198_reused", UNIT198)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod

def run():
    prior = load_unit198()
    original, sha = prior.load_pinned()
    profiles = {
        "equal_integer": ((1,) * 6, (1,) * 6),
        "nonuniform_rational": (
            (Fraction(1, 2), Fraction(2, 3), Fraction(3, 5), 1, 2, 3),
            (Fraction(3, 2), Fraction(5, 4), 1, Fraction(7, 3), 1, 2),
        ),
    }
    endpoints = {"zero": (0,) * 6, "mixed": (2, -1, 0, 1, -1, 0)}
    cases = []
    for name, (u, v) in profiles.items():
        for label, z in endpoints.items():
            for K in (4, 8, 12, 16):
                length = sum(abs(t) for t in z) + 2 * K
                args = (length, z, u, v)
                exact = original.endpoint_weight(*args)
                if prior.coefficient_endpoint_weight(*args) != exact:
                    raise AssertionError(("exact-disagreement", name, label, K))
                measures = {}
                for key, function in (
                    ("original", original.endpoint_weight),
                    ("coefficient_dp", prior.coefficient_endpoint_weight),
                ):
                    gc.collect()
                    times = []
                    for _ in range(3):
                        start = time.perf_counter_ns()
                        value = function(*args)
                        times.append(time.perf_counter_ns() - start)
                        if value != exact:
                            raise AssertionError(("timed-disagreement", name, label, K))
                    measures[key] = sorted(times)
                a = int(statistics.median(measures["original"]))
                b = int(statistics.median(measures["coefficient_dp"]))
                cases.append({
                    "profile": name, "endpoint": label, "z": z, "K": K,
                    "length": length, "terms_original": comb(K + 5, 5),
                    "source_median_ns": a, "coefficient_median_ns": b,
                    "ratio": round(a / b, 3),
                    "source_samples_ns": measures["original"],
                    "coefficient_samples_ns": measures["coefficient_dp"],
                    "exact_value_sha256": hashlib.sha256(
                        (str(exact.numerator) + "/" + str(exact.denominator)).encode()
                    ).hexdigest(),
                })
    print(json.dumps({
        "schema": "X6_UNIT199_REPRODUCIBLE_METHOD_PROFILE_V1",
        "pinned_source_sha256": sha,
        "original_calls": 48,
        "dp_calls": 48,
        "exact_cases": len(cases),
        "R063_six_file_benchmark_rerun": False,
        "rows": cases,
    }, indent=2, sort_keys=True))

if __name__ == "__main__":
    run()
