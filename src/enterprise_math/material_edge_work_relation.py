"""Finite endpoint-work relation for an energy-consistent material step.

The causal current-force world is deterministic but can violate the static
passivity of a material table because loading and returning sample different
endpoint forces.  This module studies the complementary finite policy: choose an
endpoint only when the exact branch chord work between the two represented
material states is compatible with midpoint momentum/position kinematics.

Normalize one comparison layer to unit mass and one unit time count, and let the
material deformation coordinate itself be the position coordinate for this local
constitutive step.  For a loading candidate ``i<j`` put

    dx = x_j-x_i > 0,
    p_1 = 2*dx-p_0.

The midpoint displacement equation is then exactly

    2*dx = p_0+p_1.

Let ``W2_L(i,j)`` be the doubled static loading chord work.  Energy consistency
requires

    p_0^2-p_1^2 = W2_L(i,j).

Equivalently the resisting impulse/edge-force count is

    p_0-p_1 = W2_L(i,j)/(2*dx).

For a returning candidate ``j<i`` use an outward-oriented momentum and
``dx=x_i-x_j``.  The material releases work, so

    p_1^2-p_0^2 = W2_R(j,i).

Every returned candidate therefore preserves the declared static branch work
exactly; no hidden intermediate saved state is inserted.  The price is that the
endpoint law is a finite relation: for a fixed start/momentum there may be zero,
one, or (for sufficiently nonmonotone tables) multiple represented endpoints.

Branch-memory boundary
----------------------
A loading energy candidate with ``p_1<0`` has already reversed momentum before
the saved tick ends.  For an elastic single-branch law, endpoint work may still
be meaningful.  For a genuine loading/returning material, however, that candidate
requires an unrepresented within-tick turning event followed by a returning
segment.  It is therefore marked ``requires_within_tick_branch_switch`` and is
not branch-consistent unless a separate within-tick turning policy is explicitly
declared.  ``p_1=0`` is an exact turn at the saved endpoint and is branch-
consistent.

For a nondecreasing loading force, doubled work increments are nondecreasing.
Since the required kinetic-loss curve ``4*dx*(p_0-dx)`` has strictly decreasing
secant slopes from the origin, there can be at most one positive loading endpoint.
Thus a hardening branch restores uniqueness *if* an exact endpoint exists, but
existence remains an arithmetic/precision question.

Discrete-gradient/energy-preserving endpoint forces are established numerical
analysis.  E001 uses this relation as an integer comparator and as evidence that
passivity preservation can naturally turn deterministic response into a finite
compatibility relation.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .material_force_work import FiniteForceLaw
from .material_hysteresis import LOADING, RETURNING

NO_ENDPOINT = "NO_ENDPOINT"
UNIQUE_ENDPOINT = "UNIQUE_ENDPOINT"
MULTIPLE_ENDPOINTS = "MULTIPLE_ENDPOINTS"


def _nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def branch_chord_work_between_depths_numerator2(
    law: FiniteForceLaw,
    lower_depth: int,
    upper_depth: int,
    branch: str,
) -> int:
    """Exact doubled branch work over represented material cells."""
    for name, value in (("lower_depth", lower_depth), ("upper_depth", upper_depth)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if not 0 <= lower_depth < upper_depth < len(law.profile.loading):
        raise ValueError("require 0 <= lower_depth < upper_depth inside the force law")
    if branch == LOADING:
        samples = law.profile.loading
    elif branch == RETURNING:
        samples = law.profile.returning
    else:
        raise ValueError("branch must be LOADING or RETURNING")
    grid = law.deformation_counts
    return sum(
        (samples[k - 1] + samples[k]) * (grid[k] - grid[k - 1])
        for k in range(lower_depth + 1, upper_depth + 1)
    )


@dataclass(frozen=True, order=True)
class MaterialEdgeWorkCandidate:
    start_depth: int
    end_depth: int
    branch: str
    deformation_displacement: int
    oriented_momentum_before: int
    oriented_momentum_after: int
    branch_work_numerator2: int
    kinetic_square_change: int
    edge_impulse_numerator: int
    edge_impulse_denominator: int
    edge_impulse_is_integer: bool

    @property
    def requires_within_tick_branch_switch(self) -> bool:
        return self.branch == LOADING and self.oriented_momentum_after < 0

    @property
    def branch_consistent(self) -> bool:
        return not self.requires_within_tick_branch_switch


def _reduced_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    common = gcd(abs(numerator), denominator)
    return numerator // common, denominator // common


def loading_edge_work_candidates(
    law: FiniteForceLaw,
    start_depth: int,
    inward_momentum: int,
) -> tuple[MaterialEdgeWorkCandidate, ...]:
    """Enumerate all represented deeper endpoints satisfying exact work + midpoint laws."""
    _nonnegative("start_depth", start_depth)
    _nonnegative("inward_momentum", inward_momentum)
    if start_depth >= len(law.profile.loading):
        raise ValueError("start_depth lies outside force law")
    grid = law.deformation_counts
    candidates: list[MaterialEdgeWorkCandidate] = []
    for end_depth in range(start_depth + 1, len(law.profile.loading)):
        dx = grid[end_depth] - grid[start_depth]
        after = 2 * dx - inward_momentum
        work2 = branch_chord_work_between_depths_numerator2(
            law, start_depth, end_depth, LOADING
        )
        kinetic_loss = inward_momentum * inward_momentum - after * after
        if kinetic_loss != work2:
            continue
        impulse = inward_momentum - after
        num, den = _reduced_fraction(work2, 2 * dx)
        if impulse * den != num:
            raise AssertionError("loading edge impulse disagrees with work/displacement quotient")
        candidates.append(
            MaterialEdgeWorkCandidate(
                start_depth=start_depth,
                end_depth=end_depth,
                branch=LOADING,
                deformation_displacement=dx,
                oriented_momentum_before=inward_momentum,
                oriented_momentum_after=after,
                branch_work_numerator2=work2,
                kinetic_square_change=-work2,
                edge_impulse_numerator=num,
                edge_impulse_denominator=den,
                edge_impulse_is_integer=den == 1,
            )
        )
    return tuple(candidates)


def returning_edge_work_candidates(
    law: FiniteForceLaw,
    start_depth: int,
    outward_momentum: int,
) -> tuple[MaterialEdgeWorkCandidate, ...]:
    """Enumerate all represented shallower endpoints satisfying exact released work."""
    _nonnegative("start_depth", start_depth)
    _nonnegative("outward_momentum", outward_momentum)
    if start_depth >= len(law.profile.returning):
        raise ValueError("start_depth lies outside force law")
    grid = law.deformation_counts
    candidates: list[MaterialEdgeWorkCandidate] = []
    for end_depth in range(start_depth - 1, -1, -1):
        dx = grid[start_depth] - grid[end_depth]
        after = 2 * dx - outward_momentum
        work2 = branch_chord_work_between_depths_numerator2(
            law, end_depth, start_depth, RETURNING
        )
        kinetic_gain = after * after - outward_momentum * outward_momentum
        if kinetic_gain != work2:
            continue
        impulse = after - outward_momentum
        num, den = _reduced_fraction(work2, 2 * dx)
        if impulse * den != num:
            raise AssertionError("returning edge impulse disagrees with work/displacement quotient")
        candidates.append(
            MaterialEdgeWorkCandidate(
                start_depth=start_depth,
                end_depth=end_depth,
                branch=RETURNING,
                deformation_displacement=dx,
                oriented_momentum_before=outward_momentum,
                oriented_momentum_after=after,
                branch_work_numerator2=work2,
                kinetic_square_change=work2,
                edge_impulse_numerator=num,
                edge_impulse_denominator=den,
                edge_impulse_is_integer=den == 1,
            )
        )
    return tuple(candidates)


@dataclass(frozen=True)
class MaterialEdgeWorkRelationReport:
    branch: str
    start_depth: int
    oriented_momentum_before: int
    candidates: tuple[MaterialEdgeWorkCandidate, ...]
    relation_status: str

    @property
    def branch_consistent_candidates(self) -> tuple[MaterialEdgeWorkCandidate, ...]:
        return tuple(candidate for candidate in self.candidates if candidate.branch_consistent)

    @property
    def branch_consistent_relation_status(self) -> str:
        count = len(self.branch_consistent_candidates)
        return NO_ENDPOINT if count == 0 else UNIQUE_ENDPOINT if count == 1 else MULTIPLE_ENDPOINTS


def material_edge_work_relation_report(
    law: FiniteForceLaw,
    start_depth: int,
    oriented_momentum_before: int,
    branch: str,
) -> MaterialEdgeWorkRelationReport:
    if branch == LOADING:
        candidates = loading_edge_work_candidates(
            law, start_depth, oriented_momentum_before
        )
    elif branch == RETURNING:
        candidates = returning_edge_work_candidates(
            law, start_depth, oriented_momentum_before
        )
    else:
        raise ValueError("branch must be LOADING or RETURNING")
    status = (
        NO_ENDPOINT
        if not candidates
        else UNIQUE_ENDPOINT
        if len(candidates) == 1
        else MULTIPLE_ENDPOINTS
    )
    return MaterialEdgeWorkRelationReport(
        branch=branch,
        start_depth=start_depth,
        oriented_momentum_before=oriented_momentum_before,
        candidates=candidates,
        relation_status=status,
    )


def loading_force_is_nondecreasing(law: FiniteForceLaw) -> bool:
    return all(
        left <= right
        for left, right in zip(law.profile.loading, law.profile.loading[1:])
    )


def verify_hardening_loading_endpoint_uniqueness(
    law: FiniteForceLaw,
    start_depth: int,
    inward_momentum: int,
) -> bool:
    """Executable specialization of the at-most-one endpoint theorem."""
    if not loading_force_is_nondecreasing(law):
        raise ValueError("loading force must be nondecreasing")
    candidates = loading_edge_work_candidates(law, start_depth, inward_momentum)
    return len(candidates) <= 1
