#!/usr/bin/env python3
"""Exact odds-ratio unimodality and sharp uniform dyadic error thresholds.

Frozen input: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Derived 954-event indexed-center observer; not a native X6/BRC claim.
Use --coefficients to reuse immutable predecessor stdout; otherwise regenerate
it from the adjacent repository script (requires the full repo checkout).
"""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
PREDECESSOR = HERE.parent / 'r5_all_budget_cohort_hierarchy_20261116' / 'VERIFY_R5_BUDGET_INTERACTION_HIERARCHY.py'
PIN = '435e77af0d180eac32bd1f9c4c464bc4010b7551'
EXPECTED_SHA256 = 'a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d'


def get_coefficients(filename):
    raw = Path(filename).read_bytes() if filename else subprocess.check_output([sys.executable, str(PREDECESSOR)])
    digest = sha256(raw).hexdigest()
    assert digest == EXPECTED_SHA256, ('upstream data changed', digest)
    source = json.loads(raw)
    assert source['status'] == 'PASS_R5_101_BUDGET_INTERACTION_HIERARCHY'
    assert source['scientific_input'] == PIN
    assert source['budgets'] == [214, 314]
    c = {int(k): {int(m): int(v) for m, v in d.items()}
         for k, d in source['all_budget_coefficients'].items()}
    assert sorted(c) == list(range(214, 315))
    return c, digest


def witness(a, b, c, d):
    common = gcd(gcd(a, b), gcd(c, d))
    return [str(q // common) for q in (a, b, c, d)]


def robust(p, q, bits):
    # Worst-case independent relative input errors <= 2^-bits.
    # Multiplication factors (1-e)^2 and (1+e)^2; no rounding.
    base = 1 << bits
    bigger, smaller = (p, q) if p > q else (q, p)
    return bigger * (base - 1)**2 > smaller * (base + 1)**2


def region(C, lo, hi, bit_i, bit_j, peak, required_bits, transitions):
    records = {}
    for k in range(lo, hi + 1):
        data = C[k]
        assert set(data) == {0, bit_i, bit_j, bit_i | bit_j}
        a, b, c, d = (data[t] for t in (0, bit_i, bit_j, bit_i | bit_j))
        assert min(a,b,c,d) > 0
        p,q = a*d,b*c
        assert p != q
        records[k] = (p, q, witness(a,b,c,d))
    changes = {}
    for k in range(lo,hi):
        p0,q0,_ = records[k]
        p1,q1,_ = records[k+1]
        gap = p1*q0-p0*q1
        assert gap != 0
        changes[k] = 1 if gap > 0 else -1
    assert all(changes[k] > 0 for k in range(lo,peak))
    assert all(changes[k] < 0 for k in range(peak,hi))
    assert sum(x > 0 for x in changes.values()) == peak-lo
    assert sum(x < 0 for x in changes.values()) == hi-peak
    assert all(robust(p,q,required_bits) for p,q,_ in records.values())
    margins = {k: Fraction(abs(p-q), 2*(p+q)) for k,(p,q,_) in records.items()}
    min_k = min(margins, key=lambda k:margins[k])
    assert not robust(*records[min_k][:2],required_bits-1)
    actual_transitions = []
    old_positive = records[lo][0] > records[lo][1]
    for k in range(lo+1,hi+1):
        new_positive = records[k][0] > records[k][1]
        if new_positive != old_positive: actual_transitions.append(k)
        old_positive = new_positive
    assert actual_transitions == transitions, (actual_transitions,transitions)
    critical = sorted(set([lo,peak,hi,min_k] + [k for t in transitions for k in (t-1,t)]))
    return {
        'region': [lo,hi], 'bits': [bit_i,bit_j],
        'strictly_increasing': [lo,peak], 'strictly_decreasing': [peak,hi],
        'adjacent_integer_comparisons': hi-lo,
        'increasing_comparisons': peak-lo, 'decreasing_comparisons': hi-peak,
        'sign_crossings_at_budgets': actual_transitions,
        'uniform_safe_componentwise_relative_error': f'2^-{required_bits}',
        'one_fewer_dyadic_bit_fails_at_budget': min_k,
        'minimal_margin_budget': min_k,
        'minimal_margin_numerator': str(margins[min_k].numerator),
        'minimal_margin_denominator': str(margins[min_k].denominator),
        'critical_normalized_cohorts': {str(k):records[k][2] for k in critical}
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--coefficients', type=Path)
    args = parser.parse_args()
    C, digest = get_coefficients(args.coefficients)
    first = region(C,223,290,64,128,247,20,[257])
    second = region(C,294,313,16,32,300,11,[299,302])
    assert first['minimal_margin_budget'] == 223
    assert second['minimal_margin_budget'] == 299
    result = {
        'status': 'PASS_R5_EXACT_ODDS_UNIMODALITY_AND_DYADIC_STABILITY',
        'scientific_input': PIN,
        'source_101_budget_coefficients_sha256': digest,
        'scope': 'derived 954-event indexed-center observer; exact integer cohort postprocessing',
        'total_budgets': 88,
        'total_adjacent_comparisons': 86,
        'cut25_cut27': first,
        'cut15_cut17': second,
        'assumption': 'Each of four positive exact cohort counts has independent relative error at most epsilon.',
        'sharp_dyadic_status': 'One fewer bit admits an adversarial componentwise relative perturbation at the specified budget.',
        'review': 'NOT_REVIEWED'
    }
    print(json.dumps(result, sort_keys=True, separators=(',',':')))


if __name__ == '__main__': main()
