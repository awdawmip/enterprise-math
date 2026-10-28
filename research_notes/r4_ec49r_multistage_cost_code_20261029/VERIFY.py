#!/usr/bin/env python3
"""EC49R: exact Fractions for two-purchase action-code separation.

Finite deterministic enumeration checks the analytic support value.  No floating
point, external libraries, native BRC or X6 arithmetic are used.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

W = range(3)
Z = range(3)
Q = {(w, z): F(1, 9) for w in W for z in Z}
P = {(w, z): F(1, 6) if w == z else F(1, 12) for w in W for z in Z}
D = {(w, z): P[w, z] - Q[w, z] for w in W for z in Z}
PRICE = {'A': 1, 'B': 2}
LAMBDA = F(1, 48)
CODES = tuple((a, d) for a in 'AB' for d in range(2))
ACTIONS = (None,) + CODES

def assert_sources():
    for src in (P, Q):
        assert all(v > 0 for v in src.values())
        assert sum(src.values()) == 1
        for w in W:
            assert sum(src[w, z] for z in Z) == F(1, 3)
    assert sorted({D[w, z] for w in W for z in Z}) == [-F(1, 36), F(1, 18)]

def optimize_code(group, action):
    """All 8 accept subsets after S plus the skip-S option, exact."""
    n = len(group)
    if not n:
        return (F(0), False, 0)
    first = F(n * PRICE[action], 3)
    # Every bought path pays this first cost in both P and Q.
    best = -2 * LAMBDA * first  # stop (accept/reject equivalent for L)
    buy_witness = None
    for mask in range(8):
        lval = sum(D[w, z] for w in group for z in Z if mask & (1 << z))
        both_cost = F(n * (PRICE[action] + 1), 3)
        h = lval - 2 * LAMBDA * both_cost
        if h > best:
            best = h
            buy_witness = mask
    return best, buy_witness is not None, buy_witness

def exact_max_compressed():
    records = []
    for mapping in product(ACTIONS, repeat=3):
        by_code = {code: tuple(w for w in W if mapping[w] == code) for code in CODES}
        result = sum((optimize_code(by_code[(a, d)], a)[0] for a, d in CODES), F(0))
        records.append((result, mapping))
    value = max(v for v, _ in records)
    assert value == F(5, 72), value
    assert len(records) == 125
    return value, sum(v == value for v, _ in records)

def exact_max_full():
    # Source neutral W means early accept contributes no L. In a known W leaf,
    # buying A then S yields signed gain 1/18 and costs 2 to each source.
    options = (None, 'A', 'B')
    values = []
    for actions in product(options, repeat=3):
        gain = sum((sum(max(D[w, z], 0) for z in Z) for w in W if actions[w]), F(0))
        cost = sum((F(PRICE[a] + 1, 3) for a in actions if a), F(0))
        values.append(gain - 2 * LAMBDA * cost)
    assert len(values) == 27
    maximum = max(values)
    assert maximum == F(1, 12)
    return maximum

def observation(mapping, keep_w):
    # Both explicit witnesses always buy the second S and accept iff Z=W.
    assert all(mapping[w] is not None for w in W)
    if keep_w:
        assert all(mapping[w][0] == 'A' for w in W)
    else:
        assert len(set(mapping)) == 3
    alpha = sum((P[w, w] for w in W), F(0))
    beta = sum((Q[w, w] for w in W), F(0))
    cost_p = sum((sum(P[w, z] for z in Z) * (PRICE[mapping[w][0]] + 1) for w in W), F(0))
    cost_q = sum((sum(Q[w, z] for z in Z) * (PRICE[mapping[w][0]] + 1) for w in W), F(0))
    H = alpha - beta - LAMBDA * (cost_p + cost_q)
    return {'alpha': alpha, 'beta': beta, 'E_PT': cost_p, 'E_QT': cost_q, 'H': H}


def robust_variant():
    # The first purchased sensor now reveals a weakly W-informative U.
    # Either A or B observes the same U; second sensor S reveals Z.
    eta = F(1, 200)
    sigma = {0: 1, 1: 0, 2: -1}
    def prob_u(w, u, perturbed):
        p = F(1, 2) + (eta * sigma[w] if perturbed else 0)
        return p if u == 1 else 1 - p
    for src in (P, Q):
        perturb = {(w, u, z): src[w, z] * prob_u(w, u, True)
                   for w in W for u in (0, 1) for z in Z}
        baseline = {(w, u, z): src[w, z] * prob_u(w, u, False)
                    for w in W for u in (0, 1) for z in Z}
        assert len(perturb) == 18
        assert sum(perturb.values()) == 1
        assert all(x > 0 for x in perturb.values())
        assert all(sum(perturb[w, u, z] for u in (0, 1)) == src[w, z]
                   for w in W for z in Z)
        distance = sum((abs(perturb[key] - baseline[key]) for key in perturb), F(0)) / 2
        assert distance == F(1, 300)
    # H outcomes have acceptance range 1 and total paid cost range 3.
    # Two sources give the exact TV-based uniform perturbation budget.
    h_error = 2 * distance + 2 * (3 * distance) / 48
    assert h_error == F(17, 2400)
    certified_gap = F(1, 12) - (F(5, 72) + h_error)
    assert certified_gap == F(49, 7200) and certified_gap > 0
    return {'eta': display(eta), 'source_TV': display(distance),
            'uniform_H_error_budget': display(h_error),
            'perturbed_full_witness_H': '1/12',
            'upper_bound_perturbed_compressed_H': display(F(5, 72) + h_error),
            'certified_strict_gap_lower_bound': display(certified_gap),
            'joint_atoms_per_source': 18, 'all_positive': True}

def display(f):
    return str(f.numerator) if f.denominator == 1 else f'{f.numerator}/{f.denominator}'

if __name__ == '__main__':
    assert_sources()
    full_optimum = exact_max_full()
    compressed_optimum, num_opt = exact_max_compressed()
    full = observation((('A', 0), ('A', 0), ('A', 0)), True)
    compressed = observation((('A', 0), ('A', 1), ('B', 0)), False)
    assert full['H'] == full_optimum
    assert compressed['H'] == compressed_optimum
    assert full_optimum - compressed_optimum == F(1, 72)
    report = {
        'study': 'EC49R two-purchase action-code cost obstruction',
        'scope': '9 strictly positive rational P/Q atoms, three W states, two first-tag actions, two external memory values, second sensor Z, early stops, fresh independent behavioral randomness',
        'arithmetic': 'Python stdlib fractions.Fraction',
        'sources': {'P_diag': '1/6', 'P_offdiag': '1/12', 'Q_all': '1/9'},
        'sensor_costs': {'A': 1, 'B': 2, 'S': 1},
        'penalty_lambda': '1/48',
        'initial_deterministic_compressed_maps': 125,
        'terminal_acceptance_masks_per_bought_code': 8,
        'full_first_stage_deterministic_maps_checked': 27,
        'compressed_optimal_initial_maps_count': num_opt,
        'weakly_informative_first_sensor': robust_variant(),
        'max_full_H': display(full_optimum),
        'max_compressed_H': display(compressed_optimum),
        'sharp_gap': display(full_optimum - compressed_optimum),
        'full_witness': {k: display(v) for k, v in full.items()},
        'compressed_witness': {k: display(v) for k, v in compressed.items()},
        'status': 'PASS',
        'generality': 'Finite enumeration is diagnostic; the all-real upper bounds follow from a multi-affine-extremal argument and exact three-row signed-mass cell inequality in PROOF.md.'
    }
    target = Path(__file__).with_name('EXACT_REPORT.json')
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2, ensure_ascii=False))
