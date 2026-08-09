from enterprise_math.equitable_count_quotient import (
    block_total_matrix,
    family_is_equitable,
    is_equitable,
    matrix_product,
    quotient_count_matrix,
    quotient_word,
    quotient_word_is_exact,
    recover_quotient_from_block_totals,
)
from enterprise_math.witness_coupling_defect import coupling_defect


PARTITION = ((0, 1), (2, 3))


def test_equitable_matrix_has_exact_block_count_quotient() -> None:
    matrix = (
        (1, 0, 2, 0),
        (0, 1, 0, 2),
        (3, 0, 1, 0),
        (0, 3, 0, 1),
    )
    assert is_equitable(matrix, PARTITION)
    assert quotient_count_matrix(matrix, PARTITION) == ((1, 2), (3, 1))


def test_equitable_matrices_are_closed_under_product() -> None:
    left = (
        (1, 0, 2, 0),
        (0, 1, 0, 2),
        (3, 0, 1, 0),
        (0, 3, 0, 1),
    )
    right = (
        (2, 0, 1, 0),
        (0, 2, 0, 1),
        (1, 0, 0, 2),
        (0, 1, 2, 0),
    )
    assert family_is_equitable((left, right), PARTITION)
    product = matrix_product(left, right)
    assert is_equitable(product, PARTITION)
    assert quotient_count_matrix(product, PARTITION) == matrix_product(
        quotient_count_matrix(left, PARTITION),
        quotient_count_matrix(right, PARTITION),
    )
    assert quotient_word_is_exact((left, right), PARTITION)


def test_long_equitable_operation_word_closes_on_quotients() -> None:
    first = (
        (1, 0, 1, 1),
        (0, 1, 2, 0),
        (1, 1, 1, 0),
        (2, 0, 0, 1),
    )
    second = (
        (2, 0, 0, 1),
        (0, 2, 1, 0),
        (1, 0, 1, 1),
        (0, 1, 2, 0),
    )
    # Check the intended block sums before relying on the word theorem.
    assert is_equitable(first, PARTITION)
    assert is_equitable(second, PARTITION)
    word = (first, second, first, first, second)
    assert quotient_word_is_exact(word, PARTITION)
    assert quotient_word(word, PARTITION) == (
        (355, 288),
        (432, 355),
    )


def test_block_totals_recover_quotient_when_equitable() -> None:
    matrix = (
        (1, 0, 2, 0),
        (0, 1, 0, 2),
        (3, 0, 1, 0),
        (0, 3, 0, 1),
    )
    totals = block_total_matrix(matrix, PARTITION)
    assert totals == ((2, 4), (6, 2))
    assert recover_quotient_from_block_totals(totals, (2, 2)) == (
        (1, 2),
        (3, 1),
    )


def test_non_equitable_partition_fails_at_one_step() -> None:
    matrix = (
        (1, 0, 2, 0),
        (0, 1, 1, 0),  # target-cell sum is 1 instead of 2
        (3, 0, 1, 0),
        (0, 3, 0, 1),
    )
    assert not is_equitable(matrix, PARTITION)


def test_local_zero_coupling_defect_does_not_imply_equitable_future_algebra() -> None:
    # The selected scalar join is exact by Delta=0 even though both profiles
    # are non-uniform.  A richer target-block observation can still distinguish
    # the exact middle identities.
    left_profile = (0, 0, 1)
    right_profile = (0, 2, 1)
    assert coupling_defect(left_profile, right_profile) == 0

    # Put all three exact middle states into one proposed coarse cell.  Their
    # outgoing counts to two target cells are visibly different, so identity
    # cannot be erased for the whole block-count language.
    matrix = (
        (0, 0, 0, 0, 0),
        (0, 0, 0, 2, 0),
        (0, 0, 0, 0, 1),
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0),
    )
    partition = ((0, 1, 2), (3, 4))
    assert not is_equitable(matrix, partition)
