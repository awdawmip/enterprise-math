"""Exact local Euler cancellation for singular-weighted residual core mass.

The finite-wheel bridge shows that after anchor normalization one residual
full-core cell carries the arithmetic weight

    (1/S) * prod_{p|S} p/(p-1)
          * prod_{p odd, p∤M*S} c_p,

where

    c_p = p(p-2)/(p-1)^2

is the generic two-linear-form local factor.  Factoring out the global generic
product over allowed odd primes converts a core prime p into the extra factor
``1/c_p`` on top of ``1/phi(S)``.

For the leading ordered-split weight ``2^omega(S)`` the complete prime-power
local sum at an allowed core prime is therefore

    1 + sum_{a>=1} 2 / (phi(p^a) c_p)
      = p/(p-2).

After extracting ``zeta(1+s)^2``, its s=0 local correction is

    [p/(p-2)] (1-1/p)^2 = 1/c_p.

Multiplying back the generic factor c_p gives **exactly one**.  Thus every odd
prime not dividing M disappears from the leading local constant.  An odd anchor
prime p|M is excluded from the core Euler product and from the generic twin
product, leaving only

    (1-1/p)^2.

The omitted prime 2 contributes ``(1-1/2)^2=1/4``.  Therefore the complete
finite local leading correction is exactly

    (1/4) * prod_{odd p|M} (1-1/p)^2 = delta_M^2 / 4.

If a standard double-pole Selberg--Delange/Tauberian theorem is later applied,
the corresponding partial-sum ``log(x)^2`` leading coefficient is half of this,
namely ``delta_M^2/8``.  The executable layer below proves only the exact local
Euler algebra; it does not claim the analytic asymptotic or a uniform error.

This cancellation is useful because it shows that the generic twin-product
constant and the full-core split Euler inflation are not independent losses.
"""

from __future__ import annotations

from math import gcd

from .legendre import is_prime


def _require_odd_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 3
        or not is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")


def reduced_pair(numerator: int, denominator: int) -> tuple[int, int]:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    common = gcd(numerator, denominator)
    return numerator // common, denominator // common


def multiply_pairs(*pairs: tuple[int, int]) -> tuple[int, int]:
    numerator = 1
    denominator = 1
    for left, right in pairs:
        numerator *= left
        denominator *= right
    return reduced_pair(numerator, denominator)


def generic_twin_local_factor(prime: int) -> tuple[int, int]:
    """Return c_p=p(p-2)/(p-1)^2."""
    _require_odd_prime(prime)
    return reduced_pair(prime * (prime - 2), (prime - 1) ** 2)


def core_prime_power_local_sum(prime: int) -> tuple[int, int]:
    """Return 1+sum_{a>=1}2/(phi(p^a)c_p)=p/(p-2)."""
    _require_odd_prime(prime)
    return reduced_pair(prime, prime - 2)


def allowed_prime_leading_cancellation(prime: int) -> dict[str, tuple[int, int] | int]:
    """Certify c_p * L_p(0) * (1-1/p)^2 = 1 exactly."""
    _require_odd_prime(prime)
    twin = generic_twin_local_factor(prime)
    core_local = core_prime_power_local_sum(prime)
    zeta_correction = reduced_pair((prime - 1) ** 2, prime * prime)
    combined = multiply_pairs(twin, core_local, zeta_correction)
    if combined != (1, 1):
        raise AssertionError("allowed-prime twin/core Euler factors did not cancel")
    return {
        "prime": prime,
        "generic_twin_factor": twin,
        "core_prime_power_local_sum": core_local,
        "zeta_extraction_factor": zeta_correction,
        "combined": combined,
    }


def anchor_prime_leading_factor(prime: int) -> tuple[int, int]:
    """Return the residual local factor (1-1/p)^2 for an odd p|M."""
    _require_odd_prime(prime)
    return reduced_pair((prime - 1) ** 2, prime * prime)


def finite_leading_correction(anchor_primes: tuple[int, ...]) -> dict[str, object]:
    """Return the exact finite leading correction delta_A^2/4.

    ``anchor_primes`` is the distinct odd-prime set dividing the chosen center M.
    The factor 1/4 is the missing p=2 Euler correction.
    """
    if len(set(anchor_primes)) != len(anchor_primes):
        raise ValueError("anchor primes must be distinct")
    normalized = tuple(sorted(anchor_primes))
    correction = (1, 4)
    delta = (1, 1)
    rows: list[dict[str, object]] = []
    for prime in normalized:
        _require_odd_prime(prime)
        local = anchor_prime_leading_factor(prime)
        correction = multiply_pairs(correction, local)
        delta = multiply_pairs(delta, reduced_pair(prime - 1, prime))
        rows.append({"prime": prime, "local_factor": local})

    delta_squared_over_four = multiply_pairs((1, 4), delta, delta)
    if correction != delta_squared_over_four:
        raise AssertionError("finite leading correction is not delta^2/4")

    # A double pole converts G(0) into G(0)/2 as the log^2 coefficient.  We
    # return the algebraic candidate coefficient but do not assert an asymptotic.
    candidate_log2_coefficient = reduced_pair(correction[0], 2 * correction[1])
    return {
        "anchor_primes": normalized,
        "odd_anchor_density": delta,
        "leading_correction": correction,
        "candidate_log2_coefficient": candidate_log2_coefficient,
        "rows": tuple(rows),
    }
