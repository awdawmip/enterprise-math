"""Self-certified nested intervals for the pi-free Euler rotation-root tower.

Every endpoint is computed from finitely many Decimal square roots.  The module does
not import or compare with a target numerical value of pi.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext

from enterprise_math.rotation_phase_refinement import dyadic_trace_data


@dataclass(frozen=True)
class RotationPrecisionInterval:
    level: int
    lower: Decimal
    next_half_trace: Decimal
    defect_ratio_bound: Decimal
    total_tail_defect_bound: Decimal
    upper: Decimal
    certified_width: Decimal


def rotation_precision_intervals(
    depth: int, *, precision: int = 100
) -> tuple[RotationPrecisionInterval, ...]:
    """Return the certified intervals at levels 1..depth."""

    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 1:
        raise ValueError("depth must be a positive integer")
    if isinstance(precision, bool) or not isinstance(precision, int) or precision < 30:
        raise ValueError("precision must be an integer at least 30")
    traces = dyadic_trace_data(depth + 1, precision=precision)
    with localcontext() as context:
        context.prec = precision
        one = Decimal(1)
        two = Decimal(2)
        result: list[RotationPrecisionInterval] = []
        for level in range(1, depth + 1):
            lower = traces[level - 1].finite_half_slope
            next_half_trace = traces[level].half_trace
            ratio = one / (two * (one + next_half_trace))
            total_defect = (one - next_half_trace) / (one - ratio)
            if not (Decimal(0) < total_defect < one):
                raise AssertionError("tail defect bound must lie strictly between zero and one")
            upper = lower / (one - total_defect)
            result.append(
                RotationPrecisionInterval(
                    level=level,
                    lower=+lower,
                    next_half_trace=+next_half_trace,
                    defect_ratio_bound=+ratio,
                    total_tail_defect_bound=+total_defect,
                    upper=+upper,
                    certified_width=+(upper - lower),
                )
            )
        return tuple(result)


def verify_nested_rotation_precision_intervals(
    depth: int = 30, *, precision: int = 120
) -> bool:
    """Check strict lower growth and strict upper decay without using pi."""

    intervals = rotation_precision_intervals(depth, precision=precision)
    for item in intervals:
        if not item.lower < item.upper:
            return False
        if item.certified_width != item.upper - item.lower:
            return False
    for left, right in zip(intervals, intervals[1:]):
        if not left.lower < right.lower:
            return False
        if not right.upper < left.upper:
            return False
        if not right.lower < left.upper:
            return False
    return True


def certificate(depth: int = 16, *, precision: int = 100) -> dict[str, object]:
    intervals = rotation_precision_intervals(depth, precision=precision)
    return {
        "verified_nested": verify_nested_rotation_precision_intervals(
            depth, precision=precision
        ),
        "intervals": [
            {
                "level": item.level,
                "lower": str(item.lower),
                "upper": str(item.upper),
                "width": str(item.certified_width),
                "next_half_trace": str(item.next_half_trace),
                "defect_ratio_bound": str(item.defect_ratio_bound),
                "total_tail_defect_bound": str(item.total_tail_defect_bound),
            }
            for item in intervals
        ],
        "construction": "finite nested radicals only; no target numerical pi",
    }


if __name__ == "__main__":
    import json

    print(json.dumps(certificate(), indent=2, ensure_ascii=False))
