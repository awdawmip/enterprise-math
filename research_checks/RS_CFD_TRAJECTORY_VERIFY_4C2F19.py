#!/usr/bin/env python3
"""Exact block-level confirmation checker for RS-CFD-TRAJECTORY-VERIFY-20260910.

Scope:
- six triplets per complete A/B/C order cycle;
- arbitrary dependence inside a cycle;
- inference compresses each gate/cycle to one predeclared cycle-majority bit;
- complete cycles are the independent inferential blocks;
- ties/nonpositive triplet deltas are not successes;
- exact binomial domination is used only when each block success probability <= 1/2;
- two-gate conjunction can use an intersection-union test (IUT) at alpha=.05 per gate;
- Bonferroni alpha=.025 per gate remains available when separate simultaneous claims are required.

This checker is finite/statistical only. It does not run spectralDNS or certify CFD/PDE behavior.
"""
from fractions import Fraction
from itertools import product
from math import comb
import json

ALPHA_GLOBAL = Fraction(1, 20)
ALPHA_BONF_PER_GATE = Fraction(1, 40)


def binom_tail(n, r, p=Fraction(1, 2)):
    return sum(Fraction(comb(n, k)) * p**k * (1-p)**(n-k)
               for k in range(r, n+1))


def critical(n, alpha):
    for r in range(n + 1):
        t = binom_tail(n, r)
        if t <= alpha:
            return r, t
    return None, None


def cycle_majority(signs):
    """Strict directional majority: >=4 strictly positive among six; zeros are non-success."""
    assert len(signs) == 6
    return int(sum(x > 0 for x in signs) >= 4)


def min_cycles_for_power(p, target, alpha, limit=500):
    for n in range(1, limit + 1):
        r, null_tail = critical(n, alpha)
        if r is None:
            continue
        power = binom_tail(n, r, p)
        if power >= target:
            return n, r, null_tail, power
    raise AssertionError("search limit too small")


def frac_record(q):
    return {"num": q.numerator, "den": q.denominator, "decimal": float(q)}


def main():
    # Under central sign reversal, majority success and reversed-majority success
    # are disjoint. Thus central sign symmetry of a six-dimensional cycle vector
    # is sufficient for P(block success)<=1/2, without within-cycle independence.
    sign_patterns = 0
    for s in product((-1, 0, 1), repeat=6):
        sign_patterns += 1
        rev = tuple(-x for x in s)
        assert cycle_majority(s) + cycle_majority(rev) <= 1
    assert sign_patterns == 3**6 == 729

    # Exact resolution floors.
    assert critical(4, ALPHA_BONF_PER_GATE) == (None, None)
    assert critical(5, ALPHA_BONF_PER_GATE) == (None, None)
    assert critical(6, ALPHA_BONF_PER_GATE) == (6, Fraction(1, 64))
    assert critical(4, ALPHA_GLOBAL) == (None, None)
    assert critical(5, ALPHA_GLOBAL) == (5, Fraction(1, 32))

    expected_minima = {
        (Fraction(7,10), Fraction(4,5), ALPHA_GLOBAL): (37, 24),
        (Fraction(7,10), Fraction(9,10), ALPHA_GLOBAL): (53, 33),
        (Fraction(4,5), Fraction(4,5), ALPHA_GLOBAL): (18, 13),
        (Fraction(4,5), Fraction(9,10), ALPHA_GLOBAL): (23, 16),
        (Fraction(9,10), Fraction(4,5), ALPHA_GLOBAL): (8, 7),
        (Fraction(9,10), Fraction(9,10), ALPHA_GLOBAL): (11, 9),
        (Fraction(7,10), Fraction(4,5), ALPHA_BONF_PER_GATE): (49, 32),
        (Fraction(7,10), Fraction(9,10), ALPHA_BONF_PER_GATE): (65, 41),
        (Fraction(4,5), Fraction(4,5), ALPHA_BONF_PER_GATE): (20, 15),
        (Fraction(4,5), Fraction(9,10), ALPHA_BONF_PER_GATE): (28, 20),
        (Fraction(9,10), Fraction(4,5), ALPHA_BONF_PER_GATE): (12, 10),
        (Fraction(9,10), Fraction(9,10), ALPHA_BONF_PER_GATE): (15, 12),
    }

    minima = []
    for key, expected in expected_minima.items():
        p, target, alpha = key
        n, r, null_tail, power = min_cycles_for_power(p, target, alpha)
        assert (n, r) == expected
        for n0 in range(1, n):
            r0, _ = critical(n0, alpha)
            if r0 is not None:
                assert binom_tail(n0, r0, p) < target
        minima.append({
            "p_block": frac_record(p),
            "target_marginal_power": frac_record(target),
            "per_gate_alpha": frac_record(alpha),
            "cycles": n,
            "critical_successes": r,
            "null_tail": frac_record(null_tail),
            "marginal_power": frac_record(power),
            "physical_triplets": 6*n,
            "arm_executions": 18*n,
            "frechet_joint_power_lower": frac_record(max(Fraction(0), 2*power-1)),
        })

    # Key p=.8 IUT design points.
    r18, t18 = critical(18, ALPHA_GLOBAL)
    p18 = binom_tail(18, r18, Fraction(4,5))
    assert (r18, t18) == (13, Fraction(1577, 32768))
    assert p18 >= Fraction(4,5)

    r23, t23 = critical(23, ALPHA_GLOBAL)
    p23 = binom_tail(23, r23, Fraction(4,5))
    assert (r23, t23) == (16, Fraction(763, 16384))
    assert p23 >= Fraction(9,10)
    assert 2*p23 - 1 >= Fraction(4,5)

    # Frozen four-cycle design cannot attain exact block alpha .05 or .025.
    assert binom_tail(4, 4) == Fraction(1, 16)
    assert Fraction(1,16) > ALPHA_GLOBAL

    cert = {
        "schema": "RS_CFD_BLOCK_CONFIRMATION_CERTIFICATE_V1",
        "task_id": "RS-CFD-TRAJECTORY-VERIFY-20260910",
        "researcher_id": "EM-CFD-VFY-BLOCK-4C2F19",
        "scope": {
            "cycle_size_triplets": 6,
            "within_cycle_dependence": "ARBITRARY",
            "block_observer": "success iff >=4 of 6 gate deltas are strictly positive; ties/nonpositive deltas are non-success",
            "cross_cycle_requirement": "independent block successes; each null block success probability <= 1/2",
            "sufficient_null_condition": "independent cycles plus central sign symmetry of each six-dimensional gate-difference vector",
            "raw_evidence_retained": True,
        },
        "exact_results": {
            "sign_reversal_patterns_checked": sign_patterns,
            "bonferroni_025_resolution_floor_cycles": 6,
            "iut_05_resolution_floor_cycles": 5,
            "frozen_four_cycle_best_tail": frac_record(Fraction(1,16)),
            "iut_p08_80pct_marginal": {
                "cycles": 18, "critical_successes": r18,
                "null_tail": frac_record(t18), "power": frac_record(p18),
                "triplets": 108, "arm_executions": 324,
            },
            "iut_p08_90pct_marginal_and_ge80pct_frechet_joint": {
                "cycles": 23, "critical_successes": r23,
                "null_tail": frac_record(t23), "power": frac_record(p23),
                "frechet_joint_lower": frac_record(2*p23-1),
                "triplets": 138, "arm_executions": 414,
            },
        },
        "power_minima": minima,
        "interpretation_boundary": [
            "IUT alpha=.05 per gate controls the strictly conjunctive global claim only; it does not provide two separately reportable simultaneous alpha=.05 claims.",
            "Block validity is not implied by six-order balance or by triplet-level marginal fairness alone.",
            "Power rows assume independent blocks and per-block alternative success probability at least p_block; cross-gate dependence is unrestricted for the Frechet lower bound.",
            "No native-host execution, CFD speedup, PDE theorem, Working Truth, or final acceptance is certified."
        ]
    }
    print(json.dumps(cert, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
