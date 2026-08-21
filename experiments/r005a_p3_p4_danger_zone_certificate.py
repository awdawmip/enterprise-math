#!/usr/bin/env python3
"""R005-A p=3/p=4 danger-zone certificate.

This is an exact/explicit certificate for the basin divisor-witness language

    k^p < n < (k+1)^p

with candidate prime witnesses q <= F, where

    A = k^p
    U = (k+1)^p - 1
    F = floor(sqrt(U))
    D = floor(sqrt(U/2)).

The mathematical reduction used by this script is:

(1) If a composite survives every forced witness, then its candidate-prime
    support contains at least two distinct non-forced primes.

(2) Every non-forced witness satisfies q <= sqrt(A), because q^2 itself is an
    exclusive collision whenever A < q^2 <= U.

(3) Hence a residual composite n would contain two distinct non-forced
    witnesses q1,q2 with q1*q2 <= U/2. Therefore min(q1,q2) <= sqrt(U/2).

Consequently, if every prime witness q <= D is forced, the basin has a least
safe witness basis (the forced core).

The certificate forces all q <= D by a chain:
- finite exact prime table for the low-x tail;
- Dusart 2010 short interval theorem;
- Trudgian short interval theorem;
- Axler 2022 Theorem 1.2, n=3.

No probabilistic primality test is used in the finite table.
"""

from __future__ import annotations

from bisect import bisect_left, bisect_right
from decimal import Decimal, getcontext
from math import isqrt
import json

getcontext().prec = 70

DUSART_X = Decimal(396_738)
DUSART_COEFF = Decimal(1) / Decimal(25)
TRUDGIAN_X = Decimal(2_898_239)
TRUDGIAN_COEFF = Decimal(1) / Decimal(111)
AXLER_X = Decimal(17_051_708)
AXLER_N3_COEFF = Decimal("0.0486680000822")

EXPECTED = {
    3: {
        "small_bruteforce": (2, 8),
        "finite_plus_dusart": (9, 4286),
        "dusart_uniform": (4287, 16727),
        "trudgian_uniform": (16136, 104035),
        "axler_n3_uniform": (52583, 494034),
        "certified_total": (2, 494034),
    },
    4: {
        "small_bruteforce": (2, 10),
        "finite_plus_dusart": (11, 530),
        "dusart_uniform": (531, 47977),
        "trudgian_uniform": (1433, 288522),
        "axler_n3_uniform": (3474, 2102191),
        "certified_total": (2, 2102191),
    },
}


def sieve(limit: int) -> list[int]:
    if limit < 2:
        return []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for q in range(2, isqrt(limit) + 1):
        if flags[q]:
            start = q * q
            flags[start : limit + 1 : q] = b"\x00" * (
                (limit - start) // q + 1
            )
    return [n for n in range(2, limit + 1) if flags[n]]


def next_prime_in_closed_interval(lo: int, hi: int, primes: list[int]) -> int | None:
    i = bisect_left(primes, lo)
    if i < len(primes) and primes[i] <= hi:
        return primes[i]
    return None


def basin(p: int, k: int) -> tuple[int, int, int, int]:
    A = k**p
    U = (k + 1) ** p - 1
    F = isqrt(U)
    D = isqrt(U // 2)
    return A, U, F, D


def exact_factorization(n: int, primes: list[int]) -> tuple[tuple[int, int], ...]:
    out: list[tuple[int, int]] = []
    x = n
    for q in primes:
        if q * q > x:
            break
        if x % q == 0:
            e = 0
            while x % q == 0:
                x //= q
                e += 1
            out.append((q, e))
        if x == 1:
            break
    if x > 1:
        out.append((x, 1))
    return tuple(out)


def brute_forced_danger_small(p: int, k: int, primes: list[int]) -> tuple[int, ...]:
    A, U, F, D = basin(p, k)
    candidates = [q for q in primes if q <= F]
    danger = [q for q in candidates if q <= D]
    forced: set[int] = set()
    for n in range(A + 1, U + 1):
        fac = exact_factorization(n, primes)
        if len(fac) == 1 and fac[0] == (n, 1):
            continue
        edge = {q for q, _ in fac if q <= F}
        if len(edge) == 1:
            forced.update(edge)
    missing = tuple(q for q in danger if q not in forced)
    if missing:
        raise AssertionError(("small danger witness not forced", p, k, missing))
    return tuple(danger)


def decimal_L(p: int, k: int) -> Decimal:
    K = Decimal(k)
    A = K**p
    U = (K + 1) ** p - 1
    return Decimal(2).sqrt() * A / U.sqrt()


def decimal_u(p: int, k: int) -> Decimal:
    K = Decimal(k)
    if p == 3:
        return Decimal(3) / K + Decimal(3) / (K * K)
    if p == 4:
        return Decimal(4) / K + Decimal(6) / (K * K) + Decimal(4) / (K * K * K)
    A = K**p
    U = (K + 1) ** p - 1
    return U / A - 1


def H(p: int, k: int, log_power: int) -> Decimal:
    L = decimal_L(p, k)
    return decimal_u(p, k) * (L.ln() ** log_power)


def theorem_endpoint_record(
    p: int,
    start: int,
    end: int,
    x0: Decimal,
    coeff: Decimal,
    log_power: int,
    strict_threshold: bool,
) -> dict:
    L_prev = decimal_L(p, start - 1)
    L_start = decimal_L(p, start)
    H_end = H(p, end, log_power)
    H_next = H(p, end + 1, log_power)
    if strict_threshold:
        assert L_start > x0
        assert L_prev <= x0
    else:
        assert L_start >= x0
        assert L_prev < x0
    assert L_start.ln() > Decimal(log_power * p)
    assert H_end >= coeff
    assert H_next < coeff
    return {
        "start": start,
        "end": end,
        "threshold": str(x0),
        "coefficient": str(coeff),
        "log_power": log_power,
        "L_start_minus_threshold": str(L_start - x0),
        "threshold_minus_L_previous": str(x0 - L_prev),
        "H_end_minus_coefficient": str(H_end - coeff),
        "coefficient_minus_H_next": str(coeff - H_next),
        "monotonicity_guard_logL_start_minus_mp": str(
            L_start.ln() - Decimal(log_power * p)
        ),
    }


def finite_prefix_certificate(
    p: int,
    k_start: int,
    k_end: int,
    danger_primes: list[int],
    exact_primes: list[int],
) -> dict:
    threshold_factor = DUSART_COEFF / (DUSART_X.ln() ** 2)
    end_margin = decimal_u(p, k_end) - threshold_factor
    assert end_margin > 0
    exact_checks = 0
    dusart_checks = 0
    max_exact_hi = 0
    max_exact_x_floor = 0
    witness_checks = 0
    for k in range(k_start, k_end + 1):
        A, U, F, D = basin(p, k)
        assert A // D + 1 > F
        last = bisect_right(danger_primes, D)
        for q in danger_primes[:last]:
            witness_checks += 1
            if A > 396_738 * q:
                dusart_checks += 1
                continue
            lo = A // q + 1
            hi = U // q
            max_exact_hi = max(max_exact_hi, hi)
            max_exact_x_floor = max(max_exact_x_floor, A // q)
            r = next_prime_in_closed_interval(lo, hi, exact_primes)
            if r is None:
                raise AssertionError(("danger witness lacks finite cofactor certificate", p, k, q, lo, hi))
            assert r > F
            exact_checks += 1
    return {
        "k_start": k_start,
        "k_end": k_end,
        "danger_witness_checks": witness_checks,
        "dusart_certified_checks": dusart_checks,
        "finite_prime_table_checks": exact_checks,
        "max_exact_floor_A_over_q": max_exact_x_floor,
        "max_exact_hi_floor_U_over_q": max_exact_hi,
        "uniform_dusart_margin_at_prefix_end": str(end_margin),
    }


def main() -> None:
    exact_prime_limit = 450_000
    exact_primes = sieve(exact_prime_limit)
    max_D = max(
        basin(3, EXPECTED[3]["finite_plus_dusart"][1])[3],
        basin(4, EXPECTED[4]["finite_plus_dusart"][1])[3],
    )
    danger_primes = [q for q in exact_primes if q <= max_D]

    small = {}
    for p, (lo, hi) in [(3, EXPECTED[3]["small_bruteforce"]), (4, EXPECTED[4]["small_bruteforce"])]:
        rows = []
        for k in range(lo, hi + 1):
            danger = brute_forced_danger_small(p, k, exact_primes)
            rows.append({"k": k, "danger_witness_count": len(danger)})
        small[str(p)] = rows

    finite = {
        "3": finite_prefix_certificate(3, *EXPECTED[3]["finite_plus_dusart"], danger_primes, exact_primes),
        "4": finite_prefix_certificate(4, *EXPECTED[4]["finite_plus_dusart"], danger_primes, exact_primes),
    }
    assert finite["3"]["max_exact_hi_floor_U_over_q"] <= exact_prime_limit
    assert finite["4"]["max_exact_hi_floor_U_over_q"] <= exact_prime_limit

    analytic = {}
    for p in (3, 4):
        ds = EXPECTED[p]["dusart_uniform"]
        tr = EXPECTED[p]["trudgian_uniform"]
        ax = EXPECTED[p]["axler_n3_uniform"]
        analytic[str(p)] = {
            "dusart": theorem_endpoint_record(p, ds[0], ds[1], DUSART_X, DUSART_COEFF, 2, True),
            "trudgian": theorem_endpoint_record(p, tr[0], tr[1], TRUDGIAN_X, TRUDGIAN_COEFF, 2, False),
            "axler_n3": theorem_endpoint_record(p, ax[0], ax[1], AXLER_X, AXLER_N3_COEFF, 3, False),
        }
        assert EXPECTED[p]["finite_plus_dusart"][1] + 1 == ds[0]
        assert tr[0] <= ds[1] + 1
        assert ax[0] <= tr[1] + 1

    result = {
        "status": "R005-A DANGER-ZONE CERTIFICATE / EXACT FINITE PREFIX + EXPLICIT PRIME-INTERVAL THEOREMS / NOT CANONICAL",
        "theorem_reduction": {
            "danger_radius": "D=floor(sqrt(U/2))",
            "criterion": "if every prime witness q<=D is forced, the forced core covers every composite and is the unique least safe witness basis",
            "residual_edge_min_size": 2,
            "nonforced_witness_upper_bound": "q<=sqrt(A)",
        },
        "small_bruteforce": small,
        "finite_prefix": finite,
        "analytic_intervals": analytic,
        "certified_ranges": {
            "p3": {"k_min": 2, "k_max": 494034},
            "p4": {"k_min": 2, "k_max": 2102191},
        },
        "boundary_note": "The next k only fails the current Axler-derived uniform sufficient inequality; it is not a counterexample.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
