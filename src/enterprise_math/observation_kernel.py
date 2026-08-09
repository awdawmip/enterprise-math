"""Precision/observation kernels under deterministic dynamics.

The key distinction is between true state coalescence and equality only after an
observation/projection.  An arbitrary observation kernel need not be persistent
in time: hidden fine-state distinctions can reappear at later observations.
Persistence is guaranteed when the observation kernel is a congruence for the
dynamics, equivalently (for a surjective observation) when the fine dynamics
descends to an autonomous coarse map.

The quotient-factorization and semiconjugacy principles are established
mathematics.  This module pressure-tests their exact role in Enterprise Math
precision/time semantics.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Iterable

from .coalescence_time import first_coalescence_time, iterate
from .collision_increment import collision_polynomial_from_fiber_sizes

NaturalOperation = Callable[[int], int]
Observation = Callable[[int], int]


def _states_tuple(states: Iterable[int]) -> tuple[int, ...]:
    materialized = tuple(states)
    if len(set(materialized)) != len(materialized):
        raise ValueError("states must be distinct labels")
    for state in materialized:
        if isinstance(state, bool) or not isinstance(state, int) or state < 0:
            raise ValueError("states must be non-negative integers")
    return materialized


def observed_equal_at(
    operation: NaturalOperation,
    observation: Observation,
    left: int,
    right: int,
    step: int,
) -> bool:
    """Whether two fine histories have the same observed state at one time."""
    return observation(iterate(operation, left, step)) == observation(
        iterate(operation, right, step)
    )


def observed_kernel_pairs(
    operation: NaturalOperation,
    observation: Observation,
    states: Iterable[int],
    step: int,
) -> set[tuple[int, int]]:
    """Kernel relation of ``observation ∘ operation^[step]`` on labelled states."""
    materialized = _states_tuple(states)
    return {
        (left, right)
        for left in materialized
        for right in materialized
        if observed_equal_at(operation, observation, left, right, step)
    }


def observation_compatible_on_domain(
    operation: NaturalOperation,
    observation: Observation,
    states: Iterable[int],
) -> bool:
    """Finite-domain kernel-congruence check.

    This checks ``O(x)=O(y) -> O(F(x))=O(F(y))`` for all supplied states.
    """
    materialized = _states_tuple(states)
    for left in materialized:
        for right in materialized:
            if observation(left) == observation(right) and observation(
                operation(left)
            ) != observation(operation(right)):
                return False
    return True


def semiconjugacy_holds_on_domain(
    fine_operation: NaturalOperation,
    coarse_operation: NaturalOperation,
    observation: Observation,
    states: Iterable[int],
) -> bool:
    """Finite-domain check of ``O(F(x)) = G(O(x))``."""
    materialized = _states_tuple(states)
    return all(
        observation(fine_operation(state)) == coarse_operation(observation(state))
        for state in materialized
    )


def observed_first_equal_time(
    operation: NaturalOperation,
    observation: Observation,
    left: int,
    right: int,
    *,
    max_steps: int = 10000,
) -> int | None:
    """First time two fine histories have equal observed outputs.

    Unlike true coalescence, equality found here is not assumed persistent unless
    the observation is dynamically compatible.
    """
    for step in range(max_steps + 1):
        if observed_equal_at(operation, observation, left, right, step):
            return step
    return None


def postcomposed_observation_kernel_inclusion(
    operation: NaturalOperation,
    fine_observation: Observation,
    postprocess: Observation,
    states: Iterable[int],
    step: int,
) -> bool:
    """At fixed time, postprocessing can only coarsen an observation kernel."""
    materialized = _states_tuple(states)
    coarse_observation = lambda value: postprocess(fine_observation(value))
    fine = observed_kernel_pairs(
        operation, fine_observation, materialized, step
    )
    coarse = observed_kernel_pairs(
        operation, coarse_observation, materialized, step
    )
    return fine <= coarse


def observed_kernel_persistent_on_horizon(
    operation: NaturalOperation,
    observation: Observation,
    states: Iterable[int],
    horizon: int,
) -> bool:
    """Check monotone growth of observed kernels through a finite horizon."""
    materialized = _states_tuple(states)
    previous = observed_kernel_pairs(operation, observation, materialized, 0)
    for step in range(1, horizon + 1):
        current = observed_kernel_pairs(operation, observation, materialized, step)
        if not previous <= current:
            return False
        previous = current
    return True


def observed_collision_coefficients(
    operation: NaturalOperation,
    observation: Observation,
    states: Iterable[int],
    step: int,
) -> tuple[int, ...]:
    """P011 collision coefficients of one finite observed history partition."""
    materialized = _states_tuple(states)
    images = [observation(iterate(operation, state, step)) for state in materialized]
    sizes = tuple(Counter(images).values())
    return collision_polynomial_from_fiber_sizes(sizes)


def true_merge_time_dominates_observed_first_equality(
    operation: NaturalOperation,
    observation: Observation,
    left: int,
    right: int,
    *,
    max_steps: int = 10000,
) -> bool:
    """Whenever true finite coalescence is found, observation equality occurs no later."""
    true_tau = first_coalescence_time(
        operation, left, right, max_steps=max_steps
    )
    if true_tau is None:
        return True
    observed_tau = observed_first_equal_time(
        operation, observation, left, right, max_steps=max_steps
    )
    return observed_tau is not None and observed_tau <= true_tau


def quotient_addition_descent_counterexample(radix: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Return two fine input pairs with identical coarse coordinates but distinct coarse sums.

    For every ``radix > 1``, `(0,0)` and `(radix-1,1)` both project to coarse
    coordinates `(0,0)`, while their projected sums are `0` and `1`.  Thus
    quotient coordinates alone cannot carry exact addition without detail/carry.
    """
    if isinstance(radix, bool) or not isinstance(radix, int) or radix <= 1:
        raise ValueError("radix must be an integer greater than one")
    return (0, 0), (radix - 1, 1)
