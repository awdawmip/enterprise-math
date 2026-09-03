"""Exact tetrahedral FCC chirality gauge and face-holonomy classification.

The four three-axis FCC slices are vertices of K4. A local comparison of
signed chiral generators across each of the six pairwise overlaps is an F2
edge cochain. Reversing the chosen generator in one slice is a vertex gauge
transformation. The four triangular face holonomies are the complete gauge
invariant.

This module is finite and exact. It does not infer the overlap bits from bare
FCC incidence and it does not identify slice chirality with the already
globally closed sign assignment on the twelve oriented FCC directions.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import permutations, product
from typing import Iterator, Sequence

Bit = int
EdgeBits = tuple[Bit, Bit, Bit, Bit, Bit, Bit]
GaugeBits = tuple[Bit, Bit, Bit, Bit]
FaceBits = tuple[Bit, Bit, Bit, Bit]
Permutation4 = tuple[int, int, int, int]

VERTICES: tuple[int, ...] = (0, 1, 2, 3)
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
FACE_INDEX = {face: index for index, face in enumerate(FACES)}

ZERO_EDGES: EdgeBits = (0, 0, 0, 0, 0, 0)
ANTIBALANCED_EDGES: EdgeBits = (1, 1, 1, 1, 1, 1)
ZERO_GAUGE: GaugeBits = (0, 0, 0, 0)
GLOBAL_FLIP: GaugeBits = (1, 1, 1, 1)
ZERO_FACES: FaceBits = (0, 0, 0, 0)
ALL_ODD_FACES: FaceBits = (1, 1, 1, 1)


def _bits(values: Sequence[int], length: int, name: str) -> tuple[int, ...]:
    if len(values) != length:
        raise ValueError(f"{name} must contain exactly {length} bits")
    out: list[int] = []
    for value in values:
        if isinstance(value, bool):
            value = int(value)
        if value not in (0, 1):
            raise ValueError(f"{name} entries must be 0 or 1")
        out.append(int(value))
    return tuple(out)


def normalize_edges(values: Sequence[int]) -> EdgeBits:
    return _bits(values, 6, "edge assignment")  # type: ignore[return-value]


def normalize_gauge(values: Sequence[int]) -> GaugeBits:
    return _bits(values, 4, "gauge")  # type: ignore[return-value]


def normalize_faces(values: Sequence[int]) -> FaceBits:
    return _bits(values, 4, "face pattern")  # type: ignore[return-value]


def edge_assignments() -> Iterator[EdgeBits]:
    for values in product((0, 1), repeat=6):
        yield normalize_edges(values)


def gauges() -> Iterator[GaugeBits]:
    for values in product((0, 1), repeat=4):
        yield normalize_gauge(values)


def face_patterns() -> Iterator[FaceBits]:
    for values in product((0, 1), repeat=4):
        yield normalize_faces(values)


def s4_permutations() -> Iterator[Permutation4]:
    for values in permutations(VERTICES):
        yield values  # type: ignore[misc]


def gauge_action(edges: Sequence[int], gauge: Sequence[int]) -> EdgeBits:
    """Apply the vertex-frame gauge e_ij -> e_ij + g_i + g_j (mod 2)."""

    edge_bits = normalize_edges(edges)
    gauge_bits = normalize_gauge(gauge)
    return tuple(
        edge_bits[index] ^ gauge_bits[left] ^ gauge_bits[right]
        for index, (left, right) in enumerate(EDGES)
    )  # type: ignore[return-value]


def face_holonomy(edges: Sequence[int]) -> FaceBits:
    """Return face XORs in order 012, 013, 023, 123."""

    edge_bits = normalize_edges(edges)
    values: list[int] = []
    for a, b, c in FACES:
        values.append(
            edge_bits[EDGE_INDEX[(a, b)]]
            ^ edge_bits[EDGE_INDEX[(a, c)]]
            ^ edge_bits[EDGE_INDEX[(b, c)]]
        )
    return normalize_faces(values)


def face_parity(faces: Sequence[int]) -> int:
    result = 0
    for value in normalize_faces(faces):
        result ^= value
    return result


def face_weight(faces: Sequence[int]) -> int:
    return sum(normalize_faces(faces))


def is_even_face_pattern(faces: Sequence[int]) -> bool:
    return face_parity(faces) == 0


def gauge_orbit(edges: Sequence[int]) -> frozenset[EdgeBits]:
    edge_bits = normalize_edges(edges)
    return frozenset(gauge_action(edge_bits, gauge) for gauge in gauges())


def gauge_equivalent(left: Sequence[int], right: Sequence[int]) -> bool:
    return normalize_edges(right) in gauge_orbit(left)


def globalizable(edges: Sequence[int]) -> bool:
    """Whether the transition system admits one globally signed slice J."""

    return face_holonomy(edges) == ZERO_FACES


def trivializing_gauges(edges: Sequence[int]) -> tuple[GaugeBits, ...]:
    edge_bits = normalize_edges(edges)
    return tuple(
        gauge for gauge in gauges() if gauge_action(edge_bits, gauge) == ZERO_EDGES
    )


def representative_from_even_faces(faces: Sequence[int]) -> EdgeBits:
    """Choose the star gauge e01=e02=e03=0 for an even face pattern."""

    h012, h013, h023, h123 = normalize_faces(faces)
    if h012 ^ h013 ^ h023 ^ h123:
        raise ValueError("tetrahedral face holonomy must have even parity")
    edges: EdgeBits = (0, 0, 0, h012, h013, h023)
    if face_holonomy(edges) != (h012, h013, h023, h123):
        raise AssertionError("canonical face representative failed")
    return edges


def _permutation(values: Sequence[int]) -> Permutation4:
    if len(values) != 4 or set(values) != set(VERTICES):
        raise ValueError("permutation must contain 0,1,2,3 exactly once")
    return tuple(int(value) for value in values)  # type: ignore[return-value]


def permute_face_pattern(
    faces: Sequence[int], permutation: Sequence[int]
) -> FaceBits:
    """Apply a vertex permutation to the four tetrahedral face bits."""

    face_bits = normalize_faces(faces)
    perm = _permutation(permutation)
    out = [0, 0, 0, 0]
    for index, face in enumerate(FACES):
        image = tuple(sorted(perm[vertex] for vertex in face))
        out[FACE_INDEX[image]] = face_bits[index]
    return normalize_faces(out)


def s4_orbit(faces: Sequence[int]) -> frozenset[FaceBits]:
    face_bits = normalize_faces(faces)
    return frozenset(
        permute_face_pattern(face_bits, permutation)
        for permutation in s4_permutations()
    )


def is_s4_fixed(faces: Sequence[int]) -> bool:
    face_bits = normalize_faces(faces)
    return all(
        permute_face_pattern(face_bits, permutation) == face_bits
        for permutation in s4_permutations()
    )


@dataclass(frozen=True)
class ChiralityClassification:
    edge_assignments: int
    gauge_group_size: int
    gauge_kernel_size: int
    gauge_orbit_count: int
    gauge_orbit_sizes: tuple[int, ...]
    even_face_patterns: tuple[FaceBits, ...]
    face_weight_class_counts: tuple[tuple[int, int], ...]
    s4_face_orbit_sizes: tuple[int, ...]
    s4_fixed_patterns: tuple[FaceBits, ...]
    flat_edge_assignments: int
    weight_two_edge_assignments: int
    all_odd_edge_assignments: int

    def as_dict(self) -> dict[str, object]:
        return {
            "edge_assignments": self.edge_assignments,
            "gauge_group_size": self.gauge_group_size,
            "gauge_kernel_size": self.gauge_kernel_size,
            "gauge_orbit_count": self.gauge_orbit_count,
            "gauge_orbit_sizes": list(self.gauge_orbit_sizes),
            "even_face_patterns": [
                list(pattern) for pattern in self.even_face_patterns
            ],
            "face_weight_class_counts": {
                str(weight): count for weight, count in self.face_weight_class_counts
            },
            "s4_face_orbit_sizes": list(self.s4_face_orbit_sizes),
            "s4_fixed_patterns": [list(pattern) for pattern in self.s4_fixed_patterns],
            "flat_edge_assignments": self.flat_edge_assignments,
            "weight_two_edge_assignments": self.weight_two_edge_assignments,
            "all_odd_edge_assignments": self.all_odd_edge_assignments,
        }


def classify() -> ChiralityClassification:
    all_edges = tuple(edge_assignments())
    all_gauges = tuple(gauges())

    kernel = tuple(
        gauge
        for gauge in all_gauges
        if all(gauge_action(edges, gauge) == edges for edges in all_edges)
    )
    if set(kernel) != {ZERO_GAUGE, GLOBAL_FLIP}:
        raise AssertionError("vertex-gauge kernel is not the expected global flip")

    unseen = set(all_edges)
    orbits: list[frozenset[EdgeBits]] = []
    while unseen:
        representative = min(unseen)
        orbit = gauge_orbit(representative)
        orbits.append(orbit)
        unseen.difference_update(orbit)

    orbit_holonomies: list[FaceBits] = []
    for orbit in orbits:
        values = {face_holonomy(edges) for edges in orbit}
        if len(values) != 1:
            raise AssertionError("face holonomy was not gauge invariant")
        orbit_holonomies.append(next(iter(values)))

    even_patterns = tuple(
        sorted(pattern for pattern in face_patterns() if is_even_face_pattern(pattern))
    )
    if set(orbit_holonomies) != set(even_patterns):
        raise AssertionError("face holonomy does not classify all gauge orbits")

    for left in all_edges:
        for right in all_edges:
            if (face_holonomy(left) == face_holonomy(right)) != gauge_equivalent(
                left, right
            ):
                raise AssertionError("equal holonomy failed to match gauge equivalence")

    face_weight_counts = Counter(face_weight(pattern) for pattern in even_patterns)

    remaining = set(even_patterns)
    s4_orbits: list[frozenset[FaceBits]] = []
    while remaining:
        representative = min(remaining)
        orbit = s4_orbit(representative)
        s4_orbits.append(orbit)
        remaining.difference_update(orbit)

    fixed = tuple(
        sorted(pattern for pattern in even_patterns if is_s4_fixed(pattern))
    )
    if fixed != (ZERO_FACES, ALL_ODD_FACES):
        raise AssertionError("unexpected full S4 fixed face patterns")

    edge_weight_counts = Counter(
        face_weight(face_holonomy(edges)) for edges in all_edges
    )

    return ChiralityClassification(
        edge_assignments=len(all_edges),
        gauge_group_size=len(all_gauges),
        gauge_kernel_size=len(kernel),
        gauge_orbit_count=len(orbits),
        gauge_orbit_sizes=tuple(sorted(len(orbit) for orbit in orbits)),
        even_face_patterns=even_patterns,
        face_weight_class_counts=tuple(sorted(face_weight_counts.items())),
        s4_face_orbit_sizes=tuple(sorted(len(orbit) for orbit in s4_orbits)),
        s4_fixed_patterns=fixed,
        flat_edge_assignments=edge_weight_counts[0],
        weight_two_edge_assignments=edge_weight_counts[2],
        all_odd_edge_assignments=edge_weight_counts[4],
    )


def verify_accepted_antibalanced_signature() -> dict[str, object]:
    """Certificate for the accepted P000 all-overlap-negative representative."""

    holonomy = face_holonomy(ANTIBALANCED_EDGES)
    if holonomy != ALL_ODD_FACES:
        raise AssertionError("all-negative edge signature is not all-face-odd")
    if globalizable(ANTIBALANCED_EDGES):
        raise AssertionError("all-face-odd signature unexpectedly globalized")
    return {
        "edge_bits": list(ANTIBALANCED_EDGES),
        "face_holonomy": list(holonomy),
        "s4_fixed": is_s4_fixed(holonomy),
        "global_signed_J_exists": False,
        "interpretation": "unique nonzero fully S4-invariant gauge class",
    }


def classification_report() -> dict[str, object]:
    return {
        "schema": "ENTERPRISE_EULER_FCC_CHIRALITY_CLASSIFICATION_V1",
        "classification": classify().as_dict(),
        "accepted_antibalanced_signature": verify_accepted_antibalanced_signature(),
        "typed_boundaries": [
            "direction-sign closure on 12 FCC directions is distinct from slice-chirality gluing",
            "overlap signs are inputs; bare FCC incidence does not derive them",
            "all-face-odd obstructs one global signed J but not reversal-even scalar observables",
        ],
    }


if __name__ == "__main__":
    import json

    print(json.dumps(classification_report(), indent=2, sort_keys=True))
