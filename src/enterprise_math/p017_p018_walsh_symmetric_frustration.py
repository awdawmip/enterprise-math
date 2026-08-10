"""Odd-cycle frustration lower bounds for symmetric Walsh precision.

The symmetric forced-core theorem shows that an individual root pattern above
the product horizon C_k^2 is not forced by reusable-floor precision.  It does
*not* follow that every such tail coefficient can be removed simultaneously.
Mixed-orientation interactions create an exact signed-graph obstruction.

Write

    b(S)=(-1)^|S| alpha(S),

so the normalized symmetric coefficient attached to two disjoint selected
supports A,B is, up to an irrelevant global sign,

    c(A,B)=1/2 [b(A)+b(B)].

The empty support is normalized by b(empty)=1.  If two free high-product
supports A,B are disjoint and all three root relations

    empty--A, empty--B, A--B

are retained in the declared boundary language, then their total coefficient
L1 cost is

    T(A,B)
      =1/2 (|1+b(A)|+|1+b(B)|+|b(A)+b(B)|) >= 1.

This is the shortest instance of a general odd-cycle law.  For an odd cycle

    v_0,v_1,...,v_(2m),v_0

with real vertex values b_i, put e_i=b_i+b_(i+1).  Alternating around the odd
cycle gives the exact telescoping identity

    sum_(i=0)^(2m) (-1)^i e_i = 2 b_0.

Therefore

    1/2 sum_i |b_i+b_(i+1)| >= |b_0|.

If the cycle contains a reusable-floor vertex, its b-value is forced to +/-1,
so that cycle carries at least one unit of irreducible symmetric root-pattern L1
cost.  Edge-disjoint packings of such cycles give additive lower bounds.

Thus symmetric tail compilation is an antiferromagnetic/signed-graph problem.
The C_k^2 theorem identifies individually forced coefficients; odd-cycle
frustration identifies relationally forced complexity that survives even in the
nominally free tail.  Components whose constraints are compatible with a
bipartite alternating assignment are the natural places where tail coefficients
can potentially be removed without this obstruction.

This is a coefficient-complexity theorem, not a prime-count theorem.  It does
not assert that every abstract graph edge or cycle is occupied by a physical
radius; the graph is task-relative to the declared boundary/root language.
"""

from __future__ import annotations


def symmetric_edge_cost(left_b: float, right_b: float) -> float:
    """Return 1/2 |b(A)+b(B)| for one normalized symmetric root edge."""
    return 0.5 * abs(float(left_b) + float(right_b))


def odd_cycle_frustration(values: tuple[float, ...], anchored_index: int = 0) -> dict[str, object]:
    """Certify the exact alternating telescoping identity on an odd cycle."""
    if len(values) < 3 or len(values) % 2 == 0:
        raise ValueError("values must describe an odd cycle of length at least three")
    if not (0 <= anchored_index < len(values)):
        raise ValueError("anchored_index is out of range")
    # Rotate so the declared anchored vertex is v_0.
    rotated = tuple(float(values[(anchored_index + i) % len(values)]) for i in range(len(values)))
    edge_sums = tuple(
        rotated[i] + rotated[(i + 1) % len(rotated)]
        for i in range(len(rotated))
    )
    alternating = sum(((-1) ** i) * edge_sums[i] for i in range(len(edge_sums)))
    expected = 2.0 * rotated[0]
    if abs(alternating - expected) > 1e-10:
        raise AssertionError("odd-cycle alternating sum failed to telescope")
    l1_cost = 0.5 * sum(abs(value) for value in edge_sums)
    lower = abs(rotated[0])
    if l1_cost + 1e-12 < lower:
        raise AssertionError("odd-cycle frustration cost fell below anchored magnitude")
    return {
        "cycle_length": len(rotated),
        "anchored_value": rotated[0],
        "edge_sums": edge_sums,
        "alternating_edge_sum": alternating,
        "expected_alternating_sum": expected,
        "normalized_cycle_l1_cost": l1_cost,
        "anchored_frustration_lower_bound": lower,
        "odd_cycle_frustration_identity": True,
    }


def empty_high_high_triangle_cost(left_b: float, right_b: float) -> dict[str, float | bool]:
    """Return the exact three-edge frustration cost and certify the unit lower bound."""
    cycle = odd_cycle_frustration((1.0, float(left_b), float(right_b)))
    pure_left = symmetric_edge_cost(1.0, left_b)
    pure_right = symmetric_edge_cost(1.0, right_b)
    mixed = symmetric_edge_cost(left_b, right_b)
    total = pure_left + pure_right + mixed
    if abs(total - float(cycle["normalized_cycle_l1_cost"])) > 1e-12:
        raise AssertionError("triangle cost disagreed with odd-cycle compiler")
    return {
        "left_b": float(left_b),
        "right_b": float(right_b),
        "pure_left_cost": pure_left,
        "pure_right_cost": pure_right,
        "mixed_cost": mixed,
        "triangle_l1_cost": total,
        "unit_frustration_lower_bound": total >= 1.0 - 1e-12,
    }


def canonical_triangle_tradeoffs() -> tuple[dict[str, float | bool], ...]:
    """Expose the three canonical ways to distribute the irreducible unit cost."""
    rows = (
        empty_high_high_triangle_cost(-1.0, -1.0),
        empty_high_high_triangle_cost(-1.0, 1.0),
        empty_high_high_triangle_cost(0.0, 0.0),
    )
    for row in rows:
        if abs(float(row["triangle_l1_cost"]) - 1.0) > 1e-12:
            raise AssertionError("canonical triangle tradeoff failed to saturate the lower bound")
    return rows
