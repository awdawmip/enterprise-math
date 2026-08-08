"""Intrinsic directional focusing calculus for Enterprise Math P019.

Directions are not imported from Euclidean coordinates. They are equivalence
classes of outgoing primitive incidences under automorphisms that preserve the
directed graph, the chosen current section, and any mathematically justified
vertex marks such as causal phase.

A one-orbit result is intentionally treated as a resolution limit: a marked
structure whose stabilizer is transitive on outgoing incidences has no finer
automorphism-covariant direction information available at this level.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from collections.abc import Hashable, Iterable, Mapping, Sequence
from itertools import combinations, permutations
from math import comb

Vertex = Hashable
DirectedEdge = tuple[Vertex, Vertex]
Automorphism = Mapping[Vertex, Vertex]
Marks = Mapping[Vertex, Hashable]


def _normalized_graph(
    vertices: Iterable[Vertex], edges: Iterable[DirectedEdge]
) -> tuple[tuple[Vertex, ...], tuple[DirectedEdge, ...]]:
    vertex_tuple = tuple(vertices)
    if not vertex_tuple:
        raise ValueError("vertex set must be nonempty")
    if len(vertex_tuple) != len(set(vertex_tuple)):
        raise ValueError("vertices must be distinct")
    vertex_set = set(vertex_tuple)
    normalized: list[DirectedEdge] = []
    seen: set[DirectedEdge] = set()
    for edge in edges:
        if len(edge) != 2:
            raise ValueError("directed edges must have two endpoints")
        source, target = edge
        if source not in vertex_set or target not in vertex_set:
            raise ValueError("directed edge endpoint is outside the vertex set")
        if edge not in seen:
            seen.add(edge)
            normalized.append(edge)
    return vertex_tuple, tuple(normalized)


def _section(vertices: tuple[Vertex, ...], section: Iterable[Vertex]) -> frozenset[Vertex]:
    result = frozenset(section)
    if not result:
        raise ValueError("section must be nonempty")
    if not result.issubset(set(vertices)):
        raise ValueError("section contains a vertex outside the graph")
    return result


def _marks(vertices: tuple[Vertex, ...], marks: Marks | None) -> Marks | None:
    if marks is None:
        return None
    if set(marks.keys()) != set(vertices):
        raise ValueError("marks must label every graph vertex exactly once")
    return marks


def _phase_marks(vertices: tuple[Vertex, ...], marks: Marks) -> Marks:
    mark_map = _marks(vertices, marks)
    if mark_map is None:
        raise ValueError("phase marks are required")
    if any(value not in (-1, 0, 1) for value in mark_map.values()):
        raise ValueError("causal phase marks must lie in {-1,0,1}")
    return mark_map


def outgoing_incidences(
    vertices: Iterable[Vertex], edges: Iterable[DirectedEdge], section: Iterable[Vertex]
) -> tuple[DirectedEdge, ...]:
    """Return primitive directed incidences sourced in ``section``."""
    vertex_tuple, edge_tuple = _normalized_graph(vertices, edges)
    current = _section(vertex_tuple, section)
    return tuple(edge for edge in edge_tuple if edge[0] in current)


def is_section_automorphism(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
    mapping: Automorphism,
    marks: Marks | None = None,
) -> bool:
    """Return whether a map preserves graph, section, and optional vertex marks."""
    vertex_tuple, edge_tuple = _normalized_graph(vertices, edges)
    current = _section(vertex_tuple, section)
    mark_map = _marks(vertex_tuple, marks)
    vertex_set = set(vertex_tuple)
    if set(mapping.keys()) != vertex_set or set(mapping.values()) != vertex_set:
        return False
    edge_set = set(edge_tuple)
    mapped_edges = {(mapping[u], mapping[v]) for u, v in edge_tuple}
    if mapped_edges != edge_set or {mapping[v] for v in current} != set(current):
        return False
    if mark_map is not None and any(mark_map[mapping[v]] != mark_map[v] for v in vertex_tuple):
        return False
    return True


def section_stabilizer_automorphisms(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
    marks: Marks | None = None,
) -> tuple[dict[Vertex, Vertex], ...]:
    """Enumerate the full marked-section stabilizer for small finite graphs.

    This factorial reference implementation is deliberately bounded to at most
    eight vertices. Larger research graphs should supply an externally proved
    automorphism family to ``incidence_orbits`` rather than use brute force.
    """
    vertex_tuple, edge_tuple = _normalized_graph(vertices, edges)
    current = _section(vertex_tuple, section)
    mark_map = _marks(vertex_tuple, marks)
    if len(vertex_tuple) > 8:
        raise ValueError("reference automorphism enumeration is limited to eight vertices")
    result: list[dict[Vertex, Vertex]] = []
    for image_tuple in permutations(vertex_tuple):
        mapping = dict(zip(vertex_tuple, image_tuple, strict=True))
        if is_section_automorphism(vertex_tuple, edge_tuple, current, mapping, mark_map):
            result.append(mapping)
    return tuple(result)


def incidence_orbits(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
    automorphisms: Sequence[Automorphism] | None = None,
    marks: Marks | None = None,
) -> tuple[frozenset[DirectedEdge], ...]:
    """Partition outgoing incidences into marked-section stabilizer orbits."""
    vertex_tuple, edge_tuple = _normalized_graph(vertices, edges)
    current = _section(vertex_tuple, section)
    mark_map = _marks(vertex_tuple, marks)
    incidences = outgoing_incidences(vertex_tuple, edge_tuple, current)
    family: Sequence[Automorphism]
    if automorphisms is None:
        family = section_stabilizer_automorphisms(
            vertex_tuple, edge_tuple, current, mark_map
        )
    else:
        family = automorphisms
        if not family:
            raise ValueError("automorphism family must be nonempty")
        if any(
            not is_section_automorphism(
                vertex_tuple, edge_tuple, current, mapping, mark_map
            )
            for mapping in family
        ):
            raise ValueError(
                "every supplied mapping must preserve graph, section, and marks"
            )

    unseen = set(incidences)
    orbits: list[frozenset[DirectedEdge]] = []
    while unseen:
        seed = next(iter(unseen))
        orbit = {(mapping[seed[0]], mapping[seed[1]]) for mapping in family}
        changed = True
        while changed:
            changed = False
            expanded = {
                (mapping[u], mapping[v])
                for u, v in orbit
                for mapping in family
            }
            if not expanded.issubset(orbit):
                orbit |= expanded
                changed = True
        orbit &= set(incidences)
        if not orbit:
            raise AssertionError("automorphism orbit cannot be empty")
        orbits.append(frozenset(orbit))
        unseen -= orbit
    return tuple(
        sorted(orbits, key=lambda item: (len(item), repr(sorted(item, key=repr))))
    )


def causal_phase_role(edge: DirectedEdge, phase_marks: Marks) -> tuple[int, int]:
    """Return the coordinate-free causal role ``(phase(source), phase(target))``."""
    source, target = edge
    if source not in phase_marks or target not in phase_marks:
        raise ValueError("causal phase marks must cover edge endpoints")
    left = phase_marks[source]
    right = phase_marks[target]
    if left not in (-1, 0, 1) or right not in (-1, 0, 1):
        raise ValueError("causal phase marks must lie in {-1,0,1}")
    return int(left), int(right)


def causal_role_channels(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
    phase_marks: Marks,
) -> dict[tuple[int, int], tuple[DirectedEdge, ...]]:
    """Group outgoing incidences by exact causal phase transition role."""
    vertex_tuple, edge_tuple = _normalized_graph(vertices, edges)
    current = _section(vertex_tuple, section)
    marks = _phase_marks(vertex_tuple, phase_marks)
    grouped: defaultdict[tuple[int, int], list[DirectedEdge]] = defaultdict(list)
    for edge in outgoing_incidences(vertex_tuple, edge_tuple, current):
        grouped[causal_phase_role(edge, marks)].append(edge)
    return {role: tuple(channel) for role, channel in sorted(grouped.items())}


def orbit_causal_phase_role(
    orbit: Iterable[DirectedEdge], phase_marks: Marks
) -> tuple[int, int]:
    """Return the unique causal role of a phase-preserving automorphism orbit.

    A marked automorphism orbit must lie entirely inside one exact phase-role
    channel. The helper raises if an externally supplied orbit violates that
    structural requirement.
    """
    edges = tuple(orbit)
    if not edges:
        raise ValueError("orbit must be nonempty")
    roles = {causal_phase_role(edge, phase_marks) for edge in edges}
    if len(roles) != 1:
        raise ValueError("one marked direction orbit cannot mix causal phase roles")
    return next(iter(roles))


def phase_marked_direction_roles(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
    phase_marks: Marks,
) -> tuple[dict[str, object], ...]:
    """Resolve phase-preserving direction orbits and attach causal roles.

    This is the Stage-9 bridge from the existing phase/boundary layer to the
    Stage-8 intrinsic direction layer. Multiple automorphism orbits may share
    the same causal role; a causal role is therefore a coarse structural label,
    not a complete direction identifier.
    """
    vertex_tuple, edge_tuple = _normalized_graph(vertices, edges)
    current = _section(vertex_tuple, section)
    marks = _phase_marks(vertex_tuple, phase_marks)
    orbits = incidence_orbits(vertex_tuple, edge_tuple, current, marks=marks)
    return tuple(
        {
            "role": orbit_causal_phase_role(orbit, marks),
            "orbit": orbit,
            "data": directional_channel_data(orbit),
        }
        for orbit in orbits
    )


def channel_multiplicities(channel: Iterable[DirectedEdge]) -> Counter[Vertex]:
    """Return future-target multiplicities inside one intrinsic direction channel."""
    edges = tuple(dict.fromkeys(channel))
    if not edges:
        raise ValueError("direction channel must be nonempty")
    return Counter(target for _, target in edges)


def directional_channel_data(channel: Iterable[DirectedEdge]) -> dict[str, object]:
    """Return integer branching/focusing data for one direction channel."""
    edges = tuple(dict.fromkeys(channel))
    multiplicities = channel_multiplicities(edges)
    incidence_count = len(edges)
    target_count = len(multiplicities)
    collision = incidence_count - target_count
    spectrum = tuple(
        sum(comb(multiplicity, order) for multiplicity in multiplicities.values())
        for order in range(1, max(multiplicities.values()) + 1)
    )
    return {
        "incidences": incidence_count,
        "targets": target_count,
        "collision_excess": collision,
        "spectrum": spectrum,
        "multiplicities": dict(multiplicities),
    }


def cross_channel_pair_collision(
    first: Iterable[DirectedEdge], second: Iterable[DirectedEdge]
) -> int:
    """Count cross-channel incidence pairs landing on the same future target."""
    first_counts = channel_multiplicities(first)
    second_counts = channel_multiplicities(second)
    return sum(
        first_counts[target] * second_counts[target]
        for target in first_counts.keys() | second_counts.keys()
    )


def pair_collision_channel_decomposition(
    channels: Iterable[Iterable[DirectedEdge]],
) -> dict[str, object]:
    """Decompose total J2 into within-channel and cross-channel pair collisions."""
    channel_tuple = tuple(tuple(dict.fromkeys(channel)) for channel in channels)
    if not channel_tuple or any(not channel for channel in channel_tuple):
        raise ValueError("channels must be nonempty")
    flattened = [edge for channel in channel_tuple for edge in channel]
    if len(flattened) != len(set(flattened)):
        raise ValueError("direction channels must be disjoint")
    total_counts = Counter(target for _, target in flattened)
    total_j2 = sum(comb(value, 2) for value in total_counts.values())
    internal = tuple(
        sum(
            comb(value, 2)
            for value in channel_multiplicities(channel).values()
        )
        for channel in channel_tuple
    )
    cross = {
        (left, right): cross_channel_pair_collision(
            channel_tuple[left], channel_tuple[right]
        )
        for left, right in combinations(range(len(channel_tuple)), 2)
    }
    if total_j2 != sum(internal) + sum(cross.values()):
        raise AssertionError("pair-collision channel decomposition failed")
    return {"total_j2": total_j2, "internal_j2": internal, "cross_j2": cross}


def collision_rate_anisotropy_numerator(
    channels: Iterable[Iterable[DirectedEdge]],
) -> int:
    """Return a fraction-free anisotropy witness for directional collision rates.

    For channel i let E_i be incidence count and C_i its collision excess. The
    witness is sum_{i<j}(E_j*C_i-E_i*C_j)^2. It vanishes exactly when all
    resolved channel collision rates C_i/E_i are equal, without storing
    fractions.

    Zero is only isotropy relative to the supplied intrinsic direction
    resolution. A one-orbit partition gives zero vacuously and is a resolution
    no-go, not proof of physical isotropy.
    """
    data = tuple(directional_channel_data(channel) for channel in channels)
    if not data:
        raise ValueError("channels must be nonempty")
    total = 0
    for left, right in combinations(data, 2):
        e_left = int(left["incidences"])
        e_right = int(right["incidences"])
        c_left = int(left["collision_excess"])
        c_right = int(right["collision_excess"])
        defect = e_right * c_left - e_left * c_right
        total += defect * defect
    return total


def direction_resolution_no_go(channels: Iterable[Iterable[DirectedEdge]]) -> bool:
    """Return True when intrinsic automorphism resolution yields only one channel."""
    channel_tuple = tuple(tuple(channel) for channel in channels)
    if not channel_tuple:
        raise ValueError("channels must be nonempty")
    return len(channel_tuple) == 1
