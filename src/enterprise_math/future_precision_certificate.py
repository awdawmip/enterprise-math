"""Typed A3 precision certificates for relation and guard quotient structure.

The certificate intentionally does not scalarize precision. It records:
- relation-state rank / structural quantum / translation period;
- hidden guard rank and quotient free rank;
- Smith invariant factors and finite torsion of the guard quotient module.

A refinement can expose predicate information without lowering hidden guard rank:
finite-index subgroup shrinkage may add torsion detail while rational rank stays
unchanged. This is why one scalar "precision level" is insufficient.
"""

from __future__ import annotations

from dataclasses import dataclass

from .guard_image_lattice import GuardFamily
from .guard_quotient_module import guard_partition_quotient_profile
from .linear_relation_quotient import Partition
from .relation_precision_profile import (
    partition_refines,
    relation_precision_profile,
    relation_refinement_cost,
)


@dataclass(frozen=True)
class A3PrecisionCertificate:
    relation_rank: int
    relation_quantum: int
    relation_translation_period: int
    guard_count: int
    hidden_guard_rank: int
    guard_free_rank: int
    guard_smith_invariant_factors: tuple[int, ...]
    guard_torsion_factors: tuple[int, ...]
    guard_torsion_order: int


@dataclass(frozen=True)
class A3PrecisionRefinement:
    parent: A3PrecisionCertificate
    child: A3PrecisionCertificate
    relation_rank_gain: int
    relation_quantum_factor: int
    hidden_guard_rank_drop: int
    guard_free_rank_gain: int


def a3_precision_certificate(
    fine_capacities: tuple[int, ...],
    guards: GuardFamily,
    partition: Partition,
) -> A3PrecisionCertificate:
    """Return a typed partition precision certificate without scalar weighting."""
    if len(fine_capacities) != len(guards[0]):
        raise ValueError("fine capacities and guard coordinate dimension must match")
    relation_rank, relation_quantum, relation_period = relation_precision_profile(
        fine_capacities, partition
    )
    guard_profile = guard_partition_quotient_profile(guards, partition)
    return A3PrecisionCertificate(
        relation_rank=relation_rank,
        relation_quantum=relation_quantum,
        relation_translation_period=relation_period,
        guard_count=guard_profile.guard_count,
        hidden_guard_rank=guard_profile.hidden_rank,
        guard_free_rank=guard_profile.free_rank,
        guard_smith_invariant_factors=guard_profile.smith_invariant_factors,
        guard_torsion_factors=guard_profile.torsion_factors,
        guard_torsion_order=guard_profile.torsion_order,
    )


def a3_precision_refinement(
    fine_capacities: tuple[int, ...],
    guards: GuardFamily,
    parent_partition: Partition,
    child_partition: Partition,
) -> A3PrecisionRefinement:
    """Compare two typed precision states along an actual partition refinement."""
    if not partition_refines(child_partition, parent_partition):
        raise ValueError("child_partition must refine parent_partition")
    parent = a3_precision_certificate(fine_capacities, guards, parent_partition)
    child = a3_precision_certificate(fine_capacities, guards, child_partition)
    relation_rank_gain, quantum_factor, _, _ = relation_refinement_cost(
        fine_capacities,
        parent_partition,
        child_partition,
    )
    hidden_drop = parent.hidden_guard_rank - child.hidden_guard_rank
    free_gain = child.guard_free_rank - parent.guard_free_rank
    if hidden_drop < 0:
        raise AssertionError("guard hidden rank cannot increase under refinement")
    if free_gain != hidden_drop:
        raise AssertionError("guard quotient free-rank gain must equal hidden-rank drop")
    if hidden_drop > relation_rank_gain:
        raise AssertionError("hidden guard rank cannot drop faster than relation rank is exposed")
    return A3PrecisionRefinement(
        parent=parent,
        child=child,
        relation_rank_gain=relation_rank_gain,
        relation_quantum_factor=quantum_factor,
        hidden_guard_rank_drop=hidden_drop,
        guard_free_rank_gain=free_gain,
    )
