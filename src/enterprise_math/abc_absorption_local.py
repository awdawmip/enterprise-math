"""Prime-local obstruction coordinates for the P025 absorption floor.

The closed support formula writes ``eta_min`` as a gcd of positive cross-block
integers.  This module resolves that gcd prime by prime.  The resulting local
valuation spectrum is exact finite arithmetic and is useful for falsifying
naive global correlations with abc quality.
"""

from __future__ import annotations

from .abc_absorption_formula import (
    additive_relation_content,
    minimum_absorption_redundancy_support_formula,
)
from .abc_support import abc_support_state, prime_factorization


def _valuation(n: int, prime: int) -> int:
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 1:
        raise ValueError("prime must be a prime integer > 1")
    if prime_factorization(prime) != ((prime, 1),):
        raise ValueError("prime must be prime")
    exponent = 0
    while n % prime == 0:
        n //= prime
        exponent += 1
    return exponent


def local_absorption_valuation(a: int, b: int, c: int, ell: int) -> int:
    """Return ``v_ell(eta_min)`` directly from cross-support local loads.

    For a cross-block pair ``p,q`` the normalized minor is

        K_pq = R * e_p * e_q / (g*p*q).

    Therefore

        v_ell(K_pq)
          = v_ell(R) + v_ell(e_p) + v_ell(e_q) - v_ell(g)
            - 1_[p=ell] - 1_[q=ell].

    The valuation of the gcd is the minimum of these values.
    """
    if prime_factorization(ell) != ((ell, 1),):
        raise ValueError("ell must be prime")
    data = abc_support_state(a, b, c)
    supports = tuple(tuple(int(p) for p in support) for support in data["supports"])
    valuations = tuple(dict(prime_factorization(n)) for n in (a, b, c))
    R = int(data["radical_product"])
    g = additive_relation_content(a, b, c)
    local_values: list[int] = []
    for left_block in range(3):
        for right_block in range(left_block + 1, 3):
            for p in supports[left_block]:
                for q in supports[right_block]:
                    value = (
                        _valuation(R, ell)
                        + _valuation(valuations[left_block][p], ell)
                        + _valuation(valuations[right_block][q], ell)
                        - _valuation(g, ell)
                        - int(p == ell)
                        - int(q == ell)
                    )
                    if value < 0:
                        raise AssertionError("normalized cross-support valuation must be non-negative")
                    local_values.append(value)
    if not local_values:
        raise ValueError("need at least two non-empty support blocks")
    return min(local_values)


def absorption_obstruction_spectrum(a: int, b: int, c: int) -> tuple[tuple[int, int], ...]:
    """Return the exact prime factorization of ``eta_min`` via local loads."""
    data = abc_support_state(a, b, c)
    candidate = int(data["radical_product"])
    for n in (a, b, c):
        for _prime, exponent in prime_factorization(n):
            candidate *= exponent
    candidate_primes = tuple(p for p, _exponent in prime_factorization(candidate))
    spectrum = tuple(
        (ell, local_absorption_valuation(a, b, c, ell))
        for ell in candidate_primes
        if local_absorption_valuation(a, b, c, ell) > 0
    )
    reconstructed = 1
    for ell, exponent in spectrum:
        reconstructed *= ell**exponent
    eta = minimum_absorption_redundancy_support_formula(a, b, c)
    if reconstructed != eta:
        raise AssertionError("local obstruction spectrum failed to reconstruct eta_min")
    return spectrum


def perfect_absorption_local_criterion(a: int, b: int, c: int) -> bool:
    """Return whether every prime-local absorption obstruction vanishes."""
    return not absorption_obstruction_spectrum(a, b, c)


def high_quality_absorption_counterexample() -> dict[str, int | bool | tuple[tuple[int, int], ...]]:
    """Return an exact counterexample to ``high abc quality => eta_min=1``.

    The triple ``1+512=513`` has radical 114 and satisfies
    ``513^4 > 114^5``, hence standard abc quality exceeds ``5/4``.  Nevertheless
    its exact absorption floor is 3.
    """
    a, b, c = 1, 512, 513
    data = abc_support_state(a, b, c)
    R = int(data["radical_product"])
    eta = minimum_absorption_redundancy_support_formula(a, b, c)
    rational_quality_gt_five_fourths = c**4 > R**5
    if R != 114 or eta != 3 or not rational_quality_gt_five_fourths:
        raise AssertionError("high-quality absorption counterexample changed")
    return {
        "a": a,
        "b": b,
        "c": c,
        "radical": R,
        "eta_min": eta,
        "quality_gt_5_over_4": rational_quality_gt_five_fourths,
        "obstruction_spectrum": absorption_obstruction_spectrum(a, b, c),
    }
