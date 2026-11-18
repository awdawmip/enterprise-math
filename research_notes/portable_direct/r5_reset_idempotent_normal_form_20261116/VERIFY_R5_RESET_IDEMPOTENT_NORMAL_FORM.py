#!/usr/bin/env python3
"""Exact finite tests for a reset-controller idempotent normal form.
No external dependencies. This program checks finite instances; universal theorem
has an independent symbolic proof in the accompanying research note.
"""
from itertools import product
from math import factorial, gcd
import json


def compose(f, g):
    """f after g; f and g are tuples of indexed images."""
    return tuple(f[g[i]] for i in range(len(f)))


def power(f, p):
    n = len(f)
    r = tuple(range(n))
    while p:
        if p & 1:
            r = compose(f, r)
        f = compose(f, f)
        p //= 2
    return r


def lcm(a, b):
    return a // gcd(a, b) * b


def exponent(m):
    out = 1
    for j in range(1, m + 1):
        out = lcm(out, j)
    return out


def normal_form(f0, f1):
    assert len(f0) == len(f1)
    n = len(f0)
    e = exponent(n)
    g0, g1 = power(f0, e), power(f1, e)
    assert compose(g0, g0) == g0
    assert compose(g1, g1) == g1
    im0, im1 = set(g0), set(g1)
    q = im0 | im1
    assert all(g0[x] in q and g1[x] in q for x in q)
    assert all((g0[x] == x or g1[x] == x) for x in q)
    return g0, g1, q


def formula_count(n):
    t = 0
    for a in range(n + 1):
        for b in range(n - a + 1):
            c = n - a - b
            if a + c == 0 or b + c == 0:
                continue
            t += (factorial(n) // (factorial(a)*factorial(b)*factorial(c))) * ((a+c)**b) * ((b+c)**a)
    return t


def exhaustive():
    output = []
    for n in range(1, 5):
        maps = list(product(range(n), repeat=n))
        idem = [f for f in maps if compose(f, f) == f]
        valid_pairs = 0
        pair_tests = 0
        for f in maps:
            g = power(f, exponent(n))
            assert compose(g, g) == g
        for f in idem:
            for g in idem:
                pair_tests += 1
                if len(set(f) | set(g)) == n:
                    valid_pairs += 1
        assert valid_pairs == formula_count(n)
        output.append(dict(m=n, idempotent_maps=len(idem), all_idempotent_pairs=pair_tests,
                           normalized_trimmed_pairs=valid_pairs, theoretical=formula_count(n),
                           all_transformations_checked=len(maps)))
    return output


def physical_demo():
    # k=3 and two controller variants for every physical state. The genuine
    # source centre at controller state (u,p) is exactly u, so every output is
    # feasible for its current physical unavailability mask at slack 0.
    k = 3
    n = (1 << k) * 2
    f = []
    for bit in range(2):
        f.append(tuple(2*((state//2 & ~1) | bit) + (1 - state % 2)
                       for state in range(n)))
    f0, f1 = f
    assert compose(f0, f0) != f0 and compose(f1, f1) != f1
    g0, g1, q = normal_form(f0, f1)
    assert len(q) <= n
    # Initialise the normalized machine after a physical-state-preserving
    # reset (new bit equals physical bit), and test all words of length <= 7.
    checks = 0
    for raw in range(1 << k):
        b = raw & 1
        initial = 2*raw
        old_init = (g0 if b == 0 else g1)[initial]
        assert old_init in q and old_init // 2 == raw
        for length in range(8):
            for word in product((0,1), repeat=length):
                physical = raw
                state = old_init
                for command in word:
                    physical = (physical & ~1) | command
                    state = (g0 if command == 0 else g1)[state]
                    assert state // 2 == physical
                    checks += 1
                assert state // 2 == physical
    return {'physical_k': k, 'original_m': n, 'normalized_m': len(q),
            'normalization_exponent': exponent(n), 'word_length_max': 7,
            'all_words_including_empty': (1 << k) * sum(2**d for d in range(8)),
            'step_checks': checks, 'controller_nonidempotent_original': True,
            'normal_form_idempotent': True}


def witness_cross_absorption_defect():
    f0, f1 = (0,1,1), (2,2,2)
    g0,g1,q=normal_form(f0,f1)
    assert q == {0,1,2}
    assert g0 == f0 and g1 == f1
    assert g0[g1[0]] == 1 and g0[0] == 0
    return {'m':3,'reset_0':list(g0),'reset_1':list(g1),
            'defect_state':0,'reset_0_after_1':g0[g1[0]],'reset_0_alone':g0[0]}


def main():
    data={'schema':'R5_RESET_IDEMPOTENT_NORMAL_FORM_CHECK_V1',
          'frozen_science_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
          'exhaustive':exhaustive(),
          'source_labelled_physical_example':physical_demo(),
          'cross_absorption_defect':witness_cross_absorption_defect(),
          'result':'PASS_R5_RESET_IDEMPOTENT_NORMAL_FORM',
          'limits':'Finite testing supports but does not replace the universal symbolic proof.'}
    print(json.dumps(data, ensure_ascii=False, indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
