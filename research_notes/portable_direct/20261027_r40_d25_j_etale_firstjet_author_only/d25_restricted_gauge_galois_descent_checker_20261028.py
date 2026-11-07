#!/usr/bin/env python3
"""Exact author-side checker for restricted-scalar-gauge Galois descent.

Finite fields are represented as F_p[t]/(f), using a monic irreducible f
found by exact monic-factor trial division. No external packages/randomness.
"""
from itertools import product
from math import gcd
import json


def coeffs(v, p, n):
    a = []
    for _ in range(n):
        a.append(v % p)
        v //= p
    return a


def encode(a, p):
    return sum(x * p ** i for i, x in enumerate(a))


def poly_divisible(f, h, p):
    z = list(f)
    for j in range(len(z) - len(h), -1, -1):
        c = z[j + len(h) - 1]
        if c:
            for i, b in enumerate(h):
                z[i + j] = (z[i + j] - c * b) % p
    return not any(z[:len(h) - 1])


def find_irreducible(p, e):
    if e == 1:
        return (0, 1)
    for low in product(range(p), repeat=e):
        if low[0] == 0:
            continue
        f = tuple(low) + (1,)
        if all(not poly_divisible(f, tuple(g) + (1,), p)
               for a in range(1, e // 2 + 1)
               for g in product(range(p), repeat=a)):
            return f
    raise AssertionError('irreducible polynomial not found')


class Field:
    def __init__(self, p, e):
        self.p, self.e, self.q = p, e, p ** e
        self.modulus = find_irreducible(p, e)
        self.vectors = [coeffs(i, p, e) for i in range(self.q)]

    def mul(self, u, v):
        p, e = self.p, self.e
        a, b = self.vectors[u], self.vectors[v]
        c = [0] * (2 * e - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                c[i+j] = (c[i+j] + x*y) % p
        for k in range(2*e-2, e-1, -1):
            z = c[k]
            if z:
                for j in range(e):
                    c[k-e+j] = (c[k-e+j] - z*self.modulus[j]) % p
        return encode(c[:e], p)

    def power(self, a, n):
        z = 1
        while n:
            if n & 1:
                z = self.mul(z, a)
            n >>= 1
            if n:
                a = self.mul(a, a)
        return z

    def scale(self, v, z):
        return encode([(z * x) % self.p for x in self.vectors[v]], self.p)


def one_case(p, e, r, d):
    F = Field(p, e)
    scalars = tuple(z for z in range(1, p) if pow(z, d, p) == 1)
    assert len(scalars) == d and (p-1) % d == 0
    # This is a finite exhaustive quotient: all vectors, all H elements.
    canon = lambda vec: min(tuple(F.scale(x, z) for x in vec) for z in scalars)
    reps = set(canon(v) for v in product(range(F.q), repeat=r))
    assert len(reps) == 1 + (p ** (e*r) - 1) // d
    # One Frobenius table per exponent, not per state.
    Frob = [[F.power(x, p**j) for x in range(F.q)] for j in range(e)]
    fixed = []
    fixed_naive = []
    for j in range(e):
        g = gcd(e, j)
        h = gcd(d, e // g)
        want = 1 + h * (p**(g*r) - 1) // d
        got = sum(canon(tuple(Frob[j][x] for x in v)) == v for v in reps)
        assert got == want, (p,e,r,d,j,got,want)
        fixed.append(got)
        fixed_naive.append(1 + (p**(g*r)-1)//d)
    assert sum(fixed) % e == 0
    # Independent orbit traversal of the permutation sigma on H-orbits.
    visited = set()
    num_semilinear = 0
    for v in reps:
        if v in visited:
            continue
        num_semilinear += 1
        cur = v
        while cur not in visited:
            visited.add(cur)
            cur = canon(tuple(Frob[1][x] for x in cur)) if e > 1 else v
        assert cur == v
    assert len(visited) == len(reps)
    assert num_semilinear == sum(fixed)//e
    return {
        'p':p,'e':e,'r':r,'d':d,'q':F.q,
        'field_modulus_low_to_high':list(F.modulus),
        'all_source_vectors':F.q**r,'linear_H_orbits':len(reps),
        'Frobenius_fixed_H_orbits_by_j':fixed,
        'naive_subfield_H_orbits_by_j':fixed_naive,
        'semilinear_H_orbits':num_semilinear,
        'semilinear_orbits_naive_descent_average':sum(fixed_naive)/e,
        'pass':True,
    }


def main():
    cases = [
        (3,1,2,2),(3,2,1,2),(3,2,2,2),(3,3,2,2),(3,4,2,2),
        (5,2,1,2),(5,2,2,2),(5,2,2,4),(5,3,2,2),(5,3,2,4),
        (7,2,2,2),(7,2,2,3),(7,2,2,6),
        (11,2,2,2),(11,2,2,5),(11,2,2,10),
        (2,3,2,1),
    ]
    out = [one_case(*case) for case in cases]
    p = 373
    assert p%8 == 5  # 2 is a nonsquare: t^2=2 gives F_(p^2)
    native = {
        'p':p,'e':2,'r':2,'d':2,
        'ambient_vectors':p**4,
        'linear_H_orbits':(p**4+1)//2,
        'Frobenius_fixed_H_orbits':p**2,
        'naive_subfield_H_orbits':(p**2+1)//2,
        'extra_Frobenius_fixed_no_Fp_representative':(p**2-1)//2,
        'semilinear_H_orbits':(p**2+1)**2//4,
        'naive_descent_average':((p**4+1)//2+(p**2+1)//2)//2,
        'actual_minus_naive':(p**2-1)//4,
        'explicit_witness':{'extension':'F_373[t]/(t^2-2)',
           'source_pair':['t','t'],'frobenius_pair':['-t','-t'],
           'source_product':'2','F_373_comparison_pair':['1','2'],
           'source_marked_H_equivalent':False,
           'full_GL1xGL1_equivalent':True},
    }
    # Check all exact arithmetic in the closed-form p=373 row.
    assert native['semilinear_H_orbits']==(native['linear_H_orbits']+p**2)//2
    assert native['actual_minus_naive']==native['semilinear_H_orbits']-native['naive_descent_average']
    output = {
        'title':'restricted scalar gauge Galois descent counterexample and exact fixed-orbit theorem',
        'method':'exact polynomial quotient finite fields; exhaustive H orbits and Frobenius orbit traversal',
        'status':'AUTHOR_EXACT_CHECKED_UNREVIEWED_NOT_NATIVE',
        'cases':out,
        'total_test_vectors_counted_across_cases':sum(c['all_source_vectors'] for c in out),
        'all_checks_pass':True,
        'conditional_p373_analytical_row':native,
    }
    print(json.dumps(output,indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()