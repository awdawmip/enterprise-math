"""Modulus-lattice laws for semiring branching relation precision.

For modular count coefficients, divisibility again gives the natural arithmetic
precision order, but the structural branching interface changes how joins are
realized.

For M,N>=2 and L=lcm(M,N), the map

    Z/LZ -> Z/MZ x Z/NZ,
    r |-> (r mod M, r mod N)

is an injective semiring homomorphism onto the compatible residue pairs.  Hence
mod-L branching is equivalent to product-semiring branching and therefore to
the **coupled compositional join** of mod-M and mod-N branching interfaces.

The ordinary state join of the two independently stable modular quotients may be
coarser: it need not remain transition-stable after target classes are jointly
refined.  The difference is compositional closure debt.

At terminal word-count trace level, however, no successor-type correlation is
retained.  Pairing a mod-M trace with a mod-N trace is coefficientwise exactly
mod-L information, so the independent terminal-trace join equals the mod-L
trace partition with no additional structural closure.

Thus the same arithmetic lcm supports two different semantic roles:

* terminal count traces: lcm is already the independent readout join;
* branching operations: lcm is the coupled/compositional join and may be finer
  than the independent state-label join.

CRT, modular semirings and weighted transition systems are standard prior
mathematics/CS.  The project value is the exact interaction between arithmetic
precision lattice and structural continuation semantics.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, lcm
from typing import Callable, Hashable, Mapping, Sequence

from .admissible_support import Relation
from .relation_branching_semiring import (
    SemiringMorphism,
    joint_partition,
    modular_semiring,
    morphism_commutes_with_branching_construction,
    product_semiring,
    raw_semiring_word_trace,
    semiring_branching_partition,
    verify_semiring_morphism,
    words_through_horizon,
)
from .relation_compositional_interface_join import (
    CompositionalInterfaceJoinReport,
    compositional_interface_join_report,
)
from .relation_semiring_stable_refinement import (
    coarsest_shared_semiring_refinement,
)
from .relation_support_stable_refinement import (
    Partition,
    normalize_partition,
    partition_from_observation,
    partition_refines,
)


State = Hashable
Action = Hashable
Observation = Hashable


def _modulus(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value <= 1:
        raise ValueError(f"{name} must exceed one")
    return value


def modular_reduction_morphism(
    fine_modulus: int,
    coarse_modulus: int,
) -> SemiringMorphism:
    fine = _modulus(fine_modulus, name="fine_modulus")
    coarse = _modulus(coarse_modulus, name="coarse_modulus")
    if fine % coarse != 0:
        raise ValueError("coarse modulus must divide fine modulus")
    return SemiringMorphism(
        name=f"mod-{fine}-to-mod-{coarse}",
        source=modular_semiring(fine),
        target=modular_semiring(coarse),
        map_value=lambda value: int(value) % coarse,
    )


def modular_lcm_pair_morphism(
    left_modulus: int,
    right_modulus: int,
) -> SemiringMorphism:
    left = _modulus(left_modulus, name="left_modulus")
    right = _modulus(right_modulus, name="right_modulus")
    common = lcm(left, right)
    left_semiring = modular_semiring(left)
    right_semiring = modular_semiring(right)
    return SemiringMorphism(
        name=f"mod-{common}-to-pair-{left}-{right}",
        source=modular_semiring(common),
        target=product_semiring(left_semiring, right_semiring),
        map_value=lambda value: (int(value) % left, int(value) % right),
    )


def modular_lcm_pair_morphism_is_injective(
    left_modulus: int,
    right_modulus: int,
) -> bool:
    left = _modulus(left_modulus, name="left_modulus")
    right = _modulus(right_modulus, name="right_modulus")
    common = lcm(left, right)
    morphism = modular_lcm_pair_morphism(left, right)
    images = tuple(morphism.map_value(value) for value in range(common))
    return len(set(images)) == common


def modular_divisibility_branching_refinement(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
    coarse_modulus: int,
    fine_modulus: int,
) -> bool:
    morphism = modular_reduction_morphism(fine_modulus, coarse_modulus)
    if not verify_semiring_morphism(
        morphism,
        tuple(range(morphism.source.name.count("") + 12)),
    ):
        raise AssertionError("modular reduction failed bounded semiring-hom check")
    return morphism_commutes_with_branching_construction(
        states,
        relations,
        observation,
        horizon,
        morphism,
    )


def modular_lcm_branching_equals_product(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
    left_modulus: int,
    right_modulus: int,
) -> bool:
    left = _modulus(left_modulus, name="left_modulus")
    right = _modulus(right_modulus, name="right_modulus")
    common = lcm(left, right)
    morphism = modular_lcm_pair_morphism(left, right)
    if not modular_lcm_pair_morphism_is_injective(left, right):
        raise AssertionError("lcm residue map unexpectedly lost injectivity")
    if not morphism_commutes_with_branching_construction(
        states,
        relations,
        observation,
        horizon,
        morphism,
    ):
        raise AssertionError("lcm branching failed to map to product branching")

    lcm_partition = semiring_branching_partition(
        states,
        relations,
        observation,
        horizon,
        modular_semiring(common),
    )
    product_partition = semiring_branching_partition(
        states,
        relations,
        observation,
        horizon,
        morphism.target,
    )
    # Injectivity of the coefficient morphism propagates recursively: no child
    # signature collision or coefficient collision is introduced.
    if lcm_partition != product_partition:
        raise AssertionError("injective lcm coefficient map changed branching kernel")
    return True


def modular_terminal_trace_partition(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
    modulus: int,
) -> Partition:
    mod = _modulus(modulus, name="modulus")
    order = tuple(states)
    if not order or len(set(order)) != len(order):
        raise ValueError("states must be a nonempty distinct sequence")
    if not relations:
        raise ValueError("relation family must be nonempty")
    semiring = modular_semiring(mod)
    words = words_through_horizon(tuple(relations), horizon)
    groups: dict[tuple[object, ...], set[State]] = {}
    for source in order:
        signature = tuple(
            (
                word,
                frozenset(
                    raw_semiring_word_trace(
                        order,
                        relations,
                        observation,
                        source,
                        word,
                        semiring,
                    ).items()
                ),
            )
            for word in words
        )
        groups.setdefault(signature, set()).add(source)
    return normalize_partition(tuple(groups.values()))


def modular_terminal_trace_lcm_is_independent_join(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
    left_modulus: int,
    right_modulus: int,
) -> bool:
    left = _modulus(left_modulus, name="left_modulus")
    right = _modulus(right_modulus, name="right_modulus")
    common = lcm(left, right)
    left_partition = modular_terminal_trace_partition(
        states, relations, observation, horizon, left
    )
    right_partition = modular_terminal_trace_partition(
        states, relations, observation, horizon, right
    )
    joined = joint_partition(left_partition, right_partition)
    common_partition = modular_terminal_trace_partition(
        states, relations, observation, horizon, common
    )
    if joined != common_partition:
        raise AssertionError("terminal modular trace join failed lcm law")
    return True


@dataclass(frozen=True)
class ModularBranchingLatticeReport:
    left_modulus: int
    right_modulus: int
    gcd_modulus: int
    lcm_modulus: int
    independent_branching_join: Partition
    coupled_branching_join: Partition
    lcm_branching_partition: Partition
    compositional_debt_blocks: int
    compositional_repair_steps: int


def modular_branching_lattice_report(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    left_modulus: int,
    right_modulus: int,
) -> ModularBranchingLatticeReport:
    left = _modulus(left_modulus, name="left_modulus")
    right = _modulus(right_modulus, name="right_modulus")
    common = lcm(left, right)
    initial = partition_from_observation(states, observation)
    join_report: CompositionalInterfaceJoinReport = compositional_interface_join_report(
        initial,
        relations,
        (modular_semiring(left), modular_semiring(right)),
    )
    lcm_report = coarsest_shared_semiring_refinement(
        initial,
        relations,
        (modular_semiring(common),),
    )
    if join_report.coupled_final_partition != lcm_report.final_partition:
        raise AssertionError("coupled modular join disagreed with lcm branching quotient")
    return ModularBranchingLatticeReport(
        left_modulus=left,
        right_modulus=right,
        gcd_modulus=gcd(left, right),
        lcm_modulus=common,
        independent_branching_join=join_report.independent_readout_join,
        coupled_branching_join=join_report.coupled_final_partition,
        lcm_branching_partition=lcm_report.final_partition,
        compositional_debt_blocks=join_report.extra_compositional_blocks,
        compositional_repair_steps=join_report.strict_compositional_repair_steps,
    )


def modular_gcd_is_common_coefficient_coarsening(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
    left_modulus: int,
    right_modulus: int,
) -> bool:
    left = _modulus(left_modulus, name="left_modulus")
    right = _modulus(right_modulus, name="right_modulus")
    common = gcd(left, right)
    if common == 1:
        # Mod-1 is the trivial coefficient world and is intentionally not
        # represented by ``modular_semiring``.  It is the formal bottom here.
        return True
    common_partition = semiring_branching_partition(
        states,
        relations,
        observation,
        horizon,
        modular_semiring(common),
    )
    left_partition = semiring_branching_partition(
        states,
        relations,
        observation,
        horizon,
        modular_semiring(left),
    )
    right_partition = semiring_branching_partition(
        states,
        relations,
        observation,
        horizon,
        modular_semiring(right),
    )
    if not partition_refines(left_partition, common_partition):
        raise AssertionError("left modular branching failed to refine gcd coefficient view")
    if not partition_refines(right_partition, common_partition):
        raise AssertionError("right modular branching failed to refine gcd coefficient view")
    return True
