"""Exact finite chirality globalization for the four-slice Euler structure.

The module works only with F2 edge signs and finite cyclic phase groups.  It
contains no floating-point arithmetic, trigonometry, or numerical value of pi.

Four local slices are the vertices of K4; their six shared line families are
its edges.  A bit on an edge says whether a handoff preserves or reverses the
local chiral generator.  Vertex sign changes are gauge transformations.
"""

from __future__ import annotations

from collections import Counter
from itertools import permutations, product
from typing import Iterable, Iterator, Sequence

VertexBits = tuple[int, int, int, int]
EdgeBits = tuple[int, int, int, int, int, int]
O2State = tuple[int, int]

VERTICES = (0, 1, 2, 3)
EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
EDGE_INDEX = {edge: index for index, edge in enumerate(EDGES)}
TRIANGLES = ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))


def _bit(value: int) -> int:
    if isinstance(value, bool):
        return int(value)
    if not isinstance(value, int):
        raise TypeError("F2 coordinates must be integers")
    return value & 1


def _edge(u: int, v: int) -> tuple[int, int]:
    if u == v or u not in VERTICES or v not in VERTICES:
        raise ValueError("an edge joins two distinct K4 vertices")
    return (u, v) if u < v else (v, u)


def normalize_vertex_bits(values: Sequence[int]) -> VertexBits:
    if len(values) != 4:
        raise ValueError("a K4 vertex gauge has four bits")
    return tuple(_bit(value) for value in values)  # type: ignore[return-value]


def normalize_edge_bits(values: Sequence[int]) -> EdgeBits:
    if len(values) != 6:
        raise ValueError("a K4 chirality cochain has six bits")
    return tuple(_bit(value) for value in values)  # type: ignore[return-value]


def edge_value(cochain: EdgeBits, u: int, v: int) -> int:
    return cochain[EDGE_INDEX[_edge(u, v)]]


def add_edge_bits(left: EdgeBits, right: EdgeBits) -> EdgeBits:
    return tuple(a ^ b for a, b in zip(left, right))  # type: ignore[return-value]


def coboundary(vertex_signs: Sequence[int]) -> EdgeBits:
    """Return delta sigma on K4: (delta sigma)_(uv)=sigma_u+sigma_v in F2."""

    sigma = normalize_vertex_bits(vertex_signs)
    return tuple(sigma[u] ^ sigma[v] for u, v in EDGES)  # type: ignore[return-value]


def gauge_transform(cochain: Sequence[int], vertex_signs: Sequence[int]) -> EdgeBits:
    return add_edge_bits(normalize_edge_bits(cochain), coboundary(vertex_signs))


def triangle_holonomy(cochain: Sequence[int], triangle: Sequence[int]) -> int:
    epsilon = normalize_edge_bits(cochain)
    if len(triangle) != 3 or len(set(triangle)) != 3:
        raise ValueError("triangle must contain three distinct K4 vertices")
    a, b, c = triangle
    return edge_value(epsilon, a, b) ^ edge_value(epsilon, a, c) ^ edge_value(epsilon, b, c)


def independent_holonomies(cochain: Sequence[int]) -> tuple[int, int, int]:
    epsilon = normalize_edge_bits(cochain)
    return tuple(triangle_holonomy(epsilon, triangle) for triangle in TRIANGLES[:3])  # type: ignore[return-value]


def all_triangle_holonomies(cochain: Sequence[int]) -> tuple[int, int, int, int]:
    epsilon = normalize_edge_bits(cochain)
    values = tuple(triangle_holonomy(epsilon, triangle) for triangle in TRIANGLES)
    if values[3] != (values[0] ^ values[1] ^ values[2]):
        raise AssertionError("the four K4 triangle holonomies must sum to zero")
    return values  # type: ignore[return-value]


def is_trivial_chirality_class(cochain: Sequence[int]) -> bool:
    return independent_holonomies(cochain) == (0, 0, 0)


def gauge_orbit(cochain: Sequence[int]) -> frozenset[EdgeBits]:
    epsilon = normalize_edge_bits(cochain)
    return frozenset(gauge_transform(epsilon, sigma) for sigma in product((0, 1), repeat=4))


def global_trivializations(cochain: Sequence[int]) -> tuple[VertexBits, ...]:
    """All local sign choices sigma with epsilon=delta sigma.

    The result is empty for a nontrivial holonomy class and has exactly two
    elements for a trivial class; the two solutions differ by the global flip.
    """

    epsilon = normalize_edge_bits(cochain)
    return tuple(
        normalize_vertex_bits(sigma)
        for sigma in product((0, 1), repeat=4)
        if coboundary(sigma) == epsilon
    )


def all_edge_cochains() -> Iterator[EdgeBits]:
    for values in product((0, 1), repeat=6):
        yield normalize_edge_bits(values)


def permutation_parity(permutation: Sequence[int]) -> int:
    """Parity of a tetrahedron vertex permutation: 0 even, 1 odd."""

    if sorted(permutation) != list(VERTICES):
        raise ValueError("expected a permutation of the four K4 vertices")
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(4)
        for j in range(i + 1, 4)
    )
    return inversions & 1


def transport_phase(phase: int, modulus: int, chirality_flip: int) -> int:
    """Transport a C_N phase across one handoff.

    A chirality-preserving handoff fixes the phase.  A reversing handoff acts
    by inversion k -> -k.
    """

    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 0:
        raise ValueError("modulus must be a positive integer")
    value = phase % modulus
    return value if _bit(chirality_flip) == 0 else (-value) % modulus


def inversion_fixed_phases(modulus: int) -> tuple[int, ...]:
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 0:
        raise ValueError("modulus must be a positive integer")
    return tuple(k for k in range(modulus) if (-k) % modulus == k)


def o2_multiply(left: O2State, right: O2State, modulus: int) -> O2State:
    """Finite O(2) law on C_N semidirect C2.

    (a,e)(b,f)=(a+(-1)^e b,e+f).
    """

    a, e = left
    b, f = right
    e = _bit(e)
    f = _bit(f)
    signed_b = b if e == 0 else -b
    return ((a + signed_b) % modulus, e ^ f)


def o2_inverse(state: O2State, modulus: int) -> O2State:
    angle, flip = state
    flip = _bit(flip)
    return ((-angle if flip == 0 else angle) % modulus, flip)


def is_half_turn_central(modulus: int) -> bool:
    if modulus <= 0 or modulus % 2:
        raise ValueError("half-turn centrality requires a positive even modulus")
    half_turn = (modulus // 2, 0)
    states = ((angle, flip) for angle in range(modulus) for flip in (0, 1))
    return all(
        o2_multiply(half_turn, state, modulus)
        == o2_multiply(state, half_turn, modulus)
        for state in states
    )


def exhaustive_certificate() -> dict[str, object]:
    """Exhaust all K4 sign systems and representative finite O(2) groups."""

    cochains = tuple(all_edge_cochains())
    class_counts = Counter(independent_holonomies(epsilon) for epsilon in cochains)
    orbit_sizes = {len(gauge_orbit(epsilon)) for epsilon in cochains}
    trivial_cochains = tuple(epsilon for epsilon in cochains if is_trivial_chirality_class(epsilon))
    trivialization_counts = Counter(len(global_trivializations(epsilon)) for epsilon in cochains)

    if len(cochains) != 64:
        raise AssertionError("K4 must have 64 F2 edge cochains")
    if class_counts != Counter({key: 8 for key in product((0, 1), repeat=3)}):
        raise AssertionError("triangle holonomies failed to classify eight equal gauge classes")
    if orbit_sizes != {8}:
        raise AssertionError("every K4 vertex-gauge orbit must contain eight cochains")
    if len(trivial_cochains) != 8:
        raise AssertionError("the coboundary class must contain eight cochains")
    if trivialization_counts != Counter({0: 56, 2: 8}):
        raise AssertionError("flat systems must have exactly two global signed trivializations")

    parity_counts = Counter(permutation_parity(p) for p in permutations(VERTICES))
    if parity_counts != Counter({0: 12, 1: 12}):
        raise AssertionError("tetrahedral orientations must be preserved by A4 and flipped by its odd coset")

    finite_o2 = {}
    for modulus in (6, 12, 24, 48):
        fixed = inversion_fixed_phases(modulus)
        expected = (0, modulus // 2)
        if fixed != expected:
            raise AssertionError("even cyclic inversion must fix only identity and half-turn")
        if not is_half_turn_central(modulus):
            raise AssertionError("the finite O(2) half-turn must be central")
        states = [(angle, flip) for angle in range(modulus) for flip in (0, 1)]
        for a in states:
            inverse = o2_inverse(a, modulus)
            if o2_multiply(a, inverse, modulus) != (0, 0):
                raise AssertionError("finite O(2) inverse law failed")
            for b in states:
                for c in states:
                    if o2_multiply(o2_multiply(a, b, modulus), c, modulus) != o2_multiply(
                        a, o2_multiply(b, c, modulus), modulus
                    ):
                        raise AssertionError("finite O(2) associativity failed")
        finite_o2[str(modulus)] = {
            "state_count": len(states),
            "inversion_fixed_phases": fixed,
            "half_turn_central": True,
        }

    return {
        "edge_cochains": len(cochains),
        "gauge_classes": len(class_counts),
        "cochains_per_class": sorted(set(class_counts.values())),
        "gauge_orbit_sizes": sorted(orbit_sizes),
        "trivial_holonomy_cochains": len(trivial_cochains),
        "global_trivializations_per_flat_system": 2,
        "global_orientation_torsor_size": 2,
        "tetrahedral_permutations": dict(sorted(parity_counts.items())),
        "finite_o2": finite_o2,
        "global_euler_fixed_phases": "identity and half-turn",
    }
