"""P017 residual hard-core: exact local Euler factors for global core mass.

After anchor/singular compensation, the natural cell weight is ``1/phi(S)``.
For a full-core product S with w distinct prime factors, assigning each complete
prime-power block to the lower or upper mirror side gives ``2^w`` ordered
coprime splits; excluding the two trivial sides leaves ``2^w-2`` nontrivial
core pairs.

The multiplicative leading weight ``2^omega(S)/phi(S)`` has an exact local
prime-power Euler factor.  For every prime p,

    1 + sum_{a>=1} 2/phi(p^a)
      = 1 + 2p/(p-1)^2
      = (p^2+1)/(p-1)^2.

Now suppose an odd prime p divides the common anchor M=k(k+1).  Comparing local
prime-pair opportunity with anchor-surviving demand introduces the square inverse
anchor factor

    p^2/(p-1)^2.

But gcd(S,M)=1 excludes p from every residual full-core product, deleting the
core Euler factor above.  Relative to the unrestricted local core mass, the net
factor is therefore

    [p^2/(p-1)^2] / [(p^2+1)/(p-1)^2]
      = p^2/(p^2+1) < 1.

This is an exact **local Euler-factor identity**, not yet a finite-cutoff
asymptotic theorem.  It identifies a genuine global cross-cell compensation:
anchor primes make individual affine cells locally more prime-pair-friendly,
but they simultaneously remove a slightly larger amount of full-core mass once
all coprime core products are summed.

The nonmultiplicative ``-2`` in ``2^omega(S)-2`` is retained explicitly by the
finite helper below; no asymptotic order is asserted here.
"""

from __future__ import annotations

from math import gcd

from .legendre import is_prime
from .p017_p018_anchor_singular_compensation import euler_phi


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _reduced_pair(numerator: int, denominator: int) -> tuple[int, int]:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    common = gcd(numerator, denominator)
    return numerator // common, denominator // common


def _add_pairs(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return _reduced_pair(
        left[0] * right[1] + right[0] * left[1],
        left[1] * right[1],
    )


def distinct_prime_factor_count(value: int) -> int:
    """Return omega(value), the number of distinct prime factors."""
    _require_positive("value", value)
    remaining = value
    count = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            count += 1
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        count += 1
    return count


def ordered_nontrivial_coprime_split_count(core_product: int) -> int:
    """Return 2^omega(S)-2, clipped at zero for prime-power S."""
    _require_positive("core_product", core_product)
    omega = distinct_prime_factor_count(core_product)
    if omega < 2:
        return 0
    return 2**omega - 2


def core_mass_euler_factor(prime: int) -> tuple[int, int]:
    """Return (p^2+1)/(p-1)^2 for the 2^omega/phi local mass."""
    _require_positive("prime", prime)
    if not is_prime(prime):
        raise ValueError("prime must be prime")
    return _reduced_pair(prime * prime + 1, (prime - 1) ** 2)


def anchor_demand_square_penalty(prime: int) -> tuple[int, int]:
    """Return the inverse square anchor-density factor p^2/(p-1)^2."""
    _require_positive("prime", prime)
    if not is_prime(prime):
        raise ValueError("prime must be prime")
    return _reduced_pair(prime * prime, (prime - 1) ** 2)


def anchor_core_relative_factor(prime: int) -> tuple[int, int]:
    """Return the exact net factor p^2/(p^2+1), always strictly below one."""
    mass_num, mass_den = core_mass_euler_factor(prime)
    penalty_num, penalty_den = anchor_demand_square_penalty(prime)
    relative = _reduced_pair(penalty_num * mass_den, penalty_den * mass_num)
    expected = _reduced_pair(prime * prime, prime * prime + 1)
    if relative != expected:
        raise AssertionError("anchor/core local Euler cancellation changed")
    if relative[0] >= relative[1]:
        raise AssertionError("anchor/core relative Euler factor is not <1")
    return relative


def prime_power_mass_partial(prime: int, max_exponent: int) -> dict[str, object]:
    """Return the exact finite partial sum and exact infinite-tail remainder.

    For A>=1,

      1 + sum_{a=1}^A 2/phi(p^a)

    differs from the full local Euler factor by

      2 / [p^(A-1) (p-1)^2].
    """
    _require_positive("prime", prime)
    _require_positive("max_exponent", max_exponent)
    if not is_prime(prime):
        raise ValueError("prime must be prime")

    partial = (1, 1)
    power = 1
    for exponent in range(1, max_exponent + 1):
        if exponent > 1:
            power *= prime
        phi_power = power * (prime - 1)
        partial = _add_pairs(partial, _reduced_pair(2, phi_power))

    full = core_mass_euler_factor(prime)
    remainder = _reduced_pair(2, prime ** (max_exponent - 1) * (prime - 1) ** 2)
    reconstructed = _add_pairs(partial, remainder)
    if reconstructed != full:
        raise AssertionError("finite prime-power mass plus remainder missed Euler factor")

    return {
        "prime": prime,
        "max_exponent": max_exponent,
        "partial_mass": partial,
        "tail_remainder": remainder,
        "full_euler_factor": full,
    }


def finite_split_totient_mass(
    bound: int,
    forbidden_primes: tuple[int, ...] = (),
) -> tuple[int, int]:
    """Return sum_{odd 3<=S<bound, gcd(S,F)=1}(2^omega(S)-2)/phi(S).

    This is an exact finite diagnostic only.  It deliberately keeps the global
    cutoff, so no Euler-product factorization is claimed for this quantity.
    """
    _require_positive("bound", bound)
    if bound < 3:
        return (0, 1)
    if len(set(forbidden_primes)) != len(forbidden_primes):
        raise ValueError("forbidden primes must be distinct")
    forbidden_product = 1
    for prime in forbidden_primes:
        if not is_prime(prime):
            raise ValueError("forbidden entries must be prime")
        forbidden_product *= prime

    total = (0, 1)
    for core_product in range(3, bound, 2):
        if gcd(core_product, forbidden_product) != 1:
            continue
        splits = ordered_nontrivial_coprime_split_count(core_product)
        if splits == 0:
            continue
        total = _add_pairs(total, _reduced_pair(splits, euler_phi(core_product)))
    return total


def anchor_normalized_finite_mass(
    bound: int,
    anchor_primes: tuple[int, ...],
) -> tuple[int, int]:
    """Divide finite coprime core mass by the squared odd-anchor density.

    This helper is diagnostic, not an asymptotic theorem.  It is useful for
    checking whether the exact local factor p^2/(p^2+1) is already visible at
    finite cutoffs.
    """
    mass = finite_split_totient_mass(bound, anchor_primes)
    density_num = 1
    density_den = 1
    for prime in anchor_primes:
        if prime == 2 or not is_prime(prime):
            raise ValueError("anchor_primes must be distinct odd primes")
        density_num *= prime - 1
        density_den *= prime
    return _reduced_pair(
        mass[0] * density_den * density_den,
        mass[1] * density_num * density_num,
    )
