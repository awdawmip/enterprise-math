#!/usr/bin/env python3
"""
Exact regression for the D25 supersingular ASD visibility no-go.

This checker supports, but does not replace, the proof in
d25_supersingular_asd_visibility_no_go_20260924.md.

It verifies for target primes below a bound:
  * determinant-compatible finite lifts;
  * first-order coefficient comparisons;
  * the product-second-digit formula FROB2 = U^2-e_a-e_b mod p;
  * an explicit p^2 perturbation of the p-1 coefficient that preserves
    every possible ASD occurrence modulus but changes FROB2 by the
    prescribed gauge parameter.
"""

from math import gcd

def inv(a, p2):
    return pow(a % p2, -1, p2)

def primes(n):
    out = []
    for x in range(2, n + 1):
        ok = True
        d = 2
        while d * d <= x:
            if x % d == 0:
                ok = False
                break
            d += 1
        if ok:
            out.append(x)
    return out

def check_prime(p):
    if p % 24 not in (13, 19):
        return []
    p2 = p * p
    p3 = p2 * p
    failures = []

    # Deterministic unit choices; all are source-independent regression data.
    U = (7 * p + 11) % p
    W = 5 % p2
    if gcd(W, p) != 1:
        W = 7 % p2

    # Force VW = -1-pU^2 mod p^2.
    V = ((-1 - p * U * U) * inv(W, p2)) % p2

    ea = (3 * p + 2) % p
    eb = (5 * p + 4) % p
    A = (inv(W, p2) * (1 + p * ea)) % p2
    B = (inv(V, p2) * (1 + p * eb)) % p2

    if (V * W + 1 + p * U * U) % p2:
        failures.append("determinant")
    if (W * A - 1) % p:
        failures.append("a_first_comparison")
    if (V * B - 1) % p:
        failures.append("b_first_comparison")

    raw_product = (p * A * B) % p3
    predicted = (-p + p2 * ((U * U - ea - eb) % p)) % p3
    if raw_product != predicted:
        failures.append("FROB2")

    # Gauge: A -> A + p W^{-1} t, hence a_{p-1}=pA changes by p^2 W^{-1}t.
    t = 9 % p
    A2 = (A + p * inv(W, p2) * t) % p2
    raw_product2 = (p * A2 * B) % p3
    predicted2 = (-p + p2 * ((U * U - ea - t - eb) % p)) % p3
    if raw_product2 != predicted2:
        failures.append("gauge_product")
    if (W * A2 - 1) % p:
        failures.append("gauge_first_comparison")

    # Every possible occurrence of delta c(p-1)=p^2*s in ASD is invisible:
    # first slot r=1 -> modulus p;
    # third slot r=2,n=p -> b2*delta has valuation >=3, modulo p^2;
    # third slot r=3,n=1 -> same, modulo p^3;
    # middle slot is killed by b1=0.
    s = (inv(W, p) * t) % p
    delta = p2 * s
    if delta % p:
        failures.append("ASD_first_slot")
    b2 = p
    if (b2 * delta) % p2:
        failures.append("ASD_third_r2")
    if (b2 * delta) % p3:
        failures.append("ASD_third_r3")

    expected_shift = (-t) % p
    observed_shift = ((raw_product2 - raw_product) // p2) % p
    if observed_shift != expected_shift:
        failures.append("gauge_shift")

    return failures

def main():
    tested = 0
    failures = []
    for p in primes(5000):
        if p % 24 not in (13, 19):
            continue
        tested += 1
        bad = check_prime(p)
        if bad:
            failures.append((p, bad))
    print({"target_primes_checked": tested, "failures": failures})
    if failures:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
