"""Certified rational endpoint intervals for BRC S23 cubic Chernoff proxy.

No floating point enters the certificate.  Uses rational Taylor bounds and isqrt.
The universal sign inequalities are checked by exact rational constants;
transcendental endpoint samples at v=1/21 are interval-enclosed.
"""
from fractions import Fraction as Q
from math import isqrt, factorial

V = Q(1, 21)
R2 = 1 - V * V
D0 = V / 6 + V**3 / 20
SCALE = 10**48


def sqrt_interval(q):
    assert q > 0
    a, b = q.numerator, q.denominator
    lo_i = isqrt(a * SCALE * SCALE // b)
    lo = Q(lo_i, SCALE)
    hi = Q(lo_i + 1, SCALE)
    assert lo * lo <= q <= hi * hi
    return lo, hi


def atanh_interval(x, n=15):
    assert 0 <= x < Q(1, 4)
    lower = sum((x ** (2 * j + 1) / (2 * j + 1) for j in range(n)), Q(0))
    err = x ** (2 * n + 1) / ((2 * n + 1) * (1 - x * x))
    return lower, lower + err


def exp_interval(x, n=18):
    assert 0 <= x < Q(1, 100)
    lower = sum((x ** j / factorial(j) for j in range(n)), Q(0))
    tail = x ** n / factorial(n) / (1 - x / (n + 1))
    return lower, lower + tail


def fmt(bounds, digits=52):
    # Outward-round DISPLAY of exact certified rational endpoints.
    vals = []
    for idx, q in enumerate(bounds):
        scaled = q * 10**digits
        num = scaled.numerator
        den = scaled.denominator
        outward = num // den if idx == 0 else -((-num) // den)
        sign = '-' if outward < 0 else ''
        n = abs(outward)
        vals.append(sign + str(n // 10**digits) + '.' + str(n % 10**digits).zfill(digits))
    return ' .. '.join(vals)


# Universal closed-form sign bounds for 0<v<=1/21.
assert Q(441, 440) < Q(101, 100)
assert Q(1, 6) + Q(1, 20 * 441) < Q(1, 5)
assert Q(101, 100) / (5 * 441) < Q(1, 2000)
assert Q(2000, 1999) < Q(11, 10)
assert Q(101, 100)**2 * Q(11, 10) < Q(6, 5)
assert Q(1, 6) - Q(3, 25) == Q(7, 150)
assert 32 * V**8 / R2**2 < Q(7, 1800)

rlo, rhi = sqrt_interval(R2)
alo, ahi = atanh_interval(V)
elo, ehi = exp_interval(ahi * D0)
# Monotonicity of exp applied to the lower argument too.
elo = exp_interval(alo * D0)[0]
# Exact enclosure for G3(0)=(r(e^(a*d0)-1)-v*d0)/2.
g0lo = (rlo * (elo - 1) - V * D0) / 2
g0hi = (rhi * (ehi - 1) - V * D0) / 2
assert g0lo <= g0hi < -Q(7, 1800) * V**4 < 0

# log(r)=-2 atanh((1-r)/(1+r)); atanh increases in argument.
qlo = (1 - rhi) / (1 + rhi)
qhi = (1 - rlo) / (1 + rlo)
ll, lh = atanh_interval(qlo)
hl, hh = atanh_interval(qhi)
log_r_lo, log_r_hi = -2 * hh, -2 * ll
# (1-r)/r^2 decreases with r.
f_lo = (1-rhi) / rhi**2
f_hi = (1-rlo) / rlo**2
g1lo, g1hi = f_lo + log_r_lo, f_hi + log_r_hi
assert g1hi >= g1lo > Q(1, 4) * V**4 > 0

# Previous normalized error envelope and its endpoint behavior.
err = 32 * V**12 / R2**2
assert err < Q(1, 10**14)
assert -Q(7, 1800) * V**4 + err < 0

print('BRC S23 v=1/21 rational endpoint certificate')
print('G3(0) bounds:', fmt((g0lo, g0hi)))
print('G3(1) bounds:', fmt((g1lo, g1hi)))
print('analytic G3(0) < -7*v^4/1800:', True)
print('analytic G3(1) > v^4/4:', True)
print('normalized proxy error bound:', fmt((err, err)))
print('PASS_BRC_S23_CUBIC_PROXY_ANALYTIC_ENDPOINT_SIGNS_20261104')
