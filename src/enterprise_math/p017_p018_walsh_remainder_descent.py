"""Exact Euclidean remainder descent of selected-modulus orientation-Walsh terms.

For an odd squarefree modulus m coprime to the pronic center M=k(k+1), define

the signed local root function

    f_(m,k)(x)
      = product_(p|m)
          [1_(x=M mod p)-1_(x=-M mod p)].

Let the symmetric tent selected-modulus contribution be

    B_m(k)
      = sum_(|x|<k) (1-|x|/k) f_(m,k)(x).

The root function is periodic modulo m and has zero mean for every m>1.  Put

    r = k mod m.

Since M=k(k+1)=r(r+1) mod m, the local root phases at scale k and r are the
same modulo m.  Complete m-periods of the triangular/tent Fourier kernel vanish
at all primitive root-Walsh frequencies, giving the exact Euclidean descent

    B_m(k) = (r/k) B_m(r),

with the right side interpreted as zero when r=0.  Equivalently

    k*B_m(k)

is a periodic boundary observable depending only on k mod m.

Thus every nontrivial selected-modulus correction has no reusable full-period
bulk.  In particular, if m<=k, its large-scale contribution immediately reduces
to the boundary regime r<m.  This is the signed analogue of the primitive-energy
scale descent in p017_p018_biprimitive_boundary_energy.py.

The theorem is an exact representation/descent law; it does not bound the sum
over many moduli or prove a prime-gap statement.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd


def _prime_factors_squarefree_odd(m: int) -> tuple[int, ...]:
    if isinstance(m, bool) or not isinstance(m, int) or m <= 1 or m % 2 == 0:
        raise ValueError("m must be an odd integer >1")
    remaining = m
    factors: list[int] = []
    p = 3
    while p * p <= remaining:
        if remaining % p == 0:
            remaining //= p
            factors.append(p)
            if remaining % p == 0:
                raise ValueError("m must be squarefree")
        p += 2
    if remaining > 1:
        factors.append(remaining)
    product = 1
    for p in factors:
        product *= p
    if product != m:
        raise AssertionError("squarefree factorization failed")
    return tuple(factors)


def signed_root_value(x: int, center: int, m: int) -> int:
    """Return the selected-root Walsh sign in {-1,0,1}."""
    factors = _prime_factors_squarefree_odd(m)
    if gcd(center, m) != 1:
        raise ValueError("selected modulus must be transverse to the center")
    sign = 1
    for p in factors:
        if (x - center) % p == 0:
            continue
        if (x + center) % p == 0:
            sign = -sign
            continue
        return 0
    return sign


def selected_modulus_tent_contribution(k: int, m: int) -> Fraction:
    """Return B_m(k) exactly as a rational finite tent sum."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be positive")
    _prime_factors_squarefree_odd(m)
    center = k * (k + 1)
    if gcd(center, m) != 1:
        raise ValueError("m must be transverse to k(k+1)")
    total = Fraction(0, 1)
    for x in range(-k + 1, k):
        sign = signed_root_value(x, center, m)
        if sign:
            total += sign * Fraction(k - abs(x), k)
    return total


def selected_modulus_remainder_descent(k: int, m: int) -> dict[str, object]:
    """Verify B_m(k)=(r/k)B_m(r), r=k mod m."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be positive")
    _prime_factors_squarefree_odd(m)
    center = k * (k + 1)
    if gcd(center, m) != 1:
        raise ValueError("m must be transverse to k(k+1)")
    r = k % m
    large = selected_modulus_tent_contribution(k, m)
    if r == 0:
        local = Fraction(0, 1)
        reconstructed = Fraction(0, 1)
    else:
        # Transversality descends because k(k+1)=r(r+1) mod m.
        if gcd(r * (r + 1), m) != 1:
            raise AssertionError("pronic transversality failed remainder descent")
        local = selected_modulus_tent_contribution(r, m)
        reconstructed = Fraction(r, k) * local
    if large != reconstructed:
        raise AssertionError("selected-modulus Walsh term failed Euclidean remainder descent")
    return {
        "k": k,
        "m": m,
        "remainder_r": r,
        "selected_contribution_at_k": large,
        "selected_contribution_at_remainder_scale": local,
        "reconstructed_from_remainder_scale": reconstructed,
        "scaled_boundary_numerator": k * large,
        "selected_modulus_remainder_descent_exact": True,
    }
