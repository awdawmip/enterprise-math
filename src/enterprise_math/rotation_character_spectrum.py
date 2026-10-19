"""Finite-difference spectrum of the dyadic Enterprise rotation character.

The module consumes the pi-free half-trace recursion from
``rotation_phase_refinement``.  It checks exact structural identities numerically at
arbitrary Decimal precision; no target numerical value of pi enters the recurrence.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction

from enterprise_math.rotation_phase_refinement import dyadic_trace_data


@dataclass(frozen=True)
class RotationSpectrumDatum:
    level: int
    phase_step: Fraction
    half_trace: Decimal
    skew_trace: Decimal
    precision_readout: Decimal
    skew_eigenvalue_magnitude: Decimal
    positive_laplacian_eigenvalue: Decimal
    next_precision_readout: Decimal


def rotation_spectrum_data(
    depth: int, *, precision: int = 100
) -> tuple[RotationSpectrumDatum, ...]:
    """Return levels 1..depth and their finite first/second-difference spectra."""

    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 1:
        raise ValueError("depth must be a positive integer")
    if isinstance(precision, bool) or not isinstance(precision, int) or precision < 30:
        raise ValueError("precision must be an integer at least 30")
    traces = dyadic_trace_data(depth + 1, precision=precision)
    with localcontext() as context:
        context.prec = precision
        two = Decimal(2)
        out: list[RotationSpectrumDatum] = []
        for level in range(1, depth + 1):
            trace = traces[level - 1]
            next_trace = traces[level]
            step = Fraction(1, 2 ** (level + 1))
            step_decimal = Decimal(step.numerator) / Decimal(step.denominator)
            skew_eigenvalue = trace.skew_trace / step_decimal
            laplacian_eigenvalue = (
                two * (Decimal(1) - trace.half_trace) / (step_decimal * step_decimal)
            )
            out.append(
                RotationSpectrumDatum(
                    level=level,
                    phase_step=step,
                    half_trace=trace.half_trace,
                    skew_trace=trace.skew_trace,
                    precision_readout=trace.finite_half_slope,
                    skew_eigenvalue_magnitude=+skew_eigenvalue,
                    positive_laplacian_eigenvalue=+laplacian_eigenvalue,
                    next_precision_readout=next_trace.finite_half_slope,
                )
            )
        return tuple(out)


def verify_rotation_spectrum(
    depth: int = 24, *, precision: int = 120
) -> bool:
    """Check the exact finite spectral identities within Decimal rounding tolerance."""

    tolerance = Decimal(10) ** (-(precision // 2))
    for item in rotation_spectrum_data(depth, precision=precision):
        if abs(
            item.skew_eigenvalue_magnitude - Decimal(2) * item.precision_readout
        ) > tolerance:
            return False
        if abs(
            item.positive_laplacian_eigenvalue
            - Decimal(4) * item.next_precision_readout * item.next_precision_readout
        ) > tolerance:
            return False
        if abs(
            item.skew_eigenvalue_magnitude * item.skew_eigenvalue_magnitude
            - ((Decimal(1) + item.half_trace) / Decimal(2))
            * item.positive_laplacian_eigenvalue
        ) > tolerance:
            return False
    return True


def certificate(depth: int = 12, *, precision: int = 100) -> dict[str, object]:
    data = rotation_spectrum_data(depth, precision=precision)
    return {
        "verified": verify_rotation_spectrum(depth, precision=precision),
        "levels": [
            {
                "level": item.level,
                "phase_step": str(item.phase_step),
                "precision_readout": str(item.precision_readout),
                "skew_eigenvalue_magnitude": str(item.skew_eigenvalue_magnitude),
                "positive_laplacian_eigenvalue": str(
                    item.positive_laplacian_eigenvalue
                ),
                "next_precision_readout": str(item.next_precision_readout),
            }
            for item in data
        ],
        "identities": [
            "skew_eigenvalue_magnitude = 2*precision_readout",
            "positive_laplacian_eigenvalue = 4*next_precision_readout^2",
            "skew_eigenvalue_magnitude^2 = ((1+half_trace)/2)*positive_laplacian_eigenvalue",
        ],
        "boundary": "finite phase spectrum only; no native line-metric identity asserted",
    }


if __name__ == "__main__":
    import json

    print(json.dumps(certificate(), indent=2, ensure_ascii=False))
