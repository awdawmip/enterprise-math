#!/usr/bin/env python3
"""R022 pass-15 research-only finite-state BRC compiler core.

This module consolidates semantic contracts discovered in R022. It is not a shared/canonical tool.
"""
from collections import defaultdict
from math import ceil, log2
import json


def relation(partition):
    return {(x, y) for block in partition for x in block for y in block}


def canonical_partition(groups):
    return tuple(sorted(tuple(sorted(g)) for g in groups if g))


def partition_from_key(states, key):
    groups = defaultdict(list)
    for x in states:
        groups[key(x)].append(x)
    return canonical_partition(groups.values())


def meet_partition(left, right, states):
    def block_id(partition, x):
        return next(i for i, block in enumerate(partition) if x in block)
    return partition_from_key(states, lambda x: (block_id(left, x), block_id(right, x)))


def future_kernel(states, observable, futures):
    return partition_from_key(states, lambda x: tuple(observable[f[x]] for f in futures))


def target_precision(states, current_partition, observable, futures):
    return meet_partition(current_partition, future_kernel(states, observable, futures), states)


def required_distinction_pairs(current_partition, target_partition):
    target_rel = relation(target_partition)
    pairs = []
    for block in current_partition:
        for i, x in enumerate(block):
            for y in block[i + 1:]:
                if (x, y) not in target_rel:
                    pairs.append((x, y))
    return tuple(pairs)


def verify_future_basis(states, current_partition, observable, full_futures, proposed_futures):
    full_target = target_precision(states, current_partition, observable, full_futures)
    proposed_target = target_precision(states, current_partition, observable, proposed_futures)
    return proposed_target == full_target


def verify_feature_basis(current_partition, target_partition, features):
    for x, y in required_distinction_pairs(current_partition, target_partition):
        if not any(feature[x] != feature[y] for feature in features):
            return False, (x, y)
    return True, None


def side_alphabet(existing_partition, target_partition):
    return max(sum(1 for t in target_partition if set(e) & set(t)) for e in existing_partition)


def side_bits(existing_partition, target_partition):
    return ceil(log2(side_alphabet(existing_partition, target_partition)))


def checkpoint_sufficient(existing_partition, target_partition):
    return relation(existing_partition) <= relation(target_partition)


def verify_residual_join(before, after):
    old = frozenset().union(*before) if before else frozenset()
    new = frozenset().union(*after) if after else frozenset()
    return old == new


def aggregate(values, op, zero):
    out = zero
    for v in values:
        out = op(out, v)
    return out


def verify_residual_aggregate(before, after, op, zero):
    return aggregate(before, op, zero) == aggregate(after, op, zero)


def deterministic_row_quotient(matrix):
    row_ids = {}
    labels = []
    for row in matrix:
        key = tuple(row)
        if key not in row_ids:
            row_ids[key] = len(row_ids)
        labels.append(row_ids[key])
    return tuple(labels), len(row_ids)


def verify_boolean_interface_factor(matrix, left_atoms, right_atoms):
    for i, row in enumerate(matrix):
        for j, expected in enumerate(row):
            actual = any(left_atoms[i][a] and right_atoms[j][a] for a in range(len(left_atoms[i])))
            if bool(expected) != actual:
                return False, (i, j)
    return True, None


def synthetic_end_to_end():
    states = tuple(range(6))
    observable = (0, 0, 0, 1, 1, 1)
    current = ((0, 1, 2), (3, 4, 5))
    u_a = (0, 0, 3, 0, 0, 3)  # observable pattern 0,0,1 in each coarse block
    u_b = (0, 3, 0, 0, 3, 0)  # observable pattern 0,1,0 in each coarse block
    futures = (u_a, u_b)
    target = target_precision(states, current, observable, futures)
    pairs = required_distinction_pairs(current, target)

    feature_a = tuple(observable[u_a[x]] for x in states)
    feature_b = tuple(observable[u_b[x]] for x in states)
    feature_exact, _ = verify_feature_basis(current, target, (feature_a, feature_b))
    feature_bad, feature_witness = verify_feature_basis(current, target, (feature_a,))

    future_exact = verify_future_basis(states, current, observable, futures, futures)
    future_bad = verify_future_basis(states, current, observable, futures, (u_a,))

    before_support = (frozenset({"a", "b"}), frozenset({"b", "c"}), frozenset({"c"}))
    after_support = (frozenset({"a", "b"}), frozenset({"b", "c"}))
    unsafe_support = (frozenset({"a", "b"}),)

    matrix = [[bool(i & j) for j in range(8)] for i in range(8)]
    left_atoms = [[bool(mask & (1 << a)) for a in range(3)] for mask in range(8)]
    right_atoms = [[bool(mask & (1 << a)) for a in range(3)] for mask in range(8)]
    factor_exact, _ = verify_boolean_interface_factor(matrix, left_atoms, right_atoms)
    factor_bad, factor_witness = verify_boolean_interface_factor(matrix, [r[:-1] for r in left_atoms], [r[:-1] for r in right_atoms])

    return {
        "current_partition": current,
        "target_partition": target,
        "required_distinction_pairs": pairs,
        "required_pair_count": len(pairs),
        "future_basis_exact": future_exact,
        "dropped_future_rejected": not future_bad,
        "feature_basis_exact": feature_exact,
        "dropped_feature_rejected": not feature_bad,
        "dropped_feature_witness": feature_witness,
        "side_alphabet": side_alphabet(current, target),
        "side_bits": side_bits(current, target),
        "current_checkpoint_sufficient": checkpoint_sufficient(current, target),
        "support_rewrite_exact": verify_residual_join(before_support, after_support),
        "unsafe_support_rewrite_rejected": not verify_residual_join(before_support, unsafe_support),
        "interface_factor_exact": factor_exact,
        "truncated_interface_factor_rejected": not factor_bad,
        "truncated_interface_witness": factor_witness,
        "deterministic_interface_row_classes": deterministic_row_quotient(matrix)[1],
    }


def mutation_suite():
    out = synthetic_end_to_end()
    checks = {
        "future_mutation": out["dropped_future_rejected"],
        "feature_mutation": out["dropped_feature_rejected"],
        "rjc_mutation": out["unsafe_support_rewrite_rejected"],
        "interface_mutation": out["truncated_interface_factor_rejected"],
        "checkpoint_no_resurrection": (not out["current_checkpoint_sufficient"] and out["side_bits"] == 2),
    }
    return {"checks": checks, "passed": sum(checks.values()), "total": len(checks)}


def surviving_interfaces():
    return {
        "semantic": ["future_kernel", "target_precision", "required_distinction_pairs"],
        "proof_carrying": ["verify_future_basis", "verify_feature_basis", "verify_residual_join", "verify_residual_aggregate", "verify_boolean_interface_factor"],
        "replay": ["side_alphabet", "side_bits", "checkpoint_sufficient"],
        "connect": ["deterministic_row_quotient", "verify_boolean_interface_factor"],
        "status": "research-only consolidation; not a canonical/shared tool",
    }


def run_all():
    return {
        "end_to_end": synthetic_end_to_end(),
        "mutation_suite": mutation_suite(),
        "surviving_interfaces": surviving_interfaces(),
    }


def self_test():
    out = run_all()
    e = out["end_to_end"]
    assert e["target_partition"] == ((0,), (1,), (2,), (3,), (4,), (5,))
    assert e["required_pair_count"] == 6
    assert e["future_basis_exact"] and e["dropped_future_rejected"]
    assert e["feature_basis_exact"] and e["dropped_feature_rejected"]
    assert e["side_alphabet"] == 3 and e["side_bits"] == 2
    assert not e["current_checkpoint_sufficient"]
    assert e["support_rewrite_exact"] and e["unsafe_support_rewrite_rejected"]
    assert e["interface_factor_exact"] and e["truncated_interface_factor_rejected"]
    m = out["mutation_suite"]
    assert m["passed"] == m["total"] == 5


if __name__ == "__main__":
    self_test()
    print(json.dumps(run_all(), indent=2, sort_keys=True))
