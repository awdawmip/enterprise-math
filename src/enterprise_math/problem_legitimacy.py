"""Finite structural certificates for Problem Legitimacy.

This is a thin diagnostic layer over canonical A2/P023 factorization utilities.
A declared finite task is represented by an exact signature ``Sigma : X -> S``.
The current partition is safe exactly when ``Sigma`` is constant on each fiber.

The module adds reusable certificates for semantic erasure, finite joint
signature families, finite distinguishing bases, and rejection of non-equivalence
"same enough" relations. Generic quotient/factorization, partition refinement,
and finite distinguishing-family mathematics are prior art.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable, Iterable, Mapping
from dataclasses import dataclass
from typing import TypeVar

from .composition_safe_collapse import (
    canonical_class_ids,
    coarsest_one_step_repair,
    descends_through,
    fiber_constancy_witness,
    refines,
)

State = TypeVar("State", bound=Hashable)
SignatureName = TypeVar("SignatureName", bound=Hashable)


def _states(domain: Iterable[State]) -> tuple[State, ...]:
    states = tuple(domain)
    if not states:
        raise ValueError("domain must be nonempty")
    if len(states) != len(set(states)):
        raise ValueError("domain states must be distinct")
    return states


def _require_total(
    states: tuple[State, ...], mapping: Mapping[State, Hashable], name: str
) -> None:
    if set(mapping) != set(states):
        raise ValueError(f"{name} must label every state exactly once")


def partitions_equivalent(
    domain: Iterable[State],
    left: Mapping[State, Hashable],
    right: Mapping[State, Hashable],
) -> bool:
    """Equality of induced equivalence relations, ignoring class labels."""
    states = _states(domain)
    return refines(states, left, right) and refines(states, right, left)


def signature_descends(
    domain: Iterable[State],
    current_partition: Mapping[State, Hashable],
    signature: Mapping[State, Hashable],
) -> bool:
    """Whether the exact task signature is a function of the current state."""
    return descends_through(domain, current_partition, signature)


def coarsest_static_repair(
    domain: Iterable[State],
    current_partition: Mapping[State, Hashable],
    signature: Mapping[State, Hashable],
) -> dict[State, int]:
    """Coarsest refinement making one exact task signature state-defined."""
    return coarsest_one_step_repair(domain, current_partition, signature)


@dataclass(frozen=True)
class SignatureReport:
    """Exact finite descent status plus the coarsest static repair."""

    valid_now: bool
    witness: tuple[Hashable, Hashable] | None
    current_class_count: int
    required_class_count: int
    repaired_partition: dict[Hashable, int]


def analyze_signature(
    domain: Iterable[State],
    current_partition: Mapping[State, Hashable],
    signature: Mapping[State, Hashable],
) -> SignatureReport:
    """Audit one exact task signature against the current finite partition."""
    states = _states(domain)
    _require_total(states, current_partition, "current partition")
    _require_total(states, signature, "signature")
    witness = fiber_constancy_witness(states, current_partition, signature)
    repair = coarsest_one_step_repair(states, current_partition, signature)
    return SignatureReport(
        valid_now=descends_through(states, current_partition, signature),
        witness=witness,
        current_class_count=len(set(current_partition.values())),
        required_class_count=len(set(repair.values())),
        repaired_partition=dict(repair),
    )


@dataclass(frozen=True)
class ErasureReport:
    """Whether a proposed post-summary preserves the rich semantic kernel."""

    lossless: bool
    witness: tuple[Hashable, Hashable] | None
    rich_class_count: int
    summary_class_count: int


def semantic_erasure_report(
    domain: Iterable[State],
    rich_signature: Mapping[State, Hashable],
    summary_signature: Mapping[State, Hashable],
) -> ErasureReport:
    """Check exact-kernel preservation for a proposed semantic summary.

    ``summary_signature`` must be a genuine post-summary of ``rich_signature``:
    equal rich values may not be split by the summary. Losslessness then means
    the summary also never merges distinct rich values.
    """
    states = _states(domain)
    _require_total(states, rich_signature, "rich signature")
    _require_total(states, summary_signature, "summary signature")
    if not refines(states, rich_signature, summary_signature):
        raise ValueError("summary signature must be a post-summary of the rich signature")
    witness = fiber_constancy_witness(states, summary_signature, rich_signature)
    return ErasureReport(
        lossless=witness is None,
        witness=witness,
        rich_class_count=len(set(rich_signature.values())),
        summary_class_count=len(set(summary_signature.values())),
    )


def joint_signature_partition(
    domain: Iterable[State],
    signatures: Mapping[SignatureName, Mapping[State, Hashable]],
) -> dict[State, int]:
    """Partition states by the tuple of all named finite task signatures."""
    states = _states(domain)
    for name, signature in signatures.items():
        _require_total(states, signature, f"signature {name!r}")
    names = tuple(signatures)
    labels = {
        state: tuple(signatures[name][state] for name in names) for state in states
    }
    return canonical_class_ids(states, labels)


@dataclass(frozen=True)
class SignatureBasisReport:
    """One finite subfamily inducing the full joint signature kernel."""

    names: tuple[Hashable, ...]
    final_class_count: int


def finite_signature_basis(
    domain: Iterable[State],
    signatures: Mapping[SignatureName, Mapping[State, Hashable]],
) -> SignatureBasisReport:
    """Greedily extract a kernel-equivalent subfamily with at most ``k-1`` names.

    Here ``k`` is the number of classes induced by the full finite family. This
    is an existence certificate, not a minimum-cardinality Test-Cover solver.
    """
    states = _states(domain)
    for name, signature in signatures.items():
        _require_total(states, signature, f"signature {name!r}")
    full = joint_signature_partition(states, signatures)
    target_count = len(set(full.values()))
    chosen: list[SignatureName] = []
    current = {state: 0 for state in states}

    while not partitions_equivalent(states, current, full):
        current_count = len(set(current.values()))
        for name, signature in signatures.items():
            if name in chosen:
                continue
            trial_names = (*chosen, name)
            trial = joint_signature_partition(
                states, {key: signatures[key] for key in trial_names}
            )
            if len(set(trial.values())) > current_count:
                chosen.append(name)
                current = trial
                break
        else:
            raise AssertionError("full signature family failed to supply a needed split")
        if len(chosen) > target_count - 1:
            raise AssertionError("finite signature basis exceeded the k-1 class bound")

    return SignatureBasisReport(tuple(chosen), target_count)


@dataclass(frozen=True)
class EquivalenceFailure:
    """First failure of reflexivity, symmetry, or transitivity."""

    law: str
    witness: tuple[Hashable, ...]


def equivalence_failure_witness(
    domain: Iterable[State],
    relation: Callable[[State, State], bool],
) -> EquivalenceFailure | None:
    """Reject a candidate tolerance/proximity relation that is not a quotient."""
    states = _states(domain)
    for x in states:
        if not relation(x, x):
            return EquivalenceFailure("reflexivity", (x,))
    for x in states:
        for y in states:
            if relation(x, y) != relation(y, x):
                return EquivalenceFailure("symmetry", (x, y))
    for x in states:
        for y in states:
            if not relation(x, y):
                continue
            for z in states:
                if relation(y, z) and not relation(x, z):
                    return EquivalenceFailure("transitivity", (x, y, z))
    return None
