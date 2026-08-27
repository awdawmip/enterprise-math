#!/usr/bin/env python3
"""Independent exact checker for PCF4R N-only valuation-wall replay.

Blind-forward Phase A checker. Constructor-side factor_nonly receives only N.
Hidden p,q are used only by regression oracles.
"""

from math import comb, gcd, isqrt
import bisect
import random


def sieve_primes(limit: int) -> list[int]:
    is_p = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        is_p[0] = 0
    if limit >= 1:
        is_p[1] = 0
    for x in range(2, isqrt(limit) + 1):
        if is_p[x]:
            start = x * x
            is_p[start : limit + 1 : x] = b"\x00" * (((limit - start) // x) + 1)
    return [i for i in range(2, limit + 1) if is_p[i]]


def vp_fact(n: int, p: int) -> int:
    out = 0
    while n:
        n //= p
        out += n
    return out


def vp_A(s: int, p: int) -> int:
    return vp_fact(2 * s, p) + vp_fact(3 * s, p) - 5 * vp_fact(s, p)


def A_direct(s: int) -> int:
    # (2s)!(3s)!/(s!)^5 = C(2s,s)^2 C(3s,s)
    return comb(2 * s, s) ** 2 * comb(3 * s, s)


def update_A_mod(a_prev: int, s: int, N: int) -> tuple[int | None, int]:
    """Return A_s mod N from A_{s-1} mod N when s is a unit mod N.

    A_s/A_{s-1} = 6(2s-1)(3s-2)(3s-1)/s^3.
    If s is a nonunit, return its gcd with N instead of inverting.
    """
    g = gcd(s, N)
    if g != 1:
        return None, g
    num = (6 * (2 * s - 1) * (3 * s - 2) * (3 * s - 1)) % N
    den = pow(s, 3, N)
    return (a_prev * num * pow(den, -1, N)) % N, 1


def factor_nonly(N: int, return_trace: bool = False):
    """Factor a promised distinct odd semiprime N=pq with 3<p<q.

    Constructor inputs are N and public integer constants only.
    """
    R = isqrt(N)
    t = R // 3  # floor(sqrt(N)/3), since N is nonsquare
    a = 1
    saved: dict[int, int] = {}
    trace: list[tuple[int, int]] = []

    for s in range(1, R + 1):
        a_next, den_gcd = update_A_mod(a, s, N)
        if den_gcd != 1:
            if 1 < den_gcd < N:
                result = (den_gcd, ("DENOMINATOR", s), trace)
                return result if return_trace else den_gcd
            raise AssertionError(("unexpected denominator gcd", N, s, den_gcd))
        assert a_next is not None
        a = a_next

        if s == t or s == t + 1:
            saved[s] = a

        if s & (s - 1) == 0:
            g = gcd(a, N)
            trace.append((s, g))
            if 1 < g < N:
                result = (g, ("DYADIC", s), trace)
                return result if return_trace else g

            if g == N:
                # In the synchronized branch, t,t+1 are both <= s.
                assert t in saved and t + 1 in saved, (N, s, t, sorted(saved))
                gt = gcd(saved[t], N)
                if 1 < gt < N:
                    result = (gt, ("FALLBACK_T", s, t), trace)
                    return result if return_trace else gt
                gt1 = gcd(saved[t + 1], N)
                if 1 < gt1 < N:
                    result = (gt1, ("FALLBACK_T1", s, t + 1), trace)
                    return result if return_trace else gt1
                result = (None, ("FALLBACK_FAIL", s, t, gt, gt1), trace)
                return result if return_trace else None

    result = (None, ("NO_STOP", R), trace)
    return result if return_trace else None


def main() -> None:
    primes = [p for p in sieve_primes(5000) if p > 3]

    valuation_checks = 0
    for r in [p for p in primes if p <= 1000]:
        for s in range(r):
            lhs = vp_A(s, r)
            rhs = (2 * s) // r + (3 * s) // r
            assert lhs == rhs, (r, s, lhs, rhs)
            assert (lhs > 0) == (3 * s >= r), (r, s, lhs)
            valuation_checks += 1

    recurrence_checks = 0
    for N in (1009 * 1013, 1019 * 1021, 1031 * 1033):
        a = 1
        for s in range(1, 120):
            a_next, den_gcd = update_A_mod(a, s, N)
            assert den_gcd == 1 and a_next is not None
            a = a_next
            assert a == A_direct(s) % N, (N, s, a, A_direct(s) % N)
            recurrence_checks += 1

    small = [p for p in primes if p <= 500]
    semiprime_checks = 0
    synchronized_checks = 0
    mode_counts: dict[str, int] = {}

    for i, p in enumerate(small):
        for q in small[i + 1 :]:
            N = p * q
            factor, meta, trace = factor_nonly(N, True)
            assert factor in (p, q), (p, q, meta, trace)

            mode_counts[meta[0]] = mode_counts.get(meta[0], 0) + 1
            s, g = trace[-1]
            assert s < p, (p, q, s, g)
            assert g in (p, N), (p, q, s, g)

            if g == N:
                synchronized_checks += 1
                assert q < 2 * p, (p, q, s)
                t = isqrt(N) // 3
                assert t + 1 < p, (p, q, t)
                gt = gcd(A_direct(t), N)
                gt1 = gcd(A_direct(t + 1), N)
                assert gt == p or (gt == 1 and gt1 == p), (p, q, t, gt, gt1)

            semiprime_checks += 1

    rng = random.Random(0x50434634)
    samples: set[tuple[int, int]] = set()
    for idx, p in enumerate(primes):
        if idx + 1 < len(primes):
            samples.add((p, primes[idx + 1]))

        j = bisect.bisect_left(primes, 2 * p) - 1
        if j > idx:
            samples.add((p, primes[j]))

        j = bisect.bisect_right(primes, 5 * p)
        if j < len(primes):
            samples.add((p, primes[min(j + 2, len(primes) - 1)]))

        if len(samples) > 1200:
            break

    while len(samples) < 2000:
        i = rng.randrange(len(primes) - 1)
        j = rng.randrange(i + 1, len(primes))
        samples.add((primes[i], primes[j]))

    for p, q in samples:
        factor, meta, _trace = factor_nonly(p * q, True)
        assert factor in (p, q), (p, q, meta)

    print(
        "PASS",
        f"valuation_checks={valuation_checks}",
        f"recurrence_checks={recurrence_checks}",
        f"exhaustive_semiprimes={semiprime_checks}",
        f"synchronized_cases={synchronized_checks}",
        f"adversarial_semiprimes={len(samples)}",
        "modes=" + ",".join(f"{k}:{mode_counts[k]}" for k in sorted(mode_counts)),
    )


if __name__ == "__main__":
    main()
