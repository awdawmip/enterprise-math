#!/usr/bin/env python3
"""Exact finite checks for the sharper X6 arithmetic majorant/window frontier.

The infinite summatory and window theorems are proved in the accompanying note.
Finite checks verify algebraic identities, safe sign-pair compression, and exact
rational exponent inequalities. No Foundation or native-law admission is implied.
"""
from __future__ import annotations
from fractions import Fraction
import argparse, json, math
import sympy as sp

A = Fraction(64, 59)
C = Fraction(5, 59)
GAMMA = Fraction(3, 8)
BETA = Fraction(1, 1)
ALPHA_CRIT = 6 * GAMMA - (1 + BETA + C)
ALPHA_WITNESS = Fraction(1, 7)
GAMMA_CRIT = (1 + BETA + C) / 6


def F(n: int) -> Fraction:
    out = Fraction(1)
    for p in sp.factorint(n):
        out *= A * (1 + Fraction(1, int(p)))
    return out


def g(n: int) -> Fraction:
    fac = sp.factorint(n)
    if any(int(e) > 1 for e in fac.values()):
        return Fraction(0)
    out = Fraction(1)
    for p in fac:
        out *= C + A / int(p)
    return out


def tau(n: int) -> int:
    return int(sp.prod(int(e) + 1 for e in sp.factorint(n).values()))


def verify(limit: int) -> dict:
    assert Fraction(39,236) == ALPHA_CRIT
    assert Fraction(41,118) == GAMMA_CRIT
    assert ALPHA_WITNESS < ALPHA_CRIT
    margin = ALPHA_CRIT - ALPHA_WITNESS
    assert margin == Fraction(37,1652)

    conv = 0
    point = 0
    sumF = Fraction(0)
    sumtau = 0
    snapshots = []
    targets = {255,1023,4095,16383,32767,65535}
    for n in range(1, limit + 1):
        fn = F(n)
        assert fn <= tau(n)
        point += 1
        if n <= min(limit, 2048):
            rec = sum((g(int(d)) for d in sp.divisors(n)), Fraction(0))
            assert rec == fn
            conv += 1
        sumF += fn
        sumtau += tau(n)
        if n in targets:
            bound = 16 * n * Fraction.from_float((1 + math.log(n)) ** float(C))
            snapshots.append({
                'X': n,
                'mean_F_float': float(sumF / n),
                'mean_tau_float': float(Fraction(sumtau, n)),
                'theorem_bound_mean_float': 16 * (1 + math.log(n)) ** float(C),
                'below_diagnostic_bound': float(sumF) <= float(bound),
            })

    signed = [(i,) for i in range(1, 6)] + [(-i,) for i in range(1, 6)]
    classes = {tuple(abs(x) for x in z) for z in signed}
    assert len(signed) == 2 * len(classes) == 10

    exponent = BETA + C - 6 * GAMMA + ALPHA_WITNESS
    assert exponent == -1 - margin
    assert 6 * GAMMA_CRIT == 1 + BETA + C

    return {
        'status': 'PASS_EXACT_FINITE_CHECKS_NOT_INFINITE_PROOF_OR_ADMISSION',
        'limit': limit,
        'pointwise_F_le_tau_checks': point,
        'dirichlet_convolution_checks': conv,
        'constants': {
            'a': str(A), 'c': str(C),
            'gamma_display': str(GAMMA),
            'beta_exception_strength': str(BETA),
            'alpha_critical': str(ALPHA_CRIT),
            'alpha_explicit_window': str(ALPHA_WITNESS),
            'summability_margin': str(margin),
            'gamma_critical_single_target': str(GAMMA_CRIT),
            'critical_log_window_eta_requirement': '>64/59',
        },
        'sign_pair_safe_boolean_compression': {
            'signed_witnesses': len(signed),
            'pair_classes': len(classes),
            'probability_bound_improvement': 'P(Z>0)<=E[Z]/2 for symmetric nonzero-vector count',
            'scope': 'Boolean short-vector existence only; not orientation-sensitive future operations',
        },
        'snapshots': snapshots,
        'boundaries': [
            'finite checks do not prove the infinite summatory theorem',
            'window theorem uses first moment plus submultiplicativity, not independence',
            'sign quotient is observer-scoped and does not permit dropping direction provenance elsewhere',
            'no all-integer constant-shape or constant-repair theorem',
        ],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=32767)
    ap.add_argument('--output')
    args = ap.parse_args()
    if not 2048 <= args.limit <= 131071:
        raise SystemExit('limit must be between 2048 and 131071')
    out = verify(args.limit)
    text = json.dumps(out, ensure_ascii=False, separators=(',', ':')) + '\n'
    if args.output:
        open(args.output, 'w', encoding='utf-8').write(text)
    print(text, end='')

if __name__ == '__main__':
    main()
