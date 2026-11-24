"""Exact inputs for forcing 5 and 13 in every seven-prime R1 supplement.

The all-prime result is proved in proof.md; this checks its finite arithmetic.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path


P = {7, 17, 31, 41, 71, 97, 113, 127, 151, 241, 257, 281,
     337, 641, 673, 1321, 14449, 29191, 65537, 6700417}
INACTIVE = {3, 11, 61, 331, 37, 109}
BASICS = {5, 13}
H = {0, 1, 3, 6, 9, 10, 15, 16, 21, 30, 31, 33, 36, 45, 48,
     49, 51, 54, 55, 63, 64, 66, 69, 70, 75, 76, 78, 79, 84, 85,
     90, 91, 93, 96, 99, 100}
FACTORS = {
    4: {3: 1, 5: 1},
    8: {3: 1, 5: 1, 17: 1},
    12: {3: 2, 5: 1, 7: 1, 13: 1},
    16: {3: 1, 5: 1, 17: 1, 257: 1},
    20: {3: 1, 5: 2, 11: 1, 31: 1, 41: 1},
    24: {3: 2, 5: 1, 7: 1, 13: 1, 17: 1, 241: 1},
    28: {3: 1, 5: 1, 29: 1, 43: 1, 113: 1, 127: 1},
    36: {3: 3, 5: 1, 7: 1, 13: 1, 19: 1, 37: 1, 73: 1, 109: 1},
    40: {3: 1, 5: 2, 11: 1, 17: 1, 31: 1, 41: 1, 61681: 1},
    48: {3: 2, 5: 1, 7: 1, 13: 1, 17: 1, 97: 1, 241: 1, 257: 1, 673: 1},
    60: {3: 2, 5: 2, 7: 1, 11: 1, 13: 1, 31: 1, 41: 1,
         61: 1, 151: 1, 331: 1, 1321: 1},
}


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n)+1, 2))


def exact_order(base, q):
    x = base % q
    for d in range(1, q):
        if x == 1:
            return d
        x = x*base % q
    raise AssertionError((base, q))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('basics_certificate.json'))
    args = parser.parse_args()

    for exponent, factors in FACTORS.items():
        assert prod(q**e for q, e in factors.items()) == 2**exponent-1
        assert all(is_prime(q) for q in factors)
    excluded = P | INACTIVE | BASICS
    for e in range(1, 7):
        assert set(FACTORS[4*e]) <= excluded
    assert set(FACTORS[28])-excluded == {29, 43}
    assert set(FACTORS[36])-(P | BASICS | {3}) == {19, 37, 73, 109}
    assert set(FACTORS[40])-excluded == {61681}
    assert set(FACTORS[48]) <= excluded
    assert set(FACTORS[60]) <= excluded
    orders = {q: {'order2': exact_order(2, q),
                  'order16': exact_order(16, q)}
              for q in (29, 43, 19, 37, 73, 109, 61681)}
    assert orders[29] == {'order2': 28, 'order16': 7}
    assert orders[43] == {'order2': 14, 'order16': 7}
    assert orders[61681] == {'order2': 40, 'order16': 10}
    assert all(orders[q]['order16'] == 9 for q in (19, 37, 73, 109))

    gs = (1, 3, 5, 7, 15, 21, 35, 105)
    expected_incidence = (36, 23, 11, 7, 6, 4, 2, 1)
    parity_records = []
    for epsilon in (0, 1):
        holes = {z for z in range(105) if (epsilon+2*z) % 105 in H}
        maxima = tuple(max(sum(h % g == c for h in holes)
                           for c in range(g)) for g in gs)
        assert maxima == expected_incidence
        fixed = []
        period = lcm(105, 9)
        lifted_holes = [z for z in range(period) if z % 105 in holes]
        assert len(lifted_holes) == 108
        for q, root_residue in ((19, 6), (73, 37)):
            hits = [z for z in lifted_holes
                    if root_residue**2*pow(4, epsilon+2*z, q) % q == 1]
            assert len(hits) == 13
            fixed.append({'q': q, 'root_residue': root_residue,
                          'complete_period_z': period, 'hole_count': 108,
                          'hits': hits, 'relative_density': '13/108'})
        exceptional = {}
        for e, target in ((7, Fraction(7, 36)), (10, Fraction(11, 72))):
            period = lcm(105, e)
            cells = [z for z in range(period) if z % 105 in holes]
            counts = [sum(z % e == c for z in cells) for c in range(e)]
            assert Fraction(max(counts), len(cells)) == target
            exceptional[e] = {'complete_period_z': period,
                               'hole_count': len(cells), 'class_hit_counts': counts,
                               'max_relative_density': str(target)}
        parity_records.append({'epsilon': epsilon, 'incidence_maxima': maxima,
                               'fixed_order9_channels': fixed,
                               'exceptional_period_capacities': exceptional})

    generic = [Fraction(1, 8), Fraction(13, 108), Fraction(11, 144),
               Fraction(7, 72), Fraction(1, 12), Fraction(1, 9),
               Fraction(1, 18), Fraction(1, 36)]
    assert Fraction(23, 216) < Fraction(13, 108) < Fraction(1, 8)
    assert all(c <= Fraction(1, 8) for c in generic)
    no_basics = Fraction(21+13+13+4*12, 108)
    one_basic = 2*Fraction(7, 36)+Fraction(11, 72)+3*Fraction(1, 8)
    assert no_basics == Fraction(95, 108) < 1
    assert one_basic == Fraction(11, 12) < 1
    assert Fraction(6, 35)*(1-no_basics) == Fraction(13, 630)
    assert Fraction(3, 35)*(1-one_basic) == Fraction(1, 140)

    result = {
        'schema': 'riesel-seven-cover-forced-basic-pair-v1',
        'status': 'AUTHOR_PROOF_AND_EXACT_ARITHMETIC; NOT_INDEPENDENT_REVIEW',
        'scope': 'Every complete supplement of at most seven primes throughout R1, hence R2, contains 5 and 13.',
        'source_dependencies': [
            {'commit': 'b1de1acbdc97b5e51d486127abd1fadd24babd99',
             'path': 'research_notes/portable_direct/riesel_five_cover_20261123/global/proof.md',
             'scope': 'Old holes, incidence table, effective orders1through6 and global1/9bound.'},
            {'commit': 'f57dd6fd49d5b3f0a12abb3703c76edd6dbd37b5',
             'path': 'research_notes/portable_direct/riesel_finite_observers_20261124/six/proof.md',
             'scope': 'FixedR1phases and effective-order7and9candidate descriptions.'}],
        'complete_factorizations_2_power_minus_1': FACTORS,
        'effective_periods_excluded': [1, 2, 3, 4, 5, 6, 12, 15],
        'exceptional_primes': [29, 43, 61681],
        'exact_orders': orders,
        'generic_gcd_columns': [{'g': g, 'relative_capacity': str(c)}
                                for g, c in zip(gs, generic)],
        'parity_checks': parity_records,
        'no_basic_seven_channel_capacity': str(no_basics),
        'no_basic_full_exponent_gap': '13/630',
        'one_basic_six_other_channel_capacity': str(one_basic),
        'one_basic_full_exponent_gap': '1/140',
        'native_execution_claimed': False,
        'verification_boundary': 'Finite arithmetic checks the exact proof inputs; all-prime scope follows from the eight gcd columns in proof.md.'}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'forced_pair': [5, 13],
                      'scope': 'R1 complete supplements of size at most7',
                      'exceptional_primes': [29, 43, 61681],
                      'one_basic_capacity': str(one_basic),
                      'output': str(args.output)}))


if __name__ == '__main__':
    main()
