"""Verify exact periods and count solutions for Erdős #1063. Python 3.10+.

P_k = lcm(1,...,k) lcm(1,...,floor(k/2)). This is the minimum period of
the full labelled failure set, and of the exactly-one predicate when k>=3.
The latter has period 1 for k=2. See the companion proof for minimality.
"""
from math import comb, factorial, isqrt, lcm

def primes_up_to(k):
    return [p for p in range(2, k+1) if all(p % i for i in range(2, isqrt(p)+1))]

def valuation(n, p):
    assert n > 0
    t = 0
    while n % p == 0:
        t += 1
        n //= p
    return t

def period(k):
    return lcm(*range(1, k+1)) * lcm(*range(1, k//2+1))

def local_table(k, p, repeats=1):
    """Masks indexed by n modulo the local period, using raw valuations."""
    modulus = p**valuation(period(k), p)
    n0 = ((2*k+modulus-1)//modulus)*modulus
    vals = [valuation(n, p) for n in range(n0-k+1, n0+modulus*repeats)]
    alpha = valuation(factorial(k), p)
    table = []
    for index in range(modulus*repeats):
        window = vals[index:index+k]
        excess = sum(window)-alpha
        table.append(sum(1 << i for i,v in enumerate(reversed(window)) if v > excess))
    return table

def density_numerator(k):
    columns = [1]*k
    empty = 1
    for p in primes_up_to(k):
        masks = local_table(k,p)
        zero = masks.count(0)
        columns = [c*(zero+masks.count(1<<i)) for i,c in enumerate(columns)]
        empty *= zero
    assert empty == 0
    return sum(columns)

def verify(local_max=80, direct_max=10):
    cases = observations = 0
    for k in range(2, local_max+1):
        for p in primes_up_to(k):
            table = local_table(k,p,2)
            q = len(table)//2
            assert table[:q] == table[q:]
            assert any(table[j] != table[j+q//p] for j in range(q))
            cases += 1
            observations += 2*q
    for k in range(2, direct_max+1):
        q = period(k)
        masks = []
        for n in range(2*k,2*k+q):
            b = comb(n,k)
            masks.append(sum(1<<i for i in range(k) if b%(n-i)))
        single = [m.bit_count()==1 for m in masks]
        assert sum(single) == density_numerator(k)
        for p in primes_up_to(k):
            shift = q//p
            assert any(masks[j] != masks[(j+shift)%q] for j in range(q))
            assert any(single[j] != single[(j+shift)%q] for j in range(q)) == (k!=2)
    print("verified", cases, "local cases,", observations,
          "local masks and all global residues for k=2..", direct_max)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--local-max',type=int,default=80)
    parser.add_argument('--direct-max',type=int,default=10)
    args = parser.parse_args()
    verify(args.local_max, args.direct_max)
