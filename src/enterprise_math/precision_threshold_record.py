"""Exact threshold-record generator for the R004 P016 premodel continuation.

This is a deliberately small physical-hypothesis toy.  It removes the free
``eta`` parameter from one subfamily by deriving finite record overlap from two
integer quantities: a record resolution ``d`` and an alternative separation
``delta``.  It does not claim that a real interferometer implements this map.
"""
from __future__ import annotations

from fractions import Fraction


def _nat(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _pos(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def threshold_record(system_state: int, environment_state: int, resolution: int) -> int:
    """Finite quotient record ``floor((e+x)/d)`` using exact integer division."""
    _nat(system_state, "system_state")
    _nat(environment_state, "environment_state")
    _pos(resolution, "resolution")
    if environment_state >= resolution:
        raise ValueError("environment_state must lie in the declared d-state cell")
    return (environment_state + system_state) // resolution


def threshold_record_overlap(separation: int, resolution: int) -> Fraction:
    """Fraction of d environment states giving the same record for 0 and delta.

    Exactly ``max(d-delta,0)`` of ``e=0,...,d-1`` satisfy
    ``floor(e/d)=floor((e+delta)/d)``.
    """
    _nat(separation, "separation")
    _pos(resolution, "resolution")
    agreement = max(resolution - separation, 0)
    return Fraction(agreement, resolution)


def overlap_count_by_enumeration(separation: int, resolution: int) -> int:
    _nat(separation, "separation")
    _pos(resolution, "resolution")
    return sum(
        threshold_record(0, environment_state, resolution)
        == threshold_record(separation, environment_state, resolution)
        for environment_state in range(resolution)
    )


def representative_visibility_region_excluded(
    separation: int,
    resolution: int,
    observed_lower_visibility: Fraction = Fraction(9, 100),
) -> bool:
    """Algebraic exclusion under ``V_predicted=eta*V_ordinary`` and V_ordinary<=1.

    The model can reach an observed visibility lower bound only if
    ``eta >= observed_lower_visibility``.  This is a range check, not a
    confidence-level statement.
    """
    if not isinstance(observed_lower_visibility, Fraction):
        raise ValueError("observed lower visibility must be an exact Fraction")
    if not 0 <= observed_lower_visibility <= 1:
        raise ValueError("observed lower visibility must lie in [0,1]")
    return threshold_record_overlap(separation, resolution) < observed_lower_visibility


def pedalino_representative_region_excluded(separation: int, resolution: int) -> bool:
    """Exact cross-multiplied form of eta<9/100 for the declared toy subfamily."""
    _nat(separation, "separation")
    _pos(resolution, "resolution")
    return 100 * separation > 91 * resolution
