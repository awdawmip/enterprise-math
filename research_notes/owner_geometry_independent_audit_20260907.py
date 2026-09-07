"""Independent finite geometry audit; only standard-library exact arithmetic.

No author or production executable is imported. Matrix countermodels with
negative entries are outside the positive BRC carrier, not physical branches.
"""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
N = 6
STEPS = tuple((axis, sign) for axis in range(N) for sign in (1, -1))
IDENTITY = tuple(tuple(Q(int(d == c)) for c in range(N)) for d in range(N))
SOURCES = (
    "research_notes/OWNER_GEOMETRY_FRONTIER_20260907.md",
    "research_notes/owner_geometry_20260907_check.py",
    "research_notes/X6_AXIS_CHANNEL_FRAME_GAUGE_AND_FLAT_TRANSPORT_V2_20260906.md",
    "research_notes/X6_CELL_TRIADIC_PORT_FRAME_INTERNAL_STATE_V1_20260906.md",
    "definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md",
    "definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json",
    "src/enterprise_math/brc_weighted.py",
    "src/enterprise_math/brc_histogram.py",
    "src/enterprise_math/brc_weighted_recurrent.py",
    "research_notes/owner_geometry_independent_audit_20260907.py",
)


def hashes():
    return {name: sha256((ROOT / name).read_bytes()).hexdigest() for name in SOURCES}


def branch_rule(axis, source):
    if source == axis:
        return ((source, Q(1)),)
    return tuple((destination, Q(1, 5)) for destination in range(N) if destination != axis)


def matrix(axis):
    columns = tuple(dict(branch_rule(axis, source)) for source in range(N))
    return tuple(tuple(columns[c].get(d, Q(0)) for c in range(N)) for d in range(N))


def multiply(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def transpose(a):
    return tuple(zip(*a))


def rank(a):
    rows = [list(map(Q, row)) for row in a]
    result = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(result, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[result], rows[pivot] = rows[pivot], rows[result]
        scale = rows[result][column]
        rows[result] = [x / scale for x in rows[result]]
        for i in range(result + 1, len(rows)):
            scale = rows[i][column]
            if scale:
                rows[i] = [a - scale * b for a, b in zip(rows[i], rows[result])]
        result += 1
    return result


def paths(start, signed_word):
    population = ((start, Q(1), (start,)),)
    position = [0] * N
    for axis, sign in signed_word:
        assert (axis, sign) in STEPS
        old_position = tuple(position)
        position[axis] += sign
        assert tuple(a - b for a, b in zip(position, old_position)) == tuple(
            sign if j == axis else 0 for j in range(N))
        population = tuple((target, weight * factor, history + (target,))
                           for source, weight, history in population
                           for target, factor in branch_rule(axis, source))
    vector = tuple(sum(weight for target, weight, _ in population if target == c)
                   for c in range(N))
    hist = Counter(weight for _, weight, _ in population)
    assert len({history for _, _, history in population}) == len(population)
    cwm = (len(population), sum(vector), max(hist))
    return tuple(position), vector, hist, cwm


def run():
    initial = hashes()
    kernels = tuple(matrix(i) for i in range(N))
    for a in kernels:
        assert multiply(a, a) == a and a != IDENTITY and rank(a) == 2
        assert all(sum(column) == 1 for column in transpose(a))
    all_permutations = tuple(permutations(range(N)))
    covariance_count = 0
    for p in all_permutations:
        for axis, sign in STEPS:
            assert all(kernels[p[axis]][p[d]][p[c]] == kernels[axis][d][c]
                       for d in range(N) for c in range(N))
            covariance_count += 1
    assert covariance_count == 8640

    # The stabilizer fixes axis 0; test its full 120 elements against S6.
    stabilizer = tuple(p for p in all_permutations if p[0] == 0)
    centralizer = tuple(p for p in all_permutations
                        if all(tuple(p[s[c]] for c in range(N)) == tuple(s[p[c]] for c in range(N))
                               for s in stabilizer))
    assert centralizer == (tuple(range(N)),)

    square_count = backtrack_count = word_count = 0
    for i, sign_i in STEPS:
        for j, sign_j in STEPS:
            if i == j:
                continue
            end1, vec1, hist1, cwm1 = paths(i, ((i, sign_i), (j, sign_j)))
            end2, vec2, hist2, cwm2 = paths(i, ((j, sign_j), (i, sign_i)))
            assert end1 == end2
            assert vec1 == tuple(Q(int(c != j), 5) for c in range(N))
            assert vec2 == tuple(Q(1, 5) if c == i else Q(4, 25) for c in range(N))
            assert sum(abs(a - b) for a, b in zip(vec1, vec2)) == Q(8, 25)
            assert hist1 == {Q(1, 5): 5}
            assert hist2 == {Q(1, 5): 1, Q(1, 25): 20}
            assert cwm1 == (5, Q(1), Q(1, 5)) and cwm2 == (21, Q(1), Q(1, 5))
            square_count += 1
        for c in range(N):
            if c == i:
                continue
            end, vector, hist, cwm = paths(c, ((i, sign_i), (i, -sign_i)))
            assert end == (0,) * N
            assert vector == tuple(Q(int(d != i), 5) for d in range(N))
            assert vector != tuple(Q(int(d == c)) for d in range(N))
            assert hist == {Q(1, 25): 25} and cwm == (25, Q(1), Q(1, 25))
            backtrack_count += 1
    for length in range(3):
        for word in product(STEPS, repeat=length):
            for start in range(N):
                assert paths(start, word)[3][1] == 1
                word_count += 1
    assert (square_count, backtrack_count, word_count) == (120, 60, 942)

    # l A_i = l is the joint nullspace of (A_i^T - I) l^T.
    constraints = tuple(tuple(a[d][c] - IDENTITY[d][c] for d in range(N))
                        for a in kernels for c in range(N))
    assert rank(constraints) == 5
    assert all(sum(row) == 0 for row in constraints)
    mass = (tuple(Q(1) for _ in range(N)),)
    assert all(multiply(mass, a) == mass for a in kernels)
    # Without surjectivity, R may act nontrivially outside im(q).
    q_not_onto = (mass[0], (Q(0),) * N)
    r_outside_image = ((Q(1), Q(0)), (Q(0), Q(2)))
    assert all(multiply(q_not_onto, a) == multiply(r_outside_image, q_not_onto) for a in kernels)
    assert rank(q_not_onto) == 1 and r_outside_image != ((Q(1), Q(0)), (Q(0), Q(1)))
    # A single named channel is not even a factorable observation for every A_i.
    assert kernels[1][0][1] == 0 and kernels[1][0][2] == Q(1, 5)

    # Positivity of the inverse matters: this inverse has negative off-diagonals.
    mix = tuple(tuple(IDENTITY[d][c] / 2 + Q(1, 12) for c in range(N)) for d in range(N))
    signed_inverse = tuple(tuple(2 * IDENTITY[d][c] - Q(1, 6) for c in range(N)) for d in range(N))
    assert multiply(mix, signed_inverse) == multiply(signed_inverse, mix) == IDENTITY
    assert all(sum(column) == 1 for column in transpose(mix))
    assert all(sum(column) == 1 for column in transpose(signed_inverse))
    assert any(x < 0 for row in signed_inverse for x in row)

    a, b = Q(2), Q(3)
    displacements = ((0,) * N, (2, -1, 0, 1, -2, 3), (-3, 2, 1, -4, 0, 2))
    diagonal_checks = 0
    for z in displacements:
        for c in range(N):
            actual = Q(1)
            for i, exponent in enumerate(z):
                actual *= (a if c == i else b) ** exponent
            assert actual == b ** sum(z) * (a / b) ** z[c]
            diagonal_checks += 1

    split_then_unit = tuple(left * right for left in (Q(1, 2), Q(1, 2)) for right in (Q(1),))
    assert sum(split_then_unit) == 1
    assert Counter(split_then_unit) == {Q(1, 2): 2}
    assert (len(split_then_unit), sum(split_then_unit), max(split_then_unit)) == (2, Q(1), Q(1, 2))
    assert Counter(split_then_unit) != {Q(1): 1}

    result = {
        "status": "PASS",
        "scope": "independent finite audit; universal conclusions require the report's proof",
        "source_hashes_sha256": initial,
        "checks": {"rank_two_idempotent_kernels": 6, "full_S6_signed_covariance": covariance_count,
                   "full_S5_stabilizer_size": len(stabilizer), "centralizer_size": len(centralizer),
                   "signed_ordered_squares": square_count, "signed_backtracks": backtrack_count,
                   "all_signed_words_through_length_2_with_start_channel": word_count,
                   "joint_fixed_row_constraint_rank": 5, "joint_fixed_row_kernel_dimension": 1,
                   "unnormalized_signed_displacement_coordinates": diagonal_checks},
        "square_l1_difference": "8/25",
        "first_square_histogram": [["1/5", 5]],
        "second_square_histogram": [["1/25", 20], ["1/5", 1]],
        "backtrack_histogram": [["1/25", 25]],
        "matrix_identity_micro_roundtrip_CWM": [2, "1", "1/2"],
        "guards": {"nonsurjective_q_does_not_force_global_R_identity": "PASS",
                   "single_channel_readout_fails_factorization": "PASS",
                   "inverse_with_negative_entries_is_outside_positive_BRC": "PASS"},
        "global_knowledge_sync": "main@4fa7d7d / GLOBAL_KNOWLEDGE_V1",
    }
    assert hashes() == initial, "audited bytes changed during execution"
    return result


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
