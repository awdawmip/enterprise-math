#!/usr/bin/env python3
"""Exact labelled-path BRC checks for PREFIX-324 (standard library only).

Scope: static auxiliary complex three-source / five-Port register; not X6 dynamics.
The universal planar geometry is proved in the companion paper, not inferred
from the finite witness below.
"""
from fractions import Fraction as F
import json
from pathlib import Path


def z(x=0, y=0):
    return (F(x), F(y))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def conj(a):
    return (a[0], -a[1])


def div(a, k):
    return (a[0] / k, a[1] / k)


def norm2(a):
    return mul(a, conj(a))[0]


def s(a):
    return [str(a[0]), str(a[1])]


A = [
    [z(4), z(4), z()],
    [z(), z(-4), z(4)],
    [z(-5, 3), z(), z(-3, 1)],
    [z(-2, -2), z(4, 4), z(2, 2)],
    [z(-2), z(), z(5, 2)],
]
b0 = [z(-2), z(0, -2), z(1)]
b2 = [z(0, 2), z(2), z(0, -1)]
t0, t2 = div(z(-7, 3), 14), div(z(-7, -3), 14)


def scaled_state(t, b):
    return [mul(t, x) for x in b]


def paths(port, state, reference):
    ans = [(f"source:{k+1}", div(mul(A[port][k], state[k]), 8)) for k in range(3)]
    if reference == "one":
        ans.append(("reference:one", z(1)))
    elif reference == "imag":
        ans.append(("reference:imag", z(0, 1)))
    else:
        assert reference == "none"
    return ans


stats = {"positive_mass_computations": 0, "ordered_labelled_pair_terms": 0}


def brc_mass(labelled_paths):
    # Every ordered pair is accounted for BEFORE any Port-level compression.
    total = z()
    for p_label, p in labelled_paths:
        for q_label, q in labelled_paths:
            assert p_label and q_label
            total = add(total, mul(p, conj(q)))
            stats["ordered_labelled_pair_terms"] += 1
    assert total[1] == 0 and total[0] >= 0
    stats["positive_mass_computations"] += 1
    return total[0]


def brc_observations(state):
    return {kind: [brc_mass(paths(j, state, kind)) for j in range(5)]
            for kind in ("none", "one", "imag")}


def output(port, b):
    ans = z()
    for k in range(3):
        ans = add(ans, div(mul(A[port][k], b[k]), 8))
    return ans


def main():
    states = [scaled_state(t0, b0), scaled_state(t2, b2)]
    obs = [brc_observations(a) for a in states]
    assert obs[0]["none"] == obs[1]["none"]
    q0 = obs[0]["none"]
    reports = {}
    for kind in ("one", "imag"):
        reports[kind] = [(obs[0][kind][j] + obs[1][kind][j]) / 2 for j in range(5)]
        for k in range(2):
            assert all(abs(obs[k][kind][j] - reports[kind][j]) <= 1 for j in range(5))
    for k, a in enumerate(states):
        for j in range(5):
            amp = output(j, a)
            assert obs[k]["none"][j] == norm2(amp)
            assert obs[k]["one"][j] == norm2(amp) + 1 + 2 * amp[0]
            assert obs[k]["imag"][j] == norm2(amp) + 1 + 2 * amp[1]

    c4, d4 = output(3, b0), output(3, b2)
    assert c4 == z(F(7, 4), F(-1, 4))
    assert d4 == z(F(7, 4), F(1, 4))
    assert norm2(c4) == norm2(d4) == F(25, 8)
    row4norm2 = sum(norm2(div(x, 8)) for x in A[3])
    assert row4norm2 == F(3, 4)
    r2 = norm2(t0)
    assert r2 == norm2(t2) == F(29, 98)
    assert sum(norm2(x) for x in states[0]) == sum(norm2(x) for x in states[1]) == 9*r2
    # Port4 actual amplitude square has coordinate spans at most 1.
    port4_values = [output(3, x) for x in states]
    assert abs(port4_values[0][0] - port4_values[1][0]) <= 1
    assert abs(port4_values[0][1] - port4_values[1][1]) <= 1

    threshold = F(16, 75)  # R_port4^2 > 2/3 iff r^2 > 16/75
    low_scale_bound = 9 * threshold
    high_scale_bound = F(29, 6) * r2 + F(2, 3)
    L = F(1062562, 458329)
    assert low_scale_bound == F(48, 25)
    assert high_scale_bound == F(411, 196)
    assert high_scale_bound > low_scale_bound
    assert L > high_scale_bound
    assert L - high_scale_bound == F(19888933, 89832484)
    # Published PREFIX-321 witness is a concrete nonempty mixed observation fiber.
    distance2 = sum(norm2(add(states[0][k], mul(z(-1), states[1][k]))) for k in range(3))
    assert distance2 == F(240, 49)
    assert distance2 / 4 == F(60, 49)
    assert stats == {"positive_mass_computations": 30, "ordered_labelled_pair_terms": 410}

    result = {
        "schema": "PREFIX324_EXACT_AUXILIARY_BRC_EVIDENCE_V1",
        "scope": "STATIC_S7_3_TWO_SHAPE_MIXED_FIBER_ONLY; NO_NATIVE_X6_TRANSFER",
        "parent_prerequisite": "PREFIX-321 author-side full-phase critical radius r^2<=29/98",
        "model": {
            "port4_row_U": [s(div(v, 8)) for v in A[3]],
            "port4_row_norm_sq": str(row4norm2),
            "port4_shape_values": [s(c4), s(d4)],
            "port4_shape_abs_sq": str(norm2(c4)),
            "source_abs_sq_per_unit_scale": "9",
            "noise_per_each_Q1_Qi": "1",
            "inferred_real_imag_amplitude_interval_length": "1",
            "output_cloud_diameter_sq_upper": "2"
        },
        "theorem_certificate": {
            "small_scale_cut_r_sq": str(threshold),
            "small_scale_MEB_sq_bound": str(low_scale_bound),
            "large_scale_formula_MEB_sq_bound": "(29/6)*r^2+2/3",
            "critical_r_sq": str(r2),
            "uniform_mixed_MEB_sq_bound": str(high_scale_bound),
            "full_auxiliary_preexisting_lower_L": str(L),
            "strict_L_minus_uniform_bound": str(L - high_scale_bound),
            "planar_geometry_lemma": "requires proof in paper, not asserted by finite script"
        },
        "concrete_witness": {
            "t0": s(t0), "t2": s(t2),
            "baseline_Q0": [str(x) for x in q0],
            "reference_report_Q1": [str(x) for x in reports["one"]],
            "reference_report_Qi": [str(x) for x in reports["imag"]],
            "reference_differences_Q1": [str(obs[0]["one"][j]-obs[1]["one"][j]) for j in range(5)],
            "reference_differences_Qi": [str(obs[0]["imag"][j]-obs[1]["imag"][j]) for j in range(5)],
            "two_state_MEB_sq": str(distance2/4)
        },
        "actual_executed_BRC_counts": stats,
        "checks": "PASS",
        "proof_status": "AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED"
    }
    out = Path(__file__).with_name("RESULTS_PREFIX324.json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False)+"\n", encoding="utf-8")
    print("PASS PREFIX-324: 30 exact BRC masses / 410 labelled ordered pairs;")
    print("global mixed-family upper 411/196 < L, margin", L-high_scale_bound)
    print("JSON", out)


if __name__ == "__main__":
    main()
