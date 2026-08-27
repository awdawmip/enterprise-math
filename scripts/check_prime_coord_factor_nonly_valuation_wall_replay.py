#!/usr/bin/env python3
"""Independent exact-integer checker for the PCF4R N-only valuation-wall replay.

Phase-A source discipline: this script is authored from the published taskbook,
the accepted PCF4 parent boundary, and elementary number theory only.  It does
not use the withheld duplicate execution.
"""

from math import comb, gcd, isqrt


def primes_upto(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            for m in range(p * p, limit + 1, p):
                sieve[m] = False
    return [p for p, ok in enumerate(sieve) if ok]


def vp_factorial(n: int, p: int) -> int:
    out = 0
    while n:
        n //= p
        out += n
    return out


def vp_A(s: int, p: int) -> int:
    return vp_factorial(2 * s, p) + vp_factorial(3 * s, p) - 5 * vp_factorial(s, p)


def A_direct(s: int) -> int:
    # A_s = C(2s,s)^2 C(3s,s), hence A_s is integral.
    return comb(2 * s, s) ** 2 * comb(3 * s, s)


def A_recurrence(s: int) -> int:
    # A_{k+1}/A_k = 6(2k+1)(3k+1)(3k+2)/(k+1)^3.
    a = 1
    for k in range(s):
        num = a * 6 * (2 * k + 1) * (3 * k + 1) * (3 * k + 2)
        den = (k + 1) ** 3
        assert num % den == 0
        a = num // den
    return a


def A_mod_or_factor(s: int, N: int) -> tuple[str, int]:
    """Return ('residue', A_s mod N) or a public denominator gcd factor.

    We use
      C(2s,s) = prod_{j=1}^s(s+j) / s!,
      C(3s,s) = prod_{j=1}^s(2s+j) / s!.
    If s! is a unit modulo N, one modular inverse is justified.  Otherwise the
    gcd with N is itself factor information obtained from public N and s.
    For all theorem-relevant probes in the distinct-semiprime proof, s<p, so
    s! is automatically a unit modulo N=pq.
    """
    den = 1
    num2 = 1
    num3 = 1
    for j in range(1, s + 1):
        den = (den * j) % N
        num2 = (num2 * (s + j)) % N
        num3 = (num3 * (2 * s + j)) % N
    g = gcd(den, N)
    if g != 1:
        return ("factor", g)
    inv = pow(den, -1, N)
    c2 = (num2 * inv) % N
    c3 = (num3 * inv) % N
    return ("residue", (c2 * c2 * c3) % N)


def probe_gcd(s: int, N: int) -> tuple[int, str]:
    kind, value = A_mod_or_factor(s, N)
    if kind == "factor":
        return value, kind
    return gcd(value, N), kind


def extract_distinct_odd_semiprime(N: int) -> tuple[int | None, str, list[tuple[int, int, str]]]:
    """N-only deterministic extractor tested by the Phase-A proof.

    The constructor receives only N and public seed indices.  The proof assumes
    N=pq with 3<p<q distinct primes.  No factor oracle is used by this function.
    """
    root = isqrt(N)
    d = 1
    trace: list[tuple[int, int, str]] = []
    while d <= root:
        g, kind = probe_gcd(d, N)
        trace.append((d, g, kind))
        if 1 < g < N:
            return g, "dyadic", trace
        if g == N:
            t = root // 3  # exactly floor(sqrt(N)/3)
            for s in (t, t + 1):
                g2, kind2 = probe_gcd(s, N)
                trace.append((s, g2, kind2))
                if 1 < g2 < N:
                    return g2, "fallback", trace
            return None, "fallback_fail", trace
        d *= 2
    return None, "no_nonunit", trace


def check_local_valuation_formula(limit: int = 1000) -> int:
    cases = 0
    for r in primes_upto(limit):
        if r <= 3:
            continue
        for s in range(r):
            expected = (2 * s) // r + (3 * s) // r
            assert vp_A(s, r) == expected, (r, s, vp_A(s, r), expected)
            cases += 1
    return cases


def check_constructor_crosschecks() -> tuple[int, int]:
    recurrence_cases = 0
    for s in range(80):
        assert A_recurrence(s) == A_direct(s)
        recurrence_cases += 1

    residue_cases = 0
    for N in range(5, 400):
        for s in range(30):
            kind, value = A_mod_or_factor(s, N)
            if kind == "residue":
                assert value == A_direct(s) % N, (N, s, value, A_direct(s) % N)
                residue_cases += 1
    return recurrence_cases, residue_cases


def check_semiprimes(limit: int = 1000) -> tuple[int, int, int]:
    primes = [p for p in primes_upto(limit) if p > 3]
    total = 0
    dyadic = 0
    fallback = 0
    for i, p in enumerate(primes):
        for q in primes[i + 1 :]:
            N = p * q
            factor, mode, trace = extract_distinct_odd_semiprime(N)
            assert factor in (p, q), (p, q, N, mode, trace)
            total += 1
            if mode == "dyadic":
                dyadic += 1
            elif mode == "fallback":
                fallback += 1
            else:
                raise AssertionError((p, q, N, mode, trace))
    return total, dyadic, fallback


def main() -> None:
    valuation_cases = check_local_valuation_formula()
    recurrence_cases, residue_cases = check_constructor_crosschecks()
    total, dyadic, fallback = check_semiprimes()
    print("PCF4R Phase-A independent checker: PASS")
    print(f"local valuation cases: {valuation_cases}")
    print(f"recurrence/direct cases: {recurrence_cases}")
    print(f"modular/direct residue cases: {residue_cases}")
    print(f"distinct semiprimes p<q<=1000: {total}")
    print(f"dyadic direct splits: {dyadic}")
    print(f"synchronized fallbacks: {fallback}")


if __name__ == "__main__":
    main()
