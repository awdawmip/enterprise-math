#!/usr/bin/env python3
"""PREFIX-887: exact odd-modulus axis-aligned collision classification.

No third-party dependencies. Uses exact integer arithmetic only.
All modulo comparisons include the modulus-one case.
"""
import json
from collections import Counter

P = 32
Q = (1 << 19) - 1


def factors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            out.append((d, e))
        d = 3 if d == 2 else d + 2
    if n > 1:
        out.append((n, 1))
    return out


def divisors(n):
    ds = [1]
    for prime, exponent in factors(n):
        old = ds[:]
        power = 1
        for _ in range(exponent):
            power *= prime
            ds.extend(power * x for x in old)
    return ds


def modular_classification(p, qmax):
    minus = set()
    plus = set()
    least_h = Counter()
    for q in range(1, qmax + 1, 2):
        r = 1 % q
        h0 = None
        for h in range(1, p):
            r = (2 * r) % q
            if r == 1 % q:
                minus.add(q)
                if h0 is None:
                    h0 = h
            if r == (-1) % q:
                plus.add(q)
                if h0 is None:
                    h0 = h
        if h0 is not None:
            least_h[h0] += 1
    return minus, plus, least_h


def divisor_classification(p, qmax):
    minus = set()
    plus = set()
    for h in range(1, p):
        minus.update(q for q in divisors((1 << h) - 1) if q <= qmax and q & 1)
        plus.update(q for q in divisors((1 << h) + 1) if q <= qmax and q & 1)
    return minus, plus


def brute_small(p, q):
    n = 1 << p
    trails = [(x, x) for x in range(n)]
    trails.extend((x, x ^ (1 << i)) for x in range(n) for i in range(p))
    vertical = set()
    horizontal = set()
    for x, y in trails:
        vertical.add((x % q, y))
        horizontal.add((x, y % q))
    return len(vertical) < len(trails), len(horizontal) < len(trails)


def check():
    minus, plus, least_h = modular_classification(P, Q)
    minus2, plus2 = divisor_classification(P, Q)
    assert minus == minus2 and plus == plus2, 'independent divisor census mismatch'
    a = minus | plus
    m = (Q + 1) // 2
    excluded = m * m - (m - len(a)) ** 2
    assert len(a) == 385
    assert (len(minus), len(plus), len(minus & plus)) == (304, 121, 40)
    assert excluded == 201702655
    small_checks = 0
    for p in range(2, 9):
        for q in range(1, min((1 << p), 31), 2):
            yes = any(pow(2, h, q) in (1 % q, (-1) % q) for h in range(1, p))
            vertical, horizontal = brute_small(p, q)
            assert vertical == yes and horizontal == yes, (p, q, vertical, horizontal, yes)
            small_checks += 1
    return {
        'model': 'named ordered XOR trails, 0 or one bit flip; two odd modular ports',
        'p': P, 'qmax': Q, 'odd_moduli': m, 'independently_equal_sets': True,
        'minus_count': len(minus), 'plus_count': len(plus),
        'both_count': len(minus & plus), 'axis_forcing_moduli': len(a),
        'axis_forcing_ordered_pairs': excluded,
        'remaining_outside_axis_criterion': (m - len(a)) ** 2,
        'total_ordered_pairs': m * m,
        'bruteforce_parameter_checks': small_checks,
        'least_exponent_histogram': {str(k): v for k, v in sorted(least_h.items())},
        'set_members_sorted': sorted(a),
        'all_checks': 'PASS',
        'status': 'exact finite arithmetic; not independent scientific review'
    }


if __name__ == '__main__':
    print(json.dumps(check(), ensure_ascii=False, indent=2, sort_keys=True))
