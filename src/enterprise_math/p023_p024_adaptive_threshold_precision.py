"""Static, reset-oracle adaptive, and destructive future precision.

Assume ``0 <= q <= N < 2**r``. Then a positive quotient denominator ``a``
followed by the ``r``-th-root observation is exactly the threshold bit

    root_r(q // a) = 1  iff  a <= q.

There are two different adaptive semantics and they must not be identified.

RESET / COUNTERFACTUAL ORACLE
    Each threshold query is evaluated on the same original state ``q`` (for
    example by reset, a fresh copy, or a counterfactual signature coordinate).
    Under this semantics ordinary binary search applies.  The functions named
    ``adaptive_*`` below belong to this reset-oracle model.

DESTRUCTIVE SINGLE TRAJECTORY
    A literal quotient action updates the actual state

        q <- q // a.

    Later actions continue from that changed state.  In the binary regime this
    is much weaker: for ``N >= 3`` no adaptive single-trajectory quotient
    protocol can recover the exact initial positive state at any finite depth.
    Before the first nonidentity action all positive states look the same.  If
    that first action is 2, initial states 2 and 3 both become 1; if it is at
    least 3, initial states 1 and 2 both become 0.  Once two candidates become
    the same exact state, no continuation can distinguish them.

This distinction is the intended P023/P024 pressure test: a counterfactual
future signature can be exact even when no one physically executable
state-mutating experiment path is identifying.

Binary search, information lower bounds, prime factorization, decision trees,
and irreversible state merging are prior mathematics/CS.  Project-specific
scope is only the exact quotient-root specialization and precision-layer
separation.
"""

from __future__ import annotations

from functools import lru_cache

from .p018_p023_quotient_word_basis import omega_with_multiplicity


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_binary_regime(max_state: int, root_exp: int) -> None:
    _require_natural("max_state", max_state)
    _require_positive("root_exp", root_exp)
    if max_state >= 2**root_exp:
        raise ValueError("requires max_state < 2**root_exp")


def threshold_bit(state: int, threshold: int) -> int:
    """Return the ordered threshold observation ``1[threshold <= state]``."""
    _require_natural("state", state)
    _require_positive("threshold", threshold)
    return int(threshold <= state)


def static_threshold_signature(
    state: int, thresholds: tuple[int, ...]
) -> tuple[int, ...]:
    """Return the nonadaptive counterfactual threshold signature."""
    return tuple(threshold_bit(state, threshold) for threshold in thresholds)


def static_thresholds_separate_domain(
    max_state: int, thresholds: tuple[int, ...]
) -> bool:
    """Check whether fixed counterfactual thresholds separate ``0,...,N``."""
    _require_natural("max_state", max_state)
    signatures = [
        static_threshold_signature(q, thresholds) for q in range(max_state + 1)
    ]
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
    """Exact additional depth in the RESET / counterfactual-oracle model.

    Every query is evaluated on the same original state.  The free current
    observation first isolates state 0.  If the state is positive, ``N``
    possibilities remain and balanced binary search needs exactly
    ``ceil(log2 N)`` further threshold queries.

    This is not the depth of one destructive quotient trajectory; see
    ``destructive_single_trajectory_exact_depth`` below.
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
    """Independent interval-DP oracle for RESET adaptive unit-cost depth."""
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
    """Exact RESET-oracle cost when thresholds are compiled from prime words.

    Threshold ``a`` is charged ``Omega(a)`` primitive quotient instructions,
    but the threshold result is treated as a query on the original state and
    the next query starts from that original state again.  Intermediate prefix
    observations inside the compiled word are not used by this cost model.

    Thus this is a counterfactual/reset experiment cost, not the cost of one
    continuing destructive quotient trajectory.
    """
    _require_natural("max_state", max_state)
    if max_state <= 1:
        return 0
    return _adaptive_prime_interval_cost(1, max_state)


def adaptive_prime_word_best_first_threshold(max_state: int) -> int | None:
    """Return one optimal first RESET-oracle threshold in the weighted model."""
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


def destructive_first_nonidentity_merge_pair(
    max_state: int, action: int
) -> tuple[int, int] | None:
    """Return the pair irreversibly merged by a first nonidentity quotient.

    On the positive binary-regime branch with ``N>=3``:

    * action 2 merges initial states 2 and 3 to exact state 1;
    * every action >=3 merges initial states 1 and 2 to exact state 0.

    Action 1 changes nothing and therefore has no forced merge pair yet.
    """
    _require_natural("max_state", max_state)
    _require_positive("action", action)
    if max_state < 3 or action == 1:
        return None
    if action == 2:
        return (2, 3)
    return (1, 2)


def destructive_single_trajectory_exact_depth(
    max_state: int, root_exp: int
) -> int | None:
    """Exact identification depth for one literal state-mutating trajectory.

    The result is valid in the binary root regime ``N < 2**r`` after the free
    current observation has already isolated state 0.

    * ``N<=1``: no additional action is needed;
    * ``N=2``: denominator 2 distinguishes the two positive states in one step;
    * ``N>=3``: exact identification is impossible at every finite depth.

    ``None`` denotes the last case, not an unknown bound.
    """
    _require_binary_regime(max_state, root_exp)
    if max_state <= 1:
        return 0
    if max_state == 2:
        return 1
    return None


def destructive_single_trajectory_identifiable(
    max_state: int, root_exp: int
) -> bool:
    """Return whether one destructive quotient trajectory can identify exactly."""
    return destructive_single_trajectory_exact_depth(max_state, root_exp) is not None
