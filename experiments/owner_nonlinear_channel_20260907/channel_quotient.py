"""Finite gate witnesses for the six-channel mass quotient theorem.

A gate links two inputs with the same A_i image. It is not a directed path
from one input to the other. Universal quotient constancy is proved in the
associated note, not by a finite verification status.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import importlib.util
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
GEOMETRY_SOURCE = ROOT / "research_notes/owner_geometry_20260907_check.py"
GEOMETRY_SHA256 = "d92a45acb9c455b88a3786ce99ae919cbfbd5a0b09b55ce3dfeb6b39b633c4a7"

if hashlib.sha256(GEOMETRY_SOURCE.read_bytes()).hexdigest() != GEOMETRY_SHA256:
    raise RuntimeError("the reused geometry consumer bytes changed")
sys.dont_write_bytecode = True
_spec = importlib.util.spec_from_file_location("nonlinear_reused_geometry", GEOMETRY_SOURCE)
geometry = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(geometry)

from enterprise_math.operation_quotient import operation_descends

Vector = tuple[Fraction, ...]


def channel_vector(value, *, strictly_positive=False) -> Vector:
    if type(strictly_positive) is not bool:
        raise TypeError("strictly_positive must be bool")
    if type(value) not in (tuple, list) or len(value) != 6:
        raise ValueError("expected exactly six channel masses")
    if any(type(v) not in (int, Fraction) for v in value):
        raise TypeError("channel masses must be exact int or Fraction, never bool/float")
    result = tuple(Fraction(v) for v in value)
    if any(v <= 0 if strictly_positive else v < 0 for v in result):
        raise ValueError("channel mass is outside the declared rational cone")
    return result


def _channel(index):
    if type(index) is not int or not 0 <= index < 6:
        raise ValueError("channel index must be an integer from 0 to 5")
    return index


def gate_image(vector, gate, *, strictly_positive=False) -> Vector:
    """Recompute using the original geometry matrix, not stored witness data."""
    v = channel_vector(vector, strictly_positive=strictly_positive)
    matrix = geometry.kernel(_channel(gate))
    return tuple(sum((matrix[d][c] * v[c] for c in range(6)), Fraction(0))
                 for d in range(6))


@dataclass(frozen=True)
class GateStep:
    before: Vector
    after: Vector
    donor: int
    receiver: int
    amount: Fraction
    gate: int


@dataclass(frozen=True)
class GateWitness:
    source: Vector
    target: Vector
    steps: tuple[GateStep, ...]


@dataclass(frozen=True)
class Verification:
    status: str
    reason: str
    steps_checked: int


def make_gate_witness(source, target, *, strictly_positive=False) -> GateWitness:
    """At most five rational donor-to-receiver transfers at equal total mass."""
    x = channel_vector(source, strictly_positive=strictly_positive)
    y = channel_vector(target, strictly_positive=strictly_positive)
    if sum(x) != sum(y):
        raise ValueError("gate witnesses require equal total mass")
    current, steps = x, []
    while current != y:
        donor = next(i for i in range(6) if current[i] > y[i])
        receiver = next(i for i in range(6) if current[i] < y[i])
        amount = min(current[donor] - y[donor], y[receiver] - current[receiver])
        after = list(current)
        after[donor] -= amount
        after[receiver] += amount
        following = tuple(after)
        gate = next(i for i in range(6) if i not in (donor, receiver))
        steps.append(GateStep(current, following, donor, receiver, amount, gate))
        current = following
    if len(steps) > 5:
        raise AssertionError("the six-channel transfer bound failed")
    return GateWitness(x, y, tuple(steps))


def verify_gate_witness(source, target, witness, *, strictly_positive=False) -> Verification:
    """Bind both endpoints and independently check every exact matrix gate.

    VALID certifies this finite chain only. It does not evaluate an arbitrary
    q, establish its injective-descendant contract, or prove that contract.
    """
    checked = 0
    try:
        x = channel_vector(source, strictly_positive=strictly_positive)
        y = channel_vector(target, strictly_positive=strictly_positive)
        if type(witness) is not GateWitness or type(witness.steps) is not tuple:
            raise ValueError("malformed witness type")
        if type(witness.source) is not tuple or type(witness.target) is not tuple:
            raise ValueError("witness endpoints must be immutable tuples")
        if channel_vector(witness.source, strictly_positive=strictly_positive) != x:
            raise ValueError("source binding mismatch")
        if channel_vector(witness.target, strictly_positive=strictly_positive) != y:
            raise ValueError("target binding mismatch")
        if sum(x) != sum(y) or len(witness.steps) > 5:
            raise ValueError("total mass or step bound mismatch")
        current = x
        for step in witness.steps:
            if type(step) is not GateStep or type(step.before) is not tuple or type(step.after) is not tuple:
                raise ValueError("malformed step type")
            before = channel_vector(step.before, strictly_positive=strictly_positive)
            after = channel_vector(step.after, strictly_positive=strictly_positive)
            if before != current:
                raise ValueError("broken chain adjacency")
            donor, receiver, gate = map(_channel, (step.donor, step.receiver, step.gate))
            if donor == receiver or gate in (donor, receiver):
                raise ValueError("gate must be outside the two changed channels")
            if type(step.amount) not in (int, Fraction) or step.amount <= 0:
                raise ValueError("transfer amount must be a positive exact rational")
            expected = list(before)
            expected[donor] -= step.amount
            expected[receiver] += step.amount
            if tuple(expected) != after:
                raise ValueError("stored transfer does not match the two-channel operation")
            if sum(before) != sum(after) or before[gate] != after[gate]:
                raise ValueError("total mass or fixed-gate coordinate changed")
            if gate_image(before, gate) != gate_image(after, gate):
                raise ValueError("original A_i matrix images differ")
            current = after
            checked += 1
        if current != y:
            raise ValueError("the finite chain does not reach the bound target")
        return Verification("VALID", "exact endpoint-bound gate chain", checked)
    except (ValueError, TypeError, AttributeError) as error:
        return Verification("INVALID", str(error), checked)


def brc_gate_observation(vector, gate):
    """One positive input branch per nonzero channel; retain resulting history.

    This is a declared lift of a mass vector, not recovery of arbitrary erased
    microscopic branch data. The empty vector lift has no branches.
    """
    v = channel_vector(vector)
    gate = _channel(gate)
    branches = []
    for channel, mass in enumerate(v):
        if mass:
            for target, history, state in geometry.paths(channel, (gate,)):
                branches.append((target, history,
                    geometry.cwm_propagate(geometry.cwm_edge(mass), state)))
    return geometry.observe(branches)


def finite_gate_descent_check(inputs, gate, observer):
    """Actual T6 call on a finite closed single-gate domain, not the whole cone."""
    gate = _channel(gate)
    seed = tuple(channel_vector(v) for v in inputs)
    if not seed:
        raise ValueError("need at least one finite input")
    domain = tuple(dict.fromkeys(seed + tuple(gate_image(v, gate) for v in seed)))
    operation = {v: gate_image(v, gate) for v in domain}
    if any(v not in domain for v in operation.values()):
        raise AssertionError("the idempotent single-gate domain did not close")
    partition = {v: observer(v) for v in domain}
    return operation_descends(domain, operation, partition)
