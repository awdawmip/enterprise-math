#!/usr/bin/env python3
"""Exact finite A216 character diagnostic; never a universal proof or native run."""
from math import comb

def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))

def test_bound(bound=500):
    counts = {i: 0 for i in [1, 5, 7, 11, 13, 17, 19, 23]}
    examples = []
    for p in range(5, bound):
        if not is_prime(p):
            continue
        modulus = p**3
        total = sum(
            (6*n+1)*comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,modulus)
            for n in range(p)
        ) % modulus
        expected = (p if p % 3 == 1 else -p) % modulus
        assert total == expected, (p,total,expected)
        counts[p%24] += 1
        if p in (5,7,11,13,19,23,31,373,499):
            examples.append((p,p%24,total,expected))
    print("PASS_FINITE_A216_P3_CHARACTER_DIAGNOSTIC",sum(counts.values()),"primes 5<=p<",bound)
    print("RESIDUE_CLASS_COUNTS",counts)
    print("WITNESSES",examples)

if __name__ == "__main__":
    test_bound(500)
