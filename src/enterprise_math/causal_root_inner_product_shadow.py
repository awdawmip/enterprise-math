"""Traditional simply-laced root inner products as a causal-link shadow.

For an antipodally closed equal-norm primitive direction family R, suppose every
pair obeys the simply-laced A/D/E relation pattern.  The primitive causal graph
records alpha~beta exactly when beta-alpha is again primitive.  Together with the
antipodal involution beta->-beta, this is enough to reconstruct the normalized
pair inner-product class without using angles as primitive data:

* alpha=beta             ->  +2 units;
* alpha=-beta            ->  -2 units;
* alpha~beta             ->  +1 unit;
* alpha~(-beta)          ->  -1 unit;
* otherwise              ->   0.

Here one unit means half the common primitive squared norm.  Thus, for A/D/E
root systems, the familiar inner-product values are an exact rendering of the
primitive relation graph.  The reconstruction is a theorem only when the
simply-laced pattern is verified; it is not asserted for arbitrary minimal-vector
sets such as laminated lattices.
"""

from __future__ import annotations

from .causal_primitive_link_profile import Adjacency, Vector, primitive_direction_graph


def negate(vector: Vector) -> Vector:
    return tuple(-value for value in vector)


def causal_inner_product_class(
    adjacency: Adjacency,
    left: Vector,
    right: Vector,
) -> int:
    """Return twice the inner product divided by the common primitive norm.

    Values are in {-2,-1,0,1,2}.  The function uses only equality, antipodes,
    and primitive-link adjacency.
    """
    if left not in adjacency or right not in adjacency:
        raise ValueError("directions must belong to the primitive graph")
    if left == right:
        return 2
    if left == negate(right):
        return -2
    if right in adjacency[left]:
        return 1
    antipode = negate(right)
    if antipode not in adjacency:
        raise ValueError("primitive direction family must be antipodally closed")
    if antipode in adjacency[left]:
        return -1
    return 0


def actual_scaled_inner_product_class(left: Vector, right: Vector) -> int:
    """Coordinate audit: 2<left,right>/<left,left>, requiring equal nonzero norm."""
    left_norm = sum(value * value for value in left)
    right_norm = sum(value * value for value in right)
    if left_norm == 0 or left_norm != right_norm:
        raise ValueError("primitive directions must have one common nonzero squared norm")
    numerator = 2 * sum(a * b for a, b in zip(left, right))
    if numerator % left_norm != 0:
        raise ValueError("pair is not in the simply-laced integral inner-product regime")
    return numerator // left_norm


def causal_reconstruction_matches_coordinates(roots: tuple[Vector, ...]) -> bool:
    adjacency = primitive_direction_graph(roots)
    if any(negate(root) not in adjacency for root in roots):
        return False
    return all(
        causal_inner_product_class(adjacency, left, right)
        == actual_scaled_inner_product_class(left, right)
        for left in roots
        for right in roots
    )
