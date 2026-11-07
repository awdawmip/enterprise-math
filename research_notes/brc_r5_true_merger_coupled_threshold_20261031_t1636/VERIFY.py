#!/usr/bin/env python3
"""Exact finite-policy certificate for the original R5 two-merger model.
All endpoints and all arithmetic use Fraction. The mathematical universal
quantifier is over real epsilon in [0,1] and independently chosen legal
common terminal labels, not a grid of numerical samples.
"""
from fractions import Fraction as F
from itertools import product

ALPHA = (F(1, 4), F(1, 8))
R = {-1: F(1, 2), 1: F(3, 2)}
MERGE_Q = {-1: F(1, 3), 1: F(1, 2)}
RESIDUAL_LR = {-1: F(1, 4), 1: F(2)}
STOP_ERR = {-1: 1, 1: 0}
LEAF_ERR = {-1: 0, 1: 1}
HISTORIES = tuple((i, j, a) for i in (0, 1) for j in (-1, 1) for a in (0, 1))
FULL_BITS = (1, 0, 0, 1, 0, 1, 1, 1, 1, 1)


def evaluate(bits, seedless):
    assert len(bits) == (4 if seedless else 10)
    first = {i: bits[0] if seedless else bits[i] for i in (0, 1)}
    second = {(i, j): bits[1 + (j == 1)] if seedless
              else bits[2 + 2*i + (j == 1)]
              for i in (0, 1) for j in (-1, 1)}
    last = {(i, j): bits[3] if seedless
            else bits[6 + 2*i + (j == 1)]
            for i in (0, 1) for j in (-1, 1)}
    obs = [F(0)] * 4  # error_P,error_Q,T_P,T_Q
    masses = [F(0), F(0)]
    occupancy = {h: F(0) for h in HISTORIES}

    def finish(q, lr, time, error):
        p = q * lr
        masses[0] += p
        masses[1] += q
        obs[0] += p * error
        obs[1] += q * error
        obs[2] += p * time
        obs[3] += q * time

    for i, alpha in enumerate(ALPHA):
        if not first[i]:
            finish(F(1, 2), F(1), 1, 0)
            continue
        for j, qj in ((-1, alpha), (0, 1-2*alpha), (1, alpha)):
            q = qj / 2
            if j == 0:
                finish(q, F(1), 2, 0)
            elif not second[i, j]:
                finish(q, R[j], 2, STOP_ERR[j])
            else:
                finish(q * (1-MERGE_Q[j]), RESIDUAL_LR[j], 3, LEAF_ERR[j])
                q_l = q * MERGE_Q[j]
                a = last[i, j]
                occupancy[i, j, a] += q_l
                finish(q_l, F(1), 3+a, a)
    assert masses == [1, 1], masses
    return tuple(obs), occupancy


def J(obs):
    return 41*obs[1] - 12*obs[3]


def adverse_mass(f, j):
    # STOP has baseline error zero, so perturbation is in [0,eps].
    # CONTINUE has baseline error one, so perturbation is in [-eps,0].
    return (sum(max(F(0), j[h]-f[h]) for h in HISTORIES if h[2] == 0) +
            sum(max(F(0), f[h]-j[h]) for h in HISTORIES if h[2] == 1))


def exact_formula(epsilon):
    assert F(0) <= epsilon <= F(1)
    return min(2-F(41, 16)*epsilon,
               (F(151)-205*epsilon)/32)


def main():
    full, q_f = evaluate(FULL_BITS, False)
    assert full == (F(1,4), F(1,4), F(7,4), F(27,16))
    assert q_f[(0, 1, 1)] == F(1,16)
    assert sum(q_f.values()) == F(1,16)
    assert J(full) == -10
    full_vectors = [evaluate(b, False)[0] for b in product((0,1), repeat=10)]
    assert len(full_vectors) == 1024
    assert max(map(J, full_vectors)) == -10
    table = []
    for b in product((0,1), repeat=4):
        v, q = evaluate(b, True)
        margin = J(full) - J(v)
        penalty = adverse_mass(q_f, q)
        table.append((b, margin, penalty))
    assert len(table) == 16
    assert min(x[1] for x in table) == 2
    assert table[0][1:] == (F(2), F(1,16))
    assert table[10][1:] == (F(151,32), F(5,32))
    assert table[11][1:] == (F(2), F(0))

    # Exact universal certificate: every affine row lies at least as high
    # as the proposed piecewise minimum on each of its two intervals.
    switch = F(29,41)
    for endpoint in (F(0), switch, F(1)):
        minimum = min(m - 41*p*endpoint for _,m,p in table)
        assert minimum == exact_formula(endpoint), (endpoint, minimum)
        for _,m,p in table:
            assert m-41*p*endpoint >= exact_formula(endpoint)
    assert F(151,205) > switch
    assert exact_formula(F(151,205)) == 0
    assert exact_formula(F(1,16)) == F(471,256)

    # Independent exact finite-vertex check of the common perturbation box.
    # The common label choice is shared by FULL and all LR policies.
    for eps in (F(0), F(1,16), switch, F(151,205), F(1)):
        worst = None
        for corners in product((0,1), repeat=8):
            delta = {h: (eps if h[2] == 0 else -eps) * corner
                     for h, corner in zip(HISTORIES, corners)}
            f = J(full) + 41*sum(q_f[h]*delta[h] for h in HISTORIES)
            l_max = max(J(evaluate(b, True)[0]) +
                        41*sum(evaluate(b, True)[1][h]*delta[h] for h in HISTORIES)
                        for b,_,_ in table)
            val = f-l_max
            worst = val if worst is None or val < worst else worst
        assert worst == exact_formula(eps), (eps, worst)

    # Lower support-gap guarantee is valid for every real legal shared
    # perturbation when epsilon < 151/205; not a claim that hulls coincide
    # when this fixed-witness certificate reaches zero.
    print('BASELINE_FULL', full, 'J', J(full))
    print('BASELINE_FULL_MAX', max(map(J, full_vectors)),
          'LR_MAX', max(J(evaluate(b, True)[0]) for b,_,_ in table))
    for bits, margin, penalty in table:
        print('LR', ''.join(map(str,bits)), 'margin', margin, 'adverse_Q_occupancy', penalty)
    print('PIECEWISE_SWITCH', switch)
    print('ROBUST_MARGIN_0_TO_SWITCH', '2 - 41*epsilon/16')
    print('ROBUST_MARGIN_SWITCH_TO_ONE', '(151 - 205*epsilon)/32')
    print('FIXED_WITNESS_ZERO_THRESHOLD', F(151,205))
    print('EPS_1_OVER_16', exact_formula(F(1,16)),
          'LINF_HULL_GAP_AT_LEAST', exact_formula(F(1,16))/53)
    print('CHECKED_FULL_POLICIES', len(full_vectors),
          'LR_POLICIES', len(table),
          'BOX_VERTICES_PER_SAMPLE', 256, 'BOX_SAMPLES', 5)
    print('PASS_EXACT_R5_COUPLED_MERGER_FIXED_WITNESS_THRESHOLD')

if __name__ == '__main__':
    main()
