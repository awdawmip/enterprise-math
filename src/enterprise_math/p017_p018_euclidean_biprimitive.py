"""Self-dual bi-primitive conductor blocks for the Euclidean tent channel.

For coprime positive n,d, both coprime to the center M, define the symmetric
tent channel

    C(n,d)=sum_{|r|<k,\ n|M+r,\ d|M-r} W(r/k),
    W(u)=(1-|u|)_+.

The substitution r->-r proves the exact physical self-duality

    C(n,d)=C(d,n).

Applying divisor-conductor Möbius extraction on both axes defines

    B(n,d)
      = 1/(n d) * sum_(q|n,e|d)
          mu(n/q) mu(d/e) q e C(q,e).

Then

    C(n,d)=sum_(q|n,e|d) (q e)/(n d) B(q,e),
    B(n,d)=B(d,n).

Fourier interpretation.
-----------------------
Let m=n*d.  The two congruences determine one signed radius residue rho modulo
m.  The periodized tent has Fourier expansion

    C(n,d)=k/m * sum_(h in Z) W_hat(h*k/m) e(h*rho/m).

The double Möbius extraction keeps exactly frequencies with gcd(h,m)=1, so
B(n,d) is the primitive-frequency block on the full cross modulus m.

This gives a uniform all-scale block bound without any Kloosterman theorem.

* If 1<m<=k, the primitive block has no zero frequency and the sinc^2 tail gives

      |B(n,d)| <= m/(3k).

* If m>k, group primitive frequencies h=a+l*m by reduced residues a mod m.  The
  classical sinc^2 periodization identity gives the nonnegative coefficient

      k/m sum_l W_hat(k(a+l*m)/m)
        = 1/(k m) |sum_(j=0)^(k-1) e(a j/m)|^2.

  Summing only over reduced residues is bounded by summing over every a mod m.
  Since k<m, finite Fourier Parseval gives

      sum_(a mod m) |sum_(j=0)^(k-1)e(a j/m)|^2 = m k.

  Hence the primitive coefficient L1 mass is at most one, and

      |B(n,d)| <= 1.

Thus the bi-primitive conductor plane has deterministic low-product control and
uniform high-product control.  The remaining P017×P018 problem is not an
individual primitive-block estimate; it is to sum/repack these blocks across the
divisor lattice without losing the orientation-Walsh cancellation.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from .p017_p018_poisson_conductor_mobius import tent_smoothed_channel_count


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
        p += 1
    if remaining > 1:
        count += 1
    return -1 if count % 2 else 1


def symmetric_tent_channel(center: int, k: int, n: int, d: int) -> Fraction:
    """Return C(n,d) and verify agreement with the one-axis Euclidean channel."""
    if gcd(center, n) != 1 or gcd(center, d) != 1 or gcd(n, d) != 1:
        raise ValueError("symmetric channel requires pairwise coprimality with the center")
    # Direct signed-radius definition.
    total = Fraction(0, 1)
    for r in range(-k + 1, k):
        if (center + r) % n or (center - r) % d:
            continue
        total += Fraction(k - abs(r), k)

    one_axis = tent_smoothed_channel_count(center, k, n, d)
    if total != one_axis:
        raise AssertionError("signed-radius and Euclidean tent channels disagree")
    return total


def biprimitive_block(center: int, k: int, n: int, d: int) -> Fraction:
    """Return B(n,d) by exact double divisor Möbius extraction."""
    if gcd(center, n) != 1 or gcd(center, d) != 1 or gcd(n, d) != 1:
        raise ValueError("bi-primitive block requires pairwise coprimality with center")
    total = Fraction(0, 1)
    for q in _divisors(n):
        mu_q = _mobius(n // q)
        if mu_q == 0:
            continue
        for e in _divisors(d):
            mu_e = _mobius(d // e)
            if mu_e == 0:
                continue
            total += Fraction(mu_q * mu_e * q * e, n * d) * symmetric_tent_channel(
                center, k, q, e
            )
    return total


def biprimitive_reconstruction(center: int, k: int, n: int, d: int) -> dict[str, object]:
    """Verify C(n,d)=sum qe/(nd)B(q,e) and B(n,d)=B(d,n)."""
    if gcd(center, n) != 1 or gcd(center, d) != 1 or gcd(n, d) != 1:
        raise ValueError("reconstruction requires pairwise coprimality with center")
    direct = symmetric_tent_channel(center, k, n, d)
    reconstructed = Fraction(0, 1)
    rows: list[dict[str, object]] = []
    for q in _divisors(n):
        for e in _divisors(d):
            block = biprimitive_block(center, k, q, e)
            term = Fraction(q * e, n * d) * block
            reconstructed += term
            rows.append({"q": q, "e": e, "block": block, "weighted_term": term})
    if reconstructed != direct:
        raise AssertionError("double conductor reconstruction failed")
    block_nd = biprimitive_block(center, k, n, d)
    block_dn = biprimitive_block(center, k, d, n)
    if block_nd != block_dn:
        raise AssertionError("bi-primitive block lost n<->d self-duality")
    if symmetric_tent_channel(center, k, d, n) != direct:
        raise AssertionError("physical channel lost n<->d self-duality")
    return {
        "center": center,
        "k": k,
        "n": n,
        "d": d,
        "physical_channel": direct,
        "reconstructed_channel": reconstructed,
        "biprimitive_block": block_nd,
        "rows": tuple(rows),
        "physical_self_duality": True,
        "biprimitive_self_duality": True,
        "double_conductor_reconstruction": True,
    }


def biprimitive_absolute_ceiling(k: int, n: int, d: int) -> Fraction:
    """Return m/(3k) for 1<m<=k and 1 for m>k (m=n*d)."""
    if any(isinstance(v, bool) or not isinstance(v, int) or v < 1 for v in (k, n, d)):
        raise ValueError("k,n,d must be positive integers")
    m = n * d
    if m == 1:
        return Fraction(k, 1)
    if m <= k:
        return Fraction(m, 3 * k)
    return Fraction(1, 1)


def verify_biprimitive_ceiling(center: int, k: int, n: int, d: int) -> dict[str, object]:
    block = biprimitive_block(center, k, n, d)
    ceiling = biprimitive_absolute_ceiling(k, n, d)
    if abs(block) > ceiling:
        raise AssertionError("bi-primitive tent block exceeded its analytic ceiling")
    return {
        "center": center,
        "k": k,
        "n": n,
        "d": d,
        "cross_modulus": n * d,
        "biprimitive_block": block,
        "absolute_ceiling": ceiling,
        "ceiling_verified": True,
    }
