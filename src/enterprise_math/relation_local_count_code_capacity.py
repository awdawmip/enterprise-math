"""Universal local coefficient-code criterion for exact count branching.

For a coefficient semiring K, the raw natural successor count n enters K as

    eta_K(n) = n * 1_K.

A finite relation family with maximum raw outdegree Delta only ever asks this
code to represent counts in the alphabet

    {0,1,...,Delta}.

The K-valued weighted refinement is universally identical to exact natural-count
branching on every relation world with outdegree at most Delta **iff** eta_K is
injective on that finite alphabet.

Sufficiency: on every current target partition, source-to-block weights lie in
0..Delta, so equality of K-weight vectors is exactly equality of natural-count
vectors.  Every refinement step therefore agrees by induction.

Necessity: if two distinct counts r,s<=Delta have eta_K(r)=eta_K(s), construct
two same-observation sources with r and s distinct successors, all in one
behavioural target class.  Exact N splits the sources and K merges them at the
first refinement step.

This turns coefficient precision into a finite coding-capacity question.  It
also exposes genuine capability synergy: a product of two coarse coefficient
views can be injective on a larger local count alphabet than either view alone.

Concrete capacities:

* Boolean support: 1;
* mod M: M-1;
* Boolean x mod M: M;
* product of modular worlds M_i: lcm(M_i)-1;
* Boolean x product(mod M_i): lcm(M_i).

These are universal worst-case capacities for direct compositional branching,
not necessarily the realized minimum precision of one fixed relation system.

Finite coding, CRT and semiring products are standard prior mathematics/CS. The
project value is the exact task-relative coefficient-capacity theorem and its
semantic-join interpretation.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import lcm
from typing import Callable, Hashable, Mapping, Sequence

from .admissible_support import Relation
from .relation_branching_semiring import (
    SemiringSpec,
    boolean_semiring,
    modular_semiring,
    natural_semiring,
    product_semiring,
)
from .relation_semiring_stable_refinement import (
    SharedSemiringRefinementReport,
    coarsest_shared_semiring_refinement,
)
from .relation_support_stable_refinement import Partition, partition_from_observation


State = Hashable
Action = Hashable
Observation = Hashable
Coefficient = Hashable


def _nonnegative_integer(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")
    return value


def natural_code_values(
    semiring: SemiringSpec,
    max_count: int,
) -> tuple[Coefficient, ...]:
    delta = _nonnegative_integer(max_count, name="max_count")
    return tuple(semiring.natural(count) for count in range(delta + 1))


def natural_code_injective_through(
    semiring: SemiringSpec,
    max_count: int,
) -> bool:
    values = natural_code_values(semiring, max_count)
    return len(set(values)) == len(values)


def first_natural_code_collision(
    semiring: SemiringSpec,
    max_count: int,
) -> tuple[int, int] | None:
    delta = _nonnegative_integer(max_count, name="max_count")
    seen: dict[Coefficient, int] = {}
    for count in range(delta + 1):
        code = semiring.natural(count)
        if code in seen:
            return seen[code], count
        seen[code] = count
    return None


def finite_code_capacity(
    semiring: SemiringSpec,
    search_limit: int,
) -> int:
    """Largest Delta<=search_limit with injective natural code on 0..Delta."""
    limit = _nonnegative_integer(search_limit, name="search_limit")
    capacity = 0
    for delta in range(limit + 1):
        if not natural_code_injective_through(semiring, delta):
            return delta - 1
        capacity = delta
    return capacity


def boolean_code_capacity() -> int:
    return 1


def modular_code_capacity(modulus: int) -> int:
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 1:
        raise ValueError("modulus must exceed one")
    return modulus - 1


def boolean_modular_code_capacity(modulus: int) -> int:
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 1:
        raise ValueError("modulus must exceed one")
    return modulus


def modular_family_lcm(moduli: Sequence[int]) -> int:
    values = tuple(moduli)
    if not values:
        raise ValueError("moduli must be nonempty")
    result = 1
    for modulus in values:
        if isinstance(modulus, bool) or not isinstance(modulus, int):
            raise TypeError("every modulus must be an integer")
        if modulus <= 1:
            raise ValueError("every modulus must exceed one")
        result = lcm(result, modulus)
    return result


def modular_family_code_capacity(moduli: Sequence[int]) -> int:
    return modular_family_lcm(moduli) - 1


def boolean_modular_family_code_capacity(moduli: Sequence[int]) -> int:
    return modular_family_lcm(moduli)


def product_semiring_family(semirings: Sequence[SemiringSpec]) -> SemiringSpec:
    specs = tuple(semirings)
    if not specs:
        raise ValueError("at least one semiring is required")
    result = specs[0]
    for semiring in specs[1:]:
        result = product_semiring(result, semiring)
    return result


def modular_product_semiring(moduli: Sequence[int]) -> SemiringSpec:
    return product_semiring_family(
        tuple(modular_semiring(modulus) for modulus in moduli)
    )


def boolean_modular_product_semiring(moduli: Sequence[int]) -> SemiringSpec:
    return product_semiring(
        boolean_semiring(),
        modular_product_semiring(moduli),
    )


def _stable_report(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    semiring: SemiringSpec,
) -> SharedSemiringRefinementReport:
    initial = partition_from_observation(states, observation)
    return coarsest_shared_semiring_refinement(
        initial,
        relations,
        (semiring,),
    )


def local_code_exact_branching_theorem(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    semiring: SemiringSpec,
    max_outdegree: int,
) -> bool:
    """Verify exact branching under the declared injective local count code.

    ``max_outdegree`` is an explicit theorem hypothesis.  The caller must supply
    a valid upper bound on every raw action/source outdegree.
    """
    delta = _nonnegative_integer(max_outdegree, name="max_outdegree")
    state_set = set(states)
    if not state_set:
        raise ValueError("states must be nonempty")
    actual = 0
    for relation in relations.values():
        counts = {state: 0 for state in state_set}
        for source, target in relation:
            if source not in state_set or target not in state_set:
                raise ValueError("relation contains state outside declared state set")
            counts[source] += 1
        actual = max(actual, *counts.values())
    if actual > delta:
        raise ValueError("declared max_outdegree is below the actual relation outdegree")
    if not natural_code_injective_through(semiring, delta):
        raise ValueError("local coefficient code is not injective through max_outdegree")

    exact = _stable_report(
        states,
        relations,
        observation,
        natural_semiring(),
    )
    coded = _stable_report(
        states,
        relations,
        observation,
        semiring,
    )
    if exact.steps != coded.steps:
        raise AssertionError("injective local coefficient code failed exact branching theorem")
    return True


def local_code_collision_fixture(
    semiring: SemiringSpec,
    max_outdegree: int,
) -> tuple[
    tuple[str, ...],
    dict[str, Relation],
    Callable[[str], str],
    tuple[int, int],
]:
    """Build a worst-case world from the first code collision in 0..Delta."""
    delta = _nonnegative_integer(max_outdegree, name="max_outdegree")
    collision = first_natural_code_collision(semiring, delta)
    if collision is None:
        raise ValueError("semiring natural code is injective through max_outdegree")
    left_count, right_count = collision
    maximum = max(left_count, right_count)
    targets = tuple(f"t{index}" for index in range(maximum))
    states = ("x", "y") + targets
    edges = {
        ("x", target)
        for target in targets[:left_count]
    }
    edges.update(
        ("y", target)
        for target in targets[:right_count]
    )
    return states, {"a": frozenset(edges)}, lambda _state: "visible", collision


@dataclass(frozen=True)
class LocalCountCodeCapacityReport:
    semiring_name: str
    max_outdegree: int
    injective: bool
    first_collision: tuple[int, int] | None
    code_values: tuple[Coefficient, ...]


def local_count_code_capacity_report(
    semiring: SemiringSpec,
    max_outdegree: int,
) -> LocalCountCodeCapacityReport:
    delta = _nonnegative_integer(max_outdegree, name="max_outdegree")
    values = natural_code_values(semiring, delta)
    collision = first_natural_code_collision(semiring, delta)
    return LocalCountCodeCapacityReport(
        semiring_name=semiring.name,
        max_outdegree=delta,
        injective=collision is None,
        first_collision=collision,
        code_values=values,
    )
