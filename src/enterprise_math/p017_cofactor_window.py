"""Exact cofactor-window reductions for the P017 consecutive-square pressure test.

This module keeps the useful arithmetic consequences of the recent P018/P017
experiments while avoiding special-case vocabulary as the primary object.
For a first-factor shell L_p(k), every state n=p*q is reconstructed from a
finite exact interval of possible cofactors q together with the single condition
that q is p-rough.  Near the diagonal this window degenerates to the symmetric
prime-pair formula studied previously.

All arithmetic is integer-only.  Prime sieving, rough numbers, least prime
factors, and smooth parts are classical number theory; the project-specific
question is whether these exact finite windows create useful proof leverage for
P017.
"""

from __future__ import annotations

from .factor_precision import first_factor_shell, square_basin
from .legendre import is_prime, primes_up_to


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_shell_prime(k: int, prime: int) -> None:
    _require_positive("k", k)
    _require_positive("prime", prime)
    if prime not in primes_up_to(k):
        raise ValueError("prime must be a prime <= k")


def is_p_rough(value: int, prime: int) -> bool:
    """Return whether value has no prime divisor strictly below ``prime``."""
    _require_positive("value", value)
    _require_positive("prime", prime)
    return all(value % q != 0 for q in primes_up_to(prime - 1))


def centered_cofactor_window(k: int, prime: int) -> dict[str, int]:
    """Return the exact cofactor window for the first-factor shell L_p(k).

    Put c=k+1 and r=c-p.  For a shell state n=p*q, the consecutive-square
    inequalities are equivalent to q_min <= q <= q_max with the formulas below.
    ``j`` is the centered correction in q=c+r+j.
    """
    _require_shell_prime(k, prime)
    center = k + 1
    radius = center - prime
    if radius <= 0:
        raise AssertionError("a shell prime <=k must have positive centered radius")

    lower_floor = ((radius - 1) * (radius - 1)) // prime
    upper_floor = (radius * radius - 1) // prime
    q_min = center + radius - 1 + lower_floor
    q_max = center + radius + upper_floor
    j_min = -1 + lower_floor
    j_max = upper_floor
    raw_count = q_max - q_min + 1

    # The width correction is exactly one quotient-transport increment:
    # Q_p(a+h)-Q_p(a) with a=(r-1)^2 and h=2r-2.
    base = (radius - 1) * (radius - 1)
    increment = 2 * radius - 2
    transport = (base + increment) // prime - base // prime
    bulk = increment // prime
    carry = ((base % prime) + (increment % prime)) // prime

    if transport != bulk + carry:
        raise AssertionError("quotient-transport bulk/carry decomposition failed")
    if raw_count != 2 + transport:
        raise AssertionError("cofactor-window width transport identity failed")
    if carry not in (0, 1):
        raise AssertionError("residual boundary carry must be binary")

    return {
        "k": k,
        "prime": prime,
        "center": center,
        "radius": radius,
        "q_min": q_min,
        "q_max": q_max,
        "j_min": j_min,
        "j_max": j_max,
        "raw_count": raw_count,
        "transport": transport,
        "transport_bulk": bulk,
        "transport_carry": carry,
    }


def cofactor_square_offsets(k: int, prime: int, q: int) -> dict[str, int]:
    """Return exact square-boundary offsets for q=c+r+j."""
    _require_shell_prime(k, prime)
    _require_positive("q", q)
    data = centered_cofactor_window(k, prime)
    center = data["center"]
    radius = data["radius"]
    j = q - center - radius
    n = prime * q
    upper_offset = center * center - n
    lower_offset = n - (center - 1) * (center - 1)

    if upper_offset != radius * radius - j * prime:
        raise AssertionError("upper square-offset identity failed")
    if lower_offset != prime * (j + 2) - (radius - 1) * (radius - 1):
        raise AssertionError("lower square-offset identity failed")

    return {
        "n": n,
        "j": j,
        "lower_offset": lower_offset,
        "upper_offset": upper_offset,
    }


def cofactor_window_shell(k: int, prime: int) -> list[int]:
    """Reconstruct L_p(k) from its exact cofactor window and p-roughness."""
    data = centered_cofactor_window(k, prime)
    candidates = [
        prime * q
        for q in range(data["q_min"], data["q_max"] + 1)
        if is_p_rough(q, prime)
    ]
    canonical = first_factor_shell(k, prime)
    if candidates != canonical:
        raise AssertionError("p-rough cofactor window failed to reconstruct first-factor shell")
    return candidates


def cofactor_window_survivors(k: int, prime: int) -> list[int]:
    """Return the surviving p-rough cofactor values rather than the states p*q."""
    return [n // prime for n in cofactor_window_shell(k, prime)]


def near_diagonal_prime_degeneracy(k: int, prime: int) -> dict[str, object]:
    """Recover the symmetric-prime special case when p>r^2.

    In this regime the raw cofactor window is exactly {c+r-1,c+r}.  For odd
    p>=3, the first value is even and cannot be p-rough; the second value is
    below p^2, so p-roughness is equivalent to primality.
    """
    data = centered_cofactor_window(k, prime)
    radius = data["radius"]
    if prime < 3 or prime <= radius * radius:
        raise ValueError("near-diagonal degeneration requires odd p>=3 with p>r^2")
    center = data["center"]
    expected_q = center + radius
    if data["q_min"] != expected_q - 1 or data["q_max"] != expected_q:
        raise AssertionError("near-diagonal cofactor window did not collapse to two candidates")
    shell = cofactor_window_shell(k, prime)
    expected_shell = [prime * expected_q] if is_prime(expected_q) else []
    if shell != expected_shell:
        raise AssertionError("near-diagonal shell did not reduce to symmetric prime condition")
    return {
        **data,
        "symmetric_q": expected_q,
        "symmetric_q_is_prime": is_prime(expected_q),
        "shell": shell,
    }


def omega_with_multiplicity(value: int) -> int:
    """Return the total number of prime factors counted with multiplicity."""
    _require_positive("value", value)
    remaining = value
    count = 0
    for p in primes_up_to(value):
        while remaining % p == 0:
            remaining //= p
            count += 1
        if remaining == 1:
            break
        if p * p > remaining:
            count += 1
            remaining = 1
            break
    if remaining != 1:
        count += 1
    return count


def root_depth_shell_bound(k: int, prime: int, max_omega: int) -> dict[str, object]:
    """Verify the root-depth implication p^(m+1)>U => Omega(n)<=m on L_p(k)."""
    _require_shell_prime(k, prime)
    _require_natural("max_omega", max_omega)
    upper = (k + 1) * (k + 1) - 1
    condition = prime ** (max_omega + 1) > upper
    shell = cofactor_window_shell(k, prime)
    observed = max((omega_with_multiplicity(n) for n in shell), default=0)
    if condition and observed > max_omega:
        raise AssertionError("integer-root depth bound on shell Omega failed")
    return {
        "upper": upper,
        "condition": condition,
        "max_omega": max_omega,
        "observed_max_omega": observed,
    }


def square_basin_smooth_tail(k: int, n: int) -> dict[str, int | bool]:
    """Split n into its full k-smooth core and its residual tail.

    For a square-basin state the residual tail is exactly 1 or one prime > k.
    """
    _require_positive("k", k)
    _require_positive("n", n)
    if n not in square_basin(k):
        raise ValueError("n must lie strictly between k^2 and (k+1)^2")

    remaining = n
    smooth_core = 1
    for p in primes_up_to(k):
        while remaining % p == 0:
            smooth_core *= p
            remaining //= p

    tail = remaining
    tail_ok = tail == 1 or (tail > k and is_prime(tail))
    if not tail_ok:
        raise AssertionError("square-basin k-smooth residual is neither 1 nor a single prime >k")
    if smooth_core * tail != n:
        raise AssertionError("smooth-core decomposition failed")

    prime_state = is_prime(n)
    if (smooth_core == 1) != prime_state:
        raise AssertionError("square-basin primality did not match trivial k-smooth core")

    return {
        "smooth_core": smooth_core,
        "tail": tail,
        "tail_is_large_prime": tail != 1,
        "is_prime": prime_state,
    }
