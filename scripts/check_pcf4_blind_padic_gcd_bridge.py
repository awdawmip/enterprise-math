#!/usr/bin/env python3
"""Direct exact-integer checker for PCF4.

Candidate-side functions accept only N and public seed/schedule data.  The
semiprime factors appear only in the external regression verifier.
"""

from __future__ import annotations

from math import comb, gcd, isqrt


def kernel_direct(seed: int) -> int:
    """Return A_s = C(2s,s)^2 C(3s,s) by direct exact binomials."""
    if seed < 0:
        raise ValueError("seed must be nonnegative")
    return comb(2 * seed, seed) ** 2 * comb(3 * seed, seed)


def candidate_gcd(N: int, seed: int) -> int:
    """Candidate-side observable: gcd(A_seed, N)."""
    if N <= 1:
        raise ValueError("N must exceed 1")
    return gcd(kernel_direct(seed), N)


def extract_factor(N: int) -> tuple[int | None, list[tuple[str, int, int]]]:
    """Factor-blind deterministic PCF4 seed policy.

    Returns (proper_factor_or_None, trace).  On the theorem domain of distinct
    odd semiprimes this always returns a proper factor.
    """
    if N <= 1:
        raise ValueError("N must exceed 1")

    trace: list[tuple[str, int, int]] = []
    small = gcd(N, 6)
    if 1 < small < N:
        trace.append(("small-prime-precheck", 0, small))
        return small, trace

    # Public stopping cap.  For N=pq with p<q, p<sqrt(N), so the first dyadic
    # seed with 3s>p occurs well before this bit-length-only cap.
    max_j = (N.bit_length() + 1) // 2 + 1
    for j in range(max_j + 1):
        seed = 1 << j
        g = candidate_gcd(N, seed)
        trace.append(("dyadic", seed, g))
        if 1 < g < N:
            return g, trace
        if g == N:
            # Exact synchronization fallback.  floor(sqrt(N)/3) is computed
            # without floating point; factors are not used.
            t = isqrt(N) // 3
            for seed2 in (t, t + 1):
                if seed2 <= 0:
                    continue
                g2 = candidate_gcd(N, seed2)
                trace.append(("sqrt-third-fallback", seed2, g2))
                if 1 < g2 < N:
                    return g2, trace
            return None, trace

    return None, trace


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def external_verify(bound: int = 300) -> dict[str, int]:
    """External verifier; p,q are used only after candidate extraction."""
    primes = [p for p in range(3, bound) if _is_prime(p) and p % 2]
    cases = 0
    fallback_cases = 0
    max_trace = 0
    for i, p in enumerate(primes):
        for q in primes[i + 1 :]:
            N = p * q
            factor, trace = extract_factor(N)
            assert factor in (p, q), (p, q, factor, trace)
            cases += 1
            max_trace = max(max_trace, len(trace))
            if any(stage == "sqrt-third-fallback" for stage, _, _ in trace):
                fallback_cases += 1
    return {
        "cases": cases,
        "fallback_cases": fallback_cases,
        "max_trace_entries": max_trace,
    }


def main() -> None:
    stats = external_verify()
    print(
        "PCF4_DIRECT_CHECK_PASS "
        f"cases={stats['cases']} "
        f"fallback={stats['fallback_cases']} "
        f"max_trace={stats['max_trace_entries']}"
    )


if __name__ == "__main__":
    main()
