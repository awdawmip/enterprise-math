"""Harmonic pairing on the forced Franel midpoint sector.

Let p be an odd prime, m=(p-1)/2, and put

    a_k = (-1)^k C(2k,k)^3 / 64^k                 (mod p).

The elementary congruence

    C(2k,k)/4^k = (-1)^k C(m,k)                   (mod p)

implies the exact midpoint symmetry

    a_(m-k)=a_k.

For

    f_k=H_k-H_(2k)

one also has

    f_k+f_(m-k)=H_m                                (mod p).

Indeed H_(p-1-2k)=H_(2k) modulo p, and

    H_m-H_(m-k)
      = sum_(i=0)^(k-1) 1/(m-i)
      = -2 sum_(i=0)^(k-1) 1/(2i+1)
      = H_k-2H_(2k)                                (mod p).

Therefore

    2 sum_k a_k f_k = H_m sum_k a_k               (mod p).

Moreover sum a_k equals the Franel midpoint F_m modulo p.  In the forced
midpoint sectors p=5,7 (mod 8), the classical midpoint criterion gives p|F_m,
so

    sum_k a_k (H_k-H_(2k)) = 0                     (mod p).

Writing

    U_p = sum a_k H_k,
    T_p = sum a_k (H_(2k)-H_k/2),

this is exactly

    U_p = 2 T_p                                    (mod p).

The forced-midpoint zero criterion is prior art.  The short symmetric pairing
and its use to identify the two harmonic companions are P022-local.
"""

from __future__ import annotations

from math import comb

from .p022_barlow_franel_half_index import half_index, half_index_is_forced_zero
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import triple_moment_factor


def _require_forced_prime(prime: int) -> int:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 3
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime greater than three")
    if not half_index_is_forced_zero(prime):
        raise ValueError("prime must lie in the forced-midpoint mod-8 sector")
    return half_index(prime)


def harmonic_mod(index: int, prime: int) -> int:
    """H_index modulo p, for 0<=index<p."""
    if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < prime:
        raise ValueError("index must lie in 0..p-1")
    return sum(pow(j, -1, prime) for j in range(1, index + 1)) % prime


def midpoint_central_term(prime: int, index: int) -> int:
    """a_k=(-1)^k C(2k,k)^3/64^k modulo p."""
    midpoint = _require_forced_prime(prime)
    if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index <= midpoint:
        raise ValueError("index must lie in 0..m")
    sign = prime - 1 if index % 2 else 1
    return (
        sign
        * pow(comb(2 * index, index), 3, prime)
        * pow(pow(64, index, prime), -1, prime)
    ) % prime


def midpoint_term_reflection(prime: int, index: int) -> tuple[int, int]:
    """Certify a_(m-k)=a_k modulo p."""
    midpoint = _require_forced_prime(prime)
    left = midpoint_central_term(prime, index)
    right = midpoint_central_term(prime, midpoint - index)
    if left != right:
        raise AssertionError("forced-midpoint central term reflection failed")
    return left, right


def harmonic_difference_pair(prime: int, index: int) -> tuple[int, int, int]:
    """Return (f_k,f_(m-k),H_m) and certify their pair sum."""
    midpoint = _require_forced_prime(prime)
    if not 0 <= index <= midpoint:
        raise ValueError("index must lie in 0..m")
    mirror = midpoint - index
    left = (harmonic_mod(index, prime) - harmonic_mod(2 * index, prime)) % prime
    right = (harmonic_mod(mirror, prime) - harmonic_mod(2 * mirror, prime)) % prime
    hm = harmonic_mod(midpoint, prime)
    if (left + right) % prime != hm:
        raise AssertionError("harmonic midpoint pair identity failed")
    return left, right, hm


def midpoint_central_sum(prime: int) -> int:
    """sum a_k modulo p; equals F_m modulo p."""
    midpoint = _require_forced_prime(prime)
    value = sum(midpoint_central_term(prime, k) for k in range(midpoint + 1)) % prime
    expected = triple_moment_factor(midpoint) % prime
    if value != expected or value != 0:
        raise AssertionError("forced midpoint central sum must reproduce the Franel zero")
    return value


def midpoint_harmonic_companions(prime: int) -> tuple[int, int, int]:
    """Return (U_p,T_p,pairing_sum) and certify U_p=2T_p modulo p."""
    midpoint = _require_forced_prime(prime)
    u = 0
    t = 0
    pairing = 0
    inv2 = pow(2, -1, prime)
    for k in range(midpoint + 1):
        term = midpoint_central_term(prime, k)
        hk = harmonic_mod(k, prime)
        h2k = harmonic_mod(2 * k, prime)
        u = (u + term * hk) % prime
        t = (t + term * (h2k - inv2 * hk)) % prime
        pairing = (pairing + term * (hk - h2k)) % prime

    midpoint_central_sum(prime)
    # Symmetrization gives 2*pairing=H_m*sum(a_k)=0.
    if pairing % prime != 0:
        raise AssertionError("forced-midpoint harmonic pairing must vanish")
    if u != 2 * t % prime:
        raise AssertionError("U_p and 2T_p must agree modulo p")
    return u, t, pairing
