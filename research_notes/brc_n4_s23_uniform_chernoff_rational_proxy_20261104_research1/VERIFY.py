#!/usr/bin/env python3
"""Exact rational interval audit for a *uniform analytic* Chernoff proxy theorem.
No binary floating point, optimization libraries, or assumed optimizer values.
The proof of the full real domain is analytic in PROOF.md; this script checks
exact special cases, the closed-form envelope, and strict series enclosures.
"""
from fractions import Fraction as Q


def atanh_bounds(x, n=16):
    assert Q(0) <= x < 1
    if x == 0:
        return Q(0), Q(0)
    t = sum((x ** (2*j+1)) / (2*j+1) for j in range(n))
    r = x ** (2*n+1) / ((2*n+1)*(1-x*x))
    return t, t+r


def log1p_bounds(u, n=18):
    assert Q(0) <= u < 1
    def part(m):
        return sum(((-1)**(j+1))*u**j/Q(j) for j in range(1, m+1))
    a, b = part(n), part(n+1)
    return min(a, b), max(a, b)


def log1m_bounds(x, n=18):
    assert Q(0) <= x < 1
    t = sum(x**j/Q(j) for j in range(1, n+1))
    rem = x**(n+1)/((n+1)*(1-x))
    return -t-rem, -t


def phi_bounds(x):
    """Rigorous interval for log(sqrt(1-x^2)*atanh(x)/x)."""
    assert Q(0) <= x <= Q(1,21)
    if x == 0:
        return Q(0), Q(0)
    a, b = atanh_bounds(x)
    lo, _ = log1p_bounds(a/x-1)
    _, hi = log1p_bounds(b/x-1)
    c, d = log1m_bounds(x*x)
    return lo+c/2, hi+d/2


def delta_bounds(v, k):
    assert Q(0) < v <= Q(1,21) and Q(0) <= k <= 1
    if k == 1:
        return Q(0), Q(0)
    p1, p2 = phi_bounds(k*v)
    q1, q2 = phi_bounds(v)
    a, b = atanh_bounds(v)
    c, d = atanh_bounds(k*v)
    lower_num, upper_num = p1-q2, p2-q1
    assert lower_num > 0
    return lower_num/(b+d), upper_num/(a+c)


def closed_bound(v):
    return v**8*(2-v*v)**2/(288*(1-v*v)**6)


def main():
    v_max = Q(1,21)
    top_delta = v_max/(6*(1-v_max*v_max)**2)
    global_error = closed_bound(v_max)
    assert top_delta == Q(3087,387200) and top_delta < Q(1,125)
    assert global_error == Q(776161,2089818390528000000)
    assert global_error < Q(4,10**13)

    checked = 0
    max_width = Q(0)
    for v in (Q(1,21), Q(1,28), Q(1,42), Q(1,84)):
        for k in (Q(0), Q(1,19), Q(1,5), Q(1,2), Q(9,10), Q(1)):
            lo, hi = delta_bounds(v, k)
            d0 = (1-k)*v/6
            lower = d0*(1-v*v)
            upper = d0/(1-v*v)**2
            assert lower <= lo <= hi <= upper
            assert Q(0) <= lo <= hi < Q(1,125)
            assert closed_bound(v) <= global_error
            max_width = max(max_width, hi-lo)
            checked += 1
    assert checked == 24
    print('exact rational optimizer interval checks:', checked)
    print('global delta upper: 3087/387200 < 1/125')
    print('Chernoff information proxy error upper:', global_error)
    print('maximum certified delta interval width < 1e-25:', max_width < Q(1,10**25))
    print('PASS_BRC_S23_UNIFORM_CHERNOFF_RATIONAL_PROXY_20261104')


if __name__ == '__main__':
    main()
