"""Budget-relative visibility of finite 2D material anisotropy.

``material_anisotropy_2d`` asks which clearance witness is needed to preserve
*raw material response*. A downstream world may care only about the integer
kinematic return

    K_B(r) = floor(B*r/A).

That quotient can alias distinct x/y/corner material samples. Consequently the
minimum clearance observable needed for the declared future kinematic operation
can be strictly coarser than the material-level observable and can change
nonmonotonically with incoming budget because quotient remainders change.

Only depths reachable at the declared collapse factor are tested. This is an
E001 finite specialization of future-language-relative state retention; generic
clearance observable names come from canonical ``clearance_precision``.
"""

from __future__ import annotations

from dataclasses import dataclass

from .clearance_precision import ACTIVE_COUNT, ACTIVE_SET, SCALAR_DEPTH
from .material_anisotropy_2d import AnisotropicMaterialProfile2D
from .material_hysteresis import LOADING, RETURNING


def _branch(profile, branch: str) -> tuple[int, ...]:
    if branch == LOADING:
        return profile.loading
    if branch == RETURNING:
        return profile.returning
    raise ValueError("branch must be LOADING or RETURNING")


@dataclass(frozen=True, order=True)
class AnisotropyVisibilityDepth2D:
    layer_depth: int
    x_response: int
    y_response: int
    corner_response: int
    x_returned_budget: int
    y_returned_budget: int
    corner_returned_budget: int
    minimum_clearance_observable: str


@dataclass(frozen=True)
class AnisotropyVisibility2D:
    collapse_factor: int
    incoming_budget: int
    branch: str
    represented_max_depth: int
    minimum_clearance_observable: str
    depths: tuple[AnisotropyVisibilityDepth2D, ...]


def _minimum_from_outputs(x: int, y: int, corner: int) -> str:
    if x == y == corner:
        return SCALAR_DEPTH
    if x == y:
        return ACTIVE_COUNT
    return ACTIVE_SET


def kinematic_anisotropy_visibility_2d(
    profile: AnisotropicMaterialProfile2D,
    collapse_factor: int,
    incoming_budget: int,
    branch: str = RETURNING,
) -> AnisotropyVisibility2D:
    """Return the coarsest clearance signature preserving current kinematic output."""
    if (
        isinstance(collapse_factor, bool)
        or not isinstance(collapse_factor, int)
        or collapse_factor <= 0
    ):
        raise ValueError("collapse_factor must be a positive integer")
    if (
        isinstance(incoming_budget, bool)
        or not isinstance(incoming_budget, int)
        or incoming_budget < 0
    ):
        raise ValueError("incoming_budget must be a non-negative integer")

    x_samples = _branch(profile.x_profile, branch)
    y_samples = _branch(profile.y_profile, branch)
    c_samples = _branch(profile.corner_profile, branch)
    represented_max = min(profile.depth_count - 1, collapse_factor - 1)
    depth_reports: list[AnisotropyVisibilityDepth2D] = []
    required = SCALAR_DEPTH
    for depth in range(1, represented_max + 1):
        x_response = x_samples[depth]
        y_response = y_samples[depth]
        corner_response = c_samples[depth]
        x_budget = incoming_budget * x_response // profile.amplitude
        y_budget = incoming_budget * y_response // profile.amplitude
        corner_budget = incoming_budget * corner_response // profile.amplitude
        local = _minimum_from_outputs(x_budget, y_budget, corner_budget)
        if local == ACTIVE_SET:
            required = ACTIVE_SET
        elif local == ACTIVE_COUNT and required == SCALAR_DEPTH:
            required = ACTIVE_COUNT
        depth_reports.append(
            AnisotropyVisibilityDepth2D(
                layer_depth=depth,
                x_response=x_response,
                y_response=y_response,
                corner_response=corner_response,
                x_returned_budget=x_budget,
                y_returned_budget=y_budget,
                corner_returned_budget=corner_budget,
                minimum_clearance_observable=local,
            )
        )
    return AnisotropyVisibility2D(
        collapse_factor=collapse_factor,
        incoming_budget=incoming_budget,
        branch=branch,
        represented_max_depth=represented_max,
        minimum_clearance_observable=required,
        depths=tuple(depth_reports),
    )