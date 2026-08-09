"""Terminal shell stratification as an exact re-encoding of Barlow history.

For fixed final radius n, every non-extreme unsigned height q<n carries a
shortest-path total that is strictly increasing with the absolute prefix drift
d=|delta_q|.  More strongly, d is decoded by an exact 2-adic formula.  The
extreme height q=n is the one boundary where path total is always 3^n, but its
layer cardinality recovers d by one integer square root.

Hence one terminal stratified profile -- non-extreme layer path totals plus
extreme layer cardinalities, retaining unsigned height but not side labels --
is equivalent to the complete coordination history S_0,...,S_n up to the same
positive/negative side exchange already present in whole-shell observations.
"""

from __future__ import annotations

from math import comb, isqrt

from .p022_barlow_coordination import (
    barlow_shell_vertex_count_from_extreme_imbalances,
)
from .p022_barlow_coordination_history import DriftHistory
from .p022_barlow_layer_tradeoff import (
    layer_ball_slice_count,
    layer_shell_geodesic_total,
)

LayerPair = tuple[int, int]
TerminalProfile = tuple[LayerPair, ...]


def _normalize_pair(left: int, right: int) -> LayerPair:
    return (left, right) if left <= right else (right, left)


def terminal_stratified_profile_from_drift_history(
    radius: int, drift_history: DriftHistory
) -> TerminalProfile:
    """Encode full drift history into one radius-n height-stratified profile."""
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


def _is_power_of_two(value: int) -> bool:
    return value > 0 and value & (value - 1) == 0


def _invert_nonextreme_path_total(radius: int, height: int, value: int) -> int:
    """Closed 2-adic inversion of one non-extreme layer path total.

    From

      L=C(n,q)[3*2^(n-q+(q-d)/2)(1+2^d)-6]

    form

      Y=(L/C(n,q)+6)/(3*2^(n-q))
       =2^((q-d)/2)+2^((q+d)/2).

    If Y is a power of two, the two exponents coincide and d=0. Otherwise
    v2(Y) is the smaller exponent and ``Y/2^v2(Y)-1`` is exactly ``2^d``.
    """
    if not (0 <= height < radius):
        raise ValueError("2-adic path inversion requires 0<=height<radius")
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("path total must be a positive integer")
    binomial = comb(radius, height)
    if value % binomial:
        raise ValueError("path total is incompatible with layer interleaving")
    scaled = value // binomial + 6
    denominator = 3 * (2 ** (radius - height))
    if scaled % denominator:
        raise ValueError("path total is incompatible with Barlow powers of two")
    encoded = scaled // denominator

    if _is_power_of_two(encoded):
        if height % 2:
            raise ValueError("odd height cannot have zero absolute drift")
        expected = 2 ** (height // 2 + 1)
        if encoded != expected:
            raise ValueError("power-of-two layer total has the wrong exponent")
        return 0

    low_bit = encoded & -encoded
    odd_part = encoded // low_bit
    drift_power = odd_part - 1
    if not _is_power_of_two(drift_power):
        raise ValueError("layer total does not encode one Barlow drift power")
    drift = drift_power.bit_length() - 1
    smaller_exponent = low_bit.bit_length() - 1
    if drift > height or (height - drift) % 2:
        raise ValueError("decoded drift has incompatible height parity")
    if smaller_exponent != (height - drift) // 2:
        raise ValueError("decoded 2-adic exponent is inconsistent with height")
    return drift


def _invert_extreme_vertex_count(radius: int, value: int) -> int:
    """Closed integer-square inversion of one extreme layer cardinality."""
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("extreme layer count must be a positive integer")
    square = 3 * radius * radius + 6 * radius + 4 - 4 * value
    if square < 0:
        raise ValueError("extreme layer count exceeds the Barlow bound")
    drift = isqrt(square)
    if drift * drift != square:
        raise ValueError("extreme layer count does not encode an integral drift")
    if drift > radius or (radius - drift) % 2:
        raise ValueError("extreme drift has incompatible radius parity")
    return drift


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
