"""PREFIX-418 | exact rational interval proof of the uniform two-source candidate crossing.

Evidence status: author-side, conditional on these explicit sources being globally optimal.
No floating-point operation is used to decide assertions. Pure Python standard library.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt


@dataclass(frozen=True)
class Interval:
    lo: F
    hi: F

    def __post_init__(self):
        assert self.lo <= self.hi

    def __add__(self, other):
        b = interval(other)
        return Interval(self.lo + b.lo, self.hi + b.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -interval(other)

    def __rsub__(self, other):
        return interval(other) - self

    def __mul__(self, other):
        b = interval(other)
        products = [x * y for x in (self.lo, self.hi) for y in (b.lo, b.hi)]
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def inverse(self):
        assert 0 < self.lo or self.hi < 0, (self.lo, self.hi)
        return Interval(1 / self.hi, 1 / self.lo)

    def __truediv__(self, other):
        return self * interval(other).inverse()

    def __rtruediv__(self, other):
        return interval(other) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        if n == 0:
            return interval(1)
        if n % 2:
            return Interval(self.lo**n, self.hi**n)
        if self.lo <= 0 <= self.hi:
            return Interval(F(0), max(abs(self.lo), abs(self.hi))**n)
        return Interval(min(self.lo**n, self.hi**n), max(self.lo**n, self.hi**n))


def interval(x):
    if isinstance(x, Interval):
        return x
    q = F(x)
    return Interval(q, q)


SQRT_SCALE = 10**30


def rational_sqrt(a):
    """Mathematically outward-rounded sqrt at fixed 10^-30 spacing."""
    a = interval(a)
    assert a.lo >= 0

    def floor_sqrt(q):
        return F(isqrt(q.numerator * SQRT_SCALE**2 // q.denominator), SQRT_SCALE)

    lower = floor_sqrt(a.lo)
    upper = floor_sqrt(a.hi)
    if upper * upper < a.hi:
        upper += F(1, SQRT_SCALE)
    assert lower * lower <= a.lo and upper * upper >= a.hi
    return Interval(lower, upper)


@dataclass(frozen=True)
class Dual:
    value: Interval
    derivative: Interval

    def __add__(self, other):
        b = dual(other)
        return Dual(self.value + b.value, self.derivative + b.derivative)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, -self.derivative)

    def __sub__(self, other):
        return self + -dual(other)

    def __rsub__(self, other):
        return dual(other) - self

    def __mul__(self, other):
        b = dual(other)
        return Dual(self.value * b.value,
                    self.derivative * b.value + self.value * b.derivative)

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = dual(other)
        return Dual(self.value / b.value,
                    (self.derivative * b.value - self.value * b.derivative)
                    / (b.value * b.value))

    def __rtruediv__(self, other):
        return dual(other) / self

    def __pow__(self, n):
        assert n >= 0 and isinstance(n, int)
        if n == 0:
            return dual(1)
        return Dual(self.value**n,
                    n * self.value**(n-1) * self.derivative)


def dual(x):
    return x if isinstance(x, Dual) else Dual(interval(x), interval(0))


def root(x):
    if isinstance(x, Dual):
        sq = rational_sqrt(x.value)
        assert sq.lo > 0
        return Dual(sq, x.derivative / (2*sq))
    return rational_sqrt(x)


def port_coefficients(w):
    p = (245 + 123*w)/16
    q = (-123 + 245*w)/16
    a = 36 + 12*w
    b = -20 + 28*w
    j = (53 - 8*w + 29*w*w)/2
    c = F(709,64)*(w*w - 1)
    return p,q,a,b,j,c


def candidate(eps,eta):
    """Algebraic candidate, two distinct phase leaves, no global-optimality assertion."""
    beta = F(1,10**6)
    E = F(53,8)
    wp, wm = root(1-eps), -root(1+eps)
    pp,qp,ap,bp,jp,cp = port_coefficients(wp)
    n = pp*pp + qp*qp
    k = eta-cp-E*beta
    d = n*beta-k*k
    sd = root(d)
    scalar = (ap*pp+bp*qp)/n
    c = (ap*qp-bp*pp)/n
    xp = (k*pp+sd*qp)/n
    yp = (k*qp-sd*pp)/n
    pos = jp - 37 + 16*beta + scalar*k + c*sd
    hpos = 2*xp + beta

    pm,qm,am,bm,jm,cm = port_coefficients(wm)
    x0,x1 = -eta/2, F(-1,2)
    y0 = (-eta-cm-pm*x0)/qm
    y1 = (pm/2-E)/qm
    a2 = x1*x1+y1*y1
    a1 = 2*(x0*x1+y0*y1)-1
    a0 = x0*x0+y0*y0
    disc = a1*a1-4*a2*a0
    sdisc = root(disc)
    # Small positive root, avoiding a subtractive-cancellation formula.
    t = 2*a0/(-a1+sdisc)
    r0 = 45-jm-am*x0-bm*y0
    r1 = -am*x1-bm*y1-16
    neg = r0+r1*t
    xm,ym = x0+x1*t,y0+y1*t
    return {
        'G': pos-neg, 'positive':pos,'negative':neg,
        'Dplus':d,'Dminus':disc,'small_root':t,
        'hplus':hpos,'xplus':xp,'yplus':yp,
        'xminus':xm,'yminus':ym,'a1':a1,
        'positive_c':c, 'negative_Q':qm,
    }


def main():
    eps_box = Interval(F(0),F(1,10**6))
    eta_box = Interval(F(7,4000),F(187,100000))
    low, high = eta_box.lo,eta_box.hi

    v = candidate(eps_box,eta_box)
    assert v['Dplus'].lo>0 and v['Dminus'].lo>0
    assert v['a1'].hi<0 and v['negative_Q'].hi<0
    assert v['positive_c'].lo>0
    assert v['small_root'].lo>0 and v['small_root'].hi<F(1,10**6)
    assert -low < v['hplus'].lo <= v['hplus'].hi < low
    assert v['xplus'].lo > -F(1,100) and v['xplus'].hi < F(1,100)
    print('PASS_PREFIX418_EXACT_UNIFORM_FEASIBLE_TWO_SOURCE_WITNESSES')

    g0 = candidate(eps_box, interval(low))['G']
    g1 = candidate(eps_box, interval(high))['G']
    assert g0.lo>F(19,100000)   # > 0.00019
    assert g1.hi< -F(22,100000)  # < -0.00022
    print('PASS_PREFIX418_UNIFORM_STRICT_ENDPOINT_SIGN_CERTIFICATES')

    g_eps = candidate(Dual(eps_box,interval(1)),Dual(eta_box,interval(0)))['G'].derivative
    g_eta = candidate(Dual(eps_box,interval(0)),Dual(eta_box,interval(1)))['G'].derivative
    assert F(259,100)<g_eps.lo <= g_eps.hi < F(262,100)
    assert F(-418,100)<g_eta.lo <= g_eta.hi < F(-417,100)
    slope = -g_eps/g_eta
    assert F(621,1000)<slope.lo <= slope.hi<F(627,1000)
    print('PASS_PREFIX418_UNIFORM_G_EPS_POSITIVE_G_ETA_NEGATIVE_AND_SLOPE')

    e0 = interval(F(0))
    z0,z1=F(1806822353106,10**15), F(1806822353107,10**15)
    assert candidate(e0,interval(z0))['G'].lo>0
    assert candidate(e0,interval(z1))['G'].hi<0
    ep = interval(F(1,10**6))
    z2,z3=F(1807446320202,10**15), F(1807446320203,10**15)
    assert candidate(ep,interval(z2))['G'].lo>0
    assert candidate(ep,interval(z3))['G'].hi<0
    print('PASS_PREFIX418_EXACT_ENDPOINT_ROOT_ISOLATION_1E_MINUS_15')

    # Extrema of full compound model are NOT proved by this certificate.
    print('CERTIFIED_FULL_BOX_Geps_IN (259/100,262/100)')
    print('CERTIFIED_FULL_BOX_Geta_IN (-418/100,-417/100)')
    print('CERTIFIED_FULL_BOX_Deta_deps_IN (621/1000,627/1000)')
    print('ETA0_IN',z0,z1)
    print('ETA_AT_EPS_1E-6_IN',z2,z3)
    print('STATUS: candidate families only; global branch optimality not established')

if __name__ == '__main__':
    main()