#!/usr/bin/env python3
"""R022 pass-14 checkpoint sufficiency, generalized precision debt and rewind/storage Pareto."""
from math import ceil, log2
import json


def set_partitions(n):
    items = list(range(n))
    out = {}

    def rec(rest):
        if not rest:
            yield []
            return
        first = rest[0]
        for p in rec(rest[1:]):
            yield [{first}] + [set(b) for b in p]
            for i in range(len(p)):
                q = [set(b) for b in p]
                q[i].add(first)
                yield q

    for p in rec(items):
        canon = tuple(sorted(tuple(sorted(b)) for b in p))
        out[canon] = canon
    return list(out.values())


def relation(partition):
    return {(x, y) for block in partition for x in block for y in block}


def determines(existing, target):
    return relation(existing) <= relation(target)


def side_alphabet(existing, target):
    """Minimum local side-label alphabet so (existing token, side) determines target token."""
    return max(
        sum(1 for t in target if set(e) & set(t))
        for e in existing
    )


def side_bits(existing, target):
    return ceil(log2(side_alphabet(existing, target)))


def constructive_local_labels(n, existing, target):
    labels = {}
    for e in existing:
        touched = [t for t in target if set(e) & set(t)]
        for i, t in enumerate(touched):
            for x in set(e) & set(t):
                labels[x] = i
    seen = {}
    for x in range(n):
        e_id = next(i for i, b in enumerate(existing) if x in b)
        t_id = next(i for i, b in enumerate(target) if x in b)
        key = (e_id, labels[x])
        if key in seen and seen[key] != t_id:
            return False
        seen[key] = t_id
    return max(labels.values(), default=0) + 1 <= side_alphabet(existing, target)


def exhaustive_arbitrary_partition_debt(n=5):
    parts = set_partitions(n)
    distribution = {}
    pairs = 0
    zero_debt_pairs = 0
    for existing in parts:
        for target in parts:
            pairs += 1
            m = side_alphabet(existing, target)
            distribution[m] = distribution.get(m, 0) + 1
            assert constructive_local_labels(n, existing, target)
            if side_bits(existing, target) == 0:
                zero_debt_pairs += 1
                assert determines(existing, target)
            if determines(existing, target):
                assert m == 1
    return {
        "states": n,
        "partitions": len(parts),
        "ordered_partition_pairs": pairs,
        "side_alphabet_distribution": distribution,
        "zero_debt_pairs": zero_debt_pairs,
        "counterexample": False,
    }


def nested_checkpoint_frontier():
    p0 = tuple((i,) for i in range(8))
    p1 = ((0, 1), (2, 3), (4, 5), (6, 7))
    p2 = ((0, 1, 2, 3), (4, 5, 6, 7))
    p3 = ((0, 1, 2, 3, 4, 5, 6, 7),)
    checkpoints = [p0, p1, p2, p3]
    target = p1
    current = 3
    rows = []
    for i, p in enumerate(checkpoints):
        rows.append({
            "checkpoint": i,
            "sufficient_without_side_metadata": determines(p, target),
            "minimum_side_alphabet": side_alphabet(p, target),
            "minimum_fixed_side_bits": side_bits(p, target),
            "rewind_depth": current - i,
        })
    latest = max(i for i, p in enumerate(checkpoints) if determines(p, target))
    pareto = []
    for row in rows:
        dominated = any(
            other["minimum_fixed_side_bits"] <= row["minimum_fixed_side_bits"]
            and other["rewind_depth"] <= row["rewind_depth"]
            and (
                other["minimum_fixed_side_bits"] < row["minimum_fixed_side_bits"]
                or other["rewind_depth"] < row["rewind_depth"]
            )
            for other in rows
        )
        if not dominated:
            pareto.append(row)
    return {
        "target_partition": target,
        "current_checkpoint": current,
        "latest_sufficient_checkpoint_without_extra_metadata": latest,
        "minimal_rewind_depth_without_extra_metadata": current - latest,
        "checkpoint_rows": rows,
        "storage_rewind_pareto": pareto,
    }


def latest_sufficient_theorem_witness():
    data = nested_checkpoint_frontier()
    rows = data["checkpoint_rows"]
    # Later than checkpoint 1, old tokens alone do not determine the target; side debt repairs them.
    return {
        "checkpoint_1_zero_bits_depth_2": rows[1]["minimum_fixed_side_bits"] == 0 and rows[1]["rewind_depth"] == 2,
        "checkpoint_2_one_bit_depth_1": rows[2]["minimum_fixed_side_bits"] == 1 and rows[2]["rewind_depth"] == 1,
        "checkpoint_3_two_bits_depth_0": rows[3]["minimum_fixed_side_bits"] == 2 and rows[3]["rewind_depth"] == 0,
        "lesson": "side metadata can move the latest information-sufficient recovery point forward, trading storage for rewind depth",
    }


def run_all():
    return {
        "arbitrary_partition_debt": exhaustive_arbitrary_partition_debt(),
        "checkpoint_frontier": nested_checkpoint_frontier(),
        "storage_rewind_witness": latest_sufficient_theorem_witness(),
    }


def self_test():
    out = run_all()
    a = out["arbitrary_partition_debt"]
    assert a["partitions"] == 52
    assert a["ordered_partition_pairs"] == 2704
    assert a["side_alphabet_distribution"] == {1: 358, 2: 1825, 3: 485, 4: 35, 5: 1}
    assert a["zero_debt_pairs"] == 358
    c = out["checkpoint_frontier"]
    assert c["latest_sufficient_checkpoint_without_extra_metadata"] == 1
    assert c["minimal_rewind_depth_without_extra_metadata"] == 2
    assert [(r["minimum_fixed_side_bits"], r["rewind_depth"]) for r in c["storage_rewind_pareto"]] == [(0, 2), (1, 1), (2, 0)]
    w = out["storage_rewind_witness"]
    assert all(v for k, v in w.items() if k != "lesson")


if __name__ == "__main__":
    self_test()
    print(json.dumps(run_all(), indent=2, sort_keys=True))
