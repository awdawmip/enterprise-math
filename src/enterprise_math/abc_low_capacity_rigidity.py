"""Rigidity of integers with bounded normalized derivative capacity.

For

    C(n)=sum_{p|n} v_p(n) rad(n)/p,

fix an integer horizon H.  If C(n)<=H and n has at least two distinct prime
factors, then every support prime and every exponent is <=H.  Indeed, for a
support prime p choose another support prime q; the q-term

    v_q(n) rad(n)/q

is at least p.  Also every p-term is at least v_p(n).

Consequently all bounded-capacity non-prime-powers lie in a finite set and in
fact divide

    Q_H = product_{p<=H, p prime} p^H.

The only infinite bounded-capacity families are prime powers p^e with e<=H,
for which C(p^e)=e.  This is elementary arithmetic used to isolate the hard
unit-relation slice of PCC.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_small_derivative_block import normalized_block_capacity
from .abc_support import prime_factorization


@dataclass(frozen=True)
class LowCapacityClassification:
    n: int
    horizon: int
    capacity: int
    support_size: int
    prime_power: bool
    prime_power_base: int | None
    prime_power_exponent: int | None
    all_support_primes_bounded: bool
    all_exponents_bounded: bool


def _primes_up_to(H: int) -> tuple[int, ...]:
    result: list[int] = []
    for candidate in range(2, H + 1):
        prime = True
        divisor = 2
        while divisor * divisor <= candidate:
            if candidate % divisor == 0:
                prime = False
                break
            divisor += 1
        if prime:
            result.append(candidate)
    return tuple(result)


def low_capacity_finite_universe_bound(H: int) -> int:
    """Return ``Q_H=prod_{p<=H} p^H`` containing every non-prime-power C<=H case."""
    if isinstance(H, bool) or not isinstance(H, int) or H < 1:
        raise ValueError("H must be a positive integer")
    result = 1
    for prime in _primes_up_to(H):
        result *= prime**H
    return result


def classify_low_capacity_integer(n: int, H: int) -> LowCapacityClassification:
    """Classify an integer known/queried at derivative-capacity horizon H."""
    if isinstance(n, bool) or not isinstance(n, int) or n <= 1:
        raise ValueError("n must be an integer >1")
    if isinstance(H, bool) or not isinstance(H, int) or H < 1:
        raise ValueError("H must be a positive integer")
    factors = prime_factorization(n)
    capacity = normalized_block_capacity(n)
    support_size = len(factors)
    prime_power = support_size == 1
    base = factors[0][0] if prime_power else None
    exponent = factors[0][1] if prime_power else None
    primes_bounded = all(prime <= H for prime, _exp in factors)
    exponents_bounded = all(exp <= H for _prime, exp in factors)

    if capacity <= H:
        if prime_power:
            if exponent != capacity:
                raise AssertionError("prime-power capacity must equal its exponent")
            if exponent is None or exponent > H:
                raise AssertionError("bounded prime-power capacity lost exponent bound")
        else:
            if not primes_bounded:
                raise AssertionError("bounded non-prime-power capacity lost support-prime bound")
            if not exponents_bounded:
                raise AssertionError("bounded non-prime-power capacity lost exponent bound")
            universe = low_capacity_finite_universe_bound(H)
            if universe % n:
                raise AssertionError("bounded non-prime-power failed finite-universe divisibility")

    return LowCapacityClassification(
        n=n,
        horizon=H,
        capacity=capacity,
        support_size=support_size,
        prime_power=prime_power,
        prime_power_base=base,
        prime_power_exponent=exponent,
        all_support_primes_bounded=primes_bounded,
        all_exponents_bounded=exponents_bounded,
    )


def low_capacity_rigidity_holds(n: int, H: int) -> bool:
    """Verify the finite-universe / prime-power dichotomy when ``C(n)<=H``."""
    data = classify_low_capacity_integer(n, H)
    if data.capacity > H:
        return True
    if data.prime_power:
        return data.prime_power_exponent is not None and data.prime_power_exponent <= H
    universe = low_capacity_finite_universe_bound(H)
    return universe % n == 0
