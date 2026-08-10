from enterprise_math.p022_barlow_zero_alphabet_quotient import (
    finite_free_column_classification_holds,
    primitive_source_is_in_defect_rowspace,
    right_half_twin_zero_digits,
    zero_alphabet_free_digits,
)


def test_q41_abstract_kernel_is_exactly_the_right_half_twin_axis() -> None:
    assert zero_alphabet_free_digits(41) == (30,)
    assert right_half_twin_zero_digits(41) == (30,)
    assert finite_free_column_classification_holds(41)
    assert primitive_source_is_in_defect_rowspace(41)


def test_larger_known_free_axes_are_the_same_geometric_type() -> None:
    expected = {
        521: (321,),
        2111: (1884,),
        2417: (1629,),
        2557: (1629,),
        2731: (1764,),
        2819: (1485,),
        3187: (2115,),
        3433: (2121,),
        4019: (2721,),
    }
    for prime, free in expected.items():
        assert zero_alphabet_free_digits(prime) == free
        assert right_half_twin_zero_digits(prime) == free
        assert finite_free_column_classification_holds(prime)
        assert primitive_source_is_in_defect_rowspace(prime)


def test_full_rank_examples_have_no_unexplained_kernel() -> None:
    for prime in (13, 29, 59, 67, 73, 149, 157, 179, 337, 937):
        assert zero_alphabet_free_digits(prime) == ()
        assert right_half_twin_zero_digits(prime) == ()
        assert finite_free_column_classification_holds(prime)
        assert primitive_source_is_in_defect_rowspace(prime)
