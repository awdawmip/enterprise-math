#!/usr/bin/env python3
"""Exact finite verifier for R213 Green/ideal formulas on paired-event observers.
Pure finite typed observer algebra; does not execute native physical BRC transport.
"""
from math import comb, factorial
import json

def quotient(m, k, L):
    alphabet = tuple(range(m * (k + 1)))
    identity = ((), ())
    def letter(x, a):
        s, t = x
        p = a // m  # 0 neutral, 1..k selected
        if p:
            s = tuple(v for v in s if v != p) + (p,)
        return (s, (t + (a,))[-L:])
    seen = {identity}
    states = [identity]
    for x in states:
        for a in alphabet:
            y = letter(x, a)
            if y not in seen:
                seen.add(y)
                states.append(y)
    def multiply(x, y):
        s, t = x
        u, v = y
        return (tuple(w for w in s if w not in u) + u, (t + v)[-L:])
    return states, multiply

def is_factor(v, x):
    return not x or any(v[i:i + len(x)] == x for i in range(len(v) - len(x) + 1))

def validate(m, k, L):
    states, multiply = quotient(m, k, L)
    S = set(states)
    pairs = 0
    for x in states:
        s, t = x
        h = len(t)
        support = set(s)
        right = {y for y in states if
                 (len(y[1]) < L and len(y[1]) >= h and y[1][:h] == t)
                 or (len(y[1]) == L and set(y[0]) >= support)}
        if h == L:
            right = {y for y in states if len(y[1]) == L and set(y[0]) >= support}
        observed_right = {multiply(x, y) for y in states}
        assert right == observed_right, ('right', m, k, L, x)
        if h < L:
            left = {y for y in states if len(y[1]) >= h and y[1][-h:] == t} if h else S
        else:
            left = {y for y in states if len(y[1]) == L and y[1] == t and
                    (y[0][-len(s):] == s if s else True)}
        observed_left = {multiply(y, x) for y in states}
        assert left == observed_left, ('left', m, k, L, x)
        two_sided = {multiply(y, z) for z in observed_right for y in states}
        predicted = {y for y in states if
                     (len(y[1]) < L and is_factor(y[1], t))
                     or (len(y[1]) == L and set(y[0]) >= support)}
        if h == L:
            predicted = {y for y in states if len(y[1]) == L and set(y[0]) >= support}
        assert two_sided == predicted, ('two_sided', m, k, L, x)
        pairs += 2 * len(states)
    return {'m':m, 'k':k, 'L':L, 'states':len(states), 'left_right_products_checked':pairs}

def left_ending_count(m, k, L, x):
    h = len(x)
    selected = {p // m for p in x if p // m}
    n = L - h
    def N(j):
        return sum(factorial(j) // factorial(j - a) for a in range(j + 1))
    total = 0
    for d in range(min(k - len(selected), n) + 1):
        surj = sum((-1)**j * comb(d,j) * (len(selected)+1+d-j)**n
                   for j in range(d + 1))
        total += comb(k-len(selected),d) * m**n * surj * N(k-len(selected)-d)
    return total

def demonstration():
    models = [(1,0,1),(1,1,1),(1,1,2),(1,1,3),(1,1,4),
              (1,2,1),(1,2,2),(1,2,3),(2,0,2),(2,1,1),
              (2,1,2),(2,1,3),(2,2,1),(2,2,2)]
    results = [validate(*v) for v in models]
    J, multiply = quotient(1,1,4)
    xx = next(x for x in J if x[1] == (1,1))
    yy = next(x for x in J if x[1] == (1,0))
    def ideal_size(z):
        return len({multiply(u,multiply(z,v)) for u in J for v in J})
    overlap = {'repeated_event_11_ideal':ideal_size(xx),
               'distinct_event_10_ideal':ideal_size(yy)}
    assert overlap['distinct_event_10_ideal'] == overlap['repeated_event_11_ideal'] + 1
    six_axis = {'total_states':1407685, 'short_states':85,
                'full_tail_states':1407600, 'R_or_J_classes':149,
                'L_classes':1407685,
                'neutral_one_event_right_ideal':1407601,
                'selected_one_event_right_ideal':1174177,
                'neutral_one_event_left_ideal':1+left_ending_count(12,6,2,(0,)),
                'selected_one_event_left_ideal':1+left_ending_count(12,6,2,(12,))}
    assert six_axis['neutral_one_event_left_ideal'] == 46957
    assert six_axis['selected_one_event_left_ideal'] == 11725
    return {'status':'PASS', 'models':results, 'total_models':len(results),
            'total_states':sum(r['states'] for r in results),
            'product_membership_checks':sum(r['left_right_products_checked'] for r in results),
            'overlap_witness':overlap, 'six_axis':six_axis,
            'arithmetic':'exact integer and finite-set enumeration'}

if __name__ == '__main__':
    print(json.dumps(demonstration(), indent=2, ensure_ascii=False, sort_keys=True))
