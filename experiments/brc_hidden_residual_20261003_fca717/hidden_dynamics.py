#!/usr/bin/env python3
"""Hidden residual laws on retained native X6 paths; exact old-law replay.

Native X always takes one +/-E_i step. Window displacement, integrated response,
and oscillator response have separate types. Projection residuals are rational
readouts, not extra native axes or final Cell addresses.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import importlib.util
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

N = 128
SHORT = 3
SAMPLES = {1, 2, 3, 4, 8, 16, 32, 64, 128}
ZERO = (F(0),)*6
ONES = (F(1),)*6
P5 = tuple(tuple(F(i == j)-F(1, 6) for j in range(6)) for i in range(6))
NOISE = tuple(tuple(F(sign if i == axis else 0) for i in range(6))
              for axis in range(6) for sign in (-1, 1))
OLD_DIR = ROOT / "experiments/brc_expanded_types_20261002_fca717"
REPLAY_DIR = ROOT / "experiments/brc_x6_replay_20261002_fca717"
CHECKS = Counter()


def check(category, actual, expected):
    CHECKS[category] += 1
    if actual != expected:
        raise AssertionError((category, actual, expected))


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(result)
    return result


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def norm2(x):
    return sum((a*a for a in x), F(0))


def tr(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def outer(a, b):
    return tuple(tuple(x*y for y in b) for x in a)


def mass_step(law, innovations, transition):
    out = {}
    for state, weight in law.items():
        for innovation, probability in innovations:
            target = transition(state, innovation)
            out[target] = cwm_recoalesce(out.get(target, CWM_ZERO),
                                       cwm_propagate(weight, cwm_edge(probability)))
    return out


def check_pushforward(native, old, projection, n):
    reduced = {}
    for (x, auxiliary), state in native.items():
        check("native_X_integer", all(v.denominator == 1 for v in x), True)
        target = projection((x, auxiliary))
        reduced[target] = cwm_recoalesce(reduced.get(target, CWM_ZERO), state)
    check("exact_old_joint_support", set(reduced), set(old))
    check("native_probability_one", sum((w.total for w in native.values()), F(0)), F(1))
    for target, state in old.items():
        check("exact_old_joint_mass", reduced[target].total, state.total)
        check("old_CWM_count_refinement", reduced[target].count, state.count*6**n)
        check("old_CWM_dominant_refinement", reduced[target].dominant, state.dominant/6**n)


def statistics(law, readout):
    hidden_cov = sm(0, eye(6))
    eh2 = eh4 = ev2 = ev2h2 = mixed = F(0)
    hmean = [F(0)]*6
    vmean = None
    for key, state in law.items():
        visible, hidden = readout(key)
        if vmean is None:
            vmean = [F(0)]*len(visible)
        p = state.total
        v2, h2 = norm2(visible), norm2(hidden)
        eh2 += p*h2
        eh4 += p*h2*h2
        ev2 += p*v2
        ev2h2 += p*v2*h2
        mixed += p*visible[0]*hidden[0]**3
        hidden_cov = ma(hidden_cov, sm(p, outer(hidden, hidden)))
        for i in range(6):
            hmean[i] += p*hidden[i]
        for i in range(len(visible)):
            vmean[i] += p*visible[i]
    check("explicit_hidden_centered", tuple(hmean), ZERO)
    check("explicit_visible_centered", tuple(vmean), (F(0),)*len(vmean))
    return {"hidden_covariance": hidden_cov, "hidden_squared_norm": eh2,
            "hidden_kappa4_radial": eh4-eh2**2-2*tr(mm(hidden_cov, hidden_cov)),
            "visible_squared_norm": ev2, "squared_norm_covariance": ev2h2-ev2*eh2,
            "mixed_visible0_hidden0_cubed": mixed}


def p5_row(n, s2, s4):
    return {"n": n, "hidden_covariance_coefficient_P5": s2/6,
            "hidden_squared_norm": 5*s2/6, "hidden_kappa4_radial": -5*s4/18,
            "hidden_gamma4": None if not s2 else -F(2, 5)*s4/s2**2,
            "squared_norm_covariance": F(0),
            "mixed_visible0_hidden0_cubed": 5*s4/54}


def check_direct(stats, row, projector=P5):
    check("explicit_full_hidden_covariance", stats["hidden_covariance"],
          sm(row["hidden_covariance_coefficient_P5"], projector))
    for key in ("hidden_squared_norm", "hidden_kappa4_radial", "squared_norm_covariance",
                "mixed_visible0_hidden0_cubed"):
        check("explicit_"+key, stats[key], row[key])


def fixed_moments(state):
    m = state.to_matrix()
    d = state.dimension
    check("tool_mass_one", m[d][d], F(1))
    check("tool_zero_mean", tuple(m[i][d] for i in range(d)), (F(0),)*d)
    return tuple(tuple(m[i][j] for j in range(d)) for i in range(d))


def windows(previous):
    packet = EffectHistogram.from_terms(6, [(F(1, 12), Affine(eye(6), xi), 1) for xi in NOISE])
    state = MomentState.from_point(ZERO)
    by_length = {}
    for m in range(1, 9):
        state = state.then(packet)
        by_length[m] = fixed_moments(state)
    outputs = []
    for length in (2, 4, 8):
        native = {(ZERO, (ZERO,)*length): cwm_edge(1)}
        old = {(F(0),)*length: cwm_edge(1)}
        rows, sizes = [], []
        for n in range(1, N+1):
            m = min(n, length)
            row = p5_row(n, F(m), F(m))
            check("window_hidden_covariance_from_tool", mm(mm(P5, by_length[m]), P5), sm(F(m, 6), P5))
            old_row = previous["windows"][str(length)]["rows"][n-1]
            check("original_window_variance", old_row["variance"], F(m))
            check("original_window_gamma", old_row["gamma4"], -F(2, m))
            check("window_hidden_gamma_is_fifth", row["hidden_gamma4"], old_row["gamma4"]/5)
            if n <= SHORT:
                native = mass_step(native, [(xi, F(1, 12)) for xi in NOISE],
                                   lambda key, xi: (add(key[0], xi), (xi,)+key[1][:-1]))
                old = mass_step(old, [(F(s), F(1, 2)) for s in (-1, 1)],
                                lambda queue, s: (s,)+queue[:-1])
                check_pushforward(native, old, lambda key: tuple(sum(xi, F(0)) for xi in key[1]), n)
                def readout(key):
                    z = tuple(sum((xi[i] for xi in key[1]), F(0)) for i in range(6))
                    return (sum(z, F(0)),), mv(P5, z)
                check_direct(statistics(native, readout), row)
                sizes.append({"n": n, "native_joint_endpoints": len(native), "old_queue_endpoints": len(old)})
            if n in SAMPLES:
                rows.append(row)
        outputs.append({"length": length, "hidden_type": "P5 * sum(last L native increments), with zero padding",
                        "future_state": "Retain full native X and the ordered length-L native increment queue; window sum alone is not a streaming state.",
                        "stationary_hidden_gamma": -F(2, 5*length),
                        "stationary_lag_covariance": "Cov(H_t,H_(t+k)) = max(L-k,0)*P5/6 for t>=L,k>=0",
                        "rows": rows, "explicit_sizes": sizes})
    # Independent full 12^3 word check of lagged quadratic correlation.
    for length in (2, 4, 8):
        observed = F(0)
        for a in NOISE:
            for b in NOISE:
                for c in NOISE:
                    later = add(b, c) if length == 2 else add(add(a, b), c)
                    observed += sum((x*y for x, y in zip(mv(P5, a), mv(P5, later))), F(0))/12**3
        check("independent_window_lag_trace", observed, F(0) if length == 2 else F(5, 6))
    return outputs


def integrated(previous):
    # State order is (native X, response Q); Q uses the OLD X before its update.
    a = tuple(tuple(F((i < 6 and i == j) or (i >= 6 and (i == j or i-6 == j)))
                    for j in range(12)) for i in range(12))
    packet = EffectHistogram.from_terms(12, [(F(1, 12), Affine(a, xi+ZERO), 1) for xi in NOISE])
    state = MomentState.from_point(ZERO+ZERO)
    native = {(ZERO, ZERO): cwm_edge(1)}
    old = {(F(0), F(0)): cwm_edge(1)}  # (old x, old v).
    old_rows = {row["n"]: row for row in previous["rows"]}
    rows, sizes = [], []
    for n in range(1, N+1):
        state = state.then(packet)
        cov = fixed_moments(state)
        s1 = F(n*(n-1), 2)
        s2 = F(n*(n-1)*(2*n-1), 6)
        s4 = F((n-1)*n*(2*n-1)*(3*n*n-3*n-1), 30)
        row = p5_row(n, s2, s4)
        for i in range(6):
            for j in range(6):
                check("integrated_joint_XX", cov[i][j], F(n, 6)*int(i == j))
                check("integrated_joint_XQ", cov[i][6+j], s1/6*int(i == j))
                check("integrated_joint_QQ", cov[6+i][6+j], s2/6*int(i == j))
        if n in old_rows:
            check("original_integrated_variance", old_rows[n]["position_variance"], s2)
            check("original_integrated_velocity", old_rows[n]["velocity_variance"], n)
            check("original_integrated_k4", old_rows[n]["k4"], -2*s4)
            check("original_integrated_gamma", old_rows[n]["gamma4"], None if not s2 else -2*s4/s2**2)
        if n <= SHORT:
            native = mass_step(native, [(xi, F(1, 12)) for xi in NOISE],
                               lambda key, xi: (add(key[0], xi), add(key[1], key[0])))
            old = mass_step(old, [(F(s), F(1, 2)) for s in (-1, 1)],
                            lambda key, s: (key[0]+key[1], key[1]+s))
            check_pushforward(native, old, lambda key: (sum(key[1], F(0)), sum(key[0], F(0))), n)
            check_direct(statistics(native, lambda key: ((sum(key[1], F(0)),), mv(P5, key[1]))), row)
            sizes.append({"n": n, "native_joint_endpoints": len(native), "old_joint_endpoints": len(old)})
        if n in SAMPLES:
            row.update(hidden_position_velocity_covariance_coefficient_P5=s1/6,
                       native_hidden_velocity_covariance_coefficient_P5=F(n, 6))
            rows.append(row)
    return {"hidden_type": "P5 Q where Q_(t+1)=Q_t+X_t; native X_(t+1)=X_t+xi_t",
            "old_readout": "(old x,old v) = (sum Q,sum X), preserving the complete old two-variable law",
            "asymptotic_hidden_squared_norm": "5*t^3/18",
            "asymptotic_hidden_gamma": "-18/(25*t), equivalently constant*hidden_RMS^(-2/3)",
            "rows": rows, "explicit_sizes": sizes}


def multiplicative(previous):
    native = {(ZERO, F(1)): cwm_edge(1)}
    old = {F(1): cwm_edge(1)}
    packet = EffectHistogram.from_terms(6, [(F(1, 12), Affine(eye(6), xi), 1) for xi in NOISE])
    state = MomentState.from_point(ZERO)
    old_rows = {row["n"]: row for row in previous["rows"]}
    rows, sizes = [], []
    for n in range(1, N+1):
        state = state.then(packet)
        cov = fixed_moments(state)
        row = p5_row(n, F(n), F(n))
        # Visible value is now the CENTERED multiplicative response, not sum X.
        row["mixed_visible0_hidden0_cubed"] = F(5*n, 216)
        check("multiplicative_native_hidden_covariance", mm(mm(P5, cov), P5), sm(F(n, 6), P5))
        if n in old_rows:
            check("original_multiplicative_mean", old_rows[n]["mean"], F(1))
            check("original_multiplicative_variance", old_rows[n]["variance"], F(17, 16)**n-1)
        if n <= SHORT:
            native = mass_step(native, [(xi, F(1, 12)) for xi in NOISE],
                               lambda key, xi: (add(key[0], xi), key[1]*(1+sum(xi, F(0))/4)))
            old = mass_step(old, [(F(3, 4), F(1, 2)), (F(5, 4), F(1, 2))], lambda y, factor: y*factor)
            check_pushforward(native, old, lambda key: key[1], n)
            for x, y in native:
                s = sum(x, F(0))
                plus = int((n+s)/2)
                minus = n-plus
                check("multiplicative_endpoint_sign_identity", y, F(5, 4)**plus*F(3, 4)**minus)
            check_direct(statistics(native, lambda key: ((key[1]-1,), mv(P5, key[0]))), row)
            sizes.append({"n": n, "native_joint_endpoints": len(native), "old_scalar_endpoints": len(old)})
        if n in SAMPLES:
            row.update(old_response_mean=F(1), old_response_variance=F(17, 16)**n-1,
                       old_response_gamma4=old_rows[n]["gamma4"])
            rows.append(row)
    return {"hidden_type": "P5 X, native spatial displacement hidden by the old multiplicative response",
            "old_bridge": "Y_t=(5/4)^((t+sum X_t)/2)*(3/4)^((t-sum X_t)/2); fixed t gives an injective map of sum X_t",
            "old_response_gamma_asymptotic": "(353/289)^t",
            "hidden_gamma": "-2/(5*t)",
            "response_kernel_choice": "Only the native axis routing is chosen; no arbitrary multiplicative law is imposed on hidden coordinates.",
            "rows": rows, "explicit_sizes": sizes}


def oscillators(replay, previous):
    # Do NOT rerun the old 5 x 128 moment/replay suite. Reuse its exact results.
    u, p4 = replay.U, replay.K
    outputs = []
    for saved in previous["cases"]:
        c, nu = F(saved["c"]), F(saved["hidden_gain"])
        a = tuple(tuple(F(q) for q in row) for row in saved["response_matrix_A"])
        saved_rows = {row["t"]: row for row in saved["rows"]}
        power = eye(6)
        mixed = F(0)
        native = {(ZERO, ZERO): cwm_edge(1)}
        s2 = s4 = F(0)
        rows = []
        for n in range(1, N+1):
            # New mixed fourth statistic from independent response-kernel terms.
            one_mixed = one_v2 = one_h2 = one_v2h2 = F(0)
            cross = tuple((F(0),)*6 for _ in range(2))
            for xi in NOISE:
                z = mv(power, xi)
                v, h = mv(u, z), mv(p4, z)
                one_mixed += v[0]*h[0]**3/12
                one_v2 += norm2(v)/12
                one_h2 += norm2(h)/12
                one_v2h2 += norm2(v)*norm2(h)/12
                cross = ma(cross, sm(F(1, 12), outer(v, h)))
            check("oscillator_each_innovation_cross_covariance", cross, tuple((F(0),)*6 for _ in range(2)))
            check("oscillator_each_innovation_square_cumulant", one_v2h2-one_v2*one_h2, F(0))
            mixed += one_mixed
            power = mm(a, power)
            s2 = nu*nu*s2+1
            s4 = nu**4*s4+1
            row = {"n": n, "hidden_covariance_coefficient_P4": s2/6,
                   "hidden_squared_norm": 2*s2/3, "hidden_kappa4_radial": -2*s4/9,
                   "hidden_gamma4": -s4/(2*s2**2), "squared_norm_covariance": F(0),
                   "mixed_visible0_hidden0_cubed": mixed}
            if n in saved_rows:
                old = saved_rows[n]
                check("reuse_saved_hidden_covariance", F(old["full_covariance_coefficient_K"]), s2/6)
                check("reuse_saved_hidden_squared_norm", F(old["hidden_K_Z_squared_response"]), 2*s2/3)
                check("reuse_saved_hidden_fourth_reconstruction",
                      (-9*F(old["full_Z_k4"])+F(old["old_Y_k4"]))/2, s4)
            if n <= SHORT:
                native = replay.joint_step(native, a)
                stats = statistics(native, lambda key: (mv(u, key[1]), mv(p4, key[1])))
                check("oscillator_explicit_hidden_covariance", stats["hidden_covariance"], sm(s2/6, p4))
                for key in ("hidden_squared_norm", "hidden_kappa4_radial", "squared_norm_covariance",
                            "mixed_visible0_hidden0_cubed"):
                    check("oscillator_explicit_"+key, stats[key], row[key])
            if n == 1:
                check("oscillator_nonindependence_witness", mixed, F(1, 27))
            if n in SAMPLES:
                rows.append(row)
        # New temporal covariance, independently summed over all 12^3 words.
        lag_cov = sm(0, eye(6))
        a2 = mm(a, a)
        for xi0 in NOISE:
            early = mv(p4, xi0)
            first = mv(a2, xi0)
            for xi1 in NOISE:
                second = add(first, mv(a, xi1))
                for xi2 in NOISE:
                    later = mv(p4, add(second, xi2))
                    lag_cov = ma(lag_cov, sm(F(1, 12**3), outer(early, later)))
        check("independent_oscillator_lag_covariance", lag_cov,
              sm(F(1, 6), mm(p4, transpose(a2))))
        outputs.append({"id": saved["id"], "c": c, "hidden_gain": nu,
                        "hidden_type": "P4 Z; Z is the old replay response field, not Cell position",
                        "lag_covariance_formula": "Cov(H_n,H_(n+k))=Cov(H_n)*(A^k)^T on the retained hidden subspace",
                        "independent_lag_covariance_1_to_3": lag_cov,
                        "rows": rows})
    return outputs


def run():
    CHECKS.clear()
    check("P5_projector", mm(P5, P5), P5)
    check("P5_trace_rank", tr(P5), F(5))
    check("P5_annihilates_visible_direction", mv(P5, ONES), ZERO)
    for xi in NOISE:
        check("native_primitive_direction", sum(abs(q) for q in xi), F(1))
    related = module(OLD_DIR/"related_branches.py", "old_hidden_related")
    dynamics = module(OLD_DIR/"dynamics_types.py", "old_hidden_dynamics")
    replay = module(REPLAY_DIR/"oscillation_replay.py", "existing_oscillation_replay")
    saved = json.loads((REPLAY_DIR/"oscillation_results.json").read_text())
    result = {"schema": "BRC_HIDDEN_DYNAMICS_V1", "researcher_id": "EM-BRCGRAPH-FCA717",
              "fixed_native_semantics": "Six-dimensional native X6 is the solid world; time separate; three-dimensional crystal layers are not defined by these projectors.",
              "horizon": N, "independent_full_distribution_horizon": SHORT,
              "arithmetic": "fractions.Fraction only",
              "P5": P5, "P4": replay.K,
              "windows": windows(related.finite_windows()),
              "integrated_noise": integrated(dynamics.integrated_noise()),
              "multiplicative_noise": multiplicative(dynamics.multiplicative()),
              "reused_oscillators": oscillators(replay, saved)}
    paths = [Path(__file__), OLD_DIR/"related_branches.py", OLD_DIR/"dynamics_types.py",
             REPLAY_DIR/"oscillation_replay.py", REPLAY_DIR/"oscillation_results.json",
             ROOT/"src/enterprise_math/brc_transport.py", ROOT/"src/enterprise_math/brc_weighted.py"]
    result.update(source_sha256={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
                  checks_total=sum(CHECKS.values()), checks_by_category=dict(sorted(CHECKS.items())), all_checks_passed=True)
    return result


def serialize(x):
    if isinstance(x, F):
        return str(x)
    raise TypeError(type(x).__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE/"hidden_dynamics_results.json")
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, default=serialize, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"all_checks_passed": True, "checks_total": result["checks_total"], "output": str(args.output)}))


if __name__ == "__main__":
    main()
