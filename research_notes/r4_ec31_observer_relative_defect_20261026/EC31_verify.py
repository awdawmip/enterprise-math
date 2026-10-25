#!/usr/bin/env python3
"""Exact positive-source BRC checks for EC31's scoped residual theorem.
Only uses integers and rational comparisons; no native heartbeat is simulated.
"""
import json
from fractions import Fraction
from itertools import product

CASES = ((1, 1, 1), (2, 1, 3), (1, 4, 2), (3, 2, 5))
MAX_DEPTH = 36
WORD_DEPTH = 8


def advance(pair, x, y, z):
    no_a, last_a = pair
    return ((y + z) * no_a + (y + 2 * z) * last_a,
            x * (no_a + last_a))


def source_weight(word, x, y, z, first_a=False):
    """Independent word-level positive labelled-source enumeration by factors."""
    memory = first_a
    count = 1
    for letter in word:
        if letter == 'A':
            count *= x
            memory = True
        elif letter == 'B':
            count *= y
            memory = False
        elif letter == 'C':
            count *= z * (2 if memory else 1)
            memory = False
        else:
            raise ValueError('Unknown step')
    return count


def endpoint_count(a, b, c):
    from math import factorial
    n = a + b + c
    return sum(factorial(n-r)//(
        factorial(r)*factorial(a-r)*factorial(b)*factorial(c-r))
        for r in range(min(a, c)+1))


def check():
    checked_words = 0
    checked_automaton_depths = 0
    checked_ratios = 0
    checked_endpoints = 0
    samples = []
    for x, y, z in CASES:
        s, p = x + y + z, x*z
        lower = Fraction(z*s, s*s+p+z*s)
        upper = Fraction(z, s+z)
        q0, q1 = (1, 0), (0, 1)
        prev = None
        before = None
        for h in range(MAX_DEPTH + 1):
            total0, total1 = sum(q0), sum(q1)
            if h == 0:
                assert total0 == total1 == 1
            else:
                assert total1 - total0 == z*prev
                assert total0 == s*prev + (p*before if h >= 2 else 0)
                proportion = Fraction(total1-total0, total1)
                assert lower <= proportion <= upper
                if h == 1:
                    assert proportion == upper
                if h == 2:
                    assert proportion == lower
                checked_ratios += 1
            checked_automaton_depths += 1
            if h in (1, 2, 3, 6, 12, 36):
                samples.append({'weights':[x,y,z], 'depth':h,
                    'mass_q0':str(total0), 'mass_q1':str(total1),
                    'defect':str(total1-total0),
                    'defect_over_true':f'{(total1-total0)}/{total1}',
                    'lower':str(lower), 'upper':str(upper)})
            before, prev = prev, total0
            q0 = advance(q0, x, y, z)
            q1 = advance(q1, x, y, z)
        for h in range(WORD_DEPTH + 1):
            total_word_q0, total_word_q1 = 0, 0
            for word_tuple in product('ABC', repeat=h):
                w = ''.join(word_tuple)
                w0 = source_weight(w, x, y, z)
                w1 = source_weight(w, x, y, z, first_a=True)
                assert w1-w0 == (w0 if w.startswith('C') else 0)
                total_word_q0 += w0
                total_word_q1 += w1
                checked_words += 1
            v0, v1 = (1, 0), (0, 1)
            for _ in range(h):
                v0 = advance(v0, x, y, z)
                v1 = advance(v1, x, y, z)
            assert total_word_q0 == sum(v0)
            assert total_word_q1 == sum(v1)
    for m in range(51):
        w0 = endpoint_count(m,0,1)
        delta = endpoint_count(m,0,0)
        assert (w0, delta, w0+delta) == (2*m+1,1,2*m+2)
        checked_endpoints += 1
    for c in range(1,51):
        assert endpoint_count(0,0,c) == endpoint_count(0,0,c-1) == 1
        checked_endpoints += 1
    return {'status':'PASS', 'model':'EC29/EC30 explicit positive-labelled path test model; not P000 native heartbeat',
      'exact_arithmetic':'Python arbitrary integers and Fraction',
      'weight_cases':[list(c) for c in CASES], 'depth_range':f'0..{MAX_DEPTH}',
      'word_depth_range':f'0..{WORD_DEPTH}',
      'automaton_depth_checks':checked_automaton_depths,
      'horizon_ratio_checks':checked_ratios,
      'independent_word_checks':checked_words,
      'endpoint_family_checks':checked_endpoints,
      'samples':samples,
      'universal_proof':'first-letter labelled source bijection; two-state recurrence and rational interval invariant',
      'native_heartbeat_executed':False,'independent_driver_review':False}


if __name__ == '__main__':
    print(json.dumps(check(), ensure_ascii=False, indent=2))
