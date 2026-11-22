#!/usr/bin/env python3
"""Finite-field root-obstruction witnesses for 43-jet infinite progressions.
The polynomial-in-h degree <=1 and tail factorization are proved in EXTENSION_D43_ALL_M.md;
this script certifies the required characteristic-zero nonvanishing by two
Galois-conjugate residues of one prime field, with integer modular arithmetic.
"""
from itertools import permutations

P = 1033
ROOTS = (995, 411)  # 411 == 995**2 mod 1033, both primitive order 43
MAX_M = 259
ZERO, ONE = (0, 0), (1, 0)


def add(a, b):
    return ((a[0] + b[0]) % P, (a[1] + b[1]) % P)


def sub(a, b):
    return ((a[0] - b[0]) % P, (a[1] - b[1]) % P)


def mul(a, b):
    return (a[0] * b[0] % P, (a[0] * b[1] + a[1] * b[0]) % P)


def inv(a):
    v = pow(a[0], -1, P)
    return v, -a[1] * v * v % P


def compute(root):
    def qpow(k):
        x = pow(root, k % 43, P)
        return x, k * x % P

    def inv_factor(seq, c, step):
        seq = seq.copy()
        for idx in range(step, MAX_M):
            seq[idx] = add(seq[idx], mul(c, seq[idx - step]))
        return seq

    def prod_d(prices):
        d = ONE
        for x in prices:
            d = mul(d, sub(ONE, qpow(x)))
        return d

    # True total-items block for Z={296,...,312}, including its exact first jet.
    c = [ZERO] * MAX_M
    c[0] = prod_d(range(296, 313))
    c = inv_factor(c, ONE, 1)
    for x in range(296, 313):
        c = inv_factor(c, qpow(x), 1)

    # Full three-overlap union via the six disjoint integer cones.
    a = [ZERO] * MAX_M
    for r in (219, 220, 221):
        beta = ONE
        for rp in (219, 220, 221):
            if rp != r:
                beta = mul(beta, inv(sub(ONE, qpow(rp - r))))
        for x, y, z in permutations((214, 215, r)):
            d1, d2 = int(x > y), int(y > z)
            pre = beta
            for p in range(214, 222):
                if p != x:
                    pre = mul(pre, sub(ONE, qpow(p)))
            if d1:
                pre = mul(pre, qpow(x))
            if d2:
                pre = mul(pre, qpow(x + y))
            t = [ZERO] * MAX_M
            t[d2] = pre
            for pp, st in ((0, 1), (216, 1), (217, 1), (218, 1),
                           (x + y, 1), (x + y + z, 2)):
                t = inv_factor(t, ONE if pp == 0 else qpow(pp), st)
            a = [add(u, v) for u, v in zip(a, t)]

    values = {}
    for parity in (0, 1):
        for r in range(37, 44):
            jets = []
            for h in (0, 1, 2):
                m = r + 43 * parity + 86 * h
                assert a[m - 1][0] == c[m - 1][0] == 0
                assert c[m - 1][1] == (-43 * 301 * (1 + parity + 2 * h)) % P
                jets.append((a[m - 1][1] + c[m - 1][1]) % P)
            constant, slope = jets[0], (jets[1] - jets[0]) % P
            assert (jets[2] - 2 * jets[1] + jets[0]) % P == 0
            assert constant and slope
            root_h = (-constant * pow(slope, -1, P)) % P
            values[(r, parity)] = (constant, slope, root_h)
    return values


def main():
    assert all(z != 1 and pow(z, 43, P) == 1 for z in ROOTS)
    v, w = (compute(z) for z in ROOTS)
    print('r,parity,a_z,b_z,root_h_z,a_z2,b_z2,root_h_z2,method')
    mixed, factored = 0, 0
    for parity in (0, 1):
        for r in range(37, 44):
            x, y = v[(r, parity)], w[(r, parity)]
            if parity == 1 and r >= 39:
                assert x[0] == x[1] and y[0] == y[1]
                # Proven analytically: exact f(h)=(h+1)*f(0), h>=0.
                method = 'analytic_h_plus_one'
                factored += 1
            else:
                assert x[2] != y[2]
                # Both conjugate reductions would vanish for a char-zero integer root.
                method = 'disjoint_conjugate_roots'
                mixed += 1
            print(f'{r},{parity},{*x,*y,method}'
                  .replace('(', '').replace(')', '').replace(' ', ''))
    assert (mixed, factored) == (9, 5)
    print('ALL CHECKS PASS: 9 disjoint-root and 5 analytic-factor progressions')


if __name__ == '__main__':
    main()
