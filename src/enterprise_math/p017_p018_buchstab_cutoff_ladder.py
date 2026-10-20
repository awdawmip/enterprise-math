"""Exact root-cutoff ladder for almost-prime survivors in a square interval.

Let

    I_k = {k^2+1,...,k^2+2k},
    U_k = k^2+2k = (k+1)^2-1.

After sieving by every prime <=z, a surviving integer has all prime factors
strictly larger than z.  Therefore if

    (z+1)^(m+1) > U_k,

no survivor can have m+1 prime factors counted with multiplicity.  The least
integer cutoff certified by this pure product argument is exactly

    z_m(k) = floor(U_k^(1/(m+1))).

Indeed (z_m+1)^(m+1)>U_k, while z_m^(m+1)<=U_k.

Important special cases are

    m=1: z_1(k)=k,              prime-only/full Legendre cutoff;
    m=2: z_2(k)~k^(2/3),        prime-or-semiprime/P2 cutoff;
    m=3: z_3(k)~k^(1/2),        P3 cutoff.

This gives an exact proof-complexity/root hierarchy.  The half cutoff k/2 used
by the terminal staircase is much deeper than the minimal P2 cutoff; it is a
structural microscope chosen because each high prime then has only one or two
odd cofactor candidates.

At the exact P2 cutoff z=z_2(k), every rough survivor is either prime or a
unique semiprime p*q with

    z<p<=k<q,
    k^2 < p*q <= k^2+2k.

Hence

    prime_gap(k) = R_z(k) - H_z(k),

where

    H_z(k)
      = sum_{z<p<=k, p prime}
          #{q prime : k^2/p < q <= (k^2+2k)/p}.

This is the minimal exact binary/Buchstab interface.  Controlling it requires
prime-prime information across a hyperbolic strip; the constant-degree
reciprocal staircase is the z>k/2 specialization.
"""

from __future__ import annotations

from math import gcd

from .legendre import direct_square_interval_prime_count, is_prime, primes_up_to


def integer_nth_root_floor(n: int, degree: int) -> int:
    """Return floor(n^(1/degree)) using integer arithmetic."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 1:
        raise ValueError("degree must be a positive integer")
    if n < 2 or degree == 1:
        return n
    lo, hi = 0, 1
    while hi**degree <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**degree <= n:
            lo = mid
        else:
            hi = mid
    return lo


def square_interval_upper(k: int) -> int:
    """Return the largest integer strictly below (k+1)^2."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be a positive integer")
    return k * k + 2 * k


def almost_prime_cutoff(k: int, omega_bound: int) -> dict[str, int | bool]:
    """Return the least product-certified cutoff forcing Omega<=omega_bound."""
    if isinstance(omega_bound, bool) or not isinstance(omega_bound, int) or omega_bound < 1:
        raise ValueError("omega_bound must be a positive integer")
    upper = square_interval_upper(k)
    degree = omega_bound + 1
    cutoff = integer_nth_root_floor(upper, degree)
    if not (cutoff**degree <= upper < (cutoff + 1) ** degree):
        raise AssertionError("integer root cutoff failed")
    return {
        "k": k,
        "upper": upper,
        "omega_bound": omega_bound,
        "root_degree": degree,
        "cutoff": cutoff,
        "cutoff_power_not_above_upper": True,
        "next_cutoff_power_above_upper": True,
    }


def rough_survivor_offsets(k: int, cutoff: int) -> tuple[int, ...]:
    """Return interval offsets surviving every prime <=cutoff."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be a positive integer")
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or cutoff < 0:
        raise ValueError("cutoff must be a nonnegative integer")
    wheel = 1
    for p in primes_up_to(cutoff):
        wheel *= p
    return tuple(
        r for r in range(1, 2 * k + 1) if gcd(k * k + r, wheel) == 1
    )


def prime_or_semiprime_cutoff_decomposition(k: int) -> dict[str, object]:
    """Evaluate the exact P2 decomposition at the minimal cubic-root cutoff."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    upper = square_interval_upper(k)
    cutoff = int(almost_prime_cutoff(k, 2)["cutoff"])
    offsets = rough_survivor_offsets(k, cutoff)

    prime_offsets: list[int] = []
    semiprime_edges: list[tuple[int, int, int, int]] = []
    factor_primes = tuple(p for p in primes_up_to(k) if p > cutoff)

    for r in offsets:
        value = k * k + r
        if is_prime(value):
            prime_offsets.append(r)
            continue

        p = next((p for p in factor_primes if value % p == 0), None)
        if p is None:
            raise AssertionError("P2 rough composite lost its factor above cutoff")
        q = value // p
        if not is_prime(q):
            raise AssertionError("cubic-root rough survivor exceeded Omega=2")
        if not (cutoff < p <= k < q):
            raise AssertionError("P2 semiprime factors left the hyperbolic strip")
        semiprime_edges.append((p, q, value, r))

    if len(offsets) != len(prime_offsets) + len(semiprime_edges):
        raise AssertionError("P2 rough partition failed")
    if len(prime_offsets) != direct_square_interval_prime_count(k):
        raise AssertionError("P2 decomposition lost the exact prime count")

    # Hyperbolic prime-sum formula, evaluated directly for a finite regression.
    hyperbolic_edges: list[tuple[int, int, int, int]] = []
    q_primes = primes_up_to(upper // (cutoff + 1) + 1)
    for p in factor_primes:
        for q in q_primes:
            value = p * q
            if k * k < value <= upper:
                if q <= k:
                    raise AssertionError("hyperbolic cofactor failed to exceed k")
                hyperbolic_edges.append((p, q, value, value - k * k))
    if set(hyperbolic_edges) != set(semiprime_edges):
        raise AssertionError("P2 semiprime tail does not equal the hyperbolic prime sum")

    return {
        "k": k,
        "upper": upper,
        "cubic_root_cutoff": cutoff,
        "rough_offsets": offsets,
        "rough_count": len(offsets),
        "prime_offsets": tuple(prime_offsets),
        "prime_count": len(prime_offsets),
        "semiprime_edges": tuple(sorted(semiprime_edges)),
        "semiprime_count": len(semiprime_edges),
        "hyperbolic_prime_edges": tuple(sorted(hyperbolic_edges)),
        "prime_gap_equals_rough_minus_semiprime": True,
    }
