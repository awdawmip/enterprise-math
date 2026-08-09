"""Exact staged-vs-direct finite projection defect from material response to impulse.

A finite material response ``r/A`` may first be quantized to a whole force count
and only then integrated to momentum, or it may be carried directly through the
declared force/time/momentum scales before the final projection.  These are not
semantically equivalent when the intermediate force remainder is discarded.

Let ``F`` be the full-scale force count, ``C`` the non-negative downstream
impulse multiplier (for example time-count times momentum-scale), and ``D`` the
positive force-to-momentum divisor.  Then

    direct = floor(r*F*C / (A*D)).

If force is projected first,

    r*F = A*q + rho,       0<=rho<A,
    q*C = D*s + sigma,     0<=sigma<D,

and the dropped-detail staged result is ``staged=s``.  Exactly

    direct - staged = floor((A*sigma + rho*C)/(A*D)).

The defect is non-negative and can exceed one whole momentum count.  Retaining
the force lift ``A*q+rho`` recovers the direct result exactly.

This is an E001 material specialization of future-language-dependent quotient
safety: an intermediate force quotient is safe for a future impulse task only
when its discarded remainder cannot alter that task.  The generic quotient
principle remains owned by A2/P023/P024.
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
class ResponseImpulseStagingReport:
    response_sample: int
    response_amplitude: int
    full_scale_force_count: int
    impulse_multiplier: int
    impulse_divisor: int
    force_count: int
    force_remainder: int
    staged_impulse_count: int
    staged_impulse_remainder: int
    direct_impulse_count: int
    direct_impulse_remainder: int
    defect_count: int
    defect_formula_count: int

    @property
    def intermediate_force_projection_safe(self) -> bool:
        return self.defect_count == 0


def response_impulse_staging_report(
    response_sample: int,
    response_amplitude: int,
    full_scale_force_count: int,
    impulse_multiplier: int,
    impulse_divisor: int,
) -> ResponseImpulseStagingReport:
    """Compare dropped-force-detail staging with one direct final projection."""
    _nat("response_sample", response_sample)
    _pos("response_amplitude", response_amplitude)
    _nat("full_scale_force_count", full_scale_force_count)
    _nat("impulse_multiplier", impulse_multiplier)
    _pos("impulse_divisor", impulse_divisor)
    if response_sample > response_amplitude:
        raise ValueError("response_sample must not exceed response_amplitude")

    force_count, force_remainder = divmod(
        response_sample * full_scale_force_count,
        response_amplitude,
    )
    staged_impulse, staged_remainder = divmod(
        force_count * impulse_multiplier,
        impulse_divisor,
    )

    direct_divisor = response_amplitude * impulse_divisor
    direct_impulse, direct_remainder = divmod(
        response_sample * full_scale_force_count * impulse_multiplier,
        direct_divisor,
    )
    defect_formula = (
        response_amplitude * staged_remainder
        + force_remainder * impulse_multiplier
    ) // direct_divisor
    defect = direct_impulse - staged_impulse
    if defect < 0:
        raise AssertionError("dropping a non-negative intermediate remainder improved the final count")
    if defect != defect_formula:
        raise AssertionError("staged projection defect disagrees with exact remainder formula")
    if (
        direct_impulse
        != (
            (response_amplitude * force_count + force_remainder)
            * impulse_multiplier
        )
        // direct_divisor
    ):
        raise AssertionError("retained force lift did not recover direct impulse projection")

    return ResponseImpulseStagingReport(
        response_sample=response_sample,
        response_amplitude=response_amplitude,
        full_scale_force_count=full_scale_force_count,
        impulse_multiplier=impulse_multiplier,
        impulse_divisor=impulse_divisor,
        force_count=force_count,
        force_remainder=force_remainder,
        staged_impulse_count=staged_impulse,
        staged_impulse_remainder=staged_remainder,
        direct_impulse_count=direct_impulse,
        direct_impulse_remainder=direct_remainder,
        defect_count=defect,
        defect_formula_count=defect_formula,
    )
