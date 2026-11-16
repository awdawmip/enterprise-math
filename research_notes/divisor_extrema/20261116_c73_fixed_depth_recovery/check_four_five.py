"""Pure-Python controls for the four/five-block original single-readout proof.

Jacobian entries are exact first differences modulo p^2 for rational formulas.
Every reference to stock variables uses the integer landing, not its fourth root,
except the separate Jacobian test, performed in x_i=s_i^(1/4).
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement
from math import prod
import json

P = 1_000_000_007


def rising(x, n):
    return prod(x + i for i in range(n))


def roots_by_coordinate(r):
    rows = []
    for i in range(r):
        k = 2 * (r - i) + 1
        shifts = [Fraction(k - 1)]
        if i > 0:
            shifts.extend([Fraction(k - 1, 4), *range(k, 4 * k)])
        if i < r - 1:
            shifts.extend(range(k - 1, 4 * (k - 2) + 1))
        else:
            shifts.extend([2, 3, 4])
        rows.append(Counter(shifts))
    return rows


def primitive_values(raw, zs):
    values = {1: 1, 2: 1}
    for shifts, z in zip(raw, zs):
        for shift, multiplicity in shifts.items():
            values[multiplicity] *= shift.denominator * z + shift.numerator
    return values


def raw_center(c, zs, modulus=None):
    def red(n):
        return n if modulus is None else n % modulus

    r = len(zs)
    v = (zs[-1] + 2) * (zs[-1] + 3) * (zs[-1] + 4)
    edges = []
    for i, (previous, z) in enumerate(zip((c, *zs), zs)):
        k = 2 * (r - i) + 1
        edges.append((red((z + k - 1) * rising(previous + k + 1, 3 * k)),
                      red(28 * (4 * z + k - 1) * rising(z + k, 3 * k))))
    raw_columns = []
    tail_denominators = []
    for j in (1, 10):
        a, b = 1680, red(1680 + j * v)
        for n, d in reversed(edges[1:]):
            a, b = red(d * b), red(d * b + n * a)
        tail_denominators.append(b)
        n, d = edges[0]
        raw_columns.append((red(d * b), red(d * b + n * a)))
    a, b = raw_columns[0]
    aa, bb = raw_columns[1]
    orientation = 1 if r % 2 == 0 else -1
    # For even r, X_d/X_D>1, with denominator A_D B_d.
    dcol = 1 if orientation == 1 else 0
    denominator = red(tail_denominators[dcol] * raw_columns[1 - dcol][1])
    numerator = red(1680 * 9 * v * (zs[0] + 2 * r) * prod(n * d for n, d in edges[1:]))
    if modulus is None:
        assert Fraction(numerator, denominator) == (max(Fraction(a * bb, aa * b), Fraction(aa * b, a * bb)) - 1) / rising(c + 2 * r + 2, 3 * (2 * r + 1))
    return numerator, denominator


def rank_observables(values, profile, modulus):
    def inv(x):
        return pow(x % modulus, -1, modulus)

    r = len(values)
    xs = [1, *values]
    real = center = 0
    real_derivative = center_derivative = 1
    for i in range(r, 0, -1):
        k = 2 * (r - i) + 3
        rate = 4 * pow(xs[i] * inv(xs[i - 1]), 3 * k, modulus) % modulus
        scale = 7 * inv(16) * pow(rate, 5, modulus) % modulus
        alpha = rate * inv(scale) % modulus
        deninv = inv(1 + scale * real)
        real_derivative = real_derivative * scale * (1 - rate) * deninv**2 % modulus
        real = (rate + scale * real) * deninv % modulus
        deninv = inv(1 + alpha * center)
        center_derivative = -center_derivative * alpha * deninv**2 % modulus
        center = deninv
    rows = [real_derivative * inv(xs[-1]**3 * real) % modulus,
            center_derivative * inv(xs[-1]**12 * center) % modulus]
    for exponents in profile:
        rows.append(prod(pow(x, 4 * e, modulus) for x, e in zip(values, exponents)) % modulus)
    gaps = [(xs[i]**4 - xs[i + 1]**4) % modulus for i in range(r)]
    return rows + gaps + [xs[-1]**4 % modulus]


def det(matrix):
    work = [row.copy() for row in matrix]
    result = 1
    for col in range(len(work)):
        pivot = next((j for j in range(col, len(work)) if work[j][col] % P), None)
        if pivot is None:
            return 0
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            result = -result
        factor = work[col][col] % P
        result = result * factor % P
        for j in range(col + 1, len(work)):
            multiplier = work[j][col] * pow(factor, -1, P) % P
            work[j] = [(a - multiplier * b) % P for a, b in zip(work[j], work[col])]
    return result


def controls(r):
    rows = roots_by_coordinate(r)
    assert max(max(row.values()) for row in rows) == 2
    profile = [[sum(n == m for n in row.values()) for row in rows] for m in (1, 2)]
    constant = raw_center(7, (3,) * r)[0]
    at_three = primitive_values(rows, (3,) * r)
    constant, rem = divmod(constant, at_three[1] * at_three[2]**2)
    assert rem == 0
    checked = 0
    for c in (4, 5, 6, 7, 8):
        for points in combinations_with_replacement(range(2, c + 1), r):
            zs = points[::-1]
            numerator, denominator = raw_center(c, zs)
            vals = primitive_values(rows, zs)
            assert numerator == constant * vals[1] * vals[2]**2
            checked += 1
    certs = []
    for j, row in enumerate(rows):
        for shift in sorted(row):
            zs = [137 + i * 11 for i in range(r)]
            zs[j] = -shift.numerator * pow(shift.denominator, -1, P) % P
            numerator, denominator = raw_center(379, zs, P)
            assert numerator == 0 and denominator != 0
            certs.append([j + 1, str(shift), denominator])
    q = P**2
    xs = [(13 - i) * pow(13 + i, -1, q) % q for i in range(1, r + 1)]
    orig = rank_observables(xs, profile, q)
    columns = []
    for i in range(r):
        displaced = xs.copy()
        displaced[i] += P
        diffs = [(v - u) % q for u, v in zip(orig, rank_observables(displaced, profile, q))]
        assert all(v % P == 0 for v in diffs)
        columns.append([v // P for v in diffs])
    jac = [list(row) for row in zip(*columns)]
    results = [det(jac[:4])] if r == 4 else [det(jac[:4] + [gap]) for gap in jac[4:]]
    expected = [858880007] if r == 4 else [919344456, 516372049, 677251760, 983856906, 537999365, 365175492]
    assert results == expected
    return dict(depth=r, raw_factor_profiles=profile, raw_factor_constant=constant,
                exact_integer_stocks_checked=checked, jacobian_rows_mod_p=jac,
                rank_determinants_mod_p=results, denominator_nonzero_certificates=certs)


if __name__ == '__main__':
    print(json.dumps(dict(prime=P, controls=[controls(4), controls(5)]), indent=2))
