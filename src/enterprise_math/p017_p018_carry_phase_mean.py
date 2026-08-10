"""Exact period statistics of the unified centered square-basin carry field.

After the terminal P017×P018 precision route is fully collapsed, anchor and
transverse squarefree moduli recombine into one ordinary odd squarefree modulus
E.  Put K=k-1 and M=(K+1)(K+2).  For any positive odd E, the odd signed points

    -K <= x <= K,
    x = M (mod E)

form one residue class modulo 2E.  Hence their exact count has the form

    F_E(K) = floor(K/E) + eta_E(K),

where eta_E(K) is a binary centered carry.  Since both K mod 2E and M mod 2E
are periodic, eta_E is a period-2E binary phase field.

For odd squarefree E, this period has an exact mean:

    sum_(K=0)^(2E-1) eta_E(K) = E + 1 - 2^omega(E).

Proof by square-basin counting.  Let k=K+1 range from 1 through 2E.  The full
open consecutive-square intervals contain 2E+1 odd multiples of E after the
unique odd square endpoint E^2 is removed.  The centered P017 basin stops at
(k+1)^2-2, so for odd k it additionally omits k(k+2).  The congruence

    k(k+2)=0 (mod E)

has exactly 2^omega(E) solutions modulo E (choose k=0 or -2 independently at
every p|E), and because E is odd every residue has exactly one odd lift in a
length-2E interval.  Thus

    sum_K F_E(K) = 2E+1-2^omega(E).

Meanwhile sum_(K mod 2E) floor(K/E)=E, proving the carry formula.

There is also a universal half-period imbalance for squarefree E>1:

    sum_(K=E)^(2E-1) eta_E(K)
      - sum_(K=0)^(E-1) eta_E(K) = 2.

Indeed, on k=1,...,E the full open-square union contributes (E+1)/2 relevant
odd multiples after the square endpoint is removed.  Among the 2^omega(E) CRT
roots of k(k+2)=0 mod E represented in 1,...,E, exactly 2^(omega(E)-1)+1 are
odd: the two trivial roots E and E-2 are both odd, while every nontrivial root
pairs with -2-k, and the two representatives in such a pair sum to E-2 and
therefore have opposite parity.  Hence the first half carry mass is

    (E-1-2^omega(E))/2,

and subtraction from the full-period total gives the second half

    (E+3-2^omega(E))/2.

Finally, for a nonempty squarefree product P of odd primes, the Mobius-weighted
period means factor exactly:

    sum_(E|P) mu(E) mean(eta_E)
      = 1/2 * [ product_(p|P)(1-1/p)
                - product_(p|P)(1-2/p) ].

Thus the period-average component is precisely a local Euler-product quantity.
All additional pointwise information in the boundary prime-count identity lives
in the coherent oscillatory phase eta_E(K)-mean(eta_E).  This reinforces the
already-known negative boundary that independent local densities alone cannot
close the Legendre pressure test.

This is a finite periodic-carry theorem, not a prime-gap theorem and not a proof
of Legendre's conjecture.
"""

from __future__ import annotations

from fractions import Fraction
from math import prod

from .legendre import squarefree_divisors_with_mu


def _odd_squarefree_prime_factors(value: int) -> tuple[int, ...]:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1 or value % 2 == 0:
        raise ValueError("value must be a positive odd integer")
    remaining = value
    factors: list[int] = []
    candidate = 3
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            factors.append(candidate)
            remaining //= candidate
            if remaining % candidate == 0:
                raise ValueError("value must be squarefree")
        candidate += 2
    if remaining > 1:
        factors.append(remaining)
    if prod(factors, start=1) != value:
        raise AssertionError("odd squarefree factorization failed")
    return tuple(factors)


def unified_centered_carry_bit(K: int, modulus: int) -> int:
    """Return eta_E(K) for any positive odd modulus E.

    This unified carry permits E to share factors with M=(K+1)(K+2); after the
    anchor/transverse Mobius layers are recombined, transversality is no longer
    the appropriate restriction.
    """
    if isinstance(K, bool) or not isinstance(K, int) or K < 0:
        raise ValueError("K must be a nonnegative integer")
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 1 or modulus % 2 == 0:
        raise ValueError("modulus must be a positive odd integer")

    E = modulus
    center = (K + 1) * (K + 2)
    period = 2 * E
    raw = center % E
    residue = raw if raw % 2 else raw + E
    residue %= period

    first = -((-K - residue) // period)
    last = (K - residue) // period
    exact = max(0, last - first + 1)
    coarse = K // E
    carry = exact - coarse
    if carry not in (0, 1):
        raise AssertionError("unified centered carry left the binary range")
    return carry


def carry_period_profile(modulus: int) -> dict[str, object]:
    """Verify the exact full-period and half-period squarefree carry formulas."""
    factors = _odd_squarefree_prime_factors(modulus)
    E = modulus
    omega = len(factors)
    sequence = tuple(unified_centered_carry_bit(K, E) for K in range(2 * E))
    total = sum(sequence)
    expected = E + 1 - 2**omega
    if total != expected:
        raise AssertionError("squarefree carry period mass disagrees with exact formula")

    first_half = sum(sequence[:E])
    second_half = sum(sequence[E:])
    if E == 1:
        expected_first = 0
        expected_second = 1
        imbalance = 1
    else:
        expected_first = (E - 1 - 2**omega) // 2
        expected_second = (E + 3 - 2**omega) // 2
        imbalance = 2
    if first_half != expected_first or second_half != expected_second:
        raise AssertionError("squarefree carry half-period formula failed")
    if second_half - first_half != imbalance:
        raise AssertionError("squarefree carry half-period imbalance failed")

    return {
        "modulus": E,
        "prime_factors": factors,
        "omega": omega,
        "period": 2 * E,
        "period_carry_mass": total,
        "period_carry_mass_formula": expected,
        "period_mean": Fraction(total, 2 * E),
        "first_half_carry_mass": first_half,
        "second_half_carry_mass": second_half,
        "second_minus_first_half": imbalance,
        "sequence": sequence,
    }


def mobius_weighted_period_mean(primes: tuple[int, ...]) -> dict[str, object]:
    """Return the exact factorized Mobius sum of carry period means."""
    normalized = tuple(sorted(int(p) for p in primes))
    if not normalized or len(set(normalized)) != len(normalized):
        raise ValueError("primes must be a nonempty tuple of distinct odd primes")
    for prime in normalized:
        if prime < 3 or prime % 2 == 0:
            raise ValueError("primes must be odd")
        # Minimal primality check is sufficient for this bounded reference.
        divisor = 3
        while divisor * divisor <= prime:
            if prime % divisor == 0:
                raise ValueError("entries must be prime")
            divisor += 2

    direct = Fraction(0, 1)
    rows: list[dict[str, object]] = []
    for divisor, mu in squarefree_divisors_with_mu(list(normalized)):
        profile = carry_period_profile(divisor)
        mean = profile["period_mean"]
        direct += mu * mean
        rows.append({"divisor": divisor, "mu": mu, "period_mean": mean})

    phi_factor = prod((Fraction(prime - 1, prime) for prime in normalized), start=Fraction(1, 1))
    two_root_factor = prod((Fraction(prime - 2, prime) for prime in normalized), start=Fraction(1, 1))
    factorized = Fraction(1, 2) * (phi_factor - two_root_factor)
    if direct != factorized:
        raise AssertionError("Mobius carry-period mean failed Euler-product factorization")

    return {
        "primes": normalized,
        "primorial": prod(normalized),
        "direct_mobius_period_mean": direct,
        "factorized_mobius_period_mean": factorized,
        "phi_euler_factor": phi_factor,
        "two_root_euler_factor": two_root_factor,
        "rows": tuple(rows),
    }
