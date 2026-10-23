#!/usr/bin/env python3
"""Independent exact verification of the auxiliary BRC two-pulse absorption claim.

Model: four labels 0..3, actions 0 and 2, the four good two-label masks
{0,1}, {1,2}, {1,3}, {2,3}; parameter z in [0,1].  No float arithmetic.
Finite checks supplement, not replace, the accompanying symbolic proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
import json

Q = [Fraction(0), Fraction(1, 7), Fraction(1, 4), Fraction(1, 3),
     Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(6, 7), Fraction(1)]
GOOD = {3, 6, 10, 12}


def word_delta_dp(word, z):
    """Independent 16-mask exact recursion, no use of compressed formula."""
    states = {0: Fraction(1)}
    for symbol in word:
        weights = (0, 1 + z, 1 - z, 1) if symbol == '0' else (1, 1, 0, 1)
        nxt = defaultdict(Fraction)
        for state, mass in states.items():
            for i, weight in enumerate(weights):
                if weight:
                    nxt[state | (1 << i)] += mass * weight / 3
        states = dict(nxt)
        assert sum(states.values()) == 1
    return sum((weight for state, weight in states.items() if state in GOOD), Fraction(0))


def word_delta_closed(word, z):
    """Exact count-sufficient formula derived by pair inclusion-exclusion."""
    a, b = word.count('2'), word.count('0')
    if not word:
        return Fraction(0)
    if a == 0:
        num = 2**b + (2+z)**b + (2-z)**b - 2*(1+z)**b - 2*(1-z)**b - 2
    elif b == 0:
        num = 2**(a+1) - 4
    else:
        num = ((2**a-3)*(1+z)**b + 2**a*(2+z)**b +
               2**b + (2-z)**b - 2)
    return Fraction(num, 3**(a+b))


def residuals(word, z):
    previous = Fraction(0)
    max_delta = Fraction(0)
    variation = Fraction(0)
    residual = Fraction(0)
    out = []
    for index in range(1, len(word)+1):
        current = word_delta_dp(word[:index], z)
        jump = current - previous
        variation += max(Fraction(0), jump)
        max_delta = max(max_delta, current)
        next_residual = variation-max_delta
        out.append((current, jump, next_residual, next_residual-residual))
        previous, residual = current, next_residual
    return out


def run():
    metrics = defaultdict(int)
    for n in range(1, 9):
        for word in map(''.join, product('02', repeat=n)):
            a = word.count('2')
            for z in Q:
                d = word_delta_dp(word, z)
                dc = word_delta_closed(word, z)
                assert d == dc, ('count formula mismatch', word, str(z), str(d), str(dc))
                metrics['word_parameter_count_formula_checks'] += 1
                if n >= 4 and a >= 2:
                    prev = word_delta_closed(word[:-1], z)
                    assert d < prev, ('not strict negative', word, str(z))
                    metrics['two_pulse_strict_negative_checks'] += 1
                if a >= 2 and n >= 2:
                    residual_data = residuals(word, z)
                    assert residual_data[-1][-1] == 0, ('residual increased', word, str(z))
                    metrics['two_pulse_residual_freeze_checks'] += 1
    for z in Q:
        assert word_delta_closed('22', z) == Fraction(4,9)
        assert word_delta_closed('220', z) == (11+4*z)/27
        assert word_delta_closed('220', z)-word_delta_closed('22', z)==(4*z-1)/27
        metrics['exceptional_220_checks'] += 1

    # Entire later time, count-class recurrence independent of word order.
    for z in Q:
        for n in range(9, 81):
            for a in range(2, n+1):
                b=n-a
                if a>=3:
                    s='2'*(a-1)+'0'*b+'2'
                    assert word_delta_closed(s,z) < word_delta_closed(s[:-1],z)
                    metrics['long_count_classes_last_2'] += 1
                if b>=1:
                    s='2'*a+'0'*(b-1)+'0'
                    assert word_delta_closed(s,z) < word_delta_closed(s[:-1],z)
                    metrics['long_count_classes_last_0'] += 1
                if a==2 and b>=2:
                    s='2'+'0'*b+'2'
                    assert word_delta_closed(s,z) < word_delta_closed(s[:-1],z)
                    metrics['long_count_classes_second_2'] += 1
    return {
        'scope': 'auxiliary_four_label_positive_mass_BRC_actions_0_2_z_in_[0,1]',
        'result': 'ALL_CHECKS_PASSED',
        'parameter_set': [str(x) for x in Q],
        'exhaustive_words': 'all binary 0/2 words of lengths 1 through 8',
        'additional_count_classes': 'all n=9..80 and all a=2..n on rational parameter grid',
        'note': 'universal theorem relies on the exact algebraic proof, not this finite test',
        'metrics': dict(sorted(metrics.items())),
    }


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2, ensure_ascii=False))
