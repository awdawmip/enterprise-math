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

def main():
    assert len(PHASES) == 48 and len(ACTIONS) == 6
    assert len(ROOTS) == 9
    rows = native_rows(ZERO_ROOT)
    for root in ROOTS:
        assert native_rows(root) == rows
    ids, quotient, growth = weighted_quotient(rows)
    assert len(ids) == 96
    assert (len(quotient), growth) == (37, [1, 4, 13, 21, 33, 37])

    adjacency = [set() for _ in quotient]
    for i, row in enumerate(quotient):
        for (target, a, b, gate), multiplicity in row.items():
            if multiplicity:
                adjacency[i].add(target)
                adjacency[target].add(i)
    color = [None] * 37
    for start in range(37):
        if color[start] is not None:
            continue
        color[start] = 0
        todo = deque([start])
        while todo:
            i = todo.popleft()
            for j in adjacency[i]:
                if color[j] is None:
                    color[j] = color[i] ^ 1
                    todo.append(j)
                else:
                    assert color[j] != color[i]
    left = [i for i in range(37) if color[i] == 0]
    right = [i for i in range(37) if color[i] == 1]
    assert (len(left), len(right)) == (17, 20)
    left_index = {state: i for i, state in enumerate(left)}
    right_index = {state: i for i, state in enumerate(right)}

    x, y, z, lam, u, v = S.symbols("x y z L u v")
    A = S.zeros(17, 20)
    B = S.zeros(20, 17)
    gate_sources = Counter()
    for i, row in enumerate(quotient):
        for (j, a, b, gate), multiplicity in row.items():
            term = multiplicity * x**a * y**b * z**gate
            if color[i] == 0:
                A[left_index[i], right_index[j]] += term
            else:
                B[right_index[i], left_index[j]] += term
            if gate:
                assert j == 5 and a == b == 0
                gate_sources[i] += multiplicity
    assert gate_sources == Counter({4: 1, 15: 1, 17: 1})

    characteristic = (A * B).charpoly(lam).as_expr()
    symmetric_characteristic = 0
    for (degree_lam, degree_z), coefficient in S.Poly(
        characteristic, lam, z
    ).terms():
        symmetric_characteristic += (
            symmetrize_xy(coefficient, x, y, u, v)
            * lam**degree_lam * z**degree_z
        )
    symmetric_characteristic = S.expand(symmetric_characteristic)
    cubic = lam**3 + 4*lam**2 - (32*u + 16*v)*lam + 192*v
    q14_quotient, cubic_remainder = S.div(
        S.Poly(symmetric_characteristic, lam),
        S.Poly(cubic, lam)
    )
    assert cubic_remainder.is_zero
    Q14_L = S.Poly(q14_quotient.as_expr(), lam)
    Q14 = S.Poly(q14_quotient.as_expr(), lam, u, v, z)
    assert Q14.degree(lam) == 14 and Q14.LC() == 1
    assert len(S.Poly(symmetric_characteristic, lam, u, v, z).terms()) == 258
    assert len(Q14.terms()) == 159

    expected = (
        {(0, 0, 0): 2, (2, 0, 0): 2, (4, 0, 0): 2},
        {(0, 0, 0): 4, (4, 0, 0): 2},
        {(1, 0, 1): 6},
        {(0, 0, 0): 4, (2, 0, 0): 2},
        {(3, 1, 0): 6},
    )
    M5 = S.zeros(5, 5)
    for i, row in enumerate(expected):
        for (j, ax, ay), multiplicity in row.items():
            M5[i, j] += multiplicity * x**ax * y**ay
    chi5_squared_xy = S.expand((M5**2).charpoly(lam).as_expr())
    Q5_expr = symmetrize_xy(chi5_squared_xy, x, y, u, v)
    Q5 = S.Poly(Q5_expr, lam, u, v)

    Q3_expr = lam**3 + 4*lam**2 - (32*u + 16*v)*lam + 192*v
    S5_expr = (
        lam**5 - 4*lam**4 + 64*u*lam**3 - 32*v*lam**3
        - 256*u**2*lam**2 - 384*v*lam**2
        + 3072*u*v*lam + 256*v**2*lam - 9216*v**2
    )
    R9_expected = (lam - 4) * Q3_expr * S5_expr
    Q14_z1 = S.Poly(S.expand(Q14.as_expr().subs(z, 1)), lam, u, v)
    S9_at_z1, rem_z1 = S.div(Q14_z1, Q5)
    assert rem_z1.is_zero and S9_at_z1.degree(lam) == 9
    assert S.expand(S9_at_z1.as_expr() - R9_expected) == 0

    S9_generic, generic_remainder = S.div(
        Q14,
        S.Poly(Q5_expr, lam, u, v, z)
    )
    R4 = S.Poly(
        S.cancel(generic_remainder.as_expr() / (z - 1)),
        lam, u, v, z
    )
    assert S.expand(
        generic_remainder.as_expr() - (z - 1) * R4.as_expr()
    ) == 0
    assert R4.degree(lam) == 4 and R4.degree(z) == 0
    assert len(R4.terms()) == 106
    r4_witness = R4.coeff_monomial(lam**4 * u**2)
    assert r4_witness == -12582912
    assert S9_generic.degree(lam) == 9 and len(S9_generic.terms()) == 131
    assert S.expand(S9_generic.as_expr().subs(z, 1) - R9_expected) == 0

    coefficients = [
        S.Poly(S.expand(Q14_L.nth(14 - j)), u, v, z)
        for j in range(15)
    ]
    c2 = S.factor(coefficients[2].as_expr())
    companion_c2 = S.expand(-coefficients[2].as_expr())
    assert S.expand(c2 - (-4*(2*u*z + 38*u + 84*v + z - 1))) == 0
    constant_companion_c2 = S.Poly(companion_c2, u, v, z).coeff_monomial(1)
    assert constant_companion_c2 == -4
    # Direct sparse-monomial check for every first-row companion coefficient.
    standard_orthant_invariant = True
    orthant_witness = None
    for j in range(1, 15):
        companion = S.Poly(-coefficients[j].as_expr(), u, v, z)
        for monomial, coefficient in companion.terms():
            if coefficient < 0:
                standard_orthant_invariant = False
                orthant_witness = {
                    "lag": j,
                    "monomial_uvz": list(monomial),
                    "coefficient": int(coefficient)
                }
                break
        if orthant_witness:
            break
    assert not standard_orthant_invariant
    assert orthant_witness == {
        "lag": 2, "monomial_uvz": [0, 0, 0], "coefficient": -4
    }

    rabin = rabin_irreducibility_certificate(
        Q14, lam, P, {u: 9, v: 26, z: 13}
    )
    assert rabin["rabin_irreducible"]

    expressions = {
        "Q14": str(S.expand(Q14.as_expr())),
        "Q5": str(S.expand(Q5_expr)),
        "R9_at_z1": str(S.expand(R9_expected)),
        "S5": str(S.expand(S5_expr)),
        "S9_generic_quotient": str(S.expand(S9_generic.as_expr())),
        "R4_generic_division_defect": str(S.expand(R4.as_expr()))
    }
    hashes = {
        name: hashlib.sha256(value.encode("utf-8")).hexdigest()
        for name, value in expressions.items()
    }
    sign_profile = []
    for j in range(15):
        terms = coefficients[j].terms()
        sign_profile.append({
            "lag": j,
            "monomial_terms": len(terms),
            "positive_terms": sum(1 for _, c in terms if c > 0),
            "negative_terms": sum(1 for _, c in terms if c < 0)
        })

    return {
        "status": "ALL_CHECKS_PASS",
        "science_pin": SCIENCE_PIN,
        "source_model": "frozen four-STAR native X6-BRC, 96 ordered ports, 6 actions",
        "roots": len(ROOTS),
        "native_ports": 96,
        "weighted_quotient_classes": len(quotient),
        "partition_growth": growth,
        "bipartition": [len(left), len(right)],
        "gate_sources": [4, 15, 17],
        "gate_target": 5,
        "characteristic_terms": len(
            S.Poly(symmetric_characteristic, lam, u, v, z).terms()
        ),
        "Q14_degree": Q14.degree(lam),
        "Q14_terms": len(Q14.terms()),
        "generic_irreducibility": {
            "field": "Q(u,v,z)",
            "proof": "monic specialization irreducible over F_1000003 via Rabin criterion",
            **rabin
        },
        "z_equals_1_core": {
            "Q5_is_charpoly_of_five_state_M_squared": True,
            "Q14_specialization_divides_exactly_by_Q5": True,
            "remainder_zero": True,
            "R9_degree": S9_at_z1.degree(lam),
            "R9_factorization": "(L-4)*Q3(L)*S5(L)",
            "Q5": str(S.expand(Q5_expr)),
            "Q3": str(S.expand(Q3_expr)),
            "S5": str(S.expand(S5_expr))
        },
        "generic_core_lift_obstruction": {
            "identity": "Q14 = Q5*S9_generic + (z-1)*R4",
            "Q5_divides_generic_Q14": False,
            "generic_remainder_factor": "z-1",
            "R4_degree_L": R4.degree(lam),
            "R4_degree_z": R4.degree(z),
            "R4_terms": len(R4.terms()),
            "R4_coefficient_L4_u2": int(r4_witness),
            "S9_generic_degree_L": S9_generic.degree(lam),
            "S9_generic_terms": len(S9_generic.terms())
        },
        "standard_companion_cone": {
            "c2": str(c2),
            "minus_c2": str(companion_c2),
            "standard_nonnegative_orthant_invariant": False,
            "first_negative_entry": orthant_witness
        },
        "Q14_coefficient_sign_profile": sign_profile,
        "exact_polynomial_sha256": hashes,
        "exact_polynomials": expressions,
        "next_question": (
            "Construct a genuinely gate-sensitive 14-dimensional invariant cone "
            "or prove its minimum positive-realization dimension; the fixed z=1 "
            "five-state factor does not lift, and the standard scalar companion "
            "orthant is not invariant."
        )
    }

if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=2))
