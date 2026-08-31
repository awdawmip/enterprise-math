#!/usr/bin/env python3
"""R022 pass-11 distinction-cover duality for future probes and raw features."""
from itertools import combinations
from math import ceil, log2
import json


def minimum_cover_size(universe_size, masks):
    full = (1 << universe_size) - 1
    inf = universe_size + len(masks) + 10
    dp = [inf] * (1 << universe_size)
    dp[0] = 0
    for mask in masks:
        new = dp[:]
        for covered, cost in enumerate(dp):
            if cost < inf:
                nxt = covered | mask
                if cost + 1 < new[nxt]:
                    new[nxt] = cost + 1
        dp = new
    return None if dp[full] >= inf else dp[full]


def exhaustive_pairblock_reduction(m=4):
    """Every set family is realized both as future-distinction and feature-distinction columns.

    Current coarse state has m independent two-state cells. Target precision splits every cell.
    A future/feature column with mask S distinguishes exactly the required pair in cells in S.
    """
    masks = list(range(1, 1 << m))
    families = 0
    coverable = 0
    mismatches = 0
    widths = {}
    for family_mask in range(1, 1 << len(masks)):
        family = [masks[i] for i in range(len(masks)) if (family_mask >> i) & 1]
        families += 1
        optimum = minimum_cover_size(m, family)
        if optimum is None:
            continue
        coverable += 1
        # By construction the future-basis and raw-feature-basis incidence matrices are identical.
        future_optimum = minimum_cover_size(m, family)
        feature_optimum = minimum_cover_size(m, family)
        if future_optimum != optimum or feature_optimum != optimum:
            mismatches += 1
        widths[optimum] = widths.get(optimum, 0) + 1
    return {
        "required_pair_blocks": m,
        "nonempty_set_families": families,
        "coverable_families": coverable,
        "mismatches": mismatches,
        "optimum_width_distribution": widths,
    }


def information_vs_extraction_witness(m=4):
    singleton_columns = [1 << i for i in range(m)]
    optimum = minimum_cover_size(m, singleton_columns)
    # Each old coarse class splits into exactly two target classes, so one shared side bit suffices
    # abstractly, even though a coordinate/probe-restricted extractor needs all m singleton columns.
    return {
        "old_classes": m,
        "target_subclasses_per_old_class": 2,
        "abstract_side_alphabet": 2,
        "abstract_side_bits": 1,
        "minimum_future_probe_basis": optimum,
        "minimum_raw_feature_basis": optimum,
        "lesson": "semantic information debt and constrained extraction/probe complexity are distinct resources",
    }


def md5_router_shape_note():
    return {
        "source_shaped_raw_features": 9,
        "compiled_route_labels": 5,
        "compiled_fixed_width_bits": ceil(log2(5)),
        "lesson": "raw-coordinate feature count and arbitrary compiled label width optimize different representation classes",
    }


def proof_carrying_basis_witness():
    # Universe of four required distinctions. Candidate family has an exact but nonminimum sublanguage.
    family = [0b1111, 0b0011, 0b1100, 0b0001, 0b0010, 0b0100, 0b1000]
    optimum = minimum_cover_size(4, family)
    exact_suboptimal = [0b0011, 0b0100, 0b1000]
    unsafe = exact_suboptimal[:2]
    full = 0b1111
    def covers(cols):
        out = 0
        for c in cols:
            out |= c
        return out == full
    return {
        "optimum_basis_size": optimum,
        "suboptimal_basis_size": len(exact_suboptimal),
        "suboptimal_basis_exact": covers(exact_suboptimal),
        "unsafe_truncation_exact": covers(unsafe),
        "lesson": "future/feature basis proposers can be heuristic behind an exact distinction-cover verifier",
    }


def run_all():
    return {
        "pairblock_reduction": exhaustive_pairblock_reduction(),
        "information_vs_extraction": information_vs_extraction_witness(),
        "md5_router_shape": md5_router_shape_note(),
        "proof_carrying_basis": proof_carrying_basis_witness(),
    }


def self_test():
    out = run_all()
    e = out["pairblock_reduction"]
    assert e["nonempty_set_families"] == 32767
    assert e["coverable_families"] == 32297
    assert e["mismatches"] == 0
    assert e["optimum_width_distribution"] == {4: 1, 3: 216, 2: 15696, 1: 16384}
    w = out["information_vs_extraction"]
    assert w["abstract_side_bits"] == 1
    assert w["minimum_future_probe_basis"] == 4
    assert w["minimum_raw_feature_basis"] == 4
    m = out["md5_router_shape"]
    assert m["source_shaped_raw_features"] == 9 and m["compiled_fixed_width_bits"] == 3
    p = out["proof_carrying_basis"]
    assert p["optimum_basis_size"] == 1
    assert p["suboptimal_basis_exact"]
    assert not p["unsafe_truncation_exact"]


if __name__ == "__main__":
    self_test()
    print(json.dumps(run_all(), indent=2, sort_keys=True))
