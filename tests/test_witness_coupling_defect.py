from enterprise_math.witness_coupling_defect import (
    cardinality_shadow_is_exact,
    coupling_defect,
    coupling_defect_matrix,
    exact_composite_count_matrix,
    exact_matched_count,
    pair_difference_coupling_defect,
    recover_composite_from_marginals_and_defect,
    recover_matched_count_from_marginals,
)


def test_pair_difference_identity_and_exact_recovery() -> None:
    left = (0, 2, 1, 3)
    right = (4, 1, 0, 2)
    defect = coupling_defect(left, right)
    assert defect == pair_difference_coupling_defect(left, right)
    exact = exact_matched_count(left, right)
    assert recover_matched_count_from_marginals(
        len(left), sum(left), sum(right), defect
    ) == exact


def test_p021_uniform_profile_is_zero_defect() -> None:
    left = (2, 2, 2, 2)
    right = (0, 3, 1, 5)
    assert coupling_defect(left, right) == 0
    assert cardinality_shadow_is_exact(left, right)


def test_nonuniform_zero_defect_strictly_generalizes_uniformity() -> None:
    left = (0, 0, 1)
    right = (0, 2, 1)
    assert len(set(left)) > 1
    assert len(set(right)) > 1
    assert exact_matched_count(left, right) == 1
    assert sum(left) == 1
    assert sum(right) == 3
    assert coupling_defect(left, right) == 0
    assert cardinality_shadow_is_exact(left, right)


def test_same_marginals_can_have_opposite_coupling_defects() -> None:
    left = (1, 0)
    aligned = (1, 0)
    anti_aligned = (0, 1)
    assert sum(aligned) == sum(anti_aligned) == 1
    assert coupling_defect(left, aligned) == 1
    assert coupling_defect(left, anti_aligned) == -1
    assert exact_matched_count(left, aligned) == 1
    assert exact_matched_count(left, anti_aligned) == 0


def test_matrix_defect_recovers_exact_current_composite() -> None:
    left = (
        (1, 0, 2),
        (0, 3, 1),
    )
    right = (
        (2, 0),
        (1, 4),
        (0, 1),
    )
    exact = exact_composite_count_matrix(left, right)
    defect = coupling_defect_matrix(left, right)
    left_marginals = tuple(sum(row) for row in left)
    right_marginals = tuple(
        sum(right[i][target] for i in range(len(right)))
        for target in range(len(right[0]))
    )
    assert recover_composite_from_marginals_and_defect(
        len(right), left_marginals, right_marginals, defect
    ) == exact


def test_zero_defect_matrix_matches_cardinality_formula_entrywise() -> None:
    # Every left row is uniform over the middle incidences.
    left = (
        (1, 1, 1),
        (2, 2, 2),
    )
    right = (
        (0, 1),
        (3, 2),
        (1, 4),
    )
    defect = coupling_defect_matrix(left, right)
    assert defect == ((0, 0), (0, 0))
    exact = exact_composite_count_matrix(left, right)
    left_marginals = tuple(sum(row) for row in left)
    right_marginals = tuple(
        sum(right[i][target] for i in range(len(right)))
        for target in range(len(right[0]))
    )
    expected = tuple(
        tuple(left_total * right_total // len(right) for right_total in right_marginals)
        for left_total in left_marginals
    )
    assert exact == expected
