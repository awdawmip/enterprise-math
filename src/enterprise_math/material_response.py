"""E001 finite material-curve composition over integer response samples.

The functions in this module are finite curve constructors/observables, not
physical constitutive laws.  A complete material profile has two explicit
branches—loading/compression and returning/rebound—on one common finite response
scale.

A validated loading branch alone is deliberately **not** a complete profile.
Empirical data may enter world dynamics only after a return branch is supplied
by independent data or by an explicitly declared modeling/comparator policy.
The helper ``explicit_material_curve_profile`` exists to make that assembly
visible instead of silently inventing unloading behavior.
"""

from __future__ import annotations

from dataclasses import dataclass

from .core import integer_nth_root


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _validate_sample(sample: int, amplitude: int) -> None:
    _require_natural("sample", sample)
    _require_positive("amplitude", amplitude)
    if sample > amplitude:
        raise ValueError("sample must not exceed amplitude")


def hardening_sample(sample: int, amplitude: int, power: int) -> int:
    """Scale-preserving integer power transform H_p(s;A)."""
    _validate_sample(sample, amplitude)
    _require_positive("power", power)
    return sample**power // amplitude ** (power - 1)


def softening_sample(sample: int, amplitude: int, power: int) -> int:
    """Scale-preserving integer root transform G_p(s;A)."""
    _validate_sample(sample, amplitude)
    _require_positive("power", power)
    return integer_nth_root(sample * amplitude ** (power - 1), power)


def retained_sample(sample: int, amplitude: int, retention: int) -> int:
    """Apply an explicit 0..A integer retention factor on the same scale."""
    _validate_sample(sample, amplitude)
    _require_natural("retention", retention)
    if retention > amplitude:
        raise ValueError("retention must lie in 0..amplitude")
    return retention * sample // amplitude


def offset_sample(sample: int, amplitude: int, offset: int) -> int:
    """Translate one branch sample and clamp it to the finite amplitude range."""
    _validate_sample(sample, amplitude)
    if isinstance(offset, bool) or not isinstance(offset, int):
        raise ValueError("offset must be an integer")
    return min(amplitude, max(0, sample + offset))


def hardening_branch(
    samples: tuple[int, ...] | list[int], amplitude: int, power: int
) -> tuple[int, ...]:
    return tuple(hardening_sample(sample, amplitude, power) for sample in samples)


def softening_branch(
    samples: tuple[int, ...] | list[int], amplitude: int, power: int
) -> tuple[int, ...]:
    return tuple(softening_sample(sample, amplitude, power) for sample in samples)


def retained_branch(
    samples: tuple[int, ...] | list[int], amplitude: int, retention: int
) -> tuple[int, ...]:
    return tuple(retained_sample(sample, amplitude, retention) for sample in samples)


def branch_gap_sum(
    loading: tuple[int, ...] | list[int],
    returning: tuple[int, ...] | list[int],
) -> int:
    """Finite one-sided branch-gap sum Σ max(load-return,0)."""
    if len(loading) != len(returning):
        raise ValueError("loading and return branches must have equal length")
    total = 0
    for load, ret in zip(loading, returning, strict=True):
        _require_natural("loading sample", load)
        _require_natural("return sample", ret)
        total += max(load - ret, 0)
    return total


def signed_branch_area(
    loading: tuple[int, ...] | list[int],
    returning: tuple[int, ...] | list[int],
) -> int:
    if len(loading) != len(returning):
        raise ValueError("loading and return branches must have equal length")
    total = 0
    for load, ret in zip(loading, returning, strict=True):
        _require_natural("loading sample", load)
        _require_natural("return sample", ret)
        total += load - ret
    return total


@dataclass(frozen=True)
class MaterialCurveProfile:
    amplitude: int
    loading: tuple[int, ...]
    returning: tuple[int, ...]
    branch_gap: int
    signed_area: int
    peak_loading: int
    peak_returning: int


def explicit_material_curve_profile(
    loading: tuple[int, ...] | list[int],
    returning: tuple[int, ...] | list[int],
    amplitude: int,
) -> MaterialCurveProfile:
    """Assemble a complete profile from two explicitly supplied finite branches."""
    _require_positive("amplitude", amplitude)
    load = tuple(loading)
    ret = tuple(returning)
    if not load or len(load) != len(ret):
        raise ValueError("loading and return branches must be equal nonempty sequences")
    for sample in load:
        _validate_sample(sample, amplitude)
    for sample in ret:
        _validate_sample(sample, amplitude)
    return MaterialCurveProfile(
        amplitude=amplitude,
        loading=load,
        returning=ret,
        branch_gap=branch_gap_sum(load, ret),
        signed_area=signed_branch_area(load, ret),
        peak_loading=max(load),
        peak_returning=max(ret),
    )


def material_curve_profile(
    base_samples: tuple[int, ...] | list[int],
    amplitude: int,
    loading_power: int = 1,
    return_power: int = 1,
    return_retention: int | None = None,
    return_offset: int = 0,
) -> MaterialCurveProfile:
    """Generate both branches from one declared intrinsic/program-like base curve."""
    _require_positive("amplitude", amplitude)
    _require_positive("loading_power", loading_power)
    _require_positive("return_power", return_power)
    if return_retention is None:
        return_retention = amplitude
    _require_natural("return_retention", return_retention)
    if return_retention > amplitude:
        raise ValueError("return_retention must lie in 0..amplitude")
    if isinstance(return_offset, bool) or not isinstance(return_offset, int):
        raise ValueError("return_offset must be an integer")

    base = tuple(base_samples)
    for sample in base:
        _validate_sample(sample, amplitude)

    loading = hardening_branch(base, amplitude, loading_power)
    returning = softening_branch(base, amplitude, return_power)
    returning = retained_branch(returning, amplitude, return_retention)
    if return_offset:
        returning = tuple(
            offset_sample(sample, amplitude, return_offset) for sample in returning
        )
    return explicit_material_curve_profile(loading, returning, amplitude)
