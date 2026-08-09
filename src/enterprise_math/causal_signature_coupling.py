"""Finite causal signature coupling without probabilistic primitives.

A joint future-signature quotient Q_AB can be forgotten down to the pair of
marginal signature classes actually reachable in the joint system.  The fibers
of this forgetting map are the exact extra joint distinctions hidden by the
marginals.  Their collision spectrum is therefore literally the P011 fiber
collision spectrum of the cross-future-forgetting collapse.

Two different coupling mechanisms are kept separate:

* missing reachability: marginal pairs that cannot occur jointly;
* signature splitting: one reachable marginal pair supports multiple distinct
  joint future-signature classes.

No probability, correlation coefficient, entropy, tensor product, float, or
continuous completion is assumed.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb
from typing import Hashable


JointClass = Hashable
MarginalClass = Hashable
MarginalPair = tuple[MarginalClass, MarginalClass]


@dataclass(frozen=True)
class CouplingCertificate:
    left_class_count: int
    right_class_count: int
    reachable_pair_count: int
    joint_class_count: int
    missing_reachability: int
    signature_split_excess: int
    split_spectrum: tuple[int, ...]

    @property
    def is_signature_independent(self) -> bool:
        return self.missing_reachability == 0 and self.signature_split_excess == 0


def _require_positive_count(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def coupling_fiber_multiplicities(
    joint_to_marginal: dict[JointClass, MarginalPair],
) -> dict[MarginalPair, int]:
    """Number of distinct joint signature classes over each reachable marginal pair."""
    if not isinstance(joint_to_marginal, dict) or not joint_to_marginal:
        raise ValueError("joint_to_marginal must be a non-empty dict")
    counts: dict[MarginalPair, int] = {}
    for joint_class, marginal_pair in joint_to_marginal.items():
        try:
            hash(joint_class)
            hash(marginal_pair)
        except TypeError as error:
            raise ValueError("signature classes must be hashable") from error
        if not isinstance(marginal_pair, tuple) or len(marginal_pair) != 2:
            raise ValueError("each marginal target must be a pair")
        counts[marginal_pair] = counts.get(marginal_pair, 0) + 1
    return counts


def coupling_split_spectrum(
    joint_to_marginal: dict[JointClass, MarginalPair],
    maximum_order: int | None = None,
) -> tuple[int, ...]:
    """Return C_k = sum_r binom(c(r), k), including bookkeeping C_0."""
    counts = coupling_fiber_multiplicities(joint_to_marginal)
    joint_count = len(joint_to_marginal)
    limit = joint_count if maximum_order is None else maximum_order
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("maximum_order must be a non-negative integer")
    return tuple(
        sum(comb(size, order) for size in counts.values() if size >= order)
        for order in range(limit + 1)
    )


def coupling_certificate(
    joint_to_marginal: dict[JointClass, MarginalPair],
    left_class_count: int,
    right_class_count: int,
    maximum_order: int | None = None,
) -> CouplingCertificate:
    """Typed finite coupling certificate.

    missing_reachability counts absent combinations in Q_A x Q_B.
    signature_split_excess counts extra joint classes inside reachable marginal
    pairs.  The two mechanisms must not be collapsed into one scalar.
    """
    _require_positive_count(left_class_count, "left_class_count")
    _require_positive_count(right_class_count, "right_class_count")
    counts = coupling_fiber_multiplicities(joint_to_marginal)
    reachable_pairs = len(counts)
    possible_pairs = left_class_count * right_class_count
    if reachable_pairs > possible_pairs:
        raise ValueError("reachable marginal pairs exceed declared marginal product")
    joint_count = len(joint_to_marginal)
    return CouplingCertificate(
        left_class_count=left_class_count,
        right_class_count=right_class_count,
        reachable_pair_count=reachable_pairs,
        joint_class_count=joint_count,
        missing_reachability=possible_pairs - reachable_pairs,
        signature_split_excess=joint_count - reachable_pairs,
        split_spectrum=coupling_split_spectrum(joint_to_marginal, maximum_order),
    )


def forgetting_defect(mapping: dict[Hashable, Hashable]) -> int:
    """First-order class-loss count |domain|-|image| for a finite forgetting map."""
    if not isinstance(mapping, dict) or not mapping:
        raise ValueError("mapping must be a non-empty dict")
    return len(mapping) - len(set(mapping.values()))


def compose_forgetting(
    fine_to_middle: dict[Hashable, Hashable],
    middle_to_coarse: dict[Hashable, Hashable],
) -> dict[Hashable, Hashable]:
    """Compose two finite signature-forgetting maps on the reachable middle image."""
    if not isinstance(fine_to_middle, dict) or not fine_to_middle:
        raise ValueError("fine_to_middle must be a non-empty dict")
    if not isinstance(middle_to_coarse, dict) or not middle_to_coarse:
        raise ValueError("middle_to_coarse must be a non-empty dict")
    result: dict[Hashable, Hashable] = {}
    for fine, middle in fine_to_middle.items():
        if middle not in middle_to_coarse:
            raise ValueError("middle_to_coarse must define every reachable middle class")
        result[fine] = middle_to_coarse[middle]
    return result


def staged_forgetting_defects(
    fine_to_middle: dict[Hashable, Hashable],
    middle_to_coarse: dict[Hashable, Hashable],
) -> tuple[int, int, int]:
    """Return (fine->middle, middle->coarse, fine->coarse) class-loss defects.

    For maps whose middle domain is exactly the reachable image of the first map,
    the third value equals the sum of the first two.
    """
    reachable_middle = set(fine_to_middle.values())
    if set(middle_to_coarse) != reachable_middle:
        raise ValueError("middle_to_coarse domain must equal the reachable middle image")
    composed = compose_forgetting(fine_to_middle, middle_to_coarse)
    first = forgetting_defect(fine_to_middle)
    second = forgetting_defect(middle_to_coarse)
    total = forgetting_defect(composed)
    return first, second, total
