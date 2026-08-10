"""A primitive direction link as the ridge-adjacency shadow of the response cell.

The oriented primitive facet F_(i->j) of the A response/Voronoi cell is supported
by cut vertices S with i in S and j notin S.  For two distinct facets, common cut
vertices are counted by the compatibility of these membership requirements.

- if receiver of one is donor of the other, requirements conflict: 0 vertices;
- same receiver or same donor: 2^(N-3) shared cut vertices, a ridge-level meet;
- four distinct endpoints: 2^(N-4) shared vertices, a lower-dimensional meet.

Consequently the facet-ridge adjacency graph is exactly the primitive direction
link: e_i-e_j adjacent to e_i-e_k or e_k-e_j.  In rank three this is the
cuboctahedral dual adjacency of the rhombic-dodecahedral response cell.
"""

from __future__ import annotations

from .causal_a_voronoi_bridge import facet_cut_subsets

Direction = tuple[int, int]


def common_facet_cut_subsets(slot_count: int, left: Direction, right: Direction) -> tuple[tuple[int, ...], ...]:
    if left == right:
        return facet_cut_subsets(slot_count, *left)
    left_subsets = set(facet_cut_subsets(slot_count, *left))
    right_subsets = set(facet_cut_subsets(slot_count, *right))
    return tuple(sorted(left_subsets & right_subsets))


def common_facet_vertex_count(slot_count: int, left: Direction, right: Direction) -> int:
    return len(common_facet_cut_subsets(slot_count, left, right))


def facet_requirements_conflict(left: Direction, right: Direction) -> bool:
    receiver_left, donor_left = left
    receiver_right, donor_right = right
    return receiver_left == donor_right or receiver_right == donor_left


def direction_link_adjacent_from_response_incidence(slot_count: int, left: Direction, right: Direction) -> bool:
    if left == right or facet_requirements_conflict(left, right):
        return False
    receiver_left, donor_left = left
    receiver_right, donor_right = right
    return receiver_left == receiver_right or donor_left == donor_right


def expected_common_facet_vertex_count(slot_count: int, left: Direction, right: Direction) -> int:
    if left == right:
        return 2 ** (slot_count - 2)
    if facet_requirements_conflict(left, right):
        return 0
    if direction_link_adjacent_from_response_incidence(slot_count, left, right):
        return 2 ** max(0, slot_count - 3)
    # Feasible nonadjacent facets must have four distinct endpoints.
    return 2 ** max(0, slot_count - 4)


def response_incidence_count_identity(slot_count: int, left: Direction, right: Direction) -> bool:
    return common_facet_vertex_count(slot_count, left, right) == expected_common_facet_vertex_count(
        slot_count, left, right
    )


def response_ridge_graph_edges(slot_count: int) -> tuple[tuple[Direction, Direction], ...]:
    directions = tuple(
        (receiver, donor)
        for receiver in range(slot_count)
        for donor in range(slot_count)
        if receiver != donor
    )
    edges = []
    for index, left in enumerate(directions):
        for right in directions[index + 1:]:
            if direction_link_adjacent_from_response_incidence(slot_count, left, right):
                edges.append((left, right))
    return tuple(edges)
