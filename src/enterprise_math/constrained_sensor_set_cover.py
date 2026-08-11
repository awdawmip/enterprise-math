"""Exact Set Cover reduction for constrained modular precision design.

Unrestricted modulus design for a finite integer codebook is easy: choose any
prime larger than every nonzero difference.  Combinatorial hardness appears only
when the available sensor/modulus family is itself constrained.

Given a finite Set Cover instance with universe U and candidate sets S_j, assign
one distinct prime p_j to every candidate sensor.  For each universe element i,
define a contextual two-point codebook

    L_i = {0, d_i},
    d_i = product_{j : i notin S_j} p_j.

A selected prime sensor p_j separates 0 from d_i exactly when p_j does not divide
d_i, which by construction is equivalent to i in S_j.  Hence a selected sensor
family reflects every contextual codebook iff the corresponding candidate sets
cover U.

Therefore minimum-cardinality constrained sensor selection is exactly Minimum
Set Cover on this family, already with:

* prime-only sensors;
* two-point contextual codebooks;
* no weighted transition dynamics at all.

Arbitrary nonnegative sensor costs preserve the same reduction to weighted set
cover.  The module provides exact bounded solvers only as regression/oracle tools;
it does not claim an efficient algorithm for the NP-hard optimization problem.

Set Cover and prime-factor encodings are standard prior mathematics/CS.  The
Enterprise Math value is locating the computational boundary of precision design:
arithmetic reflection is simple once one joint modulus is chosen, while choosing
a minimum subset from a constrained sensor catalogue can already encode arbitrary
covering structure.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import prod
from typing import Hashable, Mapping, Sequence

from .local_law_modulus_design import modular_sensor_family_reflects


Element = Hashable
SensorName = Hashable
Context = Hashable


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def first_primes(count: int) -> tuple[int, ...]:
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        raise ValueError("count must be a nonnegative integer")
    result = []
    candidate = 2
    while len(result) < count:
        if _is_prime(candidate):
            result.append(candidate)
        candidate += 1
    return tuple(result)


def _normalize_instance(
    universe: Sequence[Element],
    candidate_sets: Mapping[SensorName, Sequence[Element] | frozenset[Element]],
) -> tuple[tuple[Element, ...], tuple[SensorName, ...], dict[SensorName, frozenset[Element]]]:
    elements = tuple(universe)
    if len(set(elements)) != len(elements):
        raise ValueError("universe elements must be distinct")
    names = tuple(candidate_sets)
    if len(set(names)) != len(names):
        raise ValueError("candidate sensor names must be distinct")
    universe_set = frozenset(elements)
    normalized: dict[SensorName, frozenset[Element]] = {}
    for name in names:
        values = frozenset(candidate_sets[name])
        if not values.issubset(universe_set):
            raise ValueError("candidate set contains element outside universe")
        normalized[name] = values
    if elements and not names:
        raise ValueError("nonempty universe requires at least one candidate sensor")
    return elements, names, normalized


@dataclass(frozen=True)
class SetCoverSensorEncoding:
    universe: tuple[Element, ...]
    sensor_names: tuple[SensorName, ...]
    sensor_primes: dict[SensorName, int]
    candidate_sets: dict[SensorName, frozenset[Element]]
    contextual_codebooks: dict[Element, frozenset[int]]

    @property
    def sensor_moduli(self) -> tuple[int, ...]:
        return tuple(self.sensor_primes[name] for name in self.sensor_names)


def encode_set_cover_as_modular_sensors(
    universe: Sequence[Element],
    candidate_sets: Mapping[SensorName, Sequence[Element] | frozenset[Element]],
) -> SetCoverSensorEncoding:
    elements, names, normalized = _normalize_instance(universe, candidate_sets)
    primes = first_primes(len(names))
    sensor_primes = {name: prime for name, prime in zip(names, primes, strict=True)}

    codebooks: dict[Element, frozenset[int]] = {}
    for element in elements:
        noncovering_primes = tuple(
            sensor_primes[name]
            for name in names
            if element not in normalized[name]
        )
        difference = prod(noncovering_primes, start=1)
        codebooks[element] = frozenset({0, difference})

    return SetCoverSensorEncoding(
        universe=elements,
        sensor_names=names,
        sensor_primes=sensor_primes,
        candidate_sets=normalized,
        contextual_codebooks=codebooks,
    )


def selected_sets_cover(
    encoding: SetCoverSensorEncoding,
    selected_sensors: Sequence[SensorName],
) -> bool:
    selected = tuple(selected_sensors)
    if len(set(selected)) != len(selected):
        raise ValueError("selected sensors must be distinct")
    if any(name not in encoding.sensor_primes for name in selected):
        raise ValueError("selected sensor is outside encoded catalogue")
    covered = frozenset().union(
        *(encoding.candidate_sets[name] for name in selected),
    ) if selected else frozenset()
    return frozenset(encoding.universe).issubset(covered)


def selected_sensors_reflect_all_codebooks(
    encoding: SetCoverSensorEncoding,
    selected_sensors: Sequence[SensorName],
) -> bool:
    selected = tuple(selected_sensors)
    if len(set(selected)) != len(selected):
        raise ValueError("selected sensors must be distinct")
    if any(name not in encoding.sensor_primes for name in selected):
        raise ValueError("selected sensor is outside encoded catalogue")
    if not encoding.universe:
        return True
    if not selected:
        return False
    moduli = tuple(encoding.sensor_primes[name] for name in selected)
    return modular_sensor_family_reflects(
        encoding.contextual_codebooks,
        moduli,
    )


def reduction_equivalence_holds(
    encoding: SetCoverSensorEncoding,
    selected_sensors: Sequence[SensorName],
) -> bool:
    cover = selected_sets_cover(encoding, selected_sensors)
    reflective = selected_sensors_reflect_all_codebooks(encoding, selected_sensors)
    if cover != reflective:
        raise AssertionError("Set Cover / modular sensor reduction equivalence failed")
    return cover


def element_reflected_by_sensor(
    encoding: SetCoverSensorEncoding,
    element: Element,
    sensor: SensorName,
) -> bool:
    if element not in encoding.contextual_codebooks:
        raise ValueError("element outside encoded universe")
    if sensor not in encoding.sensor_primes:
        raise ValueError("sensor outside encoded catalogue")
    difference = next(
        value for value in encoding.contextual_codebooks[element] if value != 0
    ) if encoding.contextual_codebooks[element] != frozenset({0}) else 0
    prime = encoding.sensor_primes[sensor]
    reflected = difference % prime != 0
    expected = element in encoding.candidate_sets[sensor]
    if reflected != expected:
        raise AssertionError("prime sensor coverage incidence was encoded incorrectly")
    return reflected


def minimum_sensor_cover_exact(
    encoding: SetCoverSensorEncoding,
) -> tuple[SensorName, ...] | None:
    """Exponential exact oracle for bounded tests; returns None if infeasible."""
    if not encoding.universe:
        return ()
    names = encoding.sensor_names
    for size in range(1, len(names) + 1):
        for selected in combinations(names, size):
            if selected_sensors_reflect_all_codebooks(encoding, selected):
                return selected
    return None


def minimum_set_cover_exact(
    encoding: SetCoverSensorEncoding,
) -> tuple[SensorName, ...] | None:
    if not encoding.universe:
        return ()
    names = encoding.sensor_names
    for size in range(1, len(names) + 1):
        for selected in combinations(names, size):
            if selected_sets_cover(encoding, selected):
                return selected
    return None


def minimum_sensor_cardinality_equals_set_cover(
    encoding: SetCoverSensorEncoding,
) -> bool:
    sensors = minimum_sensor_cover_exact(encoding)
    cover = minimum_set_cover_exact(encoding)
    if (sensors is None) != (cover is None):
        raise AssertionError("sensor/cover feasibility mismatch")
    if sensors is None:
        return True
    if len(sensors) != len(cover):
        raise AssertionError("minimum sensor cardinality differs from minimum set cover")
    return True


def _validated_costs(
    encoding: SetCoverSensorEncoding,
    costs: Mapping[SensorName, int | float],
) -> dict[SensorName, float]:
    if set(costs) != set(encoding.sensor_names):
        raise ValueError("cost map must provide exactly one cost per sensor")
    result = {}
    for name, value in costs.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("sensor costs must be numeric")
        if value < 0:
            raise ValueError("sensor costs must be nonnegative")
        result[name] = float(value)
    return result


def minimum_weight_sensor_cover_exact(
    encoding: SetCoverSensorEncoding,
    costs: Mapping[SensorName, int | float],
) -> tuple[tuple[SensorName, ...], float] | None:
    """Exponential weighted oracle used only to verify the reduction."""
    weights = _validated_costs(encoding, costs)
    if not encoding.universe:
        return (), 0.0
    best: tuple[SensorName, ...] | None = None
    best_cost = float("inf")
    names = encoding.sensor_names
    for size in range(len(names) + 1):
        for selected in combinations(names, size):
            if not selected_sensors_reflect_all_codebooks(encoding, selected):
                continue
            cost = sum(weights[name] for name in selected)
            if cost < best_cost:
                best = selected
                best_cost = cost
    if best is None:
        return None
    return best, best_cost


def minimum_weight_set_cover_exact(
    encoding: SetCoverSensorEncoding,
    costs: Mapping[SensorName, int | float],
) -> tuple[tuple[SensorName, ...], float] | None:
    weights = _validated_costs(encoding, costs)
    if not encoding.universe:
        return (), 0.0
    best: tuple[SensorName, ...] | None = None
    best_cost = float("inf")
    names = encoding.sensor_names
    for size in range(len(names) + 1):
        for selected in combinations(names, size):
            if not selected_sets_cover(encoding, selected):
                continue
            cost = sum(weights[name] for name in selected)
            if cost < best_cost:
                best = selected
                best_cost = cost
    if best is None:
        return None
    return best, best_cost


def weighted_reduction_equivalence_holds(
    encoding: SetCoverSensorEncoding,
    costs: Mapping[SensorName, int | float],
) -> bool:
    sensor = minimum_weight_sensor_cover_exact(encoding, costs)
    cover = minimum_weight_set_cover_exact(encoding, costs)
    if (sensor is None) != (cover is None):
        raise AssertionError("weighted sensor/cover feasibility mismatch")
    if sensor is None:
        return True
    if sensor[1] != cover[1]:
        raise AssertionError("minimum weighted sensor cost differs from weighted set cover")
    return True
