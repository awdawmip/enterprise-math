"""Exact finite idempotent path-closure and Bellman helpers.

Production surface for Enterprise Toolbox family T12.

Supported semantics are deliberately bounded and explicit:

* min-plus or max-plus matrices with integer edge weights and ``None`` for
  unreachable transitions;
* all-path closure only after an exact improving-cycle check;
* finite idempotent semirings supplied as explicit finite carriers/operations;
* residual and Bellman fixed-point computation only when the finite order data
  required by the theorem exists.

The module never infers weights from incidence, path count, addresses, or
implementation priority. Residuation/Galois adjunction by itself remains owned
by the pre-existing P008 order-adjoint machinery.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Any, Callable, Iterable, Literal, Sequence, TypeAlias

PathKind: TypeAlias = Literal["min", "max"]
Weight: TypeAlias = int | None
Matrix: TypeAlias = tuple[tuple[Weight, ...], ...]


class IdempotentClosureError(ValueError):
    """Base class for typed T12 input or obstruction errors."""


class ImprovingCycleError(IdempotentClosureError):
    """A finite all-path optimum is obstructed by an improving cycle."""

    def __init__(self, *, kind: PathKind, cycle: tuple[int, ...], weight: int):
        self.kind = kind
        self.cycle = cycle
        self.weight = weight
        direction = "negative" if kind == "min" else "positive"
        super().__init__(
            f"{direction} improving cycle for {kind}-plus closure: "
            f"cycle={cycle}, weight={weight}"
        )


class ResidualDoesNotExist(IdempotentClosureError):
    """The requested greatest residual element does not exist."""


class SemiringLawError(IdempotentClosureError):
    """A declared finite semiring fails a required exact law."""


def _validate_kind(kind: str) -> PathKind:
    if kind not in {"min", "max"}:
        raise ValueError("kind must be 'min' or 'max'")
    return kind  # type: ignore[return-value]


def _validate_weight(value: Weight) -> None:
    if value is not None and (
        isinstance(value, bool) or not isinstance(value, int)
    ):
        raise TypeError("weights must be integers or None (unreachable)")


def validate_weight_matrix(
    matrix: Sequence[Sequence[Weight]], *, square: bool = False
) -> Matrix:
    """Return an immutable validated integer/unreachable matrix."""

    rows = tuple(tuple(row) for row in matrix)
    if not rows:
        raise ValueError("matrix must contain at least one row")
    width = len(rows[0])
    if width == 0:
        raise ValueError("matrix must contain at least one column")
    if any(len(row) != width for row in rows):
        raise ValueError("matrix rows must have equal length")
    if square and len(rows) != width:
        raise ValueError("matrix must be square")
    for row in rows:
        for value in row:
            _validate_weight(value)
    return rows


def identity_matrix(size: int) -> Matrix:
    """Return the min/max-plus multiplicative identity matrix."""

    if isinstance(size, bool) or not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer")
    return tuple(
        tuple(0 if i == j else None for j in range(size))
        for i in range(size)
    )


def envelope(left: Weight, right: Weight, kind: PathKind) -> Weight:
    """Idempotent addition: min or max, preserving unreachable values."""

    _validate_kind(kind)
    _validate_weight(left)
    _validate_weight(right)
    if left is None:
        return right
    if right is None:
        return left
    return min(left, right) if kind == "min" else max(left, right)


def extend(left: Weight, right: Weight) -> Weight:
    """Path extension: ordinary integer addition with unreachable absorption."""

    _validate_weight(left)
    _validate_weight(right)
    if left is None or right is None:
        return None
    return left + right


def matrix_envelope(
    left: Sequence[Sequence[Weight]],
    right: Sequence[Sequence[Weight]],
    kind: PathKind,
) -> Matrix:
    """Entrywise idempotent envelope of equally shaped matrices."""

    a = validate_weight_matrix(left)
    b = validate_weight_matrix(right)
    if (len(a), len(a[0])) != (len(b), len(b[0])):
        raise ValueError("matrix shapes must agree")
    return tuple(
        tuple(envelope(a[i][j], b[i][j], kind) for j in range(len(a[0])))
        for i in range(len(a))
    )


def matrix_multiply(
    left: Sequence[Sequence[Weight]],
    right: Sequence[Sequence[Weight]],
    kind: PathKind,
) -> Matrix:
    """Min-plus or max-plus matrix multiplication."""

    kind = _validate_kind(kind)
    a = validate_weight_matrix(left)
    b = validate_weight_matrix(right)
    if len(a[0]) != len(b):
        raise ValueError("inner matrix dimensions must agree")
    out: list[list[Weight]] = [
        [None for _ in range(len(b[0]))] for _ in range(len(a))
    ]
    for i in range(len(a)):
        for j in range(len(b[0])):
            value: Weight = None
            for k in range(len(b)):
                value = envelope(value, extend(a[i][k], b[k][j]), kind)
            out[i][j] = value
    return tuple(tuple(row) for row in out)


def matrix_power(
    matrix: Sequence[Sequence[Weight]], exponent: int, kind: PathKind
) -> Matrix:
    """Return the fixed-length path envelope ``A**exponent``."""

    a = validate_weight_matrix(matrix, square=True)
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("exponent must be a non-negative integer")
    result = identity_matrix(len(a))
    base = a
    power = exponent
    while power:
        if power & 1:
            result = matrix_multiply(result, base, kind)
        base = matrix_multiply(base, base, kind)
        power >>= 1
    return result


def path_value(
    matrix: Sequence[Sequence[Weight]], path: Sequence[int]
) -> Weight:
    """Return the exact value of one declared directed path."""

    a = validate_weight_matrix(matrix, square=True)
    vertices = tuple(path)
    if not vertices:
        raise ValueError("path must contain at least one vertex")
    if any(
        isinstance(vertex, bool)
        or not isinstance(vertex, int)
        or not 0 <= vertex < len(a)
        for vertex in vertices
    ):
        raise ValueError("path contains an invalid vertex")
    total: Weight = 0
    for source, target in zip(vertices, vertices[1:]):
        total = extend(total, a[source][target])
        if total is None:
            return None
    return total


def find_improving_cycle(
    matrix: Sequence[Sequence[Weight]], kind: PathKind
) -> tuple[tuple[int, ...], int] | None:
    """Return a simple improving cycle and its exact total weight, if any."""

    a = validate_weight_matrix(matrix, square=True)
    kind = _validate_kind(kind)
    improves = (lambda weight: weight < 0) if kind == "min" else (
        lambda weight: weight > 0
    )
    size = len(a)

    def walk(
        start: int, current: int, path: tuple[int, ...], total: int
    ) -> tuple[tuple[int, ...], int] | None:
        for nxt, weight in enumerate(a[current]):
            if weight is None:
                continue
            if nxt == start:
                cycle_weight = total + weight
                if improves(cycle_weight):
                    return path + (start,), cycle_weight
            elif nxt not in path and len(path) < size:
                found = walk(start, nxt, path + (nxt,), total + weight)
                if found is not None:
                    return found
        return None

    for start in range(size):
        found = walk(start, start, (start,), 0)
        if found is not None:
            return found
    return None


def _strictly_better(
    candidate: Weight, current: Weight, kind: PathKind
) -> bool:
    if candidate is None:
        return False
    if current is None:
        return True
    return candidate < current if kind == "min" else candidate > current


@dataclass(frozen=True)
class PathClosureResult:
    """Exact finite all-pairs closure and deterministic witness routing."""

    kind: PathKind
    closure: Matrix
    next_hop: tuple[tuple[int | None, ...], ...]

    def witness_path(self, source: int, target: int) -> tuple[int, ...] | None:
        """Reconstruct one optimal simple-path representative."""

        size = len(self.closure)
        if not 0 <= source < size or not 0 <= target < size:
            raise ValueError("source/target outside closure matrix")
        if self.closure[source][target] is None:
            return None
        if source == target:
            return (source,)
        current = source
        path = [source]
        seen = {source}
        while current != target:
            nxt = self.next_hop[current][target]
            if nxt is None:
                raise AssertionError("reachable closure entry lacks next hop")
            current = nxt
            path.append(current)
            if current != target and current in seen:
                raise AssertionError("witness routing contains a cycle")
            seen.add(current)
            if len(path) > size + 1:
                raise AssertionError("witness path exceeded simple-path bound")
        return tuple(path)


def finite_kleene_closure(
    matrix: Sequence[Sequence[Weight]], kind: PathKind
) -> PathClosureResult:
    """Compute the exact all-walk envelope when no improving cycle exists."""

    a = validate_weight_matrix(matrix, square=True)
    kind = _validate_kind(kind)
    obstruction = find_improving_cycle(a, kind)
    if obstruction is not None:
        cycle, weight = obstruction
        raise ImprovingCycleError(kind=kind, cycle=cycle, weight=weight)

    size = len(a)
    dist = [list(row) for row in matrix_envelope(identity_matrix(size), a, kind)]
    next_hop: list[list[int | None]] = [
        [None for _ in range(size)] for _ in range(size)
    ]
    for i in range(size):
        next_hop[i][i] = i
        for j in range(size):
            if i != j and a[i][j] is not None:
                next_hop[i][j] = j

    for middle in range(size):
        for source in range(size):
            if dist[source][middle] is None:
                continue
            for target in range(size):
                if dist[middle][target] is None:
                    continue
                candidate = extend(dist[source][middle], dist[middle][target])
                if _strictly_better(candidate, dist[source][target], kind):
                    dist[source][target] = candidate
                    next_hop[source][target] = next_hop[source][middle]

    return PathClosureResult(
        kind=kind,
        closure=tuple(tuple(row) for row in dist),
        next_hop=tuple(tuple(row) for row in next_hop),
    )


@dataclass(frozen=True)
class FiniteIdempotentSemiring:
    """Caller-declared finite idempotent semiring and its natural order."""

    elements: tuple[Any, ...]
    zero: Any
    one: Any
    top: Any
    add: Callable[[Any, Any], Any]
    mul: Callable[[Any, Any], Any]

    def leq(self, left: Any, right: Any) -> bool:
        return self.add(left, right) == right

    def meet(self, values: Iterable[Any]) -> Any:
        vals = tuple(values)
        lower_bounds = [
            candidate
            for candidate in self.elements
            if all(self.leq(candidate, value) for value in vals)
        ]
        greatest = [
            candidate
            for candidate in lower_bounds
            if all(self.leq(other, candidate) for other in lower_bounds)
        ]
        if len(greatest) != 1:
            raise ResidualDoesNotExist(
                "finite meet does not exist uniquely in the declared order"
            )
        return greatest[0]


def validate_finite_idempotent_semiring(
    semiring: FiniteIdempotentSemiring,
) -> None:
    """Exhaustively verify the finite idempotent-semiring law table."""

    elements = semiring.elements
    if not elements:
        raise SemiringLawError("semiring must contain at least one element")
    if len({repr(element) for element in elements}) != len(elements):
        raise SemiringLawError("semiring elements must be distinct")
    if semiring.zero not in elements or semiring.one not in elements:
        raise SemiringLawError("zero and one must belong to the carrier")
    if semiring.top not in elements:
        raise SemiringLawError("top must belong to the carrier")

    def require_closed(value: Any, law: str) -> None:
        if value not in elements:
            raise SemiringLawError(f"{law} is not closed on the carrier")

    for a in elements:
        if semiring.add(a, a) != a:
            raise SemiringLawError("addition is not idempotent")
        if semiring.add(a, semiring.zero) != a:
            raise SemiringLawError("additive zero law failed")
        if semiring.mul(a, semiring.one) != a:
            raise SemiringLawError("right multiplicative identity failed")
        if semiring.mul(semiring.one, a) != a:
            raise SemiringLawError("left multiplicative identity failed")
        if semiring.mul(a, semiring.zero) != semiring.zero:
            raise SemiringLawError("right zero annihilation failed")
        if semiring.mul(semiring.zero, a) != semiring.zero:
            raise SemiringLawError("left zero annihilation failed")
        if not semiring.leq(a, semiring.top):
            raise SemiringLawError("declared top is not above every element")
        for b in elements:
            require_closed(semiring.add(a, b), "addition")
            require_closed(semiring.mul(a, b), "multiplication")
            if semiring.add(a, b) != semiring.add(b, a):
                raise SemiringLawError("addition is not commutative")
            for c in elements:
                if semiring.add(semiring.add(a, b), c) != semiring.add(
                    a, semiring.add(b, c)
                ):
                    raise SemiringLawError("addition is not associative")
                if semiring.mul(semiring.mul(a, b), c) != semiring.mul(
                    a, semiring.mul(b, c)
                ):
                    raise SemiringLawError("multiplication is not associative")
                if semiring.mul(a, semiring.add(b, c)) != semiring.add(
                    semiring.mul(a, b), semiring.mul(a, c)
                ):
                    raise SemiringLawError("left distributivity failed")
                if semiring.mul(semiring.add(a, b), c) != semiring.add(
                    semiring.mul(a, c), semiring.mul(b, c)
                ):
                    raise SemiringLawError("right distributivity failed")


def capped_max_plus(cap: int) -> FiniteIdempotentSemiring:
    """Return the finite complete max-plus semiring ``{-inf,0,...,cap}``."""

    if isinstance(cap, bool) or not isinstance(cap, int) or cap < 0:
        raise ValueError("cap must be a non-negative integer")
    elements: tuple[Weight, ...] = (None,) + tuple(range(cap + 1))

    def add(left: Weight, right: Weight) -> Weight:
        return envelope(left, right, "max")

    def mul(left: Weight, right: Weight) -> Weight:
        if left is None or right is None:
            return None
        return min(cap, left + right)

    semiring = FiniteIdempotentSemiring(
        elements=elements,
        zero=None,
        one=0,
        top=cap,
        add=add,
        mul=mul,
    )
    validate_finite_idempotent_semiring(semiring)
    return semiring


def _validate_semiring_matrix(
    semiring: FiniteIdempotentSemiring,
    matrix: Sequence[Sequence[Any]],
) -> tuple[tuple[Any, ...], ...]:
    rows = tuple(tuple(row) for row in matrix)
    if not rows or not rows[0]:
        raise ValueError("semiring matrix must be nonempty")
    if any(len(row) != len(rows[0]) for row in rows):
        raise ValueError("semiring matrix rows must have equal length")
    if any(value not in semiring.elements for row in rows for value in row):
        raise ValueError("matrix entry is outside the semiring carrier")
    return rows


def semiring_matvec(
    semiring: FiniteIdempotentSemiring,
    matrix: Sequence[Sequence[Any]],
    vector: Sequence[Any],
) -> tuple[Any, ...]:
    a = _validate_semiring_matrix(semiring, matrix)
    x = tuple(vector)
    if len(a[0]) != len(x):
        raise ValueError("matrix/vector dimensions do not agree")
    if any(value not in semiring.elements for value in x):
        raise ValueError("vector entry is outside the semiring carrier")
    out = []
    for row in a:
        value = semiring.zero
        for coefficient, item in zip(row, x):
            value = semiring.add(value, semiring.mul(coefficient, item))
        out.append(value)
    return tuple(out)


def semiring_vecmat(
    semiring: FiniteIdempotentSemiring,
    vector: Sequence[Any],
    matrix: Sequence[Sequence[Any]],
) -> tuple[Any, ...]:
    a = _validate_semiring_matrix(semiring, matrix)
    y = tuple(vector)
    if len(y) != len(a):
        raise ValueError("vector/matrix dimensions do not agree")
    if any(value not in semiring.elements for value in y):
        raise ValueError("vector entry is outside the semiring carrier")
    out = []
    for column in range(len(a[0])):
        value = semiring.zero
        for row in range(len(a)):
            value = semiring.add(value, semiring.mul(y[row], a[row][column]))
        out.append(value)
    return tuple(out)


def scalar_residual(
    semiring: FiniteIdempotentSemiring, coefficient: Any, bound: Any
) -> Any:
    if coefficient not in semiring.elements or bound not in semiring.elements:
        raise ValueError("residual inputs must belong to the semiring")
    feasible = [
        candidate
        for candidate in semiring.elements
        if semiring.leq(semiring.mul(coefficient, candidate), bound)
    ]
    greatest = [
        candidate
        for candidate in feasible
        if all(semiring.leq(other, candidate) for other in feasible)
    ]
    if len(greatest) != 1:
        raise ResidualDoesNotExist(
            "the declared multiplication map has no greatest residual"
        )
    return greatest[0]


def right_matrix_residual(
    semiring: FiniteIdempotentSemiring,
    matrix: Sequence[Sequence[Any]],
    bound: Sequence[Any],
) -> tuple[Any, ...]:
    """Greatest vector ``x`` satisfying ``matrix * x <= bound``."""

    a = _validate_semiring_matrix(semiring, matrix)
    b = tuple(bound)
    if len(b) != len(a):
        raise ValueError("bound length must equal matrix row count")
    return tuple(
        semiring.meet(
            scalar_residual(semiring, a[row][column], b[row])
            for row in range(len(a))
        )
        for column in range(len(a[0]))
    )


def left_matrix_residual(
    semiring: FiniteIdempotentSemiring,
    matrix: Sequence[Sequence[Any]],
    bound: Sequence[Any],
) -> tuple[Any, ...]:
    """Greatest row vector ``y`` satisfying ``y * matrix <= bound``."""

    a = _validate_semiring_matrix(semiring, matrix)
    b = tuple(bound)
    if len(b) != len(a[0]):
        raise ValueError("bound length must equal matrix column count")
    return tuple(
        semiring.meet(
            scalar_residual(semiring, a[row][column], b[column])
            for column in range(len(a[0]))
        )
        for row in range(len(a))
    )


def vector_leq(
    semiring: FiniteIdempotentSemiring,
    left: Sequence[Any],
    right: Sequence[Any],
) -> bool:
    a = tuple(left)
    b = tuple(right)
    if len(a) != len(b):
        raise ValueError("vector lengths must agree")
    return all(semiring.leq(x, y) for x, y in zip(a, b))


def bellman_operator(
    semiring: FiniteIdempotentSemiring,
    matrix: Sequence[Sequence[Any]],
    bias: Sequence[Any],
    state: Sequence[Any],
) -> tuple[Any, ...]:
    product_value = semiring_matvec(semiring, matrix, state)
    b = tuple(bias)
    if len(b) != len(product_value):
        raise ValueError("bias length must equal matrix row count")
    return tuple(
        semiring.add(bias_value, dynamic_value)
        for bias_value, dynamic_value in zip(b, product_value)
    )


@dataclass(frozen=True)
class FixedPointResult:
    value: tuple[Any, ...]
    iterations: int
    extremum: Literal["least", "greatest"]


def bellman_least_fixed_point(
    semiring: FiniteIdempotentSemiring,
    matrix: Sequence[Sequence[Any]],
    bias: Sequence[Any],
) -> FixedPointResult:
    b = tuple(bias)
    state = (semiring.zero,) * len(b)
    limit = len(semiring.elements) ** len(b) + 1
    for iteration in range(1, limit + 1):
        nxt = bellman_operator(semiring, matrix, b, state)
        if nxt == state:
            return FixedPointResult(state, iteration, "least")
        if not vector_leq(semiring, state, nxt):
            raise SemiringLawError("Bellman bottom iteration is not ascending")
        state = nxt
    raise AssertionError("finite Bellman least-fixed-point iteration did not stabilize")


def bellman_greatest_fixed_point(
    semiring: FiniteIdempotentSemiring,
    matrix: Sequence[Sequence[Any]],
    bias: Sequence[Any],
) -> FixedPointResult:
    b = tuple(bias)
    state = (semiring.top,) * len(b)
    limit = len(semiring.elements) ** len(b) + 1
    for iteration in range(1, limit + 1):
        nxt = bellman_operator(semiring, matrix, b, state)
        if nxt == state:
            return FixedPointResult(state, iteration, "greatest")
        if not vector_leq(semiring, nxt, state):
            raise SemiringLawError("Bellman top iteration is not descending")
        state = nxt
    raise AssertionError("finite Bellman greatest-fixed-point iteration did not stabilize")


def enumerate_fixed_points(
    semiring: FiniteIdempotentSemiring,
    matrix: Sequence[Sequence[Any]],
    bias: Sequence[Any],
) -> tuple[tuple[Any, ...], ...]:
    b = tuple(bias)
    return tuple(
        state
        for state in product(semiring.elements, repeat=len(b))
        if tuple(state) == bellman_operator(semiring, matrix, b, state)
    )
