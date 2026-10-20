"""Deterministic local cursor certificates just beyond the cubic gap database.

Primality is certified by strong Miller--Rabin to the first twelve prime bases
only below the published Sorenson--Webster threshold psi_12.  The module raises
outside that deterministic range; it does not fall back to a probabilistic
oracle.
"""

from bisect import bisect_left, bisect_right

from .prime_collapse_field import factor_horizon
from .prime_cubic_horizontal_placement import unresolved_lower_q_interval


MR12_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
PSI12 = 318_665_857_834_031_151_167_461


def is_prime_mr12(n: int) -> bool:
    """Deterministic primality test for n<psi_12.

    Sorenson--Webster determined psi_12, the least composite strong
    pseudoprime to the first twelve prime bases.  Therefore an integer below
    psi_12 passing all twelve strong tests is prime.
    """
    if n < 2:
        return False
    for p in MR12_BASES:
        if n == p:
            return True
        if n % p == 0:
            return False
    if n >= PSI12:
        raise ValueError("n is outside the proven MR12 deterministic range")

    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    for base in MR12_BASES:
        x = pow(base, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def first_mr12_prime_after(n: int, limit: int) -> int | None:
    """Return the first deterministically certified prime in (n,limit]."""
    if limit <= n:
        return None
    candidate = n + 1
    if candidate <= 2 <= limit:
        return 2
    if candidate % 2 == 0:
        candidate += 1
    while candidate <= limit:
        if is_prime_mr12(candidate):
            return candidate
        candidate += 2
    return None


def primes_mr12_in_interval(lower: int, upper: int) -> tuple[int, ...]:
    """Return every deterministically certified prime in [lower,upper]."""
    if upper < lower:
        return ()
    return tuple(n for n in range(max(2, lower), upper + 1) if is_prime_mr12(n))


def lower_cursor_prime_qs(k: int, coverage_limit: int) -> tuple[int, ...]:
    """Return the actual prime q coordinates in the database-overflow cursor."""
    lo, hi = unresolved_lower_q_interval(k, coverage_limit)
    return primes_mr12_in_interval(lo, hi)


def cursor_state_cofactor_certificate(
    k: int,
    q: int,
    *,
    coverage_limit: int,
) -> int | None:
    """Return one deterministic e=1 cofactor witness for a cursor prime q.

    The routine requires q to lie in the unresolved lower-band cursor and to be
    prime by the MR12 theorem.  It then searches the exact cofactor interval

        floor(k^3/q) < r <= floor(((k+1)^3-1)/q)

    for one MR12-certified prime r.  Since q is in the lower band, every such r
    lies beyond the factor horizon and qr is an exclusive collision.
    """
    lo, hi = unresolved_lower_q_interval(k, coverage_limit)
    if not (lo <= q <= hi):
        raise ValueError("q is outside the unresolved lower-band cursor")
    if not is_prime_mr12(q):
        raise ValueError("q is not prime")

    a = k**3
    u = (k + 1) ** 3 - 1
    f = factor_horizon(k, 3)
    if q * f > a:
        raise ValueError("q is not in the lower cofactor band")

    lower = a // q
    upper = u // q
    r = first_mr12_prime_after(lower, upper)
    if r is None:
        return None
    if r <= f:
        raise AssertionError("certified cofactor did not clear factor horizon")
    return r


def verify_cursor_block(
    first_k: int,
    last_k: int,
    *,
    coverage_limit: int,
) -> dict[str, int]:
    """Verify every prime-q cursor state on an inclusive cubic k block.

    Prime q coordinates are precompiled once on the union of all integer
    cursors, then sliced by binary search for each k.  Every returned cofactor r
    is independently certified by MR12.  Raises on the first uncovered state.
    """
    if first_k < 1 or last_k < first_k:
        raise ValueError("invalid k block")

    intervals: list[tuple[int, int]] = []
    global_lo: int | None = None
    global_hi: int | None = None
    for k in range(first_k, last_k + 1):
        lo, hi = unresolved_lower_q_interval(k, coverage_limit)
        intervals.append((lo, hi))
        if lo <= hi:
            global_lo = lo if global_lo is None else min(global_lo, lo)
            global_hi = hi if global_hi is None else max(global_hi, hi)

    if global_lo is None or global_hi is None:
        return {
            "states": 0,
            "distinct_q_primes": 0,
            "max_search_offset": 0,
            "min_slack": 0,
            "max_cofactor_prime": 0,
        }

    q_primes = primes_mr12_in_interval(global_lo, global_hi)
    states = 0
    max_offset = 0
    min_slack: int | None = None
    max_r = 0

    for k, (lo, hi) in zip(range(first_k, last_k + 1), intervals):
        if lo > hi:
            continue
        i0 = bisect_left(q_primes, lo)
        i1 = bisect_right(q_primes, hi)
        a = k**3
        u = (k + 1) ** 3 - 1
        for q in q_primes[i0:i1]:
            states += 1
            lower = a // q
            upper = u // q
            r = cursor_state_cofactor_certificate(k, q, coverage_limit=coverage_limit)
            if r is None:
                raise AssertionError((k, q, lower, upper))
            offset = r - lower
            slack = upper - r
            max_offset = max(max_offset, offset)
            max_r = max(max_r, r)
            min_slack = slack if min_slack is None else min(min_slack, slack)

    return {
        "states": states,
        "distinct_q_primes": len(q_primes),
        "max_search_offset": max_offset,
        "min_slack": 0 if min_slack is None else min_slack,
        "max_cofactor_prime": max_r,
    }
