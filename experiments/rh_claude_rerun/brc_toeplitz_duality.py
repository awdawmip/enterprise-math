#!/usr/bin/env python3
"""Exact finite checks for the RH BRC constructive rerun.

This file does not prove RH. It verifies the finite algebraic identities used by
BRC_CONSTRUCTIVE_RERUN.md on exact rational test sequences.
"""
from fractions import Fraction
from random import Random


def det_frac(matrix):
    """Bareiss determinant over Fractions."""
    a = [list(map(Fraction, row)) for row in matrix]
    n = len(a)
    if n == 0:
        return Fraction(1)
    sign = 1
    prev = Fraction(1)
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if swap is None:
                return Fraction(0)
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) / prev
        prev = pivot
    return sign * a[n - 1][n - 1]


def seq_get(seq, n):
    return Fraction(0) if n < 0 else seq[n]


def toeplitz_minor(seq, r, k):
    if r == 0:
        return Fraction(1)
    return det_frac([[seq_get(seq, k + j - i) for j in range(r)] for i in range(r)])


def reciprocal_elementary(a, nmax):
    """e_n from E(z) A(-z)=1, assuming a_0=1."""
    assert a[0] == 1
    e = [Fraction(0)] * (nmax + 1)
    e[0] = Fraction(1)
    for n in range(1, nmax + 1):
        s = Fraction(0)
        for j in range(1, n + 1):
            aj = a[j] if j < len(a) else Fraction(0)
            s += ((-1) ** j) * aj * e[n - j]
        e[n] = -s
    return e


def check_rectangular_duality(a, rmax=4, kmax=4):
    e = reciprocal_elementary(a, rmax + kmax + 4)
    for r in range(1, rmax + 1):
        for k in range(1, kmax + 1):
            lhs = toeplitz_minor(a, r, k)
            rhs = toeplitz_minor(e, k, r)
            if lhs != rhs:
                raise AssertionError(("duality", r, k, lhs, rhs))


def check_dodgson(a, rmax=5, kmax=5):
    for r in range(2, rmax + 1):
        for k in range(1, kmax + 1):
            lhs = toeplitz_minor(a, r, k) * toeplitz_minor(a, r - 2, k)
            rhs = (
                toeplitz_minor(a, r - 1, k) ** 2
                - toeplitz_minor(a, r - 1, k - 1) * toeplitz_minor(a, r - 1, k + 1)
            )
            if lhs != rhs:
                raise AssertionError(("dodgson", r, k, lhs, rhs))


def check_q_dynamics(a, rmax=4, kmax=4):
    def d(r, k):
        return toeplitz_minor(a, r, k)

    def q(r, k):
        return d(r, k - 1) * d(r, k + 1) / (d(r, k) ** 2)

    for r in range(2, rmax + 1):
        for k in range(1, kmax + 1):
            # Every q used below must have a nonzero denominator.
            denominator_cells = [
                (r - 1, k),
                (r, k - 1),
                (r, k),
                (r, k + 1),
                (r + 1, k),
            ]
            if any(d(rr, kk) == 0 for rr, kk in denominator_cells):
                continue
            qrm1 = q(r - 1, k)
            qrk = q(r, k)
            if qrm1 == 0 or qrk == 1:
                continue
            lhs = q(r + 1, k)
            rhs = (
                qrk**2 / qrm1
                * (1 - q(r, k - 1))
                * (1 - q(r, k + 1))
                / (1 - qrk) ** 2
            )
            if lhs != rhs:
                raise AssertionError(("q-dynamics", r, k, lhs, rhs))


def synthetic_sequences():
    rng = Random(20260811)
    out = []
    for _ in range(20):
        # a_0=1 and enough exact nonzero rational coefficients for all windows.
        a = [Fraction(1)]
        for _n in range(1, 16):
            a.append(Fraction(rng.randint(1, 19), rng.randint(1, 17)))
        out.append(a)
    return out


def region_class(r, k, r_verified=10, cubic_constant=100):
    if k == 0:
        return "K0_EXACT"
    if r <= r_verified:
        return "LOW_ORDER_SECTOR"
    if k >= cubic_constant * r**3:
        return "CUBIC_TAIL"
    return "CRITICAL_UNRESOLVED"


def check_region_partition():
    counts = {}
    k_limit = 200000
    for r in range(1, 25):
        for k in range(k_limit):
            c = region_class(r, k)
            counts[c] = counts.get(c, 0) + 1
    assert sum(counts.values()) == 24 * k_limit
    assert counts["K0_EXACT"] == 24
    assert counts["LOW_ORDER_SECTOR"] > 0
    assert counts["CUBIC_TAIL"] > 0
    assert counts["CRITICAL_UNRESOLVED"] > 0
    return counts


def main():
    for a in synthetic_sequences():
        check_rectangular_duality(a)
        check_dodgson(a)
        check_q_dynamics(a)
    counts = check_region_partition()
    print("exact rational identity checks: PASS")
    print("synthetic sequences checked: 20")
    print("region partition counts:", counts)
    print("RH status: NOT_CLOSED")


if __name__ == "__main__":
    main()
