"""Exact matrix-jet checks for the three-state, two-pole order classification."""
from fractions import Fraction as Q
from itertools import product
from dataclasses import dataclass


@dataclass(frozen=True)
class Quadratic:
    """x + y sqrt(3), with exact rational coordinates."""
    x: Q
    y: Q = Q(0)

    def __add__(self, other):
        if not isinstance(other, Quadratic):
            other = Quadratic(Q(other))
        return Quadratic(self.x + other.x, self.y + other.y)

    __radd__ = __add__

    def __neg__(self):
        return Quadratic(-self.x, -self.y)

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return other + -self

    def __mul__(self, other):
        if not isinstance(other, Quadratic):
            other = Quadratic(Q(other))
        return Quadratic(self.x * other.x + 3 * self.y * other.y,
                         self.x * other.y + self.y * other.x)

    __rmul__ = __mul__

    def __bool__(self):
        return bool(self.x or self.y)


def residues(poles, poly):
    """p(z)/[(z+a)(z+b)] in the two simple fractions."""
    a, b = poles
    c, d = poly
    return (c - a*d) * Q(1, b-a), (c - b*d) * Q(1, a-b)


def primitive_matrix(poles, poly, d):
    coeff = residues(poles, poly)
    return [[sum(c * Q((-1)**(r-j-1), r * a**(r-j))
                 for a, c in zip(poles, coeff))
             if j < r else 0 for j in range(d)] for r in range(d)]


def output_column(g, f, h, j):
    return [h[r][j] + sum(g[r][s] * f[s][j] for s in range(j+1, r))
            for r in range(len(g))]


def order(values):
    return next((i for i, v in enumerate(values) if v), None)


def witness(poles, beta, wanted):
    q0, q1 = poles[0] * poles[1], sum(poles)
    slope = 2*q0*beta - q1
    mats = [primitive_matrix(poles, p, 7)
            for p in [(1, beta), (-q0, slope), (0, 1)]]
    first, second = (output_column(*mats, j) for j in (0, 1))
    assert order(first) == 5 and first[5] == wanted
    actual = second[3]
    if isinstance(actual, Quadratic):
        actual = (actual.x, actual.y)
        assert actual == (Q(1, 6*q0), 0)
    else:
        assert actual == Q(1, 6*q0)
    print(f'poles {poles}, order 5, column 0 [z^5]={first[5]}, column 1 [z^3]={actual}')


def grid(poles):
    d = 6
    polys = list(product(range(-1, 2), repeat=2))
    mats = {p: primitive_matrix(poles, p, d) for p in polys}
    counter = {}
    for g, f, h in product(polys, repeat=3):
        columns = [output_column(mats[g], mats[f], mats[h], j) for j in (0, 1)]
        # Distinct word lengths separate h and (g tensor f) in the path polynomial.
        polynomial_nonzero = any(h) or (any(g) and any(f))
        first_order = order(columns[0])
        assert (first_order is not None) == polynomial_nonzero
        if polynomial_nonzero:
            assert any(v for col in columns for v in col[:5])
            assert first_order <= 4
        counter[first_order] = counter.get(first_order, 0) + 1
    print(f'poles {poles}, 729 triples; order frequencies {counter}')


def main():
    grid((1, 2))
    beta = Quadratic(Q(1, 2), Q(1, 6))
    # beta^2(4 beta - 3)/80 = sqrt(3)/1440.
    witness((1, 2), beta, Quadratic(Q(0), Q(1, 1440)))
    witness((3, 8), Q(1, 4), Q(1, 184320))
    for poles in ((1, 2), (3, 8)):
        zero = primitive_matrix(poles, (0, 0), 6)
        t = primitive_matrix(poles, (0, 1), 6)
        cols = [output_column(t, t, zero, j) for j in range(6)]
        assert not any(v for col in cols[:4] for v in col[:4])
        assert cols[0][4] == Q(1, 8*(poles[0]*poles[1])**2)
    print('order-four lower witness annihilates the entire dimension-four tuple for both pole pairs')


if __name__ == '__main__':
    main()
