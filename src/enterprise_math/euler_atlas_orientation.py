"""Exact K4 atlas-orientation obstruction and A4-reduction checker.

The six overlap parities of a four-chart tetrahedral atlas form an F2-valued
1-cochain. Vertex chart relabelings act by coboundaries. The three independent
triangle holonomies are complete coordinates on H^1(K4,F2), and their
vanishing is equivalent to a constructive reduction of all transition
permutations from S4 to A4.
"""

from __future__ import annotations

from itertools import permutations, product
from typing import Mapping, Sequence

Edge = tuple[int, int]
Permutation4 = tuple[int, int, int, int]

EDGES: tuple[Edge, ...] = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
IDENTITY4: Permutation4 = (0, 1, 2, 3)
ODD_GAUGE4: Permutation4 = (1, 0, 2, 3)


def _require_bits(values: Sequence[int], expected_length: int, name: str) -> None:
    if len(values) != expected_length or any(bit not in (0, 1) for bit in values):
        raise ValueError(f"{name} must contain exactly {expected_length} bits")


def permutation_sign(permutation: Sequence[int]) -> int:
    if sorted(permutation) != list(range(len(permutation))):
        raise ValueError("not a permutation")
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def parity_bit(permutation: Sequence[int]) -> int:
    return 0 if permutation_sign(permutation) == 1 else 1


def compose(after: Permutation4, before: Permutation4) -> Permutation4:
    """Function composition `after o before`."""

    if sorted(after) != list(range(4)) or sorted(before) != list(range(4)):
        raise ValueError("both arguments must be permutations of four labels")
    return tuple(after[before[index]] for index in range(4))  # type: ignore[return-value]


def inverse(permutation: Permutation4) -> Permutation4:
    if sorted(permutation) != list(range(4)):
        raise ValueError("not a permutation of four labels")
    result = [0, 0, 0, 0]
    for index, image in enumerate(permutation):
        result[image] = index
    return tuple(result)  # type: ignore[return-value]


def edge_bits_from_mapping(mapping: Mapping[Edge, int]) -> tuple[int, ...]:
    try:
        result = tuple(mapping[edge] for edge in EDGES)
    except KeyError as exc:
        raise ValueError(f"missing edge {exc.args[0]}") from exc
    _require_bits(result, 6, "edge mapping")
    return result


def triangle_holonomies(edge_bits: Sequence[int]) -> tuple[int, int, int]:
    """Independent triangle parities for triangles 012, 013, and 023."""

    _require_bits(edge_bits, 6, "edge_bits")
    e01, e02, e03, e12, e13, e23 = edge_bits
    return e01 ^ e12 ^ e02, e01 ^ e13 ^ e03, e02 ^ e23 ^ e03


def fourth_triangle_holonomy(edge_bits: Sequence[int]) -> int:
    _require_bits(edge_bits, 6, "edge_bits")
    _, _, _, e12, e13, e23 = edge_bits
    return e12 ^ e23 ^ e13


def vertex_gauge(edge_bits: Sequence[int], vertex_bits: Sequence[int]) -> tuple[int, ...]:
    _require_bits(edge_bits, 6, "edge_bits")
    _require_bits(vertex_bits, 4, "vertex_bits")
    return tuple(
        bit ^ vertex_bits[left] ^ vertex_bits[right]
        for bit, (left, right) in zip(edge_bits, EDGES)
    )


def reduction_gauge(edge_bits: Sequence[int]) -> tuple[int, int, int, int] | None:
    """Construct a gauge clearing all edges iff the orientation class vanishes."""

    _require_bits(edge_bits, 6, "edge_bits")
    if triangle_holonomies(edge_bits) != (0, 0, 0):
        return None
    e01, e02, e03, _, _, _ = edge_bits
    gauge = (0, e01, e02, e03)
    if vertex_gauge(edge_bits, gauge) != (0, 0, 0, 0, 0, 0):
        raise AssertionError("constructive A4-reduction gauge failed")
    return gauge


def gauges_clearing(edge_bits: Sequence[int]) -> tuple[tuple[int, int, int, int], ...]:
    _require_bits(edge_bits, 6, "edge_bits")
    return tuple(
        gauge
        for gauge in product((0, 1), repeat=4)
        if vertex_gauge(edge_bits, gauge) == (0, 0, 0, 0, 0, 0)
    )


def orientation_class_count() -> int:
    classes: dict[tuple[int, int, int], list[tuple[int, ...]]] = {}
    for edge_bits in product((0, 1), repeat=6):
        invariant = triangle_holonomies(edge_bits)
        classes.setdefault(invariant, []).append(edge_bits)
        for gauge in product((0, 1), repeat=4):
            if triangle_holonomies(vertex_gauge(edge_bits, gauge)) != invariant:
                raise AssertionError("triangle holonomy changed under vertex gauge")
    if len(classes) != 8 or any(len(members) != 8 for members in classes.values()):
        raise AssertionError("unexpected H1(K4,F2) orbit structure")
    return len(classes)


def transition_parity_bits(
    transitions: Mapping[Edge, Permutation4],
) -> tuple[int, ...]:
    try:
        return tuple(parity_bit(transitions[edge]) for edge in EDGES)
    except KeyError as exc:
        raise ValueError(f"missing transition on edge {exc.args[0]}") from exc


def apply_vertex_relabeling(
    transitions: Mapping[Edge, Permutation4],
    vertex_bits: Sequence[int],
) -> dict[Edge, Permutation4]:
    """Apply g'_uv = h_v o g_uv o h_u^{-1} using one fixed odd h when bit=1."""

    _require_bits(vertex_bits, 4, "vertex_bits")
    relabelings = tuple(ODD_GAUGE4 if bit else IDENTITY4 for bit in vertex_bits)
    adjusted: dict[Edge, Permutation4] = {}
    for left, right in EDGES:
        if (left, right) not in transitions:
            raise ValueError(f"missing transition on edge {(left, right)}")
        adjusted[(left, right)] = compose(
            relabelings[right],
            compose(transitions[(left, right)], inverse(relabelings[left])),
        )
    expected = vertex_gauge(transition_parity_bits(transitions), vertex_bits)
    actual = transition_parity_bits(adjusted)
    if actual != expected:
        raise AssertionError("permutation relabeling did not realize the F2 gauge law")
    return adjusted


def reduce_transitions_to_a4(
    transitions: Mapping[Edge, Permutation4],
) -> tuple[dict[Edge, Permutation4], tuple[int, int, int, int]] | None:
    bits = transition_parity_bits(transitions)
    gauge = reduction_gauge(bits)
    if gauge is None:
        return None
    adjusted = apply_vertex_relabeling(transitions, gauge)
    if any(permutation_sign(item) != 1 for item in adjusted.values()):
        raise AssertionError("orientation reduction did not land in A4")
    return adjusted, gauge


def all_permutations4() -> tuple[Permutation4, ...]:
    return tuple(permutations(range(4)))  # type: ignore[return-value]


def atlas_orientation_certificate() -> dict[str, object]:
    if orientation_class_count() != 8:
        raise AssertionError("orientation class count failed")

    flat_patterns = []
    nonflat_patterns = []
    for bits in product((0, 1), repeat=6):
        gauge = reduction_gauge(bits)
        if gauge is None:
            nonflat_patterns.append(bits)
        else:
            flat_patterns.append(bits)
            clearers = gauges_clearing(bits)
            if len(clearers) != 2:
                raise AssertionError("flat gauge was not unique up to one global bit")
            if tuple(bit ^ 1 for bit in clearers[0]) != clearers[1]:
                raise AssertionError("two clearing gauges were not global reversals")
        h0, h1, h2 = triangle_holonomies(bits)
        if fourth_triangle_holonomy(bits) != (h0 ^ h1 ^ h2):
            raise AssertionError("dependent fourth triangle relation failed")

    if len(flat_patterns) != 8 or len(nonflat_patterns) != 56:
        raise AssertionError("unexpected flat/nonflat orientation pattern count")

    permutations4 = all_permutations4()
    even = [item for item in permutations4 if parity_bit(item) == 0]
    odd = [item for item in permutations4 if parity_bit(item) == 1]
    if len(even) != 12 or len(odd) != 12:
        raise AssertionError("S4 parity split failed")

    for bits in product((0, 1), repeat=6):
        transitions = {
            edge: (ODD_GAUGE4 if bit else IDENTITY4)
            for edge, bit in zip(EDGES, bits)
        }
        reduced = reduce_transitions_to_a4(transitions)
        if (reduced is not None) != (triangle_holonomies(bits) == (0, 0, 0)):
            raise AssertionError("S4-to-A4 reduction criterion failed")

    return {
        "edge_cochains": 64,
        "vertex_gauges": 16,
        "effective_gauge_orbit_size": 8,
        "orientation_classes": 8,
        "flat_patterns": 8,
        "nonflat_patterns": 56,
        "independent_triangle_tests": 3,
        "flat_clearing_gauges_per_pattern": 2,
        "coherent_J_ambiguity": "one global reversal",
        "s4_even_permutations": 12,
        "s4_odd_permutations": 12,
        "a4_reduction_criterion": "all three independent triangle parities vanish",
        "status": "PASS",
    }


if __name__ == "__main__":
    import json

    print(json.dumps(atlas_orientation_certificate(), indent=2, sort_keys=True))
