"""Generation 3: exact Matomaki--Radziwill terminal-tail specialization.

This module records a finite identity suggested by Theorem 2 of Matomaki and
Radziwill (Ann. of Math. 2016).  It does NOT extend their theorem to h=2 and
does NOT prove the analytic error bound requested below.

Put y=floor(k/2) and define the completely multiplicative function

    f_k(n) = lambda(n) * 1_{gcd(n,P_y)=1}.

For k>=9, every y-rough integer in [k,2k] is prime, hence

    f_k(n) = -1_P(n)  on [k,2k].

In the product shell k^2 <= n1*n2 <= k^2+2k with k<=n1<=2k, a non-zero product
f_k(n1)f_k(n2) therefore comes from prime-prime factors.  Apart from the lower
square endpoint k^2 and a possible doubled orientation of k(k+2), this is
exactly the Generation-1 half-cutoff terminal semiprime geometry.

The 2016 theorem handles product intervals of length h*sqrt(x) for h>=10.  The
consecutive-square shell x=k^2 has normalized width h=2.  A special-function
endpoint theorem at h=2 with normalized error O(1/log^2 k) would imply the
expected O(k/log^2 k) bound for the central terminal pair count.  No such
endpoint theorem is claimed here.
"""

from __future__ import annotations

from math import gcd, isqrt

from .legendre import is_prime, primes_up_to
from .p017_p018_buchstab_cutoff_ladder import rough_survivor_offsets, square_interval_upper


def _liouville(value: int) -> int:
    if value < 1:
        raise ValueError("value must be positive")
    remaining = value
    omega = 0
    for p in primes_up_to(isqrt(value) + 1):
        while remaining % p == 0:
            omega += 1
            remaining //= p
        if remaining == 1:
            break
        if p * p > remaining:
            break
    if remaining > 1:
        omega += 1
    return -1 if omega % 2 else 1


def half_rough_liouville(k: int, value: int) -> int:
    """Return lambda(value) on the floor(k/2)-rough support and 0 otherwise."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be a positive integer")
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    cutoff = k // 2
    wheel = 1
    for p in primes_up_to(cutoff):
        wheel *= p
    if gcd(value, wheel) != 1:
        return 0
    return _liouville(value)


def mr_h2_half_rough_bilinear_sum(k: int) -> dict[str, object]:
    """Evaluate the exact h=2 finite bilinear sum for f_k.

    The sum is

        sum_{k^2 <= n1*n2 <= k^2+2k, k<=n1<=2k} f_k(n1)f_k(n2).

    Matomaki--Radziwill Theorem 2 is NOT asserted at h=2; this is only the
    arithmetic specialization of its left-hand geometry.
    """
    if isinstance(k, bool) or not isinstance(k, int) or k < 9:
        raise ValueError("require integer k>=9")

    upper = square_interval_upper(k)
    pair_rows: list[tuple[int, int, int]] = []
    total = 0
    for n1 in range(k, 2 * k + 1):
        f1 = half_rough_liouville(k, n1)
        if f1 == 0:
            continue
        n2_min = (k * k + n1 - 1) // n1
        n2_max = upper // n1
        for n2 in range(n2_min, n2_max + 1):
            product = n1 * n2
            if not k * k <= product <= upper:
                raise AssertionError("h=2 bilinear fiber left the declared shell")
            f2 = half_rough_liouville(k, n2)
            weight = f1 * f2
            if weight == 0:
                continue
            if not (is_prime(n1) and is_prime(n2)):
                raise AssertionError("nonzero half-rough h=2 pair failed prime-prime reduction")
            if weight != 1:
                raise AssertionError("prime-prime pair should have positive Liouville product")
            total += weight
            pair_rows.append((n1, n2, product))

    # Terminal semiprime states after sieving only through floor(k/2).
    cutoff = k // 2
    central_states: list[tuple[int, int, int]] = []
    far_boundary_states: list[tuple[int, int, int]] = []
    for offset in rough_survivor_offsets(k, cutoff):
        value = k * k + offset
        if is_prime(value):
            continue
        p = next((p for p in primes_up_to(k) if p > cutoff and value % p == 0), None)
        if p is None:
            raise AssertionError("half-rough composite lost its prime factor above k/2")
        q = value // p
        if not is_prime(q):
            raise AssertionError("half-rough composite failed terminal semiprime classification")
        if q <= 2 * k:
            central_states.append((p, q, value))
        else:
            if q not in (2 * k + 1, 2 * k + 3):
                raise AssertionError("terminal q>2k escaped the two odd boundary candidates")
            far_boundary_states.append((p, q, value))

    lower_square_term = int(is_prime(k))
    twin_orientation_term = int(is_prime(k) and is_prime(k + 2))
    reconstructed = len(central_states) + lower_square_term + twin_orientation_term
    if total != reconstructed:
        raise AssertionError("h=2 MR specialization lost its terminal-pair boundary terms")
    if len(far_boundary_states) > 2:
        raise AssertionError("more than two q>2k terminal boundary states appeared")

    prime_interval_count = sum(1 for n in range(k, 2 * k + 1) if is_prime(n))
    long_f_sum = sum(half_rough_liouville(k, n) for n in range(k, 2 * k + 1))
    if long_f_sum != -prime_interval_count:
        raise AssertionError("half-rough Liouville failed to become minus prime indicator on [k,2k]")

    return {
        "k": k,
        "half_cutoff": cutoff,
        "h_normalized": 2,
        "bilinear_pair_rows": tuple(pair_rows),
        "bilinear_sum": total,
        "central_terminal_semiprime_rows": tuple(sorted(central_states)),
        "central_terminal_semiprime_count": len(central_states),
        "far_terminal_boundary_rows": tuple(sorted(far_boundary_states)),
        "far_terminal_boundary_count": len(far_boundary_states),
        "lower_square_prime_term": lower_square_term,
        "twin_double_orientation_term": twin_orientation_term,
        "prime_count_k_to_2k": prime_interval_count,
        "long_half_rough_liouville_sum": long_f_sum,
        "status": "MR_H2_TERMINAL_SPECIALIZATION_ONLY",
    }
