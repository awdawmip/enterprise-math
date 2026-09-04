"""Exact cube frame cover, tetrahedral path holonomy, and return kernel.

The checker joins two already separated readouts of one finite eight-state
object:

* the C2 frame cover of the four-slice K4 connection;
* the eight sign directions of the BCC return walk.

All calculations use integers and ``Fraction`` matrices.  No floating point,
trigonometry, or numerical value of pi is used.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial
from typing import Iterable, Iterator, Sequence

from enterprise_math.euler_o2_chirality_globalization import (
    EDGES,
    all_edge_cochains,
    independent_holonomies,
)
from enterprise_math.euler_tetrahedral_holonomy import (
    NORMALS,
    Mat3,
    expected_face_holonomy,
    identity_matrix,
    mat_mul,
    shortest_rotation,
)

CubeCode = tuple[int, int, int]
FrameState = tuple[int, int]


def cube_code(slice_index: int, sheet: int) -> CubeCode:
    """Encode one slice and one central half-turn sheet by a cube vertex.

    The sign triple is a combinatorial frame-phase code.  It is not a claim
    that one shortest SO(3) edge transport sends ``n_u`` to ``-n_v``.
    """

    if slice_index not in range(4):
        raise ValueError("slice_index must be 0,1,2,3")
    if sheet not in (0, 1):
        raise ValueError("sheet must be a C2 bit")
    sign = 1 if sheet == 0 else -1
    normal = NORMALS[slice_index]
    return sign * normal[0], sign * normal[1], sign * normal[2]


def all_frame_states() -> tuple[FrameState, ...]:
    return tuple((slice_index, sheet) for slice_index in range(4) for sheet in (0, 1))


def all_cube_codes() -> frozenset[CubeCode]:
    return frozenset(cube_code(*state) for state in all_frame_states())


def hamming_distance(left: CubeCode, right: CubeCode) -> int:
    return sum(a != b for a, b in zip(left, right))


def lifted_adjacent(left: FrameState, right: FrameState) -> bool:
    """Bipartite double-cover edge: change slice and toggle frame sheet."""

    return left[0] != right[0] and left[1] != right[1]


def frame_cover_edges() -> frozenset[frozenset[CubeCode]]:
    edges: set[frozenset[CubeCode]] = set()
    states = all_frame_states()
    for i, left in enumerate(states):
        for right in states[i + 1 :]:
            if lifted_adjacent(left, right):
                edges.add(frozenset((cube_code(*left), cube_code(*right))))
    return frozenset(edges)


def standard_cube_edges() -> frozenset[frozenset[CubeCode]]:
    vertices = tuple(product((-1, 1), repeat=3))
    return frozenset(
        frozenset((left, right))
        for index, left in enumerate(vertices)
        for right in vertices[index + 1 :]
        if hamming_distance(left, right) == 1
    )


def deck_partner(state: FrameState) -> FrameState:
    return state[0], state[1] ^ 1


def lift_slice_path(path: Sequence[int], initial_sheet: int = 0) -> tuple[FrameState, ...]:
    if not path:
        raise ValueError("a slice path must be nonempty")
    if initial_sheet not in (0, 1):
        raise ValueError("initial_sheet must be a C2 bit")
    if any(vertex not in range(4) for vertex in path):
        raise ValueError("slice labels must be 0,1,2,3")
    if any(left == right for left, right in zip(path, path[1:])):
        raise ValueError("consecutive slice labels must be distinct")
    return tuple((vertex, initial_sheet ^ (index & 1)) for index, vertex in enumerate(path))


def path_transport(path: Sequence[int]) -> Mat3:
    """Ordered product T_(v_(m-1),v_m)...T_(v_0,v_1)."""

    if not path:
        raise ValueError("a slice path must be nonempty")
    if any(vertex not in range(4) for vertex in path):
        raise ValueError("slice labels must be 0,1,2,3")
    if any(left == right for left, right in zip(path, path[1:])):
        raise ValueError("consecutive slice labels must be distinct")
    result = identity_matrix()
    for source, target in zip(path, path[1:]):
        result = mat_mul(shortest_rotation(source, target), result)
    return result


def involution_power(matrix: Mat3, exponent: int) -> Mat3:
    if exponent < 0:
        raise ValueError("exponent must be nonnegative")
    return identity_matrix() if exponent % 2 == 0 else matrix


def predicted_path_transport(path: Sequence[int]) -> Mat3:
    if not path:
        raise ValueError("a slice path must be nonempty")
    edge_count = len(path) - 1
    start = path[0]
    end = path[-1]
    half_turn = expected_face_holonomy(start)
    if end == start:
        return involution_power(half_turn, edge_count)
    return mat_mul(
        shortest_rotation(start, end),
        involution_power(half_turn, edge_count - 1),
    )


def verify_path_transport(path: Sequence[int]) -> Mat3:
    actual = path_transport(path)
    predicted = predicted_path_transport(path)
    if actual != predicted:
        raise AssertionError(f"endpoint/parity transport theorem failed for {tuple(path)}")
    lifted = lift_slice_path(path)
    expected_sheet = (len(path) - 1) & 1
    if lifted[-1][1] != expected_sheet:
        raise AssertionError("frame-cover path parity failed")
    if path[-1] == path[0]:
        same_sheet = lifted[-1] == lifted[0]
        if same_sheet != ((len(path) - 1) % 2 == 0):
            raise AssertionError("closed path sheet criterion failed")
    return actual


def iter_slice_paths(edge_count: int) -> Iterator[tuple[int, ...]]:
    if edge_count < 0:
        raise ValueError("edge_count must be nonnegative")
    for start in range(4):
        paths = [(start,)]
        for _ in range(edge_count):
            paths = [path + (next_vertex,) for path in paths for next_vertex in range(4) if next_vertex != path[-1]]
        yield from paths


def permute_edge_cochain(cochain: Sequence[int], permutation: Sequence[int]) -> tuple[int, ...]:
    if len(cochain) != 6 or any(bit not in (0, 1) for bit in cochain):
        raise ValueError("cochain must have six F2 bits")
    if sorted(permutation) != [0, 1, 2, 3]:
        raise ValueError("permutation must permute the four slices")
    edge_index = {edge: index for index, edge in enumerate(EDGES)}
    result = [0] * 6
    for (source, target), bit in zip(EDGES, cochain):
        image = tuple(sorted((permutation[source], permutation[target])))
        result[edge_index[image]] = bit
    return tuple(result)


def s4_fixed_holonomy_classes() -> frozenset[tuple[int, int, int]]:
    representatives: dict[tuple[int, int, int], tuple[int, ...]] = {}
    for cochain in all_edge_cochains():
        representatives.setdefault(independent_holonomies(cochain), cochain)
    fixed = {
        code
        for code, representative in representatives.items()
        if all(
            independent_holonomies(permute_edge_cochain(representative, permutation)) == code
            for permutation in permutations(range(4))
        )
    }
    return frozenset(fixed)


def central_parity_cochain() -> tuple[int, ...]:
    return (1, 1, 1, 1, 1, 1)


def central_parity_holonomy_code() -> tuple[int, int, int]:
    return independent_holonomies(central_parity_cochain())


def cube_steps() -> tuple[CubeCode, ...]:
    return tuple(product((-1, 1), repeat=3))


def bcc_return_count(half_length: int) -> int:
    """Return words of length 2n in the eight sign-step alphabet."""

    if isinstance(half_length, bool) or not isinstance(half_length, int) or half_length < 0:
        raise ValueError("half_length must be a nonnegative integer")
    return comb(2 * half_length, half_length) ** 3


def bcc_return_count_dynamic(half_length: int) -> int:
    if isinstance(half_length, bool) or not isinstance(half_length, int) or half_length < 0:
        raise ValueError("half_length must be a nonnegative integer")
    positions: Counter[tuple[int, int, int]] = Counter({(0, 0, 0): 1})
    for _ in range(2 * half_length):
        following: Counter[tuple[int, int, int]] = Counter()
        for position, count in positions.items():
            for step in cube_steps():
                following[(position[0] + step[0], position[1] + step[1], position[2] + step[2])] += count
        positions = following
    return positions[(0, 0, 0)]


def half_pochhammer_ratio(n: int) -> Fraction:
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    value = Fraction(1)
    for index in range(n):
        value *= Fraction(2 * index + 1, 2 * (index + 1))
    return value


def bcc_return_probability(n: int) -> Fraction:
    return Fraction(bcc_return_count(n), 8 ** (2 * n))


def ramanujan_signature_half_coefficient(n: int) -> Fraction:
    ratio = half_pochhammer_ratio(n)
    return ratio**3


def exhaustive_certificate(max_path_edges: int = 9, max_return_n: int = 5) -> dict[str, object]:
    codes = all_cube_codes()
    if codes != frozenset(product((-1, 1), repeat=3)):
        raise AssertionError("the eight frame states must encode every cube vertex")
    if frame_cover_edges() != standard_cube_edges():
        raise AssertionError("the K4 frame double cover must be the cube graph")
    for state in all_frame_states():
        left = cube_code(*state)
        right = cube_code(*deck_partner(state))
        if right != tuple(-coordinate for coordinate in left):
            raise AssertionError("the deck involution must be the cube antipode")

    paths_checked = 0
    closed_even = closed_odd = 0
    for edge_count in range(max_path_edges + 1):
        for path in iter_slice_paths(edge_count):
            verify_path_transport(path)
            paths_checked += 1
            if path[-1] == path[0]:
                if edge_count % 2:
                    closed_odd += 1
                else:
                    closed_even += 1

    fixed_classes = s4_fixed_holonomy_classes()
    if fixed_classes != frozenset(((0, 0, 0), (1, 1, 1))):
        raise AssertionError("there must be a unique nonzero S4-fixed F2 class")
    if central_parity_holonomy_code() != (1, 1, 1):
        raise AssertionError("the all-edge parity cochain must evaluate to one on every face")

    return_checks = {}
    for n in range(max_return_n + 1):
        formula = bcc_return_count(n)
        dynamic = bcc_return_count_dynamic(n)
        probability = bcc_return_probability(n)
        coefficient = ramanujan_signature_half_coefficient(n)
        if formula != dynamic:
            raise AssertionError("BCC dynamic return count disagrees with the product formula")
        if probability != coefficient:
            raise AssertionError("return probability disagrees with the signature-1/2 coefficient")
        if half_pochhammer_ratio(n) != Fraction(comb(2 * n, n), 4**n):
            raise AssertionError("half-Pochhammer ratio disagrees with the central binomial ratio")
        return_checks[str(n)] = {
            "steps": 2 * n,
            "return_words": formula,
            "probability": str(probability),
        }

    return {
        "frame_states": 8,
        "cube_vertices": len(codes),
        "cube_edges": len(frame_cover_edges()),
        "paths_checked": paths_checked,
        "maximum_path_edge_count": max_path_edges,
        "closed_even_paths_checked": closed_even,
        "closed_odd_paths_checked": closed_odd,
        "closed_path_rule": "even -> identity; odd -> tangent half-turn",
        "s4_fixed_holonomy_classes": sorted(fixed_classes),
        "unique_nonzero_s4_fixed_class": (1, 1, 1),
        "return_checks": return_checks,
        "ramanujan_kernel": "((1/2)_n/n!)^3",
    }
