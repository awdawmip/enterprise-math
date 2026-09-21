#!/usr/bin/env python3
"""R14 frozen-trial paired attribution audit for RS-CFD-SPECTRAL-HYBRID-20260910.

This checker never runs spectralDNS. It consumes the immutable 2026-09-16 author-host
JSON and asks only what its five interleaved repeats can support descriptively.
"""
from __future__ import annotations

import hashlib
import json
import statistics
from pathlib import Path

SOURCE = Path("research_notes/CFD9R2K7/host_20260916/host_validation_numba.json")
EXPECTED_GIT_BLOB = "7282be0e2949b7b7d47910607d550aecd87fb27a"
METRICS = ("total_seconds", "setup_seconds", "native_RK4_seconds", "final_readout_seconds")
FOCUS = {(16, "taylor_green"), (16, "random32"), (32, "taylor_green"), (32, "random32"), (32, "random256")}


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def med(xs):
    return statistics.median(xs)


def summarize(row):
    fft = row["trials"]["fft"]
    hybrid = row["trials"]["hybrid"]
    assert len(fft) == len(hybrid) == 5
    sparse = [x["stats"]["sparse_calls"] for x in hybrid]
    fallback = [x["stats"]["fft_calls"] for x in hybrid]
    out = {
        "n": row["n"], "input": row["input"], "seed": row["seed"],
        "repeats": len(fft), "sparse_calls": sparse, "fft_calls": fallback,
        "metrics": {},
    }
    for metric in METRICS:
        paired = [(a[metric] - b[metric]) * 1000.0 for a, b in zip(fft, hybrid)]
        out["metrics"][metric] = {
            "paired_delta_ms": paired,
            "paired_median_delta_ms": med(paired),
            "paired_mean_delta_ms": statistics.fmean(paired),
            "paired_min_delta_ms": min(paired),
            "paired_max_delta_ms": max(paired),
            "positive_pairs": sum(x > 0 for x in paired),
            "negative_pairs": sum(x < 0 for x in paired),
            "arm_median_delta_ms": (med([x[metric] for x in fft]) - med([x[metric] for x in hybrid])) * 1000.0,
            # host_validation_numba.py alternated order by repeat parity:
            # even repeats FFT->hybrid; odd repeats hybrid->FFT.
            "fft_first_median_ms": med([paired[i] for i in (0, 2, 4)]),
            "hybrid_first_median_ms": med([paired[i] for i in (1, 3)]),
        }
    return out


def main():
    raw = SOURCE.read_bytes()
    assert git_blob_sha1(raw) == EXPECTED_GIT_BLOB
    report = json.loads(raw)
    assert report["schema"] == "CFD_PINNED_NATIVE_HOST_VALIDATION_V1"
    assert report["workflow_run_id"] == "35050063789"
    assert report["upstream_commit"] == "835b01b1e820b5c56559b9a028293e57526bfbf9"
    assert report["repeats"] == 5 and report["steps"] == 12
    assert report["failures"] == []

    focus = {}
    for row in report["trajectory_cases"]:
        key = (row["n"], row["input"])
        if key in FOCUS:
            focus[f"{row['n']}_{row['input']}"] = summarize(row)

    assert set(focus) == {"16_taylor_green", "16_random32", "32_taylor_green", "32_random32", "32_random256"}
    assert all(x == 0 for x in focus["32_random256"]["sparse_calls"])
    assert all(x == 49 for x in focus["32_random256"]["fft_calls"])
    assert all(x == 1 for x in focus["32_random32"]["sparse_calls"])
    assert all(x == 48 for x in focus["32_random32"]["fft_calls"])
    assert all(x == 3 for x in focus["32_taylor_green"]["sparse_calls"])
    assert all(x == 46 for x in focus["32_taylor_green"]["fft_calls"])

    # Same-grid repeat-index contrast. This is a descriptive negative-control contrast,
    # not a randomized causal estimator because the two initial-condition cases are distinct.
    target = focus["32_random32"]
    control = focus["32_random256"]
    adjusted = {}
    for metric in METRICS:
        a = target["metrics"][metric]["paired_delta_ms"]
        c = control["metrics"][metric]["paired_delta_ms"]
        x = [u - v for u, v in zip(a, c)]
        adjusted[metric] = {
            "repeat_index_delta_minus_all_fallback_control_ms": x,
            "median_ms": med(x),
            "mean_ms": statistics.fmean(x),
            "positive_pairs": sum(v > 0 for v in x),
        }

    out = {
        "schema": "CFD_FROZEN_PAIRED_ATTRIBUTION_AUDIT_V1",
        "source_git_blob_sha1": EXPECTED_GIT_BLOB,
        "source_workflow_run_id": "35050063789",
        "pairing_basis": "same repeat index; acquisition order alternates FFT->hybrid on even repeats and hybrid->FFT on odd repeats",
        "focus": focus,
        "random32_32_minus_random256_32_control": adjusted,
        "boundary": "descriptive frozen author evidence; n=5; distinct cases are not randomized counterfactuals; no native rerun, generic speedup, PDE theorem, or independent acceptance",
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
