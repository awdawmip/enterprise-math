"""Finite resource lower bounds for pre-sampled response completions.

The statements are elementary finite counting.  R004 uses them to make one
candidate restriction on latent completions explicit: if a deterministic
initial seed must encode every response string in a declared full-support
future language, its number of distinguishable seed states cannot be smaller
than the number of required strings.
"""
from __future__ import annotations


def _positive(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def full_support_string_count(num_steps: int, outcomes_per_step: int) -> int:
    """Number of response strings when every step has the same finite alphabet."""
    _positive(num_steps, "num_steps")
    _positive(outcomes_per_step, "outcomes_per_step")
    return outcomes_per_step**num_steps


def minimum_deterministic_seed_states(
    num_steps: int, outcomes_per_step: int
) -> int:
    """Sharp seed-support lower bound for a full-support response-string law.

    A deterministic pre-sampled seed chooses exactly one complete response
    string.  If the target law assigns positive probability to every string,
    every string must occur in the image of the seed map.  Surjectivity onto
    the full response language therefore needs at least ``r**m`` seed states,
    and that many suffice by taking one seed state per response string.
    """
    return full_support_string_count(num_steps, outcomes_per_step)


def presampling_capacity_sufficient(
    seed_capacity: int, num_steps: int, outcomes_per_step: int
) -> bool:
    _positive(seed_capacity, "seed_capacity")
    return seed_capacity >= minimum_deterministic_seed_states(
        num_steps, outcomes_per_step
    )


def presampling_capacity_deficit(
    seed_capacity: int, num_steps: int, outcomes_per_step: int
) -> int:
    _positive(seed_capacity, "seed_capacity")
    required = minimum_deterministic_seed_states(num_steps, outcomes_per_step)
    return max(required - seed_capacity, 0)


def maximum_full_support_steps(
    seed_capacity: int, outcomes_per_step: int
) -> int:
    """Largest m with ``outcomes_per_step**m <= seed_capacity``.

    This is computed by finite integer multiplication; no logarithm or real
    entropy coordinate is needed.
    """
    _positive(seed_capacity, "seed_capacity")
    _positive(outcomes_per_step, "outcomes_per_step")
    if outcomes_per_step == 1:
        return seed_capacity
    steps = 0
    required = 1
    while required * outcomes_per_step <= seed_capacity:
        required *= outcomes_per_step
        steps += 1
    return steps
