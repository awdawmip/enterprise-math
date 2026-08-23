#!/usr/bin/env python3
"""Exact checker for RS-TD-IE-WEIGHTED-INCIDENCE-ENERGY-DIRICHLET-CALCULUS.

This script intentionally treats weighted Dirichlet/flow energy as requiring
extra declared structure beyond bare incidence:
- an oriented finite graph incidence operator;
- strictly positive conductances for the positive-energy theorems;
- the reciprocal resistance inner product for flows;
- explicit boundary/source semantics.

All theorem-level arithmetic uses fractions.Fraction.
"""

from __future__ import annotations

from fractions import Fraction as F
from typing import Sequence


def Z(x) -> F:
    return x if isinstance(x, F) else F(x)


def zeros(r: int, c: int) -> list[list[F]]:
    return [[F(0) for _ in range(c)] for _ in range(r)]


def transpose(A: Sequence[Sequence[F]]) -> list[list[F]]:
    return [list(row) for row in zip(*A)] if A else []


def matmul(A: Sequence[Sequence[F]], B: Sequence[Sequence[F]]) -> list[list[F]]:
    if not A or not B:
        return []
    BT = transpose(B)
    return [[sum((a * b for a, b in zip(row, col)), F(0)) for col in BT] for row in A]


def matvec(A: Sequence[Sequence[F]], x: Sequence[F]) -> list[F]:
    return [sum((a * b for a, b in zip(row, x)), F(0)) for row in A]


def vecdot(x: Sequence[F], y: Sequence[F]) -> F:
    return sum((a * b for a, b in zip(x, y)), F(0))


def sub(x: Sequence[F], y: Sequence[F]) -> list[F]:
    return [a - b for a, b in zip(x, y)]


def scale(a: F, x: Sequence[F]) -> list[F]:
    return [a * b for b in x]


def eye(n: int) -> list[list[F]]:
    A = zeros(n, n)
    for i in range(n):
        A[i][i] = F(1)
    return A


def matrix_rank(A: Sequence[Sequence[F]]) -> int:
    M = [list(map(Z, row)) for row in A]
    if not M:
        return 0
    r, c = len(M), len(M[0])
    row = 0
    rank = 0
    for col in range(c):
        pivot = next((i for i in range(row, r) if M[i][col] != 0), None)
        if pivot is None:
            continue
        M[row], M[pivot] = M[pivot], M[row]
        p = M[row][col]
        M[row] = [v / p for v in M[row]]
        for i in range(r):
            if i != row and M[i][col] != 0:
                f = M[i][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[row])]
        row += 1
        rank += 1
        if row == r:
            break
    return rank


def solve(A: Sequence[Sequence[F]], b: Sequence[F]) -> list[F]:
    """Solve a square nonsingular system exactly."""
    n = len(A)
    if n == 0:
        return []
    if any(len(row) != n for row in A) or len(b) != n:
        raise ValueError("solve expects a square system")
    M = [list(map(Z, row)) + [Z(rhs)] for row, rhs in zip(A, b)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if M[i][col] != 0), None)
        if pivot is None:
            raise ValueError("singular matrix")
        M[col], M[pivot] = M[pivot], M[col]
        p = M[col][col]
        M[col] = [v / p for v in M[col]]
        for i in range(n):
            if i != col and M[i][col] != 0:
                f = M[i][col]
                M[i] = [a - f * b_ for a, b_ in zip(M[i], M[col])]
    return [M[i][-1] for i in range(n)]


def submatrix(A: Sequence[Sequence[F]], rows: Sequence[int], cols: Sequence[int]) -> list[list[F]]:
    return [[A[i][j] for j in cols] for i in rows]


def incidence(n: int, edges: Sequence[tuple[int, int, F]]) -> list[list[F]]:
    """B has -1 at tail and +1 at head."""
    B = zeros(n, len(edges))
    for e, (tail, head, _c) in enumerate(edges):
        if tail == head:
            raise ValueError("self-loops excluded in this checker")
        B[tail][e] = F(-1)
        B[head][e] = F(1)
    return B


def validate_positive_conductances(edges: Sequence[tuple[int, int, F]]) -> None:
    if any(Z(c) <= 0 for _u, _v, c in edges):
        raise ValueError("positive-energy theorems require conductance c_e > 0")


def laplacian(n: int, edges: Sequence[tuple[int, int, F]], *, require_positive: bool = True) -> list[list[F]]:
    if require_positive:
        validate_positive_conductances(edges)
    L = zeros(n, n)
    for u, v, c0 in edges:
        c = Z(c0)
        L[u][u] += c
        L[v][v] += c
        L[u][v] -= c
        L[v][u] -= c
    return L


def dirichlet_energy(u: Sequence[F], edges: Sequence[tuple[int, int, F]], *, require_positive: bool = True) -> F:
    if require_positive:
        validate_positive_conductances(edges)
    return sum((Z(c) * (Z(u[v]) - Z(u[w])) ** 2 for v, w, c in edges), F(0))


def flow_energy(j: Sequence[F], edges: Sequence[tuple[int, int, F]]) -> F:
    validate_positive_conductances(edges)
    if len(j) != len(edges):
        raise ValueError("flow length mismatch")
    return sum((Z(x) ** 2 / Z(c) for x, (_u, _v, c) in zip(j, edges)), F(0))


def source_from_flow(n: int, edges: Sequence[tuple[int, int, F]], j: Sequence[F]) -> list[F]:
    """q=-B j, so q>0 means net outflow/source."""
    B = incidence(n, edges)
    return scale(F(-1), matvec(B, list(map(Z, j))))


def gradient_flow(u: Sequence[F], edges: Sequence[tuple[int, int, F]]) -> list[F]:
    """Ohm/gradient flow j=-C B^T u."""
    validate_positive_conductances(edges)
    return [Z(c) * (Z(u[tail]) - Z(u[head])) for tail, head, c in edges]


def r_inner(x: Sequence[F], y: Sequence[F], edges: Sequence[tuple[int, int, F]]) -> F:
    validate_positive_conductances(edges)
    return sum((Z(a) * Z(b) / Z(c) for a, b, (_u, _v, c) in zip(x, y, edges)), F(0))


def connected_components(n: int, edges: Sequence[tuple[int, int, F]], *, positive_support_only: bool = True) -> list[set[int]]:
    adj = [set() for _ in range(n)]
    for u, v, c in edges:
        if positive_support_only and Z(c) <= 0:
            continue
        adj[u].add(v)
        adj[v].add(u)
    seen = set()
    comps = []
    for s in range(n):
        if s in seen:
            continue
        stack = [s]
        comp = set()
        seen.add(s)
        while stack:
            x = stack.pop()
            comp.add(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        comps.append(comp)
    return comps


def dirichlet_minimizer(
    n: int,
    edges: Sequence[tuple[int, int, F]],
    boundary_values: dict[int, F],
) -> list[F]:
    """Unique minimizer when every connected component meets the boundary."""
    validate_positive_conductances(edges)
    boundary = sorted(boundary_values)
    if not boundary:
        raise ValueError("boundary must be nonempty for unique grounded minimizer")
    comps = connected_components(n, edges)
    Bset = set(boundary)
    if any(comp.isdisjoint(Bset) for comp in comps):
        raise ValueError("each connected component must meet the boundary")
    interior = [v for v in range(n) if v not in Bset]
    u = [F(0) for _ in range(n)]
    for v, val in boundary_values.items():
        u[v] = Z(val)
    if not interior:
        return u
    L = laplacian(n, edges)
    LII = submatrix(L, interior, interior)
    LIB = submatrix(L, interior, boundary)
    f = [u[v] for v in boundary]
    rhs = scale(F(-1), matvec(LIB, f))
    sol = solve(LII, rhs)
    for v, val in zip(interior, sol):
        u[v] = val
    return u


def grounded_potential_for_source(
    n: int,
    edges: Sequence[tuple[int, int, F]],
    q: Sequence[F],
    ground: int,
) -> list[F]:
    """Solve L u=q with u_ground=0 on a connected positive graph."""
    validate_positive_conductances(edges)
    if sum(map(Z, q), F(0)) != 0:
        raise ValueError("source must sum to zero on a connected graph")
    if len(connected_components(n, edges)) != 1:
        raise ValueError("this helper expects a connected graph")
    L = laplacian(n, edges)
    keep = [v for v in range(n) if v != ground]
    A = submatrix(L, keep, keep)
    rhs = [Z(q[v]) for v in keep]
    sol = solve(A, rhs)
    u = [F(0) for _ in range(n)]
    for v, val in zip(keep, sol):
        u[v] = val
    return u


def thomson_minimizer(
    n: int,
    edges: Sequence[tuple[int, int, F]],
    q: Sequence[F],
    ground: int,
) -> list[F]:
    u = grounded_potential_for_source(n, edges, q, ground)
    j = gradient_flow(u, edges)
    assert source_from_flow(n, edges, j) == list(map(Z, q))
    return j


def effective_resistance(
    n: int,
    edges: Sequence[tuple[int, int, F]],
    a: int,
    b: int,
) -> F:
    q = [F(0) for _ in range(n)]
    q[a] = F(1)
    q[b] = F(-1)
    u = grounded_potential_for_source(n, edges, q, b)
    j = gradient_flow(u, edges)
    e = flow_energy(j, edges)
    assert e == u[a] - u[b]
    return e


def kron_reduce(
    L: Sequence[Sequence[F]],
    boundary: Sequence[int],
) -> list[list[F]]:
    n = len(L)
    B = list(boundary)
    I = [i for i in range(n) if i not in set(B)]
    LBB = submatrix(L, B, B)
    if not I:
        return [row[:] for row in LBB]
    LBI = submatrix(L, B, I)
    LIB = submatrix(L, I, B)
    LII = submatrix(L, I, I)
    inv_cols = [solve(LII, col) for col in transpose(eye(len(I)))]
    inv = transpose(inv_cols)
    correction = matmul(matmul(LBI, inv), LIB)
    return [[LBB[i][j] - correction[i][j] for j in range(len(B))] for i in range(len(B))]


def quadratic(A: Sequence[Sequence[F]], x: Sequence[F]) -> F:
    return vecdot(list(map(Z, x)), matvec(A, list(map(Z, x))))


def overlap_gram(M: Sequence[Sequence[int]]) -> list[list[F]]:
    A = [[F(v) for v in row] for row in M]
    return matmul(transpose(A), A)


TESTS: list[tuple[str, callable]] = []


def check(name):
    def deco(fn):
        TESTS.append((name, fn))
        return fn
    return deco


@check("positive_dirichlet_psd_and_connected_kernel")
def _():
    edges = [(0, 1, F(2)), (1, 2, F(3))]
    L = laplacian(3, edges)
    samples = [
        [F(0), F(0), F(0)],
        [F(1), F(1), F(1)],
        [F(0), F(1), F(2)],
        [F(-2), F(5), F(1)],
    ]
    assert all(dirichlet_energy(u, edges) >= 0 for u in samples)
    assert matvec(L, [F(1), F(1), F(1)]) == [F(0)] * 3
    assert matrix_rank(L) == 2


@check("orientation_invariance_potential_flow_source")
def _():
    edges = [(0, 1, F(2)), (1, 2, F(3)), (0, 2, F(5))]
    flipped = [(0, 1, F(2)), (2, 1, F(3)), (0, 2, F(5))]
    u = [F(7, 3), F(-1, 2), F(4, 5)]
    assert laplacian(3, edges) == laplacian(3, flipped)
    assert dirichlet_energy(u, edges) == dirichlet_energy(u, flipped)
    j = [F(2, 3), F(-4, 5), F(9, 7)]
    jf = [j[0], -j[1], j[2]]
    assert flow_energy(j, edges) == flow_energy(jf, flipped)
    assert source_from_flow(3, edges, j) == source_from_flow(3, flipped, jf)


@check("dirichlet_minimizer_exact_and_exhaustive_grid")
def _():
    edges = [(0, 1, F(2)), (1, 2, F(3))]
    u = dirichlet_minimizer(3, edges, {0: F(0), 2: F(1)})
    assert u == [F(0), F(3, 5), F(1)]
    L = laplacian(3, edges)
    assert matvec(L, u)[1] == 0
    emin = dirichlet_energy(u, edges)
    grid = [F(k, 10) for k in range(11)]
    vals = [(dirichlet_energy([F(0), x, F(1)], edges), x) for x in grid]
    assert min(vals)[0] == emin
    assert [x for e, x in vals if e == emin] == [F(3, 5)]


@check("thomson_minimizer_and_circulation_orthogonality")
def _():
    edges = [(0, 1, F(1)), (1, 2, F(1)), (0, 2, F(1))]
    q = [F(1), F(0), F(-1)]
    j = thomson_minimizer(3, edges, q, ground=2)
    assert j == [F(1, 3), F(1, 3), F(2, 3)]
    cycle = [F(1), F(1), F(-1)]
    B = incidence(3, edges)
    assert matvec(B, cycle) == [F(0), F(0), F(0)]
    assert r_inner(j, cycle, edges) == 0
    emin = flow_energy(j, edges)
    candidates = []
    for k in range(7):
        t = F(k, 6)
        flow = [t, t, F(1) - t]
        assert source_from_flow(3, edges, flow) == q
        candidates.append((flow_energy(flow, edges), t))
    assert min(candidates)[0] == emin == F(2, 3)
    assert [t for e, t in candidates if e == emin] == [F(1, 3)]


@check("full_gradient_circulation_decomposition")
def _():
    edges = [(0, 1, F(2)), (1, 2, F(3)), (0, 2, F(5))]
    x = [F(2), F(-1), F(4)]
    q = source_from_flow(3, edges, x)
    g = thomson_minimizer(3, edges, q, ground=2)
    z = sub(x, g)
    assert matvec(incidence(3, edges), z) == [F(0), F(0), F(0)]
    assert r_inner(g, z, edges) == 0
    assert flow_energy(x, edges) == flow_energy(g, edges) + flow_energy(z, edges)


@check("effective_resistance_series_parallel")
def _():
    series = [(0, 1, F(2)), (1, 2, F(3))]
    assert effective_resistance(3, series, 0, 2) == F(5, 6)
    parallel = [(0, 1, F(2)), (0, 1, F(3))]
    assert effective_resistance(2, parallel, 0, 1) == F(1, 5)


@check("kron_schur_preserves_boundary_energy")
def _():
    edges = [(0, 1, F(2)), (1, 2, F(3))]
    L = laplacian(3, edges)
    K = kron_reduce(L, [0, 2])
    expected = [[F(6, 5), F(-6, 5)], [F(-6, 5), F(6, 5)]]
    assert K == expected
    f = [F(0), F(1)]
    reduced_e = quadratic(K, f)
    u = dirichlet_minimizer(3, edges, {0: f[0], 2: f[1]})
    assert reduced_e == dirichlet_energy(u, edges) == F(6, 5)


@check("disconnected_kernel_multiplicity")
def _():
    edges = [(0, 1, F(2)), (2, 3, F(3))]
    L = laplacian(4, edges)
    comps = connected_components(4, edges)
    assert len(comps) == 2
    assert 4 - matrix_rank(L) == 2
    assert matvec(L, [F(1), F(1), F(0), F(0)]) == [F(0)] * 4
    assert matvec(L, [F(0), F(0), F(1), F(1)]) == [F(0)] * 4


@check("zero_weight_adds_kernel_and_is_rejected_by_positive_api")
def _():
    edges = [(0, 1, F(0))]
    L = laplacian(2, edges, require_positive=False)
    assert matrix_rank(L) == 0
    try:
        dirichlet_energy([F(0), F(1)], edges)
    except ValueError:
        pass
    else:
        raise AssertionError("zero conductance should be rejected by positive-energy API")


@check("negative_weight_breaks_positivity")
def _():
    edges = [(0, 1, F(-1))]
    e = dirichlet_energy([F(0), F(1)], edges, require_positive=False)
    assert e == F(-1)
    try:
        laplacian(2, edges)
    except ValueError:
        pass
    else:
        raise AssertionError("negative conductance should be rejected by positive-energy API")


@check("nonsymmetric_operator_is_not_energy_gradient_operator")
def _():
    A = [[F(1), F(1)], [F(0), F(1)]]
    AT = transpose(A)
    S = [[(A[i][j] + AT[i][j]) / 2 for j in range(2)] for i in range(2)]
    x = [F(1), F(2)]
    assert quadratic(A, x) == quadratic(S, x)
    grad_q = matvec([[A[i][j] + AT[i][j] for j in range(2)] for i in range(2)], x)
    two_Ax = scale(F(2), matvec(A, x))
    assert grad_q != two_Ax


@check("bare_overlap_gram_is_not_dirichlet_energy")
def _():
    M = [[1, 1], [1, 0]]
    G = overlap_gram(M)
    assert G == [[F(2), F(1)], [F(1), F(1)]]
    assert G[0][1] == 1  # one shared target witness
    constants = [F(1), F(1)]
    assert quadratic(G, constants) == F(5)
    # A connected graph Dirichlet energy must kill constants.
    edge_graph = [(0, 1, F(1))]
    assert dirichlet_energy(constants, edge_graph) == 0


@check("bare_incidence_does_not_determine_effective_resistance")
def _():
    same_graph_c1 = [(0, 1, F(1))]
    same_graph_c2 = [(0, 1, F(2))]
    assert effective_resistance(2, same_graph_c1, 0, 1) == F(1)
    assert effective_resistance(2, same_graph_c2, 0, 1) == F(1, 2)


@check("minimum_energy_flow_is_not_native_shortest_path")
def _():
    edges = [(0, 1, F(1)), (1, 2, F(1)), (0, 2, F(1))]
    q = [F(1), F(0), F(-1)]
    j = thomson_minimizer(3, edges, q, ground=2)
    direct_shortest_path_flow = [F(0), F(0), F(1)]
    assert j == [F(1, 3), F(1, 3), F(2, 3)]
    assert j != direct_shortest_path_flow
    assert flow_energy(j, edges) == F(2, 3) < flow_energy(direct_shortest_path_flow, edges)


@check("kron_obstruction_when_eliminated_component_unpinned")
def _():
    # Boundary vertex 0 is disconnected from interior component {1,2}.
    edges = [(1, 2, F(1))]
    L = laplacian(3, edges)
    try:
        kron_reduce(L, [0])
    except ValueError:
        pass
    else:
        raise AssertionError("Schur elimination must fail when L_II is singular")


@check("fixed_source_feasibility_requires_component_balance")
def _():
    edges = [(0, 1, F(1)), (2, 3, F(1))]
    q_bad = [F(1), F(0), F(-1), F(0)]
    comps = connected_components(4, edges)
    balances = [sum((q_bad[v] for v in comp), F(0)) for comp in comps]
    assert balances == [F(1), F(-1)]


def main() -> int:
    failures = []
    for name, fn in TESTS:
        try:
            fn()
        except Exception as exc:
            failures.append((name, f"{type(exc).__name__}: {exc}"))
    print(f"theorem_check_pairs={len(TESTS)}")
    print(f"mismatch_count={len(failures)}")
    print("global_tool_claim=NO")
    print("second_enterprise_weighted_domain=NOT_ESTABLISHED")
    print("classification=DOMAIN_SPECIALIZATION_ONLY")
    print("ownership_recommendation=SUBTOOL_OR_EXTENSION_OF_LAPLACIAN")
    if failures:
        for name, msg in failures:
            print(f"FAIL {name}: {msg}")
        return 1
    print("ALL_EXACT_CHECKS_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
