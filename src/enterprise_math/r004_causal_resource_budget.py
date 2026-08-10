"""Integer storage/innovation capacity bounds for finite causal histories.

A deterministic causal executor may start with at most B_0 latent alternatives
and receive at step t a newly available innovation with at most B_t possible
values.  Up to time t there are at most

    B_0 * product_{j=1}^t B_j

latent transcripts, hence no more distinct visible histories can be produced.
This gives a purely integer necessary resource bound, independent of entropy.

For a fixed finite horizon, the whole transcript (Z_0,U_1,...,U_H) can also be
regarded as one ex-ante static seed with at most the same product support.  Thus
moving finite random resources from initial storage to runtime innovation does
not by itself create a new operational law.  A distinction requires an
additional causal-availability rule saying that future innovations are not
admissibly present/accessible earlier.

This is resource accounting, not a physical axiom and not a claim that nature
actually stores the compiled transcript.
"""

from __future__ import annotations

from collections.abc import Sequence


def _positive_integer(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def causal_history_capacity_profile(
    initial_atoms: int, innovation_atoms: Sequence[int]
) -> tuple[int, ...]:
    """Maximum transcript/history counts after each innovation step.

    Entry zero is the initial latent support bound B_0.  Entry t is
    B_0*B_1*...*B_t.
    """
    capacity = _positive_integer("initial_atoms", initial_atoms)
    result = [capacity]
    for index, raw in enumerate(innovation_atoms, start=1):
        factor = _positive_integer(f"innovation_atoms[{index}]", raw)
        capacity *= factor
        result.append(capacity)
    return tuple(result)


def finite_horizon_static_compilation_bound(
    initial_atoms: int, innovation_atoms: Sequence[int]
) -> int:
    """Atom bound after bundling all finite-horizon innovations into one seed."""
    return causal_history_capacity_profile(initial_atoms, innovation_atoms)[-1]


def history_support_profile_fits_budget(
    history_support_counts: Sequence[int],
    initial_atoms: int,
    innovation_atoms: Sequence[int],
) -> bool:
    """Check the necessary prefix-support capacity inequalities exactly.

    ``history_support_counts[t]`` is the number of positive visible histories
    after t steps, so the sequence must include the time-zero support at index 0
    and have one more entry than ``innovation_atoms``.
    """
    counts = tuple(history_support_counts)
    innovations = tuple(innovation_atoms)
    if len(counts) != len(innovations) + 1 or not counts:
        raise ValueError("history support profile must include time zero and one entry per step")
    if any(
        isinstance(count, bool) or not isinstance(count, int) or count <= 0
        for count in counts
    ):
        raise ValueError("history support counts must be positive integers")
    capacities = causal_history_capacity_profile(initial_atoms, innovations)
    return all(count <= capacity for count, capacity in zip(counts, capacities, strict=True))


def first_budget_violation_step(
    history_support_counts: Sequence[int],
    initial_atoms: int,
    innovation_atoms: Sequence[int],
) -> int | None:
    """First t at which target prefix support exceeds available causal transcripts."""
    counts = tuple(history_support_counts)
    innovations = tuple(innovation_atoms)
    if len(counts) != len(innovations) + 1 or not counts:
        raise ValueError("history support profile must include time zero and one entry per step")
    capacities = causal_history_capacity_profile(initial_atoms, innovations)
    for step, (count, capacity) in enumerate(zip(counts, capacities, strict=True)):
        if isinstance(count, bool) or not isinstance(count, int) or count <= 0:
            raise ValueError("history support counts must be positive integers")
        if count > capacity:
            return step
    return None


def uniform_full_support_history_profile(alphabet_size: int, horizon: int) -> tuple[int, ...]:
    """Prefix-support profile (1,r,r^2,...,r^H) of a full r-ary history tree."""
    r = _positive_integer("alphabet_size", alphabet_size)
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 0:
        raise ValueError("horizon must be a non-negative integer")
    return tuple(r**step for step in range(horizon + 1))


def uniform_history_budget_holds(
    alphabet_size: int,
    horizon: int,
    initial_atoms: int,
    innovation_atoms: Sequence[int],
) -> bool:
    """Check all prefix inequalities for the full uniform r-ary support tree."""
    innovations = tuple(innovation_atoms)
    if len(innovations) != horizon:
        raise ValueError("one innovation budget is required per history step")
    return history_support_profile_fits_budget(
        uniform_full_support_history_profile(alphabet_size, horizon),
        initial_atoms,
        innovations,
    )


def static_uniform_history_atom_requirement(alphabet_size: int, horizon: int) -> int:
    """Exact atom count needed with no runtime innovation for full r-ary H-history."""
    return uniform_full_support_history_profile(alphabet_size, horizon)[-1]


def prestored_prefix_then_online_schedule(
    alphabet_size: int, horizon: int, prestored_steps: int
) -> tuple[int, tuple[int, ...]]:
    """One exact Pareto schedule for the uniform full-support history tree.

    The initial seed stores the first ``prestored_steps`` symbols, requiring
    r^prestored_steps atoms.  No fresh support is needed during those steps;
    later steps use r-way innovations.  Every prefix capacity inequality is met
    with equality from the storage/execution handoff onward.
    """
    r = _positive_integer("alphabet_size", alphabet_size)
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 0:
        raise ValueError("horizon must be a non-negative integer")
    if (
        isinstance(prestored_steps, bool)
        or not isinstance(prestored_steps, int)
        or prestored_steps < 0
        or prestored_steps > horizon
    ):
        raise ValueError("prestored_steps must lie between zero and horizon")
    initial = r**prestored_steps
    innovations = tuple(
        1 if step <= prestored_steps else r
        for step in range(1, horizon + 1)
    )
    if not uniform_history_budget_holds(r, horizon, initial, innovations):
        raise AssertionError("declared Pareto schedule must meet every prefix capacity bound")
    return initial, innovations
