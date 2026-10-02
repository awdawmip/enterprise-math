#!/usr/bin/env python3
"""Frozen finite-graph benchmarks for positive Weighted-BRC path mass.

Run from any directory with Python 3.10+; only the standard library and the
existing enterprise_math.brc_weighted implementation are required. This is an
experiment harness, not a new BRC carrier or a signed-amplitude model.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from enterprise_math.brc_weighted import (  # noqa: E402
    CWM_ZERO, cwm_edge, cwm_propagate, cwm_recoalesce,
    is_positive_path_realizable,
)

HORIZON = 64
ENUMERATION_HORIZON = 8
TRAIN_END = 8
SAMPLE_TIMES = (0, 1, 2, 4, 8, 16, 32, 64)
CHECKS: Counter[str] = Counter()


def check(category, actual, expected):
    CHECKS[category] += 1
    if actual != expected:
        raise AssertionError((category, actual, expected))


def vector_step(p, matrix):
    return tuple(sum((p[i] * matrix[i][j] for i in range(len(p))), F(0))
                 for j in range(len(p)))


def cwm_step(states, matrix):
    out = [CWM_ZERO] * len(states)
    for i, state in enumerate(states):
        for j, weight in enumerate(matrix[i]):
            if weight:
                out[j] = cwm_recoalesce(
                    out[j], cwm_propagate(state, cwm_edge(weight)))
    return tuple(out)


def cycle(lazy):
    return tuple(tuple((F(1, 2) if lazy and i == j else
                        F(1, 4) if lazy and (i-j) % 4 in (1, 3) else
                        F(1, 2) if not lazy and (i-j) % 4 in (1, 3) else F(0))
                       for j in range(4)) for i in range(4))


def two_blocks(epsilon):
    # Two internal links of weight 1/4 and two cross-block links of epsilon.
    return tuple(tuple(F(3, 4)-epsilon if i == j else
                       F(1, 4) if j == (i ^ 1) else
                       epsilon if j == (i ^ 2) else F(0)
                       for j in range(4)) for i in range(4))


def absorbing_interval(lazy):
    # Interior sites 1,2,3; jumps from 1 to 0 or from 3 to 4 are killed.
    return tuple(tuple(F(1, 2) if lazy and i == j else
                       F(1, 4) if lazy and abs(i-j) == 1 else
                       F(1, 2) if not lazy and abs(i-j) == 1 else F(0)
                       for j in range(3)) for i in range(3))


CYCLE_BASIS = ((1, 1, 1, 1), (1, 0, -1, 0), (0, 1, 0, -1), (1, -1, 1, -1))
BLOCK_BASIS = ((1, 1, 1, 1), (1, 1, -1, -1), (1, -1, 1, -1), (1, -1, -1, 1))


def spectral_prediction(initial, basis, eigenvalues, t):
    out = [F(0)] * len(initial)
    for v, eigenvalue in zip(basis, eigenvalues):
        coefficient = sum((initial[i]*v[i] for i in range(len(v))), F(0)) / sum(x*x for x in v)
        for i in range(len(v)):
            out[i] += coefficient * eigenvalue**t * v[i]
    return tuple(out)


def tv(p, target):
    return sum((abs(a-b) for a, b in zip(p, target)), F(0)) / 2


def squared_l2(p, target):
    return sum(((a-b)**2 for a, b in zip(p, target)), F(0))


def trace(model, initial):
    matrix = model["matrix"]
    size = len(matrix)
    p = initial
    states = tuple(cwm_edge(x) if x else CWM_ZERO for x in p)
    # Independent explicit path list. It never invokes any CWM operation.
    paths = [(i, weight) for i, weight in enumerate(initial) if weight]
    values = []
    for t in range(HORIZON+1):
        for i in range(size):
            check("cwm_mass_equals_direct_recurrence", states[i].total, p[i])
            check("positive_path_realizability", is_positive_path_realizable(states[i]), True)
            check("nonnegative_endpoint_mass", p[i] >= 0, True)
        survival = sum(p, F(0))
        if model["absorbing"]:
            check("positive_survival", survival > 0, True)
            check("nonincreasing_survival", survival <= (sum(values[-1], F(0)) if t else F(1)), True)
        else:
            check("total_probability_conserved", survival, F(1))
        if t <= ENUMERATION_HORIZON:
            endpoint_weights = [[w for target, w in paths if target == i] for i in range(size)]
            for i, weights in enumerate(endpoint_weights):
                check("enumerated_path_count", states[i].count, len(weights))
                check("enumerated_path_total", states[i].total, sum(weights, F(0)))
                check("enumerated_path_dominant", states[i].dominant, max(weights, default=F(0)))
        if "basis" in model:
            prediction = spectral_prediction(initial, model["basis"], model["eigenvalues"], t)
            for actual, expected in zip(p, prediction):
                check("full_spectral_trace", actual, expected)
        values.append(p)
        if t < HORIZON:
            states = cwm_step(states, matrix)
            p = vector_step(p, matrix)
            if t < ENUMERATION_HORIZON:
                paths = [(j, weight*matrix[i][j]) for i, weight in paths
                         for j in range(size) if matrix[i][j]]
    if model["absorbing"]:
        # Characteristic-polynomial recurrence for every coordinate and start.
        coefficients = (F(0), F(1, 2), F(0)) if model["id"] == "absorbing_periodic" else (F(3, 2), F(-5, 8), F(1, 16))
        for t in range(HORIZON-2):
            for i in range(size):
                expected = sum((coefficients[k]*values[t+2-k][i] for k in range(3)), F(0))
                check("absorbing_characteristic_recurrence", values[t+3][i], expected)
    return values


def primary_observables(model, values):
    observations = []
    identifier = model["id"]
    target = tuple(F(1, len(values[0])) for _ in values[0])
    residuals = []
    survivals = []
    for t, p in enumerate(values):
        mass = sum(p, F(0))
        item = {"t": t, "endpoint_mass": p, "mass": mass}
        if not model["absorbing"]:
            residual = tv(p, target)
            l2 = squared_l2(p, target)
            item.update(tv_to_uniform=residual, squared_l2_to_uniform=l2)
            if identifier == "cycle_periodic":
                expected_tv = F(3, 4) if t == 0 else F(1, 2)
                expected_l2 = F(3, 4) if t == 0 else F(1, 4)
            elif identifier == "cycle_lazy":
                expected_tv = F(3, 4) if t == 0 else F(1, 2)**(t+1)
                expected_l2 = F(3, 4) if t == 0 else F(1, 2)**(2*t+1)
            else:
                rho = 1-2*model["epsilon"]
                expected_tv = rho**t / 2
                expected_l2 = rho**(2*t) / 4
            check("primary_tv_formula", residual, expected_tv)
            check("primary_squared_l2_formula", l2, expected_l2)
        else:
            x, y, z = p
            check("primary_absorbing_symmetry", x, z)
            raw_defect = y*y - 2*x*x
            residual = raw_defect / mass**2
            conditioned = tuple(v/mass for v in p)
            item.update(conditional_distribution=conditioned,
                        raw_quadratic_shape_defect=raw_defect,
                        conditional_quadratic_shape_defect=residual)
            if identifier == "absorbing_periodic":
                check("periodic_survival_formula", mass, F(1, 2)**(t//2))
                check("periodic_raw_shape_formula", raw_defect, F(-1, 2)**t)
                check("periodic_conditional_shape_cycle", residual, F(1) if t % 2 == 0 else F(-1, 2))
                check("periodic_conditional_distribution", conditioned,
                      (F(0), F(1), F(0)) if t % 2 == 0 else (F(1, 2), F(0), F(1, 2)))
            else:
                check("lazy_raw_shape_formula", raw_defect, F(1, 8)**t)
                check("lazy_conditional_shape_formula", residual, F(1, 8)**t/mass**2)
            survivals.append(mass)
        residuals.append(residual)
        if t in SAMPLE_TIMES:
            observations.append(item)
    if not model["absorbing"]:
        # First-order factor estimated only inside t=1..8; it predicts 9..64.
        rho_hat = residuals[2]/residuals[1]
        for t in range(1, HORIZON):
            check("frozen_scalar_factor_training" if t < TRAIN_END else "frozen_scalar_factor_holdout",
                  residuals[t+1], rho_hat*residuals[t])
        fitted = {"training_times": [1, TRAIN_END], "holdout_times": [TRAIN_END+1, HORIZON],
                  "observable": "TV to uniform", "rho_hat": rho_hat,
                  "note": "Periodic rho=1 is explicitly a no-decay result."}
    else:
        # Freeze the two-step survival recurrence s[t+2]=a*s[t+1]+b*s[t].
        s0, s1, s2, s3 = survivals[:4]
        determinant = s1*s1-s0*s2
        check("survival_fit_identifiable", determinant != 0, True)
        a = (s2*s1-s0*s3)/determinant
        b = (s1*s3-s2*s2)/determinant
        for t in range(HORIZON-1):
            check("survival_recurrence_training" if t+2 <= TRAIN_END else "survival_recurrence_holdout",
                  survivals[t+2], a*survivals[t+1]+b*survivals[t])
        fitted = {"training_times": [0, TRAIN_END], "holdout_times": [TRAIN_END+1, HORIZON],
                  "observable": "Unconditional surviving mass", "a": a, "b": b,
                  "recurrence": "s[t+2] = a*s[t+1] + b*s[t]"}
    return observations, fitted


def run():
    CHECKS.clear()
    models = [
        {"id": "cycle_periodic", "matrix": cycle(False), "absorbing": False,
         "basis": CYCLE_BASIS, "eigenvalues": (F(1), F(0), F(0), F(-1)),
         "primary": (F(1), F(0), F(0), F(0))},
        {"id": "cycle_lazy", "matrix": cycle(True), "absorbing": False,
         "basis": CYCLE_BASIS, "eigenvalues": (F(1), F(1, 2), F(1, 2), F(0)),
         "primary": (F(1), F(0), F(0), F(0))},
    ]
    for name, epsilon in (("strong_cut", F(1, 4)), ("weak_cut", F(1, 64))):
        models.append({"id": name, "matrix": two_blocks(epsilon), "absorbing": False,
                       "epsilon": epsilon, "basis": BLOCK_BASIS,
                       "eigenvalues": (F(1), 1-2*epsilon, F(1, 2), F(1, 2)-2*epsilon),
                       "primary": (F(1, 2), F(1, 2), F(0), F(0))})
    for name, lazy in (("absorbing_periodic", False), ("absorbing_lazy", True)):
        models.append({"id": name, "matrix": absorbing_interval(lazy), "absorbing": True,
                       "primary": (F(0), F(1), F(0))})
    output = []
    for model in models:
        matrix = model["matrix"]
        n = len(matrix)
        for i in range(n):
            check("matrix_row_valid", F(0) < sum(matrix[i]) <= 1, True)
            for j in range(n):
                check("matrix_nonnegative", matrix[i][j] >= 0, True)
                check("matrix_symmetric", matrix[i][j], matrix[j][i])
        if "basis" in model:
            for i, v in enumerate(model["basis"]):
                check("nonzero_spectral_basis_vector", sum(x*x for x in v) > 0, True)
                for j, w in enumerate(model["basis"]):
                    if i != j:
                        check("spectral_basis_orthogonal", sum(a*b for a, b in zip(v, w)), 0)
                image = vector_step(v, matrix)
                for actual, expected in zip(image, (model["eigenvalues"][i]*x for x in v)):
                    check("exact_eigenvector_certificate", actual, expected)
        alternate = ((F(0), F(1), F(0), F(0)) if model["id"].startswith("cycle") else
                     tuple(F(int(i == 0)) for i in range(n)))
        diverse = (F(1, 10), F(1, 5), F(3, 10), F(2, 5)) if n == 4 else (F(1, 6), F(1, 3), F(1, 2))
        starts = (model["primary"], alternate, diverse)
        traces = [trace(model, initial) for initial in starts]
        samples, fit = primary_observables(model, traces[0])
        item = {"id": model["id"], "transition_matrix": matrix,
                "initial_distributions": starts, "samples_primary": samples,
                "frozen_recurrence_fit": fit}
        if "eigenvalues" in model:
            item["full_spectrum"] = model["eigenvalues"]
        else:
            item["full_spectrum"] = (["1/sqrt(2)", "0", "-1/sqrt(2)"]
                                      if model["id"] == "absorbing_periodic" else
                                      ["(2+sqrt(2))/4", "1/2", "(2-sqrt(2))/4"])
        output.append(item)
    return {"schema": "BRC_EXPANDED_GRAPH_BOUNDARIES_V1", "researcher_id": "EM-BRCGRAPH-FCA717",
            "arithmetic": "fractions.Fraction; no floating-point assertions",
            "tool_reuse": "REUSE_EXECUTED: brc_weighted cwm_edge/cwm_propagate/cwm_recoalesce",
            "carrier_scope": "Positive rational transition/path masses; signed residual readouts are not masses.",
            "matrices": 6, "starts_per_matrix": 3, "horizon": HORIZON,
            "independent_path_enumeration_horizon": ENUMERATION_HORIZON,
            "checks_total": sum(CHECKS.values()), "checks_by_category": dict(sorted(CHECKS.items())),
            "all_checks_passed": True, "results": output}


def serialize(value):
    if isinstance(value, F):
        return str(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("graph_results.json"))
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, default=serialize, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"all_checks_passed": True, "matrices": result["matrices"],
                      "checks_total": result["checks_total"], "output": str(args.output)}))


if __name__ == "__main__":
    main()
