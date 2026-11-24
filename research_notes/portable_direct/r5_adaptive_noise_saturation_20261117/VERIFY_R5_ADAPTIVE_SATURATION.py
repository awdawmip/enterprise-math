#!/usr/bin/env python3
"""Exact finite-source certificate: all 101 budgets, arbitrary finite adaptive reads.

Use with the original R5 compact cohort output, produced at the unchanged science pin.
Only the bounded, adversarial *observation* error model is studied here.
"""
import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

SOURCE_SHA256 = 'a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d'
SCIENCE_PIN = '435e77af0d180eac32bd1f9c4c464bc4010b7551'
BUDGETS = tuple(range(214, 315))
TRIPLE = (214, 230, 302)
S_BITS = (0, 1, 2, 3, 6, 7)
T_STATES = (0, 16, 32, 48)


def gap(u, v):
    assert u > 0 and v > 0
    return Fraction(abs(u-v), u+v)


def min_margin(observations, budgets, states):
    best = None
    witness = None
    pairs = 0
    for left, right in itertools.combinations(states, 2):
        pairs += 1
        sep = max(gap(observations[k][left], observations[k][right]) for k in budgets)
        if best is None or sep < best:
            best, witness = sep, (left, right)
    return best, witness, pairs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('compact', type=Path)
    args = parser.parse_args()
    raw = args.compact.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SOURCE_SHA256
    data = json.loads(raw)
    assert data['status'] == 'PASS_R5_101_BUDGET_INTERACTION_HIERARCHY'
    assert data['scientific_input'] == SCIENCE_PIN
    assert data['budgets'] == [214, 314]
    obs = {}
    for k in BUDGETS:
        coefficients = {int(t): int(v) for t, v in data['all_budget_coefficients'][str(k)].items()}
        obs[k] = [sum(v for t, v in coefficients.items() if (t & m) == t)
                  for m in range(256)]
        assert all(v > 0 for v in obs[k])

    # A single pair is the adversarial obstruction at every allowed budget.
    d = {k: gap(obs[k][16], obs[k][32]) for k in BUDGETS}
    rho = Fraction(535905744549271, 298161762794076854)
    assert d[302] == rho
    assert all(d[k] <= rho for k in BUDGETS)
    assert [k for k in BUDGETS if d[k] == rho] == [302]
    assert all(d[k] == 0 for k in range(214, 294))
    assert d[314] == 0
    increasing = sum(d[k] < d[k+1] for k in range(293, 302))
    decreasing = sum(d[k] > d[k+1] for k in range(302, 314))
    assert increasing == 9 and decreasing == 12

    # In the 20 two-cut budgets the four counts have the same strict order,
    # and the shared closest pair is always the two singleton cut states.
    nearest_neighbor_certificates = 0
    for k in range(294, 314):
        vals = [obs[k][m] for m in T_STATES]
        assert vals == sorted(vals) and len(set(vals)) == 4
        adj = [gap(x, y) for x, y in zip(vals, vals[1:])]
        assert adj[1] < adj[0] and adj[1] < adj[2]
        assert adj[1] == d[k]
        nearest_neighbor_certificates += 1

    # Independent direct check: a previously saved fixed triple attains rho.
    s_states = [sum(((q >> j) & 1) << bit for j, bit in enumerate(S_BITS))
                for q in range(64)]
    p, pw, pc = min_margin(obs, TRIPLE[:2], s_states)
    t, tw, tc = min_margin(obs, TRIPLE[2:], T_STATES)
    full, fw, fc = min_margin(obs, TRIPLE, range(256))
    assert p > rho and t == rho and full == rho
    assert tw == (16, 32)

    result = {
        'status': 'PASS_R5_ADAPTIVE_OBSERVATION_NOISE_SATURATION',
        'scientific_pin': SCIENCE_PIN, 'source_sha256': SOURCE_SHA256,
        'budget_domain': [214, 314], 'budgets_exactly_checked': len(BUDGETS),
        'universal_witness_masks': [16, 32],
        'unique_maximizing_budget_for_witness': 302,
        'sharp_radius_fraction': [str(rho.numerator), str(rho.denominator)],
        'sharp_radius_approx': format(float(rho), '.16g'),
        'single_pair_exact_comparisons': len(BUDGETS),
        'strict_increasing_adjacent_checks': increasing,
        'strict_decreasing_adjacent_checks': decreasing,
        'common_two_cut_closest_pair_budgets': nearest_neighbor_certificates,
        'achieving_fixed_triple': list(TRIPLE),
        'partial_two_query_radius': [str(p.numerator), str(p.denominator)],
        'partial_minimum_pair': list(pw),
        'last_query_radius': [str(t.numerator), str(t.denominator)],
        'last_minimum_pair': list(tw),
        'full_three_query_radius': [str(full.numerator), str(full.denominator)],
        'full_minimum_pair': list(fw),
        'independent_pairwise_checks': {'partial': pc, 'last': tc, 'full': fc},
        'theorem': 'minimax threshold unchanged for any finite adaptive number of scalar readouts at budgets 214..314 under independently adversarial real relative observation errors',
        'review': 'NOT_REVIEWED',
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
