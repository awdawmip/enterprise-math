"""Exact sieve projection and finite-future quotient for P017 quotient channels.

This module records a negative/structural boundary for the carry-refinement
monoid.  A nonempty parent channel state is

    y_t = y0 - 2t,      0 <= t < N,

and an odd refinement d keeps exactly the indices for which d | y_t.
Therefore, for an odd squarefree product P,

    sum_(d|P) mu(d) F_(Ed)
      = #{0<=t<N : gcd(y0-2t,P)=1}.

Because 2 is invertible modulo P, this is exactly an ordinary sifted interval
of N consecutive residue indices.  Thus the refinement monoid plus Mobius
alternation factors through the classical rough-number / Jacobsthal projector;
it does not by itself add parity-breaking information.

For a finite size-only future language D, the exact child-size formula is

    F_(Ed) = floor(N/d) + 1_{rho_d(y0) < N mod d},
    rho_d(y0) = y0 * 2^{-1} mod d.

Hence the coarsest exact observable quotient is the Boolean cut signature

    sigma_D(N,y0) = (1_{rho_d(y0)<N mod d})_(d in D).

The commonly used residue y0 mod lcm(D) is sufficient but generally strictly
finer than necessary.  If a future language is expressed as refinement words,
the monoid law reduces each word to its product before forming this signature.

At N=1 the boundary reverses: F_(Ed)=1 iff d|y0.  Prime futures recover the
radical, prime-power futures recover valuations, and the all-divisor future
recovers the positive odd integer y0 itself.  Universal descendant visibility
is therefore information-complete in the singleton regime.

Finally the roughness projector has the exact Ramanujan expansion

    1_(gcd(n,P)=1)
      = phi(P)/P * sum_(d|P) mu(d)/phi(d) c_d(n),

so channel-frequency conductor decompositions are another exact basis for the
same sieve object.

The project-specific surviving question is not generic channel sieving.  In the
square basin the E=1 origin is a low-height quadratic diagonal:

    y0 = (k+1)^2-2   for even k,
    y0 = (k+1)^2-3   for odd k.

Any genuinely new theorem must exploit this simultaneous coupling of origin,
interval length and prime cutoff rather than the abstract monoid alone.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd, lcm, prod

from .legendre import squarefree_divisors_with_mu
from .p017_p018_carry_refinement_channel import (
    refine_channel_state,
    signed_fiber_channel_state,
)


def _require_distinct_odd_primes(primes: tuple[int, ...]) -> tuple[int, ...]:
    normalized = tuple(sorted(int(p) for p in primes))
    if not normalized or len(set(normalized)) != len(normalized):
        raise ValueError("primes must be a nonempty tuple of distinct odd primes")
    for prime in normalized:
        if prime < 3 or prime % 2 == 0:
            raise ValueError("primes must be odd")
        divisor = 3
        while divisor * divisor <= prime:
            if prime % divisor == 0:
                raise ValueError("entries must be prime")
            divisor += 2
    return normalized


def _require_nonempty_channel(fiber_size: int, first_quotient: int) -> None:
    if isinstance(fiber_size, bool) or not isinstance(fiber_size, int) or fiber_size < 1:
        raise ValueError("fiber_size must be a positive integer")
    if isinstance(first_quotient, bool) or not isinstance(first_quotient, int) or first_quotient <= 0:
        raise ValueError("first_quotient must be a positive integer")
    if first_quotient % 2 == 0:
        raise ValueError("first_quotient must be odd")


def size_only_future_signature(
    fiber_size: int,
    first_quotient: int,
    refinements: tuple[int, ...],
) -> dict[str, object]:
    """Return the coarsest exact cut signature for declared child-size futures."""
    _require_nonempty_channel(fiber_size, first_quotient)
    normalized = tuple(sorted(set(int(d) for d in refinements)))
    if not normalized:
        raise ValueError("refinements must be nonempty")
    child_sizes: list[int] = []
    cut_bits: list[int] = []
    modulus = 1
    for d in normalized:
        if d < 1 or d % 2 == 0:
            raise ValueError("refinements must be positive odd integers")
        data = refine_channel_state(fiber_size, first_quotient, d)
        child = int(data["child_fiber_size"])
        coarse = fiber_size // d
        bit = child - coarse
        if bit not in (0, 1):
            raise AssertionError("child-size cut bit left the binary range")
        child_sizes.append(child)
        cut_bits.append(bit)
        modulus = lcm(modulus, d)

    residue_state = first_quotient % modulus
    return {
        "fiber_size": fiber_size,
        "first_quotient": first_quotient,
        "refinements": normalized,
        "child_sizes": tuple(child_sizes),
        "cut_signature": tuple(cut_bits),
        "lcm_modulus": modulus,
        "lcm_residue_sufficient_state": residue_state,
        "coarsest_size_only_observable": "cut_signature",
    }


def same_size_only_future_class(
    fiber_size: int,
    first_quotient_a: int,
    first_quotient_b: int,
    refinements: tuple[int, ...],
) -> bool:
    """Return whether two origins are observationally equal for the declared sizes."""
    a = size_only_future_signature(fiber_size, first_quotient_a, refinements)
    b = size_only_future_signature(fiber_size, first_quotient_b, refinements)
    same_signature = a["cut_signature"] == b["cut_signature"]
    if same_signature != (a["child_sizes"] == b["child_sizes"]):
        raise AssertionError("cut signature failed exact child-size factorization")
    return same_signature


def mobius_channel_sieve_projection(
    fiber_size: int,
    first_quotient: int,
    primes: tuple[int, ...],
) -> dict[str, object]:
    """Certify that the full descendant Mobius transform is a roughness count."""
    _require_nonempty_channel(fiber_size, first_quotient)
    normalized = _require_distinct_odd_primes(primes)
    P = prod(normalized)
    rows: list[dict[str, int]] = []
    mobius_sum = 0
    for divisor, mu in squarefree_divisors_with_mu(list(normalized)):
        child = refine_channel_state(fiber_size, first_quotient, divisor)
        size = int(child["child_fiber_size"])
        mobius_sum += mu * size
        rows.append({"divisor": divisor, "mu": mu, "child_fiber_size": size})

    rough = sum(
        gcd(first_quotient - 2 * t, P) == 1
        for t in range(fiber_size)
    )
    inverse_two = pow(2, -1, P)
    shifted_origin = (first_quotient * inverse_two) % P
    consecutive = sum(
        gcd(shifted_origin - t, P) == 1
        for t in range(fiber_size)
    )
    if mobius_sum != rough or rough != consecutive:
        raise AssertionError("channel Mobius transform failed rough-interval projection")

    return {
        "fiber_size": fiber_size,
        "first_quotient": first_quotient,
        "primes": normalized,
        "primorial": P,
        "mobius_descendant_sum": mobius_sum,
        "rough_progression_count": rough,
        "consecutive_rough_interval_count": consecutive,
        "consecutive_shift_origin_mod_primorial": shifted_origin,
        "rows": tuple(rows),
        "exact_roughness_projection": True,
    }


def _squarefree_phi(modulus: int, prime_factors: tuple[int, ...]) -> int:
    result = modulus
    for prime in prime_factors:
        result = result // prime * (prime - 1)
    return result


def ramanujan_sum_squarefree(n: int, modulus: int, primes: tuple[int, ...]) -> int:
    """Return c_modulus(n) by c_d(n)=sum_(e|(d,n)) e mu(d/e)."""
    if modulus < 1:
        raise ValueError("modulus must be positive")
    factors = tuple(p for p in primes if modulus % p == 0)
    if prod(factors, start=1) != modulus:
        raise ValueError("modulus must be squarefree over the declared primes")
    total = 0
    for divisor, _mu_divisor in squarefree_divisors_with_mu(list(factors)):
        if n % divisor:
            continue
        complement = modulus // divisor
        omega_complement = sum(1 for p in factors if complement % p == 0)
        mu_complement = -1 if omega_complement % 2 else 1
        total += divisor * mu_complement
    return total


def ramanujan_channel_projection(
    fiber_size: int,
    first_quotient: int,
    primes: tuple[int, ...],
) -> dict[str, object]:
    """Reconstruct the same roughness count in the exact Ramanujan basis."""
    base = mobius_channel_sieve_projection(fiber_size, first_quotient, primes)
    normalized = tuple(base["primes"])
    P = int(base["primorial"])
    phi_P = prod(p - 1 for p in normalized)
    inner = Fraction(0, 1)
    rows: list[dict[str, object]] = []
    for divisor, mu in squarefree_divisors_with_mu(list(normalized)):
        factors = tuple(p for p in normalized if divisor % p == 0)
        phi_d = _squarefree_phi(divisor, factors)
        ramanujan_progression_sum = sum(
            ramanujan_sum_squarefree(first_quotient - 2 * t, divisor, normalized)
            for t in range(fiber_size)
        )
        term = Fraction(mu * ramanujan_progression_sum, phi_d)
        inner += term
        rows.append(
            {
                "conductor": divisor,
                "mu": mu,
                "phi": phi_d,
                "ramanujan_progression_sum": ramanujan_progression_sum,
                "weighted_term": term,
            }
        )

    value = Fraction(phi_P, P) * inner
    if value.denominator != 1:
        raise AssertionError("Ramanujan roughness projection failed integrality")
    if value.numerator != int(base["rough_progression_count"]):
        raise AssertionError("Ramanujan basis disagrees with Mobius roughness projector")
    return {
        **base,
        "ramanujan_projection": value,
        "ramanujan_rows": tuple(rows),
        "frequency_basis_adds_no_information": True,
    }


def singleton_divisor_future(first_quotient: int) -> dict[str, object]:
    """Show that the universal odd-divisor future recovers a singleton origin exactly."""
    _require_nonempty_channel(1, first_quotient)
    surviving: list[int] = []
    for d in range(1, first_quotient + 1, 2):
        child = refine_channel_state(1, first_quotient, d)
        if int(child["child_fiber_size"]):
            surviving.append(d)
    expected = [d for d in range(1, first_quotient + 1, 2) if first_quotient % d == 0]
    if surviving != expected or not surviving or surviving[-1] != first_quotient:
        raise AssertionError("singleton all-divisor future failed exact origin recovery")
    return {
        "first_quotient": first_quotient,
        "surviving_odd_refinements": tuple(surviving),
        "largest_surviving_refinement": surviving[-1],
        "universal_divisor_future_recovers_origin": True,
    }


def square_basin_quadratic_diagonal(k: int, primes: tuple[int, ...]) -> dict[str, object]:
    """Expose the non-generic low-height quadratic origin of the E=1 channel."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    normalized = _require_distinct_odd_primes(primes)
    K = k - 1
    state = signed_fiber_channel_state(K, 1)
    N = int(state["fiber_size"])
    y0 = int(state["first_quotient"])
    offset = 2 if k % 2 == 0 else 3
    if y0 + offset != (k + 1) ** 2:
        raise AssertionError("E=1 channel origin lost its square-diagonal identity")
    expected_N = k if k % 2 == 0 else k - 1
    if N != expected_N:
        raise AssertionError("E=1 channel length disagrees with basin parity")

    channels: list[dict[str, int]] = []
    for prime in normalized:
        tau = (y0 * pow(2, -1, prime)) % prime
        if (2 * tau + offset - (k + 1) ** 2) % prime:
            raise AssertionError("prime channel lost the common quadratic phase")
        channels.append({"prime": prime, "forbidden_index_residue": tau})

    return {
        "k": k,
        "K": K,
        "fiber_size": N,
        "first_quotient": y0,
        "square_offset": offset,
        "square_identity": y0 + offset,
        "prime_channels": tuple(channels),
        "quadratic_diagonal": True,
    }
