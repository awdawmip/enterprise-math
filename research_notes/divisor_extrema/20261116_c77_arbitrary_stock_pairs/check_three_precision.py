"""Exact spectral derivative bounds and checks of finite three-stock readouts."""
from fractions import Fraction as F
from functools import cache
from math import gamma, log2
import json


def stock(c, i):
    lo, hi = c, 8 * c
    bound = c**15 * 1024**4
    assert hi**15 * i**4 > bound
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**15 * i**4 <= bound:
            lo = mid
        else:
            hi = mid
    return lo


@cache
def prefix(n, k):
    top = bottom = 1
    for j in range(1, n + 1):
        top *= 4 * j + k
        bottom *= 4 * (j + k)
    return F(top, bottom)


@cache
def edge(n, s, k):
    rho = 4 * prefix(n, k) / prefix(s - 1, k)
    inva = F(28 * (k - 1 + 4 * s), k - 1 + s)
    for j in range(3 * k):
        inva *= F(s + k + j, n + k + 1 + j)
    return rho, rho * inva


def physical(c, v, w):
    tail = F(840, (w + 2) * (w + 3) * (w + 4))
    amp = prefix(w, 1) / prefix(2, 1)
    ends = [amp * (tail * a + b) / (1 + tail * amp * a)
            for a, b in [(F(3, 32), F(15, 32)), (F(3, 2), F(15, 8)),
                         (F(6), F(3))]]
    for n, s, k in [(v, w, 3), (c, v, 5)]:
        rho, tau = edge(n, s, k)
        ends = [(rho + tau * e) / (1 + tau * e) for e in ends]
    return max(ends) / min(ends) - 1


def relative_limit(x, y, t):
    A, D = 4 * x**3.75, 4 * (y / x)**2.25
    b = 7 / 16
    m = b * A**4 * D
    L = 81 / 32 * gamma(4) / gamma(13 / 4)
    norm = L * b**2 * A**4 * D**5 * abs(1 - D) * y**(-.75)
    return norm * t**4 * (1 - A*t) / ((1 + m*t**4) * (1 + m*A*t**5))


def check():
    ep = F(1, 1024)
    i = 3
    b1 = 4 * i**2 * ep / (1 - 4 * i * ep) + 448 * i**5 * ep**4
    b2 = 448 * i**8 * ep**4 + 4 * i**5 * ep
    assert b1 < F(1, 16) and b2 < 1
    det = F(7, 8) * 78 - F(17, 8) * 17
    assert det == F(257, 8)
    controls = []
    for c in (32, 128, 512):
        v, w = 3*c//4, c//2
        ns = [stock(c, j) for j in range(1, 4)]
        row = []
        for j, n in enumerate(ns, 1):
            q = physical(n, v, w)
            # Independently compute the predicted normalized scales.
            assert q > 0
            delta = float(q) * c**.75
            limit = relative_limit(.75, .5, j/1024)
            row.append(round(log2(delta / limit), 10))
        controls.append(dict(c=c, v=v, w=w, outer_stocks=ns,
                             log2_exact_normalized_width_over_limit=row))
    assert all(abs(controls[-1]['log2_exact_normalized_width_over_limit'][i])
               < abs(controls[0]['log2_exact_normalized_width_over_limit'][i])
               for i in range(3))
    return dict(A_column_error=str(b1), m_column_error=str(b2),
                scaled_determinant_floor=str(det), controls=controls)


if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
