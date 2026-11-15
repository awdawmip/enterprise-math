"""Exact BRC N=4/S23 upper-a endpoint phase certificate (author-side)."""
from dataclasses import dataclass
from fractions import Fraction as F
from functools import total_ordering
from itertools import product

@total_ordering
@dataclass(frozen=True)
class Quadratic:
    a: F
    b: F
    d: F

    def __init__(self, a=0, b=0, d=1):
        object.__setattr__(self, "a", F(a))
        object.__setattr__(self, "b", F(b))
        object.__setattr__(self, "d", F(d))
        assert self.d > 0

    def cast(self, value):
        if isinstance(value, Quadratic):
            assert value.d == self.d
            return value
        return Quadratic(value, 0, self.d)

    def __add__(self, value):
        x = self.cast(value)
        return Quadratic(self.a + x.a, self.b + x.b, self.d)

    __radd__ = __add__

    def __neg__(self):
        return Quadratic(-self.a, -self.b, self.d)

    def __sub__(self, value):
        return self + -self.cast(value)

    def __rsub__(self, value):
        return self.cast(value) - self

    def __mul__(self, value):
        x = self.cast(value)
        return Quadratic(self.a*x.a + self.b*x.b*self.d,
                         self.a*x.b + self.b*x.a, self.d)

    __rmul__ = __mul__

    def __truediv__(self, value):
        x = self.cast(value)
        den = x.a*x.a - x.b*x.b*x.d
        assert den != 0
        return Quadratic((self.a*x.a - self.b*x.b*x.d)/den,
                         (self.b*x.a - self.a*x.b)/den, self.d)

    def __rtruediv__(self, value):
        return self.cast(value)/self

    def sign(self):
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if (a > 0) == (b > 0):
            return (a > 0) - (a < 0)
        delta = b*b*self.d - a*a
        if delta == 0:
            return 0
        return (delta > 0) - (delta < 0) if b > 0 else (delta < 0) - (delta > 0)

    def __eq__(self, value):
        return (self - self.cast(value)).sign() == 0

    def __lt__(self, value):
        return (self - self.cast(value)).sign() < 0

    def __abs__(self):
        return self if self.sign() >= 0 else -self

    def __str__(self):
        return str(self.a) if self.b == 0 else f"({self.a})+({self.b})sqrt({self.d})"


def four_stop(a, b, c):
    one = a.cast(1)
    return a, (one-a)*b, (one-a)*(one-b)*c, (one-a)*(one-b)*(one-c)


def observer(a, b, c):
    d = a.d
    q = lambda z: Quadratic(z, 0, d)
    sources = (
        four_stop(a, b, q(F(1,2))),
        four_stop(a, b, q(F(1,2))),
        four_stop(a, q(0), c),
        four_stop(q(F(1,4)), b, q(F(1,2))),
        four_stop(q(F(1,4)), b, q(F(1,2))),
        four_stop(q(F(1,4)), q(F(1,3)), q(F(1,2))),
    )
    mixing20 = ((10,10,0,0,0,0), (9,11,0,0,0,0),
                (0,0,20,0,0,0), (0,0,0,10,10,0),
                (0,0,0,2,18,0), (0,0,0,0,0,20))
    out = tuple(tuple(sum(q(F(mixing20[i][j],20))*sources[j][t]
                          for j in range(6)) for t in range(4))
                for i in range(6))
    assert all(sum(row) == q(1) and all(z >= q(0) for z in row) for row in out)
    assert out[0] == out[1] and out[3] == out[4]
    return out


def tv(p, q):
    return sum(abs(x-y) for x,y in zip(p,q))/2


def max_row_tv(X,Y):
    return max(tv(p,q) for p,q in zip(X,Y))


def certify(h, radical=None):
    # Rational h -> quadratic field Q(sqrt(43-16h+16h^2)).
    # Exceptional exact h*= (4-sqrt(13))/8 -> field Q(sqrt(13)).
    if radical is None:
        assert isinstance(h,F) and 0 <= h <= F(1,8)
        d = F(43)-16*h+16*h*h
        q = lambda x: Quadratic(x,0,d)
        hh = q(h)
        T = (Quadratic(0,1,d)-q(5)+4*hh)/8
    else:
        d = F(13)
        q = lambda x: Quadratic(x,0,d)
        hh = (q(4)-Quadratic(0,1,d))/8
        assert 0 < hh < q(F(1,8))
        T = q(F(3,16))+hh/2
    u = q(F(7,8))+hh
    lo = q(F(1,2))
    qtail = q(1)-u
    F_radius = q(F(3,16))+hh/2
    H_radius = q(F(3,16))+hh/4
    r = max(F_radius,T)
    assert q(0) <= qtail <= q(F(1,8))
    assert q(F(3,16)) <= r <= q(F(1,4))
    assert F_radius >= H_radius
    assert 32*T*T+(q(40)-32*hh)*T-q(9)-12*hh == q(0)
    # Closed form legal center and shared joint-hull mixture center.
    s = qtail+r
    x = u-r
    y = q(F(1,2))-q(F(4,3))*r
    w = q(F(7,32))+qtail/4
    t = w/s
    assert lo <= x <= u
    assert q(F(1,8)) <= y <= q(F(1,2))
    assert q(F(1,2)) <= t <= q(F(7,8))
    witness_L = observer(x,y,t)
    witness_H1 = observer(lo,q(F(1,8)),q(F(7,8)))
    witness_H2 = observer(u,q(F(1,2)),q(F(1,2)))
    witness_H = tuple(tuple((a+b)/2 for a,b in zip(row1,row2))
                      for row1,row2 in zip(witness_H1,witness_H2))
    vertices = tuple(observer(a,b,c) for a,b,c in product((lo,u),
                      (q(F(1,8)),q(F(1,2))), (q(F(1,2)),q(F(7,8)))))
    actual_L = max(max_row_tv(v,witness_L) for v in vertices)
    actual_H = max(max_row_tv(v,witness_H) for v in vertices)
    assert actual_L == r
    assert actual_H == F_radius
    # The event-wise lower bounds used by the analytic proof.
    assert u-x <= r
    assert q(F(7,16))-s*(q(1)-y) <= r
    assert q(F(3,4))*(q(F(1,2))-y) <= r
    # Two-sign comparison gives the exact transition; no float arithmetic.
    key = 16*hh*hh-16*hh+q(F(3,4))
    assert (T > F_radius) == (key > q(0))
    assert (T == F_radius) == (key == q(0))
    phase = "lawful_gap" if T>F_radius else ("transition" if T==F_radius else "tight_hull")
    return f"h={hh} phase={phase} lawful={r} hull={F_radius} vertex_rows_checked=48 PASS"


if __name__ == "__main__":
    sample = (F(0),F(1,256),F(1,128),F(1,64),F(1,32),F(1,25),
              F(1,21),F(1,20),F(1,19),F(1,16),F(1,12),
              F(1,10),F(1,9),F(1,8))
    for h in sample:
        print(certify(h))
    print(certify(None,radical=13))
    assert (4*4-13)>0 and F(0)<F(1,8)
    print("exact_cases=15 rational_cases=14 algebraic_transition_cases=1")
    print("vertices_per_case=8 observed_rows_per_vertex=6 stop_atoms_per_row=4")
    print("PASS_BRC_N4_S23_A_UPPER_ENDPOINT_EXACT_PHASE_20261102")
