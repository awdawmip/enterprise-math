"""Rebuild the finite joint CHSH and robust marginal certificate exactly."""

from fractions import Fraction as Q
from itertools import permutations, product
import json

POINTS = ((0, 0), (0, 1), (1, 0), (1, 1))
OUTCOMES = tuple(product((-1, 1), repeat=2))
SIGNS = (1, 1, 1, -1)


def score(table):
    return sum(s * a * b for s, (a, b) in zip(SIGNS, table))


def observable_differences(table):
    a, b = zip(*table)
    return tuple(u // 2 for u in (a[0] - a[1], a[2] - a[3], b[0] - b[2], b[1] - b[3]))


def determinant(matrix):
    total = 0
    for perm in permutations(range(len(matrix))):
        inversions = sum(i > j for k, i in enumerate(perm) for j in perm[k+1:])
        term = -1 if inversions % 2 else 1
        for k, column in enumerate(perm):
            term *= matrix[k][column]
        total += term
    return total


def check_shift(mass, radius):
    """Use the exact maximizing transport among the -,0,+ classes."""
    p = (mass, 1 - 2 * mass, mass)
    first = min(radius, mass)
    second = min(radius - first, p[1])
    q = (p[0] - first, p[1] - second, p[2] + first + second)
    assert min(q) >= 0 and sum(q) == 1
    assert sum(abs(a - b) for a, b in zip(p, q)) / 2 <= radius
    assert q[2] - q[0] == min(1, 2 * radius, radius + mass)


def run():
    local = []
    single_context = []
    all_tables = tuple(product(OUTCOMES, repeat=4))
    for table in all_tables:
        directions = observable_differences(table)
        exposed = sum(d != 0 for d in directions)
        if exposed == 0:
            assert abs(score(table)) == 2
            if score(table) == 2:
                local.append(table)
        elif score(table) == 4 and exposed == 1:
            single_context.append(table)
    assert len(local) == len(single_context) == 8

    # Affine weights a+b*c, where c=2v−1. The quantum input has c=sqrt(2)−1.
    weighted = (
        [(table, (Q(1, 8), Q(-1, 8))) for table in local]
        + [(table, (Q(0), Q(1, 8))) for table in single_context]
    )
    assert tuple(sum(w[i] for _, w in weighted) for i in range(2)) == (1, 0)
    quantum_cells = []
    for at, sign in enumerate(SIGNS):
        for a, b in OUTCOMES:
            coeff = tuple(sum(w[i] for table, w in weighted if table[at] == (a,b))
                          for i in range(2))
            assert coeff == (Q(1,4) + Q(sign*a*b,8), Q(sign*a*b,8))
            quantum_cells.append({"setting": POINTS[at], "outcome": (a,b),
                                  "affine_probability": tuple(map(str, coeff))})
    for axis in range(4):
        for sign in [-1, 1]:
            coeff = tuple(sum(w[i] for table, w in weighted
                              if observable_differences(table)[axis] == sign) for i in range(2))
            assert coeff == (0, Q(1, 8))
    signed_points = [[1, a1, b0, b1] for ((a0,b0),(_,b1),(a1,_),_) in local if a0 == 1]
    affine_det = determinant(signed_points)
    assert abs(affine_det) == 8
    for table in single_context:
        inverse = tuple((-a, -b) for a,b in table)
        assert inverse in single_context and inverse != table
    for table in local:
        inverse = tuple((-a, -b) for a,b in table)
        assert inverse in local and inverse != table

    radius_checks = 0
    for mass in (Q(1,32), Q(1,16), Q(3,32), Q(1,8), Q(1,3), Q(1,2)):
        for j in range(65):
            check_shift(mass, Q(j,64))
            radius_checks += 1
    return {
        "deterministic_tables": len(all_tables),
        "local_score_2_tables": len(local),
        "score_4_one_context_direction_tables": len(single_context),
        "zero_bias_local_orientation_determinant_abs": abs(affine_det),
        "tv_exact_rational_checks": radius_checks,
        "visibility": {"parametric": "(1+c)/2", "dcmp02": "1/sqrt(2)", "c_dcmp02": "sqrt(2)-1"},
        "extremal_model": [
            {"outcomes_setting_order_00_01_10_11": table,
             "marginal_differences_A0_A1_B0_B1": observable_differences(table),
             "affine_weight_in_c": tuple(map(str, w))}
            for table, w in weighted
        ],
        "all_joint_probabilities": quantum_cells,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
