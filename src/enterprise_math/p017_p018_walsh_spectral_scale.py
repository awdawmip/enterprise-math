"""Exact conductor-energy law and generalized-Dickman scale for the orientation-Walsh sieve.

Let the upper orientation-Walsh weight be periodic modulo the squarefree product
P of its transverse odd primes.  With normalized Fourier transform, the local
prime factor has zero-frequency coefficient 1 and total nonzero-frequency L2
energy 2/p.  CRT independence therefore gives an exact conductor decomposition:

    E(q) = sum_{frequency conductor exactly q} |fhat|^2
         = 2^omega(q)/q,          q|P.

Consequently the total second moment is

    Z = sum_{q|P} E(q) = product_{p|P}(1+2/p).

Normalize E(q) by Z.  The resulting random squarefree conductor Q has independent
prime indicators

    B_p ~ Bernoulli(2/(p+2)),
    Q = product p^B_p.

This makes the multiplicative spectral scale completely explicit.  In
particular

    E[log Q] = sum_p 2 log p/(p+2),
    Var(log Q)=sum_p 2p (log p)^2/(p+2)^2.

For the physical transverse family p<=k, p not dividing k(k+1), classical prime
partial summation gives

    log Q / log k  ==>  D_2,

where D_2 is the generalized Dickman distribution with parameter 2, equivalently
the sum of the points of a scale-invariant Poisson process on (0,1) with
intensity 2 du/u.  Indeed for fixed real s,

    log E exp(s log Q/log k)
      -> 2 integral_0^1 (exp(su)-1) du/u.

Deleting the finitely many anchor primes p|k(k+1) does not affect the limit: for
fixed s their contribution is bounded by O((log log k)/log k).  Thus

    E[log Q]/log k -> 2,
    Var(log Q)/(log k)^2 -> 1,

and more generally the limiting cumulant of order j is 2/j.

The generalized-Dickman limit is classical probabilistic number theory.  The
project-specific content is its exact emergence as the L2 conductor-energy law
of the mirror orientation-Walsh sieve.  A key negative consequence is that the
spectrum is **not concentrated** at q~k^2: its logarithmic standard deviation is
itself asymptotic to log k.  Any useful conductor decomposition must therefore
retain multiple logarithmic scale bands rather than one hard critical modulus.

This theorem describes complete-period spectral energy.  It does not provide
the short physical-window discrepancy bound needed for Legendre.
"""

from __future__ import annotations

from fractions import Fraction
from math import exp, log, prod

from .legendre import primes_up_to


def _require_prime_tuple(primes: tuple[int, ...]) -> tuple[int, ...]:
    normalized = tuple(sorted(int(p) for p in primes))
    if len(set(normalized)) != len(normalized):
        raise ValueError("primes must be distinct")
    for prime in normalized:
        if prime < 3 or prime % 2 == 0:
            raise ValueError("primes must be odd")
        divisor = 3
        while divisor * divisor <= prime:
            if prime % divisor == 0:
                raise ValueError("entries must be prime")
            divisor += 2
    return normalized


def physical_transverse_primes(k: int) -> tuple[int, ...]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    M = k * (k + 1)
    return tuple(p for p in primes_up_to(k) if p % 2 == 1 and M % p != 0)


def conductor_energy(conductor: int, primes: tuple[int, ...]) -> Fraction:
    """Return E(q)=2^omega(q)/q for a squarefree conductor supported on primes."""
    normalized = _require_prime_tuple(primes)
    if isinstance(conductor, bool) or not isinstance(conductor, int) or conductor < 1:
        raise ValueError("conductor must be a positive integer")
    remaining = conductor
    omega = 0
    for prime in normalized:
        if remaining % prime == 0:
            remaining //= prime
            omega += 1
            if remaining % prime == 0:
                raise ValueError("conductor must be squarefree")
    if remaining != 1:
        raise ValueError("conductor uses a prime outside the declared family")
    return Fraction(2**omega, conductor)


def conductor_energy_partition(primes: tuple[int, ...]) -> dict[str, object]:
    """Enumerate the exact energy partition for a bounded declared prime family."""
    normalized = _require_prime_tuple(primes)
    rows: list[tuple[int, Fraction]] = [(1, Fraction(1, 1))]
    for prime in normalized:
        rows += [(q * prime, energy * Fraction(2, prime)) for q, energy in tuple(rows)]
    rows.sort()
    direct_total = sum((energy for _q, energy in rows), start=Fraction(0, 1))
    product_total = prod((Fraction(prime + 2, prime) for prime in normalized), start=Fraction(1, 1))
    if direct_total != product_total:
        raise AssertionError("conductor energy partition failed Euler product")
    probability_rows = tuple((q, energy / direct_total) for q, energy in rows)
    if sum((prob for _q, prob in probability_rows), start=Fraction(0, 1)) != 1:
        raise AssertionError("normalized conductor energy is not a probability measure")
    return {
        "primes": normalized,
        "energy_rows": tuple(rows),
        "total_second_moment": direct_total,
        "product_second_moment": product_total,
        "normalized_energy_rows": probability_rows,
    }


def conductor_prime_inclusion_probabilities(primes: tuple[int, ...]) -> tuple[tuple[int, Fraction], ...]:
    """Return the independent Bernoulli probabilities 2/(p+2)."""
    normalized = _require_prime_tuple(primes)
    return tuple((prime, Fraction(2, prime + 2)) for prime in normalized)


def log_conductor_moments(k: int) -> dict[str, float | int]:
    """Return the exact finite Bernoulli formulas for mean/variance of log Q."""
    primes = physical_transverse_primes(k)
    mean = 0.0
    variance = 0.0
    log_second_moment = 0.0
    for prime in primes:
        probability = 2.0 / (prime + 2.0)
        lp = log(prime)
        mean += probability * lp
        variance += probability * (1.0 - probability) * lp * lp
        log_second_moment += log(1.0 + 2.0 / prime)
    lk = log(k)
    return {
        "k": k,
        "transverse_prime_count": len(primes),
        "mean_log_conductor": mean,
        "variance_log_conductor": variance,
        "std_log_conductor": variance**0.5,
        "mean_log_conductor_over_log_k": mean / lk,
        "variance_log_conductor_over_log_k_squared": variance / (lk * lk),
        "geometric_mean_conductor": exp(mean),
        "log_total_second_moment": log_second_moment,
    }


def normalized_log_conductor_mgf(k: int, s: float) -> float:
    """Return the finite energy-law MGF E exp(s log Q/log k)."""
    primes = physical_transverse_primes(k)
    lk = log(k)
    log_mgf = 0.0
    for prime in primes:
        probability = 2.0 / (prime + 2.0)
        u = log(prime) / lk
        log_mgf += log(1.0 + probability * (exp(float(s) * u) - 1.0))
    return exp(log_mgf)


def generalized_dickman_two_log_mgf(s: float, steps: int = 20000) -> float:
    """Numerically integrate the limiting log-MGF 2 int_0^1 (e^(su)-1)/u du."""
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 100:
        raise ValueError("steps must be an integer >=100")
    s = float(s)
    # Midpoint rule avoids the removable singularity at u=0.
    total = 0.0
    width = 1.0 / steps
    for index in range(steps):
        u = (index + 0.5) * width
        total += (exp(s * u) - 1.0) / u
    return 2.0 * total * width
