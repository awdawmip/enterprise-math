#!/usr/bin/env python3
"""Independent exact coefficient-DP comparison with pinned P000 signed-X6 BRC.

Does not modify or replace the frozen producer, and does not run the R063 benchmark.
Requires the pinned git commit in a local checkout, or PINNED_SOURCE_FILE pointing
at the exact original bytes (verified by Git blob SHA-1 before import).
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha1, sha256
from itertools import product
from math import comb, factorial
from pathlib import Path
import importlib.util
import json
import os
import random
import subprocess
import sys
import tempfile

PIN = "fd2bcff10ca6e147348b6c1236027fc0d2877df3"
SOURCE = "experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py"
SOURCE_BLOB = "300a96e3dc24bf6fff73743037a0347a8bc83176"


def load_pinned():
    override = os.environ.get("PINNED_SOURCE_FILE")
    if override:
        source = Path(override).read_bytes()
    else:
        source = subprocess.check_output(["git", "show", f"{PIN}:{SOURCE}"])
    h = sha1(b"blob " + str(len(source)).encode() + b"\0" + source).hexdigest()
    if h != SOURCE_BLOB:
        raise RuntimeError(f"frozen source blob mismatch: {h}")
    with tempfile.TemporaryDirectory() as d:
        name = "pinned_signed_brc_unit198"
        p = Path(d) / (name + ".py")
        p.write_bytes(source)
        spec = importlib.util.spec_from_file_location(name, p)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return module, sha256(source).hexdigest()


def coefficient_endpoint_weight(length, z, positive_weights, negative_weights):
    """Exact six-factor coefficient convolution; not a floating approximation."""
    if len(z) != 6 or any(type(x) is not int for x in z):
        raise ValueError("six integer coordinates required")
    u = tuple(map(Fraction, positive_weights))
    v = tuple(map(Fraction, negative_weights))
    if len(u) != 6 or len(v) != 6 or any(w <= 0 for w in u + v):
        raise ValueError("six positive weights per sign required")
    if type(length) is not int or length < 0:
        raise ValueError("nonnegative integer length required")
    a = tuple(max(x, 0) for x in z)
    b = tuple(max(-x, 0) for x in z)
    gap = length - sum(a) - sum(b)
    if gap < 0 or gap % 2:
        return Fraction(0)
    K = gap // 2
    dp = [Fraction(1)] + [Fraction(0)] * K
    prefix = Fraction(factorial(length))
    for ai, bi, ui, vi in zip(a, b, u, v):
        prefix *= ui ** ai * vi ** bi / (factorial(ai) * factorial(bi))
        series = [Fraction(1)]
        q = ui * vi
        for k in range(1, K + 1):
            series.append(series[-1] * q / ((ai + k) * (bi + k)))
        new = [Fraction(0)] * (K + 1)
        for t in range(K + 1):
            if dp[t] == 0:
                continue
            for k in range(K - t + 1):
                new[t + k] += dp[t] * series[k]
        dp = new
    return prefix * dp[K]


def one_step_weighted_dp(length, u, v):
    """Independent time-step recurrence at full signed endpoints."""
    dist = {(0,) * 6: Fraction(1)}
    for step in range(length):
        nxt = {}
        for z, w in dist.items():
            for axis in range(6):
                for sign, factor in ((1, u[axis]), (-1, v[axis])):
                    t = list(z)
                    t[axis] += sign
                    t = tuple(t)
                    nxt[t] = nxt.get(t, Fraction(0)) + w * factor
        dist = nxt
    return dist


def main():
    original, original_sha = load_pinned()
    rng = random.Random(19820261121)
    profiles = [
        ((1,) * 6, (1,) * 6),
        ((1, 2, 3, 4, 5, 6), (6, 5, 4, 3, 2, 1)),
        ((Fraction(1, 2), Fraction(2, 3), Fraction(3, 5), 1, 2, 3),
         (Fraction(3, 2), Fraction(5, 4), 1, Fraction(7, 3), 1, 2)),
    ]
    checked = 0
    max_k = 0
    sampled = []
    for profile_id, (u, v) in enumerate(profiles):
        for index in range(72):
            z = tuple(rng.randrange(-2, 3) for _ in range(6))
            base = sum(map(abs, z))
            K = rng.randrange(0, 7)
            length = base + 2 * K
            # Preserve the producer's zero/odd-gap behavior in additional checks.
            for actual_length in (length, length - 1 if length else 1):
                got = coefficient_endpoint_weight(actual_length, z, u, v)
                ref = original.endpoint_weight(actual_length, z, u, v)
                if got != ref:
                    raise AssertionError((profile_id, index, z, actual_length, got, ref))
                checked += 1
            max_k = max(max_k, K)
        for K in (8, 10, 13):
            z = ((profile_id + 1), -1, 0, 1, -1, 0)
            length = sum(map(abs, z)) + 2 * K
            got = coefficient_endpoint_weight(length, z, u, v)
            ref = original.endpoint_weight(length, z, u, v)
            if got != ref:
                raise AssertionError((profile_id, K))
            checked += 1
            max_k = max(max_k, K)
            if K == 13:
                sampled.append({"profile": profile_id, "K": K, "digits_numerator": len(str(got.numerator)), "digits_denominator": len(str(got.denominator))})
    # Independent full-path weighted recurrence, covering all reachable endpoints.
    u, v = profiles[2]
    all_paths = one_step_weighted_dp(5, u, v)
    for z, weight in all_paths.items():
        if weight != coefficient_endpoint_weight(5, z, u, v):
            raise AssertionError(("independent_native_dp", z))
        checked += 1
    all_path_total = sum(all_paths.values(), Fraction(0))
    assert all_path_total == (sum(map(Fraction, u)) + sum(map(Fraction, v))) ** 5
    # Endpoint return E_0(0), E_2(0), E_4(0) against direct pinned module.
    zero = (0,) * 6
    returns = {}
    for length in (0, 2, 4):
        got = coefficient_endpoint_weight(length, zero, (1,) * 6, (1,) * 6)
        assert got == original.endpoint_multiplicity(length, zero)
        returns[str(length)] = int(got)
        checked += 1
    sample_k = 25
    structural = {
        "K": sample_k,
        "pinned_weak_composition_terms": comb(sample_k + 5, 5),
        "coefficient_convolution_upper_bound_muladds": 3 * (sample_k + 1) * (sample_k + 2),
        "coefficient_series_recurrence_steps": 6 * sample_k,
    }
    # High-K exact DP only; NOT compared to frozen original or called an original benchmark.
    high = coefficient_endpoint_weight(52, zero, (1,) * 6, (1,) * 6)
    result = {
        "schema": "X6_UNIT198_EXACT_SOURCE_TYPED_COEFFICIENT_DP_RESULT_V1",
        "frozen_commit": PIN, "frozen_source": SOURCE,
        "frozen_git_blob_sha1": SOURCE_BLOB,
        "frozen_source_sha256": original_sha,
        "method": "exact Fraction coefficient dynamic convolution",
        "local_comparisons": checked,
        "independent_native_5step_endpoints": len(all_paths),
        "largest_K_directly_compared_to_original": max_k,
        "violations": 0,
        "unweighted_returns": returns,
        "sample_exact_size": sampled,
        "K25_structural_operation_counts": structural,
        "K26_dp_only_length52_unweighted_return_digit_count": len(str(high.numerator)),
        "K26_dp_only_checked_against_original": False,
        "R063_original_six_file_benchmark_rerun": False,
        "native_source_updated": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
