"""Exact whole-vs-lifted momentum drift defect for a future position task.

A retained momentum remainder is not automatically future-safe if the position
update reads only the whole momentum count.  Write one oriented non-negative
momentum lift as

    Pi = D_p*p + eta,       0 <= eta < D_p.

For a non-negative drift multiplier C and positive drift divisor D_x, the direct
lifted position increment is

    x_direct = floor(Pi*C / (D_p*D_x)).

If the world first hides eta and drifts only from p,

    p*C = D_x*s + sigma,    0 <= sigma < D_x,
    x_staged = s.

Exactly

    x_direct - x_staged
      = floor((D_p*sigma + eta*C)/(D_p*D_x)).

The defect is non-negative and can exceed one cell.  Thus retaining ``eta`` in
state but preventing the declared future drift operation from consuming it is
not a lossless physical lift; it is a deliberate quotient at the momentum-to-
position interface.

The theorem is written in an oriented non-negative coordinate.  Signed physical
motion can be handled by applying the same magnitude identity separately on each
orientation, or by the signed-toward-zero helpers used by the E001 world.
Generic future-quotient safety remains owned by A2/P023/P024.
"""

from __future__ import annotations

from dataclasses import dataclass


def _nat(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _pos(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True)
class LiftedMomentumDriftStagingReport:
    whole_momentum_count: int
    momentum_detail_numerator: int
    momentum_detail_divisor: int
    drift_multiplier: int
    drift_divisor: int
    staged_displacement_count: int
    staged_drift_remainder: int
    direct_lifted_displacement_count: int
    direct_lifted_remainder: int
    displacement_defect_count: int
    defect_formula_count: int

    @property
    def whole_momentum_quotient_safe_for_position(self) -> bool:
        return self.displacement_defect_count == 0


def lifted_momentum_drift_staging_report(
    whole_momentum_count: int,
    momentum_detail_numerator: int,
    momentum_detail_divisor: int,
    drift_multiplier: int,
    drift_divisor: int,
) -> LiftedMomentumDriftStagingReport:
    """Compare whole-momentum drift with direct drift from the retained lift."""
    _nat("whole_momentum_count", whole_momentum_count)
    _nat("momentum_detail_numerator", momentum_detail_numerator)
    _pos("momentum_detail_divisor", momentum_detail_divisor)
    _nat("drift_multiplier", drift_multiplier)
    _pos("drift_divisor", drift_divisor)
    if momentum_detail_numerator >= momentum_detail_divisor:
        raise ValueError("momentum detail must lie inside one lifted momentum cell")

    staged, sigma = divmod(
        whole_momentum_count * drift_multiplier,
        drift_divisor,
    )
    lifted = (
        momentum_detail_divisor * whole_momentum_count
        + momentum_detail_numerator
    )
    full_divisor = momentum_detail_divisor * drift_divisor
    direct, direct_remainder = divmod(lifted * drift_multiplier, full_divisor)
    formula = (
        momentum_detail_divisor * sigma
        + momentum_detail_numerator * drift_multiplier
    ) // full_divisor
    defect = direct - staged
    if defect < 0:
        raise AssertionError("positive retained momentum detail reduced oriented displacement")
    if defect != formula:
        raise AssertionError("lifted drift defect disagrees with exact remainder formula")
    return LiftedMomentumDriftStagingReport(
        whole_momentum_count=whole_momentum_count,
        momentum_detail_numerator=momentum_detail_numerator,
        momentum_detail_divisor=momentum_detail_divisor,
        drift_multiplier=drift_multiplier,
        drift_divisor=drift_divisor,
        staged_displacement_count=staged,
        staged_drift_remainder=sigma,
        direct_lifted_displacement_count=direct,
        direct_lifted_remainder=direct_remainder,
        displacement_defect_count=defect,
        defect_formula_count=formula,
    )
