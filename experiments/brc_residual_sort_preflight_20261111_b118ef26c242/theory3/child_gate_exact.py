#!/usr/bin/env python3
"""Exact hypergeometric probabilities for two child-node gate settings."""
import csv
import sys
from fractions import Fraction
from math import comb


def tail(N, K, m, c):
    """Exact count of unordered uniform m-subsets with at least c misses."""
    lo = max(c, m-(N-K))
    hi = min(K, m)
    if lo > hi:
        return Fraction(0)
    ways = comb(K,lo)*comb(N-K,m-lo)
    total = ways
    for x in range(lo, hi):
        num = ways*(K-x)*(m-x)
        den = (x+1)*(N-K-m+x+1)
        ways, rem = divmod(num, den)
        assert rem == 0
        total += ways
    return Fraction(total, comb(N,m))


def result(n, F, e, m, margin):
    s = 1024
    N, t = n-s, n//2
    c = (m*t+N-1)//N + margin
    return c, tail(N,F-e,m,c)


def validate():
    from itertools import combinations
    for N in range(1, 9):
        for K in range(N+1):
            for m in range(N+1):
                x = [sum(i<K for i in subset) for subset in combinations(range(N),m)]
                for c in range(m+2):
                    assert tail(N,K,m,c) == Fraction(sum(v>=c for v in x),len(x))


def main():
    validate()
    n = 400_000
    totals = [n//2,n//2+1]+[n*p//100 for p in (51,52,53,54,55,56,57,58,60,70)]
    out = csv.writer(sys.stdout)
    out.writerow(["n","s","training_misses","total_misses","probe_size","margin",
                  "reject_at","p_trigger_given_complete"])
    for F in totals:
        for e in (0,512):
            for m,margin in ((64,13),(1024,42)):
                c,q = result(n,F,e,m,margin)
                out.writerow([n,1024,e,F,m,margin,c,f"{float(q):.12g}"])
    for small_n in (16384,65536,100000):
        for m,margin in ((64,13),(1024,42)):
            c,q = result(small_n,small_n//2,0,m,margin)
            out.writerow([small_n,1024,0,small_n//2,m,margin,c,f"{float(q):.12g}"])


if __name__ == "__main__":
    main()
