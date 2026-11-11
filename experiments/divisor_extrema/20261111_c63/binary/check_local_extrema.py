"""Exact polynomial certificates for the band theorem and binary runner-up."""
from fractions import Fraction
from math import prod
import json

from sympy import Poly, symbols


x = symbols("x")


def scaled_weights(r, offset, m):
    """Return a common positive scaling of 7*q0, q1, q2, for r numeric or Poly."""
    c = r + 1 + offset
    kappa = 2 * r + 1
    after_one = kappa + c - m
    after_four = kappa + 4 * (c - m)
    denom_zero = prod(4 * kappa + c - j for j in range(m + 1)) * (after_one - 1)
    denom_one = prod(kappa + c - j for j in range(m + 1)) * (after_four - 1)
    denom_two = prod(kappa + 4 * (c - j) for j in range(m + 1)) * (after_four - 1)
    return (28 * denom_one * denom_two, denom_zero * denom_two,
            4 ** m * denom_zero * denom_one)


def check_polynomial(r0, offset, m, power, multiplier, target):
    """Verify min |F'| > target / (multiplier * r**power) for all r >= r0."""
    r = Poly(x + r0, x)
    a, b, c = scaled_weights(r, offset, m)
    sign = 1 if (b - c).nth(0) > 0 else -1
    diff = sign * (b - c)
    first = multiplier * r ** power * a * diff - target * (a + b) ** 2
    second = multiplier * r ** power * a * diff - target * (a + c) ** 2
    for poly in (diff, first, second):
        assert min(poly.all_coeffs()) > 0, (r0, offset, m, poly)
    return {"offset": offset, "m": m, "r_min": r0, "sign_q1_minus_q2": sign,
            "polynomial_degrees": [p.degree() for p in (diff, first, second)]}


def derivative_range(r, offset, m):
    a, b, c = scaled_weights(r, offset, m)
    return (Fraction(a * abs(b - c), (a + max(b, c)) ** 2),
            Fraction(a * abs(b - c), (a + min(b, c)) ** 2))


def tail_lower(length):
    z = (Fraction(1, 4), Fraction(1), Fraction(4))
    weights = [prod((j + 2) * t / (1 + (j + 2) * t) for j in range(1, length + 1))
               for t in z]
    zero, one, two = weights
    return Fraction(8 * one, 7 * zero + two)


def main():
    band = []
    for offset in range(-2, 3):
        for m in range(6):
            if abs(offset + 1 - m) <= 2 and (offset, m) != (0, 1):
                r0 = max(2, 1 + m - offset)
                band.append(check_polynomial(r0, offset, m, 2, 100, 3))
    assert len(band) == 18

    binary_blocks = ((0, 0), (1, 0), (2, 0), (1, 1), (2, 1))
    binary = [check_polynomial(2, offset, m, 1, 50, 1) for offset, m in binary_blocks]
    tails = [tail_lower(m) for m in range(3)]
    assert tails == [1, Fraction(26, 17), Fraction(3536, 1745)]
    terminal = {}
    for offset in range(3):
        for m in range(offset + 1):
            lo, hi = derivative_range(1, offset, m)
            assert lo * tails[offset - m] > Fraction(1, 100)
            terminal[f"{offset},{m}"] = {"internal_min": str(lo), "internal_max": str(hi),
                                          "full_min": str(lo * tails[offset - m])}
    base_lo, base_hi = derivative_range(1, 0, 0)
    for offset, m in ((1, 0), (1, 1), (2, 1)):
        assert derivative_range(1, offset, m)[0] * tails[offset - m] > base_hi
    assert Fraction(5, 6) * 3 / (100 * base_hi) > 1

    runner_upper = (derivative_range(2, 0, 0)[1] / derivative_range(2, 0, 1)[0]
                    * derivative_range(1, 1, 1)[1] / base_lo)
    competitor_lower = tails[1] * derivative_range(1, 1, 0)[0]
    assert competitor_lower > derivative_range(1, 1, 1)[1]
    assert runner_upper == Fraction(6469632000, 390606491) < 17
    print(json.dumps({"band_certificates": band, "binary_certificates": binary,
                      "tail_TV_multipliers": [str(v) for v in tails],
                      "terminal_bounds": terminal, "binary_runner_ratio_upper": str(runner_upper),
                      "status": "PASS"}, indent=2))


if __name__ == "__main__":
    main()
