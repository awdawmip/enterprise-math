"""Exact collision-information factors behind safe-operation constraints.

For a finite observation partition with block sizes ``n_1,...,n_b`` on ``n``
states, the total-operation safe probability is

    P_total = product_i C_(n_i),

where

    C_k = sum_j (n_j/n)^k

is the order-k collision power sum of the target block-mass distribution.
For every source block with ``k>1`` one may write

    C_k = exp(-(k-1) H_k),

where ``H_k`` is the order-k Renyi entropy.  Therefore the ordinary logarithmic
operation-constraint information is

    I_total = -log P_total
            = sum_{i:n_i>1} (n_i-1) H_(n_i).

The executable layer keeps this decomposition exact without evaluating logs: it
returns the rational collision factor together with its integer coefficient
``n_i-1`` and verifies their product.

Deterministic partial operations have an equally clean interpretation.  Under
the uniform partial-endomap universe there are ``n+1`` observable pointwise
outputs: one ``UNDEFINED`` output and ``n`` ordinary target states.  At the
partition level the augmented target-mass distribution is

    p_tilde = (1/(n+1), n_1/(n+1), ..., n_b/(n+1)).

Hence the safe partial probability is the product of its collision power sums,
and

    I_partial = sum_{i:n_i>1} (n_i-1) H_(n_i)(p_tilde).

This explains the endpoint asymmetry exactly:

* total / indiscrete: target entropy is zero, so operation constraint vanishes;
* total / discrete: every source coefficient ``n_i-1`` is zero;
* partial / indiscrete: `UNDEFINED` creates a second observable target category,
  so target entropy remains positive and the endpoint no longer reconnects;
* partial / discrete: source coefficients again vanish, so all partial maps are
  safe.

Renyi entropy and collision probabilities are standard prior mathematics.  The
Enterprise Math result is the exact source-multiplicity x target-uncertainty
interpretation of collapse-generated operation freedom.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import reduce
from operator import mul
from typing import Hashable, Mapping

from .partial_safe_operation_spectrum import partition_block_sizes
from .safe_operation_collision_moments import (
    safe_partial_probability,
    safe_total_probability,
)

Vertex = Hashable
Partition = Mapping[Vertex, Hashable]


def _partition(partition: Partition) -> tuple[int, tuple[int, ...]]:
    sizes = partition_block_sizes(partition)
    n = sum(sizes)
    if n <= 0:
        raise ValueError("partition must be nonempty")
    return n, sizes


@dataclass(frozen=True)
class CollisionInformationTerm:
    source_block_size: int
    renyi_coefficient: int
    collision_factor: Fraction
    augmented_with_undefined: bool

    @property
    def contributes_constraint(self) -> bool:
        return self.renyi_coefficient > 0 and self.collision_factor < 1


def total_collision_factor(partition: Partition, exponent: int) -> Fraction:
    n, sizes = _partition(partition)
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("exponent must be an integer")
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    return Fraction(sum(size**exponent for size in sizes), n**exponent)


def partial_augmented_collision_factor(
    partition: Partition,
    exponent: int,
) -> Fraction:
    n, sizes = _partition(partition)
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("exponent must be an integer")
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    return Fraction(
        1 + sum(size**exponent for size in sizes),
        (n + 1) ** exponent,
    )


def total_collision_information_terms(
    partition: Partition,
) -> tuple[CollisionInformationTerm, ...]:
    _, sizes = _partition(partition)
    return tuple(
        CollisionInformationTerm(
            source_block_size=size,
            renyi_coefficient=size - 1,
            collision_factor=total_collision_factor(partition, size),
            augmented_with_undefined=False,
        )
        for size in sizes
    )


def partial_collision_information_terms(
    partition: Partition,
) -> tuple[CollisionInformationTerm, ...]:
    _, sizes = _partition(partition)
    return tuple(
        CollisionInformationTerm(
            source_block_size=size,
            renyi_coefficient=size - 1,
            collision_factor=partial_augmented_collision_factor(
                partition, size
            ),
            augmented_with_undefined=True,
        )
        for size in sizes
    )


def collision_term_product(
    terms: tuple[CollisionInformationTerm, ...],
) -> Fraction:
    return reduce(
        mul,
        (term.collision_factor for term in terms),
        Fraction(1, 1),
    )


def total_collision_terms_reconstruct_probability(partition: Partition) -> bool:
    return collision_term_product(
        total_collision_information_terms(partition)
    ) == safe_total_probability(partition)


def partial_collision_terms_reconstruct_probability(partition: Partition) -> bool:
    return collision_term_product(
        partial_collision_information_terms(partition)
    ) == safe_partial_probability(partition)


def total_constraint_zero_reason(partition: Partition) -> str:
    """Classify the exact zero-information endpoints of total operation safety."""
    n, sizes = _partition(partition)
    probability = safe_total_probability(partition)
    if probability != 1:
        return "INTERMEDIATE_POSITIVE_CONSTRAINT"
    if sizes == (n,):
        return "INDISCRETE_TARGET_ENTROPY_ZERO"
    if sizes == (1,) * n:
        return "DISCRETE_SOURCE_MULTIPLICITY_ZERO"
    raise AssertionError("unexpected total zero-constraint partition")


def partial_constraint_zero_reason(partition: Partition) -> str:
    """Partial operation freedom is unconstrained exactly at discrete precision."""
    n, sizes = _partition(partition)
    probability = safe_partial_probability(partition)
    if probability != 1:
        return "POSITIVE_CONSTRAINT"
    if sizes == (1,) * n:
        return "DISCRETE_SOURCE_MULTIPLICITY_ZERO"
    raise AssertionError("unexpected partial zero-constraint partition")


def source_multiplicity_constraint_mass(
    terms: tuple[CollisionInformationTerm, ...],
) -> int:
    """Sum of the integer coefficients multiplying the Renyi terms."""
    return sum(term.renyi_coefficient for term in terms)
