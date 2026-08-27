#!/usr/bin/env python3
"""Independent recurrence checker for the PCF4 factor-blind kernel splitter.

This implementation does not import or reuse the direct-binomial checker.  Its
candidate path accepts only N and public seed/schedule data.  Factors are used
only by the external test oracle.
"""

from __future__ import annotations

from math import gcd, isqrt


def kernel_recurrence(seed: int) -> int:
    """Build A_seed from the exact integer recurrence, with no modular divide."""
    if seed < 0:
        raise ValueError("seed must be nonnegative")
    a = 1
    for k in range(seed):
        numerator = a * 6 * (2 * k + 1) * (3 * k + 1) * (3 * k + 2)
        denominator = (k + 1) ** 3
        if numerator % denominator:
            raise AssertionError((k, numerator, denominator))
        a = numerator // denominator
    return a


def probe(N: int, seed: int) -> int:
    return gcd(kernel_recurrence(seed), N)


def run_candidate(N: int) -> tuple[int | None, tuple[tuple[str, int, int], ...]]:
    if N <= 1:
        raise ValueError("N must exceed 1")

    events: list[tuple[str, int, int]] = []
    d = gcd(N, 6)
    if 1 < d < N:
        events.append(("precheck", 0, d))
        return d, tuple(events)

    cap = (N.bit_length() + 1) // 2 + 2
    seed = 1
    for _ in range(cap + 1):
        d = probe(N, seed)
        events.append(("power-two", seed, d))
        if 1 < d < N:
            return d, tuple(events)
        if d == N:
            base = isqrt(N) // 3
            d0 = probe(N, base) if base > 0 else 1
            if base > 0:
                events.append(("lower-neighbour", base, d0))
                if 1 < d0 < N:
                    return d0, tuple(events)
            d1 = probe(N, base + 1)
            events.append(("upper-neighbour", base + 1, d1))
            if 1 < d1 < N:
                return d1, tuple(events)
            return None, tuple(events)
        seed *= 2

    return None, tuple(events)


def _primes_below(limit: int) -> list[int]:
    out: list[int] = []
    for n in range(3, limit, 2):
        prime = True
        d = 3
        if n > 3:
            while d * d <= n:
                if n % d == 0:
                    prime = False
                    break
                d += 2
        if prime:
            out.append(n)
    return out


def oracle_replay(limit: int = 300) -> dict[str, int]:
    primes = _primes_below(limit)
    total = 0
    synchronized = 0
    longest = 0
    for a, p in enumerate(primes):
        for q in primes[a + 1 :]:
            N = p * q
            factor, events = run_candidate(N)
            assert factor in (p, q), (p, q, factor, events)
            total += 1
            longest = max(longest, len(events))
            if any(g == N and kind == "power-two" for kind, _, g in events):
                synchronized += 1
    return {"cases": total, "synchronized": synchronized, "max_events": longest}


def main() -> None:
    stats = oracle_replay()
    print(
        "PCF4_RECURRENCE_CHECK_PASS "
        f"cases={stats['cases']} "
        f"synchronized={stats['synchronized']} "
        f"max_events={stats['max_events']}"
    )


if __name__ == "__main__":
    main()
