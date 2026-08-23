"""Exact finite toppling/Laplacian helpers for Enterprise tool-discovery.

This module deliberately separates:
- an auxiliary orientation used to build an undirected incidence matrix;
- the orientation-invariant Laplacian B W B^T;
- a generic integer toppling matrix with positive diagonal and
  nonpositive off-diagonal entries.

The mathematics is classical.  The module is a typed Enterprise interface,
not a claim of new graph/chip-firing mathematics.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Iterable, Sequence


IntVector = tuple[int, ...]
IntMatrix = tuple[tuple[int, ...], ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _vector(values: Iterable[int], *, name: str, length: int | None = None) -> IntVector:
    result = tuple(values)
    if length is not None and len(result) != length:
        raise ValueError(f"{name} must have length {length}")
    for value in result:
        _require_int(name, value)
    return result


def _matrix(rows: Iterable[Iterable[int]], *, name: str = "matrix") -> IntMatrix:
    result = tuple(tuple(row) for row in rows)
    if not result:
        raise ValueError(f"{name} must be nonempty")
    width = len(result[0])
    if width == 0:
        raise ValueError(f"{name} must have nonempty rows")
    if any(len(row) != width for row in result):
        raise ValueError(f"{name} rows must have equal length")
    for row in result:
        for value in row:
            _require_int(name, value)
    return result


def matvec(matrix: Sequence[Sequence[int]], vector: Sequence[int]) -> IntVector:
    m = _matrix(matrix)
    v = _vector(vector, name="vector", length=len(m[0]))
    return tuple(sum(row[j] * v[j] for j in range(len(v))) for row in m)


def transpose(matrix: Sequence[Sequence[int]]) -> IntMatrix:
    m = _matrix(matrix)
    return tuple(tuple(m[i][j] for i in range(len(m))) for j in range(len(m[0])))


def determinant(matrix: Sequence[Sequence[int]]) -> int:
    """Exact Bareiss determinant."""
    a = [list(row) for row in _matrix(matrix)]
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("determinant requires a square matrix")
    if n == 1:
        return a[0][0]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if a[r][k] != 0), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot_value - a[i][k] * a[k][j]) // prev
        for i in range(k + 1, n):
            a[i][k] = 0
        prev = pivot_value
    return sign * a[-1][-1]


def solve_exact(matrix: Sequence[Sequence[int]], rhs: Sequence[int]) -> tuple[Fraction, ...]:
    """Solve a nonsingular square integer system over Q."""
    a0 = _matrix(matrix)
    n = len(a0)
    if any(len(row) != n for row in a0):
        raise ValueError("solve_exact requires a square matrix")
    b0 = _vector(rhs, name="rhs", length=n)
    a = [[Fraction(value) for value in row] + [Fraction(b0[i])] for i, row in enumerate(a0)]
    for col in range(n):
        pivot = next((row for row in range(col, n) if a[row][col] != 0), None)
        if pivot is None:
            raise ValueError("matrix is singular")
        a[col], a[pivot] = a[pivot], a[col]
        pivot_value = a[col][col]
        a[col] = [value / pivot_value for value in a[col]]
        for row in range(n):
            if row == col:
                continue
            factor = a[row][col]
            if factor:
                a[row] = [a[row][j] - factor * a[col][j] for j in range(n + 1)]
    return tuple(a[i][-1] for i in range(n))


def _lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)


@dataclass(frozen=True)
class StabilizationResult:
    stable_state: IntVector
    odometer: IntVector
    steps: int
    termination_witness: IntVector
    termination_margin: IntVector


@dataclass(frozen=True)
class TopplingSystem:
    """Finite integer toppling system c -> c - Delta e_i.

    Required sign pattern:
      Delta_ii > 0,
      Delta_ij <= 0 for i != j.

    A state is nonnegative and i is legal iff c_i >= Delta_ii.
    """

    delta: IntMatrix
    labels: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        d = _matrix(self.delta, name="delta")
        n = len(d)
        if any(len(row) != n for row in d):
            raise ValueError("delta must be square")
        for i in range(n):
            if d[i][i] <= 0:
                raise ValueError("delta diagonal must be positive")
            for j in range(n):
                if i != j and d[i][j] > 0:
                    raise ValueError("delta off-diagonal entries must be nonpositive")
        if self.labels and len(self.labels) != n:
            raise ValueError("labels must match delta size")
        object.__setattr__(self, "delta", d)

    @property
    def size(self) -> int:
        return len(self.delta)

    def state(self, values: Sequence[int]) -> IntVector:
        result = _vector(values, name="state", length=self.size)
        if any(value < 0 for value in result):
            raise ValueError("state must be nonnegative")
        return result

    def legal_sites(self, state: Sequence[int]) -> IntVector:
        c = self.state(state)
        return tuple(i for i in range(self.size) if c[i] >= self.delta[i][i])

    def stable(self, state: Sequence[int]) -> bool:
        return not self.legal_sites(state)

    def fire(self, state: Sequence[int], site: int) -> IntVector:
        c = list(self.state(state))
        _require_int("site", site)
        if not 0 <= site < self.size:
            raise IndexError("site out of range")
        if c[site] < self.delta[site][site]:
            raise ValueError("site is not legal")
        for row in range(self.size):
            c[row] -= self.delta[row][site]
        if any(value < 0 for value in c):
            raise AssertionError("Z-matrix legal firing must preserve nonnegativity")
        return tuple(c)

    def witness_margin(self, witness: Sequence[int]) -> IntVector:
        q = _vector(witness, name="termination witness", length=self.size)
        if any(value <= 0 for value in q):
            raise ValueError("termination witness must be strictly positive")
        return tuple(
            sum(q[row] * self.delta[row][col] for row in range(self.size))
            for col in range(self.size)
        )

    def strict_termination_witness(self) -> IntVector:
        """Return an exact positive integer q with q^T Delta > 0 when found.

        We solve Delta^T q = 1 over Q.  Positivity is checked, not assumed.
        This is a certificate finder, not a completeness claim for arbitrary
        matrices outside the declared Z-matrix semantics.
        """
        q_rat = solve_exact(transpose(self.delta), (1,) * self.size)
        if any(value <= 0 for value in q_rat):
            raise ValueError("no positive witness obtained from Delta^T q = 1")
        scale = 1
        for value in q_rat:
            scale = _lcm(scale, value.denominator)
        q = tuple(int(value * scale) for value in q_rat)
        margin = self.witness_margin(q)
        if any(value <= 0 for value in margin):
            raise AssertionError("constructed witness is not strict")
        return q

    def stabilize(
        self,
        state: Sequence[int],
        *,
        witness: Sequence[int] | None = None,
    ) -> StabilizationResult:
        c = list(self.state(state))
        q = self.strict_termination_witness() if witness is None else _vector(
            witness, name="termination witness", length=self.size
        )
        margin = self.witness_margin(q)
        if any(value <= 0 for value in margin):
            raise ValueError("termination witness must have q^T Delta > 0")
        initial_potential = sum(q[i] * c[i] for i in range(self.size))
        min_margin = min(margin)
        max_steps = initial_potential // min_margin
        u = [0] * self.size
        steps = 0
        while True:
            legal = [i for i in range(self.size) if c[i] >= self.delta[i][i]]
            if not legal:
                return StabilizationResult(tuple(c), tuple(u), steps, tuple(q), tuple(margin))
            site = legal[0]
            for row in range(self.size):
                c[row] -= self.delta[row][site]
            u[site] += 1
            steps += 1
            if steps > max_steps:
                raise AssertionError("strict termination bound violated")

    def apply_firing_vector(self, state: Sequence[int], firings: Sequence[int]) -> IntVector:
        c = self.state(state)
        u = _vector(firings, name="firings", length=self.size)
        if any(value < 0 for value in u):
            raise ValueError("firings must be nonnegative")
        du = matvec(self.delta, u)
        return tuple(c[i] - du[i] for i in range(self.size))

    def verify_odometer_certificate(
        self,
        initial: Sequence[int],
        stable_state: Sequence[int],
        odometer: Sequence[int],
    ) -> bool:
        """Verify the compact odometer certificate without storing a firing log.

        The verifier first checks c^o = c - Delta u and stability.  It then
        deterministically reconstructs a legal realization using only u.
        By the least-action theorem, a legally realizable stabilizing u is the
        unique odometer and is coordinatewise <= every nonnegative stabilizing
        firing vector.
        """
        c0 = self.state(initial)
        final = self.state(stable_state)
        u = _vector(odometer, name="odometer", length=self.size)
        if any(value < 0 for value in u):
            return False
        if self.apply_firing_vector(c0, u) != final or not self.stable(final):
            return False
        remaining = list(u)
        current = c0
        while any(remaining):
            candidates = [
                i
                for i in range(self.size)
                if remaining[i] > 0 and current[i] >= self.delta[i][i]
            ]
            if not candidates:
                return False
            site = candidates[0]
            current = self.fire(current, site)
            remaining[site] -= 1
        return current == final

    def same_firing_lattice_class(self, left: Sequence[int], right: Sequence[int]) -> bool:
        """Exact membership test for left-right in Delta Z^n when Delta is nonsingular."""
        a = _vector(left, name="left", length=self.size)
        b = _vector(right, name="right", length=self.size)
        diff = tuple(a[i] - b[i] for i in range(self.size))
        coeff = solve_exact(self.delta, diff)
        return all(value.denominator == 1 for value in coeff)

    def cokernel_order(self) -> int:
        det = determinant(self.delta)
        if det == 0:
            raise ValueError("singular toppling matrix has infinite cokernel rank")
        return abs(det)


@dataclass(frozen=True)
class UndirectedEdge:
    u: int
    v: int
    weight: int = 1
    type_label: str | None = None

    def __post_init__(self) -> None:
        _require_int("u", self.u)
        _require_int("v", self.v)
        _require_int("weight", self.weight)
        if self.u == self.v:
            raise ValueError("loops are outside the core loopless interface")
        if self.weight <= 0:
            raise ValueError("edge weight must be positive")


def incidence_matrix(
    vertex_count: int,
    edges: Sequence[UndirectedEdge],
    *,
    reverse_columns: Iterable[int] = (),
) -> IntMatrix:
    _require_int("vertex_count", vertex_count)
    if vertex_count <= 0:
        raise ValueError("vertex_count must be positive")
    reverse = set(reverse_columns)
    if any(not isinstance(i, int) or isinstance(i, bool) for i in reverse):
        raise TypeError("reverse column indices must be integers")
    rows = [[0] * len(edges) for _ in range(vertex_count)]
    for j, edge in enumerate(edges):
        if not (0 <= edge.u < vertex_count and 0 <= edge.v < vertex_count):
            raise ValueError("edge endpoint out of range")
        tail, head = (edge.v, edge.u) if j in reverse else (edge.u, edge.v)
        rows[tail][j] = 1
        rows[head][j] = -1
    return tuple(tuple(row) for row in rows)


def divergence(incidence: Sequence[Sequence[int]], flow: Sequence[int]) -> IntVector:
    return matvec(incidence, flow)


def weighted_laplacian(
    incidence: Sequence[Sequence[int]],
    weights: Sequence[int],
) -> IntMatrix:
    b = _matrix(incidence, name="incidence")
    m = len(b[0])
    w = _vector(weights, name="weights", length=m)
    if any(value <= 0 for value in w):
        raise ValueError("weights must be positive integers")
    n = len(b)
    return tuple(
        tuple(sum(b[i][e] * w[e] * b[j][e] for e in range(m)) for j in range(n))
        for i in range(n)
    )


def graph_laplacian(
    vertex_count: int,
    edges: Sequence[UndirectedEdge],
    *,
    reverse_columns: Iterable[int] = (),
) -> IntMatrix:
    b = incidence_matrix(vertex_count, edges, reverse_columns=reverse_columns)
    return weighted_laplacian(b, tuple(edge.weight for edge in edges))


def reduced_graph_system(
    vertex_count: int,
    edges: Sequence[UndirectedEdge],
    sinks: Iterable[int],
) -> tuple[TopplingSystem, IntVector, IntMatrix]:
    sink_set = set(sinks)
    if not sink_set:
        raise ValueError("at least one sink is required")
    if any(not isinstance(s, int) or isinstance(s, bool) or not 0 <= s < vertex_count for s in sink_set):
        raise ValueError("sink out of range")
    full = graph_laplacian(vertex_count, edges)
    active = tuple(i for i in range(vertex_count) if i not in sink_set)
    if not active:
        raise ValueError("at least one active vertex is required")
    reduced = tuple(tuple(full[i][j] for j in active) for i in active)
    labels = tuple(str(i) for i in active)
    return TopplingSystem(reduced, labels), active, full


def full_graph_fire(
    state: Sequence[int],
    laplacian: Sequence[Sequence[int]],
    site: int,
) -> IntVector:
    l = _matrix(laplacian, name="laplacian")
    n = len(l)
    if any(len(row) != n for row in l):
        raise ValueError("laplacian must be square")
    c = _vector(state, name="state", length=n)
    _require_int("site", site)
    if not 0 <= site < n:
        raise IndexError("site out of range")
    if c[site] < l[site][site]:
        raise ValueError("site is not legal")
    result = tuple(c[row] - l[row][site] for row in range(n))
    if any(value < 0 for value in result):
        raise AssertionError("legal full-graph firing must preserve nonnegativity")
    return result
