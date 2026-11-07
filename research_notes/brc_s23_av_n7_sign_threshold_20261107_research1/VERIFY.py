#!/usr/bin/env python3
"""Exact Fraction certificate for the S23/AV two-fiber first sign-change at n=7.

Independent exhaustive ordered-word and multinomial/count witnesses; no floats in
any assertion. Python >=3.8, standard library only.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial

P0 = (F(1, 2), F(1, 4), F(1, 4))  # labels (1,3,4)
P1 = (F(5, 7), F(1, 4), F(1, 28))
Z = F(1, 4)


def pword(word, p):
    v = F(1)
    for j in word:
        v *= p[j]
    return v


def ordered_tv(n):
    pos = F(0)
    neg = F(0)
    wrong = []
    for w in product(range(3), repeat=n):
        d = pword(w, P0) - pword(w, P1)
        if d > 0:
            pos += d
        elif d < 0:
            neg -= d
            if 2 in w:
                wrong.append(w)
    assert pos == neg
    return pos, wrong


def histogram_tv(n):
    total = F(0)
    for k in range(n + 1):
        for ell in range(n - k + 1):
            r = n - k - ell
            multiplicity = factorial(n) // (factorial(k) * factorial(ell) * factorial(r))
            d = P0[0]**k * P0[1]**r * P0[2]**ell - P1[0]**k * P1[1]**r * P1[2]**ell
            total += multiplicity * abs(d)
    return total / 2


def event_tv_difference(n):
    return (1-P1[2])**n - (1-P0[2])**n


assert P0[1] == P1[1] == Z
assert all(sum(x) == 1 for x in (P0, P1))
assert F(1, 2)*F(1, 2) == Z
assert (1-F(5, 7))*F(7, 8) == Z

for n in range(1, 8):
    exact, bad = ordered_tv(n)
    assert exact == histogram_tv(n)
    event = event_tv_difference(n)
    if n <= 6:
        assert exact == event
        assert not bad
    else:
        assert n == 7
        assert len(bad) == 7
        assert all(w.count(0) == 6 and w.count(2) == 1 and w.count(1) == 0 for w in bad)
        correction = 7*(P1[0]**6*P1[2] - P0[0]**6*P0[2])
        assert exact == event + correction
        assert correction == F(176457, 30118144)
        assert exact == F(4369158699, 6746464256)
    print(f'n={n} pair_TV={exact} minimax_lower={exact/2} event_difference={event} flipped_words={len(bad)}')

assert event_tv_difference(4)/2 == F(5265, 19208)
assert (event_tv_difference(4)/2 - F(5211, 21952)) == F(5643, 153664)
assert (event_tv_difference(7) + F(176457, 30118144))/2 == F(4369158699, 13492928512)
assert 7*F(7, 10)**5 > 1 and 7*F(7, 10)**6 < 1
# Exact likelihood-ratio classifier for all n; these tests are finite spot checks.
for n in range(1, 13):
    for k in range(n + 1):
        for ell in range(n - k + 1):
            r = n - k - ell
            d = P0[0]**k * P0[1]**r * P0[2]**ell - P1[0]**k * P1[1]**r * P1[2]**ell
            assert (d > 0) == (7**(k+ell) > 10**k)
            assert (d < 0) == (7**(k+ell) < 10**k)
    if n >= 7:
        assert histogram_tv(n) > event_tv_difference(n)
print('PASS_INTEGER_LR_CLASSIFIER_N1_TO_12')
print('PASS_S23_N7_LIKELIHOOD_SIGN_TRANSITION_EXACT_20261107')
