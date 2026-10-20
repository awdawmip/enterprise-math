#!/usr/bin/env python3
"""R022 pass-12 adaptive raw-feature acquisition for the md5collgen-shaped router."""
from functools import lru_cache
from itertools import product
from collections import Counter
import json

FEATURES = (
    "iv1_b31", "iv2_b31", "iv3_b31",
    "iv1_b25", "iv2_b25", "iv3_b25",
    "iv1_b0", "iv2_b0", "iv1_b6",
)


def md5_route(bits):
    d = dict(zip(FEATURES, bits))
    eligible = (
        d["iv1_b31"] == d["iv2_b31"] == d["iv3_b31"]
        and d["iv1_b25"] == d["iv2_b25"] == d["iv3_b25"] == 0
        and d["iv1_b0"] == d["iv2_b0"]
    )
    return f"S{d['iv1_b6']}{d['iv1_b0']}" if eligible else "WANG"


ASSIGNMENTS = list(product((0, 1), repeat=9))
LABELS = [md5_route(x) for x in ASSIGNMENTS]


@lru_cache(None)
def matching_indices(pattern):
    return tuple(
        i for i, x in enumerate(ASSIGNMENTS)
        if all(p == -1 or x[j] == p for j, p in enumerate(pattern))
    )


@lru_cache(None)
def expected_optimum(pattern):
    inds = matching_indices(pattern)
    labels = {LABELS[i] for i in inds}
    if len(labels) <= 1:
        return 0.0, None
    best = (10**9, None)
    n = len(inds)
    for j, p in enumerate(pattern):
        if p != -1:
            continue
        expected = 1.0
        for bit in (0, 1):
            child = list(pattern)
            child[j] = bit
            child = tuple(child)
            expected += len(matching_indices(child)) / n * expected_optimum(child)[0]
        if expected < best[0] - 1e-12:
            best = (expected, j)
    return best


@lru_cache(None)
def worst_optimum(pattern):
    inds = matching_indices(pattern)
    labels = {LABELS[i] for i in inds}
    if len(labels) <= 1:
        return 0, None
    best = (10**9, None)
    for j, p in enumerate(pattern):
        if p != -1:
            continue
        child_costs = []
        for bit in (0, 1):
            child = list(pattern)
            child[j] = bit
            child_costs.append(worst_optimum(tuple(child))[0])
        cost = 1 + max(child_costs)
        if cost < best[0]:
            best = (cost, j)
    return best


def optimal_depth_for_assignment(x):
    pattern = (-1,) * 9
    depth = 0
    while True:
        inds = matching_indices(pattern)
        labels = {LABELS[i] for i in inds}
        if len(labels) <= 1:
            return depth
        j = expected_optimum(pattern)[1]
        pattern = list(pattern)
        pattern[j] = x[j]
        pattern = tuple(pattern)
        depth += 1


def source_order_cached_raw_reads(x):
    """Model C++ && short-circuit order while charging each raw bit once when first needed."""
    read = set()

    def get(i):
        read.add(i)
        return x[i]

    if get(0) != get(1):
        return len(read)
    if get(0) != get(2):
        return len(read)
    if get(5) != 0:
        return len(read)
    if get(4) != 0:
        return len(read)
    if get(3) != 0:
        return len(read)
    if get(7) != get(6):
        return len(read)
    get(8)
    return len(read)


def md5_adaptive_model():
    root = (-1,) * 9
    expected = expected_optimum(root)[0]
    worst = worst_optimum(root)[0]
    depths = [optimal_depth_for_assignment(x) for x in ASSIGNMENTS]
    source_depths = [source_order_cached_raw_reads(x) for x in ASSIGNMENTS]
    route_counts = Counter(LABELS)
    return {
        "assignments": 512,
        "route_counts": dict(sorted(route_counts.items())),
        "static_raw_signature_bits": 9,
        "static_materialized_reads_per_state": 9,
        "source_short_circuit_average_cached_raw_reads": sum(source_depths) / len(source_depths),
        "source_short_circuit_worst_cached_raw_reads": max(source_depths),
        "source_short_circuit_depth_distribution": dict(sorted(Counter(source_depths).items())),
        "optimal_adaptive_expected_raw_reads_uniform": expected,
        "optimal_adaptive_worst_raw_reads": worst,
        "optimal_adaptive_depth_distribution": dict(sorted(Counter(depths).items())),
        "optimal_first_feature": FEATURES[expected_optimum(root)[1]],
        "static_to_adaptive_expected_read_ratio": 9 / expected,
        "source_to_optimal_expected_read_ratio": (sum(source_depths) / len(source_depths)) / expected,
        "warning": "bounded source-shaped raw-bit query model; not a claim about measured C++ word-load/runtime cost or real IV distribution",
    }


def purity_verifier():
    """Every leaf reached by the expected-optimal tree must contain one route label."""
    leaves = []

    def visit(pattern):
        inds = matching_indices(pattern)
        labels = {LABELS[i] for i in inds}
        if len(labels) <= 1:
            leaves.append((pattern, tuple(sorted(labels)), len(inds)))
            return
        j = expected_optimum(pattern)[1]
        for bit in (0, 1):
            child = list(pattern)
            child[j] = bit
            visit(tuple(child))

    visit((-1,) * 9)
    return {
        "leaf_count": len(leaves),
        "all_leaves_route_pure": all(len(labels) == 1 for _, labels, _ in leaves),
        "covered_assignments": sum(size for _, _, size in leaves),
    }


def run_all():
    return {
        "md5_adaptive_signature": md5_adaptive_model(),
        "proof_carrying_leaf_verifier": purity_verifier(),
    }


def self_test():
    out = run_all()
    m = out["md5_adaptive_signature"]
    assert m["static_raw_signature_bits"] == 9
    assert m["source_short_circuit_average_cached_raw_reads"] == 3.015625
    assert m["optimal_adaptive_expected_raw_reads_uniform"] == 2.140625
    assert m["optimal_adaptive_worst_raw_reads"] == 9
    assert m["optimal_adaptive_depth_distribution"] == {1: 256, 2: 128, 3: 64, 5: 32, 6: 16, 8: 8, 9: 8}
    v = out["proof_carrying_leaf_verifier"]
    assert v["all_leaves_route_pure"] and v["covered_assignments"] == 512


if __name__ == "__main__":
    self_test()
    print(json.dumps(run_all(), indent=2, sort_keys=True))
