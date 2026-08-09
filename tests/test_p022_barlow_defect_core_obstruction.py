from enterprise_math.p022_barlow_defect_core_obstruction import (
    OBSTRUCTION_ROW_PRIME,
    core_times_obstruction_vector_150,
    exceptional_null_support_150,
    exceptional_prime_null_vector_150,
    obstruction_support_size_150,
    obstruction_vector_by_defect_150,
    primitive_obstruction_vector_150,
)
from enterprise_math.p022_barlow_defect_core_compression import (
    compressed_core_defect_labels_150,
    compressed_core_row_primes_150,
)
from enterprise_math.p022_barlow_defect_core_smith import (
    CORE_EXCEPTIONAL_PRIMES,
    CORE_EXACT_DETERMINANT,
)


def test_primitive_obstruction_has_expected_support_and_gcd_one() -> None:
    vector = primitive_obstruction_vector_150()
    assert len(vector) == 40
    assert obstruction_support_size_150() == 34
    sparse = obstruction_vector_by_defect_150()
    assert sparse[:4] == ((5, -15041), (8, 31564), (11, 5723), (13, 3205))
    assert sparse[-3:] == ((134, -13311), (149, 6561), (150, -6750))


def test_exact_near_kernel_equation_is_concentrated_on_prime_269_row() -> None:
    output = core_times_obstruction_vector_150()
    row_primes = compressed_core_row_primes_150()
    assert row_primes[17] == OBSTRUCTION_ROW_PRIME == 269
    assert output[17] == CORE_EXACT_DETERMINANT == -26622
    assert all(value == 0 for index, value in enumerate(output) if index != 17)


def test_each_exceptional_prime_has_same_integer_obstruction_direction() -> None:
    labels = compressed_core_defect_labels_150()
    for prime in CORE_EXCEPTIONAL_PRIMES:
        vector = exceptional_prime_null_vector_150(prime)
        assert len(vector) == len(labels) == 40
        assert any(vector)
        assert exceptional_null_support_150(prime) == tuple(
            label
            for label, coefficient in zip(labels, vector, strict=True)
            if coefficient
        )


def test_17_and_29_exceptional_null_supports_coincide() -> None:
    assert exceptional_null_support_150(17) == exceptional_null_support_150(29)
    assert len(exceptional_null_support_150(17)) == 30


def test_two_and_three_have_their_own_reduced_supports() -> None:
    support_two = exceptional_null_support_150(2)
    support_three = exceptional_null_support_150(3)
    assert support_two != support_three
    assert support_two != exceptional_null_support_150(17)
    assert support_three != exceptional_null_support_150(17)
