"""Finite, deterministic checks for the frozen 142-C auxiliary-prime definition."""
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt, prod


def prime_by_division(x):
    return x >= 2 and all(x % d for d in range(2, isqrt(x) + 1))


def sieve(n):
    a = bytearray(b'\1') * (n + 1)
    a[0:2] = b'\0\0'
    for d in range(2, isqrt(n) + 1):
        if a[d]:
            a[d*d::d] = b'\0' * (1 + (n - d*d)//d)
    return a


def first_two_joint():
    # First two candidates of each row; prime 73 occurs in both lists.
    lists = [[x for x in range(1+12*q, 150, 12*q) if prime_by_division(x)][:2]
             for q in (2, 3)]
    modulus = prod({x for row in lists for x in row})
    table = Counter()
    for b in range(1, modulus):
        if gcd(b, modulus) != 1:
            continue
        ranks = tuple(next((i for i, x in enumerate(row, 1)
                            if pow(b, (x-1)//q, x) != 1), 3)
                      for q, row in zip((2, 3), lists))
        table[ranks] += 1
    total = sum(table.values())
    def law(q, j):
        return Fraction(1, q*q) if j == 3 else Fraction(q-1, q**j)
    for (i, j), value in table.items():
        assert value == total * law(2, i) * law(3, j)
    return dict(modulus=modulus, lists=lists, units=total,
                rows_J2_columns_J3_last_means_gt2=[[table[i, j] for j in (1, 2, 3)]
                                                    for i in (1, 2, 3)])


def samples():
    n, X = 43, 100_000
    prime = sieve(2*X)
    qs = [q for q in range(2, n+1) if prime[q]]
    lists = {q: [x for x in range(1+12*q, 10_001, 12*q) if prime[x]]
             for q in qs}
    # Build q-th powers by direct image, independent of Euler's exponent test.
    symbols = {(q, x): {pow(b, q, x) for b in range(1, x)}
               for q in qs for x in lists[q][:10]}
    tallest, extras, maxnum = Counter(), Counter(), 0
    for p in range(X, 2*X):
        if not prime[p]:
            continue
        ranks = []
        for q in qs:
            for i, x in enumerate(lists[q], 1):
                hit = p != x and pow(p, (x-1)//q, x) != 1
                if (q, x) in symbols:
                    assert hit == (p % x != 0 and p % x not in symbols[q, x])
                if hit:
                    ranks.append(i)
                    maxnum = max(maxnum, x)
                    break
            else:
                raise AssertionError("insufficient candidate cutoff")
        tallest[max(ranks)] += 1
        extras[sum(ranks)-len(qs)] += 1
    return dict(interval=[X, 2*X], degree=n, rows=len(qs), input_primes=sum(tallest.values()),
                max_rank_counts=dict(sorted(tallest.items())),
                extra_prime_tests_counts=dict(sorted(extras.items())), maximum_ell=maxnum)


def quadratic_products():
    X, Y = 250_000, 480
    primes = sieve(2*X)
    full = [l for l in range(25, Y+1, 24) if primes[l]]
    block = [l for l in full if l > Y//2]
    products = [a*b for a, b in combinations(block, 2)]
    assert len(set(products)) == len(products) and max(products) <= X
    bad = [p for p in range(X, 2*X) if primes[p]
           and all(pow(p, (l-1)//2, l) == 1 for l in full)]
    assert bad and all(sum(1 if pow(d, (p-1)//2, p)==1 else -1
                           for d in products)==len(products) for p in bad)
    return dict(X=X, Y=Y, block=block, products=len(products),
                full_prefix=full, bad_primes=len(bad), first_bad=min(bad),
                last_bad=max(bad), maximum_product=max(products))


def capped_mersenne(max_ell):
    n, e = 43, 136_279_841
    B = 20+(n+1)*(e+1)
    assert e-1 > 200_000 * B.bit_length()
    rows, trials = [], 0
    for q in range(2, n+1):
        if not prime_by_division(q):
            continue
        j = 0
        for x in range(1+12*q, max_ell+1, 12*q):
            trials += 1
            if not prime_by_division(x):
                continue
            j += 1
            b = (pow(2, e, x)-1) % x
            test = pow(b, (x-1)//q, x)
            assert b and ((test != 1) == (b not in {pow(a, q, x) for a in range(1, x)}))
            if test != 1:
                rows.append([q, j, x, b, test])
                break
        else:
            rows.append([q, None])
    return dict(exponent=e, n=n, B=B, cap=max_ell, integer_candidates_examined=trials,
                rows_q_rank_ell_base_power=rows)


if __name__ == '__main__':
    print(json.dumps(dict(exact_CRT=first_two_joint(), prime_interval=samples(), quadratic_amplifier=quadratic_products(),
                          bounded_failure=capped_mersenne(500),
                          genuine_large_branch=capped_mersenne(10000)),
                     indent=2, sort_keys=True))
