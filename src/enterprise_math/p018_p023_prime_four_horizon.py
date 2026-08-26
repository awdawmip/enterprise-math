"""Exact executable geometry for the bounded prime ISA plus macro ``4``.

This module isolates one particularly sharp Stage131 resource point.  In the
high-root regime ``N < 2**r`` every positive denominator up to ``N`` is a
semantic action.  Adding the single composite instruction ``4`` to all bounded
primes changes the shortest length of

    b = 2**e2 * product_{p odd} p**e_p

to

    ceil(e2 / 2) + sum_{p odd} e_p.

The least integer requiring exactly ``k>=1`` instructions is therefore

    2 * 3**(k - 1),

so the exact worst-case depth is

    1 + floor(log_3(floor(N / 2)))

for ``N>=2``.  The direct routines below intentionally call the pre-existing
packing oracle, while the closed-form routines use only integer arithmetic, so
the two paths can regression-test one another.

Prime factorization, weighted multiplicative length and integer logarithms are
prior mathematics.  This file is the quotient-root specialization and an
independent executable check for the proof-shaped Lean development.
"""

from __future__ import annotations

from .p018_p023_power_free_action_basis import (
    minimal_root_quotient_action_basis,
)
from .p018_p023_quotient_word_compression import (
    shortest_prime_macro_word_length,
)


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_root_exp(root_exp: int) -> None:
    if isinstance(root_exp, bool) or not isinstance(root_exp, int) or root_exp < 2:
        raise ValueError("root_exp must be an integer at least 2")


def floor_log(base: int, n: int) -> int:
    """Return the largest ``k`` with ``base**k <= n`` for ``base>=2,n>=1``."""
    if isinstance(base, bool) or not isinstance(base, int) or base < 2:
        raise ValueError("base must be an integer at least 2")
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    k = 0
    power = 1
    while power * base <= n:
        power *= base
        k += 1
    return k


def prime_four_shortest_word_length(boundary: int) -> int:
    """Exact shortest quotient-word length over bounded primes plus macro 4."""
    if isinstance(boundary, bool) or not isinstance(boundary, int) or boundary < 1:
        raise ValueError("boundary must be a positive integer")
    if boundary == 1:
        return 0
    return shortest_prime_macro_word_length(boundary, (4,))


def prime_four_required_horizon(max_state: int, root_exp: int) -> int:
    """Direct exact worst-case depth using the independent macro-packing oracle."""
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    return max(
        (
            prime_four_shortest_word_length(boundary)
            for boundary in minimal_root_quotient_action_basis(max_state, root_exp)
            if boundary >= 2
        ),
        default=0,
    )


def minimal_boundary_for_prime_four_length(length: int) -> int:
    """Closed-form least positive integer with prime+4 word length ``length``.

    For ``length=0`` the empty word gives boundary 1.  For ``length>=1`` the
    minimum is ``2*3**(length-1)``.
    """
    _require_natural("length", length)
    if length == 0:
        return 1
    return 2 * 3 ** (length - 1)


def binary_prime_four_required_horizon(max_state: int, root_exp: int) -> int:
    """Closed-form prime+4 depth in the high-root/binary semantic regime."""
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    if max_state >= 2**root_exp:
        raise ValueError("binary/high-root regime requires max_state < 2**root_exp")
    if max_state < 2:
        return 0
    return 1 + floor_log(3, max_state // 2)


def binary_prime_four_formula_matches_direct(max_state: int, root_exp: int) -> bool:
    """Cross-check closed form against the independent direct packing path."""
    return binary_prime_four_required_horizon(
        max_state, root_exp
    ) == prime_four_required_horizon(max_state, root_exp)
