"""Charged static-horizon pressure test for Enterprise Math P019.

The algebraic comparison target is a Reissner-Nordstrom-type factor

    1 - a/n + b/n^2 = (n^2 - a*n + b) / n^2.

Here ``a`` and ``b`` are integer coefficients.  Their physical calibration to
mass, charge, G, c, and a typed unit system is deliberately outside this
integer-only executable core.
"""

from __future__ import annotations

from .core import collapse, integer_nth_root


def _positive(name: str, value: int) -> int:
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def _nonnegative(name: str, value: int) -> int:
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")
    return value


def charged_residual(radius: int, mass_coefficient: int, charge_square: int) -> int:
    """Return P(n)=n^2-a*n+b for nonnegative integer coefficients."""
    _nonnegative("radius", radius)
    _nonnegative("mass_coefficient", mass_coefficient)
    _nonnegative("charge_square", charge_square)
    return radius * radius - mass_coefficient * radius + charge_square


def charged_discriminant(mass_coefficient: int, charge_square: int) -> int:
    """Return Delta=a^2-4b."""
    _nonnegative("mass_coefficient", mass_coefficient)
    _nonnegative("charge_square", charge_square)
    return mass_coefficient * mass_coefficient - 4 * charge_square


def completed_square_difference(
    radius: int, mass_coefficient: int, charge_square: int
) -> int:
    """Return (2n-a)^2-Delta, which equals 4*P(n)."""
    residual = charged_residual(radius, mass_coefficient, charge_square)
    return 4 * residual


def discriminant_is_square_fixed_point(
    mass_coefficient: int, charge_square: int
) -> bool:
    """Return whether nonnegative Delta is fixed by square collapse."""
    delta = charged_discriminant(mass_coefficient, charge_square)
    return delta >= 0 and collapse(delta, 2) == delta


def integer_horizon_states(
    mass_coefficient: int, charge_square: int
) -> tuple[int, ...]:
    """Return all nonnegative integer zeros of P, with duplicates removed."""
    _nonnegative("mass_coefficient", mass_coefficient)
    _nonnegative("charge_square", charge_square)
    delta = charged_discriminant(mass_coefficient, charge_square)
    if delta < 0:
        return ()
    root = integer_nth_root(delta, 2)
    if root * root != delta:
        return ()
    # Delta == a^2 mod 4, so an exact square root has the same parity as a.
    lower = (mass_coefficient - root) // 2
    upper = (mass_coefficient + root) // 2
    if lower == upper:
        return (lower,)
    return (lower, upper)


def positive_horizon_states(
    mass_coefficient: int, charge_square: int
) -> tuple[int, ...]:
    """Return positive integer zeros; radius zero remains a separate boundary."""
    return tuple(
        radius
        for radius in integer_horizon_states(mass_coefficient, charge_square)
        if radius > 0
    )


def charged_phase(radius: int, mass_coefficient: int, charge_square: int) -> int:
    """Return -1, 0, +1 according to the sign of P(n)."""
    residual = charged_residual(radius, mass_coefficient, charge_square)
    return (residual > 0) - (residual < 0)


def trapped_interval(
    mass_coefficient: int, charge_square: int
) -> tuple[int, int] | None:
    """Return the positive integer interval on which P(n)<0, if nonempty."""
    _positive("mass_coefficient", mass_coefficient)
    _nonnegative("charge_square", charge_square)
    delta = charged_discriminant(mass_coefficient, charge_square)
    if delta <= 0:
        return None

    d = integer_nth_root(delta, 2)
    if d * d == delta:
        max_abs_state = d - 2
    else:
        max_abs_state = d if (d - mass_coefficient) % 2 == 0 else d - 1

    if max_abs_state < 0:
        return None
    lower = (mass_coefficient - max_abs_state) // 2
    upper = (mass_coefficient + max_abs_state) // 2
    lower = max(lower, 1)
    if lower > upper:
        return None
    return lower, upper


def horizon_boundary_complex(
    mass_coefficient: int, charge_square: int
) -> dict[str, tuple[object, ...]]:
    """Return a vertex-edge horizon boundary on the radial N_0 line graph.

    Exact positive zeros are boundary vertices.  When no zero lies on the
    lattice, adjacent states with opposite residual signs define boundary
    edges.  Radius zero is never promoted to a horizon vertex here; it remains
    the separate center/denominator boundary.
    """
    _positive("mass_coefficient", mass_coefficient)
    _nonnegative("charge_square", charge_square)
    vertices = positive_horizon_states(mass_coefficient, charge_square)
    edges = tuple(
        (left, left + 1)
        for left in range(0, mass_coefficient + 1)
        if charged_residual(left, mass_coefficient, charge_square)
        * charged_residual(left + 1, mass_coefficient, charge_square)
        < 0
    )
    return {"vertices": vertices, "edges": edges}


def parity_square_floor(mass_coefficient: int, delta: int) -> int:
    """Largest u>=0 with u == a (mod 2) and u^2 <= Delta."""
    _nonnegative("mass_coefficient", mass_coefficient)
    _nonnegative("delta", delta)
    d = integer_nth_root(delta, 2)
    if (d - mass_coefficient) % 2 != 0:
        d -= 1
    if d < 0:
        raise AssertionError("parity-compatible square floor must be nonnegative")
    return d


def discriminant_horizon_cell(
    mass_coefficient: int, charge_square: int
) -> dict[str, int | bool]:
    """Return the parity-constrained square cell bracketing Delta.

    For a nonsquare nonnegative discriminant, the two symmetric states built
    from ``u`` lie just inside the sign-changing boundary, while the states
    built from ``u+2`` lie just outside.  For an exact square, the inner defect
    is zero and the symmetric states are exact integer horizons.
    """
    _nonnegative("mass_coefficient", mass_coefficient)
    _nonnegative("charge_square", charge_square)
    delta = charged_discriminant(mass_coefficient, charge_square)
    if delta < 0:
        raise ValueError("horizon cell requires nonnegative discriminant")
    u = parity_square_floor(mass_coefficient, delta)
    exact = u * u == delta
    inner_defect = (delta - u * u) // 4
    outer_defect = ((u + 2) * (u + 2) - delta) // 4
    inner_lower = (mass_coefficient - u) // 2
    inner_upper = (mass_coefficient + u) // 2
    outer_lower = (mass_coefficient - (u + 2)) // 2
    outer_upper = (mass_coefficient + (u + 2)) // 2
    return {
        "delta": delta,
        "u": u,
        "exact": exact,
        "inner_defect": inner_defect,
        "outer_defect": outer_defect,
        "inner_lower": inner_lower,
        "inner_upper": inner_upper,
        "outer_lower": outer_lower,
        "outer_upper": outer_upper,
    }


def charged_horizon_observation(
    precision: int, radius: int, mass_coefficient: int, charge_square: int
) -> int:
    """Return floor(lambda*|P(n)|/n^2) for positive radius."""
    _positive("precision", precision)
    _positive("radius", radius)
    residual = charged_residual(radius, mass_coefficient, charge_square)
    return precision * abs(residual) // (radius * radius)


def project_charged_observation(
    fine_value: int, coarse_precision: int, fine_precision: int
) -> int:
    """Project a divisible fine precision charged observation to a coarse one."""
    _nonnegative("fine_value", fine_value)
    _positive("coarse_precision", coarse_precision)
    _positive("fine_precision", fine_precision)
    if fine_precision % coarse_precision != 0:
        raise ValueError("coarse precision must divide fine precision")
    return fine_value // (fine_precision // coarse_precision)


def zero_persistence_limit(
    radius: int, mass_coefficient: int, charge_square: int
) -> int | None:
    """Largest precision for which a non-root state still observes as zero.

    ``None`` denotes an exact root, whose zero observation persists at every
    positive precision.
    """
    _positive("radius", radius)
    residual = charged_residual(radius, mass_coefficient, charge_square)
    if residual == 0:
        return None
    return (radius * radius - 1) // abs(residual)


def terminal_zero_precision(mass_coefficient: int) -> int:
    """A universal finite precision at which false positive zero states vanish.

    For a>=1 and b>=0, lambda=max(2,(2a-1)^2) guarantees that
    charged_horizon_observation(lambda,n,a,b)=0 iff P(n)=0 for every n>0.
    """
    _positive("mass_coefficient", mass_coefficient)
    return max(2, (2 * mass_coefficient - 1) ** 2)


def rescale_coefficients(
    scale: int, mass_coefficient: int, charge_square: int
) -> tuple[int, int]:
    """Uniform integer radial refinement: a -> s*a, b -> s^2*b."""
    _positive("scale", scale)
    _nonnegative("mass_coefficient", mass_coefficient)
    _nonnegative("charge_square", charge_square)
    return scale * mass_coefficient, scale * scale * charge_square
