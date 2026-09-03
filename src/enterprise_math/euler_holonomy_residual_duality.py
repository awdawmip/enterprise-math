"""Exact S4-module bridge between Euler face holonomy and endpoint residuals.

The four triangular face holonomies of a K4 overlap-sign cochain form an
even-parity function on the four opposite vertices.  The mod-two tetrahedral
endpoint residual is the same even-function module, written in affine
coordinates `(p,q,e)`.  This module supplies the explicit mutual inverses,
the torsion-line identification, the six edge-state supports, and exhaustive
S4-equivariance checks.

No floating point, angle, trigonometry, or numerical value of pi is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from typing import Iterable, Iterator

from enterprise_math.euler_c12_root_torsor import (
    EdgeBits,
    HolonomyCode,
    all_edge_bits,
    edge_bits,
    face_holonomies,
    gauge_equivalent,
    holonomy_code,
    xor,
)

Bit = int
VertexValues = tuple[Bit, Bit, Bit, Bit]
Permutation = tuple[int, int, int, int]

VERTEX_NAMES = ("A", "B", "C", "D")
EDGE_PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
_EDGE_INDEX = {pair: index for index, pair in enumerate(EDGE_PAIRS)}


def _bit(value: int | bool) -> Bit:
    if isinstance(value, bool):
        return int(value)
    if not isinstance(value, int):
        raise TypeError("bit values must be integers or booleans")
    return value & 1


def vertex_values(values: Iterable[int | bool]) -> VertexValues:
    result = tuple(_bit(value) for value in values)
    if len(result) != 4:
        raise ValueError("vertex values must have exactly four entries")
    return result  # type: ignore[return-value]


@dataclass(frozen=True)
class AffineResidual:
    """Mod-two endpoint-residual coordinates for `f(x,y)=e+p*x+q*y`."""

    p: Bit
    q: Bit
    e: Bit

    def __post_init__(self) -> None:
        object.__setattr__(self, "p", _bit(self.p))
        object.__setattr__(self, "q", _bit(self.q))
        object.__setattr__(self, "e", _bit(self.e))

    @property
    def values(self) -> VertexValues:
        return (
            self.e,
            xor(self.e, self.p),
            xor(self.e, self.q),
            xor(self.e, self.p, self.q),
        )

    @property
    def support(self) -> tuple[int, ...]:
        return tuple(index for index, value in enumerate(self.values) if value)

    @property
    def is_constant(self) -> bool:
        return self.p == 0 and self.q == 0

    @property
    def is_torsion(self) -> bool:
        return self == TORSION_RESIDUAL

    def add(self, other: "AffineResidual") -> "AffineResidual":
        return AffineResidual(xor(self.p, other.p), xor(self.q, other.q), xor(self.e, other.e))

    def complement(self) -> "AffineResidual":
        return self.add(TORSION_RESIDUAL)


ZERO_RESIDUAL = AffineResidual(0, 0, 0)
TORSION_RESIDUAL = AffineResidual(0, 0, 1)


def all_residuals() -> Iterator[AffineResidual]:
    for p, q, e in product((0, 1), repeat=3):
        yield AffineResidual(p, q, e)


def values_to_residual(values: VertexValues) -> AffineResidual:
    a, b, c, d = vertex_values(values)
    if xor(a, b, c, d) != 0:
        raise ValueError("affine/even residual values must have even parity")
    result = AffineResidual(xor(a, b), xor(a, c), a)
    if result.values != (a, b, c, d):
        raise AssertionError("even vertex values failed affine reconstruction")
    return result


def opposite_face_values_from_code(code: HolonomyCode) -> VertexValues:
    """Assign each vertex the holonomy of its opposite triangular face.

    The code stores `(ABC, ABD, ACD)`.  The fourth value is
    `BCD = ABC + ABD + ACD`.
    """

    h_abc, h_abd, h_acd = _bit(code.abc), _bit(code.abd), _bit(code.acd)
    h_bcd = xor(h_abc, h_abd, h_acd)
    return h_bcd, h_acd, h_abd, h_abc


def opposite_face_values(edges: EdgeBits) -> VertexValues:
    h_abc, h_abd, h_acd, h_bcd = face_holonomies(edge_bits(edges))
    return h_bcd, h_acd, h_abd, h_abc


def holonomy_to_residual(code: HolonomyCode) -> AffineResidual:
    return values_to_residual(opposite_face_values_from_code(code))


def residual_to_holonomy(residual: AffineResidual) -> HolonomyCode:
    a, b, c, d = residual.values
    # Faces ABC, ABD, ACD are opposite D, C, B respectively.
    return HolonomyCode(d, c, b)


def edge_to_residual(edges: EdgeBits) -> AffineResidual:
    return holonomy_to_residual(holonomy_code(edge_bits(edges)))


def all_face_flip_code() -> HolonomyCode:
    """The code whose fourth face is also one."""

    return HolonomyCode(True, True, True)


def all_face_flip_edge_witness() -> EdgeBits:
    """All six overlap signs one; every triangular face has odd holonomy."""

    return (1, 1, 1, 1, 1, 1)


def residual_support_edge(residual: AffineResidual) -> tuple[int, int]:
    support = residual.support
    if len(support) != 2:
        raise ValueError("only a nonconstant affine residual has a two-vertex edge support")
    return support  # type: ignore[return-value]


def opposite_edge(edge: tuple[int, int]) -> tuple[int, int]:
    if len(edge) != 2 or edge[0] == edge[1] or any(vertex not in range(4) for vertex in edge):
        raise ValueError("edge must contain two distinct tetrahedral vertices")
    complement = tuple(vertex for vertex in range(4) if vertex not in edge)
    return complement  # type: ignore[return-value]


def all_permutations() -> Iterator[Permutation]:
    for permutation in permutations(range(4)):
        yield permutation  # type: ignore[misc]


def validate_permutation(permutation: Permutation) -> Permutation:
    permutation = tuple(permutation)  # type: ignore[assignment]
    if len(permutation) != 4 or set(permutation) != set(range(4)):
        raise ValueError("permutation must be a rearrangement of 0,1,2,3")
    return permutation  # type: ignore[return-value]


def permute_vertex_values(values: VertexValues, permutation: Permutation) -> VertexValues:
    """Push values forward under `old_vertex -> permutation[old_vertex]`."""

    values = vertex_values(values)
    permutation = validate_permutation(permutation)
    result = [0, 0, 0, 0]
    for old, new in enumerate(permutation):
        result[new] = values[old]
    return tuple(result)  # type: ignore[return-value]


def permute_edge_bits(edges: EdgeBits, permutation: Permutation) -> EdgeBits:
    """Push an edge cochain forward under a vertex permutation."""

    edges = edge_bits(edges)
    permutation = validate_permutation(permutation)
    result = [0] * 6
    for index, (left, right) in enumerate(EDGE_PAIRS):
        new_pair = tuple(sorted((permutation[left], permutation[right])))
        result[_EDGE_INDEX[new_pair]] = edges[index]
    return tuple(result)  # type: ignore[return-value]


def permute_residual(residual: AffineResidual, permutation: Permutation) -> AffineResidual:
    return values_to_residual(permute_vertex_values(residual.values, permutation))


def invariant_residuals() -> tuple[AffineResidual, ...]:
    permutations_all = tuple(all_permutations())
    return tuple(
        residual
        for residual in all_residuals()
        if all(permute_residual(residual, permutation) == residual for permutation in permutations_all)
    )


@dataclass(frozen=True)
class DualityReport:
    edge_cochains: int
    gauge_classes: int
    residual_states: int
    invariant_states: tuple[AffineResidual, ...]
    nonconstant_edge_states: int
    permutations_checked: int
    equivariance_pairs_checked: int


def verify_holonomy_residual_duality() -> DualityReport:
    residuals = tuple(all_residuals())
    edge_states = tuple(all_edge_bits())
    permutations_all = tuple(all_permutations())

    # Mutual inverse between the two three-bit coordinate systems.
    for residual in residuals:
        if holonomy_to_residual(residual_to_holonomy(residual)) != residual:
            raise AssertionError("holonomy/residual inverse failed")
    codes = tuple(HolonomyCode(bool(a), bool(b), bool(c)) for a, b, c in product((0, 1), repeat=3))
    for code in codes:
        if residual_to_holonomy(holonomy_to_residual(code)) != code:
            raise AssertionError("residual/holonomy inverse failed")

    # Complete gauge invariant inherited from face holonomy.
    for left in edge_states:
        for right in edge_states:
            if gauge_equivalent(left, right) != (edge_to_residual(left) == edge_to_residual(right)):
                raise AssertionError("endpoint residual failed to classify chirality gauge orbit")

    # Opposite-face evaluation and S4 equivariance.
    equivariance_pairs = 0
    for edges in edge_states:
        for permutation in permutations_all:
            pushed_edges = permute_edge_bits(edges, permutation)
            expected_values = permute_vertex_values(opposite_face_values(edges), permutation)
            if opposite_face_values(pushed_edges) != expected_values:
                raise AssertionError("opposite-face holonomy is not S4-equivariant")
            if edge_to_residual(pushed_edges) != permute_residual(edge_to_residual(edges), permutation):
                raise AssertionError("holonomy-to-residual bridge is not S4-equivariant")
            equivariance_pairs += 1

    # Distinguished invariant line.
    invariants = invariant_residuals()
    if invariants != (ZERO_RESIDUAL, TORSION_RESIDUAL):
        raise AssertionError("the invariant subspace is not the expected torsion line")
    if holonomy_to_residual(all_face_flip_code()) != TORSION_RESIDUAL:
        raise AssertionError("all-face-flip holonomy did not map to endpoint torsion")
    if edge_to_residual(all_face_flip_edge_witness()) != TORSION_RESIDUAL:
        raise AssertionError("all-edge-one witness did not represent endpoint torsion")

    # Six nonconstant affine states reconstruct the six K4 edges, and torsion
    # complements each support to the opposite edge.
    nonconstant = tuple(residual for residual in residuals if not residual.is_constant)
    supports = {residual_support_edge(residual) for residual in nonconstant}
    if supports != set(EDGE_PAIRS):
        raise AssertionError("nonconstant residual supports do not recover all K4 edges")
    for residual in nonconstant:
        if residual_support_edge(residual.complement()) != opposite_edge(residual_support_edge(residual)):
            raise AssertionError("torsion addition did not exchange opposite edges")

    return DualityReport(
        edge_cochains=len(edge_states),
        gauge_classes=len(residuals),
        residual_states=len(residuals),
        invariant_states=invariants,
        nonconstant_edge_states=len(nonconstant),
        permutations_checked=len(permutations_all),
        equivariance_pairs_checked=equivariance_pairs,
    )


def complete_duality_certificate() -> dict[str, object]:
    report = verify_holonomy_residual_duality()
    return {
        "edge_cochains": report.edge_cochains,
        "gauge_classes": report.gauge_classes,
        "residual_states": report.residual_states,
        "invariant_states": [
            {"p": residual.p, "q": residual.q, "e": residual.e}
            for residual in report.invariant_states
        ],
        "nonconstant_edge_states": report.nonconstant_edge_states,
        "permutations_checked": report.permutations_checked,
        "equivariance_pairs_checked": report.equivariance_pairs_checked,
        "all_face_flip_maps_to": {"p": 0, "q": 0, "e": 1},
        "orbit_decomposition": [1, 1, 6],
        "boundary": (
            "This is an S4-equivariant mod-two representation bridge. It does not "
            "identify a local C12 root-kernel operation with the integral endpoint "
            "torsion generator as a native operation."
        ),
    }
