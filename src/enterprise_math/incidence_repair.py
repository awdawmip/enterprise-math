"""Finite incidence-relation repair burden for P023/A4.

A tagged state is one realized incidence ``(label, state)``.  If only an
observation of ``state`` is retained but the task must recover ``label``, the
minimum repair alphabet is the maximum number of distinct labels realized in
one observation fiber.

Two monotonicities are fundamental:

* enlarging the admissible relation cannot lower repair burden;
* coarsening the retained observation cannot lower repair burden.

This module is a finite executable specification of those elementary facts.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping
from typing import TypeVar

Label = TypeVar("Label", bound=Hashable)
State = TypeVar("State", bound=Hashable)
Obs = TypeVar("Obs", bound=Hashable)
CoarseObs = TypeVar("CoarseObs", bound=Hashable)

Incidence = frozenset[tuple[Label, State]]


def _relation(relation: Iterable[tuple[Label, State]]) -> Incidence:
    result = frozenset(relation)
    if not result:
        raise ValueError("incidence relation must be nonempty")
    return result


def label_sets_by_observation(
    relation: Iterable[tuple[Label, State]], observation: Mapping[State, Obs]
) -> dict[Obs, frozenset[Label]]:
    """Return the distinct realized labels in every retained observation fiber."""

    rel = _relation(relation)
    missing = {state for _, state in rel if state not in observation}
    if missing:
        raise ValueError("observation must cover every state used by the relation")

    labels: dict[Obs, set[Label]] = {}
    for label, state in rel:
        labels.setdefault(observation[state], set()).add(label)
    return {obs: frozenset(values) for obs, values in labels.items()}


def incidence_repair_alphabet_size(
    relation: Iterable[tuple[Label, State]], observation: Mapping[State, Obs]
) -> int:
    """Exact minimum alphabet for recovering the label over the observation.

    By P023-S9 this is the maximum local split multiplicity of the observation
    quotient when the target also retains the incidence label.
    """

    labels = label_sets_by_observation(relation, observation)
    return max(len(values) for values in labels.values())


def label_decoder_exists(
    relation: Iterable[tuple[Label, State]], observation: Mapping[State, Obs]
) -> bool:
    """Whether no nonconstant repair coordinate is needed for label recovery."""

    return incidence_repair_alphabet_size(relation, observation) == 1


def relation_enlargement_monotone(
    subrelation: Iterable[tuple[Label, State]],
    superrelation: Iterable[tuple[Label, State]],
    observation: Mapping[State, Obs],
) -> bool:
    """Verify ``R⊆R' => M(R,g)<=M(R',g)`` for supplied finite relations."""

    sub = _relation(subrelation)
    sup = _relation(superrelation)
    if not sub.issubset(sup):
        raise ValueError("subrelation must be contained in superrelation")
    return incidence_repair_alphabet_size(sub, observation) <= incidence_repair_alphabet_size(
        sup, observation
    )


def observation_factors_through(
    states: Iterable[State],
    fine: Mapping[State, Obs],
    coarse: Mapping[State, CoarseObs],
) -> bool:
    """Whether ``coarse = phi ∘ fine`` on the supplied finite state set."""

    domain = tuple(states)
    if not domain:
        raise ValueError("state domain must be nonempty")
    if any(state not in fine or state not in coarse for state in domain):
        raise ValueError("both observations must cover the state domain")
    seen: dict[Obs, CoarseObs] = {}
    for state in domain:
        fine_value = fine[state]
        coarse_value = coarse[state]
        previous = seen.get(fine_value)
        if previous is not None and previous != coarse_value:
            return False
        seen[fine_value] = coarse_value
    return True


def observation_coarsening_monotone(
    relation: Iterable[tuple[Label, State]],
    fine: Mapping[State, Obs],
    coarse: Mapping[State, CoarseObs],
) -> bool:
    """Verify that coarsening a retained observation cannot lower repair burden."""

    rel = _relation(relation)
    states = {state for _, state in rel}
    if not observation_factors_through(states, fine, coarse):
        raise ValueError("coarse observation must factor through the fine observation")
    return incidence_repair_alphabet_size(rel, fine) <= incidence_repair_alphabet_size(
        rel, coarse
    )


def joint_monotonicity(
    subrelation: Iterable[tuple[Label, State]],
    superrelation: Iterable[tuple[Label, State]],
    fine: Mapping[State, Obs],
    coarse: Mapping[State, CoarseObs],
) -> bool:
    """Verify the combined admissibility/observation monotonicity square."""

    sub = _relation(subrelation)
    sup = _relation(superrelation)
    if not sub.issubset(sup):
        raise ValueError("subrelation must be contained in superrelation")
    states = {state for _, state in sup}
    if not observation_factors_through(states, fine, coarse):
        raise ValueError("coarse observation must factor through the fine observation")
    return incidence_repair_alphabet_size(sub, fine) <= incidence_repair_alphabet_size(
        sup, coarse
    )
