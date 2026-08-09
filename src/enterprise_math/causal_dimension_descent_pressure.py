"""Recursive directional-boundary descent across candidate minimum-precision lattices.

For a Cayley-ball B_d(r) and primitive direction alpha, define the outgoing
directional section

    D_alpha(r)={x in B_d(r): x+alpha not in B_d(r)}.

Two families have exact same-family descent:

- standard-axis Z^d with L1 balls: D_(+e1)(r) is bijective with the entire
  Z^(d-1) L1 ball by deleting x1 and reconstructing x1=r-||y||_1;
- A_p root lattices: D_(e0-e1)(r) is bijective with the entire A_(p-1) ball by
  merging the two distinguished coordinates, with an explicit inverse.

The D-family already fails this closure at D4.  For alpha=e1+e2, exact integer
counting gives

    |D_alpha^D4(r)|=(2r+1)(2r^2+2r+1),

whereas the D3=A3 ball has

    |B_D3(r)|=(2r+1)(5r^2+5r+3)/3.

Their difference is r(r+1)(2r+1)/3>0 for r>0.

The exceptional E8 root graph also fails the natural E8->E7 radius-one test:
for a fixed E8 root alpha, 183 of the 240 root states in B1 exit under +alpha,
while the orthogonal E7 root subsystem has 126 roots and hence radius-one root
ball size 127.

Recursive descent is therefore a useful independent pressure-test axis, but not
a standalone selector: Z^d passes it while failing primitive-direction-link
connectedness.
"""

from __future__ import annotations

from itertools import product
from math import comb

from .causal_e8_direction_link import e8_scaled_roots
from .lattice_geometry import a_ball_count


def z_l1_ball_count(dimension: int, radius: int) -> int:
    if isinstance(dimension, bool) or not isinstance(dimension, int) or dimension < 0:
        raise ValueError("dimension must be a non-negative integer")
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    return sum(
        (2 ** active) * comb(dimension, active) * comb(radius, active)
        for active in range(0, min(dimension, radius) + 1)
    )


def z_directional_boundary_count(dimension: int, radius: int) -> int:
    if dimension < 1:
        raise ValueError("dimension must be at least one")
    return z_l1_ball_count(dimension - 1, radius)


def z_directional_boundary_bijection(
    y: tuple[int, ...],
    radius: int,
) -> tuple[int, ...]:
    """Lift y in the Z^(d-1) L1 ball to the +e1 boundary of the Z^d ball."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be non-negative")
    norm = sum(abs(value) for value in y)
    if norm > radius:
        raise ValueError("y must lie in the lower-dimensional L1 ball")
    return (radius - norm,) + y


def a_directional_boundary_count(p: int, radius: int) -> int:
    if isinstance(p, bool) or not isinstance(p, int) or p < 1:
        raise ValueError("p must be positive")
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be non-negative")
    if p == 1:
        return 1
    return a_ball_count(p - 1, radius)


def a_directional_boundary_lift(
    y: tuple[int, ...],
    radius: int,
) -> tuple[int, ...]:
    """Lift y in A_(p-1) ball to the +e0-e1 boundary of A_p.

    `y` has p integer coordinates summing to zero.  Split its first coordinate
    y0 into x0+x1, choosing x0 so that the positive-coordinate sum of x is
    exactly radius, with x0>=0 and x1<=0.
    """
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be non-negative")
    if len(y) < 1 or sum(y) != 0:
        raise ValueError("y must be a zero-sum A_(p-1) coordinate vector")
    positive_rest = sum(value for value in y[1:] if value > 0)
    positive_y = sum(value for value in y if value > 0)
    if positive_y > radius:
        raise ValueError("y must lie in the A_(p-1) ball of the supplied radius")
    x0 = radius - positive_rest
    x1 = y[0] - x0
    x = (x0, x1) + y[1:]
    if sum(x) != 0 or x0 < 0 or x1 > 0:
        raise AssertionError("A_p directional-boundary lift conditions failed")
    if sum(value for value in x if value > 0) != radius:
        raise AssertionError("lift must lie on the outgoing directional section")
    return x


def a_directional_boundary_project(x: tuple[int, ...]) -> tuple[int, ...]:
    if len(x) < 2 or sum(x) != 0:
        raise ValueError("x must be an A_p zero-sum vector")
    if x[0] < 0 or x[1] > 0:
        raise ValueError("x must lie in the +e0-e1 directional boundary sector")
    return (x[0] + x[1],) + x[2:]


def d4_l1_face_boundary_count(radius: int) -> int:
    """Boundary part with x1,x2>=0 and ||x||_1=2r."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be non-negative")
    r = radius
    return (8 * r**3 + 6 * r**2 + 4 * r + 3) // 3


def d4_coordinate_cap_boundary_count(radius: int) -> int:
    """Extra part x1=r or x2=r with ||x||_1<2r, disjoint from the L1 face part."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be non-negative")
    r = radius
    return 2 * r * (r - 1) * (2 * r - 1) // 3


def d4_directional_boundary_count(radius: int) -> int:
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be non-negative")
    r = radius
    direct = (2 * r + 1) * (2 * r**2 + 2 * r + 1)
    split = d4_l1_face_boundary_count(r) + d4_coordinate_cap_boundary_count(r)
    if direct != split:
        raise AssertionError("D4 boundary decomposition must equal closed formula")
    return direct


def d3_a3_ball_count(radius: int) -> int:
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be non-negative")
    r = radius
    return (2 * r + 1) * (5 * r**2 + 5 * r + 3) // 3


def d4_same_family_descent_defect(radius: int) -> int:
    """Positive cardinality defect against the natural D4->D3 candidate."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be non-negative")
    r = radius
    defect = d4_directional_boundary_count(r) - d3_a3_ball_count(r)
    expected = r * (r + 1) * (2 * r + 1) // 3
    if defect != expected:
        raise AssertionError("D4 descent defect closed form failed")
    return defect


def _d4_ball_contains(x: tuple[int, int, int, int], radius: int) -> bool:
    return (
        sum(x) % 2 == 0
        and max(abs(value) for value in x) <= radius
        and sum(abs(value) for value in x) <= 2 * radius
    )


def d4_directional_boundary_count_bruteforce(radius: int) -> int:
    if radius < 0:
        raise ValueError("radius must be non-negative")
    alpha = (1, 1, 0, 0)
    count = 0
    for x in product(range(-radius, radius + 1), repeat=4):
        if not _d4_ball_contains(x, radius):
            continue
        y = tuple(x[index] + alpha[index] for index in range(4))
        if not _d4_ball_contains(y, radius):
            count += 1
    return count


def _dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(a * b for a, b in zip(left, right))


def e8_fixed_direction_boundary_radius_one() -> int:
    roots = e8_scaled_roots()
    root_set = set(roots)
    zero = (0,) * 8
    alpha = roots[0]
    boundary = 0
    for x in (zero,) + roots:
        y = tuple(x[index] + alpha[index] for index in range(8))
        if y != zero and y not in root_set:
            boundary += 1
    return boundary


def e7_orthogonal_root_count_inside_e8() -> int:
    roots = e8_scaled_roots()
    alpha = roots[0]
    return sum(1 for root in roots if _dot(alpha, root) == 0)


def e7_root_ball_radius_one_inside_e8() -> int:
    return 1 + e7_orthogonal_root_count_inside_e8()


def e8_to_e7_radius_one_descent_defect() -> int:
    return e8_fixed_direction_boundary_radius_one() - e7_root_ball_radius_one_inside_e8()
