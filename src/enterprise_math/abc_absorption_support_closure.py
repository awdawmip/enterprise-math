"""Second-order prime-support closure for the P025 absorption floor.

The closed cross-support formula

    eta_min = gcd R*e_p*e_q/(g*p*q)

shows that every prime label appearing in ``eta_min`` is already present either
in the radical support of ``abc`` or in the prime support of one valuation
exponent ``e_p=v_p(abc)``.  No third-order prime label is needed for this
certificate language.

This is an elementary corollary of the closed formula, not a claim that
factor-of-valuation data are generally new arithmetic objects.
"""

from __future__ import annotations

from .abc_absorption_formula import minimum_absorption_redundancy_support_formula
from .abc_support import abc_support_state, prime_factorization


def first_order_prime_support(a: int, b: int, c: int) -> tuple[int, ...]:
    """Return the prime support of ``abc`` for a primitive abc triple."""
    data = abc_support_state(a, b, c)
    primes = sorted({p for support in data["supports"] for p in support})
    return tuple(primes)


def valuation_exponent_prime_support(a: int, b: int, c: int) -> tuple[int, ...]:
    """Return primes dividing at least one valuation exponent ``v_p(abc)``."""
    abc_support_state(a, b, c)  # validation
    primes: set[int] = set()
    for n in (a, b, c):
        for _p, exponent in prime_factorization(n):
            for ell, _multiplicity in prime_factorization(exponent):
                primes.add(ell)
    return tuple(sorted(primes))


def second_order_absorption_candidate_support(
    a: int, b: int, c: int
) -> tuple[int, ...]:
    """Return first-order support union valuation-exponent prime support."""
    return tuple(
        sorted(
            set(first_order_prime_support(a, b, c))
            | set(valuation_exponent_prime_support(a, b, c))
        )
    )


def absorption_floor_prime_support(a: int, b: int, c: int) -> tuple[int, ...]:
    """Return the ordinary prime support of the exact absorption floor."""
    eta = minimum_absorption_redundancy_support_formula(a, b, c)
    return tuple(p for p, _exponent in prime_factorization(eta))


def absorption_support_closes_at_second_order(
    a: int, b: int, c: int
) -> bool:
    """Verify the exact support containment for ``eta_min``.

    ``supp(eta_min)`` is contained in

        supp(rad(abc)) union union_p supp(v_p(abc)).

    This follows directly because every normalized cross minor has numerator
    ``R*e_p*e_q``; dividing by the integer denominator cannot introduce a new
    prime factor, and a gcd cannot introduce one either.
    """
    floor_support = set(absorption_floor_prime_support(a, b, c))
    candidate = set(second_order_absorption_candidate_support(a, b, c))
    if not floor_support <= candidate:
        raise AssertionError("absorption floor introduced a third-order prime label")
    return True


def exponent_only_obstruction_example() -> dict[str, object]:
    """Return the clean ``1+242=243`` second-order necessity example."""
    triple = (1, 242, 243)
    first = first_order_prime_support(*triple)
    second = valuation_exponent_prime_support(*triple)
    floor = absorption_floor_prime_support(*triple)
    if first != (2, 3, 11) or 5 not in second or floor != (5,):
        raise AssertionError("second-order support example changed")
    return {
        "triple": triple,
        "first_order_support": first,
        "valuation_exponent_support": second,
        "absorption_floor_support": floor,
        "new_label_beyond_radical": 5,
    }
