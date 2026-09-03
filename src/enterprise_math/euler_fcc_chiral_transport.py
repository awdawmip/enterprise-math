"""Exact FCC chirality-transport obstruction and repair calculus.

The four local Euler/Cell slices are the vertices of a tetrahedral adjacency
graph. Six overlap signs form an F2 edge connection. Independent flips of
the four local chiral frames act by vertex coboundaries. This module computes
the complete gauge-invariant curvature, flat reconstruction, minimum repair,
and the induced conjugation monodromy on Euler phase and signed winding.

Only exact integer/Boolean arithmetic is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Iterable, Iterator, Sequence

VertexBits = tuple[int, int, int, int]
EdgeBits = tuple[int, int, int, int, int, int]
FaceBits = tuple[int, int, int, int]
RootDefect = tuple[int, int, int]

VERTICES = (0, 1, 2, 3)
EDGES: tuple[tuple[int, int], ...] = (
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 2),
    (1, 3),
    (2, 3),
)
FACES: tuple[tuple[int, int, int], ...] = (
    (0, 1, 2),
    (0, 1, 3),
    (0, 2, 3),
    (1, 2, 3),
)
EDGE_INDEX = {edge: index for index, edge in enumerate(EDGES)}
OPPOSITE_EDGE_PAIRS: tuple[tuple[int, int], ...] = ((0, 5), (1, 4), (2, 3))


def _bit(value: int | bool) -> int:
    if value in (0, False):
        return 0
    if value in (1, True):
        return 1
    raise ValueError(f"expected an F2 bit, got {value!r}")


def _bits(values: Iterable[int | bool], length: int) -> tuple[int, ...]:
    result = tuple(_bit(value) for value in values)
    if len(result) != length:
        raise ValueError(f"expected {length} bits, got {len(result)}")
    return result


def as_vertex_bits(values: Iterable[int | bool]) -> VertexBits:
    return _bits(values, 4)  # type: ignore[return-value]


def as_edge_bits(values: Iterable[int | bool]) -> EdgeBits:
    return _bits(values, 6)  # type: ignore[return-value]


def as_face_bits(values: Iterable[int | bool]) -> FaceBits:
    return _bits(values, 4)  # type: ignore[return-value]


def xor_bits(left: Sequence[int], right: Sequence[int]) -> tuple[int, ...]:
    if len(left) != len(right):
        raise ValueError("bit vectors must have equal length")
    return tuple(a ^ b for a, b in zip(left, right))


def edge_coboundary(vertex_bits: VertexBits) -> EdgeBits:
    """Relative local-frame flips on the six slice overlaps."""

    g = as_vertex_bits(vertex_bits)
    return tuple(g[u] ^ g[v] for u, v in EDGES)  # type: ignore[return-value]


def gauge_transform(connection: EdgeBits, vertex_bits: VertexBits) -> EdgeBits:
    return xor_bits(as_edge_bits(connection), edge_coboundary(vertex_bits))  # type: ignore[return-value]


def face_holonomy(connection: EdgeBits) -> FaceBits:
    """Triangle chirality monodromy on the four tetrahedral faces."""

    e = as_edge_bits(connection)
    e01, e02, e03, e12, e13, e23 = e
    return (
        e01 ^ e02 ^ e12,
        e01 ^ e03 ^ e13,
        e02 ^ e03 ^ e23,
        e12 ^ e13 ^ e23,
    )


def root_defect(connection: EdgeBits) -> RootDefect:
    h = face_holonomy(connection)
    return h[0], h[1], h[2]


def is_even_face_pattern(pattern: FaceBits) -> bool:
    h = as_face_bits(pattern)
    return (h[0] ^ h[1] ^ h[2] ^ h[3]) == 0


def is_flat(connection: EdgeBits) -> bool:
    return face_holonomy(connection) == (0, 0, 0, 0)


def all_faces_frustrated(connection: EdgeBits) -> bool:
    return face_holonomy(connection) == (1, 1, 1, 1)


def tree_flat_connection(e01: int | bool, e02: int | bool, e03: int | bool) -> EdgeBits:
    """Unique flat extension of the rooted spanning-tree edge signs."""

    a, b, c = _bit(e01), _bit(e02), _bit(e03)
    return a, b, c, a ^ b, a ^ c, b ^ c


def flat_part(connection: EdgeBits) -> EdgeBits:
    e = as_edge_bits(connection)
    return tree_flat_connection(e[0], e[1], e[2])


def root_gauge_normal_form(connection: EdgeBits) -> EdgeBits:
    """Unique representative supported on the three non-tree chords."""

    return xor_bits(as_edge_bits(connection), flat_part(connection))  # type: ignore[return-value]


def potential_for_flat(connection: EdgeBits) -> VertexBits:
    """Recover a vertex potential, normalized to zero at slice 0."""

    e = as_edge_bits(connection)
    if not is_flat(e):
        raise ValueError("connection is not flat")
    potential = (0, e[0], e[1], e[2])
    if edge_coboundary(potential) != e:
        raise AssertionError("flat reconstruction failed")
    return potential


def edge_weight(bits: EdgeBits) -> int:
    return sum(as_edge_bits(bits))


def face_weight(bits: FaceBits) -> int:
    return sum(as_face_bits(bits))


def correction(connection: EdgeBits, repair: EdgeBits) -> EdgeBits:
    return xor_bits(as_edge_bits(connection), as_edge_bits(repair))  # type: ignore[return-value]


def all_edge_bits() -> Iterator[EdgeBits]:
    for values in product((0, 1), repeat=6):
        yield values  # type: ignore[misc]


def all_vertex_bits() -> Iterator[VertexBits]:
    for values in product((0, 1), repeat=4):
        yield values  # type: ignore[misc]


def all_face_bits() -> Iterator[FaceBits]:
    for values in product((0, 1), repeat=4):
        yield values  # type: ignore[misc]


def repair_candidates(connection: EdgeBits) -> tuple[EdgeBits, ...]:
    """All minimum-Hamming corrections that make the connection flat."""

    e = as_edge_bits(connection)
    repairs = [repair for repair in all_edge_bits() if is_flat(correction(e, repair))]
    minimum = min(edge_weight(repair) for repair in repairs)
    return tuple(repair for repair in repairs if edge_weight(repair) == minimum)


def repair_distance(connection: EdgeBits) -> int:
    return edge_weight(repair_candidates(connection)[0])


def one_edge_mask(index: int) -> EdgeBits:
    if not 0 <= index < 6:
        raise ValueError("edge index must lie in 0..5")
    return tuple(1 if i == index else 0 for i in range(6))  # type: ignore[return-value]


def two_edge_mask(first: int, second: int) -> EdgeBits:
    if first == second:
        raise ValueError("edge indices must be distinct")
    return xor_bits(one_edge_mask(first), one_edge_mask(second))  # type: ignore[return-value]


def transport_phase(sign: int | bool, phase: tuple[int, int]) -> tuple[int, int]:
    """Identity or complex conjugation on the (even, odd) Euler coordinates."""

    c, s = phase
    return c, -s if _bit(sign) else s


def transport_winding(sign: int | bool, winding: int) -> int:
    return -winding if _bit(sign) else winding


def face_phase_monodromy(
    connection: EdgeBits, face_index: int, phase: tuple[int, int]
) -> tuple[int, int]:
    if not 0 <= face_index < 4:
        raise ValueError("face index must lie in 0..3")
    return transport_phase(face_holonomy(connection)[face_index], phase)


def face_winding_monodromy(connection: EdgeBits, face_index: int, winding: int) -> int:
    if not 0 <= face_index < 4:
        raise ValueError("face index must lie in 0..3")
    return transport_winding(face_holonomy(connection)[face_index], winding)


def signed_winding_globalizes(connection: EdgeBits) -> bool:
    return all(face_winding_monodromy(connection, face, 1) == 1 for face in range(4))


def chiral_quarter_turn_globalizes(connection: EdgeBits) -> bool:
    return all(face_phase_monodromy(connection, face, (0, 1)) == (0, 1) for face in range(4))


def half_turn_endpoint_globalizes(connection: EdgeBits) -> bool:
    return all(face_phase_monodromy(connection, face, (-1, 0)) == (-1, 0) for face in range(4))


@dataclass(frozen=True)
class ConnectionCertificate:
    connection: EdgeBits
    holonomy: FaceBits
    root_defect: RootDefect
    flat_part: EdgeBits
    root_normal_form: EdgeBits
    repair_distance: int
    minimum_repairs: tuple[EdgeBits, ...]
    signed_winding_globalizes: bool
    quarter_turn_globalizes: bool
    half_turn_endpoint_globalizes: bool


def connection_certificate(connection: EdgeBits) -> ConnectionCertificate:
    e = as_edge_bits(connection)
    return ConnectionCertificate(
        connection=e,
        holonomy=face_holonomy(e),
        root_defect=root_defect(e),
        flat_part=flat_part(e),
        root_normal_form=root_gauge_normal_form(e),
        repair_distance=repair_distance(e),
        minimum_repairs=repair_candidates(e),
        signed_winding_globalizes=signed_winding_globalizes(e),
        quarter_turn_globalizes=chiral_quarter_turn_globalizes(e),
        half_turn_endpoint_globalizes=half_turn_endpoint_globalizes(e),
    )


def exhaustive_audit() -> dict[str, object]:
    """Exhaustively verify the complete 64-state finite theorem package."""

    connections = tuple(all_edge_bits())
    gauges = tuple(all_vertex_bits())

    if len(connections) != 64 or len(gauges) != 16:
        raise AssertionError("finite state-space cardinality failure")

    fibers: dict[FaceBits, list[EdgeBits]] = {}
    flat_connections: list[EdgeBits] = []
    repair_histogram: dict[int, int] = {}

    for e in connections:
        h = face_holonomy(e)
        if not is_even_face_pattern(h):
            raise AssertionError("tetrahedral face parity failed")
        fibers.setdefault(h, []).append(e)

        for g in gauges:
            if face_holonomy(gauge_transform(e, g)) != h:
                raise AssertionError("holonomy is not gauge invariant")

        normal = root_gauge_normal_form(e)
        expected_normal = (0, 0, 0, h[0], h[1], h[2])
        if normal != expected_normal:
            raise AssertionError("root gauge normal form failed")

        if is_flat(e):
            flat_connections.append(e)
            if edge_coboundary(potential_for_flat(e)) != e:
                raise AssertionError("flat connection is not exact")
        else:
            try:
                potential_for_flat(e)
            except ValueError:
                pass
            else:
                raise AssertionError("nonflat connection admitted a potential")

        if signed_winding_globalizes(e) != is_flat(e):
            raise AssertionError("winding obstruction is not flatness")
        if chiral_quarter_turn_globalizes(e) != is_flat(e):
            raise AssertionError("quarter-turn obstruction is not flatness")
        if not half_turn_endpoint_globalizes(e):
            raise AssertionError("half-turn endpoint should be chirality blind")

        minimum_repairs = repair_candidates(e)
        distance = edge_weight(minimum_repairs[0])
        if any(edge_weight(repair) != distance for repair in minimum_repairs):
            raise AssertionError("minimum repair set has mixed weights")
        if any(not is_flat(correction(e, repair)) for repair in minimum_repairs):
            raise AssertionError("minimum repair did not flatten")
        repair_histogram[distance] = repair_histogram.get(distance, 0) + 1

        holonomy_weight = face_weight(h)
        if holonomy_weight == 0 and (distance != 0 or len(minimum_repairs) != 1):
            raise AssertionError("flat repair classification failed")
        if holonomy_weight == 2 and (distance != 1 or len(minimum_repairs) != 1):
            raise AssertionError("two-face repair classification failed")
        if holonomy_weight == 4:
            expected = {two_edge_mask(*pair) for pair in OPPOSITE_EDGE_PAIRS}
            if distance != 2 or set(minimum_repairs) != expected:
                raise AssertionError("fully frustrated repair classification failed")

    even_patterns = tuple(pattern for pattern in all_face_bits() if is_even_face_pattern(pattern))
    if len(even_patterns) != 8:
        raise AssertionError("even face-pattern dimension failure")
    if set(fibers) != set(even_patterns):
        raise AssertionError("curvature map is not onto the even face subspace")
    if {len(fiber) for fiber in fibers.values()} != {8}:
        raise AssertionError("curvature fibers do not all have cardinality eight")
    if len(flat_connections) != 8:
        raise AssertionError("flat connection count failed")

    for e in flat_connections:
        orbit = {gauge_transform(e, g) for g in gauges}
        if orbit != set(flat_connections):
            raise AssertionError("flat gauge action is not transitive")
        if len(orbit) != 8:
            raise AssertionError("global flip was not the exact gauge kernel")

    return {
        "connections": len(connections),
        "vertex_gauges": len(gauges),
        "effective_gauges": 8,
        "flat_connections": len(flat_connections),
        "curvature_patterns": len(even_patterns),
        "curvature_fiber_size": 8,
        "repair_distance_histogram": dict(sorted(repair_histogram.items())),
        "fully_frustrated_minimum_repairs": [
            two_edge_mask(*pair) for pair in OPPOSITE_EDGE_PAIRS
        ],
        "status": "PASS",
    }
