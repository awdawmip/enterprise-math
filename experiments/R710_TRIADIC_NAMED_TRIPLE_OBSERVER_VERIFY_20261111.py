#!/usr/bin/env python3
"""R710 exact positive BRC source event checker: four-state joint and three-state minimal triad observer."""
from itertools import permutations, product, combinations
from fractions import Fraction as F
from math import comb, factorial
import json
from pathlib import Path

def kernel(state, m):
    f, g = state
    out = {state: F(1, 2)}
    for channel in (0, 1):
        for i, j in combinations(range(m), 2):
            u, v = list(f), list(g)
            if channel == 0:
                u[i], u[j] = u[j], u[i]
            else:
                v[i], v[j] = v[j], v[i]
            target = (tuple(u), tuple(v))
            out[target] = out.get(target, F(0)) + F(1, 4 * comb(m, 2))
    assert sum(out.values(), F(0)) == 1
    return out

def test(m):
    perms = list(permutations(range(m)))
    states = list(product(perms, perms))
    alpha = F(1, 2 * m)
    beta = F(1, 2 * m * (m - 1))
    q = {
        0: {1: 2 * beta, 0: 1 - 2 * beta},
        1: {0: alpha, 2: beta, 1: 1 - alpha - beta},
        2: {1: 2 * alpha, 2: 1 - 2 * alpha}}
    class_counts = {k: 0 for k in range(3)}
    joint = {}
    for state in states:
        e = int(state[0][0] == 0)
        f = int(state[1][0] == 0)
        k = e + f
        class_counts[k] += 1
        observed = {j: F(0) for j in range(3)}
        obs4 = {(x, y): F(0) for x in (0, 1) for y in (0, 1)}
        for target, mass in kernel(state, m).items():
            E = int(target[0][0] == 0)
            G = int(target[1][0] == 0)
            observed[E + G] += mass
            obs4[(E, G)] += mass
        assert all(observed[j] == q[k].get(j, F(0)) for j in range(3))
        loss_e = alpha if e else beta
        loss_f = alpha if f else beta
        assert obs4[(e, f)] == 1 - loss_e - loss_f
        assert obs4[(1 - e, f)] == loss_e
        assert obs4[(e, 1 - f)] == loss_f
        assert obs4[(1 - e, 1 - f)] == 0
        row = tuple(str(obs4[(x, y)]) for x in (0, 1) for y in (0, 1))
        joint.setdefault((e, f), row)
        assert joint[(e, f)] == row
    assert len(states) == factorial(m) ** 2
    for k in range(3):
        expected = comb(2, k) * (m - 1) ** (2 - k) * factorial(m) ** 2 // (m * m)
        assert class_counts[k] == expected
    p = F(1, m)
    pi = {k: F(comb(2, k)) * (p ** k) * ((1 - p) ** (2 - k))
          for k in range(3)}
    assert sum(pi.values(), F(0)) == 1
    for k in range(3):
        assert sum(q[k].values(), F(0)) == 1
        for j in range(3):
            assert pi[k] * q[k].get(j, F(0)) == pi[j] * q[j].get(k, F(0))
    assert q[0].get(2, F(0)) == 0 and q[1][2] == beta
    p02_two = sum(q[0].get(j, F(0)) * q[j].get(2, F(0)) for j in range(3))
    assert p02_two == 2 * beta * beta
    return {
        "m": m, "full_states": len(states), "K_fibers": class_counts,
        "alpha": str(alpha), "beta": str(beta),
        "K_transition": {str(k): {
            str(j): str(q[k].get(j, F(0))) for j in range(3)}
            for k in range(3)},
        "stationary_K": {str(k): str(pi[k]) for k in range(3)},
        "K0_to_K2_in_two_steps": str(p02_two),
        "binary_H_not_Markov": True, "minimal_K_states": 3}

def run():
    cases = [test(m) for m in (2, 3, 4)]
    assert [(x["m"], x["full_states"]) for x in cases] == [
        (2, 4), (3, 36), (4, 576)]
    evidence = {
        "marker": "R710_THREE_STATE_NAMED_TRIAD_BRC_MINIMAL_FUTURE_OBSERVER_PASS",
        "claim": {
            "joint_EF": "four-state strongly lumpable",
            "triad_H": "two-state instantaneous H=E*F not Markov",
            "minimal_H_future": "K=E+F, exactly three predictive states",
            "alpha": "1/(2m)", "beta": "1/[2m(m-1)]",
            "transitions": "0->1:2beta;1->0:alpha;1->2:beta;2->1:2alpha",
            "stationary": "Binomial(2,1/m)", "K0_to_K2_two": "2beta**2",
            "single_update": "at most one E/F bit flips"},
        "exact_checker": {"full_source_coverage": cases, "arithmetic": "Fraction exact"},
        "scope": "R709 Cell-local positive BRC candidate; native V29/V39 pending"}
    print(evidence["marker"], [(a["m"], a["full_states"]) for a in cases])
    return evidence

if __name__ == "__main__":
    evidence = run()
    Path(__file__).with_name(
        "R710_TRIADIC_NAMED_TRIPLE_OBSERVER_EVIDENCE_20261111.json"
    ).write_text(json.dumps(evidence, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
                 encoding="utf-8")
