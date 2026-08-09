"""Terminal shell stratification as an exact re-encoding of Barlow history.

For fixed final radius n, every non-extreme unsigned height q<n carries a
shortest-path total that is strictly increasing with the absolute prefix drift
d=|delta_q|.  The extreme height q=n is the one boundary where path total is
always 3^n, but its layer cardinality is strictly decreasing in d.

Hence one terminal stratified profile -- non-extreme layer path totals plus
extreme layer cardinalities, retaining unsigned height but not side labels --
is equivalent to the complete coordination history S_0,...,S_n up to the same
positive/negative side exchange already present in whole-shell observations.
"""

from __future__ import annotations

from .p022_barlow_coordination import (
    barlow_shell_vertex_count_from_extreme_imbalances,
)
from .p022_barlow_coordination_history import DriftHistory
from .p022_barlow_layer_tradeoff import (
    layer_ball_slice_count,
    layer_shell_geodesic_total,
)

LayerPair = tuple[int, int]
TerminalProfile = tuple[LayerPair, ...]  # index q=0..n; q=0 uses one duplicated fixed value


def _normalize_pair(left: int, right: int) -> LayerPair:
    return (left, right) if left <= right else (right, left)


def terminal_stratified_profile_from_drift_history(
    radius: int, drift_history: DriftHistory
) -> TerminalProfile:
    """Encode full drift history into one radius-n height-stratified profile.

    Entry q<n is the unordered pair of shell-layer geodesic totals at heights
    +q and -q.  Entry q=n is instead the unordered pair of extreme-layer vertex
    counts, because extreme path totals are drift-independent.
    """
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be non-negative")
    if len(drift_history) <= radius or drift_history[0] != (0, 0):
        raise ValueError("drift_history must contain radii 0..radius")
    if radius == 0:
        return ((1, 1),)

    central = layer_shell_geodesic_total(radius, 0, 0)
    output: list[LayerPair] = [(central, central)]
    for height in range(1, radius):
        left_drift, right_drift = drift_history[height]
        output.append(
            _normalize_pair(
                layer_shell_geodesic_total(radius, height, left_drift),
                layer_shell_geodesic_total(radius, height, right_drift),
            )
        )

    left_drift, right_drift = drift_history[radius]
    output.append(
        _normalize_pair(
            layer_ball_slice_count(radius, radius, left_drift),
            layer_ball_slice_count(radius, radius, right_drift),
        )
    )
    return tuple(output)


def _allowed_absolute_drifts(height: int) -> tuple[int, ...]:
    return tuple(range(height % 2, height + 1, 2))


def _invert_nonextreme_path_total(radius: int, height: int, value: int) -> int:
    candidates = [
        drift
        for drift in _allowed_absolute_drifts(height)
        if layer_shell_geodesic_total(radius, height, drift) == value
    ]
    if len(candidates) != 1:
        raise ValueError("non-extreme path total does not encode one legal drift")
    return candidates[0]


def _invert_extreme_vertex_count(radius: int, value: int) -> int:
    candidates = [
        drift
        for drift in _allowed_absolute_drifts(radius)
        if layer_ball_slice_count(radius, radius, drift) == value
    ]
    if len(candidates) != 1:
        raise ValueError("extreme layer count does not encode one legal drift")
    return candidates[0]


def drift_history_from_terminal_stratified_profile(
    profile: TerminalProfile,
) -> DriftHistory:
    """Invert one terminal stratified profile to the unordered drift history."""
    if not isinstance(profile, tuple) or not profile:
        raise ValueError("profile must be a nonempty tuple")
    radius = len(profile) - 1
    if radius == 0:
        if profile != ((1, 1),):
            raise ValueError("radius-zero terminal profile is fixed")
        return ((0, 0),)

    output: list[LayerPair] = [(0, 0)]
    expected_central = layer_shell_geodesic_total(radius, 0, 0)
    if profile[0] != (expected_central, expected_central):
        raise ValueError("central layer profile is incompatible with radius")

    for height in range(1, radius):
        left_value, right_value = profile[height]
        output.append(
            _normalize_pair(
                _invert_nonextreme_path_total(radius, height, left_value),
                _invert_nonextreme_path_total(radius, height, right_value),
            )
        )

    left_value, right_value = profile[radius]
    output.append(
        _normalize_pair(
            _invert_extreme_vertex_count(radius, left_value),
            _invert_extreme_vertex_count(radius, right_value),
        )
    )
    return tuple(output)


def coordination_history_from_terminal_stratified_profile(
    profile: TerminalProfile,
) -> tuple[int, ...]:
    """Recover ``(S_0,...,S_n)`` from one terminal shell stratification."""
    drift_history = drift_history_from_terminal_stratified_profile(profile)
    output = [1]
    for radius in range(1, len(drift_history)):
        left, right = drift_history[radius]
        output.append(
            barlow_shell_vertex_count_from_extreme_imbalances(
                radius, left, right
            )
        )
    return tuple(output)
