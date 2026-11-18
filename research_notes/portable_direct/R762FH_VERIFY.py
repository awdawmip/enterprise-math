#!/usr/bin/env python3
"""Exact finite q=9 six-branch BRC Fourier-blindness certificate.
No numerical approximation, third-party packages, or downloaded inputs.
"""
import json
from collections import Counter

Q = 9
STEPS = ((0, 0, 0), (1, 0, 0), (0, 0, 1),
         (1, 1, 0), (0, 1, 1), (1, 1, 1))

# Integral basis of Z[zeta_9] = Z[t]/(t^6+t^3+1).
POW = []
for k in range(Q):
    v = [0] * 6
    if k < 6:
        v[k] = 1
    else:
        v[k - 6] = -1
        v[k - 3] = -1
    POW.append(tuple(v))
ONE = POW[0]
ZERO = (0,) * 6

def multiply(a, b, modulus=None):
    tmp = [0] * 9
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            tmp[(i + j) % 9] += x * y
    result = [sum(tmp[k] * POW[k][j] for k in range(9)) for j in range(6)]
    if modulus is not None:
        result = [x % modulus for x in result]
    return tuple(result)

def power(a, exponent, modulus=None):
    result = ONE
    while exponent:
        if exponent & 1:
            result = multiply(result, a, modulus)
        a = multiply(a, a, modulus)
        exponent //= 2
    return result

def lambda_character(a, b, c):
    terms = (0, a, c, (a+b) % 9, (b+c) % 9, (a+b+c) % 9)
    return tuple(sum(POW[e][j] for e in terms) for j in range(6))

def verify_characters():
    bucket = Counter()
    for a in range(Q):
        for b in range(Q):
            for c in range(Q):
                cubed = power(lambda_character(a, b, c), 3)
                assert all(x % 3 == 0 for x in cubed), (a, b, c)
                beta = tuple(x // 3 for x in cubed)
                if all(x % 3 == 0 for x in beta):
                    bucket['beta_zero_mod_3'] += 1
                else:
                    assert power(beta, 6, 3) == ONE, (a, b, c, beta)
                    bucket['beta_six_one_mod_3'] += 1
    assert bucket == Counter(beta_zero_mod_3=243, beta_six_one_mod_3=486)
    return dict(bucket)

def idx(x, y, z):
    return 81*x + 9*y + z

SHIFTS = [tuple(idx((i//81+dx)%9, ((i//9)%9+dy)%9, (i%9+dz)%9)
                for i in range(729)) for dx, dy, dz in STEPS]

def v3(n):
    if not n:
        return None
    n = abs(n)
    count = 0
    while n % 3 == 0:
        n //= 3
        count += 1
    return count

def verify_terminals():
    targets = {36} | {36 + 18*3**(h-3) for h in range(3, 9)}
    saved = {}
    vector = [0] * 729
    vector[0] = 1
    for n in range(1, max(targets)+1):
        following = [0] * 729
        for shift in SHIFTS:
            for i, value in enumerate(vector):
                if value:
                    following[shift[i]] += value
        vector = following
        if n in targets:
            scalar = 3**(n//3-2)
            assert all(value % scalar == 0 for value in vector), n
            saved[n] = tuple(value//scalar for value in vector)
    records = []
    for h in range(3, 9):
        L = 18*3**(h-3)
        delta = tuple(x-y for x, y in zip(saved[36+L], saved[36]))
        nonzero_vals = [v3(x) for x in delta if x]
        minimum = min(nonzero_vals)
        origin = delta[0] % 3**h
        assert minimum == h-2, (h, minimum)
        assert origin == 2*3**(h-2), (h, origin)
        records.append(dict(h=h, L=L, n=36, minimum_full_terminal_v3=minimum,
                            origin_mod_3h=origin, origin_div_3hminus2_mod9=2,
                            terminals_checked=729))
    return records

if __name__ == '__main__':
    evidence = dict(schema='R762FH_Q9_FOURIER_BLINDSPOT_EVIDENCE_V1',
                    task_id='RS-X6-TRIADIC-CLOSURE-DYNAMICS',
                    model='P=1+X+Z+XY+YZ+XYZ in Z[(Z/9Z)^3]',
                    all_729_characters=verify_characters(),
                    exact_terminal_differences=verify_terminals(),
                    arithmetic='integer-only exact division, no approximation',
                    reviewed='NOT_REVIEWED', result='PASS')
    print(json.dumps(evidence, indent=2, ensure_ascii=False))
