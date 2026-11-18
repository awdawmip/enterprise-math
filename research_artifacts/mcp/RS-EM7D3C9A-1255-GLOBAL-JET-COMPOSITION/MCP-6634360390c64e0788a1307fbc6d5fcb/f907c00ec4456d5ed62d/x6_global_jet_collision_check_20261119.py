#!/usr/bin/env python3
"""Exact integer subsequence-signature collision check for U_n,V_n, 1<=n<=6."""
from collections import Counter

def words(n):
    u, v = 'A', 'B'
    for _ in range(n):
        u, v = u + v, v + u
    return u, v

def signature(word, max_degree):
    levels = [Counter() for _ in range(max_degree + 1)]
    levels[0][''] = 1
    for letter in word:
        for k in range(max_degree, 0, -1):
            for monomial, multiplicity in list(levels[k-1].items()):
                levels[k][monomial + letter] += multiplicity
    return levels

def main():
    for n in range(1, 7):
        u, v = words(n)
        assert len(u) == len(v) == 2 ** n and u != v
        su, sv = signature(u, n+1), signature(v, n+1)
        assert all(su[k] == sv[k] for k in range(n+1))
        assert su[n+1] != sv[n+1]
        print(f'n={n} length={len(u)} jet<=n COLLISION; jet_(n+1) separates')

if __name__ == '__main__':
    main()