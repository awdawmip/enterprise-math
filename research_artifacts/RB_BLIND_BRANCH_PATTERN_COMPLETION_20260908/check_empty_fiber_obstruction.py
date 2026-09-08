"""Integer polynomial and finite-label checks for a blind empty-fiber obstruction.

The only mathematical code dependency is our corrected frozen task-local
integer ring checker. No coordinate, division, root or rational function is
evaluated. Paper arguments establish the geometric implication.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from research_artifacts.RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908 import check_squareclass_rr as p

REL = "research_artifacts/RB_BLIND_BRANCH_PATTERN_COMPLETION_20260908"
DEPENDENCIES = {
    "check_squareclass_rr.py": "32282b30357638b5f0a2b709a0c917b29711b43a4d7f407a113bfb6502ddf269",
    "squareclass_rr_certificate.json": "d861e5b4d9d5b562c7e2a972c56b30144f2cd41275963f80a3aa80c5f1d3a289",
    "source_binding.json": "516400d46ae5dd5a8aa2d25520021ee3a57dc839538746a550ad2a7bfae2a473",
}


def base_curve_reduce(polynomial):
    """Indices a,b denote the parameter u,v, with v^2=u^3-3u."""
    result = {}
    work = list(polynomial.items())
    while work:
        monomial, coefficient = work.pop()
        if monomial[1] >= 2:
            cubic = list(monomial)
            cubic[1] -= 2
            cubic[0] += 3
            linear = list(monomial)
            linear[1] -= 2
            linear[0] += 1
            work.append((tuple(cubic), coefficient))
            work.append((tuple(linear), -3 * coefficient))
        else:
            result[monomial] = result.get(monomial, 0) + coefficient
    return p.add(result)


def mul(*values):
    return base_curve_reduce(p.multiply(*values))


def determinant(matrix):
    return p.add(mul(matrix[0][0], matrix[1][1], matrix[2][2]),
                 mul(matrix[0][1], matrix[1][2], matrix[2][0]),
                 mul(matrix[0][2], matrix[1][0], matrix[2][1]),
                 p.scale(mul(matrix[0][2], matrix[1][1], matrix[2][0]), -1),
                 p.scale(mul(matrix[0][1], matrix[1][0], matrix[2][2]), -1),
                 p.scale(mul(matrix[0][0], matrix[1][2], matrix[2][1]), -1))


def identities():
    u, v, A, B, C, _, R, t, k, _s = (p.variable(i) for i in range(len(p.NAMES)))
    h_num = p.add(t, v)
    h_den = p.add(R, p.scale(u, -1))
    U = p.add(mul(p.twice_delta(h_num), h_den),
              p.scale(mul(h_num, p.twice_delta(h_den)), -1))
    U_expected = p.add(mul(R, R, R), p.scale(mul(u, R, R), -3), p.scale(R, 3),
                       p.scale(u, 3), p.scale(mul(v, t), -2))
    if U != U_expected:
        raise AssertionError("general-pole basis derivative identity failed")
    W = p.add(mul(A, p.add(mul(R, U), p.scale(mul(t, h_num, h_den), -2))),
              mul(B, U), p.scale(mul(C, t, h_den, h_den), 2))
    k_square = mul(k, k)
    matrix = [
        [p.constant(6), p.scale(u, -3), p.scale(k, -2)],
        [p.add(p.scale(k_square, -1), p.scale(u, -6), p.scale(mul(v, k), 4)),
         p.constant(6), p.scale(mul(k, u), 4)],
        [p.add(p.scale(mul(u, k_square), -1), p.scale(mul(u, v, k), -2)),
         p.add(k_square, p.scale(u, 3), p.scale(mul(v, k), 2)),
         p.scale(mul(k, u, u), -2)],
    ]
    coefficient_rows = [p.add(*(mul(entry, minor) for entry, minor in zip(row, (A, B, C))))
                        for row in matrix]
    expected_restriction = p.add(mul(coefficient_rows[0], R, R), mul(coefficient_rows[1], R),
                                 coefficient_rows[2])
    actual_restriction = base_curve_reduce(p.restrict_to_critical_divisor(W))
    if actual_restriction != expected_restriction:
        raise AssertionError("critical-divisor coefficient matrix failed")
    actual_det = determinant(matrix)
    factor = mul(p.constant(2), k, p.add(v, p.scale(k, -1)), p.add(v, p.scale(k, -1)),
                 p.add(p.scale(u, 18), k_square))
    if actual_det != factor:
        raise AssertionError("determinant factorization failed")
    # An altered coefficient must not be hidden by the formal relation normalizer.
    changed = [[dict(entry) for entry in row] for row in matrix]
    changed[0][0] = p.add(changed[0][0], p.constant(1))
    if determinant(changed) == factor:
        raise AssertionError("changed matrix coefficient was not detected")
    return {"variable_aliases": {"a": "u", "b": "v", "c": "A", "d": "B", "e": "C"},
            "matrix_rows_coefficients_of_R2_R_1": [[p.polynomial_rows(value) for value in row]
                                                    for row in matrix],
            "determinant": p.polynomial_rows(actual_det),
            "determinant_factorization": "2*k*(v-k)^2*(18*u+k^2)",
            "integer_identities_checked": 3,
            "changed_matrix_coefficient_rejected": True}


def branch_triples():
    # First coordinate is the signed coefficient of P in this group calculation,
    # not negative native population. Second coordinate is a two-torsion label.
    labels = ((0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (-1, 0))
    rows = []
    sums = set()
    for triple in itertools.combinations(range(6), 3):
        point_sum = (sum(labels[i][0] for i in triple),
                     labels[triple[0]][1] ^ labels[triple[1]][1] ^ labels[triple[2]][1])
        sums.add(point_sum)
        rows.append({"branch_indices": triple, "sum_P_coefficient_and_torsion_label": point_sum})
    expected = {(0, torsion) for torsion in range(4)} | {
        (sign, torsion) for sign in (-1, 1) for torsion in (1, 2, 3)}
    if sums != expected or len(rows) != 20:
        raise AssertionError("triple-fiber class coverage failed")
    return {"twenty_triples": rows, "ten_possible_pole_classes": sorted(sums),
            "finite_x_relations": {
                "(0,1)": "x=0", "(0,2)": "x=s", "(0,3)": "x=-s",
                "(+/-1,1)": "2*x=3", "(+/-1,2)": "x=7*s-12", "(+/-1,3)": "x=-7*s-12"},
            "origin": "(0,0)", "field_membership": "Every finite x lies in Q(s), s^2=3; no coordinate is numerically evaluated."}


def build_certificate(root):
    for name, expected_sha in DEPENDENCIES.items():
        data = root.joinpath(REL, name).read_bytes()
        if hashlib.sha256(data).hexdigest() != expected_sha:
            raise ValueError("dependency changed: " + name)
    rr = json.loads(root.joinpath(REL, "squareclass_rr_certificate.json").read_bytes())
    twists = rr["integer_identities"]["compatible_geometric_twists"]
    exclusions = []
    for row in rr["patterns"]["4+2+0+0"]["rows"]:
        empty_labels = [i for i, block in enumerate(row["finite_branch_blocks_0_1_lambda"]) if not block]
        if len(empty_labels) != 1:
            raise AssertionError("four-plus-two normalization has incorrect empty finite fiber")
        empty = empty_labels[0]
        forbidden = [entry["twists_0_1_lambda"] for entry in twists if entry["twists_0_1_lambda"][empty] == 0]
        if len(forbidden) != 4:
            raise AssertionError("trivial empty-fiber twist count failed")
        exclusions.append({"infinity_empty_representative": row["infinity_empty_representative"],
                           "empty_finite_label": empty, "excluded_geometric_twists": forbidden})
    excluded = sum(len(row["excluded_geometric_twists"]) for row in exclusions)
    original_42 = rr["patterns"]["4+2+0+0"]["geometric_squareclass_components"]
    untouched_222 = rr["patterns"]["2+2+2+0"]["geometric_squareclass_components"]
    if excluded != 180 or original_42 - excluded != 540 or untouched_222 != 1440:
        raise AssertionError("residual component count failed")
    return {"schema": "RB_BLIND_TRIVIAL_EMPTY_FIBER_OBSTRUCTION_V1",
            "phase": "BLIND_FORWARD_PROGRESS_NOT_FINAL_RAW_FREEZE",
            "dependencies": DEPENDENCIES,
            "formal_integer_checks": identities(), "triple_fiber_classes": branch_triples(),
            "excluded_components": exclusions,
            "counts": {"excluded_4_plus_2": excluded, "remaining_4_plus_2": original_42 - excluded,
                       "untouched_2_plus_2_plus_2": untouched_222, "remaining_total": original_42 - excluded + untouched_222},
            "theorem_scope": "Every finite-empty-fiber geometrically trivial square class in the 4+2 pattern is excluded for the frozen k, over an algebraic closure. No nontrivial empty square class or 2+2+2 component is excluded.",
            "necessary_paper_arguments": ["Local-degree transfer makes all three Q critical for g", "The four-point block splits as three plus one in two degree-three g fibers", "The pole class is a sum of three fixed branch points", "Each finite x(S) is in Q(sqrt(3)) while k^2 is not", "Exceptional denominator zeros are impossible for those ten classes; S=O is excluded by the prior separate proof"],
            "arithmetic": {"evaluated_divisions": 0, "evaluated_roots": 0, "brc_calls": 0,
                           "description": "Integer polynomial operations, formal curve relations and finite abelian-group labels only."},
            "not_claimed": ["RR solution in any surviving component", "X/Y reconstruction", "field descent", "period normalization", "both-pattern no-go", "formal Result or Driver acceptance", "unblinding"]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)
    result = build_certificate(args.root)
    data = p.encoded(result)
    path = args.root.joinpath(REL, "empty_fiber_obstruction_certificate.json")
    if args.write:
        path.write_bytes(data)
    elif path.read_bytes() != data:
        raise SystemExit("EMPTY_FIBER_OBSTRUCTION: FAIL (certificate bytes differ)")
    print(json.dumps({"status": "PASS", "certificate_sha256": hashlib.sha256(data).hexdigest(),
                      "counts": result["counts"], "integer_identities": 3,
                      "no_RR_solution_or_unblinding": True}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
