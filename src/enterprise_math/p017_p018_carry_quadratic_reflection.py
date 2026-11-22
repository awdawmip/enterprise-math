"""Quadratic reflection law for the unified P017×P018 Mobius carry field.

Let eta_E(K) be the period-2E unified centered carry, extended periodically to
all integer K.  The consecutive-product center

    (K+1)(K+2)

is invariant under the involution

    K -> -K-3.

For one odd squarefree modulus E the two reflected carry bits are almost
complementary.  The exceptional orbit is controlled by two explicit divisibility
conditions.  After Mobius recombination over every divisor E|P of a nontrivial
odd squarefree product P, those divisibility conditions collapse to only two
roughness bits:

    C_P(K) + C_P(-K-3)
      = 1_{gcd(P,H(K))=1} - 1_{gcd(P,A(K))=1},

where

    H(K)=(K+2)/2, A(K)=(K+1)(K+3)   if K is even,
    H(K)=(K+1)/2, A(K)=K(K+2)       if K is odd.

Here

    C_P(K)=sum_{E|P} mu(E) eta_E(K).

Thus an entire cross-modulus binary phase field has a reflection defect of only
two bits.  This is stronger than period averages or half-period skews, but it is
still an exact representation identity rather than a prime-gap theorem.

At the physical square-basin phase K=k-1 with

    P_k=product_{3<=p<k, p prime} p,

one gets the exact endpoint specialization (k>=4):

    k even:
      C_P(k-1)+C_P(-k-2)=1_{k is a power of two};

    k odd (k>=5):
      C_P(k-1)+C_P(-k-2)
        =1_{k+1 is a power of two}-1_{k and k+2 are twin primes}.

Combining this with the existing terminal boundary identity gives the
orientation-dual exact prime-count formula

    pi((k+1)^2)-pi(k^2)
      = L_2(k-1) + rho(k) - C_{P_k}(-k-2).

The theorem does not prove positivity.  It converts the physical carry lower
bound into an orientation-dual carry upper bound plus a tiny explicit endpoint
defect, exposing a new cross-phase interface for further work.
"""

from __future__ import annotations

from math import gcd, prod

from .legendre import primes_up_to, squarefree_divisors_with_mu
from .p017_p018_bonferroni_precision import signed_support_profile
from .p017_p018_boundary_prime_count_identity import dyadic_bulk_axis_count
from .p017_p018_carry_phase_mean import unified_centered_carry_bit


def _require_odd_prime_tuple(primes: tuple[int, ...]) -> tuple[int, ...]:
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


def periodic_unified_carry(K: int, modulus: int) -> int:
    """Extend eta_E periodically from nonnegative representatives to all integers."""
    if isinstance(K, bool) or not isinstance(K, int):
        raise ValueError("K must be an integer")
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 1 or modulus % 2 == 0:
        raise ValueError("modulus must be a positive odd integer")
    representative = K % (2 * modulus)
    return unified_centered_carry_bit(representative, modulus)


def mobius_carry_field(K: int, primes: tuple[int, ...]) -> int:
    """Return C_P(K)=sum_{E|P} mu(E) eta_E(K)."""
    normalized = _require_odd_prime_tuple(primes)
    return sum(
        mu * periodic_unified_carry(K, divisor)
        for divisor, mu in squarefree_divisors_with_mu(list(normalized))
    )


def reflection_observables(K: int) -> dict[str, int]:
    """Return the two explicit integer observables in the reflection defect."""
    if isinstance(K, bool) or not isinstance(K, int):
        raise ValueError("K must be an integer")
    if K % 2 == 0:
        half_observable = (K + 2) // 2
        adjacent_observable = (K + 1) * (K + 3)
    else:
        half_observable = (K + 1) // 2
        adjacent_observable = K * (K + 2)
    return {
        "K": K,
        "half_observable": half_observable,
        "adjacent_observable": adjacent_observable,
    }


def mobius_carry_quadratic_reflection(
    K: int,
    primes: tuple[int, ...],
) -> dict[str, object]:
    """Verify the exact two-bit quadratic-reflection law on one squarefree P."""
    normalized = _require_odd_prime_tuple(primes)
    P = prod(normalized)
    observables = reflection_observables(K)
    half = int(observables["half_observable"])
    adjacent = int(observables["adjacent_observable"])

    physical = mobius_carry_field(K, normalized)
    reflected = mobius_carry_field(-K - 3, normalized)
    half_rough = int(gcd(P, half) == 1)
    adjacent_rough = int(gcd(P, adjacent) == 1)
    rhs = half_rough - adjacent_rough
    if physical + reflected != rhs:
        raise AssertionError("Mobius carry quadratic reflection law failed")

    return {
        "K": K,
        "reflected_K": -K - 3,
        "primes": normalized,
        "primorial": P,
        "physical_carry_field": physical,
        "reflected_carry_field": reflected,
        "half_observable": half,
        "adjacent_observable": adjacent,
        "half_roughness_bit": half_rough,
        "adjacent_roughness_bit": adjacent_rough,
        "reflection_defect": rhs,
        "quadratic_reflection_identity": True,
    }


def _is_power_of_two(value: int) -> bool:
    return value > 0 and value & (value - 1) == 0


def physical_square_reflection(k: int) -> dict[str, object]:
    """Specialize the reflection defect to P_k=product of odd primes below k."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")
    primes = tuple(p for p in primes_up_to(k - 1) if p % 2 == 1)
    if not primes:
        raise AssertionError("k>=4 should have at least one odd prime below k")
    data = mobius_carry_quadratic_reflection(k - 1, primes)

    if k % 2 == 0:
        expected = int(_is_power_of_two(k))
        endpoint_kind = "EVEN_DYADIC" if expected else "EVEN_GENERIC"
        dyadic_successor = False
        twin_endpoint = False
    else:
        dyadic_successor = _is_power_of_two(k + 1)
        adjacent_bit = int(data["adjacent_roughness_bit"])
        # For odd k>=5, gcd(k(k+2),P_k)=1 iff both k and k+2 are prime.
        twin_endpoint = bool(adjacent_bit)
        expected = int(dyadic_successor) - int(twin_endpoint)
        endpoint_kind = (
            "ODD_DYADIC_SUCCESSOR"
            if dyadic_successor
            else "ODD_TWIN_ENDPOINT"
            if twin_endpoint
            else "ODD_GENERIC"
        )

    if int(data["reflection_defect"]) != expected:
        raise AssertionError("physical reflection defect classification failed")
    return {
        **data,
        "k": k,
        "physical_K": k - 1,
        "orientation_dual_K": -k - 2,
        "endpoint_kind": endpoint_kind,
        "k_is_power_of_two": _is_power_of_two(k),
        "k_plus_one_is_power_of_two": dyadic_successor,
        "twin_prime_endpoint_bit": twin_endpoint,
        "physical_reflection_defect": expected,
    }


def orientation_dual_prime_count_diagnostic(k: int) -> dict[str, object]:
    """Bounded exact diagnostic of the orientation-dual prime-count identity."""
    data = physical_square_reflection(k)
    dyadic = dyadic_bulk_axis_count(k)
    reflected = int(data["reflected_carry_field"])
    rho = int(data["physical_reflection_defect"])
    predicted = dyadic + rho - reflected
    actual = int(signed_support_profile(k)["prime_state_count"])
    if predicted != actual:
        raise AssertionError("orientation-dual boundary identity missed prime count")
    return {
        **data,
        "dyadic_bulk_axis_count": dyadic,
        "orientation_dual_predicted_prime_count": predicted,
        "actual_prime_count": actual,
        "orientation_dual_prime_count_identity": True,
    }
