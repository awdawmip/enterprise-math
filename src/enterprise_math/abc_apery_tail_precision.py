"""Task-minimal compression of the P025 Apéry access profile.

Stage 16 stores, for every defect residue j modulo P=sum(b_i), an Apéry value
``a_j`` and the minimum non-negative L-infinity factorization radius ``L_j``.
For the future language that asks only

* whether a target has entered its exact affine-periodic tail, and
* the exact access radius once it has,

``L_j`` is over-refined.  Only

    q_j = ceil(L_j / 2)

is observable because the signed/non-negative defect transform supplies a
coordinate capacity of ``2*r``.

This module keeps that task-relative distinction explicit and also records a
finite exact signature for the *entire* non-negative access function: tail
profile plus the finite exceptional-response table.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_block_access_apery import (
    apery_access_profile,
    exact_block_access_radius,
    primitive_positive_row,
)


@dataclass(frozen=True)
class CertifiedTailResidue:
    target_residue: int
    apery_value: int
    half_factorization_cap: int
    first_stable_target: int


@dataclass(frozen=True)
class CertifiedTailSignature:
    coefficients: tuple[int, ...]
    period: int
    residues: tuple[CertifiedTailResidue, ...]


@dataclass(frozen=True)
class ExactAccessSignature:
    tail: CertifiedTailSignature
    exceptional_responses: tuple[tuple[int, int], ...]


def certified_tail_signature(coefficients: tuple[int, ...]) -> CertifiedTailSignature:
    """Return the coarser ``(a_j,ceil(L_j/2))`` tail-certification state."""
    profile = apery_access_profile(coefficients)
    residues = tuple(
        CertifiedTailResidue(
            target_residue=record.target_residue,
            apery_value=record.apery_value,
            half_factorization_cap=(record.apery_min_linf + 1) // 2,
            first_stable_target=record.first_stable_target,
        )
        for record in profile.residues
    )
    return CertifiedTailSignature(
        coefficients=profile.coefficients,
        period=profile.period,
        residues=residues,
    )


def tail_access_query(
    signature: CertifiedTailSignature, target: int
) -> dict[str, int | bool]:
    """Decide stability and, on the stable tail, reconstruct exact access radius."""
    if isinstance(target, bool) or not isinstance(target, int) or target < 0:
        raise ValueError("target must be a non-negative integer")
    residue = target % signature.period
    record = next(item for item in signature.residues if item.target_residue == residue)
    stable = target >= record.first_stable_target
    result: dict[str, int | bool] = {
        "stable": stable,
        "first_stable_target": record.first_stable_target,
    }
    if stable:
        numerator = target + record.apery_value
        if numerator % signature.period:
            raise AssertionError("tail signature lost Apéry residue compatibility")
        result["radius"] = numerator // signature.period
    return result


def exact_access_signature(coefficients: tuple[int, ...]) -> ExactAccessSignature:
    """Return a finite signature reconstructing ``kappa_b(N)`` for every ``N>=0``."""
    profile = apery_access_profile(coefficients)
    tail = certified_tail_signature(coefficients)
    exceptions = tuple(
        (target, exact_block_access_radius(profile.coefficients, target))
        for target in profile.exceptional_targets
    )
    return ExactAccessSignature(tail=tail, exceptional_responses=exceptions)


def exact_access_from_signature(signature: ExactAccessSignature, target: int) -> int:
    """Reconstruct the full non-negative access response from the finite signature."""
    if isinstance(target, bool) or not isinstance(target, int) or target < 0:
        raise ValueError("target must be a non-negative integer")
    exceptions = dict(signature.exceptional_responses)
    if target in exceptions:
        return exceptions[target]
    query = tail_access_query(signature.tail, target)
    if not query["stable"]:
        raise AssertionError("non-exception target failed tail-certification state")
    return int(query["radius"])


def same_apery_different_tail_onset_counterexample() -> dict[str, object]:
    """Show semigroup/Apéry membership data alone do not determine access onset."""
    first = (2, 4, 5, 11)
    second = (2, 5, 7, 8)
    p1 = apery_access_profile(first)
    p2 = apery_access_profile(second)
    a1 = tuple(record.apery_value for record in p1.residues)
    a2 = tuple(record.apery_value for record in p2.residues)
    if p1.period != p2.period or a1 != a2:
        raise AssertionError("counterexample lost equal period/Apéry values")
    target = 16
    k1 = exact_block_access_radius(first, target)
    k2 = exact_block_access_radius(second, target)
    if (k1, k2) != (1, 2):
        raise AssertionError("counterexample lost distinct access precision")
    t1 = certified_tail_signature(first)
    t2 = certified_tail_signature(second)
    return {
        "rows": (first, second),
        "period": p1.period,
        "apery_values": a1,
        "target": target,
        "access_radii": (k1, k2),
        "first_tail_signature": t1,
        "second_tail_signature": t2,
    }


def same_tail_signature_different_raw_factorization_profile() -> dict[str, object]:
    """Show ``L_j`` can differ while all certified-tail observables remain equal."""
    first = (2, 4, 5, 11)
    second = (2, 5, 6, 9)
    p1 = apery_access_profile(first)
    p2 = apery_access_profile(second)
    s1 = certified_tail_signature(first)
    s2 = certified_tail_signature(second)
    reduced1 = tuple(
        (r.target_residue, r.apery_value, r.half_factorization_cap, r.first_stable_target)
        for r in s1.residues
    )
    reduced2 = tuple(
        (r.target_residue, r.apery_value, r.half_factorization_cap, r.first_stable_target)
        for r in s2.residues
    )
    if p1.period != p2.period or reduced1 != reduced2:
        raise AssertionError("example lost equal certified-tail signature")
    raw_l1 = tuple(record.apery_min_linf for record in p1.residues)
    raw_l2 = tuple(record.apery_min_linf for record in p2.residues)
    if raw_l1 == raw_l2:
        raise AssertionError("example lost distinct raw L-infinity factorization profile")
    return {
        "rows": (first, second),
        "period": p1.period,
        "raw_linf_profiles": (raw_l1, raw_l2),
        "certified_tail_profile": reduced1,
    }
