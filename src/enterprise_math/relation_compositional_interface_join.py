"""Independent readout joins versus compositional shared-state joins.

For several coefficient-sensitive relation interfaces, two different joins are
possible.

### Independent readout join

Compute each interface's own coarsest stable quotient and intersect the resulting
state partitions.  This is the coarsest state representation from which all final
interface labels can be read independently.

### Compositional shared-state join

Require every interface to remain a well-defined transition structure on one
**shared** quotient state space.  The independent join can fail this stronger
condition because splitting target classes for one interface can make another
interface unsafe again.  Close the independent join under the full interface
family to obtain the true shared-state quotient.

The extra block splits are the **compositional closure debt**: state precision
needed solely because the capabilities must continue to compose on one common
successor state space.

The direct shared closure from the original observation equals the shared closure
started from the independent join.  Thus the workflow

    individual closures -> state join -> compositional repair

is exact.

If one coefficient interface factors through another by a semiring morphism,
the richer interface already guarantees the poorer one on the same target
partition, so their compositional debt is zero.  Positive debt therefore exposes
interaction between capabilities not ordered by the coefficient morphism
preorder (though incomparability alone does not force positive debt on every
world).

Congruence closure and product-interface constructions are standard prior
mathematics/CS.  The project value is isolating the precision tax caused by
cross-capability compositionality.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Mapping, Sequence

from .admissible_support import Relation
from .relation_branching_semiring import (
    SemiringMorphism,
    SemiringSpec,
    joint_partition,
)
from .relation_semiring_stable_refinement import (
    SharedSemiringRefinementReport,
    coarsest_shared_semiring_refinement,
    multi_semiring_relation_stable_on_partition,
)
from .relation_support_stable_refinement import (
    Partition,
    normalize_partition,
    partition_refines,
)


Action = Hashable


def joint_partitions(partitions: Sequence[Partition]) -> Partition:
    values = tuple(partitions)
    if not values:
        raise ValueError("at least one partition is required")
    result = normalize_partition(values[0])
    for partition in values[1:]:
        result = joint_partition(result, normalize_partition(partition))
    return result


@dataclass(frozen=True)
class CompositionalInterfaceJoinReport:
    initial_partition: Partition
    semiring_names: tuple[str, ...]
    individual_final_partitions: tuple[Partition, ...]
    independent_readout_join: Partition
    coupled_final_partition: Partition
    repair_steps_from_independent_join: tuple[Partition, ...]

    @property
    def independent_block_count(self) -> int:
        return len(self.independent_readout_join)

    @property
    def coupled_block_count(self) -> int:
        return len(self.coupled_final_partition)

    @property
    def extra_compositional_blocks(self) -> int:
        return self.coupled_block_count - self.independent_block_count

    @property
    def strict_compositional_repair_steps(self) -> int:
        return len(self.repair_steps_from_independent_join) - 1

    @property
    def has_compositional_debt(self) -> bool:
        return self.extra_compositional_blocks > 0


def compositional_interface_join_report(
    partition: Sequence[Sequence[Hashable] | frozenset[Hashable]],
    relations: Mapping[Action, Relation],
    semirings: Sequence[SemiringSpec],
) -> CompositionalInterfaceJoinReport:
    initial = normalize_partition(partition)
    specs = tuple(semirings)
    if not specs:
        raise ValueError("at least one semiring interface is required")

    individual_reports = tuple(
        coarsest_shared_semiring_refinement(
            initial,
            relations,
            (semiring,),
        )
        for semiring in specs
    )
    independent = joint_partitions(
        tuple(report.final_partition for report in individual_reports)
    )

    repair = coarsest_shared_semiring_refinement(
        independent,
        relations,
        specs,
    )
    direct = coarsest_shared_semiring_refinement(
        initial,
        relations,
        specs,
    )

    if repair.final_partition != direct.final_partition:
        raise AssertionError(
            "shared compositional closure depended on whether individual joins were precomputed"
        )
    if not partition_refines(direct.final_partition, independent):
        raise AssertionError("coupled quotient failed to refine independent readout join")
    if not multi_semiring_relation_stable_on_partition(
        direct.final_partition,
        relations,
        specs,
    ):
        raise AssertionError("coupled final partition is not stable for every interface")

    return CompositionalInterfaceJoinReport(
        initial_partition=initial,
        semiring_names=tuple(semiring.name for semiring in specs),
        individual_final_partitions=tuple(
            report.final_partition for report in individual_reports
        ),
        independent_readout_join=independent,
        coupled_final_partition=direct.final_partition,
        repair_steps_from_independent_join=repair.steps,
    )


def morphism_ordered_pair_has_zero_compositional_debt(
    partition: Sequence[Sequence[Hashable] | frozenset[Hashable]],
    relations: Mapping[Action, Relation],
    morphism: SemiringMorphism,
) -> bool:
    """Verify the no-debt theorem for a declared coefficient factor map."""
    report = compositional_interface_join_report(
        partition,
        relations,
        (morphism.source, morphism.target),
    )
    source_final = report.individual_final_partitions[0]
    target_final = report.individual_final_partitions[1]
    if not partition_refines(source_final, target_final):
        raise AssertionError("source coefficient interface failed to refine its morphic target")
    if report.independent_readout_join != source_final:
        raise AssertionError("independent join exceeded the morphism-dominating source quotient")
    if report.coupled_final_partition != source_final:
        raise AssertionError("morphism-ordered interface pair unexpectedly acquired closure debt")
    if report.has_compositional_debt:
        raise AssertionError("morphism-ordered interface pair reported positive debt")
    return True
