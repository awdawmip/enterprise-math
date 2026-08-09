"""Explicit force-role material law and irregular-grid cycle-work accounting.

``MaterialCurveProfile`` is generic.  Its samples are not force, energy, velocity,
or restitution unless a caller supplies a role/calibration.  This module declares
one finite force interpretation on an explicit deformation grid.

Let deformation counts be strictly increasing ``x_0<...<x_K``.  Loading and
returning force samples ``L_k,R_k`` live on one force count scale.  For each
interval ``dx_k=x_k-x_{k-1}`` this module uses the symmetric two-endpoint finite
work rule

    2 W_load   = sum (L_{k-1}+L_k) dx_k,
    2 W_return = sum (R_{k-1}+R_k) dx_k.

No uniform-grid assumption is hidden.  If force counts represent ``1/Fs`` of the
declared force unit and deformation counts represent ``1/Xs`` of the declared
length unit, physical work is the exact rational

    W = work_numerator2 / (2*Fs*Xs)

in ``force_unit * deformation_unit``.  Without a meaningful external calibration
this remains an exact finite work-coordinate, not a claim in joules.

A passive full load-return family on this declared chord schedule requires
``W_load(K)-W_return(K)>=0`` for every reachable peak K.  Pointwise
``R_k<=L_k`` is sufficient but not necessary.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .material_response import MaterialCurveProfile


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True)
class ExactWorkCoordinate:
    numerator: int
    denominator: int
    unit: str

    def __post_init__(self) -> None:
        if isinstance(self.numerator, bool) or not isinstance(self.numerator, int):
            raise ValueError("numerator must be an integer")
        _require_positive("denominator", self.denominator)
        if not isinstance(self.unit, str) or not self.unit:
            raise ValueError("unit must be a nonempty string")


@dataclass(frozen=True)
class FiniteForceLaw:
    profile: MaterialCurveProfile
    deformation_counts: tuple[int, ...]
    force_scale_factor: int
    force_unit: str
    deformation_scale_factor: int
    deformation_unit: str

    def __post_init__(self) -> None:
        if not self.profile.loading or len(self.profile.loading) != len(self.profile.returning):
            raise ValueError("force law requires equal nonempty loading/returning branches")
        if len(self.deformation_counts) != len(self.profile.loading):
            raise ValueError("deformation grid must have one coordinate per force sample")
        if any(
            isinstance(value, bool) or not isinstance(value, int)
            for value in self.deformation_counts
        ):
            raise ValueError("deformation counts must be integers")
        if any(
            right <= left
            for left, right in zip(
                self.deformation_counts,
                self.deformation_counts[1:],
            )
        ):
            raise ValueError("deformation counts must be strictly increasing")
        _require_positive("force_scale_factor", self.force_scale_factor)
        _require_positive("deformation_scale_factor", self.deformation_scale_factor)
        if not isinstance(self.force_unit, str) or not self.force_unit:
            raise ValueError("force_unit must be a nonempty string")
        if not isinstance(self.deformation_unit, str) or not self.deformation_unit:
            raise ValueError("deformation_unit must be a nonempty string")

    @property
    def work_unit(self) -> str:
        return f"{self.force_unit}*{self.deformation_unit}"


def uniform_force_law(
    profile: MaterialCurveProfile,
    force_scale_factor: int = 1,
    force_unit: str = "force_q",
    deformation_scale_factor: int = 1,
    deformation_unit: str = "depth_cell",
    cell_width_counts: int = 1,
) -> FiniteForceLaw:
    """Convenience constructor for an explicitly uniform intrinsic grid."""
    _require_positive("cell_width_counts", cell_width_counts)
    grid = tuple(index * cell_width_counts for index in range(len(profile.loading)))
    return FiniteForceLaw(
        profile=profile,
        deformation_counts=grid,
        force_scale_factor=force_scale_factor,
        force_unit=force_unit,
        deformation_scale_factor=deformation_scale_factor,
        deformation_unit=deformation_unit,
    )


def _exact_work(law: FiniteForceLaw, numerator2: int) -> ExactWorkCoordinate:
    denominator = 2 * law.force_scale_factor * law.deformation_scale_factor
    common = gcd(abs(numerator2), denominator)
    return ExactWorkCoordinate(
        numerator=numerator2 // common,
        denominator=denominator // common,
        unit=law.work_unit,
    )


@dataclass(frozen=True)
class ForceCycleWorkReport:
    peak_depth: int
    loading_work_numerator2: int
    returned_work_numerator2: int
    dissipated_work_numerator2: int
    loading_work: ExactWorkCoordinate
    returned_work: ExactWorkCoordinate
    dissipated_work: ExactWorkCoordinate
    passive: bool


def force_cycle_work_report(law: FiniteForceLaw, peak_depth: int) -> ForceCycleWorkReport:
    """Exact irregular-grid chord work for one 0->K->0 finite material cycle."""
    if isinstance(peak_depth, bool) or not isinstance(peak_depth, int) or peak_depth < 0:
        raise ValueError("peak_depth must be a non-negative integer")
    if peak_depth >= len(law.profile.loading):
        raise ValueError("peak_depth lies outside the finite force law")
    load2 = 0
    return2 = 0
    for depth in range(1, peak_depth + 1):
        width = law.deformation_counts[depth] - law.deformation_counts[depth - 1]
        load2 += (
            law.profile.loading[depth - 1] + law.profile.loading[depth]
        ) * width
        return2 += (
            law.profile.returning[depth - 1] + law.profile.returning[depth]
        ) * width
    loss2 = load2 - return2
    return ForceCycleWorkReport(
        peak_depth=peak_depth,
        loading_work_numerator2=load2,
        returned_work_numerator2=return2,
        dissipated_work_numerator2=loss2,
        loading_work=_exact_work(law, load2),
        returned_work=_exact_work(law, return2),
        dissipated_work=_exact_work(law, loss2),
        passive=loss2 >= 0,
    )


def force_cycle_work_prefixes(law: FiniteForceLaw) -> tuple[ForceCycleWorkReport, ...]:
    return tuple(
        force_cycle_work_report(law, depth)
        for depth in range(len(law.profile.loading))
    )


def force_law_is_cumulatively_passive(law: FiniteForceLaw) -> bool:
    return all(report.passive for report in force_cycle_work_prefixes(law))


def first_force_passivity_violation(law: FiniteForceLaw) -> ForceCycleWorkReport | None:
    for report in force_cycle_work_prefixes(law):
        if not report.passive:
            return report
    return None


@dataclass(frozen=True)
class OpposingImpulseKineticReport:
    inward_momentum: int
    outward_impulse: int
    after_signed_momentum: int
    kinetic_numerator_before: int
    kinetic_numerator_after: int
    kinetic_numerator_change: int
    phase: str


SLOWING = "SLOWING"
STOP = "STOP"
DISSIPATIVE_REVERSAL = "DISSIPATIVE_REVERSAL"
ELASTIC_REVERSAL = "ELASTIC_REVERSAL"
SUPERELASTIC_REVERSAL = "SUPERELASTIC_REVERSAL"


def opposing_impulse_kinetic_report(
    inward_momentum: int,
    outward_impulse: int,
) -> OpposingImpulseKineticReport:
    """Classify one opposing kick by ``(P-J)^2-P^2=J(J-2P)``."""
    for name, value in (
        ("inward_momentum", inward_momentum),
        ("outward_impulse", outward_impulse),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"{name} must be a non-negative integer")
    after = inward_momentum - outward_impulse
    before_k = inward_momentum * inward_momentum
    after_k = after * after
    change = after_k - before_k
    if change != outward_impulse * (outward_impulse - 2 * inward_momentum):
        raise AssertionError("opposing impulse kinetic identity failed")

    if outward_impulse < inward_momentum:
        phase = SLOWING
    elif outward_impulse == inward_momentum:
        phase = STOP
    elif outward_impulse < 2 * inward_momentum:
        phase = DISSIPATIVE_REVERSAL
    elif outward_impulse == 2 * inward_momentum:
        phase = ELASTIC_REVERSAL
    else:
        phase = SUPERELASTIC_REVERSAL
    return OpposingImpulseKineticReport(
        inward_momentum=inward_momentum,
        outward_impulse=outward_impulse,
        after_signed_momentum=after,
        kinetic_numerator_before=before_k,
        kinetic_numerator_after=after_k,
        kinetic_numerator_change=change,
        phase=phase,
    )
