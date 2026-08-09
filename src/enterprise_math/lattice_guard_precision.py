"""Lattice guard precision for P024.

This module extends the one-dimensional P024 action-language precision theorem to
integer lattice states observed by a *full vector* of integer affine threshold
guards.  It deliberately does not handle arbitrary aggregate observables; those
belong to the generic P023 future-equivalence layer until a sharper arithmetic
specialization is proved.

For a guard ``row . x >= threshold`` the row is normalized by the gcd of its
integer coefficients.  A future translation word shifts only the scalar guard
score.  The coarsest finite-horizon state for the full guard vector is therefore
the vector of ranks induced by the actually reachable pulled-back guard cuts.

The ambient dimension is not the relevant dimension: all visible information
factors through the integer score map defined by the primitive guard rows.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from math import gcd
from typing import Iterable, Sequence


Vector = tuple[int, ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _vector(values: Sequence[int] | Iterable[int], *, name: str) -> Vector:
    result = tuple(values)
    if not result:
        raise ValueError(f"{name} must be nonempty")
    for value in result:
        _require_int(name, value)
    return result


def _same_dimension(vectors: Sequence[Vector]) -> int:
    if not vectors:
        raise ValueError("at least one vector is required")
    dimension = len(vectors[0])
    if any(len(vector) != dimension for vector in vectors):
        raise ValueError("all vectors must have the same dimension")
    return dimension


def dot(left: Sequence[int], right: Sequence[int]) -> int:
    a = _vector(left, name="left")
    b = _vector(right, name="right")
    if len(a) != len(b):
        raise ValueError("dot-product vectors must have the same dimension")
    return sum(x * y for x, y in zip(a, b, strict=True))


def ceil_div(numerator: int, denominator: int) -> int:
    _require_int("numerator", numerator)
    _require_int("denominator", denominator)
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    return -((-numerator) // denominator)


def coefficient_gcd(row: Sequence[int]) -> int:
    vector = _vector(row, name="row")
    common = 0
    for value in vector:
        common = gcd(common, abs(value))
    return common


@dataclass(frozen=True)
class IntegerGuard:
    """One integer affine threshold predicate ``row . x >= threshold``."""

    row: Vector
    threshold: int

    def __post_init__(self) -> None:
        _vector(self.row, name="row")
        _require_int("threshold", self.threshold)

    @property
    def coefficient_gcd(self) -> int:
        return coefficient_gcd(self.row)

    @property
    def is_constant(self) -> bool:
        return self.coefficient_gcd == 0

    @property
    def primitive_row(self) -> Vector:
        common = self.coefficient_gcd
        if common == 0:
            return self.row
        return tuple(value // common for value in self.row)

    @property
    def primitive_threshold(self) -> int:
        """Exact threshold on the primitive integer score coordinate."""
        common = self.coefficient_gcd
        if common == 0:
            return int(0 >= self.threshold)
        return ceil_div(self.threshold, common)

    def evaluate(self, point: Sequence[int]) -> bool:
        vector = _vector(point, name="point")
        if len(vector) != len(self.row):
            raise ValueError("point and guard dimensions differ")
        return dot(self.row, vector) >= self.threshold

    def primitive_score(self, point: Sequence[int]) -> int:
        vector = _vector(point, name="point")
        if len(vector) != len(self.row):
            raise ValueError("point and guard dimensions differ")
        if self.is_constant:
            return 0
        return dot(self.primitive_row, vector)


def _normalize_guards(guards: Iterable[IntegerGuard]) -> tuple[IntegerGuard, ...]:
    values = tuple(guards)
    if not values:
        raise ValueError("at least one guard is required")
    dimension = len(values[0].row)
    if any(len(guard.row) != dimension for guard in values):
        raise ValueError("all guards must have the same state dimension")
    return values


def _normalize_actions(actions: Iterable[Sequence[int]], dimension: int) -> tuple[Vector, ...]:
    values = tuple(_vector(action, name="action") for action in actions)
    if not values:
        raise ValueError("at least one action is required")
    if any(len(action) != dimension for action in values):
        raise ValueError("action dimension differs from state dimension")
    return values


def reachable_translation_sums(
    actions: Iterable[Sequence[int]],
    horizon: int,
) -> tuple[Vector, ...]:
    """All cumulative translation vectors reachable by words of length <= horizon."""
    _require_int("horizon", horizon)
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    raw = tuple(_vector(action, name="action") for action in actions)
    dimension = _same_dimension(raw)
    zero = (0,) * dimension
    frontier = {zero}
    reached = {zero}
    for _ in range(horizon):
        next_frontier: set[Vector] = set()
        for state in frontier:
            for action in raw:
                nxt = tuple(x + a for x, a in zip(state, action, strict=True))
                next_frontier.add(nxt)
        frontier = next_frontier
        reached.update(frontier)
    return tuple(sorted(reached))


def translated_point(point: Sequence[int], increment: Sequence[int]) -> Vector:
    x = _vector(point, name="point")
    a = _vector(increment, name="increment")
    if len(x) != len(a):
        raise ValueError("point and increment dimensions differ")
    return tuple(u + v for u, v in zip(x, a, strict=True))


def direct_future_guard_signature(
    point: Sequence[int],
    guards: Iterable[IntegerGuard],
    actions: Iterable[Sequence[int]],
    horizon: int,
) -> tuple[tuple[bool, ...], ...]:
    """Direct full-guard future signature over all reachable translations."""
    guard_values = _normalize_guards(guards)
    x = _vector(point, name="point")
    if len(x) != len(guard_values[0].row):
        raise ValueError("point and guard dimensions differ")
    action_values = _normalize_actions(actions, len(x))
    sums = reachable_translation_sums(action_values, horizon)
    return tuple(
        tuple(guard.evaluate(translated_point(x, increment)) for guard in guard_values)
        for increment in sums
    )


def projected_action_shifts(
    guard: IntegerGuard,
    translation_sums: Iterable[Sequence[int]],
) -> tuple[int, ...]:
    """Distinct future shifts in the guard's primitive scalar score."""
    if guard.is_constant:
        return (0,)
    shifts = set()
    for increment in translation_sums:
        vector = _vector(increment, name="translation")
        if len(vector) != len(guard.row):
            raise ValueError("translation and guard dimensions differ")
        shifts.add(dot(guard.primitive_row, vector))
    return tuple(sorted(shifts))


def pulled_guard_cuts(
    guard: IntegerGuard,
    translation_sums: Iterable[Sequence[int]],
) -> tuple[int, ...]:
    """Reachable present-time cut coordinates for one primitive guard score."""
    if guard.is_constant:
        return ()
    threshold = guard.primitive_threshold
    shifts = projected_action_shifts(guard, translation_sums)
    return tuple(sorted({threshold - shift for shift in shifts}))


def scalar_cut_rank(score: int, cuts: Iterable[int]) -> int:
    _require_int("score", score)
    values = tuple(sorted(set(cuts)))
    for cut in values:
        _require_int("cut", cut)
    return sum(cut <= score for cut in values)


def guard_rank_signature_from_sums(
    point: Sequence[int],
    guards: Iterable[IntegerGuard],
    translation_sums: Iterable[Sequence[int]],
) -> tuple[int, ...]:
    """Coarsest full-guard rank vector for a supplied reachable-sum set."""
    guard_values = _normalize_guards(guards)
    x = _vector(point, name="point")
    if len(x) != len(guard_values[0].row):
        raise ValueError("point and guard dimensions differ")
    sums = tuple(_vector(value, name="translation") for value in translation_sums)
    if not sums:
        raise ValueError("translation sum set must be nonempty")
    if any(len(value) != len(x) for value in sums):
        raise ValueError("translation and state dimensions differ")

    result = []
    for guard in guard_values:
        if guard.is_constant:
            result.append(0)
            continue
        score = guard.primitive_score(x)
        result.append(scalar_cut_rank(score, pulled_guard_cuts(guard, sums)))
    return tuple(result)


def guard_rank_signature(
    point: Sequence[int],
    guards: Iterable[IntegerGuard],
    actions: Iterable[Sequence[int]],
    horizon: int,
) -> tuple[int, ...]:
    guard_values = _normalize_guards(guards)
    action_values = _normalize_actions(actions, len(guard_values[0].row))
    sums = reachable_translation_sums(action_values, horizon)
    return guard_rank_signature_from_sums(point, guard_values, sums)


def primitive_score_vector(
    point: Sequence[int],
    guards: Iterable[IntegerGuard],
) -> tuple[int, ...]:
    """Image of one state in the primitive guard-score lattice."""
    guard_values = _normalize_guards(guards)
    x = _vector(point, name="point")
    if len(x) != len(guard_values[0].row):
        raise ValueError("point and guard dimensions differ")
    return tuple(guard.primitive_score(x) for guard in guard_values)


def rank_box_sizes(
    guards: Iterable[IntegerGuard],
    actions: Iterable[Sequence[int]],
    horizon: int,
) -> tuple[int, ...]:
    """Per-guard rank counts before score-lattice feasibility is imposed."""
    guard_values = _normalize_guards(guards)
    action_values = _normalize_actions(actions, len(guard_values[0].row))
    sums = reachable_translation_sums(action_values, horizon)
    return tuple(1 if guard.is_constant else len(pulled_guard_cuts(guard, sums)) + 1 for guard in guard_values)


def projected_action_generators(
    guard: IntegerGuard,
    actions: Iterable[Sequence[int]],
) -> tuple[int, ...]:
    """Generator increments in one primitive guard-score direction."""
    action_values = _normalize_actions(actions, len(guard.row))
    if guard.is_constant:
        return tuple(0 for _ in action_values)
    return tuple(dot(guard.primitive_row, action) for action in action_values)


@dataclass(frozen=True)
class ProjectedActionType:
    kind: str
    grain: int
    generators: tuple[int, ...]


def classify_projected_action_monoid(
    guard: IntegerGuard,
    actions: Iterable[Sequence[int]],
) -> ProjectedActionType:
    """Classify the one-dimensional action monoid seen by one guard.

    ``two_sided_group`` uses the P024 one-dimensional result: a finite integer
    generator family containing both signs generates its full gcd subgroup as a
    nonnegative-word monoid.  Same-sign families remain one-sided semigroups.
    """
    generators = projected_action_generators(guard, actions)
    nonzero = tuple(value for value in generators if value)
    if not nonzero:
        return ProjectedActionType("invariant", 0, generators)
    grain = 0
    for value in nonzero:
        grain = gcd(grain, abs(value))
    has_positive = any(value > 0 for value in nonzero)
    has_negative = any(value < 0 for value in nonzero)
    if has_positive and has_negative:
        kind = "two_sided_group"
    elif has_positive:
        kind = "positive_semigroup"
    else:
        kind = "negative_semigroup"
    return ProjectedActionType(kind, grain, generators)


def positive_zero_relation_inverse_words(
    actions: Iterable[Sequence[int]],
    coefficients: Sequence[int],
) -> tuple[tuple[int, ...], ...]:
    """Construct nonnegative words for every generator inverse from a positive zero relation.

    If ``lambda_i > 0`` and ``sum lambda_i a_i = 0``, then

    ``-a_i = (lambda_i-1) a_i + sum_(j!=i) lambda_j a_j``.

    Returning these coefficient vectors is an explicit certificate that the
    action monoid already equals the group generated by the actions.
    """
    action_values = tuple(_vector(action, name="action") for action in actions)
    dimension = _same_dimension(action_values)
    lambdas = tuple(coefficients)
    if len(lambdas) != len(action_values):
        raise ValueError("one positive coefficient is required per action")
    for coefficient in lambdas:
        _require_int("coefficient", coefficient)
        if coefficient <= 0:
            raise ValueError("zero-relation coefficients must be strictly positive")

    total = [0] * dimension
    for coefficient, action in zip(lambdas, action_values, strict=True):
        for index, value in enumerate(action):
            total[index] += coefficient * value
    if any(total):
        raise ValueError("coefficients do not form a zero relation")

    inverse_words = []
    for index in range(len(action_values)):
        word = list(lambdas)
        word[index] -= 1
        inverse_words.append(tuple(word))
    return tuple(inverse_words)


def nonnegative_2d_semigroup_contains(
    target: Sequence[int],
    generators: Iterable[Sequence[int]],
) -> bool:
    """Exact finite membership test for a semigroup generated in ``N^2``.

    This helper is intentionally narrow and audit-oriented.  Nonnegative
    generators cannot leave and later re-enter the target rectangle, so breadth-
    first search inside ``[0,target_0] x [0,target_1]`` is exact.
    """
    point = _vector(target, name="target")
    if len(point) != 2:
        raise ValueError("target must be two-dimensional")
    if any(value < 0 for value in point):
        return False
    gens = tuple(_vector(generator, name="generator") for generator in generators)
    if not gens:
        raise ValueError("at least one generator is required")
    if any(len(generator) != 2 for generator in gens):
        raise ValueError("generators must be two-dimensional")
    if any(value < 0 for generator in gens for value in generator):
        raise ValueError("this exact helper requires nonnegative generators")
    if any(generator == (0, 0) for generator in gens):
        raise ValueError("zero generators are excluded from this audit helper")

    origin = (0, 0)
    queue = deque([origin])
    reached = {origin}
    while queue:
        current = queue.popleft()
        if current == point:
            return True
        for generator in gens:
            nxt = (current[0] + generator[0], current[1] + generator[1])
            if nxt[0] > point[0] or nxt[1] > point[1]:
                continue
            if nxt not in reached:
                reached.add(nxt)
                queue.append(nxt)
    return False
