#!/usr/bin/env python3
"""Independent exact integer verifier for the X6 signed C12 diagonal quotient."""
from itertools import product
from math import factorial
import json

N = 6
D = (1,) * N
ZERO = (0,) * N

def rotor(x):
    return (-x[-1],) + x[:-1]

def iterate(x, k):
    for _ in range(k):
        x = rotor(x)
    return x

def parity_class(x):
    bits = tuple(t % 2 for t in x)
    return tuple(b ^ bits[0] for b in bits[1:])

def in_M(x):
    return all((x[i] - x[0]) % 2 == 0 for i in range(N))

def q(x):
    return tuple(t - x[-1] for t in x[:-1])

def brc(x):
    k = sum(abs(a) for a in x)
    r = factorial(k)
    for a in x:
        r //= factorial(abs(a))
    return r

assert iterate(D, 6) == tuple(-v for v in D)
assert iterate(D, 12) == D
for k in range(1, 7):
    expected = tuple(-1 if i < k else 1 for i in range(N))
    assert iterate(D, k) == expected
    delta = tuple(iterate(D, k)[i] - iterate(D, k - 1)[i] for i in range(N))
    assert delta == tuple(-2 if i == k - 1 else 0 for i in range(N))

vectors = list(product(range(-2, 3), repeat=N))
for x in vectors:
    assert in_M(x) == (parity_class(x) == (0,) * (N - 1))
    assert in_M(rotor(x)) == in_M(x)
    assert parity_class(iterate(x, 6)) == parity_class(x)
    assert parity_class(rotor(x)) == parity_class(rotor(tuple(v % 2 for v in x)))
    assert sum(v*v for v in rotor(x)) == sum(v*v for v in x)
    assert brc(rotor(x)) == brc(x)

classes = set(parity_class(x) for x in product((0, 1), repeat=N))
assert len(classes) == 32
for k in range(1, 6):
    assert any(parity_class(iterate(x, k)) != parity_class(x)
               for x in product((0, 1), repeat=N))
assert all(parity_class(iterate(x, 6)) == parity_class(x)
           for x in product((0, 1), repeat=N))
assert q(D) == q(ZERO)
assert q(rotor(D)) != q(rotor(ZERO))
assert brc(ZERO) == 1 and brc(D) == 720
assert in_M(D) and in_M(tuple(2 if i == 0 else 0 for i in range(N)))

out = {
    "schema": "X6_UNIT166_C12_DIAGONAL_EQUIVARIANT_QUOTIENT_EXACT_V1",
    "unit": 166,
    "historical_pin": "fd2bcff10ca6e147348b6c1236027fc0d2877df3",
    "scientific_pin": "59538f585d037d09ef687b28715c4bc1a3f9fe03",
    "finite_integer_vectors": len(vectors),
    "induced_parity_classes": len(classes),
    "minimal_A_invariant_lattice_index": 32,
    "induced_A_order": 6,
    "rotor_native_order": 12,
    "diagonal_BRC": brc(D),
    "zero_BRC": brc(ZERO),
    "failures": 0,
    "scope": "exact finite checks; universal assertions separately proved in research note",
}
print(json.dumps(out, ensure_ascii=False, sort_keys=True, indent=2))
