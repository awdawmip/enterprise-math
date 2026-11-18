"""Finite certificates for the marked P11 three-division field. Python 3.8+."""
from collections import Counter
from itertools import product
from math import isqrt
import json

P, Q = 233, 119
A, B = -(P * P + Q * Q), (P * Q) ** 2
HX, HY = 194089, 69872040


def cubic(x):
    return x ** 3 + A * x ** 2 + B * x


def psi3(x):
    return 3 * x ** 4 + 4 * A * x ** 3 + 6 * B * x ** 2 - B ** 2


def marked_polynomial(x):
    r = (x ** 6 + 2 * A * x ** 5 + 5 * B * x ** 4
         - 5 * B ** 2 * x ** 2 - 2 * A * B ** 2 * x - B ** 3)
    return (x - HX) * psi3(x) ** 2 - 8 * cubic(x) * r


def trim(poly, p):
    result = [c % p for c in poly]
    while result and result[-1] == 0:
        result.pop()
    return result


def remainder(poly, modulus, p):
    result = trim(poly, p)
    while len(result) >= len(modulus):
        shift = len(result) - len(modulus)
        factor = result[-1] * pow(modulus[-1], -1, p) % p
        for i, coefficient in enumerate(modulus):
            result[shift + i] -= factor * coefficient
        result = trim(result, p)
    return result


def torsion_certificate():
    raw = [-B ** 2, 0, 6 * B, 4 * A, 3]
    monic = {p: trim([c * pow(3, -1, p) for c in raw], p) for p in (13, 41)}
    cubic13 = [-2, 4, -5, 1]
    verify_product = [0] * 5
    for i, c in enumerate(cubic13):
        verify_product[i] -= 6 * c
        verify_product[i + 1] += c
    assert trim(verify_product, 13) == monic[13]
    assert all(sum(c * x ** i for i, c in enumerate(cubic13)) % 13
               for x in range(13))

    quartic = monic[41]
    assert quartic == trim([-15, 0, -4, 13, 1], 41)
    residue = [1]
    for _ in range(41 ** 2):
        residue = remainder([0] + residue, quartic, 41)
    assert residue == trim([5, 6, 9, -16], 41)
    u, v = quartic, trim([residue[0], residue[1] - 1, *residue[2:]], 41)
    while v:
        u, v = v, remainder(u, v, 41)
    assert len(u) == 1
    return {"13_monic_factors_ascending": [[7, 1], trim(cubic13, 13)],
            "41_monic_quartic_ascending": quartic,
            "41_X_to_1681_remainder_ascending": residue,
            "41_monic_gcd_with_X_to_1681_minus_X": [1]}


def add(left, right, p):
    if left is None:
        return right
    if right is None:
        return left
    x, y = left
    u, v = right
    if x == u and (y + v) % p == 0:
        return None
    if x == u:
        slope = (3 * x ** 2 + 2 * A * x + B) * pow(2 * y, -1, p)
    else:
        slope = (v - y) * pow(u - x, -1, p)
    z = (slope ** 2 - A - x - u) % p
    return z, (slope * (x - z) - y) % p


def local_certificate(p, expected):
    assert 6 * P * Q * (P ** 2 - Q ** 2) * HY % p != 0
    assert all(p % d for d in range(2, isqrt(p) + 1))
    h = HX % p, HY % p
    roots_by_square = {}
    for y in range(p):
        roots_by_square.setdefault(y * y % p, []).append(y)
    order = 1
    solutions = []
    for x in range(p):
        for y in roots_by_square.get(cubic(x) % p, ()):
            order += 1
            point = x, y
            if add(add(point, point, p), point, p) == h:
                solutions.append(point)
    poly_roots = [x for x in range(p) if marked_polynomial(x) % p == 0]
    assert poly_roots == [x for x, _ in solutions] and len(solutions) == expected
    out = {"H": h, "group_order": order, "preimages_by_group_law": solutions,
           "roots_by_polynomial": poly_roots}
    if p == 23:
        power = h
        powers = []
        for _ in range(3):
            power = add(power, power, p)
            powers.append(power)
        assert order == 24 and powers[-1] == (2, 9)
        out["H_doubled_three_times"] = powers
    return out


def affine_counts():
    vectors = list(product(range(3), repeat=2))
    result = {1: Counter(), 2: Counter()}
    for a, b, c, d in product(range(3), repeat=4):
        determinant = (a * d - b * c) % 3
        if determinant:
            for u, v in vectors:
                fixed = sum((a * x + b * y + u - x) % 3 == 0 and
                            (c * x + d * y + v - y) % 3 == 0 for x, y in vectors)
                result[determinant][fixed] += 1
    total = result[1] + result[2]
    assert total == {0: 128, 1: 243, 3: 60, 9: 1}
    assert sum(total.values()) == 432
    return {"by_determinant": result, "total": total}


if __name__ == "__main__":
    data = {"parameters": [P, Q], "H": [HX, HY], "linear_certificates": torsion_certificate(),
            "affine_fixed_counts": affine_counts(), "local_witnesses":
            {p: local_certificate(p, n) for p, n in [(13, 1), (41, 1), (23, 0),
                                                      (89, 3), (2833, 9)]}}
    print(json.dumps(data, sort_keys=True, indent=2))
