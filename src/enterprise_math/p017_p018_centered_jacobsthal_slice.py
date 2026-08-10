"""Centered low-height Jacobsthal slice for the P017 consecutive-square basin.

The terminal carry/roughness reduction can be stated as one exact constrained
Jacobsthal problem rather than as an arbitrary covering system.

Fix k>=4 and put

    P_k = product of all odd primes p<k.

The E=1 signed square-basin channel consists exactly of the odd candidate states
that can possibly be prime after the deterministic composite endpoint is
removed.  Written in descending order,

    y_t = y_0 - 2t,        0<=t<N_k,

where

    k even: N_k=k,   y_0=(k+1)^2-2,
    k odd:  N_k=k-1, y_0=(k+1)^2-3.

Every y_t lies strictly between k^2 and (k+1)^2.  Moreover

    gcd(y_t,P_k)=1  iff  y_t is prime.

The nontrivial direction is elementary: if y_t were composite, its least prime
factor would be <=sqrt(y_t)<k+1 and hence <=k.  It cannot equal k, because
writing y_t=M-x_t with M=k(k+1) and |x_t|<k would make k|x_t; the signed
candidate x_t is odd and nonzero.  Thus a composite y_t has an odd prime factor
strictly below k and is not P_k-rough.

Now set

    z_t = (P_k+y_t)/2.

Both P_k and y_t are odd, so z_t is integral and

    z_t=z_0-t.

Also 2 is invertible modulo the odd P_k, hence

    gcd(z_t,P_k)=gcd(y_t,P_k).

Therefore the prime-count question is exactly the existence of a reduced
residue in one distinguished interval of N_k consecutive integers:

    I_k = {z_0-N_k+1,...,z_0},
    z_0 = P_k/2 + y_0/2.

The displacement from the half-primorial is only quadratic in k, while a generic
Jacobsthal covering may place its bad interval at an arbitrary phase modulo
P_k.  This is the precise surviving content of the earlier ``low CRT root
height'' observation.

Thus a prime-free consecutive-square basin is equivalent to a *centered
low-height Jacobsthal covering* of this specific slice.  This equivalence is a
frontier coordinate, not a proof of Legendre's conjecture; any argument that
only proves a generic Jacobsthal bound without using the constrained phase has
not used the remaining square-basin structure.
"""

from __future__ import annotations

from math import gcd, prod

from .legendre import is_prime, primes_up_to


def odd_primorial_below_k(k: int) -> int:
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")
    return prod((p for p in primes_up_to(k - 1) if p % 2 == 1), start=1)


def square_basin_candidate_progression(k: int) -> dict[str, object]:
    """Return the exact E=1 odd candidate progression y_t."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")
    if k % 2 == 0:
        count = k
        top = (k + 1) ** 2 - 2
        endpoint_rule = "EVEN_K_ALL_ODD_INTERIOR_CANDIDATES"
    else:
        count = k - 1
        top = (k + 1) ** 2 - 3
        endpoint_rule = "ODD_K_OMIT_GUARANTEED_COMPOSITE_UPPER_MINUS_ONE"
    values = tuple(top - 2 * t for t in range(count))
    if not values or values[-1] <= k * k or values[0] >= (k + 1) ** 2:
        raise AssertionError("candidate progression left the open square basin")
    if any(value % 2 == 0 for value in values):
        raise AssertionError("candidate progression must be odd")
    return {
        "k": k,
        "candidate_count": count,
        "top_candidate": top,
        "bottom_candidate": values[-1],
        "endpoint_rule": endpoint_rule,
        "candidates": values,
    }


def centered_jacobsthal_slice(k: int) -> dict[str, object]:
    """Map the square-basin candidates to one consecutive interval near P_k/2."""
    data = square_basin_candidate_progression(k)
    P = odd_primorial_below_k(k)
    candidates = tuple(int(value) for value in data["candidates"])
    interval = tuple((P + value) // 2 for value in candidates)
    if any(P + value % 2 == 0 for value in ()):  # pragma: no cover - documentation guard
        raise AssertionError("unreachable")
    if any((P + value) % 2 != 0 for value in candidates):
        raise AssertionError("half-primorial coordinate is not integral")
    if any(interval[index] - interval[index + 1] != 1 for index in range(len(interval) - 1)):
        raise AssertionError("half-primorial image is not a consecutive interval")

    prime_bits: list[int] = []
    rough_bits: list[int] = []
    for value, shifted in zip(candidates, interval):
        rough = int(gcd(value, P) == 1)
        shifted_rough = int(gcd(shifted, P) == 1)
        if rough != shifted_rough:
            raise AssertionError("half-primorial translation changed roughness")
        prime = int(is_prime(value))
        if rough != prime:
            raise AssertionError("P_k-rough candidate is not equivalent to primality")
        rough_bits.append(rough)
        prime_bits.append(prime)

    prime_count = sum(prime_bits)
    return {
        **data,
        "odd_primorial_below_k": P,
        "half_primorial_interval_descending": interval,
        "interval_low": interval[-1],
        "interval_high": interval[0],
        "interval_length": len(interval),
        "top_offset_twice_from_half_primorial": candidates[0],
        "bottom_offset_twice_from_half_primorial": candidates[-1],
        "roughness_bits": tuple(rough_bits),
        "prime_bits": tuple(prime_bits),
        "prime_count": prime_count,
        "prime_free_basin": prime_count == 0,
        "fully_covered_centered_jacobsthal_slice": not any(rough_bits),
        "centered_jacobsthal_equivalence": True,
    }
