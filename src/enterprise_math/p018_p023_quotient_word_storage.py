"""Exact finite storage optimization for bounded quotient-word compilers.

Canonical #249 fixes the one-step semantic action set.  The quotient-word
normalization theorem shows that any positive separating primitive alphabet can
be intersected with the finite nontrivial power-free semantic basis without
losing separation or increasing word length.  Therefore minimum-cardinality
primitive presentation is a finite dictionary-selection problem.

For each required semantic denominator ``b`` and word horizon ``h``, let
``Pi_h(b)`` be the multiplicative partitions of ``b`` into at most ``h``
nontrivial semantic factors.  A normalized alphabet ``G`` reaches ``b`` iff
at least one partition is entirely contained in ``G``:

    OR_{F in Pi_h(b)} AND_{g in F} [g in G].

Thus the general storage problem is a monotone finite OR-of-ANDs optimization,
not ordinary set cover in general.  The penultimate-horizon semiprime set-cover
result is a special collapse of this model.

All multiplicative-basis / monotone Boolean optimization ingredients are prior
mathematics.  This module is an exact exponential oracle for small bounded
quotient-root instances, intended for theorem discovery and regression rather
than large-scale optimization.
"""

from __future__ import annotations

from collections.abc import Iterable
from itertools import combinations

from .p018_p023_power_free_action_basis import (
    minimal_root_quotient_action_basis,
)
from .p018_p023_quotient_word_basis import (
    prime_generator_basis,
    quotient_word_language_separates_bounded_domain,
)


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_root_exp(root_exp: int) -> None:
    if isinstance(root_exp, bool) or not isinstance(root_exp, int) or root_exp < 2:
        raise ValueError("root_exp must be an integer at least 2")


def semantic_storage_candidates(max_state: int, root_exp: int) -> tuple[int, ...]:
    """Finite normalized primitive candidates for storage optimization."""
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    return tuple(
        boundary
        for boundary in minimal_root_quotient_action_basis(max_state, root_exp)
        if boundary >= 2
    )


def forced_prime_storage_core(max_state: int) -> tuple[int, ...]:
    """Bounded primes, forced in every separator when root order is at least 2."""
    _require_natural("max_state", max_state)
    return prime_generator_basis(max_state)


def multiplicative_partitions_within_horizon(
    boundary: int,
    horizon: int,
    candidates: Iterable[int] | None = None,
) -> tuple[tuple[int, ...], ...]:
    """Return all unordered nontrivial factor words for ``boundary``.

    Tuples are stored in nondecreasing order, so permutations of the same
    primitive multiset occur only once.  Repetition is allowed.  The empty word
    is returned only for boundary 1.
    """
    if isinstance(boundary, bool) or not isinstance(boundary, int) or boundary <= 0:
        raise ValueError("boundary must be a positive integer")
    _require_natural("horizon", horizon)
    if boundary == 1:
        return ((),)
    if horizon == 0:
        return ()

    if candidates is None:
        normalized = tuple(range(2, boundary + 1))
    else:
        normalized = tuple(sorted(set(candidates)))
        if any(
            isinstance(value, bool) or not isinstance(value, int) or value < 2
            for value in normalized
        ):
            raise ValueError("candidates must be integers at least 2")

    divisors = tuple(value for value in normalized if boundary % value == 0)
    result: set[tuple[int, ...]] = set()

    def visit(
        remaining: int,
        slots: int,
        start_index: int,
        prefix: tuple[int, ...],
    ) -> None:
        if remaining == 1:
            result.add(prefix)
            return
        if slots == 0:
            return
        for index in range(start_index, len(divisors)):
            factor = divisors[index]
            if factor > remaining or remaining % factor:
                continue
            quotient = remaining // factor
            next_prefix = prefix + (factor,)
            if quotient == 1:
                result.add(next_prefix)
                continue
            if slots == 1:
                continue
            # Maintaining nondecreasing factors prevents permutation duplicates.
            if quotient < factor:
                continue
            visit(quotient, slots - 1, index, next_prefix)

    visit(boundary, horizon, 0, ())
    return tuple(sorted(result, key=lambda part: (len(part), part)))


def storage_partition_constraints(
    max_state: int, root_exp: int, horizon: int
) -> tuple[tuple[int, tuple[tuple[int, ...], ...]], ...]:
    """Return the exact monotone DNF constraint for each nontrivial target."""
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    _require_natural("horizon", horizon)
    candidates = semantic_storage_candidates(max_state, root_exp)
    return tuple(
        (
            boundary,
            multiplicative_partitions_within_horizon(
                boundary, horizon, candidates
            ),
        )
        for boundary in candidates
    )


def normalized_alphabet_satisfies_storage_constraints(
    max_state: int,
    root_exp: int,
    alphabet: Iterable[int],
    horizon: int,
) -> bool:
    """Check separation using the finite normalized multiplicative DNF model."""
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    _require_natural("horizon", horizon)
    candidates = set(semantic_storage_candidates(max_state, root_exp))
    chosen = set(alphabet)
    if not chosen <= candidates:
        raise ValueError("normalized alphabet must lie inside the semantic candidate set")
    return all(
        any(all(factor in chosen for factor in part) for part in partitions)
        for _boundary, partitions in storage_partition_constraints(
            max_state, root_exp, horizon
        )
    )


def minimum_storage_alphabets(
    max_state: int,
    root_exp: int,
    horizon: int,
    *,
    max_solutions: int | None = None,
) -> tuple[tuple[int, ...], ...]:
    """Enumerate minimum-cardinality normalized separating alphabets.

    This is an exact exponential oracle.  Bounded primes are inserted as the
    forced core; composite candidates are then searched by increasing added
    cardinality.  ``max_solutions`` may cap the number of returned optima after
    the minimum cardinality has been established.
    """
    _require_natural("max_state", max_state)
    _require_root_exp(root_exp)
    _require_natural("horizon", horizon)
    if max_solutions is not None:
        if (
            isinstance(max_solutions, bool)
            or not isinstance(max_solutions, int)
            or max_solutions <= 0
        ):
            raise ValueError("max_solutions must be a positive integer or None")

    candidates = semantic_storage_candidates(max_state, root_exp)
    candidate_set = set(candidates)
    forced = tuple(
        prime for prime in forced_prime_storage_core(max_state)
        if prime in candidate_set
    )
    forced_set = set(forced)
    optional = tuple(value for value in candidates if value not in forced_set)
    constraints = storage_partition_constraints(max_state, root_exp, horizon)

    def satisfies(chosen: set[int]) -> bool:
        return all(
            any(all(factor in chosen for factor in part) for part in partitions)
            for _boundary, partitions in constraints
        )

    for extra_count in range(len(optional) + 1):
        solutions: list[tuple[int, ...]] = []
        for extra in combinations(optional, extra_count):
            chosen = forced_set | set(extra)
            if satisfies(chosen):
                solutions.append(tuple(sorted(chosen)))
                if max_solutions is not None and len(solutions) >= max_solutions:
                    return tuple(solutions)
        if solutions:
            return tuple(solutions)
    return ()


def minimum_storage_size(
    max_state: int, root_exp: int, horizon: int
) -> int | None:
    """Return the exact minimum normalized alphabet cardinality, if feasible."""
    solutions = minimum_storage_alphabets(
        max_state, root_exp, horizon, max_solutions=1
    )
    if not solutions:
        return None
    return len(solutions[0])


def minimum_composite_storage_count(
    max_state: int, root_exp: int, horizon: int
) -> int | None:
    """Minimum number of non-prime primitive types beyond the forced core."""
    size = minimum_storage_size(max_state, root_exp, horizon)
    if size is None:
        return None
    return size - len(forced_prime_storage_core(max_state))


def storage_oracle_matches_literal_separator(
    max_state: int,
    root_exp: int,
    alphabet: Iterable[int],
    horizon: int,
) -> bool:
    """Cross-check the partition oracle against the independent word bridge."""
    chosen = tuple(sorted(set(alphabet)))
    dnf = normalized_alphabet_satisfies_storage_constraints(
        max_state, root_exp, chosen, horizon
    )
    literal = quotient_word_language_separates_bounded_domain(
        max_state, root_exp, chosen, horizon
    )
    return dnf == literal
