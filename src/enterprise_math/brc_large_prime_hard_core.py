"""Exact degree-one large-prime hard-core identities for BRC carry research.

For every odd prime p,

    c_p(n) = floor(2n/p) - 2 floor(n/p)
           = 1[(n mod p) >= (p+1)/2],

and the time increment is

    c_p(n+1)-c_p(n) = 1[p | (2n+1)] - 1[p | (n+1)].

When the BRC hard layer retains primes p>y pointwise only after they enter the
population (p<=n), the uncentered selected-prime valuation therefore has an
exact increment compiled from the rough prime radicals of 2n+1 and n+1,
with endpoint-prime corrections.  The centered observer adds the separate
new-prime term ``-gamma_c log(n+1)`` when n+1 itself is a retained prime.

This module is finite exact arithmetic.  It does not estimate prime
correlations and does not prove RH.
"""
from __future__ import annotations

from dataclasses import dataclass

from .brc_count_centered_carry import (
    PrimeValuations,
    _require_positive_int,
    carry_bit,
    factor_positive_integer,
    primes_up_to,
)


def is_prime(value: int) -> bool:
    n = _require_positive_int("value", value)
    return len(factor_positive_integer(n)) == 1 and factor_positive_integer(n)[0][1] == 1


def odd_prime_carry_by_residue(n: int, prime: int) -> int:
    """Exact half-residue form of the doubling carry for an odd prime."""
    n = _require_positive_int("n", n)
    p = _require_positive_int("prime", prime)
    if p == 2 or not is_prime(p):
        raise ValueError("prime must be an odd prime")
    return int(n % p >= (p + 1) // 2)


def odd_prime_carry_time_increment(n: int, prime: int) -> int:
    """Return c_p(n+1)-c_p(n) in its exact divisibility form."""
    n = _require_positive_int("n", n)
    p = _require_positive_int("prime", prime)
    if p == 2 or not is_prime(p):
        raise ValueError("prime must be an odd prime")
    return int((2 * n + 1) % p == 0) - int((n + 1) % p == 0)


def rough_prime_radical_valuations(value: int, cutoff: int) -> PrimeValuations:
    """Formal log of the radical of prime divisors strictly above cutoff."""
    n = _require_positive_int("value", value)
    y = _require_positive_int("cutoff", cutoff)
    return tuple((p, 1) for p, _exponent in factor_positive_integer(n) if p > y)


def endpoint_prime_valuations(value: int, cutoff: int) -> PrimeValuations:
    """Formal log of value iff it is itself a prime strictly above cutoff."""
    n = _require_positive_int("value", value)
    y = _require_positive_int("cutoff", cutoff)
    factors = factor_positive_integer(n)
    if len(factors) == 1 and factors[0] == (n, 1) and n > y:
        return ((n, 1),)
    return ()


def _signed_add(target: dict[int, int], values: PrimeValuations, sign: int) -> None:
    for prime, exponent in values:
        target[prime] = target.get(prime, 0) + sign * exponent
        if target[prime] == 0:
            del target[prime]


def selected_large_prime_valuations(n: int, cutoff: int) -> PrimeValuations:
    """Valuations of product of selected ordinary primes cutoff<p<=n."""
    n = _require_positive_int("n", n)
    y = _require_positive_int("cutoff", cutoff)
    return tuple((p, 1) for p in primes_up_to(n) if p > y and carry_bit(n, p))


@dataclass(frozen=True)
class LargePrimeIncrementCertificate:
    """Exact increment of the uncentered selected large-prime valuation state."""

    n: int
    cutoff: int
    direct_increment: PrimeValuations
    rough_increment: PrimeValuations
    new_prime: PrimeValuations

    @property
    def rough_degree_one_on_two_n_plus_one(self) -> bool:
        return self.cutoff * self.cutoff > 2 * self.n + 1

    def verify(self) -> bool:
        return self.direct_increment == self.rough_increment


def large_prime_increment_certificate(n: int, cutoff: int) -> LargePrimeIncrementCertificate:
    """Compile and verify the exact hard-layer time increment.

    If ``V_y(n)=sum_{y<p<=n} c_p(n) e_p`` in formal prime-valuation
    coordinates, then

        V_y(n+1)-V_y(n)
          = rad_y(2n+1)-P_y(2n+1)-rad_y(n+1)+P_y(n+1),

    where ``rad_y`` keeps distinct prime divisors above y and ``P_y(m)`` is
    the endpoint prime m itself when m is a retained prime.  The centered
    log observer additionally changes by ``-gamma_c log(n+1)`` exactly when
    ``new_prime`` is nonempty.
    """
    n = _require_positive_int("n", n)
    y = _require_positive_int("cutoff", cutoff)

    before = dict(selected_large_prime_valuations(n, y))
    after = dict(selected_large_prime_valuations(n + 1, y))
    direct = {
        p: after.get(p, 0) - before.get(p, 0)
        for p in set(before) | set(after)
    }
    direct_tuple = tuple(sorted((p, e) for p, e in direct.items() if e))

    compiled: dict[int, int] = {}
    _signed_add(compiled, rough_prime_radical_valuations(2 * n + 1, y), +1)
    _signed_add(compiled, endpoint_prime_valuations(2 * n + 1, y), -1)
    _signed_add(compiled, rough_prime_radical_valuations(n + 1, y), -1)
    new_prime = endpoint_prime_valuations(n + 1, y)
    _signed_add(compiled, new_prime, +1)
    rough_tuple = tuple(sorted((p, e) for p, e in compiled.items() if e))

    state = LargePrimeIncrementCertificate(
        n=n,
        cutoff=y,
        direct_increment=direct_tuple,
        rough_increment=rough_tuple,
        new_prime=new_prime,
    )
    if not state.verify():
        raise AssertionError("large-prime hard-core increment verification failed")
    return state
