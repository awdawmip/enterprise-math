"""Exact bridge bounds and enumeration of small cylinders. Python 3 standard library."""
from fractions import Fraction
from itertools import combinations
from math import comb
import json


def cylinder(r, k, n, s):
    if n > r or s > k:
        return Fraction(0)
    return Fraction(comb(r+k-n-s, r-n), comb(r+k, r))


def sparse_bound(r, k):
    assert k+2 <= r+1+r//51
    return sum((comb(n+s-1, s)*cylinder(r, k, n, s)
                for s in range(34, k+1)
                for n in range(1, min(r, (51*s+102)//52)+1)), Fraction(0))


def cylinder_controls():
    checks = 0
    for r in range(1, 8):
        for k in range(0, 7):
            N = r+k
            words = []
            for indices in combinations(range(N), k):
                fives = set(indices)
                words.append(''.join('5' if i in fives else 'B' for i in range(N)))
            counts = {}
            for word in words:
                for i, sym in enumerate(word):
                    if sym == 'B':
                        prefix = word[:i+1]
                        counts[prefix] = counts.get(prefix, 0)+1
            for prefix, size in counts.items():
                assert Fraction(size,len(words)) == cylinder(r,k,prefix.count('B'),prefix.count('5'))
                checks += 1
    return checks


def main():
    bounds = []
    for r,k in [(900,100),(950,50),(966,34),(1000,33)]:
        val = sparse_bound(r,k)
        bounds.append(dict(r=r,c=k+2,k=k,exact=str(val),rounded_display=f'{float(val):.9e}'))
    output = dict(cylinder_checks=cylinder_controls(),upper_bounds=bounds)
    print(json.dumps(output,indent=2))


if __name__ == '__main__':
    main()
