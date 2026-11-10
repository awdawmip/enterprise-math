#!/usr/bin/env python3
"""Original W216 fourth-valuation band through p^5; author-side checker.

Scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
Three independent routes: p^5 hypergeometric recurrence, factorial p-unit
stripping, and first-order Wilson/harmonic digit transport.
No native H0/B0 calculation or research claim is made.
"""
import hashlib
import json
from math import isqrt


def target_primes(bound=10000):
    for p in range(13, bound + 1):
        if p % 24 in (13, 19) and all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def recurrence_top(p):
    m = (p - 1) // 6
    mod = p**5
    a = 1
    top, weighted = 0, 0
    for k in range(p):
        weighted = (weighted + (6*k+1)*a) % mod
        if k >= 4*m + 1:
            assert a % (p**3) == 0
            top = (top + (6*k+1)*a) % mod
        if k+1 < p:
            a = a*(2*k+1)*(3*k+1)*(3*k+2)
            a = a*pow(36*(k+1)**3, -1, mod) % mod
    assert top % p**3 == 0
    return top // p**3, weighted


def factorial_units_top(p, factorial_mod_p2):
    m = (p - 1) // 6
    mod = p*p
    unit = [1] * (3*p)
    for n in range(1, 3*p):
        factor = n//p if n % p == 0 else n
        unit[n] = unit[n-1] * factor % mod
    out = 0
    for k in range(4*m+1, 6*m+1):
        a_over_p3 = unit[2*k]*unit[3*k]
        a_over_p3 *= pow(216, -k, mod)*pow(factorial_mod_p2[k], -5, mod)
        out = (out + (6*k+1)*a_over_p3) % mod
    return out


def harmonic_wilson_top(p):
    m = (p - 1)//6
    mod = p*p
    fact = [1]*p
    harmonic = [0]*p
    for n in range(1, p):
        fact[n] = fact[n-1]*n % mod
        harmonic[n] = (harmonic[n-1] + pow(n, -1, p)) % p
    assert (fact[p-1] + 1) % p == 0
    wilson = ((fact[p-1] + 1)//p) % p
    base, harmonic_part = 0, 0
    for k in range(4*m+1, 6*m+1):
        x, y = 2*k-p, 3*k-2*p
        assert 0 <= x < p and 0 <= y < p
        b = (-2*fact[x]*fact[y]*pow(216, -k, mod)
             *pow(fact[k], -5, mod)) % mod
        weight = 6*k+1
        base = (base + weight*b) % mod
        harmonic_part = (harmonic_part
                         + (weight*b % p)*(harmonic[x]+2*harmonic[y])) % p
    f = base % p
    transported = (base+p*(harmonic_part-3*wilson*f)) % mod
    return transported, fact, (wilson, f, base, harmonic_part)


def run(bound=10000):
    rows = []
    special = {13, 19, 109, 139, 157, 163, 373, 997, 2131}
    for p in target_primes(bound):
        transfer, fact, components = harmonic_wilson_top(p)
        factorial = factorial_units_top(p, fact)
        recurrence, weighted = recurrence_top(p)
        assert recurrence == factorial == transfer, (p, recurrence, factorial, transfer)
        if p in special:
            print("p", p, "T/p^3 mod p^2", transfer, "F", transfer%p,
                  "next-digit", transfer//p, "wilson", components[0])
        rows.append({"p": p, "t_over_p3_mod_p2": transfer,
                     "F_mod_p": transfer%p, "G_digit_mod_p": transfer//p})
    serial = json.dumps(rows, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(serial.encode("utf-8")).hexdigest()
    print("cases", len(rows), "F-zeros", sum(r["F_mod_p"] == 0 for r in rows),
          "G-zeros", [r["p"] for r in rows if r["G_digit_mod_p"] == 0])
    print("row_sha256", digest)
    if bound == 10000:
        assert len(rows) == 312
        assert digest == "a135512864827fc7926a2a2672c2bbb207993d4abdb850854351d074d3ce3653"
        assert {r["p"] for r in rows if r["G_digit_mod_p"] == 0} == {2131}
    return rows


if __name__ == "__main__":
    run()
