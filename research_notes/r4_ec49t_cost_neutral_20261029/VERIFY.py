#!/usr/bin/env python3
"""EC49T: exact finite rational checks, no floating point."""
import json
from fractions import Fraction as F
from itertools import product

W = range(3)
SIGMA = (1, 0, -1)
ETAS = tuple(F(x) for x in ('0', '1/200', '1/6', '1/4', '1/3', '5/12', '49/100'))

def law(source, eta):
    data = {}
    for w, u, z in product(W, range(2), W):
        base = F(1, 9) if source == 'Q' else (F(1, 6) if w == z else F(1, 12))
        t = F(1, 2) + (2*u-1) * eta * SIGMA[w]
        data[w, u, z] = base * t
    assert len(data) == 18 and all(x > 0 for x in data.values())
    assert sum(data.values()) == 1
    return data

def best_terminal(encoding, p, q):
    """All deterministic terminal masks optimized exactly via positive parts."""
    alpha = beta = F(0)
    mask = []
    for d, u, z in product(range(2), range(2), W):
        pp = sum(p[w, u, z] for w in W if encoding[w] == d)
        qq = sum(q[w, u, z] for w in W if encoding[w] == d)
        if pp > qq:
            alpha += pp
            beta += qq
            mask.append((d, u, z))
    return alpha, beta, alpha-beta, mask

def check_eta(eta):
    p, q = law('P', eta), law('Q', eta)
    assert all(sum(p[w,u,z] for u in range(2) for z in W) == F(1,3) for w in W)
    assert all(sum(q[w,u,z] for u in range(2) for z in W) == F(1,3) for w in W)
    rows = [(enc, best_terminal(enc, p, q)) for enc in product(range(2), repeat=3)]
    observed = max(v[2] for _, v in rows)
    expected = F(1,9) + max(F(0), 6*eta-1)/36
    assert observed == expected
    assert observed < F(1,6)
    full_alpha = sum(p[w,u,w] for w in W for u in range(2))
    full_beta = sum(q[w,u,w] for w in W for u in range(2))
    assert (full_alpha, full_beta) == (F(1,2), F(1,3))
    # At identical per-source stage costs (first=A=1, second=S=1), all policies here cost 2.
    witness_enc, witness_val = next((e, v) for e, v in rows if v[2] == observed)
    return {'eta': str(eta), 'full': ['1/2', '1/3', '2', '2'],
            'compressed_optimum_delta': str(observed), 'compressed_best_alpha': str(witness_val[0]),
            'compressed_best_beta': str(witness_val[1]), 'sharp_gap': str(F(1,6)-observed),
            'witness_encoding': list(witness_enc), 'witness_mask': [list(x) for x in witness_val[3]],
            'enumerated_encoding_vertices': len(rows)}

def main():
    rows = [check_eta(eta) for eta in ETAS]
    assert rows[1]['compressed_optimum_delta'] == '1/9'
    assert rows[1]['sharp_gap'] == '1/18'
    assert rows[5]['compressed_optimum_delta'] == '11/72'
    assert rows[5]['sharp_gap'] == '1/72'
    result = {'status': 'PASS', 'arithmetic': 'fractions.Fraction',
              'verified_scope': '7 rational eta x 8 deterministic encoding vertices, optimized 12 terminal masks via exact source P/Q masses',
              'universal_scope': 'analytic convex extreme-point lemma and finite fiber identities in PROOF.md',
              'stage_cost_constraint': 'first-source expectation=1 and second-source expectation=1 in each of P,Q',
              'rows': rows}
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
