"""Exact arbitrary-support norm/absorption Pareto profile in block values.

For radius ``r``, let ``R_r`` be the compressed additive derivative-value set
reachable with fine L-infinity radius at most ``r``.  Define ``E(r)`` as the
minimum positive absorption redundancy on ``R_r``.  The sets ``R_r`` are nested,
so ``E(r)`` is nonincreasing once the first nondegenerate witness appears.

The complete witness Pareto frontier is exactly the strict-drop graph of this
profile between ``mu`` and ``nu``.  This turns the infinite fine witness lattice
into a finite integer step profile while preserving all rectangle queries in
(radius, absorption) cost space.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_block_floor_line import exact_absorption_floor_access
from .abc_block_mu import (
    compressed_additive_states_at_radius,
    exact_minimum_nondegenerate_witness_radius,
)
from .abc_block_value_lattice import block_value_absorption_floor
from .abc_support import abc_support_state, multiplicity_residual
from .abc_witness_absorption import certified_absorption_pareto_frontier


@dataclass(frozen=True)
class RadiusAbsorptionPoint:
    radius: int
    minimum_absorption: int


@dataclass(frozen=True)
class BlockParetoProfile:
    abc: tuple[int, int, int]
    mu: int
    nu: int
    eta_min: int
    profile: tuple[RadiusAbsorptionPoint, ...]
    frontier: tuple[tuple[int, int], ...]


def minimum_absorption_at_radius(a: int, b: int, c: int, radius: int) -> int | None:
    """Return minimum positive ``eta`` among additive states reachable by ``radius``."""
    abc_support_state(a, b, c)
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    residual = (
        multiplicity_residual(a)
        * multiplicity_residual(b)
        * multiplicity_residual(c)
    )
    best: int | None = None
    for u, v, _w in compressed_additive_states_at_radius(a, b, c, radius):
        wronskian = a * v - b * u
        if wronskian == 0:
            continue
        if abs(wronskian) % residual:
            raise AssertionError("compressed additive state violated residual divisibility")
        eta = abs(wronskian) // residual
        best = eta if best is None else min(best, eta)
    return best


def exact_block_pareto_profile(a: int, b: int, c: int) -> BlockParetoProfile:
    """Return the exact arbitrary-support Pareto frontier from compressed states."""
    mu_solution = exact_minimum_nondegenerate_witness_radius(a, b, c)
    floor_solution = exact_absorption_floor_access(a, b, c)
    mu = mu_solution.mu
    nu = floor_solution.nu
    eta_min = block_value_absorption_floor(a, b, c)
    if mu > nu:
        raise AssertionError("mu must not exceed floor-access radius nu")

    profile: list[RadiusAbsorptionPoint] = []
    frontier: list[tuple[int, int]] = []
    previous: int | None = None
    for radius in range(mu, nu + 1):
        eta = minimum_absorption_at_radius(a, b, c, radius)
        if eta is None:
            raise AssertionError("profile lost nondegenerate state after mu")
        if previous is not None and eta > previous:
            raise AssertionError("minimum absorption must be nonincreasing with radius")
        profile.append(RadiusAbsorptionPoint(radius=radius, minimum_absorption=eta))
        if previous is None or eta < previous:
            frontier.append((radius, eta))
        previous = eta

    if not profile or profile[-1].minimum_absorption != eta_min:
        raise AssertionError("profile failed to attain exact absorption floor at nu")
    if not frontier or frontier[-1] != (nu, eta_min):
        if frontier[-1][1] != eta_min:
            raise AssertionError("Pareto frontier failed absorption-floor endpoint")
        # If eta_min was reached before nu, then nu was not the first floor-access
        # radius.  The floor solver definition forbids this.
        raise AssertionError("nu must be the first radius attaining eta_min")

    return BlockParetoProfile(
        abc=(a, b, c),
        mu=mu,
        nu=nu,
        eta_min=eta_min,
        profile=tuple(profile),
        frontier=tuple(frontier),
    )


def frontier_cardinality_bound_holds(a: int, b: int, c: int) -> bool:
    """Check the finite bound from radius span and integer absorption drops."""
    data = exact_block_pareto_profile(a, b, c)
    first_eta = data.frontier[0][1]
    bound = min(
        data.nu - data.mu + 1,
        first_eta - data.eta_min + 1,
    )
    if len(data.frontier) > bound:
        raise AssertionError("Pareto strict-drop frontier exceeded finite bound")
    return True


def compressed_and_fine_frontiers_agree_on_reference_examples() -> bool:
    """Compare the arbitrary-support compressed frontier with the prior fine oracle."""
    examples = (
        ((2, 3, 5), 3),
        ((2, 7, 9), 6),
        ((5, 7, 12), 3),
        ((5, 27, 32), 4),
    )
    for triple, max_bound in examples:
        compressed = exact_block_pareto_profile(*triple).frontier
        fine = certified_absorption_pareto_frontier(*triple, max_bound=max_bound)
        if compressed != fine:
            raise AssertionError(
                f"compressed/fine Pareto mismatch for {triple}: {compressed} != {fine}"
            )
    return True
