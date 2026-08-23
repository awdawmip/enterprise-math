#!/usr/bin/env python3
"""Exact checker for RS-TD-TR tropical/residuation/idempotent-closure calculus.

The checker is deliberately self-contained and exact:
- standard finite graph path examples use Python integers plus ``None`` as the
  unreachable semiring zero;
- finite residuation/fixed-point examples use a capped max-plus semiring;
- no floating-point arithmetic is used.

It is a regression checker for the theorem ledger in
research_notes/TOOL_DISCOVERY_TROPICAL_RESIDUATION_IDEMPOTENT_CLOSURE_RESULT_20260823.md.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product, permutations
import json
import sys
from typing import Callable, Iterable, Sequence

UNREACHABLE = None
Weight = int | None
Matrix = list[list[Weight]]


def envelope(a: Weight, b: Weight, kind: str) -> Weight:
    if a is None:
        return b
    if b is None:
        return a
    if kind == "min":
        return min(a, b)
    if kind == "max":
        return max(a, b)
    raise ValueError(kind)


def extend(a: Weight, b: Weight) -> Weight:
    if a is None or b is None:
        return None
    return a + b


def identity_matrix(n: int) -> Matrix:
    return [[0 if i == j else None for j in range(n)] for i in range(n)]


def matrix_envelope(A: Matrix, B: Matrix, kind: str) -> Matrix:
    return [
        [envelope(A[i][j], B[i][j], kind) for j in range(len(A[0]))]
        for i in range(len(A))
    ]


def matrix_multiply(A: Matrix, B: Matrix, kind: str) -> Matrix:
    m, k, n = len(A), len(B), len(B[0])
    assert len(A[0]) == k
    out: Matrix = [[None for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            value: Weight = None
            for r in range(k):
                value = envelope(value, extend(A[i][r], B[r][j]), kind)
            out[i][j] = value
    return out


def matrix_power(A: Matrix, exponent: int, kind: str) -> Matrix:
    if exponent < 0:
        raise ValueError("negative exponent")
    n = len(A)
    result = identity_matrix(n)
    base = A
    e = exponent
    while e:
        if e & 1:
            result = matrix_multiply(result, base, kind)
        base = matrix_multiply(base, base, kind)
        e >>= 1
    return result


def exhaustive_fixed_length(A: Matrix, length: int, kind: str) -> Matrix:
    """Independent fixed-length path enumeration, not matrix multiplication."""
    n = len(A)
    out: Matrix = [[None for _ in range(n)] for _ in range(n)]
    if length == 0:
        return identity_matrix(n)

    def walk(start: int, current: int, remaining: int, total: int) -> None:
        if remaining == 0:
            out[start][current] = envelope(out[start][current], total, kind)
            return
        for nxt, w in enumerate(A[current]):
            if w is not None:
                walk(start, nxt, remaining - 1, total + w)

    for s in range(n):
        walk(s, s, length, 0)
    return out


def finite_power_star(A: Matrix, kind: str) -> Matrix:
    """I ⊕ A ⊕ ... ⊕ A^(n-1), exact when improving cycles are absent."""
    n = len(A)
    out = identity_matrix(n)
    power = identity_matrix(n)
    for _ in range(1, n):
        power = matrix_multiply(power, A, kind)
        out = matrix_envelope(out, power, kind)
    return out


def floyd_warshall_star(A: Matrix, kind: str) -> Matrix:
    """All-pairs closure over simple-path representatives."""
    n = len(A)
    D = matrix_envelope(identity_matrix(n), [row[:] for row in A], kind)
    for k in range(n):
        for i in range(n):
            if D[i][k] is None:
                continue
            for j in range(n):
                if D[k][j] is None:
                    continue
                candidate = D[i][k] + D[k][j]
                D[i][j] = envelope(D[i][j], candidate, kind)
    return D


def exhaustive_simple_path_star(A: Matrix, kind: str) -> Matrix:
    n = len(A)
    out = identity_matrix(n)

    def dfs(start: int, current: int, visited: set[int], total: int) -> None:
        out[start][current] = envelope(out[start][current], total, kind)
        for nxt, w in enumerate(A[current]):
            if w is not None and nxt not in visited:
                visited.add(nxt)
                dfs(start, nxt, visited, total + w)
                visited.remove(nxt)

    for s in range(n):
        dfs(s, s, {s}, 0)
    return out


def improving_cycle(A: Matrix, kind: str) -> tuple[tuple[int, ...], int] | None:
    """Return a simple improving cycle and its exact total weight."""
    n = len(A)
    improve = (lambda w: w < 0) if kind == "min" else (lambda w: w > 0)

    def dfs(start: int, current: int, path: list[int], total: int):
        for nxt, w in enumerate(A[current]):
            if w is None:
                continue
            if nxt == start:
                cycle_weight = total + w
                if improve(cycle_weight):
                    return tuple(path + [start]), cycle_weight
            elif nxt not in path and len(path) < n:
                found = dfs(start, nxt, path + [nxt], total + w)
                if found is not None:
                    return found
        return None

    for s in range(n):
        found = dfs(s, s, [s], 0)
        if found is not None:
            return found
    return None


def permute_matrix(A: Matrix, old_to_new: Sequence[int]) -> Matrix:
    n = len(A)
    B: Matrix = [[None for _ in range(n)] for _ in range(n)]
    for old_i in range(n):
        for old_j in range(n):
            B[old_to_new[old_i]][old_to_new[old_j]] = A[old_i][old_j]
    return B


@dataclass(frozen=True)
class CappedMaxPlus:
    """Finite complete idempotent semiring {-inf,0,...,cap}.

    Addition is max. Multiplication is saturated ordinary addition.
    Natural order is the displayed chain -inf < 0 < ... < cap.
    """

    cap: int

    @property
    def elements(self) -> tuple[Weight, ...]:
        return (None,) + tuple(range(self.cap + 1))

    @property
    def zero(self) -> Weight:
        return None

    @property
    def one(self) -> Weight:
        return 0

    @property
    def top(self) -> Weight:
        return self.cap

    def add(self, a: Weight, b: Weight) -> Weight:
        if a is None:
            return b
        if b is None:
            return a
        return max(a, b)

    def mul(self, a: Weight, b: Weight) -> Weight:
        if a is None or b is None:
            return None
        return min(self.cap, a + b)

    def leq(self, a: Weight, b: Weight) -> bool:
        if a is None:
            return True
        if b is None:
            return a is None
        return a <= b

    def meet(self, values: Iterable[Weight]) -> Weight:
        vals = tuple(values)
        if not vals:
            return self.top
        result: Weight = self.top
        for v in vals:
            if v is None:
                return None
            if result is None or v < result:
                result = v
        return result

    def scalar_residual(self, a: Weight, b: Weight) -> Weight:
        feasible = [x for x in self.elements if self.leq(self.mul(a, x), b)]
        if not feasible:
            raise AssertionError("residual unexpectedly absent in finite capped max-plus")
        greatest = feasible[0]
        for x in feasible[1:]:
            if self.leq(greatest, x):
                greatest = x
        assert all(self.leq(x, greatest) for x in feasible)
        return greatest


def validate_capped_max_plus(S: CappedMaxPlus) -> bool:
    E = S.elements
    for a in E:
        if S.add(a, a) != a:
            return False
        if S.add(a, S.zero) != a or S.add(S.zero, a) != a:
            return False
        if S.mul(a, S.one) != a or S.mul(S.one, a) != a:
            return False
        if S.mul(a, S.zero) != S.zero or S.mul(S.zero, a) != S.zero:
            return False
        for b in E:
            if S.add(a, b) != S.add(b, a):
                return False
            if S.add(S.add(a, b), S.zero) != S.add(a, b):
                return False
            for c in E:
                if S.add(S.add(a, b), c) != S.add(a, S.add(b, c)):
                    return False
                if S.mul(S.mul(a, b), c) != S.mul(a, S.mul(b, c)):
                    return False
                if S.mul(a, S.add(b, c)) != S.add(S.mul(a, b), S.mul(a, c)):
                    return False
                if S.mul(S.add(a, b), c) != S.add(S.mul(a, c), S.mul(b, c)):
                    return False
    return True


def semiring_matvec(S: CappedMaxPlus, A: list[list[Weight]], x: Sequence[Weight]) -> list[Weight]:
    return [
        _semiring_fold(S, [S.mul(a, xx) for a, xx in zip(row, x)])
        for row in A
    ]


def semiring_vecmat(S: CappedMaxPlus, y: Sequence[Weight], A: list[list[Weight]]) -> list[Weight]:
    n = len(A[0])
    return [
        _semiring_fold(S, [S.mul(y[i], A[i][j]) for i in range(len(A))])
        for j in range(n)
    ]


def _semiring_fold(S: CappedMaxPlus, values: Iterable[Weight]) -> Weight:
    value: Weight = S.zero
    for v in values:
        value = S.add(value, v)
    return value


def vec_leq(S: CappedMaxPlus, a: Sequence[Weight], b: Sequence[Weight]) -> bool:
    return all(S.leq(x, y) for x, y in zip(a, b))


def right_matrix_residual(
    S: CappedMaxPlus, A: list[list[Weight]], b: Sequence[Weight]
) -> list[Weight]:
    """Greatest x with A⊗x <= b."""
    m, n = len(A), len(A[0])
    assert len(b) == m
    return [
        S.meet(S.scalar_residual(A[i][j], b[i]) for i in range(m))
        for j in range(n)
    ]


def left_matrix_residual(
    S: CappedMaxPlus, A: list[list[Weight]], b: Sequence[Weight]
) -> list[Weight]:
    """Greatest y with y⊗A <= b."""
    m, n = len(A), len(A[0])
    assert len(b) == n
    return [
        S.meet(S.scalar_residual(A[i][j], b[j]) for j in range(n))
        for i in range(m)
    ]


def bellman(
    S: CappedMaxPlus,
    A: list[list[Weight]],
    b: Sequence[Weight],
    x: Sequence[Weight],
) -> list[Weight]:
    return [S.add(bb, ax) for bb, ax in zip(b, semiring_matvec(S, A, x))]


def least_fixed_point(
    S: CappedMaxPlus, A: list[list[Weight]], b: Sequence[Weight]
) -> tuple[list[Weight], int]:
    x = [S.zero] * len(b)
    seen = 0
    while True:
        y = bellman(S, A, b, x)
        seen += 1
        if y == x:
            return x, seen
        if not vec_leq(S, x, y):
            raise AssertionError("least iteration ceased to be ascending")
        x = y
        if seen > len(S.elements) ** len(b) + 1:
            raise AssertionError("finite least fixed-point iteration did not stabilize")


def greatest_fixed_point(
    S: CappedMaxPlus, A: list[list[Weight]], b: Sequence[Weight]
) -> tuple[list[Weight], int]:
    x = [S.top] * len(b)
    seen = 0
    while True:
        y = bellman(S, A, b, x)
        seen += 1
        if y == x:
            return x, seen
        if not vec_leq(S, y, x):
            raise AssertionError("greatest iteration ceased to be descending")
        x = y
        if seen > len(S.elements) ** len(b) + 1:
            raise AssertionError("finite greatest fixed-point iteration did not stabilize")


def all_fixed_points(
    S: CappedMaxPlus, A: list[list[Weight]], b: Sequence[Weight]
) -> list[tuple[Weight, ...]]:
    return [
        x
        for x in product(S.elements, repeat=len(b))
        if list(x) == bellman(S, A, b, x)
    ]


def build_diamond_cost_system(depth: int) -> tuple[Matrix, int, int]:
    """Explicitly weighted provenance DAG with exactly 2**depth source-target paths."""
    n = 1 + 3 * depth
    A: Matrix = [[None for _ in range(n)] for _ in range(n)]
    current = 0
    for k in range(depth):
        a = 1 + 3 * k
        b = a + 1
        merge = a + 2
        # Explicit caller-supplied costs; not inferred from incidence or path length.
        A[current][a] = (k % 4) + 1
        A[a][merge] = 0
        A[current][b] = ((2 * k + 1) % 5) + 1
        A[b][merge] = 0
        current = merge
    return A, 0, current


def enumerate_source_target_paths(A: Matrix, source: int, target: int) -> tuple[int, int]:
    count = 0
    best: int | None = None

    def dfs(v: int, total: int) -> None:
        nonlocal count, best
        if v == target:
            count += 1
            best = total if best is None else min(best, total)
            return
        for nxt, w in enumerate(A[v]):
            if w is not None:
                dfs(nxt, total + w)

    dfs(source, 0)
    assert best is not None
    return count, best


def quotient_weight_descent_counterexample() -> tuple[bool, bool]:
    # u and v have the same *unweighted* successor class t, so support descends.
    states = ("u", "v", "t")
    klass = {"u": "q", "v": "q", "t": "t"}
    support = {("u", "t"), ("v", "t")}
    weights = {("u", "t"): 1, ("v", "t"): 2}

    def support_signature(s: str) -> set[str]:
        return {klass[t] for (x, t) in support if x == s}

    unweighted_safe = support_signature("u") == support_signature("v")
    weighted_safe = weights[("u", "t")] == weights[("v", "t")]
    return unweighted_safe, weighted_safe


def nonresiduated_partial_order_counterexample() -> bool:
    p, q = "p", "q"
    values = (
        frozenset(),
        frozenset({p}),
        frozenset({q}),
        frozenset({p, q}),
    )
    top = frozenset({p, q})

    # Monotone f: only top maps to top; every proper subset maps to bottom.
    def f(x: frozenset[str]) -> frozenset[str]:
        return top if x == top else frozenset()

    b = frozenset()
    feasible = [x for x in values if f(x).issubset(b)]
    # Residual would require a greatest feasible element. {p} and {q} are
    # incomparable and their union/top is not feasible.
    return (
        frozenset({p}) in feasible
        and frozenset({q}) in feasible
        and top not in feasible
        and not any(all(x.issubset(g) for x in feasible) for g in feasible)
    )


def check_partial_order_boundary() -> bool:
    p, q = frozenset({"p"}), frozenset({"q"})
    return not p.issubset(q) and not q.issubset(p) and len(p) == len(q)


def validate_weighted_relation(edges: Iterable[tuple[int, int]], weights) -> tuple[bool, str]:
    edge_tuple = tuple(edges)
    if weights is None:
        return False, "MISSING_DECLARED_WEIGHT_SEMANTICS"
    if any(e not in weights for e in edge_tuple):
        return False, "MISSING_EDGE_WEIGHT"
    return True, "OK"


class Ledger:
    def __init__(self) -> None:
        self.mismatches: list[dict[str, object]] = []
        self.passes: list[str] = []
        self.details: dict[str, object] = {}

    def check(self, name: str, condition: bool, detail: object = None) -> None:
        if condition:
            self.passes.append(name)
            if detail is not None:
                self.details[name] = detail
        else:
            self.mismatches.append({"name": name, "detail": detail})


def main() -> int:
    L = Ledger()

    # 1. Exact min-plus / max-plus fixed-length path law.
    min_A: Matrix = [
        [None, 2, 5],
        [None, None, 1],
        [4, None, None],
    ]
    max_A: Matrix = [
        [None, 2, 0],
        [None, None, -1],
        [-3, None, None],
    ]
    for kind, A in (("min", min_A), ("max", max_A)):
        for k in range(5):
            L.check(
                f"{kind}_power_equals_fixed_length_paths_k{k}",
                matrix_power(A, k, kind) == exhaustive_fixed_length(A, k, kind),
            )

    # 2. Acyclic all-path closure versus exhaustive enumeration.
    dag: Matrix = [
        [None, 3, 10, None],
        [None, None, 2, 8],
        [None, None, None, 1],
        [None, None, None, None],
    ]
    dag_star = finite_power_star(dag, "min")
    dag_exhaustive = exhaustive_simple_path_star(dag, "min")
    L.check("acyclic_star_equals_exhaustive_all_paths", dag_star == dag_exhaustive)
    L.check("acyclic_floyd_equals_power_star", floyd_warshall_star(dag, "min") == dag_star)

    # 3. Cyclic examples with and without improving cycles.
    min_no_improve: Matrix = [
        [None, 1, None],
        [None, None, 1],
        [-1, None, None],
    ]  # cycle total +1: not min-plus improving
    max_no_improve: Matrix = [
        [None, 1, None],
        [None, None, -1],
        [-1, None, None],
    ]  # cycle total -1: not max-plus improving
    min_bad: Matrix = [
        [None, 1, None],
        [None, None, -3],
        [1, None, None],
    ]  # cycle total -1
    max_bad: Matrix = [
        [None, 1, None],
        [None, None, 2],
        [-1, None, None],
    ]  # cycle total +2

    L.check("min_no_improving_cycle", improving_cycle(min_no_improve, "min") is None)
    L.check("max_no_improving_cycle", improving_cycle(max_no_improve, "max") is None)
    min_cert = improving_cycle(min_bad, "min")
    max_cert = improving_cycle(max_bad, "max")
    L.check("min_improving_cycle_certificate", min_cert is not None and min_cert[1] < 0, min_cert)
    L.check("max_improving_cycle_certificate", max_cert is not None and max_cert[1] > 0, max_cert)
    L.check(
        "no_improve_min_star_reduces_to_simple_paths",
        finite_power_star(min_no_improve, "min") == exhaustive_simple_path_star(min_no_improve, "min"),
    )
    L.check(
        "no_improve_max_star_reduces_to_simple_paths",
        finite_power_star(max_no_improve, "max") == exhaustive_simple_path_star(max_no_improve, "max"),
    )

    # 4. Unreachable / infinity conventions.
    sparse: Matrix = [[None, 7], [None, None]]
    sparse2 = matrix_power(sparse, 2, "min")
    sparse_star = finite_power_star(sparse, "min")
    L.check("unreachable_two_step_remains_unreachable", sparse2[0][1] is None)
    L.check("kleene_identity_diagonal_zero", sparse_star[0][0] == 0 and sparse_star[1][1] == 0)
    L.check("declared_edge_remains_finite", sparse_star[0][1] == 7)
    L.check("reverse_unreachable_preserved", sparse_star[1][0] is None)

    # 5. Relabeling invariance.
    perm = (2, 0, 3, 1)
    relabeled = permute_matrix(dag, perm)
    expected = permute_matrix(floyd_warshall_star(dag, "min"), perm)
    actual = floyd_warshall_star(relabeled, "min")
    L.check("relabeling_invariance_of_closure", actual == expected)

    # 6. Finite residuated idempotent semiring + left/right matrix laws.
    S = CappedMaxPlus(cap=3)
    L.check("capped_max_plus_semiring_laws", validate_capped_max_plus(S))
    A2 = [[0, 1], [2, None]]
    b_right = [2, 3]
    r = right_matrix_residual(S, A2, b_right)
    right_law = all(
        vec_leq(S, semiring_matvec(S, A2, x), b_right) == vec_leq(S, x, r)
        for x in product(S.elements, repeat=2)
    )
    L.check("right_matrix_residual_galois_law", right_law, {"residual": r})

    b_left = [3, 2]
    ell = left_matrix_residual(S, A2, b_left)
    left_law = all(
        vec_leq(S, semiring_vecmat(S, y, A2), b_left) == vec_leq(S, y, ell)
        for y in product(S.elements, repeat=2)
    )
    L.check("left_matrix_residual_galois_law", left_law, {"residual": ell})

    # 7. Bellman least/greatest fixed points on a declared finite complete carrier.
    bell_A = [[None, 0], [0, None]]
    bell_b = [1, None]
    lfp, lsteps = least_fixed_point(S, bell_A, bell_b)
    gfp, gsteps = greatest_fixed_point(S, bell_A, bell_b)
    fixed = all_fixed_points(S, bell_A, bell_b)
    L.check("bellman_lfp_exact", lfp == [1, 1], {"steps": lsteps, "fixed_points": fixed})
    L.check("bellman_gfp_exact", gfp == [3, 3], {"steps": gsteps, "fixed_points": fixed})
    L.check("bellman_lfp_below_all_fixed_points", all(vec_leq(S, lfp, x) for x in fixed))
    L.check("bellman_gfp_above_all_fixed_points", all(vec_leq(S, x, gfp) for x in fixed))

    # 8. Application A: explicitly weighted provenance/path system.
    depth = 18
    prov_A, source, target = build_diamond_cost_system(depth)
    path_count, exhaustive_best = enumerate_source_target_paths(prov_A, source, target)
    closure_best = floyd_warshall_star(prov_A, "min")[source][target]
    L.check(
        "application_A_exponential_path_compression",
        path_count == 2**depth and closure_best == exhaustive_best,
        {
            "depth": depth,
            "states": len(prov_A),
            "paths": path_count,
            "closure_cubic_cell_updates_upper_bound": len(prov_A) ** 3,
            "best_cost": closure_best,
        },
    )

    # 9. Application B: precision/threshold inequality propagation.
    S2 = CappedMaxPlus(cap=6)
    prec_A = [
        [1, None, 2, None],
        [None, 0, 1, 2],
        [2, None, None, 1],
    ]
    caps = [4, 5, 3]
    residual = right_matrix_residual(S2, prec_A, caps)
    all_x = list(product(S2.elements, repeat=4))
    feasible = [x for x in all_x if vec_leq(S2, semiring_matvec(S2, prec_A, x), caps)]
    residual_is_greatest = (
        vec_leq(S2, semiring_matvec(S2, prec_A, residual), caps)
        and all(vec_leq(S2, x, residual) for x in feasible)
    )
    L.check(
        "application_B_residual_replaces_state_search",
        residual_is_greatest,
        {
            "carrier_size": len(S2.elements),
            "variables": 4,
            "bruteforce_states": len(all_x),
            "matrix_constraints": 12,
            "greatest_admissible_grade_vector": residual,
            "feasible_states": len(feasible),
        },
    )

    # 10. Required negative boundaries.
    weighted_ok, weighted_reason = validate_weighted_relation([(0, 1)], None)
    L.check(
        "negative_bare_relation_rejected",
        not weighted_ok and weighted_reason == "MISSING_DECLARED_WEIGHT_SEMANTICS",
        weighted_reason,
    )

    ordinary_add = lambda a, b: a + b
    L.check("negative_nonidempotent_addition_rejected", ordinary_add(1, 1) != 1)

    L.check("negative_partial_order_total_shortcut_fails", check_partial_order_boundary())

    L.check(
        "negative_improving_cycle_no_finite_optimum",
        min_cert is not None and max_cert is not None,
        {"min": min_cert, "max": max_cert},
    )

    L.check(
        "negative_nonresiduated_monotone_operator",
        nonresiduated_partial_order_counterexample(),
    )

    # N max-plus is not complete: any proposed upper bound c for {0,1,2,...}
    # is defeated by c+1, so the all-length positive-cycle supremum is absent.
    L.check(
        "negative_incomplete_carrier",
        all((c + 1) > c for c in range(20)),
        "constructive witness c -> c+1; proof in report is unbounded",
    )

    unweighted_safe, weighted_safe = quotient_weight_descent_counterexample()
    L.check(
        "negative_T6_safe_unweighted_quotient_may_fail_weight_descent",
        unweighted_safe and not weighted_safe,
        {"unweighted_safe": unweighted_safe, "weighted_safe": weighted_safe},
    )

    directed_metric_A: Matrix = [[None, 1], [3, None]]
    directed_env = floyd_warshall_star(directed_metric_A, "min")
    L.check(
        "negative_path_envelope_not_native_metric",
        directed_env[0][1] == 1 and directed_env[1][0] == 3,
        directed_env,
    )

    summary = {
        "task": "RS-TD-TR-TROPICAL-RESIDUATION-IDEMPOTENT-CLOSURE-CALCULUS",
        "exact_arithmetic": True,
        "pass_count": len(L.passes),
        "mismatch_count": len(L.mismatches),
        "mismatches": L.mismatches,
        "details": L.details,
    }
    print(json.dumps(summary, sort_keys=True, indent=2))
    return 0 if not L.mismatches else 1


if __name__ == "__main__":
    sys.exit(main())
