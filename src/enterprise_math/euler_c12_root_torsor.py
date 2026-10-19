"""Exact C12 quarter-turn torsor and tetrahedral chirality-flatness calculus.

The module separates three finite objects that are all abstractly binary but have
three different mathematical types:

* the C2 orientation-reversal factor in C6 = C3 x C2;
* the kernel of the non-split root cover C12 -> C6;
* the free transitive choice between the two quarter-turn roots 3 and 9.

It also treats the four FCC slice charts as the vertices of K4.  Edge bits are
local comparisons of the two quarter-turn signs.  The three independent face
holonomies classify the graph gauge orbit, while vanishing face holonomy is
necessary and sufficient for a global signed root, unique up to overall
reversal.

Only integer arithmetic and exhaustive finite enumeration are used.  No angle,
trigonometric function, floating point, or numerical value of pi appears.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Iterable, Iterator

Bit = int
VertexBits = tuple[Bit, Bit, Bit, Bit]
EdgeBits = tuple[Bit, Bit, Bit, Bit, Bit, Bit]
HolonomyCode = tuple[Bit, Bit, Bit]

VERTICES = ("A", "B", "C", "D")
EDGES = ("AB", "AC", "AD", "BC", "BD", "CD")
FACES = ("ABC", "ABD", "ACD", "BCD")


def _bit(value: int | bool) -> Bit:
    if isinstance(value, bool):
        return int(value)
    if not isinstance(value, int):
        raise TypeError("bit values must be integers or booleans")
    return value & 1


def _bits(values: Iterable[int | bool], length: int, name: str) -> tuple[Bit, ...]:
    result = tuple(_bit(value) for value in values)
    if len(result) != length:
        raise ValueError(f"{name} must have exactly {length} entries")
    return result


def vertex_bits(values: Iterable[int | bool]) -> VertexBits:
    return _bits(values, 4, "vertex bits")  # type: ignore[return-value]


def edge_bits(values: Iterable[int | bool]) -> EdgeBits:
    return _bits(values, 6, "edge bits")  # type: ignore[return-value]


def xor(*values: int | bool) -> Bit:
    result = 0
    for value in values:
        result ^= _bit(value)
    return result


def add_mod(left: int, right: int, modulus: int) -> int:
    if isinstance(left, bool) or isinstance(right, bool):
        raise TypeError("cyclic coordinates must be integers")
    if not isinstance(left, int) or not isinstance(right, int):
        raise TypeError("cyclic coordinates must be integers")
    if not isinstance(modulus, int) or isinstance(modulus, bool) or modulus <= 0:
        raise ValueError("modulus must be a positive integer")
    return (left + right) % modulus


def neg_mod(value: int, modulus: int) -> int:
    return (-value) % modulus


def nsmul_mod(multiplier: int, value: int, modulus: int) -> int:
    return (multiplier * value) % modulus


# ---------------------------------------------------------------------------
# C6 and C12 Chinese-remainder structure
# ---------------------------------------------------------------------------


def crt6(value: int) -> tuple[int, int]:
    value %= 6
    return value % 3, value % 2


def crt6_inverse(value: tuple[int, int]) -> int:
    a, b = value
    return (4 * (a % 3) + 3 * (b % 2)) % 6


def crt12(value: int) -> tuple[int, int]:
    value %= 12
    return value % 3, value % 4


def crt12_inverse(value: tuple[int, int]) -> int:
    a, b = value
    return (4 * (a % 3) + 9 * (b % 4)) % 12


def reduce12_to6(value: int) -> int:
    return value % 6


def reduce4_to2(value: int) -> int:
    return value % 2


def root_cover_kernel() -> tuple[int, int]:
    return tuple(value for value in range(12) if reduce12_to6(value) == 0)  # type: ignore[return-value]


def generator_lifts() -> tuple[int, int]:
    return tuple(value for value in range(12) if reduce12_to6(value) == 1)  # type: ignore[return-value]


def quarter_turn_roots() -> tuple[int, int]:
    """Solutions of 2q=6 in C12, ordered as +J and -J representatives."""

    return tuple(value for value in range(12) if (2 * value) % 12 == 6)  # type: ignore[return-value]


def root_state(sign: int | bool) -> int:
    """Return one of the two quarter-turn roots; bit zero gives 3, one gives 9."""

    return 3 if _bit(sign) == 0 else 9


def root_sign(root: int) -> Bit:
    root %= 12
    if root == 3:
        return 0
    if root == 9:
        return 1
    raise ValueError("root must be one of the two quarter-turn roots 3 or 9")


def transport_root(edge_sign: int | bool, root: int) -> int:
    """Transport a local root across an overlap: bit one applies inversion."""

    root %= 12
    if root not in quarter_turn_roots():
        raise ValueError("transport is defined here only on the quarter-turn torsor")
    return root if _bit(edge_sign) == 0 else neg_mod(root, 12)


def root_cover_report() -> dict[str, object]:
    kernel = root_cover_kernel()
    generators = generator_lifts()
    roots = quarter_turn_roots()
    report = {
        "c6_crt": {value: crt6(value) for value in range(6)},
        "c12_crt": {value: crt12(value) for value in range(12)},
        "kernel": kernel,
        "generator_lifts": generators,
        "generator_lift_sixfolds": {value: nsmul_mod(6, value, 12) for value in generators},
        "quarter_turn_roots": roots,
        "root_reductions": {value: reduce12_to6(value) for value in roots},
        "root_doubles": {value: nsmul_mod(2, value, 12) for value in roots},
        "root_inversions": {value: neg_mod(value, 12) for value in roots},
    }
    verify_root_cover()
    return report


def verify_root_cover() -> None:
    for value in range(6):
        if crt6_inverse(crt6(value)) != value:
            raise AssertionError("C6 Chinese-remainder inverse failed")
    for value in product(range(3), range(2)):
        if crt6(crt6_inverse(value)) != value:
            raise AssertionError("C6 inverse Chinese-remainder map failed")

    for value in range(12):
        if crt12_inverse(crt12(value)) != value:
            raise AssertionError("C12 Chinese-remainder inverse failed")
        left = crt6(reduce12_to6(value))
        a, b4 = crt12(value)
        right = (a, reduce4_to2(b4))
        if left != right:
            raise AssertionError("root-cover CRT square failed to commute")
    for value in product(range(3), range(4)):
        if crt12(crt12_inverse(value)) != value:
            raise AssertionError("C12 inverse Chinese-remainder map failed")

    if root_cover_kernel() != (0, 6):
        raise AssertionError("C12 -> C6 kernel is not {0,6}")
    if set(reduce12_to6(value) for value in range(12)) != set(range(6)):
        raise AssertionError("C12 -> C6 is not surjective")

    # A group section would send the C6 generator to a preimage annihilated by 6.
    if generator_lifts() != (1, 7):
        raise AssertionError("unexpected lifts of the C6 generator")
    if any(nsmul_mod(6, value, 12) == 0 for value in generator_lifts()):
        raise AssertionError("the root cover unexpectedly admits a generator section")

    roots = quarter_turn_roots()
    if roots != (3, 9):
        raise AssertionError("unexpected quarter-turn root fiber")
    for root in roots:
        if reduce12_to6(root) != 3:
            raise AssertionError("quarter-turn root does not reduce to the C6 half-turn")
        if nsmul_mod(2, root, 12) != 6:
            raise AssertionError("quarter-turn root does not square/double to the half-turn")
        if neg_mod(root, 12) == root:
            raise AssertionError("quarter-turn root was incorrectly inversion-fixed")
        if neg_mod(root, 12) not in roots:
            raise AssertionError("inversion left the quarter-turn torsor")


# ---------------------------------------------------------------------------
# Tetrahedral slice atlas over F2
# Edge order: AB, AC, AD, BC, BD, CD.
# ---------------------------------------------------------------------------


def edge_xor(left: EdgeBits, right: EdgeBits) -> EdgeBits:
    left = edge_bits(left)
    right = edge_bits(right)
    return tuple(xor(a, b) for a, b in zip(left, right))  # type: ignore[return-value]


def vertex_flip(vertices: VertexBits) -> VertexBits:
    vertices = vertex_bits(vertices)
    return tuple(xor(value, 1) for value in vertices)  # type: ignore[return-value]


def coboundary(vertices: VertexBits) -> EdgeBits:
    a, b, c, d = vertex_bits(vertices)
    return (
        xor(a, b),
        xor(a, c),
        xor(a, d),
        xor(b, c),
        xor(b, d),
        xor(c, d),
    )


def face_holonomies(edges: EdgeBits) -> tuple[Bit, Bit, Bit, Bit]:
    ab, ac, ad, bc, bd, cd = edge_bits(edges)
    return (
        xor(ab, ac, bc),
        xor(ab, ad, bd),
        xor(ac, ad, cd),
        xor(bc, bd, cd),
    )


def holonomy_code(edges: EdgeBits) -> HolonomyCode:
    h_abc, h_abd, h_acd, _ = face_holonomies(edges)
    return h_abc, h_abd, h_acd


def is_flat(edges: EdgeBits) -> bool:
    return face_holonomies(edges) == (0, 0, 0, 0)


def gauge_transform(edges: EdgeBits, gauge: VertexBits) -> EdgeBits:
    return edge_xor(edge_bits(edges), coboundary(vertex_bits(gauge)))


def gauge_equivalent(left: EdgeBits, right: EdgeBits) -> bool:
    left = edge_bits(left)
    right = edge_bits(right)
    return any(gauge_transform(left, gauge) == right for gauge in all_vertex_bits())


def reconstruct_vertex_signs(edges: EdgeBits, *, root_at_a: int | bool = 0) -> VertexBits:
    """Reconstruct a global root assignment from a flat edge system.

    `root_at_a` chooses the overall sign.  The result exists exactly for flat
    edge data and the two choices are global complements.
    """

    edges = edge_bits(edges)
    if not is_flat(edges):
        raise ValueError("non-flat edge signs do not globalize")
    a = _bit(root_at_a)
    ab, ac, ad, _, _, _ = edges
    result = (a, xor(a, ab), xor(a, ac), xor(a, ad))
    if coboundary(result) != edges:
        raise AssertionError("flat reconstruction failed")
    return result


def global_root_assignments(edges: EdgeBits) -> tuple[VertexBits, VertexBits]:
    first = reconstruct_vertex_signs(edges, root_at_a=0)
    second = reconstruct_vertex_signs(edges, root_at_a=1)
    if second != vertex_flip(first):
        raise AssertionError("global root assignments are not overall reversals")
    return first, second


def transport_assignment(vertices: VertexBits) -> tuple[int, int, int, int]:
    """Map four vertex bits to the corresponding local C12 roots."""

    return tuple(root_state(bit) for bit in vertex_bits(vertices))  # type: ignore[return-value]


def edge_transport_is_consistent(vertices: VertexBits) -> bool:
    vertices = vertex_bits(vertices)
    edges = coboundary(vertices)
    roots = transport_assignment(vertices)
    edge_indices = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
    return all(
        transport_root(edges[index], roots[left]) == roots[right]
        for index, (left, right) in enumerate(edge_indices)
    )


def triangle_transport(edges: EdgeBits, face: str, root: int = 3) -> int:
    """Transport a root once around one oriented triangular face."""

    ab, ac, ad, bc, bd, cd = edge_bits(edges)
    face_edges = {
        "ABC": (ab, bc, ac),
        "ABD": (ab, bd, ad),
        "ACD": (ac, cd, ad),
        "BCD": (bc, cd, bd),
    }
    try:
        signs = face_edges[face.upper()]
    except KeyError as exc:
        raise ValueError(f"unknown tetrahedral face {face!r}") from exc
    result = root % 12
    for sign in signs:
        result = transport_root(sign, result)
    return result


def projective_half_turn_endpoint(root: int) -> int:
    """The chirality-even endpoint obtained by composing a root with itself."""

    root %= 12
    if root not in quarter_turn_roots():
        raise ValueError("expected one of the two quarter-turn roots")
    return nsmul_mod(2, root, 12)


def all_vertex_bits() -> Iterator[VertexBits]:
    for values in product((0, 1), repeat=4):
        yield values  # type: ignore[misc]


def all_edge_bits() -> Iterator[EdgeBits]:
    for values in product((0, 1), repeat=6):
        yield values  # type: ignore[misc]


def all_holonomy_codes() -> Iterator[HolonomyCode]:
    for values in product((0, 1), repeat=3):
        yield values  # type: ignore[misc]


@dataclass(frozen=True)
class TetrahedralFlatnessReport:
    edge_systems: int
    flat_edge_systems: int
    gauge_orbits: int
    systems_per_holonomy_code: int
    global_lifts_per_flat_system: int
    independent_face_bits: int
    fourth_face_relation_verified: bool
    projective_endpoint: int


def verify_tetrahedral_flatness() -> TetrahedralFlatnessReport:
    edge_states = tuple(all_edge_bits())
    vertex_states = tuple(all_vertex_bits())

    image = {coboundary(vertices) for vertices in vertex_states}
    flat = {edges for edges in edge_states if is_flat(edges)}
    if image != flat:
        raise AssertionError("flat edge systems are not exactly the coboundaries")

    for vertices in vertex_states:
        if coboundary(vertex_flip(vertices)) != coboundary(vertices):
            raise AssertionError("overall root reversal changed overlap signs")
        if not edge_transport_is_consistent(vertices):
            raise AssertionError("coboundary edge data failed to transport local roots")

    for edges in edge_states:
        h_abc, h_abd, h_acd, h_bcd = face_holonomies(edges)
        if h_bcd != xor(h_abc, h_abd, h_acd):
            raise AssertionError("the fourth face holonomy is not the sum of the first three")

        lifts = tuple(vertices for vertices in vertex_states if coboundary(vertices) == edges)
        if is_flat(edges):
            if len(lifts) != 2:
                raise AssertionError("a flat transition system should have exactly two global roots")
            reconstructed = global_root_assignments(edges)
            if set(reconstructed) != set(lifts):
                raise AssertionError("explicit reconstruction missed a global lift")
            for face in FACES:
                for root in quarter_turn_roots():
                    if triangle_transport(edges, face, root) != root:
                        raise AssertionError("flat face transport changed the root")
        elif lifts:
            raise AssertionError("a non-flat transition system unexpectedly globalized")

    code_fibers = {
        code: {edges for edges in edge_states if holonomy_code(edges) == code}
        for code in all_holonomy_codes()
    }
    if any(len(fiber) != 8 for fiber in code_fibers.values()):
        raise AssertionError("holonomy-code fibers do not all have size eight")

    # The three face bits are a complete gauge invariant.
    for left in edge_states:
        for right in edge_states:
            same_code = holonomy_code(left) == holonomy_code(right)
            if gauge_equivalent(left, right) != same_code:
                raise AssertionError("three face holonomies failed to classify a gauge orbit")

    # Nonzero face holonomy flips every local quarter-turn root on transport.
    for edges in edge_states:
        for face, holonomy in zip(FACES, face_holonomies(edges)):
            for root in quarter_turn_roots():
                transported = triangle_transport(edges, face, root)
                expected = root if holonomy == 0 else neg_mod(root, 12)
                if transported != expected:
                    raise AssertionError("triangle root transport disagrees with face holonomy")

    endpoints = {projective_half_turn_endpoint(root) for root in quarter_turn_roots()}
    if endpoints != {6}:
        raise AssertionError("projective half-turn endpoint depends on chirality")

    return TetrahedralFlatnessReport(
        edge_systems=len(edge_states),
        flat_edge_systems=len(flat),
        gauge_orbits=len(code_fibers),
        systems_per_holonomy_code=next(iter(map(len, code_fibers.values()))),
        global_lifts_per_flat_system=2,
        independent_face_bits=3,
        fourth_face_relation_verified=True,
        projective_endpoint=6,
    )


def complete_certificate() -> dict[str, object]:
    verify_root_cover()
    flatness = verify_tetrahedral_flatness()
    return {
        "root_cover": root_cover_report(),
        "tetrahedral_flatness": {
            "edge_systems": flatness.edge_systems,
            "flat_edge_systems": flatness.flat_edge_systems,
            "gauge_orbits": flatness.gauge_orbits,
            "systems_per_holonomy_code": flatness.systems_per_holonomy_code,
            "global_lifts_per_flat_system": flatness.global_lifts_per_flat_system,
            "independent_face_bits": flatness.independent_face_bits,
            "fourth_face_relation_verified": flatness.fourth_face_relation_verified,
            "projective_endpoint": flatness.projective_endpoint,
        },
        "boundaries": [
            "C6 orientation parity is not identified with the C12 root-cover kernel",
            "incidence data do not supply the six overlap signs",
            "native dynamics have not yet forced triangular flatness",
            "the two global chiralities remain an overall C2 torsor",
            "J is a derived rotation character, not a primitive spatial axis",
        ],
    }
