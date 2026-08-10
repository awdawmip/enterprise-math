"""Finite support diagnostics for witness/precision quantifier order.

For a finite set of inspected precisions, let ``S_i`` be the witness labels that
remain locally admissible at precision i.

Two statements are different:

    forall i exists lambda_i in S_i

versus

    exists lambda in intersection_i S_i.

The first says every support is nonempty; the second says one witness survives
all inspected precisions.

For modular precision, a directed family should also include/semantically control
common lcm refinements.  If M,N and L=lcm(M,N) are all present, ordinary witness
reduction requires

    S_L subseteq S_M intersect S_N.

Thus incompatible prime-local labels are exposed as an empty joint support at the
lcm precision rather than being silently treated as one coherent witness.

This module is a finite diagnostic surface for the quantifier theorem; infinite
compactness/descent remains theorem-level mathematics.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import lcm
from typing import Hashable, Mapping


Label = Hashable


def _normalize_supports(
    supports: Mapping[int, frozenset[Label] | set[Label] | tuple[Label, ...]],
) -> dict[int, frozenset[Label]]:
    if not supports:
        raise ValueError("support map must be nonempty")
    result: dict[int, frozenset[Label]] = {}
    for modulus, support in supports.items():
        if isinstance(modulus, bool) or not isinstance(modulus, int):
            raise TypeError("precision keys/moduli must be integers")
        if modulus <= 0:
            raise ValueError("precision keys/moduli must be positive")
        result[modulus] = frozenset(support)
    return result


@dataclass(frozen=True)
class WitnessQuantifierReport:
    precisions: tuple[int, ...]
    supports: tuple[tuple[int, frozenset[Label]], ...]
    every_precision_has_witness: bool
    common_witnesses: frozenset[Label]

    @property
    def one_witness_survives_every_precision(self) -> bool:
        return bool(self.common_witnesses)

    @property
    def forall_exists_but_not_exists_forall(self) -> bool:
        return (
            self.every_precision_has_witness
            and not self.one_witness_survives_every_precision
        )


def witness_quantifier_report(
    supports: Mapping[int, frozenset[Label] | set[Label] | tuple[Label, ...]],
) -> WitnessQuantifierReport:
    normalized = _normalize_supports(supports)
    ordered = tuple(sorted(normalized.items()))
    every = all(bool(support) for _, support in ordered)
    common = set(ordered[0][1])
    for _, support in ordered[1:]:
        common.intersection_update(support)
    return WitnessQuantifierReport(
        precisions=tuple(modulus for modulus, _ in ordered),
        supports=ordered,
        every_precision_has_witness=every,
        common_witnesses=frozenset(common),
    )


def verify_present_lcm_refinements(
    supports: Mapping[int, frozenset[Label] | set[Label] | tuple[Label, ...]],
) -> bool:
    """Verify support descent for every pair whose lcm is present in the map."""
    normalized = _normalize_supports(supports)
    moduli = tuple(normalized)
    for left in moduli:
        for right in moduli:
            joint = lcm(left, right)
            if joint not in normalized:
                continue
            if not normalized[joint].issubset(
                normalized[left] & normalized[right]
            ):
                raise AssertionError("joint precision created a witness label")
    return True


def missing_pairwise_lcm_refinements(
    supports: Mapping[int, frozenset[Label] | set[Label] | tuple[Label, ...]],
) -> tuple[int, ...]:
    normalized = _normalize_supports(supports)
    moduli = tuple(normalized)
    missing = {
        lcm(left, right)
        for left in moduli
        for right in moduli
        if lcm(left, right) not in normalized
    }
    return tuple(sorted(missing))


def add_joint_support(
    supports: Mapping[int, frozenset[Label] | set[Label] | tuple[Label, ...]],
    left: int,
    right: int,
    joint_support: frozenset[Label] | set[Label] | tuple[Label, ...],
) -> WitnessQuantifierReport:
    normalized = _normalize_supports(supports)
    if left not in normalized or right not in normalized:
        raise ValueError("left/right precisions must already be present")
    joint = lcm(left, right)
    proposed = frozenset(joint_support)
    if not proposed.issubset(normalized[left] & normalized[right]):
        raise ValueError("joint support must descend from both coarser supports")
    updated = dict(normalized)
    updated[joint] = proposed
    verify_present_lcm_refinements(updated)
    return witness_quantifier_report(updated)
