#!/usr/bin/env python3
"""Exact author-side check for the observational fibre in R5 two-gate example.

All chance weights, rewards and policy vectors are rational. 128 FULL and
8 seedless LR deterministic policies are enumerated for each of four pairs.
All-real statements in RESEARCH.md are algebraic proofs, not claims based on
these finite enumerations.
"""
from fractions import Fraction as F
from itertools import product

R = (F(1), F(3, 2), F(2), F(3))
D = F(1, 8)


def kernel(ell):
    return (F(1, 4), ell, F(1, 2) - F(3, 2) * ell,
            F(1, 4) + ell / 2)


def check_kernel(ell):
    assert 0 < ell < F(1, 3)
    k = kernel(ell)
    assert all(v > 0 for v in k)
    assert sum(k) == 1
    assert sum(p * r for p, r in zip(k, R)) == 2
    assert sum(p * r / 2 for p, r in zip(k, R)) == 1
    return k


def observe(ell0, ell1, a):
    x0, x1, u0, u1, ub, z0, z1 = a
    ks = [check_kernel(ell0), check_kernel(ell1)]
    out = []
    for law in ('P', 'Q'):
        err = tm = F(0)
        for i, (x, u) in enumerate(((x0, u0), (x1, u1))):
            mass = F(1, 4) if law == 'P' else F(1, 8)
            if not x:
                err += mass * D
                tm += mass
            else:
                for j, q in enumerate(ks[i]):
                    prob = mass * (q * R[j] / 2 if law == 'P' else q)
                    t = (2 if u else 3) if j == 0 else 3
                    err += prob * D
                    tm += prob * t
        mass_b = F(1, 4)
        err += mass_b * (F(5, 8) if ub else D)
        tm += mass_b * (2 if ub else 3)
        for z in (z0, z1):
            mass_c = F(1, 8) if law == 'P' else F(1, 4)
            err += mass_c * (D if z else F(5, 8))
            tm += mass_c * (3 if z else 1)
        out.append((err, tm))
    return (out[0][0], out[1][0], out[0][1], out[1][1])


def expected(a):
    x0, x1, u0, u1, ub, z0, z1 = a
    x, z = F(x0 + x1, 2), F(z0 + z1, 2)
    w = F(x0 * u0 + x1 * u1, 2)
    s = F(ub, 4) + w / 16
    return (D + F(ub, 8) + (1 - z) / 8,
            D + F(ub, 8) + (1 - z) / 4,
            F(3, 2) + x + z / 2 - s,
            F(3, 2) + x / 2 + z - s)


def h(v):
    e_p, e_q, t_p, t_q = v
    return 14 * e_p - 19 * e_q + 2 * t_p - 4 * t_q


def determinant(columns):
    n = len(columns)
    m = [[columns[j][i] for j in range(n)] for i in range(n)]
    det = F(1)
    for j in range(n):
        pivot = next(k for k in range(j, n) if m[k][j])
        if pivot != j:
            m[j], m[pivot] = m[pivot], m[j]
            det = -det
        piv = m[j][j]
        det *= piv
        for i in range(j + 1, n):
            fac = m[i][j] / piv
            for k in range(j, n):
                m[i][k] -= fac * m[j][k]
    return det


def main():
    all_full = list(product((0, 1), repeat=7))
    all_lr = [(x, x, u, u, u, z, z)
              for x, u, z in product((0, 1), repeat=3)]
    assert len(all_full) == 128 and len(all_lr) == 8
    choices = [(F(1, 12), F(1, 6)),
               (F(1, 6), F(1, 6)),
               (F(1, 24), F(7, 24)),
               (F(1, 1000), F(1, 3) - F(1, 1000))]
    base_full = base_lr = None
    for ell0, ell1 in choices:
        full = [observe(ell0, ell1, a) for a in all_full]
        lr = [observe(ell0, ell1, a) for a in all_lr]
        assert all(v == expected(a) for v, a in zip(full, all_full))
        assert all(v == expected(a) for v, a in zip(lr, all_lr))
        if base_full is None:
            base_full, base_lr = full, lr
        assert full == base_full and lr == base_lr
        gap = max(map(h, full)) - max(map(h, lr))
        assert max(map(h, full)) == F(-13, 2)
        assert max(map(h, lr)) == F(-53, 8)
        assert gap == F(1, 8)
        tv = sum(abs(x - y) for x, y in zip(kernel(ell0), kernel(ell1))) / 2
        assert tv == F(3, 2) * abs(ell0 - ell1)
        print(f'ell0={ell0} ell1={ell1} TV={tv} FULL={len(full)} '
              f'LR={len(lr)} support_gap={gap}')
    X = (F(0), F(0), F(1), F(1, 2))
    U = (F(1, 8), F(1, 8), F(-1, 4), F(-1, 4))
    Z = (F(-1, 8), F(-1, 4), F(1, 2), F(1))
    W = (F(0), F(0), F(-1, 16), F(-1, 16))
    assert determinant([X, U, Z, W]) == F(1, 2048)
    midpoint = tuple((a + b) / 2 for a, b in zip(
        expected((0, 0, 0, 0, 0, 0, 0)),
        expected((1, 1, 1, 1, 1, 0, 0))))
    assert midpoint == (F(5, 16), F(7, 16), F(59, 32), F(51, 32))
    # A legitimate FULL behavioural witness; uB=1/2 is not deterministic.
    witness = expected((1, 0, 1, 0, F(1, 2), 0, 0))
    assert witness == midpoint
    print(f'rank_det={determinant([X, U, Z, W])} midpoint={midpoint}')
    print('PASS_EXACT_R5_OBSERVER_FIBRE_RESIDUAL_RANGE_AND_FIXED_GAP')


if __name__ == '__main__':
    main()
