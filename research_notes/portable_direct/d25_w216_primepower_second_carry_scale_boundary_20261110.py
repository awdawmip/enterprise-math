#!/usr/bin/env python3
"""W216 exact prime-power second-carry checks; author-side, not native H0/B0.

Only Python integers and modular inverse of p-units. Two independent coefficient
constructions: factorial-unit arrays and forward p-adic coefficient recurrence.
All arithmetic is modulo p**(3*r+2) for each r. No floating point.
"""
from __future__ import annotations

def strip_p(x: int, p: int) -> tuple[int, int]:
    v = 0
    while x % p == 0:
        x //= p
        v += 1
    return x, v

def W_factorial(p: int, r: int, exp: int) -> int:
    n, modulus = p**r, p**exp
    limit = 3 * (n - 1)
    valuation = [0] * (limit + 1)
    fact_unit = [1] * (limit + 1)
    for i in range(1, limit + 1):
        u, v = strip_p(i, p)
        valuation[i] = valuation[i-1] + v
        fact_unit[i] = fact_unit[i-1] * u % modulus
    inverse = [0] * (limit + 1)
    inverse[limit] = pow(fact_unit[limit], -1, modulus)
    for i in range(limit, 0, -1):
        u, _ = strip_p(i, p)
        inverse[i-1] = inverse[i] * u % modulus
    inverse_216 = pow(216, -1, modulus)
    power_216 = 1
    power_p = [p**i for i in range(exp + 1)]
    answer = 0
    for k in range(n):
        v = valuation[2*k] + valuation[3*k] - 5 * valuation[k]
        assert v >= 0, ("negative v_p(A_k)", p, k, v)
        if v < exp:
            unit = fact_unit[2*k] * fact_unit[3*k] % modulus
            unit = unit * pow(inverse[k], 5, modulus) % modulus
            ak = unit * power_216 % modulus * power_p[v] % modulus
            answer = (answer + (6*k+1)*ak) % modulus
        power_216 = power_216 * inverse_216 % modulus
    return answer

def W_recurrence(p: int, r: int, exp: int) -> int:
    n, modulus = p**r, p**exp
    u, v, answer = 1, 0, 0
    inv36 = pow(36, -1, modulus)
    powers = [p**i for i in range(exp + 1)]
    for k in range(n):
        assert v >= 0
        if v < exp:
            answer = (answer + (6*k+1) * u * powers[v]) % modulus
        top, vt = strip_p((2*k+1)*(3*k+1)*(3*k+2), p)
        bot, vb = strip_p(k+1, p)
        v += vt-3*vb
        u = u * (top % modulus) % modulus
        u = u * pow(bot, -3, modulus) % modulus
        u = u * inv36 % modulus
    return answer

def witness(p: int, r: int, method) -> int:
    exp = 3*r + 2
    chi = 1 if p % 3 == 1 else -1
    w = method(p, r, exp)
    prev = method(p, r-1, exp) if r > 1 else 1
    remainder = (w - chi*p*prev) % p**exp
    assert remainder % p**(3*r) == 0, (p, r, "valuation")
    return remainder // p**(3*r)

CASES = {
    13: [126, 61, 61, 61],
    19: [88, 297, 297, 297],
    37: [537, 870, 870],
    43: [1266, 1438, 1438],
    61: [373, 2447, 2447],
    67: [3941, 591, 591],
}
def main() -> None:
    for p, expectations in CASES.items():
        for r, expected in enumerate(expectations, start=1):
            a = witness(p, r, W_factorial)
            b = witness(p, r, W_recurrence)
            assert a == b == expected, (p, r, a, b, expected)
            print(f"p={p} r={r} p**r={p**r} E(mod p**2)={a}: PASS")
    for p in [13,19]:
        assert CASES[p][0] != CASES[p][1]
        assert CASES[p][0] % p == CASES[p][1] % p
    print("Verified: two target-class counterexamples to r=1 second-carry lift.")
    print("Stable r>=2 second-carry at sampled scales is CONJECTURAL globally.")

if __name__ == "__main__":
    main()
