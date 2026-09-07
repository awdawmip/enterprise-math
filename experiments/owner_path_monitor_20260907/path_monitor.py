"""Finite native-X6 path monitor, BRC histogram, and port-composition consumer.

Reuses WBRC-T33..T37 carriers and T6. Excursions have positive length and no
interior port. Only complete results certify coefficients through the declared
horizon. Budget exhaustion preserves partial evidence without a zero/no-path
claim. No convergence, unbounded closure, or complexity theorem is asserted.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from enterprise_math.brc_histogram import WeightHistogram, histogram_recoalesce, histogram_serial
from enterprise_math.operation_quotient import class_count, family_future_partition_sequence


START = 0
HIT = "HIT"
ALPHABET = tuple(range(1, 7)) + tuple(range(-1, -7, -1))
MONITOR_STATES = (START,) + ALPHABET + (HIT,)
ZERO = WeightHistogram.from_weights(())
ONE = WeightHistogram.from_weights([1])
# source port, target port, length, initial monitor, final monitor
CoefficientKey = tuple[str, str, int, int | str, int | str]


def _label(value, name):
    if not isinstance(value, str) or not value:
        raise ValueError(f"{name} must be a nonempty string")
    return value


def _nonnegative(value, name):
    if type(value) is not int or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def _monitor_state(value):
    return (type(value) is int and value in (START,) + ALPHABET) or (type(value) is str and value == HIT)


@dataclass(frozen=True)
class Node:
    label: str
    coordinate: tuple[int, ...]

    def __post_init__(self):
        _label(self.label, "node label")
        coordinate = tuple(self.coordinate)
        if len(coordinate) != 6 or any(type(value) is not int for value in coordinate):
            raise ValueError("node coordinates must be six raw signed integers")
        object.__setattr__(self, "coordinate", coordinate)


@dataclass(frozen=True)
class Edge:
    label: str
    source: str
    target: str
    step: int
    weight: Fraction = Fraction(1)

    def __post_init__(self):
        for value, name in ((self.label, "edge label"), (self.source, "source"), (self.target, "target")):
            _label(value, name)
        if type(self.step) is not int or self.step not in ALPHABET:
            raise ValueError("edge step must be one of the twelve signed primitive axes +/-1..6")
        if isinstance(self.weight, bool) or not isinstance(self.weight, (int, Fraction)):
            raise TypeError("edge weights must be exact int or Fraction")
        if self.weight <= 0:
            raise ValueError("edge weights must be positive")
        object.__setattr__(self, "weight", Fraction(self.weight))


@dataclass(frozen=True)
class NativeGraph:
    nodes: tuple[Node, ...]
    edges: tuple[Edge, ...]

    def __post_init__(self):
        nodes, edges = tuple(self.nodes), tuple(self.edges)
        if not nodes or not all(isinstance(node, Node) for node in nodes):
            raise ValueError("a graph needs a nonempty sequence of Node values")
        if not all(isinstance(edge, Edge) for edge in edges):
            raise TypeError("graph edges must be Edge values")
        nodes = tuple(Node(node.label, node.coordinate) for node in nodes)
        edges = tuple(Edge(edge.label, edge.source, edge.target, edge.step, edge.weight) for edge in edges)
        if len({node.label for node in nodes}) != len(nodes) or len({edge.label for edge in edges}) != len(edges):
            raise ValueError("node labels and edge labels must each be unique")
        coordinates = {node.label: node.coordinate for node in nodes}
        for edge in edges:
            if edge.source not in coordinates or edge.target not in coordinates:
                raise ValueError("edge endpoint label is missing from graph nodes")
            difference = tuple(b - a for a, b in zip(coordinates[edge.source], coordinates[edge.target]))
            expected = tuple((1 if edge.step > 0 else -1) if i == abs(edge.step) - 1 else 0 for i in range(6))
            if difference != expected:
                raise ValueError(f"edge {edge.label} coordinate difference is not its declared signed primitive step")
        object.__setattr__(self, "nodes", nodes)
        object.__setattr__(self, "edges", edges)


@dataclass(frozen=True)
class ReverseStepMonitor:
    states: tuple
    operations: Mapping
    partition_sizes: tuple[int, ...]

    def advance(self, state, step):
        if not _monitor_state(state):
            raise ValueError("invalid monitor state")
        if type(step) is not int or step not in ALPHABET:
            raise ValueError("invalid signed primitive step")
        return self.operations[step][state]


def reverse_step_monitor() -> ReverseStepMonitor:
    """T6 verifies the 14-state monitor's coarsest all-suffix partition."""
    operations = {
        step: {state: HIT if state == HIT or state == -step else step for state in MONITOR_STATES}
        for step in ALPHABET
    }
    stages = family_future_partition_sequence(
        MONITOR_STATES, operations, {state: state == HIT for state in MONITOR_STATES}
    )
    sizes = tuple(class_count(stage) for stage in stages)
    if sizes != (2, 14):
        raise ArithmeticError("T6 did not certify the declared 14-state monitor")
    frozen = MappingProxyType({step: MappingProxyType(operation) for step, operation in operations.items()})
    return ReverseStepMonitor(MONITOR_STATES, frozen, sizes)


@dataclass(frozen=True)
class PathWitness:
    source: str
    target: str
    edge_labels: tuple[str, ...]
    word: tuple[int, ...]
    weight: Fraction


@dataclass(frozen=True)
class SeriesResult:
    """Public result container; a COMPLETE label is not an independent proof.

    External or persisted instances require verify_port_series against the
    independently declared graph/ports/horizon before relying on coefficients.
    """
    kind: str
    graph: NativeGraph
    ports: tuple[str, ...]
    horizon: int
    status: str
    complete_through: int
    coefficients: Mapping[CoefficientKey, WeightHistogram]
    budget_used: int
    budget_limit: int
    budget_unit: str
    reason: str = ""
    witnesses: tuple[PathWitness, ...] = ()

    @property
    def complete(self):
        return self.status == "COMPLETE"


class _BudgetExhausted(Exception):
    pass


class _Budget:
    def __init__(self, limit):
        self.limit = _nonnegative(limit, "budget")
        self.used = 0

    def consume(self, amount):
        if self.used + amount > self.limit:
            raise _BudgetExhausted
        self.used += amount


def _inputs(graph, ports, horizon):
    if not isinstance(graph, NativeGraph):
        raise TypeError("expected NativeGraph")
    ports = tuple(ports)
    node_labels = {node.label for node in graph.nodes}
    if not ports or any(not isinstance(port, str) or port not in node_labels for port in ports):
        raise ValueError("ports must be a nonempty selection of existing node labels")
    if len(set(ports)) != len(ports):
        raise ValueError("port labels must be distinct")
    _nonnegative(horizon, "horizon")
    adjacent = {node.label: [] for node in graph.nodes}
    for edge in graph.edges:
        adjacent[edge.source].append(edge)
    return ports, adjacent


def _add(mapping, key, histogram):
    mapping[key] = histogram_recoalesce(mapping.get(key, ZERO), histogram)


def _finish(kind, graph, ports, horizon, complete, complete_through, coefficients, budget, unit, witnesses=()):
    # Both histogram container levels are independently frozen and validated.
    frozen = {key: WeightHistogram(tuple(tuple(entry) for entry in histogram.entries))
              for key, histogram in coefficients.items()}
    return SeriesResult(kind, graph, ports, horizon, "COMPLETE" if complete else "INCOMPLETE",
                        complete_through, MappingProxyType(frozen), budget.used, budget.limit, unit,
                        "" if complete else "budget exhausted; later or partially accumulated coefficients are not complete",
                        tuple(witnesses))


def port_excursion_series(graph: NativeGraph, ports, horizon: int, *, budget: int = 1000000) -> SeriesResult:
    """Product graph first: positive-length first-port-return coefficients.

    Each key retains BOTH monitor endpoints. Internal routing nodes may share
    spatial coordinates, but remain distinct graph states. No zero excursion.
    """
    ports, adjacent = _inputs(graph, ports, horizon)
    meter = _Budget(budget)
    monitor = reverse_step_monitor()
    frontier = {(port, initial, port, initial): ONE for port in ports for initial in MONITOR_STATES}
    coefficients = {}
    completed = 0
    try:
        for length in range(1, horizon + 1):
            next_frontier = {}
            for (source, initial, node, state), prefix in frontier.items():
                for edge in adjacent[node]:
                    meter.consume(len(prefix.entries))
                    final = monitor.advance(state, edge.step)
                    weighted = histogram_serial(prefix, WeightHistogram.from_weights([edge.weight]))
                    if edge.target in ports:
                        _add(coefficients, (source, edge.target, length, initial, final), weighted)
                    else:
                        _add(next_frontier, (source, initial, edge.target, final), weighted)
            frontier = next_frontier
            completed = length
            if not frontier:
                completed = horizon
                break
    except _BudgetExhausted:
        return _finish("EXCURSIONS", graph, ports, horizon, False, completed, coefficients, meter,
                       "histogram-product terms")
    return _finish("EXCURSIONS", graph, ports, horizon, True, horizon, coefficients, meter,
                   "histogram-product terms")


def compose_port_series(excursions: SeriesResult, *, budget: int = 1000000) -> SeriesResult:
    """Finite K_0=I, K_n=sum_{l=1}^n K_{n-l} E_l; monitor boundary is matched.

    Incomplete input is refused. E has no degree-zero terms, preventing the
    spurious infinity that would result from repeated empty excursions.
    """
    if (not isinstance(excursions, SeriesResult) or excursions.kind != "EXCURSIONS" or not excursions.complete
        or excursions.complete_through != excursions.horizon):
        raise ValueError("composition requires a COMPLETE excursion series")
    graph, ports, horizon = excursions.graph, excursions.ports, excursions.horizon
    _inputs(graph, ports, horizon)
    meter = _Budget(budget)
    index = {}
    for (source, target, length, initial, final), histogram in excursions.coefficients.items():
        if type(length) is not int or not 1 <= length <= horizon:
            raise ValueError("excursions must have strictly positive length within horizon")
        if source not in ports or target not in ports or not _monitor_state(initial) or not _monitor_state(final):
            raise ValueError("excursion coefficient uses an undeclared port or monitor state")
        index.setdefault((length, source, initial), []).append((target, final, histogram))
    layers = [{(port, port, initial, initial): ONE for port in ports for initial in MONITOR_STATES}]
    coefficients = {(port, port, 0, initial, initial): ONE for port in ports for initial in MONITOR_STATES}
    completed = 0
    try:
        for length in range(1, horizon + 1):
            layer = {}
            for excursion_length in range(1, length + 1):
                for (source, middle, initial, boundary), prefix in layers[length - excursion_length].items():
                    for target, final, suffix in index.get((excursion_length, middle, boundary), ()):
                        meter.consume(len(prefix.entries) * len(suffix.entries))
                        weighted = histogram_serial(prefix, suffix)
                        _add(layer, (source, target, initial, final), weighted)
                        _add(coefficients, (source, target, length, initial, final), weighted)
            layers.append(layer)
            completed = length
    except _BudgetExhausted:
        return _finish("WALKS", graph, ports, horizon, False, completed, coefficients, meter,
                       "histogram-product terms")
    return _finish("WALKS", graph, ports, horizon, True, horizon, coefficients, meter,
                   "histogram-product terms")


def _scan_word(initial, word):
    """Independent explicit-word observation; no use of monitor transitions."""
    if initial == HIT:
        return HIT
    tested = word if initial == START else (initial,) + word
    if any(left == -right for left, right in zip(tested, tested[1:])):
        return HIT
    return word[-1] if word else initial


def enumerate_port_walks(graph: NativeGraph, ports, horizon: int, *, budget: int = 1000000) -> SeriesResult:
    """Independent finite path enumeration retaining edge words and weights."""
    ports, adjacent = _inputs(graph, ports, horizon)
    meter = _Budget(budget)
    frontier = [PathWitness(port, port, (), (), Fraction(1)) for port in ports]
    witnesses = list(frontier)
    buckets = {(port, port, 0, initial, initial): [Fraction(1)] for port in ports for initial in MONITOR_STATES}
    completed = 0

    def finish(complete):
        coefficients = {key: WeightHistogram.from_weights(weights) for key, weights in buckets.items()}
        return _finish("ENUMERATED_WALKS", graph, ports, horizon, complete,
                       horizon if complete else completed, coefficients, meter, "individual path-edge extensions", witnesses)

    try:
        for length in range(1, horizon + 1):
            next_frontier = []
            for prefix in frontier:
                for edge in adjacent[prefix.target]:
                    meter.consume(1)
                    path = PathWitness(prefix.source, edge.target, prefix.edge_labels + (edge.label,),
                                       prefix.word + (edge.step,), prefix.weight * edge.weight)
                    next_frontier.append(path)
                    if edge.target in ports:
                        witnesses.append(path)
                        for initial in MONITOR_STATES:
                            key = (path.source, path.target, length, initial, _scan_word(initial, path.word))
                            buckets.setdefault(key, []).append(path.weight)
            frontier = next_frontier
            completed = length
            if not frontier:
                break
    except _BudgetExhausted:
        return finish(False)
    return finish(True)


def coefficient(series: SeriesResult, source, target, length, initial=START, final=None):
    """Convenience readout of a computed result; final=None forgets final state.

    Partial result mappings remain accessible for diagnosis, but this readout
    refuses them even when an individual missing key might appear to be zero.
    COMPLETE is a container label, not independent validation: external or
    persisted input must first pass verify_port_series against its actual scope.
    """
    if not series.complete or series.complete_through != series.horizon:
        raise ValueError("an INCOMPLETE series cannot supply a complete coefficient readout")
    if source not in series.ports or target not in series.ports:
        raise ValueError("undeclared port label")
    if type(length) is not int or not 0 <= length <= series.horizon:
        raise ValueError("coefficient length is outside the declared horizon")
    if not _monitor_state(initial):
        raise ValueError("invalid initial monitor state")
    if final is not None and not _monitor_state(final):
        raise ValueError("invalid final monitor state")
    result = ZERO
    for state in MONITOR_STATES if final is None else (final,):
        result = histogram_recoalesce(result, series.coefficients.get((source, target, length, initial, state), ZERO))
    return result


def verify_port_series(graph: NativeGraph, ports, horizon: int, series: SeriesResult,
                       *, enumeration_budget: int = 1000000) -> dict:
    """Bind full monitor coefficients to independently declared finite inputs.

    Supports WALKS and ENUMERATED_WALKS only. Fresh explicit path enumeration
    uses direct word scanning, not the product-monitor transitions or supplied
    witnesses. Enumeration exhaustion is UNVERIFIED, never a successful proof.
    Supplied runtime metadata and supplied provenance witnesses are not audited;
    the VERIFIED scope is the complete coefficient family on graph/ports/horizon.
    """
    ports, _ = _inputs(graph, ports, horizon)
    _nonnegative(enumeration_budget, "enumeration_budget")
    if not isinstance(series, SeriesResult):
        return {"status": "REJECTED", "reason": "expected a SeriesResult container"}
    if (type(series.horizon) is not int or series.graph != graph
        or not isinstance(series.ports, tuple) or series.ports != ports or series.horizon != horizon):
        return {"status": "REJECTED", "reason": "graph/frame, ordered ports, or horizon do not match declared inputs"}
    if series.kind not in ("WALKS", "ENUMERATED_WALKS"):
        return {"status": "UNVERIFIED", "reason": "independent verifier supports complete WALKS/ENUMERATED_WALKS only; EXCURSIONS unsupported"}
    if (series.status != "COMPLETE" or type(series.complete_through) is not int
        or series.complete_through != horizon):
        return {"status": "UNVERIFIED", "reason": "supplied series is incomplete or has an inconsistent completion horizon"}
    if not isinstance(series.coefficients, Mapping):
        return {"status": "REJECTED", "reason": "coefficients must be a finite mapping"}
    copied = {}
    try:
        for key, histogram in series.coefficients.items():
            if not isinstance(key, tuple) or len(key) != 5:
                return {"status": "REJECTED", "reason": "malformed coefficient key"}
            source, target, length, initial, final = key
            if (source not in ports or target not in ports or type(length) is not int
                or not 0 <= length <= horizon or not _monitor_state(initial) or not _monitor_state(final)):
                return {"status": "REJECTED", "reason": "coefficient key is outside the declared port/length/monitor scope"}
            if not isinstance(histogram, WeightHistogram):
                return {"status": "REJECTED", "reason": "coefficient must be a WeightHistogram"}
            # Revalidate base semantics and freeze mutable inner pairs as well.
            exact = WeightHistogram(tuple(tuple(entry) for entry in histogram.entries))
            if not exact.is_zero:
                copied[key] = exact
    except (TypeError, ValueError, AttributeError):
        return {"status": "REJECTED", "reason": "malformed exact histogram coefficient"}
    enumerated = enumerate_port_walks(graph, ports, horizon, budget=enumeration_budget)
    if not enumerated.complete:
        return {"status": "UNVERIFIED", "reason": "independent enumeration budget exhausted",
                "enumeration_status": enumerated.status,
                "complete_through": enumerated.complete_through,
                "enumeration_budget_used": enumerated.budget_used}
    expected = enumerated.coefficients
    mismatches = []
    for key in dict.fromkeys(tuple(expected) + tuple(copied)):
        left, right = expected.get(key, ZERO), copied.get(key, ZERO)
        if left != right:
            mismatches.append({"key": key, "expected": left, "supplied": right})
    if mismatches:
        return {"status": "REJECTED", "reason": "supplied coefficients disagree with fresh explicit path enumeration",
                "enumeration_status": "COMPLETE", "mismatches": tuple(mismatches)}
    return {"status": "VERIFIED", "reason": "complete monitor coefficients match fresh explicit path enumeration",
            "scope": "declared graph/frame, ordered ports, horizon and all monitor coefficient blocks",
            "enumeration_status": "COMPLETE", "checked_nonzero_blocks": len(expected),
            "provided_runtime_metadata_and_witnesses_verified": False,
            "verified_series": enumerated}
