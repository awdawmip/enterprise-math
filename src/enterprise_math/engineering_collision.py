"""E001 deterministic multi-resolution collision engine.

This engineering probe uses only finite integer state.  A body has an explicit
terminal integer position and radius.  Coarser precision levels observe aligned
integer cells of that finite state; no real-valued coordinate or hidden
infinite-precision remainder is introduced.

Collision uses the intrinsic Chebyshev/L-infinity metric on Z^2 because it gives
an exact axis-aligned square-body test with integer arithmetic.  At a coarse
cell size, the engine computes lower and upper bounds for every exact position
consistent with the observed cells.  A pair is certified COLLIDES or SEPARATE
only when every compatible terminal position has the same answer; otherwise the
pair refines to a smaller cell size.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

COLLIDES = "COLLIDES"
SEPARATE = "SEPARATE"
UNRESOLVED = "UNRESOLVED"
CollisionStatus = str
Pair = tuple[int, int]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


@dataclass(frozen=True, order=True)
class Body2D:
    """Finite terminal state for one axis-aligned square body on Z^2."""

    body_id: int
    x: int
    y: int
    radius: int = 0

    def __post_init__(self) -> None:
        _require_int("body_id", self.body_id)
        _require_int("x", self.x)
        _require_int("y", self.y)
        _require_int("radius", self.radius)
        if self.radius < 0:
            raise ValueError("radius must be non-negative")


@dataclass(frozen=True)
class ScaleCertificate:
    """Collision knowledge available from one finite cell observation."""

    cell_size: int
    status: CollisionStatus
    lower_distance: int
    upper_distance: int


@dataclass(frozen=True)
class CollisionDecision:
    """Adaptive collision result for one body pair."""

    pair: Pair
    collides: bool
    decided_cell_size: int
    observations: int
    trace: tuple[ScaleCertificate, ...]


@dataclass(frozen=True)
class CollisionEngineReport:
    """Deterministic E001 broad-phase plus adaptive narrow-phase result."""

    body_count: int
    possible_pairs: int
    candidate_pairs: int
    collision_pairs: tuple[Pair, ...]
    precision_observations: int
    terminal_checks: int
    decisions_by_cell_size: tuple[tuple[int, int], ...]


def validate_refinement_schedule(cell_sizes: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    """Validate an aligned coarse-to-fine integer refinement chain ending at 1."""
    schedule = tuple(cell_sizes)
    if not schedule:
        raise ValueError("at least one cell size is required")
    for cell_size in schedule:
        _require_int("cell_size", cell_size)
        if cell_size <= 0:
            raise ValueError("cell sizes must be positive")
    if schedule[-1] != 1:
        raise ValueError("the terminal cell size must be 1")
    for coarse, fine in zip(schedule, schedule[1:]):
        if fine >= coarse or coarse % fine != 0:
            raise ValueError("cell sizes must form a strict aligned divisibility refinement")
    return schedule


def _cell_interval(value: int, cell_size: int) -> tuple[int, int]:
    """Return the terminal-coordinate fiber of one aligned cell observation."""
    cell = value // cell_size
    lower = cell * cell_size
    return lower, lower + cell_size - 1


def _absolute_difference_bounds(
    left: tuple[int, int], right: tuple[int, int]
) -> tuple[int, int]:
    """Exact min/max |a-b| over two finite integer intervals."""
    left_lo, left_hi = left
    right_lo, right_hi = right
    if left_hi < right_lo:
        minimum = right_lo - left_hi
    elif right_hi < left_lo:
        minimum = left_lo - right_hi
    else:
        minimum = 0
    maximum = max(abs(left_lo - right_hi), abs(left_hi - right_lo))
    return minimum, maximum


def exact_collision(left: Body2D, right: Body2D) -> bool:
    """Exact terminal collision under integer Chebyshev distance."""
    threshold = left.radius + right.radius
    return max(abs(left.x - right.x), abs(left.y - right.y)) <= threshold


def collision_certificate_at_scale(
    left: Body2D, right: Body2D, cell_size: int
) -> ScaleCertificate:
    """Certify collision status from one finite cell-size observation.

    ``lower_distance`` and ``upper_distance`` are exact bounds on the terminal
    Chebyshev distance over every pair of terminal positions consistent with the
    two observed cells.  Therefore a returned COLLIDES/SEPARATE status is sound;
    UNRESOLVED means refinement is genuinely necessary for this observation.
    """
    _require_int("cell_size", cell_size)
    if cell_size <= 0:
        raise ValueError("cell_size must be positive")

    x_min, x_max = _absolute_difference_bounds(
        _cell_interval(left.x, cell_size), _cell_interval(right.x, cell_size)
    )
    y_min, y_max = _absolute_difference_bounds(
        _cell_interval(left.y, cell_size), _cell_interval(right.y, cell_size)
    )
    lower = max(x_min, y_min)
    upper = max(x_max, y_max)
    threshold = left.radius + right.radius

    if lower > threshold:
        status = SEPARATE
    elif upper <= threshold:
        status = COLLIDES
    else:
        status = UNRESOLVED
    return ScaleCertificate(cell_size, status, lower, upper)


def adaptive_collision(
    left: Body2D,
    right: Body2D,
    cell_sizes: tuple[int, ...] | list[int],
) -> CollisionDecision:
    """Refine only while the current finite observation cannot decide collision."""
    schedule = validate_refinement_schedule(cell_sizes)
    if left.body_id == right.body_id:
        raise ValueError("collision pair must contain two distinct body ids")
    pair = tuple(sorted((left.body_id, right.body_id)))
    trace: list[ScaleCertificate] = []
    for cell_size in schedule:
        certificate = collision_certificate_at_scale(left, right, cell_size)
        trace.append(certificate)
        if certificate.status != UNRESOLVED:
            return CollisionDecision(
                pair=pair,
                collides=certificate.status == COLLIDES,
                decided_cell_size=cell_size,
                observations=len(trace),
                trace=tuple(trace),
            )
    raise AssertionError("terminal cell size 1 failed to decide an exact integer collision")


def _body_bucket_range(body: Body2D, cell_size: int) -> tuple[range, range]:
    """Buckets intersecting the body's exact square extent."""
    x_min = (body.x - body.radius) // cell_size
    x_max = (body.x + body.radius) // cell_size
    y_min = (body.y - body.radius) // cell_size
    y_max = (body.y + body.radius) // cell_size
    return range(x_min, x_max + 1), range(y_min, y_max + 1)


def broad_phase_candidates(bodies: list[Body2D], cell_size: int) -> tuple[Pair, ...]:
    """Return a sound integer spatial-hash broad phase with no collision false negatives."""
    _require_int("cell_size", cell_size)
    if cell_size <= 0:
        raise ValueError("cell_size must be positive")
    ids = [body.body_id for body in bodies]
    if len(ids) != len(set(ids)):
        raise ValueError("body ids must be unique")

    buckets: dict[tuple[int, int], list[int]] = {}
    for body in sorted(bodies):
        x_range, y_range = _body_bucket_range(body, cell_size)
        for bucket_x in x_range:
            for bucket_y in y_range:
                buckets.setdefault((bucket_x, bucket_y), []).append(body.body_id)

    candidates: set[Pair] = set()
    for occupants in buckets.values():
        if len(occupants) < 2:
            continue
        for left_id, right_id in combinations(sorted(set(occupants)), 2):
            candidates.add((left_id, right_id))
    return tuple(sorted(candidates))


def run_collision_engine(
    bodies: list[Body2D],
    cell_sizes: tuple[int, ...] | list[int],
) -> CollisionEngineReport:
    """Run the E001 integer broad phase and adaptive multi-resolution narrow phase."""
    schedule = validate_refinement_schedule(cell_sizes)
    ids = [body.body_id for body in bodies]
    if len(ids) != len(set(ids)):
        raise ValueError("body ids must be unique")
    by_id = {body.body_id: body for body in bodies}
    candidates = broad_phase_candidates(bodies, schedule[0])

    collisions: list[Pair] = []
    observations = 0
    terminal_checks = 0
    decisions = {cell_size: 0 for cell_size in schedule}
    for left_id, right_id in candidates:
        decision = adaptive_collision(by_id[left_id], by_id[right_id], schedule)
        observations += decision.observations
        decisions[decision.decided_cell_size] += 1
        if decision.decided_cell_size == 1:
            terminal_checks += 1
        if decision.collides:
            collisions.append(decision.pair)

    count = len(bodies)
    return CollisionEngineReport(
        body_count=count,
        possible_pairs=count * (count - 1) // 2,
        candidate_pairs=len(candidates),
        collision_pairs=tuple(collisions),
        precision_observations=observations,
        terminal_checks=terminal_checks,
        decisions_by_cell_size=tuple((size, decisions[size]) for size in schedule),
    )


def exact_collision_pairs(bodies: list[Body2D]) -> tuple[Pair, ...]:
    """Brute-force terminal oracle used for E001 differential validation."""
    ids = [body.body_id for body in bodies]
    if len(ids) != len(set(ids)):
        raise ValueError("body ids must be unique")
    collisions: list[Pair] = []
    for left, right in combinations(sorted(bodies), 2):
        if exact_collision(left, right):
            collisions.append((left.body_id, right.body_id))
    return tuple(collisions)
