#!/usr/bin/env python3
"""Deterministic exact checker for the TD-LP tool-discovery task.

All arithmetic is integer/rational and all enumerations are finite.
Enumeration is regression evidence only; the general laws are proved in the
accompanying research note.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations, product
from math import gcd
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from enterprise_math.discrete_laplacian_chip_firing import (  # noqa: E402
    TopplingSystem,
    UndirectedEdge,
    determinant,
    divergence,
    graph_laplacian,
    incidence_matrix,
    matvec,
    reduced_graph_system,
    weighted_laplacian,
)


MISMATCHES: list[str] = []
CHECKS = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        MISMATCHES.append(f"{name}: {detail}" if detail else name)


def exhaustive_legal_outcomes(system: TopplingSystem, initial: tuple[int, ...]):
    """Return exact terminal (state, odometer) pairs and legal-order count."""
    q = system.strict_termination_witness()
    margin = system.witness_margin(q)
    max_steps = sum(q[i] * initial[i] for i in range(system.size)) // min(margin)

    @lru_cache(None)
    def rec(state: tuple[int, ...]):
        legal = system.legal_sites(state)
        if not legal:
            return frozenset({(state, (0,) * system.size)}), 1
        outcomes = set()
        order_count = 0
        for site in legal:
            child = system.fire(state, site)
            child_outcomes, child_count = rec(child)
            order_count += child_count
            for final, odo in child_outcomes:
                u = list(odo)
                u[site] += 1
                outcomes.add((final, tuple(u)))
        return frozenset(outcomes), order_count

    outcomes, count = rec(tuple(initial))
    check("exhaustive_bound", all(sum(u) <= max_steps for _, u in outcomes))
    return outcomes, count


def raw_apply(delta, initial, u):
    du = matvec(delta, u)
    return tuple(initial[i] - du[i] for i in range(len(initial)))


def bounded_least_action_regression(
    system: TopplingSystem,
    initial: tuple[int, ...],
    odometer: tuple[int, ...],
    pad: int = 2,
) -> None:
    """Compare u against every stabilizing vector in a deterministic small box."""
    diag = tuple(system.delta[i][i] for i in range(system.size))
    for v in product(*(range(odometer[i] + pad + 1) for i in range(system.size))):
        candidate = raw_apply(system.delta, initial, v)
        if all(candidate[i] < diag[i] for i in range(system.size)):
            check(
                "least_action_box",
                all(odometer[i] <= v[i] for i in range(system.size)),
                f"u={odometer}, v={v}, candidate={candidate}",
            )


def minor(matrix, rows, cols):
    return tuple(tuple(matrix[i][j] for j in cols) for i in rows)


def smith_invariants_by_minors(matrix):
    """Exact SNF invariant factors for tiny full-rank matrices via determinantal divisors."""
    n = len(matrix)
    deltas = [1]
    for k in range(1, n + 1):
        g = 0
        for rows in combinations(range(n), k):
            for cols in combinations(range(n), k):
                g = gcd(g, abs(determinant(minor(matrix, rows, cols))))
        deltas.append(g)
    if deltas[-1] == 0:
        raise ValueError("matrix must be full rank")
    return tuple(deltas[k] // deltas[k - 1] for k in range(1, n + 1))


def graph_fixtures():
    return {
        "path": (
            3,
            [UndirectedEdge(0, 1), UndirectedEdge(1, 2)],
            {2},
            (3, 1),
        ),
        "cycle_with_sink": (
            4,
            [
                UndirectedEdge(0, 1),
                UndirectedEdge(1, 2),
                UndirectedEdge(2, 3),
                UndirectedEdge(3, 0),
            ],
            {3},
            (4, 2, 0),
        ),
        "tree": (
            4,
            [
                UndirectedEdge(0, 1),
                UndirectedEdge(0, 2),
                UndirectedEdge(2, 3),
            ],
            {3},
            (4, 1, 0),
        ),
        "multigraph": (
            3,
            [
                UndirectedEdge(0, 1, 1, "parallel-a"),
                UndirectedEdge(0, 1, 1, "parallel-b"),
                UndirectedEdge(0, 2),
                UndirectedEdge(1, 2),
            ],
            {2},
            (6, 1),
        ),
    }


def test_orientation_invariance():
    for name, (n, edges, _sinks, _initial) in graph_fixtures().items():
        baseline = graph_laplacian(n, edges)
        for mask in range(1 << len(edges)):
            rev = [j for j in range(len(edges)) if (mask >> j) & 1]
            candidate = graph_laplacian(n, edges, reverse_columns=rev)
            check(f"orientation_laplacian_{name}", candidate == baseline, f"mask={mask}")

        if edges:
            flow = tuple(j + 1 for j in range(len(edges)))
            b0 = incidence_matrix(n, edges)
            d0 = divergence(b0, flow)
            for j in range(len(edges)):
                b1 = incidence_matrix(n, edges, reverse_columns=[j])
                f1 = list(flow)
                f1[j] *= -1
                check(
                    f"orientation_divergence_{name}",
                    divergence(b1, tuple(f1)) == d0,
                    f"edge={j}",
                )


def test_potential_divergence_identity():
    for name, (n, edges, _sinks, _initial) in graph_fixtures().items():
        b = incidence_matrix(n, edges)
        weights = tuple(edge.weight for edge in edges)
        phi = tuple(i * i - 2 * i + 1 for i in range(n))
        gradient = tuple(
            sum(b[v][e] * phi[v] for v in range(n))
            for e in range(len(edges))
        )
        weighted_flow = tuple(weights[e] * gradient[e] for e in range(len(edges)))
        lhs = divergence(b, weighted_flow)
        rhs = matvec(weighted_laplacian(b, weights), phi)
        check(f"laplacian_div_grad_{name}", lhs == rhs, f"lhs={lhs}, rhs={rhs}")


def test_graph_stabilization_and_least_action():
    for name, (n, edges, sinks, initial) in graph_fixtures().items():
        system, _active, _full = reduced_graph_system(n, edges, sinks)
        result = system.stabilize(initial)
        outcomes, _count = exhaustive_legal_outcomes(system, initial)
        check(
            f"unique_stabilization_{name}",
            outcomes == frozenset({(result.stable_state, result.odometer)}),
            f"outcomes={outcomes}, deterministic={result}",
        )
        check(
            f"odometer_certificate_{name}",
            system.verify_odometer_certificate(initial, result.stable_state, result.odometer),
        )
        bounded_least_action_regression(system, initial, result.odometer)


def test_vertex_relabeling():
    edges = [
        UndirectedEdge(0, 1),
        UndirectedEdge(0, 2),
        UndirectedEdge(1, 3),
        UndirectedEdge(2, 3),
        UndirectedEdge(1, 2),
    ]
    system, _active, _ = reduced_graph_system(4, edges, {3})
    initial = (10, 0, 0)
    base = system.stabilize(initial)

    perm = (2, 0, 1)
    d2 = tuple(tuple(system.delta[perm[i]][perm[j]] for j in range(3)) for i in range(3))
    c2 = tuple(initial[perm[i]] for i in range(3))
    relabeled = TopplingSystem(d2).stabilize(c2)
    check(
        "vertex_relabel_stable",
        relabeled.stable_state == tuple(base.stable_state[perm[i]] for i in range(3)),
    )
    check(
        "vertex_relabel_odometer",
        relabeled.odometer == tuple(base.odometer[perm[i]] for i in range(3)),
    )


def test_conservation_and_sink_loss():
    for name, (n, edges, sinks, _initial) in graph_fixtures().items():
        full = graph_laplacian(n, edges)
        active = tuple(i for i in range(n) if i not in sinks)
        for site in active:
            degree = full[site][site]
            state = [0] * n
            state[site] = degree
            after = tuple(state[row] - full[row][site] for row in range(n))
            check(f"full_conservation_{name}", sum(after) == sum(state), f"site={site}")
            sink_gain = sum(after[s] - state[s] for s in sinks)
            active_loss = sum(state[i] for i in active) - sum(after[i] for i in active)
            check(
                f"sink_loss_{name}",
                active_loss == sink_gain,
                f"site={site}, loss={active_loss}, gain={sink_gain}",
            )


def test_reduced_laplacian_and_cokernel():
    c3_edges = [UndirectedEdge(0, 1), UndirectedEdge(1, 2), UndirectedEdge(2, 0)]
    c3, _, _ = reduced_graph_system(3, c3_edges, {2})
    check("c3_reduced_laplacian", c3.delta == ((2, -1), (-1, 2)))
    check("c3_det", c3.cokernel_order() == 3)
    check("c3_snf", smith_invariants_by_minors(c3.delta) == (1, 3))

    mg_edges = [
        UndirectedEdge(0, 1),
        UndirectedEdge(0, 1),
        UndirectedEdge(0, 2),
        UndirectedEdge(1, 2),
    ]
    mg, _, _ = reduced_graph_system(3, mg_edges, {2})
    check("multigraph_reduced_laplacian", mg.delta == ((3, -2), (-2, 3)))
    check("multigraph_det", mg.cokernel_order() == 5)
    check("multigraph_snf", smith_invariants_by_minors(mg.delta) == (1, 5))

    left = (0, 0)
    right = (1, 1)
    check("cokernel_same_class", c3.same_firing_lattice_class(left, right))
    check("cokernel_both_stable", c3.stable(left) and c3.stable(right))
    check("cokernel_not_normal_form", left != right)


def test_sinkless_and_directed_boundaries():
    try:
        TopplingSystem(())
    except ValueError:
        pass
    else:
        check("no_declared_carrier_rejected", False)

    sinkless = TopplingSystem(((1, -1), (-1, 1)))
    c0 = (1, 0)
    c1 = sinkless.fire(c0, 0)
    c2 = sinkless.fire(c1, 1)
    check("sinkless_period_step1", c1 == (0, 1))
    check("sinkless_period_step2", c2 == c0)
    try:
        sinkless.strict_termination_witness()
    except ValueError:
        pass
    else:
        check("sinkless_no_strict_witness", False, "singular sinkless system returned witness")

    directed_ab = TopplingSystem(((2, 0), (-1, 1)))
    directed_ba = TopplingSystem(((1, -1), (0, 2)))
    ra = directed_ab.stabilize((2, 0))
    rb = directed_ba.stabilize((2, 0))
    check("directed_semantic_orientation_changes_odo", ra.odometer != rb.odometer)
    check("directed_semantic_orientation_changes_path", ra.odometer == (1, 1) and rb.odometer == (2, 0))

    inaccessible = TopplingSystem(((1, -1), (-1, 1)))
    x1 = inaccessible.fire((1, 0), 0)
    x2 = inaccessible.fire(x1, 1)
    check("inaccessible_sink_period", x2 == (1, 0))

    try:
        TopplingSystem(((-1,),))
    except ValueError:
        pass
    else:
        check("negative_weight_rejected", False)


def test_application_a_incidence_provenance():
    edges = [
        UndirectedEdge(0, 1, type_label="route-A"),
        UndirectedEdge(0, 2, type_label="route-B"),
        UndirectedEdge(1, 3, type_label="to-sink"),
        UndirectedEdge(2, 3, type_label="to-sink"),
        UndirectedEdge(1, 2, type_label="cross-check"),
    ]
    system, _, _ = reduced_graph_system(4, edges, {3})
    initial = (10, 0, 0)
    result = system.stabilize(initial)
    outcomes, count = exhaustive_legal_outcomes(system, initial)
    check("appA_stable", result.stable_state == (0, 2, 2))
    check("appA_odometer", result.odometer == (8, 3, 3))
    check("appA_all_orders", outcomes == frozenset({((0, 2, 2), (8, 3, 3))}))
    check("appA_order_count", count == 144, f"count={count}")
    check(
        "appA_potential_equation",
        raw_apply(system.delta, initial, result.odometer) == result.stable_state,
    )
    check(
        "appA_compact_cert",
        system.verify_odometer_certificate(initial, result.stable_state, result.odometer),
    )
    bounded_least_action_regression(system, initial, result.odometer)


def test_application_b_precision_carry():
    delta = (
        (2, 0, 0),
        (-1, 3, 0),
        (0, -1, 2),
    )
    system = TopplingSystem(delta, ("fine", "middle", "coarse"))
    initial = (5, 8, 3)
    result = system.stabilize(initial)
    outcomes, count = exhaustive_legal_outcomes(system, initial)
    check("appB_nonsymmetric", delta != tuple(zip(*delta)))
    check("appB_stable", result.stable_state == (1, 1, 0))
    check("appB_odometer", result.odometer == (2, 3, 3))
    check("appB_all_orders", outcomes == frozenset({((1, 1, 0), (2, 3, 3))}))
    check("appB_order_count", count == 209, f"count={count}")
    check(
        "appB_compact_cert",
        system.verify_odometer_certificate(initial, result.stable_state, result.odometer),
    )
    bounded_least_action_regression(system, initial, result.odometer)

    place_value = (1, 2, 6)
    top_sink_value = 12
    initial_value = sum(place_value[i] * initial[i] for i in range(3))
    final_value = sum(place_value[i] * result.stable_state[i] for i in range(3))
    sink_value = top_sink_value * result.odometer[2]
    check("appB_value_conservation", initial_value == final_value + sink_value)
    check("appB_value_39", initial_value == 39 and final_value == 3 and sink_value == 36)

    q = (1, 1, 1)
    margin = system.witness_margin(q)
    check("appB_termination_witness", margin == (1, 2, 2))


def main() -> int:
    test_orientation_invariance()
    test_potential_divergence_identity()
    test_graph_stabilization_and_least_action()
    test_vertex_relabeling()
    test_conservation_and_sink_loss()
    test_reduced_laplacian_and_cokernel()
    test_sinkless_and_directed_boundaries()
    test_application_a_incidence_provenance()
    test_application_b_precision_carry()

    print(f"CHECKS={CHECKS}")
    print(f"MISMATCHES={len(MISMATCHES)}")
    for mismatch in MISMATCHES:
        print(f"MISMATCH: {mismatch}")
    print("FINAL=PASS" if not MISMATCHES else "FINAL=FAIL")
    return 0 if not MISMATCHES else 1


if __name__ == "__main__":
    raise SystemExit(main())
