"""Adaptive versus static future precision in the binary root regime.

Assume ``0 <= q <= N < 2**r``.  Then a positive quotient action ``a`` followed
by the ``r``-th-root observation is exactly the threshold bit

    root_r(q // a) = 1  iff  a <= q.

Thus the quotient-root future language becomes an ordered threshold-query
system.  This module keeps three resources separate:

* static future alphabet size;
* adaptive query depth when arbitrary thresholds are one-step actions;
* adaptive primitive-action cost when only prime generators are primitive and
  a threshold ``a`` is compiled as a prime word of length ``Omega(a)``.

Binary search, information lower bounds, prime factorization, and ordered
threshold decision trees are prior mathematics.  The project-specific role of
this module is only to expose their exact finite quotient-root specialization as
an executable P023/P024 pressure test.
"""

from __future__ import annotations

from functools import lru_cache

from .p018_p023_quotient_word_basis import omega_with_multiplicity


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def threshold_bit(state: int, threshold: int) -> int:
    """Return the ordered threshold observation ``1[threshold <= state]``."""
    _require_natural("state", state)
    if isinstance(threshold, bool) or not isinstance(threshold, int) or threshold <= 0:
        raise ValueError("threshold must be a positive integer")
    return int(threshold <= state)


def static_threshold_signature(state: int, thresholds: tuple[int, ...]) -> tuple[int, ...]:
    """Return the nonadaptive threshold signature in the supplied query order."""
    return tuple(threshold_bit(state, threshold) for threshold in thresholds)


def static_thresholds_separate_domain(max_state: int, thresholds: tuple[int, ...]) -> bool:
    """Check whether fixed threshold queries distinguish every state ``0,...,N``."""
    _require_natural("max_state", max_state)
    signatures = [static_threshold_signature(q, thresholds) for q in range(max_state + 1)]
    return len(signatures) == len(set(signatures))


def minimal_static_future_thresholds_after_current(max_state: int) -> tuple[int, ...]:
    """Exact future threshold set after the free current/root query at threshold 1.

    In the binary root regime the current observation already distinguishes
    state 0 from all positive states.  To distinguish every remaining adjacent
    pair ``a-1,a`` one needs, and is sufficed by, every threshold ``a=2,...,N``.
    """
    _require_natural("max_state", max_state)
    return tuple(range(2, max_state + 1))


def adaptive_unit_query_depth_after_current(max_state: int) -> int:
    """Exact worst-case number of *additional* adaptive threshold queries.

    The free current observation first isolates state 0.  If the state is
    positive, ``N`` possibilities remain and ordinary balanced binary search
    needs exactly ``ceil(log2 N)`` further threshold queries.
    """
    _require_natural("max_state", max_state)
    if max_state <= 1:
        return 0
    return (max_state - 1).bit_length()


@lru_cache(maxsize=None)
def _adaptive_unit_interval_depth(lower: int, upper: int) -> int:
    if lower >= upper:
        return 0
    return 1 + min(
        max(
            _adaptive_unit_interval_depth(lower, threshold - 1),
            _adaptive_unit_interval_depth(threshold, upper),
        )
        for threshold in range(lower + 1, upper + 1)
    )


def adaptive_unit_query_depth_dp_after_current(max_state: int) -> int:
    """Independent exact interval-DP realization of the unit-cost depth."""
    _require_natural("max_state", max_state)
    if max_state <= 1:
        return 0
    return _adaptive_unit_interval_depth(1, max_state)


@lru_cache(maxsize=None)
def _adaptive_prime_interval_cost(lower: int, upper: int) -> int:
    if lower >= upper:
        return 0
    return min(
        omega_with_multiplicity(threshold)
        + max(
            _adaptive_prime_interval_cost(lower, threshold - 1),
            _adaptive_prime_interval_cost(threshold, upper),
        )
        for threshold in range(lower + 1, upper + 1)
    )


def adaptive_prime_word_cost_after_current(max_state: int) -> int:
    """Exact worst-case primitive-action cost for the prime generator alphabet.

    A threshold ``a`` is executable by a shortest prime word of length
    ``Omega(a)``.  The recurrence minimizes the worst-case sum of those word
    lengths over adaptive ordered threshold trees on the remaining states
    ``1,...,N`` after the free current observation.
    """
    _require_natural("max_state", max_state)
    if max_state <= 1:
        return 0
    return _adaptive_prime_interval_cost(1, max_state)


def adaptive_prime_word_best_first_threshold(max_state: int) -> int | None:
    """Return one optimal first threshold for the weighted prime-word problem."""
    _require_natural("max_state", max_state)
    if max_state <= 1:
        return None
    best_threshold = None
    best_cost = None
    for threshold in range(2, max_state + 1):
        value = omega_with_multiplicity(threshold) + max(
            _adaptive_prime_interval_cost(1, threshold - 1),
            _adaptive_prime_interval_cost(threshold, max_state),
        )
        if best_cost is None or value < best_cost:
            best_cost = value
            best_threshold = threshold
    return best_threshold
