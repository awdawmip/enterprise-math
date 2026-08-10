"""Derive the A_p Voronoi cell from primitive conservative unit responses.

Let A_(N-1)={v in Z^N: sum v_i=0}.  Primitive moves are unit transfers
e_i-e_j and the derived anonymous quadratic shadow is Q(v)=sum v_i^2.

The primitive response cell in the real zero-sum shadow space is

    C={x: x_i-x_j <= 1 for all i,j}.

For any lattice displacement v, let m=sum_{v_i>0} v_i be its minimum unit-transfer
mass.  Primitive response constraints imply <x,v><=m.  Since integer squares
satisfy Q(v)>=sum |v_i|=2m, every full Voronoi inequality

    2<x,v> <= Q(v)

is already implied by primitive unit-transfer constraints.  Conversely every
primitive root is a lattice displacement of Q=2, so the primitive constraints are
Voronoi constraints.  Hence C is exactly the Voronoi cell of A_(N-1) for the
derived quadratic shadow.

Its vertices are the centered two-level probes 1_S-(|S|/N)1 for every nonempty
proper subset S of the N anonymous slots, giving 2^N-2 vertices.  In rank three
this is the rhombic dodecahedral FCC/Wigner-Seitz shadow.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations

Vector = tuple[int, ...]
RationalVector = tuple[Fraction, ...]


def a_transfer_mass(displacement: Vector) -> int:
    if not displacement or any(isinstance(value, bool) or not isinstance(value, int) for value in displacement):
        raise ValueError("displacement must be a non-empty integer tuple")
    if sum(displacement) != 0:
        raise ValueError("A relation displacement must have zero total")
    return sum(value for value in displacement if value > 0)


def a_quadratic_grade(displacement: Vector) -> int:
    return sum(value * value for value in displacement)


def quadratic_dominates_twice_transfer_mass(displacement: Vector) -> bool:
    return a_quadratic_grade(displacement) >= 2 * a_transfer_mass(displacement)


def probe_is_primitive_unit_bounded(probe: RationalVector) -> bool:
    if not probe:
        raise ValueError("probe must be non-empty")
    return max(probe) - min(probe) <= 1


def probe_pairing(probe: RationalVector, displacement: Vector) -> Fraction:
    if len(probe) != len(displacement):
        raise ValueError("probe and displacement must have the same slot count")
    return sum(value * coordinate for value, coordinate in zip(displacement, probe))


def primitive_response_implies_voronoi_inequality(
    probe: RationalVector,
    displacement: Vector,
) -> bool:
    if not probe_is_primitive_unit_bounded(probe):
        raise ValueError("probe must satisfy all primitive unit-transfer response constraints")
    mass = a_transfer_mass(displacement)
    pairing = probe_pairing(probe, displacement)
    if pairing > mass:
        return False
    return 2 * pairing <= a_quadratic_grade(displacement)


def centered_subset_probe(slot_count: int, subset: tuple[int, ...]) -> RationalVector:
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 2:
        raise ValueError("slot_count must be at least two")
    chosen = set(subset)
    if not chosen or len(chosen) == slot_count or any(index < 0 or index >= slot_count for index in chosen):
        raise ValueError("subset must be nonempty, proper, and inside slot range")
    mean = Fraction(len(chosen), slot_count)
    return tuple(Fraction(1 if index in chosen else 0) - mean for index in range(slot_count))


def a_voronoi_response_vertices(slot_count: int) -> tuple[RationalVector, ...]:
    vertices = []
    for size in range(1, slot_count):
        for subset in combinations(range(slot_count), size):
            vertices.append(centered_subset_probe(slot_count, subset))
    return tuple(vertices)


def a_voronoi_vertex_count(slot_count: int) -> int:
    if slot_count < 2:
        raise ValueError("slot_count must be at least two")
    return 2 ** slot_count - 2


def probe_has_zero_gauge(probe: RationalVector) -> bool:
    return sum(probe) == 0


def all_declared_vertices_are_primitive_unit_bounded(slot_count: int) -> bool:
    vertices = a_voronoi_response_vertices(slot_count)
    return (
        len(vertices) == a_voronoi_vertex_count(slot_count)
        and all(probe_has_zero_gauge(vertex) for vertex in vertices)
        and all(probe_is_primitive_unit_bounded(vertex) for vertex in vertices)
    )


def a3_voronoi_vertex_partition() -> dict[int, int]:
    """Rank-3 / four-slot vertices by subset size: 4 + 6 + 4 = 14."""
    return {size: len(tuple(combinations(range(4), size))) for size in range(1, 4)}
