"""Reconstruct hidden Barlow drift from the full coordination history.

A single shell cardinality sees only

    Q_n = d_plus(n)^2 + d_minus(n)^2,

which can have multiple static sum-of-two-squares representations.  Across
successive radii, however, each one-sided absolute drift changes by exactly one
in the reflected sense ``d -> |d±1|``.  Given the previous unordered drift
pair, distinct successor orbits have distinct squared energies.  Therefore the
entire Q-history reconstructs the unordered absolute drift pair at every
radius.

Since whole-shell geodesic totals use positive/negative target layers only
through the symmetric sum of their absolute-drift contributions, the complete
coordination history through radius n determines T_n exactly.
"""

from __future__ import annotations

from itertools import product

from .p022_barlow_coordination import shell_drift_energy_from_vertex_count
from .p022_barlow_coordination_fibers import admissible_absolute_imbalances
from .p022_barlow_layer_tradeoff import layer_shell_geodesic_total

DriftPair = tuple[int, int]  # canonical nondecreasing absolute pair
DriftHistory = tuple[DriftPair, ...]


def canonical_drift_pair(left: int, right: int) -> DriftPair:
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in (left, right)
    ):
        raise ValueError("absolute drifts must be non-negative integers")
    return (left, right) if left <= right else (right, left)


def candidate_absolute_drift_pairs(radius: int, drift_energy: int) -> tuple[DriftPair, ...]:
    """All static unordered parity-compatible representations of one Q_n."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be non-negative")
    if isinstance(drift_energy, bool) or not isinstance(drift_energy, int) or drift_energy < 0:
        raise ValueError("drift_energy must be non-negative")
    values = admissible_absolute_imbalances(radius)
    return tuple(
        sorted(
            {
                canonical_drift_pair(left, right)
                for left in values
                for right in values
                if left * left + right * right == drift_energy
            }
        )
    )


def one_coordinate_absolute_successors(drift: int) -> tuple[int, ...]:
    """Possible next absolute magnitudes after one additional ±1 sign."""
    if isinstance(drift, bool) or not isinstance(drift, int) or drift < 0:
        raise ValueError("drift must be a non-negative integer")
    if drift == 0:
        return (1,)
    return (drift - 1, drift + 1)


def unordered_drift_pair_successors(pair: DriftPair) -> tuple[DriftPair, ...]:
    """All next unordered drift pairs from one current unordered pair."""
    left, right = canonical_drift_pair(*pair)
    return tuple(
        sorted(
            {
                canonical_drift_pair(next_left, next_right)
                for next_left, next_right in product(
                    one_coordinate_absolute_successors(left),
                    one_coordinate_absolute_successors(right),
                )
            }
        )
    )


def successor_energy_map(pair: DriftPair) -> tuple[tuple[int, DriftPair], ...]:
    """Map successor squared energy to successor orbit.

    The energies must be unique.  Algebraically, from a signed representative
    (a,b) the energy increment is ``2+2(±a±b)``.  Equal increments can only
    arise from coordinate exchange/sign symmetries that produce the same
    unordered absolute successor.
    """
    mapping: dict[int, DriftPair] = {}
    for successor in unordered_drift_pair_successors(pair):
        energy = successor[0] * successor[0] + successor[1] * successor[1]
        if energy in mapping and mapping[energy] != successor:
            raise AssertionError("distinct drift successor orbits cannot share energy")
        mapping[energy] = successor
    return tuple(sorted(mapping.items()))


def reconstruct_unordered_drift_history(
    shell_cardinalities: tuple[int, ...]
) -> DriftHistory:
    """Recover unordered absolute drift pairs from S_0,...,S_n.

    The input must include the radius-zero shell ``S_0=1``.
    """
    if not isinstance(shell_cardinalities, tuple) or not shell_cardinalities:
        raise ValueError("shell_cardinalities must be a nonempty tuple")
    if shell_cardinalities[0] != 1:
        raise ValueError("coordination history must start with S_0=1")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in shell_cardinalities
    ):
        raise ValueError("shell cardinalities must be positive integers")

    history: list[DriftPair] = [(0, 0)]
    previous = (0, 0)
    for radius, shell in enumerate(shell_cardinalities[1:], start=1):
        energy = shell_drift_energy_from_vertex_count(radius, shell)
        static_candidates = set(candidate_absolute_drift_pairs(radius, energy))
        dynamic_candidates = {
            successor
            for successor in unordered_drift_pair_successors(previous)
            if successor[0] * successor[0] + successor[1] * successor[1]
            == energy
        }
        candidates = static_candidates.intersection(dynamic_candidates)
        if len(candidates) != 1:
            raise ValueError(
                "shell history is not a unique legal Barlow drift trajectory"
            )
        current = next(iter(candidates))
        history.append(current)
        previous = current
    return tuple(history)


def geodesic_total_from_unordered_drift_history(
    radius: int, drift_history: DriftHistory
) -> int:
    """Reconstruct whole-shell T_n from unordered absolute drift history."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be non-negative")
    if len(drift_history) <= radius:
        raise ValueError("drift_history must contain radii through target")
    if drift_history[0] != (0, 0):
        raise ValueError("drift history must start at (0,0)")
    if radius == 0:
        return 1

    total = layer_shell_geodesic_total(radius, 0, 0)
    for height in range(1, radius + 1):
        left, right = drift_history[height]
        total += layer_shell_geodesic_total(radius, height, left)
        total += layer_shell_geodesic_total(radius, height, right)
    return total


def geodesic_total_from_coordination_history(
    shell_cardinalities: tuple[int, ...]
) -> int:
    """Exact map ``(S_0,...,S_n) -> T_n``."""
    history = reconstruct_unordered_drift_history(shell_cardinalities)
    return geodesic_total_from_unordered_drift_history(
        len(shell_cardinalities) - 1, history
    )
