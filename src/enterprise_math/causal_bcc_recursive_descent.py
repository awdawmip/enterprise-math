"""Exact integer BCC ball and directional-boundary descent to A2.

Use the scaled BCC nearest-neighbor generators {(+/-1,+/-1,+/-1)}.  Reachable
vertices are triples whose coordinates have common parity.  The graph distance
from zero is max_i |x_i|, so the radius-r ball contains the common-parity points
in [-r,r]^3 and has

    V_BCC(r)=r^3+(r+1)^3.

For the +++ primitive direction, a state exits the ball exactly when at least one
coordinate equals +r.  All boundary coordinates have parity r, so

    y_i=(r-x_i)/2

bijects the directional boundary with triples in [0,r]^3 having at least one zero
coordinate.  Therefore

    |D_+++(r)|=(r+1)^3-r^3=3r^2+3r+1,

which is exactly the A2 graph-ball count.

BCC therefore passes recursive descent to the triangular A2 candidate while its
primitive-direction link is edgeless.  Recursive descent and local relation-link
connectedness are independent selection axes.
"""

from __future__ import annotations

from itertools import product

from .lattice_geometry import a_ball_count

Vector3 = tuple[int, int, int]


def bcc_primitive_directions() -> tuple[Vector3, ...]:
    return tuple(product((-1, 1), repeat=3))


def bcc_first_direction_link_edge_count() -> int:
    directions = set(bcc_primitive_directions())
    count = 0
    ordered = tuple(directions)
    for index, left in enumerate(ordered):
        for right in ordered[index + 1 :]:
            difference = tuple(right[i] - left[i] for i in range(3))
            if difference in directions:
                count += 1
    return count


def bcc_ball_count(radius: int) -> int:
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    r = radius
    return r**3 + (r + 1) ** 3


def bcc_directional_boundary_count(radius: int) -> int:
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    r = radius
    return (r + 1) ** 3 - r**3


def bcc_boundary_equals_a2_ball(radius: int) -> bool:
    return bcc_directional_boundary_count(radius) == a_ball_count(2, radius)


def bcc_boundary_to_a2_coordinates(x: Vector3, radius: int) -> Vector3:
    """Map +++ directional boundary point to nonnegative triple with one zero.

    Nonnegative triples summing only indirectly encode the usual A2 ball; the
    cardinality identity is the primary descent statement here.  The returned
    triple lies in [0,r]^3 and has minimum coordinate zero.
    """
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in x
    ):
        raise ValueError("x must be an integer triple")
    if any(abs(value) > radius for value in x):
        raise ValueError("x must lie in the BCC radius-r cube")
    if not (x[0] % 2 == x[1] % 2 == x[2] % 2 == radius % 2):
        raise ValueError("boundary point coordinates must share the radius parity")
    if max(x) != radius:
        raise ValueError("x must lie on the +++ outgoing directional boundary")
    y = tuple((radius - value) // 2 for value in x)
    if min(y) != 0 or any(not (0 <= value <= radius) for value in y):
        raise AssertionError("BCC boundary coordinate map failed")
    return y


def bcc_directional_boundary_count_bruteforce(radius: int) -> int:
    directions = bcc_primitive_directions()
    alpha = (1, 1, 1)
    points = []
    for x in product(range(-radius, radius + 1), repeat=3):
        if not (x[0] % 2 == x[1] % 2 == x[2] % 2):
            continue
        # Common parity plus max norm <=r characterizes the BCC graph ball.
        if max(abs(value) for value in x) > radius:
            continue
        points.append(x)
    point_set = set(points)
    return sum(
        tuple(x[i] + alpha[i] for i in range(3)) not in point_set
        for x in points
    )
