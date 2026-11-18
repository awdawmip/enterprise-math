"""Exact full-shell Hart runs and independent rational checks. Standard library only."""
import json
from fractions import Fraction as F
from itertools import product
from math import isqrt

SCALE = 10**55
CUTS = [F(1, 12), F(3, 32), F(1, 8), F(1, 6), F(1, 5), F(1, 4)]


def icbrt(n):
    lo, hi = 0, 1 << ((n.bit_length() + 2) // 3)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**3 <= n:
            lo = mid
        else:
            hi = mid
    return hi if hi**3 == n else lo


def sqrt_interval(x):
    m = isqrt(x.numerator * SCALE**2 // x.denominator)
    return F(m, SCALE), F(m + 1, SCALE)


def pow_four_thirds(x):
    m = icbrt(x.numerator * SCALE**3 // x.denominator)
    return F(m, SCALE)**4, F(m + 1, SCALE)**4


def decimals(lo, hi, digits=15):
    """Two decimal strings bracket the specified rationals outwards."""
    scale = 10**digits
    def fmt(n):
        return format(n // scale, 'd') + '.' + str(n % scale).zfill(digits)
    return [fmt(lo * scale // 1), fmt(-((-hi * scale) // 1))]


def primitive_integral(b):
    if 32 * b * b <= 1:
        return F(0), F(0)
    assert b <= F(1, 2)
    qlo, qhi = sqrt_interval(F(2))
    plo, phi = pow_four_thirds(2 * b)
    a = 2 * b * b - F(1, 32)
    return a + b * qlo - F(9, 8) * phi, a + b * qhi - F(9, 8) * plo


def closed_density(a):
    lo, hi = primitive_integral(2 * a)
    sublo, subhi = primitive_integral(a)
    return (lo - 2 * subhi) / 4, (hi - 2 * sublo) / 4


def section(a, c):
    return (max(2 * a - c, F(0))**2 - 2 * max(a - c, F(0))**2) / 4


def riemann_density(a, panels=256):
    values = []
    for j in range(panels + 1):
        z = F(panels + j, panels)
        c_lo, c_hi = sqrt_interval(1 / (4 * z**3))
        values.append((section(a, c_hi), section(a, c_lo)))
    return (sum(v[0] for v in values[:-1]) / panels,
            sum(v[1] for v in values[1:]) / panels)


def clip(poly, form):
    """Intersect a rational polygon with form(x,y) >= 0."""
    out = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        fp, fq = form(*p), form(*q)
        if fp >= 0:
            out.append(p)
        if fp * fq < 0:
            w = fp / (fp - fq)
            out.append(tuple(i + w*(j-i) for i, j in zip(p, q)))
    return out


def clipped_torus_area(a, c):
    square = [(F(0), F(0)), (a, F(0)), (a, a), (F(0), a)]
    area = F(0)
    for winding in range(-2, 3):
        poly = clip(square, lambda x, y: 2*y - x + c - winding)
        poly = clip(poly, lambda x, y: winding + a - (2*y - x + c))
        area += abs(sum((p[0]*q[1] - p[1]*q[0]
                         for p, q in zip(poly, poly[1:] + poly[:1])), F(0))) / 2
    return area


def analytic_evidence():
    pairs = 0
    for a, c in product([F(i, 40) for i in range(11)], [F(i, 80) for i in range(14, 41)]):
        assert section(a, c) == clipped_torus_area(a, c)
        pairs += 1
    densities = {}
    for a in CUTS:
        lo, hi = closed_density(a)
        rlo, rhi = riemann_density(a)
        assert rlo <= lo <= hi <= rhi
        densities[str(a)] = {'closed': decimals(lo, hi), 'riemann_256': decimals(rlo, rhi)}
    rootlo, roothi = sqrt_interval(F(2))
    coefficient = decimals(32 * rootlo / 9, 32 * roothi / 9)
    cubic = {}
    for tau in (F(1, 4), F(1, 16), F(1, 64), F(1, 256), F(1, 1024)):
        t = 1 + tau
        plo, phi = pow_four_thirds(t)
        b = t*t/16 + t/4 - F(1, 32)
        lo, hi = (b - 9*phi/32)/4, (b - 9*plo/32)/4
        cubic[str(tau)] = decimals(lo*1024*rootlo/tau**3, hi*1024*roothi/tau**3)
    return {'rational_polygon_sections': pairs, 'density': densities, 'cubic_coefficient': coefficient,
            'density_over_epsilon_cubed_for_epsilon_equal_tau_times_cutoff': cubic}


def isprime(n):
    return n >= 2 and all(n % i for i in range(2, isqrt(n) + 1))


def full_shell(n, factors=None):
    low0 = icbrt(n)
    low, high = low0 + (low0**3 < n), icbrt(8*n)
    assert (low-1)**3 < n <= low**3 and high**3 <= 8*n < (high+1)**3
    if factors:
        assert factors[0]*factors[1] == n and all(isprime(p) for p in factors)
    thresholds = [(a.numerator, a.denominator) for a in CUTS]
    thresholds.append(None)
    labels = [str(a) for a in CUTS] + ['1/(8sqrt(2))']
    run_counts, pair_counts = [0]*len(labels), [0]*len(labels)
    first_quarter = None
    squares = 0
    last = []
    for k in range(low, high+1):
        h = 4*n*k
        r = isqrt(h)
        x = r + (r*r < h)
        e, den = x*x - h, 2*x-1
        assert (x-1)**2 < h <= x*x
        squares += e == 0
        hits = [e*v <= den*u for u, v in thresholds[:-1]]
        hits.append(128*e*e <= den*den)
        last.append((hits, x, e, den))
        if len(last) < 3:
            continue
        old, mid, new = last
        for j, (i0, i2) in enumerate(zip(old[0], new[0])):
            if i0 and i2:
                pair_counts[j] += 1
                run_counts[j] += mid[0][j]
        if old[0][-2] and mid[0][-2] and new[0][-2]:
            assert old[1] - 2*mid[1] + new[1] == 0
            if first_quarter is None:
                first_quarter = {'k': k-2, 'x': [v[1] for v in last],
                                 'score_numerators': [v[2] for v in last],
                                 'score_denominators': [v[3] for v in last]}
        last.pop(0)
    assert run_counts[-1] == 0
    return {'N': n, 'prime_factors_if_selected': factors, 'inclusive_shell': [low, high],
            'complete_starts': high-low-1, 'exact_square_positions': squares,
            'three_hits': dict(zip(labels, run_counts)), 'endpoint_hits': dict(zip(labels, pair_counts)),
            'first_three_at_quarter': first_quarter}


def main():
    examples = [(1009*1013, [1009, 1013]), (10**9, None),
                (1000003*1000033, [1000003, 1000033]),
                (1000000007*1000000009, [1000000007, 1000000009])]
    output = {'scope': 'fixed rational or squared-algebraic tests on all original integer scores in each complete shell',
              'analytic': analytic_evidence(), 'integer_shells': [full_shell(*example) for example in examples]}
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
