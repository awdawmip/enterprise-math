"""Bridge A3 weighted relation-state algebra to A4 admissible supports.

Given positive capacities ``m_i`` and a closed A3 weighted relation field

    Z_ij = m_j*c_i - m_i*c_j,

define zero-density equivalence by ``Z_ij == 0``.  On the quotient classes,
for an integer radius ``r >= 0`` define

    [i] R_r [j]  iff  |Z_ij| <= r*m_i*m_j.

The weighted three-block closure law implies the integer triangle inequality

    m_j*|Z_ik| <= m_k*|Z_ij| + m_i*|Z_jk|,

so the induced family is identity at radius zero, monotone, and subadditive
under relational composition.  No floating-point density or hidden rational
state is required.

A3 partition coarsening has only a one-way compatibility with this support:
if every fine pair across two coarse groups satisfies the radius bound, then
the coarse pair satisfies it.  The converse can fail because signed relation
entries may cancel under ``Z'_AB = sum Z_ij``.
"""

from __future__ import annotations

from .weighted_relation_field import WeightedField, weighted_relation_field_is_closed

SupportRelation = frozenset[tuple[int, int]]
Partition = tuple[tuple[int, ...], ...]


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
        # Defensive executable check of representative independence/transitivity.
        if any(field[left][right] != 0 for left in group for right in group):
            raise AssertionError("zero relation must be transitive on a closed weighted field")
        classes.append(group)
        unseen.difference_update(group)
    return tuple(classes)


def quotient_support_relation(
    block_sizes: tuple[int, ...], field: WeightedField, radius: int
) -> SupportRelation:
    """Generate the A4 support relation induced by an A3 weighted field.

    Relation vertices are indices of ``zero_relation_classes``.  The support
    test is representative-independent; the implementation checks that fact
    across every pair of members in the two classes.
    """
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
                raise AssertionError("normalized support must be class-representative independent")
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
