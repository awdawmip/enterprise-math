"""Anchored reduced-residue formulation of the surviving P017/P018 carry phase.

The channel-sieve boundary shows that the full descendant Mobius block is an
exact rough-number count.  This module removes one more coordinate artifact.

Let K=k-1 and let W_K be the product of the odd primes p<=K.  At parent E=1,
the quotient channel is the ordered odd candidate set

    y_t = y_0 - 2t,             0 <= t < N.

Because W_K is odd, multiplication by 2^(-1) modulo W_K converts this step-two
progression into an ordinary interval of consecutive residue classes.  Put

    a_K = y_0 * 2^(-1) (mod W_K).

Then

    gcd(y_0-2t,W_K)=1  iff  gcd(a_K-t,W_K)=1,

and therefore

    pi((k+1)^2)-pi(k^2)
      = #{0<=t<N : gcd(a_K-t,W_K)=1}.

Thus Legendre positivity is exactly an **anchored Jacobsthal-type avoidance
problem**: the particular backward interval

    a_K, a_K-1, ..., a_K-(N-1)     (mod W_K)

must contain a reduced residue.

This distinction matters.  A worst-phase Jacobsthal/wheel-gap estimate treats
the anchor as arbitrary.  Classical Erdos--Rankin/Ford--Green--Konyagin--Tao
covering constructions show that primorial wheels admit very long phases with
no reduced residue, eventually much longer than the O(K) window relevant here.
Hence a uniform-in-anchor wheel-gap theorem cannot be the missing Legendre
mechanism.  Any surviving phase argument must prove that the **square-generated
anchor a_K avoids the exceptional long wheel gaps**.

The exact reduction here is elementary and project-local.  The existence of
superlinear generic primorial gaps is external prior art and is not reproved by
this module.
"""

from __future__ import annotations

from math import gcd

from .legendre import primes_up_to
from .p017_p018_carry_channel_sieve_boundary import channel_rough_count
from .p017_p018_carry_refinement_channel import signed_fiber_channel_state


def odd_prime_wheel(limit: int) -> int:
    """Return the odd primorial product over primes p<=limit."""
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("limit must be a nonnegative integer")
    wheel = 1
    for prime in primes_up_to(limit):
        if prime != 2:
            wheel *= prime
    return wheel


def unit_step_anchor(first_quotient: int, wheel: int) -> int:
    """Convert y-2t modulo an odd wheel to the consecutive residues a-t."""
    if isinstance(first_quotient, bool) or not isinstance(first_quotient, int):
        raise ValueError("first_quotient must be an integer")
    if first_quotient % 2 == 0:
        raise ValueError("first_quotient must be odd")
    if isinstance(wheel, bool) or not isinstance(wheel, int) or wheel < 1 or wheel % 2 == 0:
        raise ValueError("wheel must be a positive odd integer")
    if wheel == 1:
        return 0
    return (first_quotient * pow(2, -1, wheel)) % wheel


def anchored_unit_step_rough_count(fiber_size: int, first_quotient: int, wheel: int) -> dict[str, object]:
    """Verify the exact step-two -> unit-step reduced-residue coordinate change."""
    if isinstance(fiber_size, bool) or not isinstance(fiber_size, int) or fiber_size < 0:
        raise ValueError("fiber_size must be a nonnegative integer")
    anchor = unit_step_anchor(first_quotient, wheel)
    transformed = sum(gcd(anchor - offset, wheel) == 1 for offset in range(fiber_size))
    direct = channel_rough_count(fiber_size, first_quotient, wheel)
    if transformed != direct:
        raise AssertionError("unit-step anchor lost channel roughness")
    first_survivor = next(
        (offset for offset in range(fiber_size) if gcd(anchor - offset, wheel) == 1),
        None,
    )
    return {
        "fiber_size": fiber_size,
        "first_quotient": first_quotient,
        "wheel": wheel,
        "unit_step_anchor": anchor,
        "rough_count": transformed,
        "first_survivor_offset": first_survivor,
        "empty_anchored_window": first_survivor is None,
        "unit_step_equivalence": True,
    }


def square_boundary_anchored_wheel_state(k: int) -> dict[str, object]:
    """Return the exact odd-primorial anchored interval for one square boundary."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    K = k - 1
    parent = signed_fiber_channel_state(K, 1)
    fiber_size = int(parent["fiber_size"])
    first_quotient = parent["first_quotient"]
    if first_quotient is None:
        raise AssertionError("E=1 square-boundary channel cannot be empty for k>=3")
    wheel = odd_prime_wheel(K)
    anchored = anchored_unit_step_rough_count(fiber_size, int(first_quotient), wheel)

    # The E=1 channel lists every odd integer in the open square interval,
    # except that for odd k the top odd endpoint k(k+2) is intentionally outside
    # the centered signed window; it is composite and cannot affect prime count.
    expected_size = k if k % 2 == 0 else k - 1
    if fiber_size != expected_size:
        raise AssertionError("unexpected E=1 square-boundary channel length")

    return {
        "k": k,
        "K": K,
        "odd_prime_wheel": wheel,
        "parent_channel": parent,
        **anchored,
        "candidate_count": fiber_size,
        "square_anchor_requires_phase_specific_avoidance": True,
    }
