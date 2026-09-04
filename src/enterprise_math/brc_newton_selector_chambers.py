"""Exact complete split-affine selector chambers for Weighted-BRC Newton edges.

Implements WBRC-T60/T61 only.  The module assumes a caller-supplied complete
real-root certificate consisting of one fixed rational declared root and
finitely many rational-affine real-root branches.  It does not factor arbitrary
polynomials or implement general parametric Sturm/subresultant chambers.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Literal, Sequence, TypeAlias

from .brc_newton_schedule_strata import RationalAffineForm

RationalInput: TypeAlias = int | Fraction
OrderRelation: TypeAlias = Literal["GT_ZERO", "LE_ZERO"]
Poly: TypeAlias = tuple[Fraction, ...]


def _fraction(name: str, value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be int or Fraction")
    return Fraction(value)


def _trim(poly: Sequence[RationalInput]) -> Poly:
    if not poly:
        raise ValueError("polynomial must be nonempty")
    values = [_fraction("polynomial coefficient", value) for value in poly]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def _mul(left: Poly, right: Poly) -> Poly:
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return _trim(out)


def _power(poly: Poly, exponent: int) -> Poly:
    out: Poly = (Fraction(1),)
    for _ in range(exponent):
        out = _mul(out, poly)
    return out


def _monic(poly: Sequence[RationalInput]) -> Poly:
    normalized = _trim(poly)
    if normalized == (Fraction(0),):
        raise ValueError("zero polynomial has no root inventory")
    leading = normalized[-1]
    return tuple(value / leading for value in normalized)


def _threshold_form(form: RationalAffineForm, threshold: Fraction) -> RationalAffineForm:
    return form.add(RationalAffineForm.constant(-threshold, form.parameter_count))


@dataclass(frozen=True)
class SplitAffineRootBranch:
    root_form: RationalAffineForm
    multiplicity: int = 1

    def __post_init__(self) -> None:
        if not isinstance(self.root_form, RationalAffineForm):
            raise TypeError("root_form must be RationalAffineForm")
        if isinstance(self.multiplicity, bool) or not isinstance(self.multiplicity, int):
            raise TypeError("branch multiplicity must be an integer")
        if self.multiplicity < 1:
            raise ValueError("branch multiplicity must be positive")


@dataclass(frozen=True)
class SplitAffineRootCertificate:
    declared_root: Fraction
    declared_multiplicity: int
    branches: tuple[SplitAffineRootBranch, ...]
    polynomial_degree: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "declared_root", _fraction("declared_root", self.declared_root))
        if isinstance(self.declared_multiplicity, bool) or not isinstance(self.declared_multiplicity, int):
            raise TypeError("declared_multiplicity must be an integer")
        if self.declared_multiplicity < 1:
            raise ValueError("declared_multiplicity must be positive")
        if any(not isinstance(branch, SplitAffineRootBranch) for branch in self.branches):
            raise TypeError("branches must contain SplitAffineRootBranch")
        parameter_counts = {branch.root_form.parameter_count for branch in self.branches}
        if len(parameter_counts) > 1:
            raise ValueError("all root branches must share one parameter count")
        if isinstance(self.polynomial_degree, bool) or not isinstance(self.polynomial_degree, int):
            raise TypeError("polynomial_degree must be an integer")
        expected = self.declared_multiplicity + sum(branch.multiplicity for branch in self.branches)
        if self.polynomial_degree != expected:
            raise ValueError("polynomial_degree does not match complete root multiplicities")

    @property
    def parameter_count(self) -> int:
        if not self.branches:
            return 0
        return self.branches[0].root_form.parameter_count


@dataclass(frozen=True)
class AffineOrderAtom:
    form: RationalAffineForm
    relation: OrderRelation

    def __post_init__(self) -> None:
        if not isinstance(self.form, RationalAffineForm):
            raise TypeError("form must be RationalAffineForm")
        if self.relation not in ("GT_ZERO", "LE_ZERO"):
            raise ValueError("unsupported affine order relation")

    def holds(self, parameters: Sequence[RationalInput]) -> bool:
        value = self.form.evaluate(parameters)
        return value > 0 if self.relation == "GT_ZERO" else value <= 0


@dataclass(frozen=True)
class AffineOrderClause:
    """One disjunction of affine order atoms."""

    atoms: tuple[AffineOrderAtom, ...]

    def __post_init__(self) -> None:
        if not self.atoms:
            raise ValueError("order clause must contain at least one atom")
        if any(not isinstance(atom, AffineOrderAtom) for atom in self.atoms):
            raise TypeError("clause atoms must be AffineOrderAtom")
        counts = {atom.form.parameter_count for atom in self.atoms}
        if len(counts) != 1:
            raise ValueError("clause atoms must share one parameter count")

    def holds(self, parameters: Sequence[RationalInput]) -> bool:
        return any(atom.holds(parameters) for atom in self.atoms)


@dataclass(frozen=True)
class SplitAffineSelectorChamber:
    """Conjunction of disjunctive affine-order clauses."""

    clauses: tuple[AffineOrderClause, ...]
    selector: Literal["SMALLEST_REAL_ROOT", "SMALLEST_POSITIVE_REAL_ROOT"]

    def __post_init__(self) -> None:
        if self.selector not in ("SMALLEST_REAL_ROOT", "SMALLEST_POSITIVE_REAL_ROOT"):
            raise ValueError("unsupported selector")
        if any(not isinstance(clause, AffineOrderClause) for clause in self.clauses):
            raise TypeError("clauses must contain AffineOrderClause")
        counts = {clause.atoms[0].form.parameter_count for clause in self.clauses}
        if len(counts) > 1:
            raise ValueError("selector clauses must share one parameter count")

    def holds(self, parameters: Sequence[RationalInput]) -> bool:
        return all(clause.holds(parameters) for clause in self.clauses)


def split_affine_fixed_multiplicity_holds(
    certificate: SplitAffineRootCertificate,
    parameters: Sequence[RationalInput],
) -> bool:
    if not isinstance(certificate, SplitAffineRootCertificate):
        raise TypeError("certificate must be SplitAffineRootCertificate")
    return all(branch.root_form.evaluate(parameters) != certificate.declared_root for branch in certificate.branches)


def split_affine_smallest_real_chamber(
    certificate: SplitAffineRootCertificate,
) -> SplitAffineSelectorChamber:
    if not isinstance(certificate, SplitAffineRootCertificate):
        raise TypeError("certificate must be SplitAffineRootCertificate")
    clauses = tuple(
        AffineOrderClause((AffineOrderAtom(_threshold_form(branch.root_form, certificate.declared_root), "GT_ZERO"),))
        for branch in certificate.branches
    )
    return SplitAffineSelectorChamber(clauses, "SMALLEST_REAL_ROOT")


def split_affine_smallest_positive_chamber(
    certificate: SplitAffineRootCertificate,
) -> SplitAffineSelectorChamber:
    if not isinstance(certificate, SplitAffineRootCertificate):
        raise TypeError("certificate must be SplitAffineRootCertificate")
    if certificate.declared_root <= 0:
        raise ValueError("declared root must be positive for smallest-positive selection")
    clauses = tuple(
        AffineOrderClause(
            (
                AffineOrderAtom(branch.root_form, "LE_ZERO"),
                AffineOrderAtom(_threshold_form(branch.root_form, certificate.declared_root), "GT_ZERO"),
            )
        )
        for branch in certificate.branches
    )
    return SplitAffineSelectorChamber(clauses, "SMALLEST_POSITIVE_REAL_ROOT")


def split_affine_smallest_real_selected(
    certificate: SplitAffineRootCertificate,
    parameters: Sequence[RationalInput],
) -> bool:
    return split_affine_fixed_multiplicity_holds(certificate, parameters) and split_affine_smallest_real_chamber(certificate).holds(parameters)


def split_affine_smallest_positive_selected(
    certificate: SplitAffineRootCertificate,
    parameters: Sequence[RationalInput],
) -> bool:
    return split_affine_fixed_multiplicity_holds(certificate, parameters) and split_affine_smallest_positive_chamber(certificate).holds(parameters)


def split_affine_materialize_monic_polynomial(
    certificate: SplitAffineRootCertificate,
    parameters: Sequence[RationalInput],
) -> Poly:
    if not isinstance(certificate, SplitAffineRootCertificate):
        raise TypeError("certificate must be SplitAffineRootCertificate")
    root = certificate.declared_root
    poly = _power((-root, Fraction(1)), certificate.declared_multiplicity)
    for branch in certificate.branches:
        value = branch.root_form.evaluate(parameters)
        poly = _mul(poly, _power((-value, Fraction(1)), branch.multiplicity))
    if len(poly) - 1 != certificate.polynomial_degree:
        raise AssertionError("split materialization degree changed unexpectedly")
    return poly


def split_affine_matches_polynomial(
    certificate: SplitAffineRootCertificate,
    parameters: Sequence[RationalInput],
    polynomial: Sequence[RationalInput],
) -> bool:
    return split_affine_materialize_monic_polynomial(certificate, parameters) == _monic(polynomial)


__all__ = [
    "SplitAffineRootBranch",
    "SplitAffineRootCertificate",
    "AffineOrderAtom",
    "AffineOrderClause",
    "SplitAffineSelectorChamber",
    "split_affine_fixed_multiplicity_holds",
    "split_affine_smallest_real_chamber",
    "split_affine_smallest_positive_chamber",
    "split_affine_smallest_real_selected",
    "split_affine_smallest_positive_selected",
    "split_affine_materialize_monic_polynomial",
    "split_affine_matches_polynomial",
]
