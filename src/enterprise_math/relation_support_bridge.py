"""Bridge A3 weighted relation-state algebra to A4 admissible supports.

Given positive capacities ``m_i`` and a closed A3 weighted relation field

    Z_ij = m_j*c_i - m_i*c_j,

define zero-density equivalence by ``Z_ij == 0``. On the quotient classes,
for an integer radius ``r >= 0`` define

    [i] R_r [j] iff |Z_ij| <= r*m_i*m_j.

The weighted three-block closure law implies the integer triangle inequality

    m_j*|Z_ik| <= m_k*|Z_ij| + m_i*|Z_jk|,

so the induced family is identity at radius zero, monotone, and subadditive
under relational composition. No floating-point density or hidden rational
state is required.

A3 partition coarsening has only a one-way compatibility with this support:
if every fine pair across two coarse groups satisfies the radius bound, then
the coarse pair satisfies it. The converse can fail because signed relation
entries may cancel under ``Z'_AB = sum Z_ij``.

For this generated symmetric family, A4 common-target composition is simply
``R_r ; R_s``. Equality with ``R_(r+s)`` is therefore an interpolation
property of the A3 zero-relation quotient.

The support filtration also induces a canonical integer metric

    rho(i,j) = min {r : i R_r j}
             = ceil(|Z_ij| / (m_i*m_j)),

computed by exact ceiling division. Global A4 split-completeness is equivalent
to this metric being the shortest-path metric of its radius-one support graph.
"""

from __future__ import annotations

from collections import deque

from .weighted_relation_field import WeightedField, weighted_relation_field_is_closed

SupportRelation = frozenset[tuple[int, int]]
Partition = tuple[tuple[int, ...], ...]
DistanceMatrix = tuple[tuple[int, ...], ...]
GraphDistanceMatrix = tuple[tuple[int | None, ...], ...]


def _require_radius(radius: int) -> None:
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")


def zero_relation_classes(
    block_sizes: tuple[int, ...], field: WeightedField
) -> tuple[tuple[int, ...], ...]:
    """Return canonical classes for i~j iff Z_ij=0.

    Closedness and positive capacities make this an equivalence relation.
    Classes are ordered by their smallest member.
    """
    if not weighted_relation_field_is_closed(block_sizes, field):
        raise ValueError("weighted relation field must be closed")
    unseen = set(range(len(block_sizes)))
    classes: list[tuple[int, ...]] = []
    while unseen:
        seed = min(unseen)
        group = tuple(index for index in sorted(unseen) if field[seed][index] == 0)
        if any(field[left][right] != 0 for left in group for right in group):
            raise AssertionError("zero relation must be transitive on a closed weighted field")
        classes.append(group)
        unseen.difference_update(group)
    return tuple(classes)


def quotient_support_relation(
    block_sizes: tuple[int, ...], field: WeightedField, radius: int
) -> SupportRelation:
    """Generate the A4 support relation induced by an A3 weighted field."""
    _require_radius(radius)
    classes = zero_relation_classes(block_sizes, field)
    relation: set[tuple[int, int]] = set()
    for left_class, left_members in enumerate(classes):
        for right_class, right_members in enumerate(classes):
            decisions = {
                abs(field[i][j]) <= radius * block_sizes[i] * block_sizes[j]
                for i in left_members
                for j in right_members
            }
            if len(decisions) != 1:
                raise AssertionError(
                    "normalized support must be class-representative independent"
                )
            if True in decisions:
                relation.add((left_class, right_class))
    return frozenset(relation)


def compose_support(left: SupportRelation, right: SupportRelation) -> SupportRelation:
    """Finite relational composition on quotient-class indices."""
    right_by_source: dict[int, set[int]] = {}
    for source, target in right:
        right_by_source.setdefault(source, set()).add(target)
    return frozenset(
        (source, target)
        for source, middle in left
        for target in right_by_source.get(middle, ())
    )


def support_family_is_admissible(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    max_radius: int,
) -> bool:
    """Executable audit of identity, monotonicity, and subadditivity."""
    _require_radius(max_radius)
    classes = zero_relation_classes(block_sizes, field)
    family = tuple(
        quotient_support_relation(block_sizes, field, radius)
        for radius in range(max_radius + 1)
    )
    identity = frozenset((index, index) for index in range(len(classes)))
    if family[0] != identity:
        return False
    for radius in range(max_radius + 1):
        for larger in range(radius, max_radius + 1):
            if not family[radius].issubset(family[larger]):
                return False
    for left_radius in range(max_radius + 1):
        for right_radius in range(max_radius + 1 - left_radius):
            if not compose_support(
                family[left_radius], family[right_radius]
            ).issubset(family[left_radius + right_radius]):
                return False
    return True


def common_target_support(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    left_radius: int,
    right_radius: int,
) -> SupportRelation:
    """A4 common-target relation for the symmetric A3-generated family."""
    left = quotient_support_relation(block_sizes, field, left_radius)
    right = quotient_support_relation(block_sizes, field, right_radius)
    return compose_support(left, right)


def split_complete_at(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    left_radius: int,
    right_radius: int,
) -> bool:
    """Check whether every combined-budget pair has an actual intermediate class.

    This is exactly ``R_left ; R_right == R_(left+right)`` for the generated
    symmetric support family.
    """
    _require_radius(left_radius)
    _require_radius(right_radius)
    return common_target_support(
        block_sizes, field, left_radius, right_radius
    ) == quotient_support_relation(
        block_sizes, field, left_radius + right_radius
    )


def missing_interpolations(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    left_radius: int,
    right_radius: int,
) -> SupportRelation:
    """Return endpoint pairs inside total budget but lacking a split witness."""
    _require_radius(left_radius)
    _require_radius(right_radius)
    combined = quotient_support_relation(
        block_sizes, field, left_radius + right_radius
    )
    witnessed = common_target_support(
        block_sizes, field, left_radius, right_radius
    )
    return frozenset(combined.difference(witnessed))


def integer_relation_distance_matrix(
    block_sizes: tuple[int, ...], field: WeightedField
) -> DistanceMatrix:
    """Return rho=ceil(|Z_ij|/(m_i*m_j)) on zero-relation classes.

    The implementation remains integer-only. Representative independence is
    checked across every raw member pair of each quotient-class pair.
    """
    classes = zero_relation_classes(block_sizes, field)
    rows: list[tuple[int, ...]] = []
    for left_members in classes:
        row: list[int] = []
        for right_members in classes:
            distances = set()
            for i in left_members:
                for j in right_members:
                    denominator = block_sizes[i] * block_sizes[j]
                    numerator = abs(field[i][j])
                    distances.add((numerator + denominator - 1) // denominator)
            if len(distances) != 1:
                raise AssertionError(
                    "integer relation distance must be representative independent"
                )
            row.append(next(iter(distances)))
        rows.append(tuple(row))
    return tuple(rows)


def unit_graph_shortest_distances(
    block_sizes: tuple[int, ...], field: WeightedField
) -> GraphDistanceMatrix:
    """Shortest-path distances in the rho=1 graph; None represents infinity."""
    metric = integer_relation_distance_matrix(block_sizes, field)
    size = len(metric)
    adjacency = tuple(
        tuple(j for j in range(size) if j != i and metric[i][j] == 1)
        for i in range(size)
    )
    result: list[tuple[int | None, ...]] = []
    for source in range(size):
        distances: list[int | None] = [None] * size
        distances[source] = 0
        queue: deque[int] = deque([source])
        while queue:
            current = queue.popleft()
            current_distance = distances[current]
            if current_distance is None:
                raise AssertionError("visited graph vertex must have a distance")
            for target in adjacency[current]:
                if distances[target] is None:
                    distances[target] = current_distance + 1
                    queue.append(target)
        result.append(tuple(distances))
    return tuple(result)


def geodesic_defect_matrix(
    block_sizes: tuple[int, ...], field: WeightedField
) -> GraphDistanceMatrix:
    """Return d_G1-rho; None means the unit graph disconnects the pair."""
    metric = integer_relation_distance_matrix(block_sizes, field)
    graph = unit_graph_shortest_distances(block_sizes, field)
    defects: list[tuple[int | None, ...]] = []
    for i in range(len(metric)):
        row: list[int | None] = []
        for j in range(len(metric)):
            graph_distance = graph[i][j]
            if graph_distance is None:
                row.append(None)
                continue
            if graph_distance < metric[i][j]:
                raise AssertionError("unit graph path cannot beat the direct metric")
            row.append(graph_distance - metric[i][j])
        defects.append(tuple(row))
    return tuple(defects)


def unit_graph_realizes_integer_metric(
    block_sizes: tuple[int, ...], field: WeightedField
) -> bool:
    """Audit B08: rho equals the intrinsic shortest-path metric of R_1."""
    metric = integer_relation_distance_matrix(block_sizes, field)
    graph = unit_graph_shortest_distances(block_sizes, field)
    return all(graph[i][j] == metric[i][j] for i in range(len(metric)) for j in range(len(metric)))


def all_cross_pairs_supported(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    left_group: tuple[int, ...],
    right_group: tuple[int, ...],
    radius: int,
) -> bool:
    """Check the strong fine condition used by the quotient compatibility theorem."""
    _require_radius(radius)
    return all(
        abs(field[i][j]) <= radius * block_sizes[i] * block_sizes[j]
        for i in left_group
        for j in right_group
    )


def coarse_pair_supported_from_partition(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    left_group: tuple[int, ...],
    right_group: tuple[int, ...],
    radius: int,
) -> bool:
    """Evaluate the induced radius bound after aggregating two fine groups."""
    _require_radius(radius)
    left_size = sum(block_sizes[i] for i in left_group)
    right_size = sum(block_sizes[j] for j in right_group)
    coarse_relation = sum(field[i][j] for i in left_group for j in right_group)
    return abs(coarse_relation) <= radius * left_size * right_size


def universal_fine_support_implies_coarse_support(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    left_group: tuple[int, ...],
    right_group: tuple[int, ...],
    radius: int,
) -> bool:
    """Audit the one-way A3 quotient -> A4 support compatibility statement."""
    if not all_cross_pairs_supported(
        block_sizes, field, left_group, right_group, radius
    ):
        return True
    return coarse_pair_supported_from_partition(
        block_sizes, field, left_group, right_group, radius
    )
