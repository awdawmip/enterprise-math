#!/usr/bin/env python3
"""Finite exact corroboration of signed-X6 native vs diagonal-observer BRC returns.
Independent author-side checker, not a replacement for the original signed_brc.py.
Standard library; integer-only arithmetic. Frozen mathematical input 59538f58...
"""
from collections import Counter
from functools import lru_cache
from math import factorial

D = 6
O = (0,) * D

@lru_cache(None)
def compositions(n, d):
    if d == 1:
        return ((n,),)
    return tuple((i,) + a for i in range(n + 1) for a in compositions(n - i, d - 1))


def exact_coefficient(n, k):
    """[x_1^k ... x_6^k](sum_i(x_i + x_i^-1))**n."""
    h = abs(k)
    if n < 6*h or (n - 6*h) % 2:
        return 0
    m = (n - 6*h) // 2
    return sum(factorial(n) //
               __import__('math').prod(factorial(v+h)*factorial(v) for v in a)
               for a in compositions(m, 6))


def enumerated_levels(max_length):
    z = Counter({O: 1})
    for n in range(max_length + 1):
        yield n, z
        if n < max_length:
            new = Counter()
            for p, count in z.items():
                for axis in range(D):
                    q = list(p); q[axis] += 1
                    new[tuple(q)] += count
                    q[axis] -= 2
                    new[tuple(q)] += count
            z = new


def main():
    rows = []
    checked = 0
    for n, dist in enumerated_levels(10):
        assert sum(dist.values()) == 12**n
        diag = {p[0]: count for p, count in dist.items() if len(set(p)) == 1}
        native = dist.get(O, 0)
        relative = sum(diag.values())
        assert native == exact_coefficient(n, 0)
        assert relative == sum(exact_coefficient(n, k) for k in range(-n//6-1, n//6+2))
        for k, count in diag.items():
            assert count == exact_coefficient(n, k)
            assert count == exact_coefficient(n, -k)
            checked += 2
        assert relative == native if n < 6 or n % 2 else relative > native
        rows.append((n, len(dist), native, relative, relative-native))
    assert rows[6][-1] == 1440
    assert rows[8][-1] == 241920
    print('PASS_X6_SIGNED_BRC_DIAGONAL_FIBER_EXACT')
    print('n,number_of_native_endpoints,native_return,relative_return,collision_mass')
    for r in rows: print(*r, sep=',')
    print('exact_integer_checks=', checked, 'first_difference_length=6')

if __name__ == '__main__':
    main()
