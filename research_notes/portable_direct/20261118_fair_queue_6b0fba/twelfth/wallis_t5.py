"""All-order subtool for T5_PRECISION_REFINEMENT / precision.spectral_decimation_completion."""
from dataclasses import dataclass
from fractions import Fraction
from math import factorial, isqrt


@dataclass(frozen=True)
class HighOrderSpectralCertificate:
    q: int
    order: int
    method: str
    interval: tuple[Fraction, Fraction]
    working_bits: int
    weights: tuple[Fraction, ...]
    moment_count: int


def dyadic_annihilation_weights(order):
    if order < 0:
        raise ValueError("order must be nonnegative")
    d = [1]
    for r in range(1, order+1):
        d.append(d[-1]*(4**r-1))
    return tuple(Fraction((-1)**(order-j)*4**(j*(j+1)//2), d[j]*d[order-j])
                 for j in range(order+1))


def phase_moments(count):
    if count < 1:
        raise ValueError("at least one moment is required")
    m = [Fraction(1)]
    for j in range(1, count):
        m.append(m[-1] * Fraction(2*j*j, (j+1)*(2*j+1)))
    return m


def _orthogonal(moments, n):
    if n == 0:
        return [Fraction(1)]
    rows = [moments[i:i+n]+[-moments[i+n]] for i in range(n)]
    # Leading principal Hankel determinants are strictly positive.
    for i in range(n):
        pivot = rows[i][i]
        rows[i] = [x/pivot for x in rows[i]]
        for j in range(n):
            if j != i:
                factor = rows[j][i]
                rows[j] = [x-factor*y for x,y in zip(rows[j], rows[i])]
    return [rows[i][-1] for i in range(n)]+[Fraction(1)]


def _product(a, b):
    c = [Fraction(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def phase_moment_fractions(order):
    """Lower and upper resolvents as (numerator, denominator), constant first."""
    if order < 1:
        raise ValueError("quadrature order must be positive")
    m = phase_moments(2*order)
    lower_den = list(reversed(_orthogonal(m, order)))
    modified = [m[j+1]-m[j+2] for j in range(2*order-2)]
    upper_den = _product([1,-1], list(reversed(_orthogonal(modified, order-1))))
    lower_num = _product(lower_den, m)[:order]
    upper_num = _product(upper_den, m)[:order+1]
    return (lower_num, lower_den), (upper_num, upper_den)


def _value(poly, x):
    result = Fraction(0)
    for c in reversed(poly):
        result = result*x+c
    return result


def _resolvent(nd, x):
    num, den = nd
    return _value(num, x)/_value(den, x)


def _sqrt_interval(x, bits):
    scale = 1 << bits
    numerator = x.numerator*scale*scale
    lo = isqrt(numerator//x.denominator)
    exact = lo*lo*x.denominator == numerator
    return Fraction(lo,scale), Fraction(lo if exact else lo+1,scale)


def _first_mode(q, bits):
    lo = hi = Fraction(2)
    for _ in range(q.bit_length()-2):
        lo, hi = 2-_sqrt_interval(4-lo,bits)[1], 2-_sqrt_interval(4-hi,bits)[0]
    return lo, hi


def high_order_spectral_certificate(q, order, method="moments", bits=128):
    """Outward rational interval for the internal first completion phase on a dyadic grid."""
    if q < 2 or q & (q-1):
        raise ValueError("q must be a power of two, q >= 2")
    if bits < 1:
        raise ValueError("positive working precision is required")
    if method == "moments":
        lower, upper = phase_moment_fractions(order)
        al, ah = _first_mode(q,bits)
        lo = q*_sqrt_interval(al*_resolvent(lower,al/4),bits)[0]
        hi = q*_sqrt_interval(ah*_resolvent(upper,ah/4),bits)[1]
        return HighOrderSpectralCertificate(q,order,method,(lo,hi),bits,(),2*order)
    if method != "richardson":
        raise ValueError("method must be moments or richardson")
    w = dyadic_annihilation_weights(order)
    lo = hi = Fraction(0)
    for j, weight in enumerate(w):
        scale = q*(1 << j)
        al, ah = _first_mode(scale,bits)
        tl = scale*_sqrt_interval(al,bits)[0]
        th = scale*_sqrt_interval(ah,bits)[1]
        lo += weight*(tl if weight >= 0 else th)
        hi += weight*(th if weight >= 0 else tl)
    width = Fraction(4*4**(order+1), q**(2*order+2)*4**(order*(order+1)//2)*factorial(2*order+3))
    return HighOrderSpectralCertificate(q,order,method,(lo,hi+width),bits,w,0)
