#!/usr/bin/env python3
"""EC49C: exact local binary W/V stopping example and finite spectrum certificates."""
from fractions import Fraction as F
from itertools import product
import json

ZERO, ONE = F(0), F(1)


def pos(x):
    return max(ZERO, x)


def spectrum(p, q):
    """Q-law of terminal LR, P(V=1)=p, Q(V=1)=q, all strictly positive."""
    out = {}
    for mass, ratio in ((q, p / q), (ONE - q, (ONE - p) / (ONE - q))):
        out[ratio] = out.get(ratio, ZERO) + mass
    return out


def call(nu, tau):
    return sum((mass * pos(r - tau) for r, mass in nu.items()), ZERO)


def improvement(nu, tau):
    return call(nu, tau) - pos(ONE - tau)


def gap(nu0, nu1, weight, tau, cost):
    ds = (improvement(nu0, tau), improvement(nu1, tau))
    return weight * pos(ds[0] - cost) + (ONE - weight) * pos(ds[1] - cost) - pos(weight * ds[0] + (ONE - weight) * ds[1] - cost)


def four_vector(actions, terminal_bits, p, q, weight=F(1, 2)):
    """actions: W-specific 0=reject,1=accept,2=continue; terminal_bits by LR."""
    out_p = ZERO
    out_q = ZERO
    live_p = ZERO
    live_q = ZERO
    for w in (0, 1):
        kw = weight if w == 0 else ONE - weight
        act = actions[w]
        if act == 1:
            out_p += kw
            out_q += kw
        elif act == 2:
            live_p += kw
            live_q += kw
            for v in (0, 1):
                pv = p[w] if v else ONE - p[w]
                qv = q[w] if v else ONE - q[w]
                lr = pv / qv
                if terminal_bits[lr]:
                    out_p += kw * pv
                    out_q += kw * qv
    return out_p, out_q, ONE + live_p, ONE + live_q


def objective(obs):
    a, b, ep, eq = obs
    return a - b - F(3, 16) * (ep + eq - 2)


def main():
    p = (F(3, 4), F(1, 2))
    q = (F(1, 4), F(1, 4))
    weight = F(1, 2)
    nus = [spectrum(p[w], q[w]) for w in (0, 1)]
    ratios = sorted(set(nus[0]) | set(nus[1]))
    assert ratios == [F(1, 3), F(2, 3), F(2), F(3)]
    leaves = []
    for w, v in product((0, 1), repeat=2):
        pw = (p[w] if v else ONE - p[w]) * weight
        qw = (q[w] if v else ONE - q[w]) * weight
        leaves.append(dict(w=w, v=v, P=str(pw), Q=str(qw), LR=str(pw / qw)))
        assert pw > 0 and qw > 0
    assert sum((F(row['P']) for row in leaves), ZERO) == ONE
    assert sum((F(row['Q']) for row in leaves), ZERO) == ONE
    assert [improvement(n, ONE) for n in nus] == [F(1, 2), F(1, 4)]
    assert gap(*nus, weight, ONE, F(3, 8)) == F(1, 16)
    
    # Exact exhaustive deterministic controllers; the same terminal LR bits are
    # available to both coarse and refined policies.
    coarse_values = []
    fine_values = []
    for bits in product((False, True), repeat=len(ratios)):
        terminal = dict(zip(ratios, bits))
        for a in (0, 1, 2):
            coarse_values.append(objective(four_vector((a, a), terminal, p, q)))
        for actions in product((0, 1, 2), repeat=2):
            fine_values.append(objective(four_vector(actions, terminal, p, q)))
    assert len(coarse_values) == 48 and len(fine_values) == 144
    assert max(coarse_values) == ZERO
    assert max(fine_values) == F(1, 16)
    terminal_best = {r: r > ONE for r in ratios}
    witness = four_vector((2, 0), terminal_best, p, q)
    assert witness == (F(3, 8), F(1, 8), F(3, 2), F(3, 2))
    assert objective(witness) == F(1, 16)

    # Exhaustively probe a nontrivial finite positive rational binary family:
    # every unequal LR spectrum has a rational hinge/cost separating witness.
    vals = (F(1, 4), F(1, 2), F(3, 4))
    matches = 0
    mismatches = 0
    total_cases = 0
    for p0, q0, p1, q1, weight0 in product(vals, repeat=5):
        nu0, nu1 = spectrum(p0, q0), spectrum(p1, q1)
        knots = sorted(set(nu0) | set(nu1) | {ONE})
        witness_tau = next((t for t in knots if improvement(nu0, t) != improvement(nu1, t)), None)
        total_cases += 1
        if nu0 == nu1:
            matches += 1
            assert witness_tau is None
            for t in knots:
                assert gap(nu0, nu1, weight0, t, F(1, 3)) == 0
        else:
            mismatches += 1
            assert witness_tau is not None
            d0 = improvement(nu0, witness_tau)
            d1 = improvement(nu1, witness_tau)
            mid = (d0 + d1) / 2
            assert mid >= 0
            assert gap(nu0, nu1, weight0, witness_tau, mid) > 0
    assert total_cases == 3**5
    report = {
        'arithmetic': 'Python standard-library Fraction only',
        'positive_leaf_table': leaves,
        'conditional_Q_LR_spectra': [{str(k): str(v) for k, v in sorted(n.items())} for n in nus],
        'hinge_tau': '1', 'conditional_continuation_gains': ['1/2', '1/4'],
        'incremental_cost': '3/8', 'strict_support_gap': '1/16',
        'coarse_max_objective': str(max(coarse_values)),
        'refined_max_objective': str(max(fine_values)),
        'refined_witness_four_vector': list(map(str, witness)),
        'coarse_deterministic_controllers': len(coarse_values),
        'refined_deterministic_controllers': len(fine_values),
        'binary_rational_family_cases': total_cases,
        'equal_spectrum_cases': matches, 'different_spectrum_cases': mismatches,
        'all_assertions_passed': True,
        'scope': 'fixed-prefix one-optional-terminal-step positive dual-source behavioral observer; finite numeric checks are examples, not all-real proof'
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
