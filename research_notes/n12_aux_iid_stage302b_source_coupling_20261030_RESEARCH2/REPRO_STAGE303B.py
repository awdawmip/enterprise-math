#!/usr/bin/env python3
"""Stage303-B: rational evidence for exact noise-coupled source minimax.

Run next to REPRO_STAGE302B.py using standard-library Python.
"""
from fractions import Fraction as F
from itertools import product
from REPRO_STAGE302B import P, HALF, exact_law, law_k, tv, binomial_tv_formula


def mix(left, right, rate):
    assert left.keys() == right.keys()
    return {k: (1-rate) * left[k] + rate * right[k] for k in left}


def model_risk(plan, q0, q1):
    a, b = exact_law(plan, 0), exact_law(plan, 1)
    qa = mix(a, b, q0)
    qb = mix(a, b, q1)
    epsilon = (q0 + 1-q1) / 2
    risk = (tv(a, qa) + tv(b, qb)) / 2
    assert risk == epsilon * tv(a, b)
    assert sum(qa.values()) == 1 and sum(qb.values()) == 1
    assert all(v > 0 for v in qa.values()) and all(v > 0 for v in qb.values())
    return risk


def joint_label_tv(q0, q1):
    original, coupled = {}, {}
    for s, j in product(range(2), repeat=2):
        original[s, j] = HALF if s == j else F(0)
        coupled[s, j] = HALF * (q0 if j else 1-q0) if s == 0 else HALF * (q1 if j else 1-q1)
    return tv(original, coupled)


def main():
    cases = [(F(0), F(1)), (HALF, HALF), (F(1, 8), F(7, 8)),
             (F(1, 4), F(3, 4)), (F(1), F(0)), (F(0), F(0))]
    for q0, q1 in cases:
        epsilon = (q0 + 1-q1) / 2
        risk_all = []
        for plan in product(range(2), repeat=6):
            risk_all.append(model_risk(plan, q0, q1))
        assert len(risk_all) == 64
        assert max(risk_all) == epsilon / 2  # TV two-F=1/2
        assert joint_label_tv(q0, q1) == epsilon
        for n in range(1, 8):
            a, b = law_k(0, n), law_k(1, n)
            qa, qb = mix(a, b, q0), mix(a, b, q1)
            risk = (tv(a, qa) + tv(b, qb)) / 2
            assert risk == epsilon * binomial_tv_formula(n)
        print(f'q0={q0}; q1={q1}; Pr(J!=S)={epsilon}; n2_risk={max(risk_all)}; joint_label_TV={joint_label_tv(q0,q1)}')
    assert binomial_tv_formula(7) == F(1759, 2048)
    print('couplings=6; adaptive_policies_per_case=64; all_F_horizons=1..7')
    print('STAGE303B_NOISY_COUPLING_EXACT_PASS')


if __name__ == '__main__':
    main()
