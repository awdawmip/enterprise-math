#!/usr/bin/env python3
"""Exact checks for R159. No floats or external packages."""
from fractions import Fraction
from itertools import product
from math import floor, ceil
import json


def signature(word):
    m = len(word)
    prefix = [0]
    for bit in word:
        prefix.append(prefix[-1] + bit)
    alpha, beta = Fraction(0), Fraction(1)
    for i in range(m):
        for j in range(i + 1, m + 1):
            k, q = j - i, prefix[j] - prefix[i]
            alpha = max(alpha, Fraction(q - 1, k))
            beta = min(beta, Fraction(q + 1, k))
    if alpha >= beta:
        return None
    A = min(prefix[j] - j * alpha for j in range(m + 1))
    B = max(prefix[j] - j * beta for j in range(m + 1))
    U = alpha.denominator * (1 + A)
    V = beta.denominator * B
    assert U.denominator == 1 and V.denominator == 1
    return alpha, beta, int(U), int(V)


def phase_count(s, L):
    alpha, beta, U, V = s
    return (ceil(L * beta - Fraction(V, beta.denominator))
            - floor(L * alpha - Fraction(U, alpha.denominator)) - 1)


def width_ratio(s):
    alpha, beta, U, V = s
    return ((1 + Fraction(V, beta.denominator)
             - Fraction(U, alpha.denominator)) / (beta - alpha))


def run(max_length=13, max_L=31):
    totals = dict(max_length=max_length, candidate_words=0, admitted_words=0,
                  nonconstant_admitted=0, complement_count_checks=0,
                  reversal_width_checks=0, nonconstant_palindromes=0,
                  widest_word_counts={})
    for m in range(1, max_length + 1):
        widest = []
        for w in product((0, 1), repeat=m):
            totals['candidate_words'] += 1
            s = signature(w)
            if s is None:
                continue
            totals['admitted_words'] += 1
            alpha, beta, U, V = s
            flipped = signature(tuple(1 - bit for bit in w))
            assert flipped == (1 - beta, 1 - alpha,
                               beta.denominator - V, alpha.denominator - U)
            for L in range(1, max_L + 1):
                assert phase_count(s, L) == phase_count(flipped, L)
                totals['complement_count_checks'] += 1
            if len(set(w)) != 2:
                continue
            totals['nonconstant_admitted'] += 1
            n = sum(w)
            reversed_w = tuple(reversed(w))
            reversed_s = signature(reversed_w)
            assert reversed_s == (
                alpha, beta,
                alpha.denominator * (n + 1) - alpha.numerator * m - U,
                beta.denominator * (n + 1) - beta.numerator * m - V,
            )
            assert width_ratio(s) + width_ratio(reversed_s) == 2/(beta - alpha) - m
            totals['reversal_width_checks'] += 1
            if reversed_w == w:
                assert width_ratio(s) == 1/(beta - alpha) - Fraction(m, 2)
                totals['nonconstant_palindromes'] += 1
            if m >= 2 and beta - alpha == Fraction(2, m):
                widest.append(''.join(map(str, w)))
        if m >= 2:
            locations = [m // 2, m // 2 + 1] if m % 2 == 0 else [(m + 1) // 2]
            expected = set()
            for pos in locations:
                unit = [0] * m
                unit[pos - 1] = 1
                expected.add(''.join(map(str, unit)))
                expected.add(''.join(str(1 - b) for b in unit))
            assert set(widest) == expected, (m, widest, expected)
            totals['widest_word_counts'][str(m)] = len(widest)
    return totals


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True))
