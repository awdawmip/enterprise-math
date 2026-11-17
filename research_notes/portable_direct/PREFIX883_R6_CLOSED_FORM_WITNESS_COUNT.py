#!/usr/bin/env python3
"""PREFIX-883: exact closed-form count of signed named-XOR collision witnesses.
Standard library only; no floating-point arithmetic.
"""
from itertools import product
from math import gcd
import json


def ones_prefix(t, z):
    """Extended integer prefix of bit-t ones, valid for negative z."""
    h = 1 << t
    quot, rem = divmod(z, 2 * h)
    return quot * h + max(0, rem - h)


def bit_range(lo, hi, t, shift, want):
    if hi <= lo:
        return 0
    ones = ones_prefix(t, hi + shift) - ones_prefix(t, lo + shift)
    return ones if want else hi - lo - ones


def major_intervals(t, shift, want):
    h = 1 << t
    period = 2 * h
    start = (want * h - shift) % period
    if start + h <= period:
        return [(start, start + h)]
    return [(start, period), (0, start + h - period)]


def constrained_prefix(terms, z):
    """Exact count in [0,z) for 0,1,2 signed XOR source constraints."""
    if z <= 0:
        return 0
    if not terms:
        return z
    if len(terms) == 1:
        t, shift, want = terms[0]
        return bit_range(0, z, t, shift, want)
    a, b = terms
    if a[0] < b[0]:
        a, b = b, a
    period = 1 << (a[0] + 1)
    major = major_intervals(*a)
    if a[0] == b[0]:
        minor = major_intervals(*b)

        def segment(right):
            return sum(max(0, min(v, z_, right) - max(u, w))
                       for u,v in major for w,z_ in minor)
    else:
        t, shift, want = b

        def segment(right):
            return sum(bit_range(u, min(v, right), t, shift, want)
                       for u,v in major if u < right)
    cycles, rem = divmod(z, period)
    return cycles * segment(period) + segment(rem)


def witness_count(p, a, d, e):
    """Number of x such that (x,x+d) and (x+a,x+a+e) are both legal."""
    N = 1 << p
    L = max(0, -a, -d, -a-e)
    U = min(N-1, N-1-a, N-1-d, N-1-a-e)
    if L > U:
        return 0
    terms = []
    for delta, shift in ((d, 0), (e, a)):
        if delta:
            value = abs(delta)
            if value & (value-1) or value >= N:
                raise ValueError("signed change is not one declared source")
            t = value.bit_length()-1
            terms.append((t, shift, int(delta < 0)))
    return constrained_prefix(terms, U+1) - constrained_prefix(terms, L)


def brute_count(p, a, d, e):
    N = 1 << p
    accepted = 0
    allowed = {0} | {1 << i for i in range(p)}
    for x in range(N):
        y = x+a
        if all(0 <= z < N for z in (x, x+d, y, y+e)):
            if (x ^ (x+d)) in allowed and (y ^ (y+e)) in allowed:
                accepted += 1
    return accepted


def collision_pairs(p, q1, q2):
    """Number of distinct unordered collisions of ordered transitions."""
    N = 1 << p
    D = [0] + [s * (1 << i) for i in range(p) for s in (-1,1)]
    larger_old = same_old = 0
    for k in range((N-1)//q1 + 1):
        a = k*q1
        for d in D:
            for e in D:
                if (a+e-d) % q2:
                    continue
                if k == 0:
                    if d != e:
                        same_old += witness_count(p, 0, d, e)
                else:
                    larger_old += witness_count(p, a, d, e)
    assert same_old % 2 == 0
    return larger_old + same_old//2


def brute_collision_pairs(p, q1, q2):
    N = 1 << p
    groups = {}
    for x in range(N):
        for y in (x,) + tuple(x ^ (1 << i) for i in range(p)):
            key = (x % q1, y % q2)
            groups[key] = groups.get(key, 0) + 1
    return sum(n*(n-1)//2 for n in groups.values())


def noop_pairs(p, q1, q2):
    N = 1 << p
    step = q1 // gcd(q1, q2) * q2
    t, r = divmod(N, step)
    return r*t*(t+1)//2 + (step-r)*t*(t-1)//2


def brute_noop_pairs(p, q1, q2):
    groups = {}
    for x in range(1 << p):
        key = (x % q1, x % q2)
        groups[key] = groups.get(key,0)+1
    return sum(n*(n-1)//2 for n in groups.values())


def validate():
    cases = 0
    by_p = []
    for p in range(1,7):
        N = 1 << p
        D = [0] + [s*(1<<i) for i in range(p) for s in (-1,1)]
        tests = 0
        for a,d,e in product(range(N+1),D,D):
            got = witness_count(p,a,d,e)
            expected = brute_count(p,a,d,e)
            assert got == expected,(p,a,d,e,got,expected)
            tests += 1
        cases += tests
        by_p.append({'p':p,'cases':tests})
    n_spectrum = 0
    for p,Q in ((1,3),(2,7),(3,15),(4,31),(5,31),(6,15)):
        for q1 in range(1,Q+1,2):
            for q2 in range(1,Q+1,2):
                a = collision_pairs(p,q1,q2)
                b = brute_collision_pairs(p,q1,q2)
                assert a == b,(p,q1,q2,a,b)
                n_spectrum += 1
    n_noop = 0
    for p in range(1,8):
        N = 1 << p
        for q1 in range(1,2*N+1,2):
            for q2 in range(1,2*N+1,2):
                a = noop_pairs(p,q1,q2)
                b = brute_noop_pairs(p,q1,q2)
                assert a == b,(p,q1,q2,a,b)
                n_noop += 1

    count_pairs = count_witnesses = 0
    for q1 in range(523001,524288,2):
        for q2 in range(523001,524288,2):
            n = noop_pairs(32,q1,q2)
            count_pairs += bool(n)
            count_witnesses += n

    examples = []
    for a,d,e in ((4294959104,16384,0),(3831432631,0,2),
                  ((1<<32)-1,0,0),(1<<31,-(1<<30),1<<25),
                  (0,1,1),(0,1,-1),(0,1<<31,-(1<<31))):
        examples.append({'a':a,'d':d,'e':e,'count':witness_count(32,a,d,e)})

    return {
        'schema':'PREFIX883_EXACT_WITNESS_COUNT_VALIDATION_V1',
        'precision':'exact_integer',
        'signed_parameter_checks':cases,
        'per_p':by_p,
        'full_collision_spectrum_cross_checks':n_spectrum,
        'no_op_pair_cross_checks':n_noop,
        'p32_high_strip':{
            'odd_moduli':644,
            'ordered_modulus_pairs':644*644,
            'pairs_with_noop_collisions':count_pairs,
            'unordered_noop_witness_pairs_sum':count_witnesses
        },
        'p32_examples':examples,
        'mismatches':0,
        'claim':'author proof plus exhaustive stated finite validation'
    }


if __name__ == '__main__':
    print(json.dumps(validate(), ensure_ascii=False, indent=2))
