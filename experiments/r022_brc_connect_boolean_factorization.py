#!/usr/bin/env python3
"""R022 pass-13 exact compatibility interfaces via row quotients and biclique atoms."""
from math import ceil, log2
import json


def subset_intersection_relation(k):
    n = 1 << k
    return [[bool(i & j) for j in range(n)] for i in range(n)]


def distinct_rows(matrix):
    return len({tuple(row) for row in matrix})


def distinct_columns(matrix):
    if not matrix:
        return 0
    return len({tuple(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))})


def atom_factorization(k):
    n = 1 << k
    left_atoms = [[bool(mask & (1 << a)) for a in range(k)] for mask in range(n)]
    right_atoms = [[bool(mask & (1 << a)) for a in range(k)] for mask in range(n)]
    return left_atoms, right_atoms


def verify_factorization(matrix, left_atoms, right_atoms):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            factor = any(left_atoms[i][a] and right_atoms[j][a] for a in range(len(left_atoms[i])))
            if factor != matrix[i][j]:
                return False, (i, j)
    return True, None


def subset_intersection_model(k=5):
    matrix = subset_intersection_relation(k)
    n = 1 << k
    left_atoms, right_atoms = atom_factorization(k)
    exact, witness = verify_factorization(matrix, left_atoms, right_atoms)
    ones = sum(sum(1 for x in row if x) for row in matrix)
    memberships = sum(sum(row) for row in left_atoms) + sum(sum(row) for row in right_atoms)
    return {
        "atom_dimension": k,
        "left_branches": n,
        "right_branches": n,
        "distinct_left_compatibility_rows": distinct_rows(matrix),
        "distinct_right_compatibility_columns": distinct_columns(matrix),
        "deterministic_row_label_bits": ceil(log2(distinct_rows(matrix))),
        "full_compatibility_table_cells": n * n,
        "compatible_cells": ones,
        "atom_membership_incidences_both_sides": memberships,
        "dense_membership_bits_both_sides": 2 * n * k,
        "full_table_to_dense_membership_ratio": (n * n) / (2 * n * k),
        "average_live_atoms_per_branch": k / 2,
        "max_live_atoms_per_branch": k,
        "branch_atom_bitmask_bits": k,
        "factorization_exact": exact,
        "factorization_failure": witness,
        "boolean_rank_lower_bound": k,
        "boolean_rank_lower_bound_reason": "singleton-subset rows/columns induce a k x k identity submatrix, whose diagonal 1s require k bicliques",
        "boolean_rank_exact": k,
        "warning": "atom vocabulary compresses relation/interface structure; branch membership/configuration information remains charged",
    }


def omitted_atom_kill(k=5):
    matrix = subset_intersection_relation(k)
    left_atoms, right_atoms = atom_factorization(k)
    # Drop final atom column from both factors.
    left_bad = [row[:-1] for row in left_atoms]
    right_bad = [row[:-1] for row in right_atoms]
    exact, witness = verify_factorization(matrix, left_bad, right_bad)
    missing_singleton = 1 << (k - 1)
    return {
        "dropped_atom": k - 1,
        "exact_after_drop": exact,
        "first_failure": witness,
        "missing_singleton_pair_should_connect": matrix[missing_singleton][missing_singleton],
        "factor_after_drop_connects": any(a and b for a, b in zip(left_bad[missing_singleton], right_bad[missing_singleton])),
    }


def scaling_rows():
    rows = []
    for k in (2, 5, 10):
        n = 1 << k
        rows.append({
            "k": k,
            "branches_each_side": n,
            "deterministic_row_classes": n,
            "boolean_atom_dimension": k,
            "row_label_bits": k,
            "branch_atom_bitmask_bits": k,
            "full_relation_cells": n * n,
            "dense_membership_bits_both_sides": 2 * n * k,
            "relation_to_factor_membership_ratio": (n * n) / (2 * n * k),
        })
    return rows


def proof_carrying_factor_verifier():
    matrix = subset_intersection_relation(4)
    left, right = atom_factorization(4)
    exact, _ = verify_factorization(matrix, left, right)
    left_bad = [row[:-1] for row in left]
    right_bad = [row[:-1] for row in right]
    bad_exact, bad_witness = verify_factorization(matrix, left_bad, right_bad)
    return {
        "exact_factor_accepted": exact,
        "truncated_factor_rejected": not bad_exact,
        "truncated_failure_witness": bad_witness,
    }


def run_all():
    return {
        "subset_intersection_k5": subset_intersection_model(5),
        "omitted_atom_kill": omitted_atom_kill(5),
        "scaling": scaling_rows(),
        "proof_carrying_factor": proof_carrying_factor_verifier(),
    }


def self_test():
    out = run_all()
    m = out["subset_intersection_k5"]
    assert m["left_branches"] == 32 and m["right_branches"] == 32
    assert m["distinct_left_compatibility_rows"] == 32
    assert m["distinct_right_compatibility_columns"] == 32
    assert m["boolean_rank_exact"] == 5
    assert m["full_compatibility_table_cells"] == 1024
    assert m["compatible_cells"] == 781
    assert m["atom_membership_incidences_both_sides"] == 160
    assert m["dense_membership_bits_both_sides"] == 320
    assert m["factorization_exact"]
    k = out["omitted_atom_kill"]
    assert not k["exact_after_drop"]
    assert k["missing_singleton_pair_should_connect"]
    assert not k["factor_after_drop_connects"]
    p = out["proof_carrying_factor"]
    assert p["exact_factor_accepted"] and p["truncated_factor_rejected"]


if __name__ == "__main__":
    self_test()
    print(json.dumps(run_all(), indent=2, sort_keys=True))
