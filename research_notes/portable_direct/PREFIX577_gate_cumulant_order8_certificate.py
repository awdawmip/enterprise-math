#!/usr/bin/env python3
"""PREFIX-577: exact fifth-through-eighth gate-cumulant rates on frozen native X6-BRC.

Frozen science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Reuses PREFIX565/566 native kernel and gate-preserving quotient, and PREFIX576's
first three mean-zero group-inverse potentials. Standard-library exact arithmetic.
"""
from collections import Counter, deque
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import json
import hashlib

from PREFIX565_positive_marginal_certificate import (
    SCIENCE_PIN, ZERO_ROOT, ROOTS, ACTIONS, edge
)
from PREFIX566_gate_quotient_certificate import marginal_gate_rows, weighted_quotient
from PREFIX576_gate_cumulant_rank_one_certificate import X, Y, Z

PIN = "f42f2906d77f24085c123f3ccfe9667d41caa96d"
ORDER = 8
DEPTH = 128
SNAPSHOT_DEPTHS = (128,)


def poly_mul(a, b, degree):
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, ai in enumerate(a[:degree + 1]):
        if not ai:
            continue
        for j, bj in enumerate(b[:degree + 1 - i]):
            if bj:
                out[i + j] += ai * bj
    return out


def poly_pow(a, power, degree):
    out = [Fraction(0) for _ in range(degree + 1)]
    out[0] = Fraction(1)
    for _ in range(power):
        out = poly_mul(out, a, degree)
    return out


def cumulants_from_resolvent(a, r_coefficients, order):
    # epsilon = delta * (a + r_0 epsilon + r_1 epsilon^2 + ...).
    epsilon = [Fraction(0) for _ in range(order + 1)]
    for degree in range(1, order + 1):
        rhs = [Fraction(0) for _ in range(order)]
        rhs[0] = a
        for j, rj in enumerate(r_coefficients):
            power = poly_pow(epsilon, j + 1, order - 1)
            for k in range(order):
                rhs[k] += rj * power[k]
        epsilon[degree] = rhs[degree - 1]

    # Substitute delta=e^s-1, then take log(lambda(e^s)).
    delta = [Fraction(0)] + [
        Fraction(1, factorial(k)) for k in range(1, order + 1)
    ]
    lam = [Fraction(0) for _ in range(order + 1)]
    lam[0] = Fraction(1)
    delta_power = [Fraction(1)] + [Fraction(0) for _ in range(order)]
    for degree in range(1, order + 1):
        delta_power = poly_mul(delta_power, delta, order)
        for k in range(order + 1):
            lam[k] += epsilon[degree] * delta_power[k]

    u = lam[:]
    u[0] -= 1
    log_series = [Fraction(0) for _ in range(order + 1)]
    u_power = [Fraction(1)] + [Fraction(0) for _ in range(order)]
    for degree in range(1, order + 1):
        u_power = poly_mul(u_power, u, order)
        coefficient = Fraction(1 if degree % 2 else -1, degree)
        for k in range(order + 1):
            log_series[k] += coefficient * u_power[k]

    kappas = [
        factorial(k) * log_series[k] for k in range(1, order + 1)
    ]
    return epsilon, log_series, kappas


def solve_mean_zero(L, sizes, rhs):
    """Solve Lx=rhs with sum_i sizes_i*x_i=0 using exact Fraction elimination."""
    n = len(sizes)
    matrix = [[Fraction(v) for v in row] for row in L]
    target = [Fraction(v) for v in rhs]
    matrix[0] = [Fraction(v) for v in sizes]
    target[0] = Fraction(0)

    for col in range(n):
        pivot = next((row for row in range(col, n) if matrix[row][col]), None)
        assert pivot is not None, ("singular constrained system", col)
        if pivot != col:
            matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
            target[col], target[pivot] = target[pivot], target[col]
        scale = matrix[col][col]
        matrix[col] = [v / scale for v in matrix[col]]
        target[col] /= scale
        for row in range(n):
            if row == col or not matrix[row][col]:
                continue
            factor = matrix[row][col]
            matrix[row] = [
                matrix[row][j] - factor * matrix[col][j] for j in range(n)
            ]
            target[row] -= factor * target[col]

    solution = tuple(target)
    assert sum(Fraction(sizes[i]) * solution[i] for i in range(n)) == 0
    assert all(
        sum(Fraction(L[i][j]) * solution[j] for j in range(n)) == rhs[i]
        for i in range(n)
    )
    return solution


def reachable(graph, start):
    seen = {start}
    queue = deque([start])
    while queue:
        i = queue.popleft()
        for j in graph[i]:
            if j not in seen:
                seen.add(j)
                queue.append(j)
    return seen


def finite_moment_dp(transitions, sizes, depth=DEPTH, order=ORDER):
    n = len(sizes)
    moments = [[0] * n for _ in range(order + 1)]
    moments[0] = list(sizes)
    snapshots = []

    for d in range(depth + 1):
        total = sum(moments[0])
        assert total == 96 * (6 ** d)
        if d in SNAPSHOT_DEPTHS:
            raw = [Fraction(sum(moments[k]), total) for k in range(order + 1)]
            cumulants = []
            for r in range(1, order + 1):
                value = raw[r]
                for j in range(1, r):
                    value -= comb(r - 1, j - 1) * cumulants[j - 1] * raw[r - j]
                cumulants.append(value)
            rates = [value / d for value in cumulants]
            rate_strings = [str(v) for v in rates]
            rate_digest = hashlib.sha256("\n".join(rate_strings).encode("utf-8")).hexdigest()
            snapshots.append({
                "depth": d,
                "total_paths": str(total),
                "orders_computed": order,
                "first_four_cumulant_rates": rate_strings[:4],
                "all_eight_cumulant_rates_sha256": rate_digest,
            })

        if d == depth:
            break

        new = [[0] * n for _ in range(order + 1)]
        for i, row in enumerate(transitions):
            for (j, gate), multiplicity in row.items():
                if gate:
                    for r in range(order + 1):
                        value = sum(
                            comb(r, k) * moments[k][i] for k in range(r + 1)
                        )
                        new[r][j] += multiplicity * value
                else:
                    for r in range(order + 1):
                        new[r][j] += multiplicity * moments[r][i]
        moments = new

    return {
        "initial_distribution": "stationary pushforward pi_i=class_size_i/96",
        "raw_moment_orders": list(range(1, order + 1)),
        "depths_checked": [0, depth],
        "snapshots": snapshots,
    }


def main():
    assert SCIENCE_PIN == PIN
    assert len(ROOTS) == 9 and len(ACTIONS) == 6

    # Reconstruct the exact native 96-port BRC action table and gate-preserving quotient.
    native = [[edge(i, action, ZERO_ROOT) for action in ACTIONS] for i in range(96)]
    assert all(len(row) == 6 for row in native)
    indegree = Counter(j for row in native for j, weight in row)
    assert set(indegree) == set(range(96)) and set(indegree.values()) == {6}
    native_gate_edges = sorted(
        (i, j) for i, row in enumerate(native) for j, weight in row if weight[6]
    )
    assert native_gate_edges == [(7, 9), (29, 9), (31, 9)]

    rows = marginal_gate_rows(ZERO_ROOT)
    assert all(marginal_gate_rows(root) == rows for root in ROOTS)
    ids, quotient, growth = weighted_quotient(rows)
    assert len(ids) == 96 and len(quotient) == 37
    assert growth == [1, 4, 13, 21, 33, 37]

    n = 37
    C = [[0] * n for _ in range(n)]
    gate_source = [0] * n
    marked_edges = []
    for i, row in enumerate(quotient):
        for (j, x, y, mark), multiplicity in row.items():
            C[i][j] += multiplicity
            gate_source[i] += multiplicity * mark
            if mark:
                marked_edges.append((i, j, multiplicity, x, y))

    sizes = [Counter(ids)[i] for i in range(n)]
    assert all(sum(row) == 6 for row in C)
    assert sum(sizes) == 96
    assert all(
        sum(sizes[i] * C[i][j] for i in range(n)) == 6 * sizes[j]
        for j in range(n)
    )
    assert sorted(marked_edges) == [
        (4, 5, 1, 0, 0), (15, 5, 1, 0, 0), (17, 5, 1, 0, 0)
    ]
    assert [(i, v) for i, v in enumerate(gate_source) if v] == [
        (4, 1), (15, 1), (17, 1)
    ]

    L = [[6 * (i == j) - C[i][j] for j in range(n)] for i in range(n)]
    adjacency = [{j for j, value in enumerate(C[i]) if value} for i in range(n)]
    reverse = [set() for _ in range(n)]
    for i in range(n):
        for j in adjacency[i]:
            reverse[j].add(i)
    assert len(reachable(adjacency, 0)) == n
    assert len(reachable(reverse, 0)) == n

    color = [None] * n
    color[0] = 0
    queue = deque([0])
    while queue:
        i = queue.popleft()
        for j in adjacency[i]:
            if color[j] is None:
                color[j] = 1 - color[i]
                queue.append(j)
            else:
                assert color[j] == 1 - color[i]
    assert (color.count(0), color.count(1)) == (17, 20)
    bipartition_masses = [
        sum(sizes[i] for i in range(n) if color[i] == side)
        for side in (0, 1)
    ]
    assert bipartition_masses == [48, 48]
    assert 7 in adjacency[0] and 0 in adjacency[7]  # period exactly two

    # Recheck the prior X/Y/Z potentials, then extend the group-inverse chain to T.
    prior = [tuple(map(Fraction, X)), tuple(map(Fraction, Y)), tuple(map(Fraction, Z))]
    assert all(
        sum(L[i][j] * prior[0][j] for j in range(n)) == 2304 * gate_source[i] - 72
        for i in range(n)
    )
    assert all(
        sum(L[i][j] * prior[1][j] for j in range(n)) == 72 * prior[0][i]
        for i in range(n)
    )
    assert all(
        sum(L[i][j] * prior[2][j] for j in range(n)) == 72 * prior[1][i]
        for i in range(n)
    )
    assert all(
        sum(sizes[i] * vector[i] for i in range(n)) == 0 for vector in prior
    )

    potentials = prior[:]
    for _ in range(4):
        previous = potentials[-1]
        rhs = [72 * value for value in previous]
        current = solve_mean_zero(L, sizes, rhs)
        assert all(value.denominator == 1 for value in current)
        potentials.append(current)

    denominators = [384 * (12 ** k) for k in range(7)]
    names = ["X", "Y", "Z", "U", "V", "W", "T"]
    assert len(potentials) == 7
    for k in range(1, 7):
        assert all(
            sum(L[i][j] * potentials[k][j] for j in range(n))
            == 72 * potentials[k - 1][i]
            for i in range(n)
        )
        assert sum(sizes[i] * potentials[k][i] for i in range(n)) == 0

    a = Fraction(1, 192)
    r = [
        (((-1) ** k) * potentials[k][5]) / (6 * denominators[k])
        for k in range(7)
    ]
    epsilon, psi, kappa = cumulants_from_resolvent(a, r, ORDER)

    # The existing PREFIX-576 first four asymptotic rates must be reproduced.
    expected_prefix576 = [
        Fraction(1, 192),
        Fraction(1127, 221184),
        Fraction(206963, 42467328),
        Fraction(434651857, 97844723712),
    ]
    assert kappa[:4] == expected_prefix576

    transitions = []
    for row in quotient:
        grouped = Counter()
        for (j, x, y, mark), multiplicity in row.items():
            grouped[(j, mark)] += multiplicity
        transitions.append(grouped)
    assert sum(len(row) for row in transitions) == 109

    finite = finite_moment_dp(transitions, sizes)
    old_results_path = Path(__file__).with_name("PREFIX576_GATE_CUMULANT_RESULTS.json")
    old_results = json.loads(old_results_path.read_text(encoding="utf-8"))
    old_128 = next(
        row for row in old_results["finite_stationary_integer_DP"]["snapshots"]
        if row["depth"] == 128
    )
    new_128 = next(row for row in finite["snapshots"] if row["depth"] == 128)
    assert new_128["first_four_cumulant_rates"][0] == old_128["mean_per_step"]
    assert new_128["first_four_cumulant_rates"][1] == old_128["variance_per_step"]
    assert new_128["first_four_cumulant_rates"][2] == old_128["third_cumulant_per_step"]
    assert new_128["first_four_cumulant_rates"][3] == old_128["fourth_cumulant_per_step"]

    return {
        "status": "ALL_CHECKS_PASS",
        "line": "PREFIX-577",
        "science_pin": PIN,
        "model": "frozen four-STAR native X6-BRC; 48 phases; 96 ordered ports; six labeled actions",
        "observer": "q1=q2=q3=q4=q5=q6=1; gate counter retained",
        "quotient": {
            "native_ports": 96,
            "classes": 37,
            "partition_growth": growth,
            "class_sizes": sizes,
            "stationary_distribution": "pi_i=class_size_i/96",
            "gate_sources": [4, 15, 17],
            "gate_target": 5,
            "gate_perturbation": "P(z)=P(1)+(z-1) g e_5^T/6",
            "bipartition": [17, 20],
            "bipartition_stationary_masses": bipartition_masses,
            "period": 2,
        },
        "inherited_group_inverse_potentials": {
            "source": "PREFIX576_gate_cumulant_rank_one_certificate.py",
            "source_blob": "d1ba22145e7c38afbda26469f23dc10849285cc0",
            "vectors": ["X", "Y", "Z"],
            "denominators": denominators[:3],
            "rechecked": True,
        },
        "new_group_inverse_potentials": {
            name: {
                "denominator": denominators[i],
                "weighted_mean": "0",
                "target_class_5": str(potentials[i][5]),
                "integer_equation": f"(6I-C){name}=72*{names[i-1]}",
                "full_vector_recomputed_and_row_verified": True,
            }
            for i, name in enumerate(names[3:], start=3)
        },
        "resolvent_laurent": {
            "a_minus1": str(a),
            **{f"r{k}": str(value) for k, value in enumerate(r)},
        },
        "lambda_delta_coefficients": {
            f"c{k}": str(epsilon[k]) for k in range(1, ORDER + 1)
        },
        "asymptotic_cumulant_rates": {
            f"kappa{k}": str(value) for k, value in enumerate(kappa, 1)
        },
        "scaled_cumulant_generating_function_coefficients": {
            f"s^{k}": str(psi[k]) for k in range(1, ORDER + 1)
        },
        "finite_stationary_integer_DP": {
            "initial_distribution": finite["initial_distribution"],
            "raw_moment_orders": finite["raw_moment_orders"],
            "depth": DEPTH,
            "total_paths": finite["snapshots"][0]["total_paths"],
            "first_four_match_prefix576": True,
            "all_eight_cumulant_rates_sha256": finite["snapshots"][0]["all_eight_cumulant_rates_sha256"],
        },
        "validation": {
            "native_outdegree": 6,
            "native_indegree": 6,
            "native_gate_edges": native_gate_edges,
            "marked_quotient_edges": [list(v) for v in sorted(marked_edges)],
            "root_invariance_checks": len(ROOTS),
            "quotient_rows": 37,
            "stationary_identity_rows": 37,
            "group_inverse_rows": [37] * 7,
            "weighted_mean_zero_potentials": 7,
            "moment_orders": list(range(1, ORDER + 1)),
            "finite_DP_depth": DEPTH,
            "finite_DP_transition_types": 109,
            "depth_128_paths": str(96 * (6 ** DEPTH)),
            "all_assertions_pass": True,
        },
        "status_boundary": "AUTHOR_PROVED / EXACT_RATIONAL_AND_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED",
        "limitations": [
            "observer is specialized to q1=...=q6=1 with the gate counter retained",
            "ordered action depth is not physical time, a heartbeat interval, or solver iteration",
            "no x=q5,y=q6 parameterized gate-cumulant theorem is claimed",
            "native activity/claim, independent review, and mathematical admission remain separate",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=2))
