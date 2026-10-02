#!/usr/bin/env python3
"""Exact replay of the OLD cR oscillators with native X6 path innovations.

X is the integer native Cell displacement; Z is a rational six-component
response field on the SAME path. A*Z is never called a primitive Cell move.
Y=U*Z has precisely the old four-direction innovation law. Full path counts
are enriched by the lift even though the Y probability law is unchanged.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "src"))
from enterprise_math.brc_transport import (  # noqa: E402
    Affine, EffectHistogram, MomentState, eye, ma, mm, mv, sm, transpose,
)
from enterprise_math.brc_weighted import (  # noqa: E402
    CWM_ZERO, cwm_edge, cwm_propagate, cwm_recoalesce,
)

HORIZON = 128                 # Same horizon as the original rotating_modes.
EXPLICIT_HORIZON = 3          # Full joint (X,Z), not only response marginals.
SAMPLE_TIMES = (1, 2, 3, 4, 8, 16, 32, 64, 128)
OLD_PATH = ROOT / "experiments/brc_expanded_types_20261002_fca717/dynamics_types.py"
R = ((F(3, 5), F(-4, 5)), (F(4, 5), F(3, 5)))
U = tuple(tuple(F(int(i == j % 2)) for j in range(6)) for i in range(2))
O = tuple(tuple(R[i % 2][j % 2] if i // 2 == j // 2 else F(0)
                for j in range(6)) for i in range(6))
E = sm(F(1, 3), mm(transpose(U), U))
K = ma(eye(6), sm(-1, E))
ZERO6 = (F(0),) * 6
ZERO2 = (F(0),) * 2
NOISE = tuple(tuple(F(sign if i == axis else 0) for i in range(6))
              for axis in range(6) for sign in (-1, 1))
OLD_NOISE = tuple(sorted(set(mv(U, x) for x in NOISE)))
CHECKS: Counter[str] = Counter()


def check(category, actual, expected):
    CHECKS[category] += 1
    if actual != expected:
        raise AssertionError((category, actual, expected))


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def norm2(x):
    return sum((a*a for a in x), F(0))


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def outer(x):
    return tuple(tuple(a*b for b in x) for a in x)


def mean_covariance(state):
    m = state.to_matrix()
    n = state.dimension
    check("moment_total_mass", m[n][n], F(1))
    mean = tuple(m[i][n] for i in range(n))
    covariance = tuple(tuple(m[i][j]-mean[i]*mean[j] for j in range(n)) for i in range(n))
    return mean, covariance


def observations(law, component):
    size = len(component(next(iter(law))))
    m = [F(0)]*size
    covariance = sm(0, eye(size))
    radial4 = F(0)
    for key, state in law.items():
        point = component(key)
        for i in range(size):
            m[i] += state.total*point[i]
        covariance = ma(covariance, sm(state.total, outer(point)))
        radial4 += state.total*norm2(point)**2
    check("explicit_zero_mean", tuple(m), (F(0),)*size)
    return covariance, radial4


def joint_step(law, a):
    out = {}
    for (x, z), state in law.items():
        response = mv(a, z)
        for noise in NOISE:
            target = (add(x, noise), add(response, noise))
            out[target] = cwm_recoalesce(
                out.get(target, CWM_ZERO), cwm_propagate(state, cwm_edge(F(1, 12))))
    return out


def old_step(law, a):
    out = {}
    for y, state in law.items():
        response = mv(a, y)
        for noise in OLD_NOISE:
            target = add(response, noise)
            out[target] = cwm_recoalesce(
                out.get(target, CWM_ZERO), cwm_propagate(state, cwm_edge(F(1, 4))))
    return out


def explicit_checks(joint, old, a, powers, n, expected_cov, expected_k4, old_s2, old_s4):
    # Independently enumerate complete words using the closed response sum,
    # with no CWM operations or iterative endpoint recurrence.
    counts = Counter()
    for word in product(range(12), repeat=n):
        x = ZERO6
        z = ZERO6
        for t, label in enumerate(word):
            x = add(x, NOISE[label])
            z = add(z, mv(powers[n-1-t], NOISE[label]))
        counts[(x, z)] += 1
    check("independent_joint_support", set(joint), set(counts))
    check("native_word_count", sum(counts.values()), 12**n)
    for (x, z), count in counts.items():
        state = joint[(x, z)]
        check("native_X_is_integer", all(q.denominator == 1 for q in x), True)
        check("joint_CWM_count", state.count, count)
        check("joint_CWM_total", state.total, F(count, 12**n))
        check("joint_CWM_dominant", state.dominant, F(1, 12**n))
    projected = {}
    for (_, z), state in joint.items():
        y = mv(U, z)
        projected[y] = cwm_recoalesce(projected.get(y, CWM_ZERO), state)
    check("old_law_support", set(projected), set(old))
    for y, old_state in old.items():
        check("old_law_mass_preserved", projected[y].total, old_state.total)
        check("old_law_count_refinement", projected[y].count, old_state.count*3**n)
        check("old_law_dominant_refinement", projected[y].dominant, old_state.dominant/3**n)
    native_cov, native_fourth = observations(joint, lambda key: key[0])
    response_cov, response_fourth = observations(joint, lambda key: key[1])
    old_cov, old_fourth = observations(old, lambda key: key)
    check("explicit_native_covariance", native_cov, sm(F(n, 6), eye(6)))
    check("explicit_native_fourth_moment", native_fourth, F(4*n*n-n, 3))
    check("explicit_response_covariance", response_cov, expected_cov)
    check("explicit_full_fourth_cumulant", response_fourth-trace(response_cov)**2-2*trace(mm(response_cov, response_cov)), expected_k4)
    check("explicit_old_covariance", old_cov, sm(old_s2/2, eye(2)))
    check("explicit_old_fourth_cumulant", old_fourth-2*old_s2**2, -old_s4)
    cross = tuple(tuple(sum((s.total*x[i]*z[j] for (x, z), s in joint.items()), F(0))
                        for j in range(6)) for i in range(6))
    cross_expected = sm(F(1, 6), transpose(
        tuple(tuple(sum((p[i][j] for p in powers[:n]), F(0)) for j in range(6)) for i in range(6))))
    check("joint_native_response_cross_covariance", cross, cross_expected)
    return {"t": n, "joint_endpoints": len(joint), "old_endpoints": len(old),
            "word_count": 12**n, "fiber_refinement": 3**n,
            "native_response_cross_covariance": cross}


def old_results():
    spec = importlib.util.spec_from_file_location("old_brc_dynamics", OLD_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    result = module.rotating_modes()  # Execute the original code, unchanged.
    return {case["c"]: {row["n"]: row for row in case["rows"]} for case in result["cases"]}


def run_case(identifier, c, hidden_gain, base, previous):
    a = sm(c, O) if base else ma(sm(c, mm(O, E)), sm(hidden_gain, K))
    old_a = sm(c, R)
    check("intertwining_UA_equals_cRU", mm(U, a), mm(old_a, U))
    packet = EffectHistogram.from_terms(6, [(F(1, 12), Affine(a, xi), 1) for xi in NOISE])
    old_packet = EffectHistogram.from_terms(2, [(F(1, 4), Affine(old_a, xi), 1) for xi in OLD_NOISE])
    state = MomentState.from_point(ZERO6)
    old_state = MomentState.from_point(ZERO2)
    joint = {(ZERO6, ZERO6): cwm_edge(1)}
    old = {ZERO2: cwm_edge(1)}
    powers = [eye(6)]
    kernel_cov = sm(0, eye(6))
    kernel_k4 = F(0)
    sc2 = sc4 = sh2 = sh4 = F(0)
    rows, explicit = [], []
    for n in range(1, HORIZON+1):
        # Independent response-kernel cumulant calculation from A^j xi.
        power = powers[-1]
        transformed_cov = sm(F(1, 6), mm(power, transpose(power)))
        transformed_r4 = sum((norm2(mv(power, xi))**2 for xi in NOISE), F(0))/12
        kernel_k4 += transformed_r4-trace(transformed_cov)**2-2*trace(mm(transformed_cov, transformed_cov))
        kernel_cov = ma(kernel_cov, transformed_cov)
        powers.append(mm(a, power))
        sc2 = c*c*sc2+1
        sc4 = c**4*sc4+1
        sh2 = hidden_gain**2*sh2+1
        sh4 = hidden_gain**4*sh4+1
        expected_cov = ma(sm(sc2/6, E), sm(sh2/6, K))
        expected_k4 = -(sc4+2*sh4)/9
        state = state.then(packet)
        old_state = old_state.then(old_packet)
        mean, covariance = mean_covariance(state)
        old_mean, old_cov = mean_covariance(old_state)
        check("full_response_mean", mean, ZERO6)
        check("old_mean", old_mean, ZERO2)
        check("full_covariance_matches_formula", covariance, expected_cov)
        check("full_covariance_matches_response_sum", covariance, kernel_cov)
        check("full_cumulant_matches_response_sum", kernel_k4, expected_k4)
        check("six_to_two_covariance_pushforward", mm(mm(U, covariance), transpose(U)), old_cov)
        check("old_covariance_matches_formula", old_cov, sm(sc2/2, eye(2)))
        visible = trace(mm(E, covariance))
        hidden = trace(mm(K, covariance))
        check("visible_squared_response", visible, sc2/3)
        check("hidden_squared_response", hidden, 2*sh2/3)
        check("orthogonal_response_split", trace(covariance), visible+hidden)
        old_gamma = -sc4/sc2**2
        full_gamma = expected_k4/trace(covariance)**2
        if base:
            check("base_full_trace_equals_old_trace", trace(covariance), sc2)
            check("base_normalized_cumulant_ratio", full_gamma, old_gamma/3)
        if n <= EXPLICIT_HORIZON:
            joint = joint_step(joint, a)
            old = old_step(old, old_a)
            explicit.append(explicit_checks(joint, old, a, powers, n, expected_cov,
                                            expected_k4, sc2, sc4))
        if n in previous[c]:
            old_row = previous[c][n]
            check("original_code_ell_squared", sc2, old_row["ell_squared"])
            check("original_code_radial_k4", -sc4, old_row["radial_k4"])
            check("original_code_gamma", old_gamma, old_row["normalized_radial_k4"])
        if n in SAMPLE_TIMES:
            rows.append({"t": n, "native_position_covariance_coefficient_I6": F(n, 6),
                         "native_position_squared_displacement": n,
                         "native_position_k4": F(-n, 3), "native_position_gamma": F(-1, 3*n),
                         "old_Y_squared_response": sc2, "old_Y_k4": -sc4, "old_Y_gamma": old_gamma,
                         "full_Z_squared_response": trace(covariance), "full_Z_k4": expected_k4,
                         "full_Z_gamma": full_gamma, "visible_E_Z_squared_response": visible,
                         "hidden_K_Z_squared_response": hidden,
                         "full_covariance_coefficient_E": sc2/6,
                         "full_covariance_coefficient_K": sh2/6})
    return {"id": identifier, "c": c, "hidden_gain": hidden_gain,
            "response_matrix_A": a, "native_kernel": "+/-E_i, all 12 primitive directions, each 1/12",
            "initial_X": ZERO6, "initial_Z": ZERO6, "fitted_parameters_changed": False,
            "explicit_joint_checks": explicit, "rows": rows,
            "covariance_storage": "Exact complete 6x6 covariance = coefficient_E*E + coefficient_K*K; both matrices stored in constants."}


def run():
    CHECKS.clear()
    check("orthogonal_lift", mm(O, transpose(O)), eye(6))
    check("rotation_intertwining", mm(U, O), mm(R, U))
    check("observer_gram", mm(U, transpose(U)), sm(3, eye(2)))
    check("visible_projector", mm(E, E), E)
    check("hidden_projector", mm(K, K), K)
    check("orthogonal_projectors", mm(E, K), sm(0, eye(6)))
    check("hidden_not_visible", mm(U, K), tuple((F(0),)*6 for _ in range(2)))
    check("noise_pushforward_multiplicity", Counter(mv(U, xi) for xi in NOISE), Counter({eta: 3 for eta in OLD_NOISE}))
    previous = old_results()
    cases = [run_case(f"original_c_{c}_block_rotation", c, c, True, previous)
             for c in (F(3, 4), F(1), F(4, 3))]
    cases += [run_case(f"same_old_c_3_4_hidden_gain_{nu}", F(3, 4), nu, False, previous)
              for nu in (F(1), F(3, 2))]
    old_damped = cases[0]["rows"]
    for case in cases[3:]:
        for original, modified in zip(old_damped, case["rows"]):
            for key in ("old_Y_squared_response", "old_Y_k4", "old_Y_gamma"):
                check("nonidentifiable_hidden_kernel_same_old_observables", modified[key], original[key])
        check("hidden_kernel_changes_full_response", case["rows"][-1]["full_Z_squared_response"] != old_damped[-1]["full_Z_squared_response"], True)
    return {"schema": "BRC_NATIVE_X6_OSCILLATION_REPLAY_V1", "researcher_id": "EM-BRCGRAPH-FCA717",
            "arithmetic": "fractions.Fraction; no floating-point assertions",
            "horizon": HORIZON, "explicit_joint_horizon": EXPLICIT_HORIZON,
            "old_source_path": str(OLD_PATH.relative_to(ROOT)),
            "old_source_sha256": hashlib.sha256(OLD_PATH.read_bytes()).hexdigest(),
            "source_sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in (Path(__file__), ROOT/"src/enterprise_math/brc_transport.py", ROOT/"src/enterprise_math/brc_weighted.py")},
            "constants": {"R": R, "U": U, "O": O, "E": E, "K": K, "primitive_noise": NOISE},
            "typing": "X in Z^6 is native position; Z in Q^6 is response, not Cell position/address; Y=UZ is the old response.",
            "tool_reuse": "REUSE_EXECUTED: Affine/EffectHistogram/MomentState and positive CWM; original rotating_modes executed unchanged.",
            "metric": "Declared response squared norm sum(Z_i^2), not native spatial distance of rational response values.",
            "checks_total": sum(CHECKS.values()), "checks_by_category": dict(sorted(CHECKS.items())),
            "all_checks_passed": True, "cases": cases}


def serialize(value):
    if isinstance(value, F):
        return str(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE/"oscillation_results.json")
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, default=serialize, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"all_checks_passed": True, "checks_total": result["checks_total"],
                      "cases": len(result["cases"]), "output": str(args.output)}))


if __name__ == "__main__":
    main()
