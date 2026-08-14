#!/usr/bin/env python3
"""Exact finite checks for the weighted pair/Toda BRC checkpoint.

This verifies finite algebra and conservative rational arithmetic only.
It is not a proof of RH.
"""
from fractions import Fraction


def det_frac(matrix):
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
    return sign * a[-1][-1]


def elementary_from_roots(roots, nmax):
    e = [Fraction(0)] * (nmax + 1)
    e[0] = Fraction(1)
    for x in roots:
        for n in range(nmax, 0, -1):
            e[n] += x * e[n - 1]
    return e


def convolve(a, b, nmax):
    out = [Fraction(0)] * (nmax + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= nmax:
                out[i + j] += x * y
    return out


def toeplitz_minor(seq, r, k):
    if r == 0:
        return Fraction(1)

    def get(n):
        if n < 0 or n >= len(seq):
            return Fraction(0)
        return seq[n]

    return det_frac([[get(k + j - i) for j in range(r)] for i in range(r)])


def complete_from_elementary(e, nmax):
    # H(z) E(-z) = 1.
    h = [Fraction(0)] * (nmax + 1)
    h[0] = Fraction(1)
    for n in range(1, nmax + 1):
        total = Fraction(0)
        for j in range(1, min(n, len(e) - 1) + 1):
            total += ((-1) ** j) * e[j] * h[n - j]
        h[n] = -total
    return h


def normalize_partition(p):
    return tuple(x for x in p if x > 0)


def partitions(max_size, max_width):
    out = [()]

    def rec(rem, last, cur):
        for x in range(min(rem, last, max_width), 0, -1):
            nxt = cur + (x,)
            out.append(nxt)
            rec(rem - x, x, nxt)

    rec(max_size, max_width, ())
    return list(dict.fromkeys(out))


def conjugate(lam):
    if not lam:
        return ()
    return tuple(sum(1 for x in lam if x >= j) for j in range(1, lam[0] + 1))


def subset(mu, lam):
    return len(mu) <= len(lam) and all(mu[i] <= lam[i] for i in range(len(mu)))


def horizontal_strip(lam, mu, size):
    if not subset(mu, lam) or sum(lam) - sum(mu) != size:
        return False
    lc, mc = conjugate(lam), conjugate(mu)
    return all(
        lc[j] - (mc[j] if j < len(mc) else 0) in (0, 1)
        for j in range(len(lc))
    )


def hget(h, n):
    return Fraction(0) if n < 0 or n >= len(h) else h[n]


def schur_from_h(lam, h):
    lam = normalize_partition(lam)
    ell = len(lam)
    if ell == 0:
        return Fraction(1)
    return det_frac([[hget(h, lam[i] - i + j) for j in range(ell)] for i in range(ell)])


def skew_schur_from_h(lam, mu, h):
    lam = normalize_partition(lam)
    mu = normalize_partition(mu)
    if not subset(mu, lam):
        return Fraction(0)
    ell = len(lam)
    mup = mu + (0,) * (ell - len(mu))
    return det_frac(
        [[hget(h, lam[i] - mup[j] - i + j) for j in range(ell)] for i in range(ell)]
    )


def partitions_inside(lam):
    lam = normalize_partition(lam)
    out = []

    def rec(i, prev, cur):
        if i == len(lam):
            out.append(normalize_partition(cur))
            return
        for v in range(min(prev, lam[i]), -1, -1):
            rec(i + 1, v, cur + (v,))

    rec(0, 10**9, ())
    return list(dict.fromkeys(out))


def test_first_unsafe_pair_and_toda():
    # Y has generating factor 1+z+z^2: R=1, theta=pi/3.
    # h_0..h_6 = 1,1,0,-1,-1,0,1, so r=3 is the first negative h_r.
    pair_e = [Fraction(1), Fraction(1), Fraction(1)]
    pair_h = complete_from_elementary(pair_e, 8)
    assert pair_h[:7] == [1, 1, 0, -1, -1, 0, 1]

    r = 3
    roots = [
        Fraction(1, 2),
        Fraction(1, 3),
        Fraction(1, 5),
        Fraction(1, 7),
        Fraction(1, 11),
        Fraction(1, 13),
    ]
    a_x = elementary_from_roots(roots, 20)
    a_xy = convolve(a_x, pair_e, 20)

    for k in range(1, 5):
        actual = toeplitz_minor(a_xy, r, k)
        lower = (
            toeplitz_minor(a_x, r, k)
            + toeplitz_minor(a_x, r, k - 1) * pair_h[r]
        )
        assert actual >= lower

    for k in range(1, 4):
        dm = toeplitz_minor(a_x, r, k - 1)
        d0 = toeplitz_minor(a_x, r, k)
        dp = toeplitz_minor(a_x, r, k + 1)
        p_k = dm / d0
        p_k1 = d0 / dp
        q = dm * dp / (d0 * d0)
        assert p_k / p_k1 == q

    h_x = complete_from_elementary(a_x, r)
    assert toeplitz_minor(a_x, r, 1) == h_x[r]


def test_top_row_drop():
    for r in range(1, 6):
        states = partitions(14, r)
        for lam in states:
            predecessors = [mu for mu in states if horizontal_strip(lam, mu, r)]
            expected = [lam[1:]] if lam and lam[0] == r else []
            assert predecessors == expected, (r, lam, predecessors, expected)


def test_three_pair_majorant():
    pair_e = [Fraction(1), Fraction(1), Fraction(1)]
    pair_h = complete_from_elementary(pair_e, 20)
    eta = Fraction(1)

    r, k, m_pairs = 3, 4, 3
    roots = [
        Fraction(1, 2),
        Fraction(1, 3),
        Fraction(1, 5),
        Fraction(1, 7),
        Fraction(1, 11),
        Fraction(1, 13),
    ]
    a_x = elementary_from_roots(roots, 30)
    h_x = complete_from_elementary(a_x, 30)

    target = (r,) * k
    states = partitions_inside(target)
    f = {mu: schur_from_h(mu, h_x) for mu in states}

    def apply_positive_majorant(state):
        out = {}
        for lam in states:
            total = Fraction(0)
            for mu in states:
                if not subset(mu, lam):
                    continue
                coeff = skew_schur_from_h(lam, mu, pair_h)
                if horizontal_strip(lam, mu, r):
                    coeff += eta
                assert coeff >= 0
                total += state[mu] * coeff
            out[lam] = total
        return out

    F = f
    for _ in range(m_pairs):
        F = apply_positive_majorant(F)

    pair_power = [Fraction(1)]
    for _ in range(m_pairs):
        pair_power = convolve(pair_power, pair_e, 30)
    actual_seq = convolve(a_x, pair_power, 30)
    actual = toeplitz_minor(actual_seq, r, k)

    lower = F[target]
    lower -= 3 * eta * F[(r,) * (k - 1)]
    lower -= eta**3 * F[(r,) * (k - 3)]
    assert actual >= lower


def test_boundary_zero_count_arithmetic():
    endpoint_error = (
        Fraction(10076, 100000) * 29
        + Fraction(24460, 100000) * 4
        + Fraction(808292, 100000)
    )
    main_increment = Fraction(2, 5) * Fraction(29, 6)
    total = 2 * endpoint_error + main_increment
    assert total < 26
    assert 25 // 2 == 12


def main():
    test_first_unsafe_pair_and_toda()
    test_top_row_drop()
    test_three_pair_majorant()
    test_boundary_zero_count_arithmetic()
    print("weighted pair/Toda exact checks: PASS")
    print("top-row-drop exhaustive small-state check: PASS")
    print("three-pair majorant exact check: PASS")
    print("first-boundary off-line pair cap: 12")
    print("RH status: NOT_CLOSED")


if __name__ == "__main__":
    main()
