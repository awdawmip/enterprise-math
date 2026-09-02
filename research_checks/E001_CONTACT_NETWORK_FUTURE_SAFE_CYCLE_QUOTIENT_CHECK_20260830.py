#!/usr/bin/env python3
"""Exact regression for the E001 future-safe cycle-quotient criterion.

The theorem proved in the matching research return is semantic.  This checker
certifies the smallest simple-cycle pressure test and the linear persistent-state
corollary over exact rational arithmetic; it is not used as a substitute for the
proof.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import product


def transpose(matrix):
    return tuple(tuple(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0])))


def matvec(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


def matmul(left, right):
    right_t = transpose(right)
    return tuple(
        tuple(sum(a * b for a, b in zip(row, column)) for column in right_t)
        for row in left
    )


def rank_q(matrix):
    rows = [[Fraction(value) for value in row] for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    column_count = len(rows[0])
    rank = 0
    for column in range(column_count):
        pivot = next((i for i in range(rank, row_count) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][column]
        rows[rank] = [value / pivot_value for value in rows[rank]]
        for i in range(row_count):
            if i == rank or not rows[i][column]:
                continue
            factor = rows[i][column]
            rows[i] = [a - factor * b for a, b in zip(rows[i], rows[rank])]
        rank += 1
        if rank == row_count:
            break
    return rank


def linear_future_safe(incidence, witness_update):
    """ker(B) subset ker(C) iff row_Q(C) subset row_Q(B)."""
    return rank_q(tuple(incidence) + tuple(witness_update)) == rank_q(incidence)


def main():
    # Oriented triangle: columns are 1->2, 2->3, 3->1.
    incidence = (
        (-1, 0, 1),
        (1, -1, 0),
        (0, 1, -1),
    )
    cycle = (1, 1, 1)
    gram = matmul(transpose(incidence), incidence)
    identity = (
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
    )

    assert matvec(incidence, cycle) == (0, 0, 0)
    assert matvec(gram, cycle) == (0, 0, 0)
    assert rank_q(incidence) == 2

    # C=B records only body-effect information and is future-safe.
    assert linear_future_safe(incidence, incidence)
    # C=I persists the per-contact allocation itself and exposes the cycle witness.
    assert not linear_future_safe(incidence, identity)
    assert matvec(identity, cycle) == cycle

    # Exhaust every one-row C with coefficients in {-1,0,1}.  For the triangle
    # ker(B)=span_Q{(1,1,1)}, so safety is exactly c dot cycle = 0.
    mismatches = []
    cases = 0
    for row in product((-1, 0, 1), repeat=3):
        cases += 1
        kernel_test = sum(a * b for a, b in zip(row, cycle)) == 0
        rank_test = linear_future_safe(incidence, (row,))
        if kernel_test != rank_test:
            mismatches.append({"row": row, "kernel_test": kernel_test, "rank_test": rank_test})

    assert not mismatches
    report = {
        "schema": "ENTERPRISE_MATH_E001_CYCLE_QUOTIENT_CHECK_V1",
        "task_id": "RS-E001-CONTACT-NETWORK",
        "researcher_id": "EM-E001-0FB652",
        "verdict": "PASS",
        "triangle": {
            "rank_B_over_Q": rank_q(incidence),
            "cycle_vector": cycle,
            "B_cycle": matvec(incidence, cycle),
            "K_cycle": matvec(gram, cycle),
            "safe_C_equals_B": linear_future_safe(incidence, incidence),
            "unsafe_C_equals_identity": linear_future_safe(incidence, identity),
        },
        "exhaustive_one_row_C": {"cases": cases, "coefficient_alphabet": [-1, 0, 1], "mismatches": len(mismatches)},
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
