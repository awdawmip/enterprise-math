"""Exact Q(sqrt(43)) verifier: BRC N4/S23 asymmetric lawful-vs-hull radius.
No floating point, third-party modules, or native physics claims.
"""
import json
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product

@dataclass(frozen=True)
class Q43:
    a: F = F(0)
    b: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, 'a', F(self.a))
        object.__setattr__(self, 'b', F(self.b))

    def __add__(self, other):
        other = q(other)
        return Q43(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q43(-self.a, -self.b)

    def __sub__(self, other):
        return self + -q(other)

    def __rsub__(self, other):
        return q(other) - self

    def __mul__(self, other):
        other = q(other)
        return Q43(self.a * other.a + 43 * self.b * other.b,
                   self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = q(other)
        norm = other.a * other.a - 43 * other.b * other.b
        assert norm != 0
        return self * Q43(other.a / norm, -other.b / norm)

    def __rtruediv__(self, other):
        return q(other) / self

    def sign(self):
        a, b = self.a, self.b
        if b == 0:
            return (a > 0) - (a < 0)
        if a == 0:
            return (b > 0) - (b < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        diff = a*a - 43*b*b
        assert diff != 0  # sqrt(43) is irrational
        return ((diff > 0) - (diff < 0)) * (1 if a > 0 else -1)

    def __lt__(self, other):
        return (self - other).sign() < 0

    def __le__(self, other):
        return (self - other).sign() <= 0

    def __eq__(self, other):
        other = q(other)
        return (self.a, self.b) == (other.a, other.b)

    def __abs__(self):
        return self if self.sign() >= 0 else -self


def q(x):
    return x if isinstance(x, Q43) else Q43(F(x))


def prepared(a, b, c):
    a, b, c = q(a), q(b), q(c)
    au = [a, (1-a)*b, (1-a)*(1-b)/2, (1-a)*(1-b)/2]
    av = [a, q(0), (1-a)*c, (1-a)*(1-c)]
    bu = [q(F(1,4)), 3*b/4, 3*(1-b)/8, 3*(1-b)/8]
    bv = [q(F(1,4)) for _ in range(4)]
    return [au, au, av, bu, bu, bv]


def tv(p, r):
    assert sum(p) == q(1) and sum(r) == q(1)
    return sum(abs(x-y) for x, y in zip(p,r)) / 2


def center_combo(terms):
    return [[sum(q(w)*prepared(*abc)[i][t] for w,abc in terms)
             for t in range(4)] for i in range(6)]


def verify():
    A, B, C = [F(1,2),F(7,8)], [F(1,8),F(1,2)], [F(1,2),F(7,8)]
    corners = list(product(A,B,C))
    # Rational hull center as a single four-vertex joint mixture.
    combo = [(F(4,9), (A[0],B[0],C[1])),
             (F(1,18),(A[0],B[1],C[0])),
             (F(2,9), (A[1],B[0],C[1])),
             (F(5,18),(A[1],B[1],C[0]))]
    assert sum(w for w,_ in combo) == 1
    H = center_combo(combo)
    assert H[0] == list(map(q,[F(11,16),F(1,16),F(1,8),F(1,8)]))
    assert H[2] == list(map(q,[F(11,16),0,F(1,4),F(1,16)]))
    assert H[3] == list(map(q,[F(1,4),F(3,16),F(9,32),F(9,32)]))
    hull = q(F(3,16))
    h_tv = [[tv(prepared(*v)[i],H[i]) for i in range(6)] for v in corners]
    assert max(max(row) for row in h_tv) == hull
    assert all(t<=hull for row in h_tv for t in row)
    # Exact algebraic r*: positive root of 32r^2+40r-9.
    r = Q43(F(-5,8),F(1,8))
    assert 32*r*r+40*r-9 == q(0)
    assert hull < r < q(F(1,5))
    x, y = q(F(7,8))-r, q(F(1,2))-4*r/3
    c = 1/(4*(1-x))
    assert q(A[0]) <= x <= q(A[1])
    assert q(B[0]) <= y <= q(B[1])
    assert q(C[0]) <= c <= q(C[1])
    assert (1-x)*(1-y) == q(F(7,16))-r
    assert (1-x)*c == q(F(1,4))
    L = prepared(x,y,c)
    l_tv = [[tv(prepared(*v)[i],L[i]) for i in range(6)] for v in corners]
    assert max(max(row) for row in l_tv) == r
    assert all(t<=r for row in l_tv for t in row)
    assert [max(row[i] for row in l_tv) for i in range(6)] == [r,r,r,r,r,q(0)]
    # Hull center is not lawful: its forced a=11/16,b=1/4 give AU time2=5/64.
    assert (1-q(F(11,16)))*q(F(1,4)) - H[0][1] == q(F(1,64))
    assert 32*hull*hull+40*hull-9 == q(F(-3,8))
    return {
      'pass':'PASS_BRC_N4_S23_ASYMMETRIC_STRICT_HULL_GAP_SQRT43_20261101',
      'arithmetic':'exact standard-library Fraction in Q(sqrt(43)); no floats',
      'lawful_box':[['1/2','7/8'],['1/8','1/2'],['1/2','7/8']],
      'corners_checked':len(corners), 'prepared_row_corner_checks':len(corners)*6,
      'hull_weights':['4/9','1/18','2/9','5/18'],
      'hull_radius':'3/16', 'lawful_radius':'(sqrt(43)-5)/8',
      'strict_gap':'(2sqrt(43)-13)/16 > 0',
      'lawful_witness':{
        'a':'(12-sqrt(43))/8', 'b':'(8-sqrt(43))/6',
        'c':'2(sqrt(43)+4)/27'},
      'lawful_tv_by_preparation':['r*','r*','r*','r*','r*','0'],
      'hull_tv_by_preparation':['3/16','3/16','3/16','3/16','3/16','0'],
      'hull_center_nonlawful_AU_time2_discrepancy':'1/64',
      'all_real_scope':'proved analytically via causal-positive source marginal ranges and multi-affinity',
      'scientific_status':'AUTHOR_ANALYTIC_PROOF / EXACT_QUADRATIC_EXECUTED / UNREVIEWED / NOT_ADMITTED',
      'P000_native_embedding':'NOT_ESTABLISHED'
    }

if __name__=='__main__':
    print(json.dumps(verify(), indent=2))
