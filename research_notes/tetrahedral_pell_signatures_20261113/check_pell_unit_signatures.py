"""Exact checks in Q(sqrt(2),sqrt(29)), in basis 1,a,b,ab."""

from fractions import Fraction
from itertools import combinations, product


def multiply(left, right):
    coefficients = [Fraction(0)] * 4
    for i, value_left in enumerate(left):
        for j, value_right in enumerate(right):
            repeated = i & j
            factor = (2 if repeated & 1 else 1) * (29 if repeated & 2 else 1)
            coefficients[i ^ j] += factor * value_left * value_right
    return tuple(coefficients)


def conjugate(value, automorphism):
    """Bit zero reverses sqrt(2), bit one reverses sqrt(29)."""
    return tuple(
        coefficient * (-1) ** (index & automorphism).bit_count()
        for index, coefficient in enumerate(value)
    )


def rational_sign(value):
    return (value > 0) - (value < 0)


def quadratic_sign(constant, radical, radicand):
    """Sign of constant + radical * sqrt(radicand), at the positive root."""
    if radical == 0:
        return rational_sign(constant)
    if constant == 0 or rational_sign(constant) == rational_sign(radical):
        return rational_sign(radical)
    return rational_sign(constant) * rational_sign(constant**2 - radicand * radical**2)


def sign(value):
    """For x + sqrt(2)y, compare x*x and 2*y*y if x and y have opposite signs."""
    a, c, b, d = value  # x=a+b*sqrt(29), y=c+d*sqrt(29)
    sign_x = quadratic_sign(a, b, 29)
    sign_y = quadratic_sign(c, d, 29)
    if not sign_x:
        return sign_y
    if not sign_y or sign_x == sign_y:
        return sign_x
    difference = a*a + 29*b*b - 2*(c*c + 29*d*d)
    radical = 2*a*b - 4*c*d
    return sign_x * quadratic_sign(difference, radical, 29)


def negative_embeddings(unit):
    return frozenset(g for g in range(4) if sign(conjugate(unit, g)) < 0)


def check():
    one = (1, 0, 0, 0)
    eta = (0, Fraction(13, 2), -1, Fraction(1, 2))
    assert negative_embeddings(eta) == {1}
    norms = [multiply(eta, conjugate(eta, g)) for g in (1, 2, 3)]
    assert norms == [(-70, 0, -13, 0), (41, 29, 0, 0), (-99, 0, 0, 13)]
    assert multiply(norms[0], conjugate(norms[0], 2)) == (-1, 0, 0, 0)
    assert multiply(norms[2], (99, 0, 0, 13)) == one
    assert multiply(norms[1], (1, 1, 0, 0)) == (99, 70, 0, 0)

    embeddings = frozenset(range(4))
    star = [negative_embeddings(norm) for norm in norms]
    assert star == [{0, 1}, {1, 3}, {1, 2}]
    assert set(star) | {embeddings - edge for edge in star} == {
        frozenset(pair) for pair in combinations(embeddings, 2)
    }

    units = [(1, 1, 0, 0), (Fraction(5, 2), 0, Fraction(1, 2), 0), (-1, 0, 0, 0), eta]
    signatures = set()
    for exponents in product(range(2), repeat=4):
        value = one
        for exponent, unit in zip(exponents, units):
            if exponent:
                value = multiply(value, unit)
        signatures.add(negative_embeddings(value))
    assert len(signatures) == 16
    assert sum(len(s) % 2 == 0 for s in signatures) == 8
    print("Verified the relative norms, all six edges, eight even signatures and sixteen unit signatures.")


if __name__ == "__main__":
    check()
