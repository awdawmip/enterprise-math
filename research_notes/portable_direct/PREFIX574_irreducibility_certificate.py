#!/usr/bin/env python3
"""PREFIX-574: gate-aware BRC annihilator irreducibility and the z=1 core defect.

Frozen science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Reconstructs the pinned 4-STAR / 96-port / 6-action X6-BRC source, the
37-class gate-preserving weighted quotient, and the PREFIX-572 14-degree
annihilator. Requires Python 3 and SymPy. All algebra is exact; the finite-field
irreducibility certificate uses modular integer polynomial arithmetic.
"""
from collections import Counter, deque
from itertools import product
import hashlib
import json
import sympy as S

SCIENCE_PIN = "f42f2906d77f24085c123f3ccfe9667d41caa96d"
P = 1000003
STARS = ((1, 3, 6), (1, 4, 5), (2, 3, 5), (2, 4, 6))
ACTIONS = tuple(product(range(3), (0, 1)))
ZERO_ROOT = (0,) * 6
ROOTS = (ZERO_ROOT,) + tuple(
    tuple(sign if j == axis else 0 for j in range(6))
    for axis in range(4) for sign in (-1, 1)
)

def near(star, current):
    return tuple((-1 if current > 0 else 1) * k
                 for k in STARS[star] if k != abs(current))

PHASES = tuple(
    (a, prev, sign * k)
    for a in range(4)
    for k in STARS[a]
    for sign in (-1, 1)
    for prev in near(a, sign * k)
)
PHASE_INDEX = {phase: i for i, phase in enumerate(PHASES)}

def successors(phase):
    a, prev, current = PHASES[phase]
    b = next(b for b in range(4)
             if b != a and abs(current) in STARS[b])
    targets = (
        [(a, current, k) for k in near(a, current) if k != prev]
        + [(b, current, k) for k in near(b, current)]
    )
    return tuple(PHASE_INDEX[t] for t in targets)

NEXT = tuple(successors(i) for i in range(48))
TARGET = PHASE_INDEX[(0, 1, -3)]

def sign_on_axis(phase, axis):
    current = PHASES[phase][2]
    return (1 if current > 0 else -1) if abs(current) == axis else 0

def native_edge(port, action, root):
    phase, bit = divmod(port, 2)
    slot, new_bit = action
    nxt = NEXT[phase][slot]
    weights = []
    for axis in range(1, 7):
        left = sign_on_axis(phase, axis)
        right = sign_on_axis(nxt, axis)
        r = root[axis - 1]
        value = abs(left) + abs(right) - abs(right - r) + abs(left - r)
        assert value in (0, 2)
        weights.append(value // 2)
    gate = int(bit == new_bit == 1 and nxt == TARGET)
    return 2 * nxt + new_bit, tuple(weights) + (gate,)

def native_rows(root):
    return [
        Counter((target, weights[4], weights[5], weights[6])
                for action in ACTIONS
                for target, weights in [native_edge(port, action, root)])
        for port in range(96)
    ]

def weighted_quotient(rows):
    ids = [0] * len(rows)
    growth = [1]
    for _ in range(len(rows)):
        keys = []
        for row in rows:
            out = Counter()
            for (target, a, b, gate), multiplicity in row.items():
                out[(ids[target], a, b, gate)] += multiplicity
            keys.append(tuple(sorted(out.items())))
        lookup = {}
        new_ids = [lookup.setdefault(key, len(lookup)) for key in keys]
        if new_ids == ids:
            break
        ids = new_ids
        growth.append(len(lookup))
    else:
        raise AssertionError("weighted partition did not stabilize")

    quotient = {}
    for i, row in enumerate(rows):
        out = Counter()
        for (target, a, b, gate), multiplicity in row.items():
            out[(ids[target], a, b, gate)] += multiplicity
        if ids[i] in quotient:
            assert quotient[ids[i]] == out
        else:
            quotient[ids[i]] = out
    return ids, tuple(quotient[i] for i in range(len(quotient))), growth

def symmetrize_xy(expr, x, y, u, v):
    symmetric, remainder, symbols = S.symmetrize(expr, [x, y], formal=True)
    assert remainder == 0
    return S.expand(symmetric.subs({
        symbols[0][0]: u,
        symbols[1][0]: v
    }))

def trim_mod(poly, p):
    poly = [int(c) % p for c in poly]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly

def sub_mod(a, b, p):
    n = max(len(a), len(b))
    return trim_mod([
        ((a[i] if i < len(a) else 0)
         - (b[i] if i < len(b) else 0)) % p
        for i in range(n)
    ], p)

def mul_mod_poly(a, b, modulus_poly, p):
    a = trim_mod(a, p)
    b = trim_mod(b, p)
    n = len(modulus_poly) - 1
    product_poly = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            product_poly[i + j] = (
                product_poly[i + j] + ai * bj
            ) % p
    for k in range(len(product_poly) - 1, n - 1, -1):
        lead = product_poly[k] % p
        if lead:
            shift = k - n
            for j in range(n + 1):
                product_poly[shift + j] = (
                    product_poly[shift + j] - lead * modulus_poly[j]
                ) % p
    return trim_mod(product_poly[:n], p)

def pow_mod_poly(base, exponent, modulus_poly, p):
    result = [1]
    base = trim_mod(base, p)
    while exponent:
        if exponent & 1:
            result = mul_mod_poly(result, base, modulus_poly, p)
        base = mul_mod_poly(base, base, modulus_poly, p)
        exponent //= 2
    return trim_mod(result, p)

def divmod_mod_poly(a, b, p):
    a = trim_mod(a, p)
    b = trim_mod(b, p)
    if b == [0]:
        raise ZeroDivisionError
    inverse_lead = pow(b[-1], -1, p)
    while len(a) >= len(b) and a != [0]:
        factor = a[-1] * inverse_lead % p
        shift = len(a) - len(b)
        for j in range(len(b)):
            a[shift + j] = (a[shift + j] - factor * b[j]) % p
        a = trim_mod(a, p)
    return trim_mod(a, p)

def gcd_mod_poly(a, b, p):
    a = trim_mod(a, p)
    b = trim_mod(b, p)
    while b != [0]:
        a, b = b, divmod_mod_poly(a, b, p)
    inverse_lead = pow(a[-1], -1, p)
    return trim_mod([c * inverse_lead % p for c in a], p)

def rabin_irreducibility_certificate(poly, variable, p, specialization):
    assert S.isprime(p)
    specialized = S.Poly(
        S.expand(poly.as_expr().subs(specialization)),
        variable, modulus=p
    )
    degree = specialized.degree()
    assert degree == 14 and int(specialized.LC()) % p == 1
    f = [int(specialized.nth(i)) % p for i in range(degree + 1)]
    x = [0, 1]
    frobenius = {}
    current = x
    for k in range(1, degree + 1):
        current = pow_mod_poly(current, p, f, p)
        if k in (2, 7, 14):
            frobenius[k] = current
    gcd2 = gcd_mod_poly(f, sub_mod(frobenius[2], x, p), p)
    gcd7 = gcd_mod_poly(f, sub_mod(frobenius[7], x, p), p)
    passed = (
        frobenius[14] == x
        and gcd2 == [1]
        and gcd7 == [1]
    )
    assert passed
    return {
        "prime": p,
        "formal_parameter_specialization": {str(k): int(v) for k, v in specialization.items()},
        "degree": degree,
        "monic": True,
        "polynomial_coefficients_ascending_mod_p": f,
        "x_p2_mod_f": frobenius[2],
        "x_p7_mod_f": frobenius[7],
        "x_p14_mod_f": frobenius[14],
        "gcd_f_x_p2_minus_x": gcd2,
        "gcd_f_x_p7_minus_x": gcd7,
        "rabin_irreducible": True
    }

