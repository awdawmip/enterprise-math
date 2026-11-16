"""Recover the two landings from one exact H(0,1) at a large outer stock.

The quadratic template triangle is never enumerated.  All operations are
rational or integer.  No file is read and no floats are used by decode().
"""
from bisect import bisect_left
from fractions import Fraction as Q
from functools import lru_cache
from math import gcd, prod


class NotCertified(ValueError):
    """The measurement/bounds do not certify this inversion."""


def _valuation(q):
    def v(n):
        n = abs(n)
        return (n & -n).bit_length() - 1
    if not q:
        raise ValueError("zero valuation not required")
    return v(q.numerator) - v(q.denominator)


def _rising(x, length):
    return prod(range(x, x+length))


@lru_cache(maxsize=32)
def outer_product(n):
    """a(n) = product from j=3 through n, with cancellations by subtrees."""
    def span(lo, hi):
        if hi-lo <= 40:
            return Q(prod(4*j+5 for j in range(lo, hi)),
                     prod(4*j+20 for j in range(lo, hi)))
        mid = (lo+hi)//2
        return span(lo, mid) * span(mid, hi)
    return span(3, n+1)


def _residue(q, bits):
    if q.denominator % 2 == 0:
        raise NotCertified("insufficient dyadic precision for integral lift")
    modulus = 1 << bits
    return (q.numerator * pow(q.denominator, -1, modulus)) % modulus


def _reconstruct(value, bound, precision):
    """Recover a height <= 2**bound rational congruent to value mod 2**precision.

    Denominators can be even. Divide out value's valuation first to give a
    unit with odd denominator, without increasing its numerator/denominator.
    """
    d = _valuation(value)
    if precision <= d:
        raise NotCertified("residue has no determined leading unit")
    bits = precision - d
    # If the true valuation is positive (negative), the unit numerator
    # (denominator) has a correspondingly smaller magnitude bound.
    nbits = bound - max(d, 0)
    dbits = bound + min(d, 0)
    if min(nbits, dbits) < 0 or bits <= nbits+dbits+1:
        raise NotCertified("dyadic separation insufficient for rational lift")
    if d >= 0:
        unit = value / (1 << d)
    else:
        unit = value * (1 << -d)
    bits = nbits + dbits + 2
    modulus = 1 << bits
    residue = _residue(unit, bits)
    upper_r, upper_t = modulus, 0
    r, t = residue, 1
    max_num, max_den = 1 << nbits, 1 << dbits
    while r > max_num:
        quotient, rem = divmod(upper_r, r)
        upper_r, r = r, rem
        upper_t, t = t, upper_t-quotient*t
    if not t or abs(t)>max_den or gcd(r, t) != 1 or t % 2 == 0:
        raise NotCertified("no bounded rational representative")
    candidate = Q(r, t)
    if (candidate.numerator - residue*candidate.denominator) % modulus:
        raise NotCertified("invalid rational reconstruction")
    return candidate*(1 << d) if d >= 0 else candidate/(1 << -d)


def _first_parameters(v):
    A = Q(4*v+5, v+5) / outer_product(v)
    B = Q(28*(4+4*v)*_rising(v+5, 15), v+4)
    return A, B


def _inner_extremes(v, w):
    """Native positive inner block and three terminal columns."""
    amp = Q(prod(4*j+1 for j in range(3, w+1)),
            prod(4*j+4 for j in range(3, w+1)))
    p = Q(840, (w+2)*(w+3)*(w+4))
    cols = [amp*(p*a+b)/(1+p*amp*a) for a,b in
            [(Q(3,32),Q(15,32)),(Q(3,2),Q(15,8)),(Q(6),Q(3))]]
    rho = 4*Q(prod(4*j+3 for j in range(w,v+1)),
              prod(4*(j+3) for j in range(w,v+1)))
    tau = rho*Q(28*(2+4*w)*_rising(w+3,9), (2+w)*_rising(v+4,9))
    out = [(rho+tau*z)/(1+tau*z) for z in cols]
    return min(out), max(out)


def decode(c, n, measurement, bounds=None, *, certificate=None):
    """Return (v,w). Optional (hA,hL) must be valid on the admissible set.

    Defaults come from C74 and guarantee n >= 120 max(100,c). The same
    degree-one inversion is attempted at smaller n and succeeds whenever the
    height/precision tests certify it. Inputs outside the certified conditions
    raise NotCertified. Optional certificate is a dict populated on success.
    hA bounds log2 height of A; hL bounds both endpoints
    after multiplication by B. Height means max(abs(numerator), denominator).
    """
    if not isinstance(c, int) or not isinstance(n, int) or c < 2 or n < c:
        raise ValueError("integer stocks n >= c >= 2 required")
    if not isinstance(measurement, (Q, int)) or measurement <= 1:
        raise ValueError("an exact Fraction greater than 1 is required")
    measurement = Q(measurement)
    M = max(100,c)
    hA, hL = (20*M,42*M) if bounds is None else bounds
    if not all(isinstance(v, int) and v > 0 for v in (hA,hL)):
        raise ValueError("height bounds must be positive integers")
    P = _rising(n+6, 15)
    e = 1 / outer_product(n)
    D = _valuation(e)
    pbits = (P-1).bit_length()
    uv_bound = pbits+hA+hL
    if D <= uv_bound:
        raise NotCertified("denominator of Taylor model not certified a unit")
    # G(e)=C*(1+e U)/(1+e V); log2 heights of C, U, V are bounded.
    # C=(P*den(H)+num(H))*num(L) / ((P*den(L)+num(L))*num(H)).
    center_bound = pbits+2*hL+1
    width_bound = 2*uv_bound+1
    # The relative error for both rational lifts has valuation >= D-uv_bound.
    # In the first lift this follows from v2(U-V) >= -uv_bound.
    def lift(value, bound):
        if not value:
            raise NotCertified("vanishing observed Taylor coefficient")
        return _reconstruct(value, bound, _valuation(value)+D-uv_bound)
    center = lift(measurement, center_bound)
    if center <= 0:
        raise NotCertified("invalid center")
    q = (measurement/center-1)/e
    W = lift(q, width_bound)
    V = (W/q-1)/e
    U = W+V
    if min(U,V) <= 0 or center*U == V:
        raise NotCertified("nonphysical reconstructed pole")
    # center = (A V+1)/(A U+1); either ordering of the names U,V is valid.
    A = (1-center)/(center*U-V)
    v = bisect_left(range(2,c+1), A, key=lambda z: _first_parameters(z)[0]) + 2
    if v > c or _first_parameters(v)[0] != A:
        raise NotCertified("first landing parameter not in admissible inventory")
    A, B = _first_parameters(v)
    lower, upper = sorted((P/(A*U*B), P/(A*V*B)))
    # C67: J = max|z-1|/min|z-1| is strictly increasing in w.
    def ratio(pair):
        a,b = sorted(abs(z-1) for z in pair)
        if not a:
            raise NotCertified("blind inner endpoint")
        return b/a
    j_obs = ratio((lower,upper))
    w = bisect_left(range(2,v+1), j_obs,
                    key=lambda z: ratio(_inner_extremes(v,z))) + 2
    if w > v or _inner_extremes(v,w) != (lower,upper):
        raise NotCertified("second landing endpoints not in admissible inventory")
    if certificate is not None:
        certificate.update(outer_stock=n, precision_of_units=D-uv_bound,
                           center_height_bound=center_bound, width_height_bound=width_bound,
                           center_valuation=_valuation(center), width_valuation=_valuation(W),
                           uniform_120_applies=n>=120*M)
    return v,w
