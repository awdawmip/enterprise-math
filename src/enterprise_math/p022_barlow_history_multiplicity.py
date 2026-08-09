"""Reconstruct Barlow geodesic multiplicity spectra from coordination history.

The coordination history S_0,...,S_n reconstructs, at every unsigned height q,
the unordered pair {|delta_q|,|delta_-q|}.  A target-layer shortest-path
multiplicity histogram depends only on q and |delta_q| up to coordinate
reflection.  Therefore the whole radius-n multiplicity spectrum is an exact
factor of the coordination history, even though the single terminal shell
cardinality S_n is not sufficient.
"""

from __future__ import annotations

from .p022_barlow_coordination_history import (
    DriftHistory,
    reconstruct_unordered_drift_history,
)
from .p022_barlow_stacking import barlow_distance_and_geodesic_count

Spectrum = tuple[tuple[int, int], ...]


def _require_layer_state(radius: int, height: int, absolute_drift: int) -> None:
    for name, value in (
        ("radius", radius),
        ("height", height),
        ("absolute_drift", absolute_drift),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"{name} must be a non-negative integer")
    if height > radius:
        raise ValueError("height cannot exceed radius")
    if absolute_drift > height or (height - absolute_drift) % 2:
        raise ValueError("absolute drift is incompatible with height")


def _canonical_prefix_pattern(height: int, absolute_drift: int) -> tuple[int, ...]:
    """One representative prefix with the requested non-negative imbalance."""
    if height == 0:
        # The stacking API requires a nonempty periodic pattern, but target
        # layer zero traverses no interfaces so the actual sign is irrelevant.
        return (1,)
    plus = (height + absolute_drift) // 2
    minus = (height - absolute_drift) // 2
    return (1,) * plus + (-1,) * minus


def layer_geodesic_multiplicity_spectrum(
    radius: int, height: int, absolute_drift: int
) -> Spectrum:
    """Exact shortest-path multiplicity histogram on one unsigned-height layer.

    Signed drift reversal reflects the axial coordinate system and therefore
    preserves the multiplicity histogram.  Literal order inside the traversed
    prefix is invisible by the Barlow normal form, so ``(height,|delta|)`` is
    sufficient.
    """
    _require_layer_state(radius, height, absolute_drift)
    pattern = _canonical_prefix_pattern(height, absolute_drift)
    counts: dict[int, int] = {}

    # Every shortest path of length radius changes each axial coordinate by at
    # most radius in absolute value.  This finite box therefore contains every
    # endpoint on the requested layer; the exact distance filter removes the
    # rest.
    for first in range(-radius, radius + 1):
        for second in range(-radius, radius + 1):
            distance, multiplicity = barlow_distance_and_geodesic_count(
                (first, second, height), pattern
            )
            if distance == radius:
                counts[multiplicity] = counts.get(multiplicity, 0) + 1
    return tuple(sorted(counts.items()))


def _add_spectrum(target: dict[int, int], spectrum: Spectrum) -> None:
    for multiplicity, endpoint_count in spectrum:
        target[multiplicity] = target.get(multiplicity, 0) + endpoint_count


def global_multiplicity_spectrum_from_drift_history(
    radius: int, drift_history: DriftHistory
) -> Spectrum:
    """Whole-shell spectrum from unordered two-sided absolute drift history."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    if len(drift_history) <= radius or drift_history[0] != (0, 0):
        raise ValueError("drift history must contain radii 0..radius")

    counts: dict[int, int] = {}
    _add_spectrum(counts, layer_geodesic_multiplicity_spectrum(radius, 0, 0))
    for height in range(1, radius + 1):
        first, second = drift_history[height]
        _add_spectrum(
            counts,
            layer_geodesic_multiplicity_spectrum(radius, height, first),
        )
        _add_spectrum(
            counts,
            layer_geodesic_multiplicity_spectrum(radius, height, second),
        )
    return tuple(sorted(counts.items()))


def global_multiplicity_spectrum_from_coordination_history(
    shell_cardinalities: tuple[int, ...],
) -> Spectrum:
    """Exact map ``(S_0,...,S_n) ->`` radius-n multiplicity spectrum."""
    drift_history = reconstruct_unordered_drift_history(shell_cardinalities)
    return global_multiplicity_spectrum_from_drift_history(
        len(shell_cardinalities) - 1, drift_history
    )


def spectrum_shell_cardinality(spectrum: Spectrum) -> int:
    """Number of shell endpoints represented by a multiplicity spectrum."""
    return sum(endpoint_count for _, endpoint_count in spectrum)


def spectrum_total_geodesic_paths(spectrum: Spectrum) -> int:
    """Total shortest-path count represented by a multiplicity spectrum."""
    return sum(
        multiplicity * endpoint_count
        for multiplicity, endpoint_count in spectrum
    )
