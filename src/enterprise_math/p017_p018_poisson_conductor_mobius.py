"""Physical-space Möbius inversion of Euclidean Poisson conductor layers.

Let C(n,d) be the exact tent-smoothed divisor-channel observable

    C(n,d)=sum_(j=r_(n,d) mod d) W((n*j-R_n(M))/k),

where W(u)=(1-|u|)_+ and gcd(M,n)=gcd(n,d)=1.

Poisson completion followed by frequency-conductor descent groups every Fourier
frequency h by

    q=n/gcd(h,n).

Let P(q,d) denote the *native primitive-frequency block* at conductor q, i.e. the
Poisson block with (h',q)=1.  Exact phase/scale descent gives

    C(n,d)=sum_(q|n) (q/n) P(q,d).

Hence the primitive blocks are recovered from physical positive channel
observables by ordinary divisor Möbius inversion:

    P(n,d)=(1/n) sum_(q|n) mu(n/q) q C(q,d).

Thus primitive Kloosterman precision is not an independent state family: it is
the Möbius repair left after all coarser divisor-conductor futures have been
subtracted.  The q=1 block is the only layer containing the zero frequency; all
q>1 primitive blocks are pure oscillation.

The executable functions below compute C and the Möbius-inverted P exactly as
rational numbers from the finite tent window.  The identification of P with the
primitive Fourier block is the analytic Poisson theorem recorded in
p017_p018_euclidean_poisson_conductor.py.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd


def _divisors(n: int) -> tuple[int, ...]:
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def _mobius(n: int) -> int:
    if n < 1:
        raise ValueError("Mobius argument must be positive")
    remaining = n
    count = 0
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            count += 1
            if remaining % p == 0:
                return 0
            while remaining % p == 0:
                remaining //= p
        p += 1
    if remaining > 1:
        count += 1
    return -1 if count % 2 else 1


def tent_smoothed_channel_count(center: int, k: int, n: int, d: int) -> Fraction:
    """Return the exact finite tent channel count C(n,d)."""
    if any(isinstance(v, bool) or not isinstance(v, int) or v < 1 for v in (center, k, n, d)):
        raise ValueError("center,k,n,d must be positive integers")
    if gcd(center, n) != 1:
        raise ValueError("channel requires gcd(center,n)=1")
    if gcd(n, d) != 1:
        raise ValueError("channel requires gcd(n,d)=1")

    Q, t = divmod(center, n)
    residue = (Q + 2 * t * pow(n, -1, d)) % d
    j_min = (-k + t) // n + 1
    j_max = (k - 1 + t) // n
    total = Fraction(0, 1)
    for j in range(j_min, j_max + 1):
        if j % d != residue:
            continue
        offset = abs(n * j - t)
        if offset >= k:
            raise AssertionError("tent channel enumerator included an exterior point")
        total += Fraction(k - offset, k)
    return total


def primitive_conductor_block(center: int, k: int, n: int, d: int) -> Fraction:
    """Recover P(n,d) by exact Möbius inversion of physical channel observables."""
    if gcd(center, n) != 1 or gcd(n, d) != 1:
        raise ValueError("primitive block requires center,n,d pairwise conditions")
    total = Fraction(0, 1)
    for q in _divisors(n):
        mu = _mobius(n // q)
        if mu == 0:
            continue
        total += Fraction(mu * q, n) * tent_smoothed_channel_count(center, k, q, d)
    return total


def conductor_mobius_reconstruction(center: int, k: int, n: int, d: int) -> dict[str, object]:
    """Verify C(n,d)=sum_(q|n)(q/n)P(q,d) exactly in physical space."""
    if gcd(center, n) != 1 or gcd(n, d) != 1:
        raise ValueError("reconstruction requires gcd(center,n)=gcd(n,d)=1")
    rows: list[dict[str, object]] = []
    reconstructed = Fraction(0, 1)
    for q in _divisors(n):
        primitive = primitive_conductor_block(center, k, q, d)
        term = Fraction(q, n) * primitive
        reconstructed += term
        rows.append({"q": q, "primitive_block": primitive, "weighted_term": term})
    direct = tent_smoothed_channel_count(center, k, n, d)
    if reconstructed != direct:
        raise AssertionError("conductor Möbius inversion failed to reconstruct the physical channel")
    return {
        "center": center,
        "k": k,
        "n": n,
        "d": d,
        "physical_channel_C_n_d": direct,
        "primitive_rows": tuple(rows),
        "reconstructed_channel": reconstructed,
        "conductor_mobius_identity": True,
    }
