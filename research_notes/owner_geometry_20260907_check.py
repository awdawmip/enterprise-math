"""Bounded exact witnesses for the conditional X6/BRC geometry note.

No solver, dynamics inference, randomized search, or floating arithmetic.
The six-channel contract uses columns as input and rows as output.
Run from any directory; stdout is the complete compact JSON certificate.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from enterprise_math.brc_histogram import WeightHistogram
from enterprise_math.brc_weighted import (
    CWM_ONE,
    CWM_ZERO,
    cwm_edge,
    cwm_propagate,
    cwm_recoalesce,
)
from enterprise_math.brc_weighted_recurrent import recurrent_mass_power

N = 6


def kernel(axis):
    return tuple(
        tuple(F(int(d == axis)) if c == axis else
              F(int(d != axis), 5) for c in range(N))
        for d in range(N)
    )


def paths(start, word):
    """Keep every distinct intermediate-channel branch, even after merging."""
    current = [(start, (start,), CWM_ONE)]
    for axis in word:
        matrix = kernel(axis)
        following = []
        for source, history, state in current:
            for target in range(N):
                weight = matrix[target][source]
                if weight:
                    following.append((target, history + (target,),
                                      cwm_propagate(state, cwm_edge(weight))))
        current = following
    return current


def observe(branches):
    total = CWM_ZERO
    vector = [F(0) for _ in range(N)]
    weights = []
    for target, _, state in branches:
        assert state.count == 1
        total = cwm_recoalesce(total, state)
        vector[target] += state.total
        weights.append(state.total)
    histogram = WeightHistogram.from_weights(weights)
    assert (histogram.count, histogram.total_mass, histogram.dominant_mass) == (
        total.count, total.total, total.dominant)
    return vector, total, histogram


def endpoint(signed_word):
    result = [0] * N
    for axis, sign in signed_word:
        result[axis] += sign
    return tuple(result)


def record(branches):
    vector, state, hist = observe(branches)
    return {
        "channel_mass": [str(x) for x in vector],
        "CWM": [state.count, str(state.total), str(state.dominant)],
        "weight_histogram": [[str(w), c] for w, c in hist.entries],
    }


def main():
    matrices = [kernel(i) for i in range(N)]
    covariance_checks = 0
    for axis, matrix in enumerate(matrices):
        assert all(x >= 0 for row in matrix for x in row)
        assert all(sum(matrix[d][c] for d in range(N)) == 1
                   for c in range(N))
        assert recurrent_mass_power(matrix, 2) == matrix
        assert matrix != recurrent_mass_power(matrix, 0)
        # These adjacent transpositions generate the full simultaneous S6 action.
        for adjacent in range(N - 1):
            permutation = list(range(N))
            permutation[adjacent], permutation[adjacent + 1] = (
                permutation[adjacent + 1], permutation[adjacent])
            transformed = matrices[permutation[axis]]
            assert all(transformed[permutation[d]][permutation[c]] == matrix[d][c]
                       for d in range(N) for c in range(N))
            covariance_checks += 1

    square_checks = 0
    backtrack_checks = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            forward, first, _ = observe(paths(i, (i, j)))
            swapped, second, _ = observe(paths(i, (j, i)))
            assert forward == [F(int(d != j), 5) for d in range(N)]
            assert swapped == [F(1, 5) if d == i else F(4, 25)
                               for d in range(N)]
            assert (first.count, first.total, first.dominant) == (5, F(1), F(1, 5))
            assert (second.count, second.total, second.dominant) == (21, F(1), F(1, 5))
            assert sum(abs(a - b) for a, b in zip(forward, swapped)) == F(8, 25)
            assert endpoint(((i, 1), (j, 1))) == endpoint(((j, 1), (i, 1)))
            square_checks += 1
            returned, state, _ = observe(paths(j, (i, i)))
            assert endpoint(((i, 1), (i, -1))) == (0,) * N
            assert returned == [F(int(d != i), 5) for d in range(N)]
            assert returned != [F(int(d == j)) for d in range(N)]
            assert (state.count, state.total, state.dominant) == (25, F(1), F(1, 25))
            backtrack_checks += 1

    # Exact coefficient identity L A_i = L; enough for every finite future word.
    mass_factorizations = 0
    for matrix in matrices:
        assert tuple(sum(matrix[d][c] for d in range(N)) for c in range(N)) == (F(1),) * N
        mass_factorizations += 1

    # Check the elementary common-fixed-row argument on every coordinate pair:
    # choose an actual axis outside the pair; A_i makes its two columns equal.
    equal_column_witnesses = 0
    for c in range(N):
        for d in range(c + 1, N):
            i = next(i for i in range(N) if i not in (c, d))
            assert tuple(matrices[i][r][c] for r in range(N)) == tuple(
                matrices[i][r][d] for r in range(N))
            equal_column_witnesses += 1

    # Identity on channel masses need not be identity on BRC provenance.
    split = [cwm_edge(F(1, 2)), cwm_edge(F(1, 2))]
    identity_visible = cwm_recoalesce(*split)
    round_trip = cwm_recoalesce(*(cwm_propagate(s, cwm_edge(1)) for s in split))
    assert identity_visible == round_trip
    assert (round_trip.count, round_trip.total, round_trip.dominant) == (2, F(1), F(1, 2))
    assert round_trip != CWM_ONE

    # A positive inverse alone permits diagonal reweighting before normalization.
    a, b = F(2), F(3)
    displacement = (2, -1, 0, 1, -2, 3)
    diagonal_checks = 0
    for c in range(N):
        composed = F(1)
        for i, power in enumerate(displacement):
            coefficient = a if c == i else b
            assert coefficient * (1 / coefficient) == 1
            composed *= coefficient ** power
        assert composed == b ** sum(displacement) * (a / b) ** displacement[c]
        diagonal_checks += 1

    return {
        "status": "PASS",
        "arithmetic": "fractions.Fraction; finite deterministic checks",
        "checks": {
            "idempotent_stochastic_kernels": N,
            "S6_generator_covariance": covariance_checks,
            "ordered_native_squares": square_checks,
            "signed_native_backtracks": backtrack_checks,
            "total_mass_factorizations": mass_factorizations,
            "common_fixed_row_pair_witnesses": equal_column_witnesses,
            "unnormalized_displacement_coordinates": diagonal_checks,
            "microscopic_identity_counterexample": 1,
        },
        "axis_labels": "script 0..5 correspond to note 1..6",
        "witness_start_channel": 0,
        "path_0_then_1": record(paths(0, (0, 1))),
        "path_1_then_0": record(paths(0, (1, 0))),
        "channel_l1_defect": "8/25",
        "backtrack_axis_0_start_1": record(paths(1, (0, 0))),
        "identity_visible_round_trip_CWM": [2, "1", "1/2"],
        "scope": "conditional auxiliary X6/BRC fixture; not a physical law or official claim",
        "global_knowledge": "main@4fa7d7d",
    }


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, separators=(",", ":")))
