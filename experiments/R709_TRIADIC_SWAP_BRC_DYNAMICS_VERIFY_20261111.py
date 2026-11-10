#!/usr/bin/env python3
"""R709 exact BRC full-triad source swap and observer-fiber checker."""
import json
from itertools import permutations, combinations, product
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path

def step(state, m):
    """Full state=(f,g), each a bijection; simultaneous partner swap only."""
    f, g = state
    if m < 2:
        return {state: F(1)}
    C = comb(m, 2)
    out = {state: F(1, 2)}
    for channel in (0, 1):
        for i, j in combinations(range(m), 2):
            u, v = list(f), list(g)
            if channel == 0:
                u[i], u[j] = u[j], u[i]
            else:
                v[i], v[j] = v[j], v[i]
            target = (tuple(u), tuple(v))
            out[target] = out.get(target, F(0)) + F(1, 4 * C)
    return out

def test(m):
    perms = list(permutations(range(m)))
    states = list(product(perms, perms))
    state_set = set(states)
    assert len(states) == factorial(m) ** 2
    p11 = F(1) - F(1, 2 * m)
    p01 = F(1, 2 * m * (m - 1))
    return2 = F(1, 4) + F(1, 8 * comb(m, 2))
    e_true = [s for s in states if s[0][0] == 0]
    e_false = [s for s in states if s[0][0] != 0]
    assert len(e_true) == len(states) // m
    for state in states:
        kernel = step(state, m)
        assert sum(kernel.values(), F(0)) == 1
        assert all(target in state_set for target in kernel)
        observed = sum((w for target, w in kernel.items()
                        if target[0][0] == 0), F(0))
        assert observed == (p11 if state[0][0] == 0 else p01)
        for target, weight in kernel.items():
            assert step(target, m).get(state, F(0)) == weight
    starting = states[0]
    two = sum((w * step(t, m).get(starting, F(0))
               for t, w in step(starting, m).items()), F(0))
    assert two == return2
    return {
        "m": m, "full_state_count": len(states),
        "observer_true_fiber": len(e_true), "observer_false_fiber": len(e_false),
        "p_11": str(p11), "p_01": str(p01),
        "two_step_exact_return": str(return2)}

def run():
    details = [test(m) for m in (2, 3, 4)]
    assert [x["two_step_exact_return"] for x in details] == [
        "3/8", "7/24", "13/48"]
    output = {
        "marker": "R709_TRIADIC_SWAP_BRC_KERNEL_LUMPABILITY_PASS",
        "axioms": "Cell-local labeled complete 3-axis triads, m>=2",
        "transition": "hold 1/2; each f/g-channel pair-swap 1/(4*comb(m,2))",
        "analytic": {
            "source_states": "(m!)^2", "p_11": "1-1/(2*m)",
            "p_01": "1/(2*m*(m-1))", "stationary_true": "1/m",
            "lambda": "1-1/(2*(m-1))",
            "p_true_after_n_given_true": "1/m+(1-1/m)*lambda**n",
            "p_true_after_n_given_false": "(1/m)*(1-lambda**n)",
            "two_step_full_return": "1/4+1/(8*comb(m,2))"},
        "exact_checker": {
            "m_values": [2, 3, 4], "details": details,
            "arithmetic": "Fraction exact",
            "checks": "normalization, full-source preservation, detailed balance, observer-fiber constancy and 2-step return"},
        "scope": "Positive BRC source-counting candidate kernel; no native V29/V39 update or heartbeat timing"}
    print(output["marker"], details)
    return output

if __name__ == "__main__":
    output = run()
    Path(__file__).with_name(
        "R709_TRIADIC_SWAP_BRC_EVIDENCE_20261111.json"
    ).write_text(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                 encoding="utf-8")
