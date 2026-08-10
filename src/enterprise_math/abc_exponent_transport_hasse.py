"""Hasse-cover sufficiency for the P025 exponent-pressure transport cocycle.

On the research domain n>=2:

* difference same-sign transport uses ordinary divisibility; its primitive roots
  are exactly prime exponents;
* sum same-sign transport allows only odd exponent quotients; its components are
  indexed by v_2(n), and its primitive roots are odd primes together with powers
  of two.

Every non-cover inheritance multiplier is the product of prime-ratio cover-edge
multipliers along any admissible Hasse path.  The product is path-independent
by the exact cocycle law from Supplement 84.  Thus long-range transition data
are redundant once the cover edges are known.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_exponent_pressure_inheritance import (
    exponent_pressure_inheritance_state,
)
from .abc_support import prime_factorization


@dataclass(frozen=True)
class ExponentTransportCover:
    lower_exponent: int
    upper_exponent: int
    prime_ratio: int


@dataclass(frozen=True)
class ExponentTransportPath:
    start_exponent: int
    end_exponent: int
    mode: str
    covers: tuple[ExponentTransportCover, ...]
    edge_multipliers: tuple[Fraction, ...]
    path_multiplier: Fraction
    direct_multiplier: Fraction
    path_independent_verified: bool


def _require_exponent(n: int) -> None:
    if isinstance(n, bool) or not isinstance(n, int) or n < 2:
        raise ValueError("exponent must be an integer >=2")


def _is_prime_integer(n: int) -> bool:
    if n < 2:
        return False
    return len(prime_factorization(n)) == 1 and prime_factorization(n)[0] == (n, 1)


def _is_power_of_two(n: int) -> bool:
    return n >= 2 and n & (n - 1) == 0


def same_sign_cover_predecessors(exponent: int, mode: str) -> tuple[ExponentTransportCover, ...]:
    """Return Hasse-cover predecessors inside the n>=2 same-sign transport graph."""
    _require_exponent(exponent)
    if mode not in {"difference", "sum"}:
        raise ValueError("mode must be 'sum' or 'difference'")
    result: list[ExponentTransportCover] = []
    for prime, _power in prime_factorization(exponent):
        if mode == "sum" and prime == 2:
            continue
        lower = exponent // prime
        if lower < 2:
            continue
        result.append(
            ExponentTransportCover(
                lower_exponent=lower,
                upper_exponent=exponent,
                prime_ratio=prime,
            )
        )
    return tuple(sorted(result, key=lambda item: (item.lower_exponent, item.prime_ratio)))


def primitive_same_sign_exponent(exponent: int, mode: str) -> bool:
    """Return whether exponent has no proper same-sign ancestor in the n>=2 domain."""
    _require_exponent(exponent)
    covers = same_sign_cover_predecessors(exponent, mode)
    primitive = len(covers) == 0
    if mode == "difference":
        expected = _is_prime_integer(exponent)
    elif mode == "sum":
        expected = _is_power_of_two(exponent) or (
            exponent % 2 == 1 and _is_prime_integer(exponent)
        )
    else:
        raise ValueError("mode must be 'sum' or 'difference'")
    if primitive != expected:
        raise AssertionError("primitive-root classification disagreed with Hasse covers")
    return primitive


def _prime_multiset(n: int) -> list[int]:
    result: list[int] = []
    for prime, exponent in prime_factorization(n):
        result.extend([prime] * exponent)
    return result


def exponent_transport_cover_path(
    q: int,
    p: int,
    start_exponent: int,
    end_exponent: int,
    mode: str,
    prime_order: tuple[int, ...] | None = None,
) -> ExponentTransportPath:
    """Compose one admissible prime-ratio Hasse path and verify the direct multiplier."""
    _require_exponent(start_exponent)
    _require_exponent(end_exponent)
    if end_exponent <= start_exponent or end_exponent % start_exponent:
        raise ValueError("require start<end and start|end")
    ratio = end_exponent // start_exponent
    factors = _prime_multiset(ratio)
    if mode == "sum" and any(prime == 2 for prime in factors):
        raise ValueError("same-sign sum path cannot contain an even quotient edge")
    if mode not in {"difference", "sum"}:
        raise ValueError("mode must be 'sum' or 'difference'")

    order = list(prime_order) if prime_order is not None else sorted(factors)
    if sorted(order) != sorted(factors):
        raise ValueError("prime_order must be exactly the prime-factor multiset of end/start")

    current = start_exponent
    covers: list[ExponentTransportCover] = []
    multipliers: list[Fraction] = []
    for prime in order:
        nxt = current * prime
        edge = exponent_pressure_inheritance_state(q, p, current, nxt, mode)
        covers.append(ExponentTransportCover(current, nxt, prime))
        multipliers.append(edge.inheritance_multiplier)
        current = nxt
    if current != end_exponent:
        raise AssertionError("cover path did not reach target exponent")

    path_multiplier = Fraction(1, 1)
    for multiplier in multipliers:
        path_multiplier *= multiplier
    direct = exponent_pressure_inheritance_state(
        q, p, start_exponent, end_exponent, mode
    ).inheritance_multiplier
    if path_multiplier != direct:
        raise AssertionError("cover-edge product disagreed with direct transport")

    return ExponentTransportPath(
        start_exponent=start_exponent,
        end_exponent=end_exponent,
        mode=mode,
        covers=tuple(covers),
        edge_multipliers=tuple(multipliers),
        path_multiplier=path_multiplier,
        direct_multiplier=direct,
        path_independent_verified=True,
    )


def exponent_transport_diamond_holds(
    q: int,
    p: int,
    base_exponent: int,
    first_prime: int,
    second_prime: int,
    mode: str,
) -> bool:
    """Verify the local commuting-prime diamond for two distinct cover primes."""
    _require_exponent(base_exponent)
    if first_prime == second_prime or not _is_prime_integer(first_prime) or not _is_prime_integer(second_prime):
        raise ValueError("first_prime and second_prime must be distinct primes")
    if mode == "sum" and (first_prime == 2 or second_prime == 2):
        raise ValueError("same-sign sum diamonds use odd prime ratios only")

    end = base_exponent * first_prime * second_prime
    path_one = exponent_transport_cover_path(
        q,
        p,
        base_exponent,
        end,
        mode,
        (first_prime, second_prime),
    )
    path_two = exponent_transport_cover_path(
        q,
        p,
        base_exponent,
        end,
        mode,
        (second_prime, first_prime),
    )
    if path_one.path_multiplier != path_two.path_multiplier:
        raise AssertionError("exponent transport Hasse diamond failed to commute")
    return True
