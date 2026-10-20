"""Fourier and second-order structure of the P017 orientation-Walsh sieve.

The orientation-Walsh weight from p017_p018_orientation_walsh_sieve has a
factorized nonconstant spectrum.  This module records the exact finite formulas
that expose the analytic object still missing from the consecutive-square
argument.

For a nonempty squarefree transverse modulus d and sign vector epsilon_p in
{+1,-1}, let rho_epsilon mod d be the CRT root

    rho_epsilon = epsilon_p M (mod p),  p|d,

and give it Walsh weight prod epsilon_p.  Then for every integer h,

    sum_epsilon (prod epsilon_p) exp(2*pi*i*h*rho_epsilon/d)
      = product_(p|d)
          [exp(2*pi*i*h*M*inv(d/p,p)/p)
           -exp(-2*pi*i*h*M*inv(d/p,p)/p)]
      = (2i)^omega(d) product_(p|d)
          sin(2*pi*h*M*inv(d/p,p)/p).

In particular the h=0 constant frequency is exactly zero, the Fourier version
of the boundary-only / zero-floor-bulk theorem.

There is also an exact complete-period autocorrelation law for the one-sided
upper-prime Walsh weight.  At one transverse prime p define the local factor

    f_p(r)=1+1_{r=M mod p}-1_{r=-M mod p}.

Its mean over r mod p is 1 and its second moment is 1+2/p.  For a shift h,

    mean_r f_p(r)f_p(r+h)
      = 1+2/p  if h=0 mod p,
        1-1/p  if h=+/-2M mod p,
        1      otherwise.

Because distinct prime coordinates are CRT independent, complete-period means,
second moments and correlations multiply over p.  Thus the Walsh weight has an
explicit bilinear/collision structure rather than an unspecified sieve error.

These complete-period formulas do not control the distinguished length-k
physical window by themselves.  The remaining analytic target is precisely a
short-window bilinear/discrepancy estimate strong enough to transfer the
complete-period mean 1 to the P017 centered phase.  This is analogous in role,
not claimed identical in hypotheses, to the additional bilinear information
used by prime-detecting/asymptotic sieves to break the classical parity barrier.
"""

from __future__ import annotations

from cmath import exp, pi
from fractions import Fraction
from math import prod, sin

from .legendre import primes_up_to


def _require_transverse_primes(k: int, selected_primes: tuple[int, ...]) -> tuple[int, ...]:
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    normalized = tuple(sorted(int(p) for p in selected_primes))
    if not normalized or len(set(normalized)) != len(normalized):
        raise ValueError("selected_primes must be nonempty and distinct")
    M = k * (k + 1)
    for prime in normalized:
        if prime < 3 or prime > k or prime % 2 == 0 or M % prime == 0:
            raise ValueError("selected primes must be odd transverse primes <=k")
        divisor = 3
        while divisor * divisor <= prime:
            if prime % divisor == 0:
                raise ValueError("selected entries must be prime")
            divisor += 2
    return normalized


def _crt_root_from_signs(M: int, primes: tuple[int, ...], signs: tuple[int, ...]) -> int:
    modulus = prod(primes)
    root = 0
    for prime, sign in zip(primes, signs):
        cofactor = modulus // prime
        inverse = pow(cofactor, -1, prime)
        root += (sign * M) * cofactor * inverse
    return root % modulus


def signed_root_fourier(k: int, selected_primes: tuple[int, ...], frequency: int) -> dict[str, object]:
    """Check the exact CRT product factorization numerically at one frequency."""
    if isinstance(frequency, bool) or not isinstance(frequency, int):
        raise ValueError("frequency must be an integer")
    primes = _require_transverse_primes(k, selected_primes)
    M = k * (k + 1)
    modulus = prod(primes)

    direct = 0j
    # iterative sign enumeration without importing another combinatorics helper
    sign_vectors: list[tuple[int, ...]] = [()]
    for _prime in primes:
        sign_vectors = [prefix + (sign,) for prefix in sign_vectors for sign in (1, -1)]
    roots: list[dict[str, object]] = []
    for signs in sign_vectors:
        root = _crt_root_from_signs(M, primes, signs)
        weight = prod(signs)
        term = weight * exp(2j * pi * frequency * root / modulus)
        direct += term
        roots.append({"signs": signs, "root": root, "weight": weight})

    product_form = 1 + 0j
    sine_form = (2j) ** len(primes)
    for prime in primes:
        cofactor = modulus // prime
        inverse = pow(cofactor, -1, prime)
        angle = 2 * pi * frequency * M * inverse / prime
        product_form *= exp(1j * angle) - exp(-1j * angle)
        sine_form *= sin(angle)

    tolerance = 1e-8 * max(1.0, abs(direct), abs(product_form), abs(sine_form))
    if abs(direct - product_form) > tolerance or abs(direct - sine_form) > tolerance:
        raise AssertionError("orientation root Fourier product factorization failed")
    if frequency % modulus == 0 and abs(direct) > tolerance:
        raise AssertionError("nonempty orientation root cube retained a constant Fourier mode")

    return {
        "k": k,
        "selected_primes": primes,
        "modulus": modulus,
        "frequency": frequency,
        "direct_fourier_sum": direct,
        "product_fourier_sum": product_form,
        "sine_fourier_sum": sine_form,
        "constant_mode_zero": frequency % modulus != 0 or abs(direct) <= tolerance,
        "roots": tuple(roots),
    }


def walsh_local_correlation(k: int, prime: int, shift: int) -> Fraction:
    """Return the exact one-prime complete-period correlation at a shift."""
    if isinstance(shift, bool) or not isinstance(shift, int):
        raise ValueError("shift must be an integer")
    primes = _require_transverse_primes(k, (prime,))
    p = primes[0]
    M = k * (k + 1)
    residue = shift % p
    if residue == 0:
        return Fraction(p + 2, p)
    plus = (2 * M) % p
    minus = (-2 * M) % p
    if residue in (plus, minus):
        return Fraction(p - 1, p)
    return Fraction(1, 1)


def walsh_complete_period_moments(k: int, selected_primes: tuple[int, ...] | None = None) -> dict[str, object]:
    """Return exact mean and second moment without enumerating the CRT period."""
    if selected_primes is None:
        M = k * (k + 1)
        selected_primes = tuple(
            p for p in primes_up_to(k)
            if p % 2 == 1 and M % p != 0
        )
        if not selected_primes:
            return {
                "k": k,
                "selected_primes": (),
                "mean": Fraction(1, 1),
                "second_moment": Fraction(1, 1),
                "variance": Fraction(0, 1),
            }
    primes = _require_transverse_primes(k, selected_primes)
    second = prod((Fraction(p + 2, p) for p in primes), start=Fraction(1, 1))
    return {
        "k": k,
        "selected_primes": primes,
        "mean": Fraction(1, 1),
        "second_moment": second,
        "variance": second - 1,
    }


def walsh_complete_period_correlation(
    k: int,
    shift: int,
    selected_primes: tuple[int, ...] | None = None,
) -> dict[str, object]:
    """Multiply the exact local collision factors over a declared prime family."""
    if selected_primes is None:
        M = k * (k + 1)
        selected_primes = tuple(
            p for p in primes_up_to(k)
            if p % 2 == 1 and M % p != 0
        )
        if not selected_primes:
            return {"k": k, "shift": shift, "selected_primes": (), "correlation": Fraction(1, 1)}
    primes = _require_transverse_primes(k, selected_primes)
    rows = tuple((p, walsh_local_correlation(k, p, shift)) for p in primes)
    correlation = prod((value for _p, value in rows), start=Fraction(1, 1))
    return {
        "k": k,
        "shift": shift,
        "selected_primes": primes,
        "local_factors": rows,
        "correlation": correlation,
    }
