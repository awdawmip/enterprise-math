#!/usr/bin/env python3
"""Exact author-side EC48U certificate; finite auxiliary positive dual-source BRC model."""
from fractions import Fraction as F
from itertools import product
import json

def s(x):
    return str(x.numerator) + '/' + str(x.denominator)

def plus(x):
    return max(F(0), x)

def terminal_case():
    p = {'A': F(3, 4), 'B': F(1, 4)}
    q = {'A': F(1, 4), 'B': F(3, 4)}
    r = {'A': {'1': F(3, 4), '0': F(1, 4)},
         'B': {'1': F(1, 4), '0': F(3, 4)}}
    assert sum(p.values()) == sum(q.values()) == 1
    assert all(0 < v < 1 for row in r.values() for v in row.values())
    assert all(sum(row.values()) == 1 for row in r.values())
    accepted_p = sum(p[h] * r[h]['1'] for h in p)
    accepted_q = sum(q[h] * r[h]['1'] for h in q)
    assert (accepted_p, accepted_q) == (F(5, 8), F(3, 8))
    b = {h: r[h]['1'] for h in p}
    assert accepted_p == sum(p[h] * b[h] for h in p)
    assert accepted_q == sum(q[h] * b[h] for h in q)
    n_checked = 0
    for bits in product((F(0), F(1)), repeat=4):
        a = dict(zip(product(('A', 'B'), ('1', '0')), bits))
        b = {h: sum(r[h][j] * a[(h, j)] for j in ('1', '0')) for h in p}
        fine = tuple(sum(dist[h] * r[h][j] * a[(h, j)]
                         for h in p for j in ('1', '0')) for dist in (p, q))
        coarse = tuple(sum(dist[h] * b[h] for h in p) for dist in (p, q))
        assert fine == coarse
        n_checked += 1
    return {
        'strict_positive_joint_leaves': 4,
        'fine_accept_j1': [s(accepted_p), s(accepted_q)],
        'old_LR_fiber_simulation': [s(accepted_p), s(accepted_q)],
        'no_joint_LR_old_support': s(F(0)),
        'no_joint_LR_refined_support': s(F(1, 4)),
        'checked_terminal_deterministic_decoders': n_checked,
    }

def future_case():
    p_h = q_h = {'A': F(1, 2), 'B': F(1, 2)}
    r = {'A': {'1': F(3, 4), '0': F(1, 4)},
         'B': {'1': F(1, 4), '0': F(3, 4)}}
    py = {'A': {'1': F(3, 4), '0': F(1, 4)},
          'B': {'1': F(1, 2), '0': F(1, 2)}}
    qy = {'A': {'1': F(1, 4), '0': F(3, 4)},
          'B': {'1': F(1, 2), '0': F(1, 2)}}
    leaves = []
    for h, j, y in product(('A', 'B'), ('1', '0'), ('1', '0')):
        leaves.append((h, j, y, p_h[h] * r[h][j] * py[h][y],
                       q_h[h] * r[h][j] * qy[h][y]))
    assert len(leaves) == 8
    assert all(pp > 0 and qq > 0 for _, _, _, pp, qq in leaves)
    assert sum(row[3] for row in leaves) == sum(row[4] for row in leaves) == 1
    assert p_h == q_h
    assert all(p_h[h] * r[h][j] == q_h[h] * r[h][j]
               for h in p_h for j in ('1', '0'))
    alpha = sum(pp for h, j, y, pp, qq in leaves if j == '1' and pp > qq)
    beta  = sum(qq for h, j, y, pp, qq in leaves if j == '1' and pp > qq)
    p_cont = sum(pp for h, j, y, pp, qq in leaves if j == '1')
    q_cont = sum(qq for h, j, y, pp, qq in leaves if j == '1')
    tp, tq = F(2) + p_cont, F(2) + q_cont
    assert (alpha, beta, tp, tq) == (F(9, 32), F(3, 32), F(5, 2), F(5, 2))
    assert alpha-beta == F(3, 16)
    assert p_cont == q_cont == F(1, 2)
    c = F(1, 8)
    fine_centered = alpha - beta - c * (tp + tq - 4)
    assert fine_centered == F(1, 16)
    assert alpha - beta - c * (tp + tq) == -F(7, 16)
    old_centered = plus(F(1, 4) - 2 * c)
    assert old_centered == 0
    fine_opt = plus(F(3, 16) - c) + plus(F(1, 16) - c)
    assert fine_opt == fine_centered
    checked = 0
    samples = [F(k, 64) for k in range(0, 17)] + [F(1, 16), F(1, 8), F(3, 16), F(1, 4)]
    for c0 in samples:
        gain = {'1': F(3, 16), '0': F(1, 16)}
        allfine = []
        for a1, a0 in product((0, 1), repeat=2):
            allfine.append(a1 * (gain['1']-c0) + a0 * (gain['0']-c0))
        allold = [F(0), F(1, 4)-2*c0]
        assert max(allold) == plus(F(1, 4)-2*c0)
        assert max(allfine) == plus(F(3, 16)-c0) + plus(F(1, 16)-c0)
        checked += 1
    for c0 in (F(1, 32), F(1, 16), F(1, 12), F(1, 8), F(1, 6), F(3, 16), F(1, 4)):
        diff = plus(F(3, 16)-c0) + plus(F(1, 16)-c0) - plus(F(1, 4)-2*c0)
        assert (diff > 0) == (F(1, 16) < c0 < F(3, 16))
    return {
        'strict_positive_joint_leaves': len(leaves),
        'old_centered_support_at_c_1_8': s(old_centered),
        'refined_centered_support_at_c_1_8': s(fine_opt),
        'strict_gap': s(fine_opt - old_centered),
        'refined_policy_observation_vector': [s(v) for v in (alpha,beta,tp,tq)],
        'old_raw_support_at_c_1_8': s(old_centered - 4*c),
        'refined_raw_support_at_c_1_8': s(fine_opt - 4*c),
        'exact_parameter_grids': checked,
        'strict_gap_open_interval': '(1/16,3/16)',
    }

def general_fiber_tests():
    qr = [F(x) for x in (1, 2, 3, 4, 5, 6)]
    pr = [F(x) for x in (1, 2, 9, 12, 5, 6)]
    q = [x / sum(qr) for x in qr]
    p = [x / sum(pr) for x in pr]
    mu = [[F(1, 4), F(3, 4)], [F(2, 5), F(3, 5)], [F(3, 7), F(4, 7)]]
    r = [
        [F(1, 2), F(1, 3), F(1, 6)],
        [F(1, 4), F(1, 4), F(1, 2)],
        [F(1, 3), F(1, 3), F(1, 3)],
        [F(1, 5), F(2, 5), F(2, 5)],
        [F(1, 6), F(1, 3), F(1, 2)],
        [F(1, 2), F(1, 4), F(1, 4)],
    ]
    assert all(sum(row) == 1 and all(x>0 for x in row) for row in r)
    ratios = [p[i] / q[i] for i in range(6)]
    assert ratios[0] == ratios[1] == ratios[4] == ratios[5]
    assert ratios[2] == ratios[3] != ratios[0]
    checks = 0
    for seed in range(83):
        def a(m, i, rr, j):
            return F(1 + (seed + 3*m + 5*i + 7*j + (0 if rr==ratios[0] else 2)) % 11, 12)
        numer = {}
        denom = {}
        for h in range(3):
            for i in range(2):
                ix=2*h+i; rr=ratios[ix]
                for m in range(2):
                    key=(m,i,rr)
                    w=q[ix]*mu[h][m]
                    denom[key] = denom.get(key,F(0)) + w
                    numer[key] = numer.get(key,F(0)) + w*sum(r[ix][j]*a(m,i,rr,j) for j in range(3))
        b={key:numer[key]/denom[key] for key in denom}
        assert all(F(0)<=v<=F(1) for v in b.values())
        for base in (p,q):
            fine = sum(base[2*h+i]*mu[h][m]*r[2*h+i][j]*a(m,i,ratios[2*h+i],j)
                       for h in range(3) for i in range(2) for m in range(2) for j in range(3))
            old  = sum(base[2*h+i]*mu[h][m]*b[(m,i,ratios[2*h+i])]
                       for h in range(3) for i in range(2) for m in range(2))
            assert fine == old, (seed, base == p, fine, old)
        checks += 1
    return {'hidden_histories': 3, 'old_terminal_symbols': 2, 'states': 2,
            'clones_per_old_terminal': 3, 'exact_rational_policies_checked': checks,
            'two_source_acceptance_pairs_reconstructed': 2*checks,
            'LR_collisions_present': True}

if __name__ == '__main__':
    report = {'schema': 'EM_EC48U_EXACT_V1', 'arithmetic':'python fractions.Fraction exact rational',
              'terminal_history_dependent':terminal_case(),
              'preterminal_future_operation':future_case(),
              'general_LR_fiber_randomized':general_fiber_tests(),
              'verification':'ALL_ASSERTIONS_PASS',
              'scope':'finite examples, not a universal proof; universals rely on argument in PROOF.md'}
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
