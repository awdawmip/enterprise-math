"""Frustration lower bound for the free tail of symmetric Walsh precision.

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
      =1/2 (|1+b(A)|+|1+b(B)|+|b(A)+b(B)|).

For arbitrary real b(A),b(B),

    T(A,B) >= 1.

Indeed

    |1+x|+|1+y| >= |2+x+y|

and

    |2+x+y|+|x+y| >= 2.

Thus the triangle cannot be made coefficient-free.  Killing both pure roots
forces x=y=-1 and leaves unit mixed cost; killing the mixed root forces x=-y
and leaves at least unit pure-root cost; intermediate values only redistribute
the same irreducible frustration.

Consequently symmetric tail compilation is an antiferromagnetic/signed-graph
optimization, not independent deletion of free coefficients.  The C_k^2 result
identifies the individually forced core; the present theorem identifies a
second, relational source of unavoidable complexity in the nominally free tail.

This is a coefficient-complexity lower bound.  It is not a prime-count theorem
and it does not assert that every abstract triangle corresponds to an occupied
physical radius.
"""

from __future__ import annotations


def symmetric_edge_cost(left_b: float, right_b: float) -> float:
    """Return 1/2 |b(A)+b(B)| for one normalized symmetric root edge."""
    return 0.5 * abs(float(left_b) + float(right_b))


def empty_high_high_triangle_cost(left_b: float, right_b: float) -> dict[str, float | bool]:
    """Return the exact three-edge frustration cost and certify the unit lower bound."""
    pure_left = symmetric_edge_cost(1.0, left_b)
    pure_right = symmetric_edge_cost(1.0, right_b)
    mixed = symmetric_edge_cost(left_b, right_b)
    total = pure_left + pure_right + mixed
    if total < 1.0 - 1e-12:
        raise AssertionError("symmetric Walsh triangle violated the unit frustration lower bound")
    return {
        "left_b": float(left_b),
        "right_b": float(right_b),
        "pure_left_cost": pure_left,
        "pure_right_cost": pure_right,
        "mixed_cost": mixed,
        "triangle_l1_cost": total,
        "unit_frustration_lower_bound": True,
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
