"""E001.6 spatial-collapse x primitive-motion integer phase diagnostics.

This module follows the active E001 precision-direction decision:

* larger ``collapse_factor d`` = coarser / more macroscopic spatial precision;
* smaller ``d`` = finer / more microscopic refinement;
* terminal spatial factor is ``d=1``.

For finite E001 square supports let ``g`` be their primitive Chebyshev clearance:
``g=0`` exactly when the terminal supports overlap, and ``g>0`` is a positive
integer graph-step separation.  The candidate macro contact law is

    Contact_d(g)  iff  g // d == 0  iff  g < d.

Thus a positive terminal clearance may collapse to contact at coarse scales and
then disappear under refinement once ``d <= g``.

The 1D crossing model also keeps a separate transition/time coordinate.  For
support radii ``r_left,r_right``, let ``R=r_left+r_right`` and signed center
separation be ``q``.  Macro contact at factor ``d`` is

    |q| <= R + d - 1.

Hence the symmetric interaction band contains exactly

    h = 2*(R+d)-1

integer q-states.  A monotone arithmetic-progression crossing with positive
relative step magnitude ``s`` is guaranteed, for every phase, to sample at
least one band state iff ``s <= h``.  If ``s>h``, the explicit one-step phase
``q0=H+1 -> q1=H+1-s`` with ``H=R+d-1`` skips the whole band.

This is a static-sampling theorem, not a physical rebound law.  E001 primitive
transition targets can still detect some crossings (e.g. an atomic edge swap)
that static endpoint sampling misses.  Longer nonprimitive jumps remain outside
the current transition contract and should be decomposed/refined rather than
silently interpolated through a continuum.
"""

from __future__ import annotations

from dataclasses import dataclass

from .engineering_collision import Body2D


@dataclass(frozen=True)
class CollisionPhase1D:
    """One finite point in the spatial-collapse / relative-motion phase plane."""

    radius_sum: int
    collapse_factor: int
    relative_step: int
    contact_half_width: int
    interaction_band_states: int
    static_no_skip_guaranteed: bool
    skip_witness: tuple[int, int] | None


def _require_nonnegative_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def primitive_clearance(left: Body2D, right: Body2D) -> int:
    """Exact terminal Chebyshev clearance between two square supports."""
    radius_sum = left.radius + right.radius
    center_distance = max(abs(left.x - right.x), abs(left.y - right.y))
    return max(0, center_distance - radius_sum)


def coarse_clearance(primitive_gap: int, collapse_factor: int) -> int:
    """Collapse a non-negative primitive clearance by one integer spatial factor."""
    _require_nonnegative_int("primitive_gap", primitive_gap)
    _require_positive_int("collapse_factor", collapse_factor)
    return primitive_gap // collapse_factor


def macro_contact_from_gap(primitive_gap: int, collapse_factor: int) -> bool:
    """Candidate collapse-contact observable: coarse clearance has collapsed to zero."""
    return coarse_clearance(primitive_gap, collapse_factor) == 0


def finest_contact_factor(primitive_gap: int) -> int | None:
    """Smallest (finest) integer factor that still reports macro contact.

    ``None`` means primitive contact ``g=0`` persists even at terminal factor 1.
    For positive ``g``, contact exists exactly for ``d>=g+1``, so ``g+1`` is the
    finest still-contact factor and refinement to ``d=g`` is the first resolved
    non-contact level when that integer level exists.
    """
    _require_nonnegative_int("primitive_gap", primitive_gap)
    if primitive_gap == 0:
        return None
    return primitive_gap + 1


def first_resolving_factor(primitive_gap: int) -> int | None:
    """Largest threshold value at which positive clearance is no longer collapsed.

    With all positive integer factors available, a positive gap ``g`` is
    non-contact exactly for ``d<=g``.  Therefore ``d=g`` is the coarse-to-fine
    threshold where the contact first disappears.  Primitive contact has no
    resolving factor in this model.
    """
    _require_nonnegative_int("primitive_gap", primitive_gap)
    return None if primitive_gap == 0 else primitive_gap


def contact_half_width_1d(radius_sum: int, collapse_factor: int) -> int:
    """Maximum absolute signed center separation still in macro contact."""
    _require_nonnegative_int("radius_sum", radius_sum)
    _require_positive_int("collapse_factor", collapse_factor)
    return radius_sum + collapse_factor - 1


def interaction_band_states_1d(radius_sum: int, collapse_factor: int) -> int:
    """Number of integer signed-separation states in the symmetric contact band."""
    half_width = contact_half_width_1d(radius_sum, collapse_factor)
    return 2 * half_width + 1


def static_no_skip_guaranteed_1d(
    radius_sum: int,
    collapse_factor: int,
    relative_step: int,
) -> bool:
    """Phase-independent static-sampling criterion for monotone 1D crossing.

    ``relative_step`` is the positive magnitude by which signed center
    separation changes each tick.  Zero means no crossing progress and is
    trivially non-skipping.
    """
    _require_nonnegative_int("relative_step", relative_step)
    band = interaction_band_states_1d(radius_sum, collapse_factor)
    return relative_step <= band


def minimum_factor_for_static_no_skip_1d(radius_sum: int, relative_step: int) -> int:
    """Finest integer spatial factor that guarantees no static band skip.

    Solve ``s <= 2*(R+d)-1`` for integer ``d>=1``:

        d >= ceil((s+1)/2) - R.

    The returned factor is clamped at terminal factor 1.
    """
    _require_nonnegative_int("radius_sum", radius_sum)
    _require_nonnegative_int("relative_step", relative_step)
    required = (relative_step + 2) // 2 - radius_sum
    return max(1, required)


def static_skip_witness_1d(
    radius_sum: int,
    collapse_factor: int,
    relative_step: int,
) -> tuple[int, int] | None:
    """Return an explicit one-tick phase that skips the contact band when possible."""
    _require_nonnegative_int("relative_step", relative_step)
    if static_no_skip_guaranteed_1d(radius_sum, collapse_factor, relative_step):
        return None
    half_width = contact_half_width_1d(radius_sum, collapse_factor)
    start = half_width + 1
    end = start - relative_step
    if not (start > half_width and end < -half_width):
        raise AssertionError("constructed skip witness did not cross the full band")
    return start, end


def collision_phase_1d(
    radius_sum: int,
    collapse_factor: int,
    relative_step: int,
) -> CollisionPhase1D:
    """Return exact integer phase diagnostics for one 1D scale/motion point."""
    half_width = contact_half_width_1d(radius_sum, collapse_factor)
    band = interaction_band_states_1d(radius_sum, collapse_factor)
    no_skip = static_no_skip_guaranteed_1d(radius_sum, collapse_factor, relative_step)
    witness = static_skip_witness_1d(radius_sum, collapse_factor, relative_step)
    return CollisionPhase1D(
        radius_sum=radius_sum,
        collapse_factor=collapse_factor,
        relative_step=relative_step,
        contact_half_width=half_width,
        interaction_band_states=band,
        static_no_skip_guaranteed=no_skip,
        skip_witness=witness,
    )
