#!/usr/bin/env python3
"""Deterministic regression for the D25 finite discrete adjoint reduction.

This checks only finite exact modular consequences. The all-prime proof is in the
companion note, not in this scan.
"""

def primes_below(n):
    sieve = bytearray(b"\x01") * n
    if n > 0:
        sieve[0] = 0
    if n > 1:
        sieve[1] = 0
    q = 2
    while q * q < n:
        if sieve[q]:
            start = q * q
            sieve[start:n:q] = b"\x00" * (((n - 1 - start) // q) + 1)
        q += 1
    return [i for i in range(2, n) if sieve[i]]

def inv(a, p):
    return pow(a % p, -1, p)

def check_prime(p):
    assert p % 6 == 1
    m = (p - 1) // 6
    N = p - 1
    c = [0] * (N + 1)
    d = [0] * (N + 1)
    e = [0] * (N + 1)
    c[0] = 1
    for k in range(N):
        den = ((k + 1) * (k + 1)) % p
        r0 = ((k - m) * (k - 2 * m)) % p
        r1 = (3 * k - 4 * m) % p
        c[k + 1] = c[k] * r0 * inv(den, p) % p
        d[k + 1] = (d[k] * r0 + c[k] * r1) * inv(den, p) % p
        e[k + 1] = (e[k] * r0 + 2 * d[k] * r1 + 4 * c[k]) * inv(den, p) % p
    f = [0] * (p + 1)
    for k in range(1, N + 1):
        b_prev = ((k - 1 - m) * (k - 1 - 2 * m)) % p
        f[k] = (k * k * e[k] - b_prev * e[k - 1]) % p
        expected = (2 * (3 * (k - 1) - 4 * m) * d[k - 1] + 4 * c[k - 1]) % p
        if f[k] != expected:
            return ("INTERIOR_FORCING", k, f[k], expected)
    b_N = ((N - m) * (N - 2 * m)) % p
    f[p] = (-b_N * e[N]) % p
    half = inv(2, p)
    lam = [0] * (p + 1)
    lam[p] = pow(half, p, p)
    for k in range(N, 0, -1):
        b_k = ((k - m) * (k - 2 * m)) % p
        lam[k] = (pow(half, k, p) + b_k * lam[k + 1]) * inv(k * k, p) % p
    f2_half = sum(e[k] * pow(half, k, p) for k in range(N + 1)) % p
    adjoint_eval = sum(lam[k] * f[k] for k in range(1, p + 1)) % p
    if adjoint_eval != f2_half:
        return ("ADJOINT_EVAL", f2_half, adjoint_eval)
    terminal = lam[p] * f[p] % p
    if terminal != (-2) % p:
        return ("TERMINAL_SOURCE", terminal, (-2) % p)
    if any(c[j] % p for j in range(m + 1, N + 1)):
        return ("C_SUPPORT",)
    if any(d[j] % p for j in range(2 * m + 1, N + 1)):
        return ("D_SUPPORT",)
    S = 0
    for j in range(0, 2 * m + 1):
        src = (2 * (3 * j - 4 * m) * d[j] + 4 * c[j]) % p
        S = (S + lam[j + 1] * src) % p
    if f2_half != (S - 2) % p:
        return ("REDUCED_SECOND_JET", f2_half, (S - 2) % p)
    return None

def main():
    targets = [p for p in primes_below(5000) if p % 24 in (13, 19)]
    failures = []
    by_class = {13: 0, 19: 0}
    for p in targets:
        by_class[p % 24] += 1
        err = check_prime(p)
        if err is not None:
            failures.append((p, err))
    print({"target_primes": len(targets), "by_class": by_class, "failures": failures})
    if failures:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
