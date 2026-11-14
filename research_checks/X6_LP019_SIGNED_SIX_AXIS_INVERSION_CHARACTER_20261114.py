#!/usr/bin/env python3
"""Independent exact check: signed X6 N-BRC paths vs inversion-parity character.

Frozen science: P000 V5, Z^6 signed primitive axis steps. This new
order-character is OPTIONAL, not the native N-valued path multiplicity.
No historical R063 C3/C4 benchmark is invoked.
"""
from functools import lru_cache
from itertools import product, combinations
from math import factorial


def multinomial(c):
    n = sum(c)
    x = factorial(n)
    den = 1
    for v in c:
        den *= factorial(v)
    return x // den


def inversion_character_formula(c):
    if sum(x & 1 for x in c) >= 2:
        return 0
    return factorial(sum(c) // 2) // _factorial_product(x // 2 for x in c)


def _factorial_product(xs):
    den = 1
    for x in xs:
        den *= factorial(x)
    return den


@lru_cache(None)
def inversion_character_recurrence(c):
    """Independent exact signed word recursion, append axis i last."""
    if not any(c):
        return 1
    result = 0
    for i, ci in enumerate(c):
        if ci:
            prev = c[:i] + (ci - 1,) + c[i + 1:]
            result += (-1 if sum(prev[i + 1:]) % 2 else 1) * inversion_character_recurrence(prev)
    return result


@lru_cache(None)
def native_word_count_recurrence(c):
    if not any(c):
        return 1
    return sum(native_word_count_recurrence(c[:i] + (ci - 1,) + c[i + 1:])
               for i, ci in enumerate(c) if ci)


def brute_inversion_character(c):
    """Independent explicit shortest labeled words, only small c."""
    n = sum(c)
    word = []
    def rec(left):
        if len(word) == n:
            inv = sum(word[i] > word[j] for i in range(n) for j in range(i + 1, n))
            yield -1 if inv & 1 else 1
            return
        for i, v in enumerate(left):
            if v:
                word.append(i)
                nxt = list(left)
                nxt[i] -= 1
                yield from rec(tuple(nxt))
                word.pop()
    vals = list(rec(tuple(c)))
    return sum(vals), len(vals)


def run():
    tested = 0
    zero = 0
    max_n = 0
    for c in product(range(4), repeat=6):
        native = multinomial(c)
        signed = inversion_character_formula(c)
        assert native_word_count_recurrence(c) == native, c
        assert inversion_character_recurrence(c) == signed, c
        assert 0 <= abs(signed) <= native, c
        assert (native - signed) % 2 == 0, c
        if sum(x & 1 for x in c) >= 2:
            assert signed == 0
            zero += 1
        tested += 1
        max_n = max(max_n, sum(c))
    explicit = 0
    for c in product(range(3), repeat=4):
        a, b = brute_inversion_character(c)
        assert (a, b) == (inversion_character_formula(c), multinomial(c)), c
        explicit += 1
    signed_two_support = 0
    for i, j in combinations(range(6), 2):
        for sign_i, sign_j in product((-1, 1), repeat=2):
            d = [0] * 6
            d[i] = sign_i
            d[j] = sign_j
            c = tuple(abs(x) for x in d)
            assert (multinomial(c), inversion_character_formula(c)) == (2, 0)
            signed_two_support += 1
    assert tested == 4096 and explicit == 81 and signed_two_support == 60
    assert (multinomial((2, 2, 2, 0, 0, 0)),
            inversion_character_formula((2, 2, 2, 0, 0, 0))) == (90, 6)
    assert (multinomial((1, 1, 1, 0, 0, 0)),
            inversion_character_formula((1, 1, 1, 0, 0, 0))) == (6, 0)
    print('PASS_X6_LP019_SIX_AXIS_INVERSION_CHARACTER',
          'six_axis_profiles=', tested, 'max_total_steps=', max_n,
          'zero_character_profiles=', zero,
          'independent_brute_profiles=', explicit,
          'signed_two_axis_endpoints=', signed_two_support)

if __name__ == '__main__':
    run()
