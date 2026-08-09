from math import comb

from enterprise_math.p022_barlow_binary_repair_boundary import (
    all_equal_cluster_radices_binary_through_dimension_two,
    equal_cluster_target,
    equal_cluster_transition_multiplicity,
    has_odd_prime_repair,
    nonbinary_equal_cluster_witness,
    path_prime_repair_signature,
    prime_signature,
)
from enterprise_math.p022_barlow_higher_channel_repair import (
    path_lift_count,
    transition_multiplicity,
)


def test_equal_positive_cluster_has_exact_binomial_transition_multiplicities() -> None:
    for dimension in range(1, 10):
        for magnitude in range(1, 5):
            previous = (magnitude,) * dimension
            for inward in range(dimension + 1):
                target = equal_cluster_target(dimension, magnitude, inward)
                expected = comb(dimension, inward)
                assert equal_cluster_transition_multiplicity(
                    dimension, magnitude, inward
                ) == expected
                assert transition_multiplicity(previous, target) == expected


def test_rank_two_is_the_only_binary_multi_channel_equal_cluster_rank() -> None:
    assert all_equal_cluster_radices_binary_through_dimension_two(1)
    assert all_equal_cluster_radices_binary_through_dimension_two(2)
    for dimension in range(3, 40):
        assert not all_equal_cluster_radices_binary_through_dimension_two(dimension)


def test_explicit_nonbinary_witness_exists_in_every_rank_at_least_three() -> None:
    assert nonbinary_equal_cluster_witness(3) == (3, 1, 3)
    for dimension in range(4, 50):
        d, inward, multiplicity = nonbinary_equal_cluster_witness(dimension)
        assert d == dimension
        assert inward == 2
        assert multiplicity == dimension * (dimension - 1) // 2
        assert multiplicity & (multiplicity - 1)


def test_rank_three_path_has_odd_prime_repair_coordinate() -> None:
    path = ((1, 1, 1), (0, 0, 2))
    assert path_lift_count(path) == 24
    assert path_prime_repair_signature(path) == ((2, 3), (3, 1))
    assert has_odd_prime_repair(path)


def test_rank_two_binary_paths_have_only_two_adic_signature() -> None:
    paths = (
        ((1, 1),),
        ((1, 1), (0, 2)),
        ((1, 1), (0, 0), (1, 1)),
    )
    for path in paths:
        signature = path_prime_repair_signature(path)
        assert all(prime == 2 for prime, _ in signature)
        assert not has_odd_prime_repair(path)


def test_prime_signature_is_exact_for_small_integers() -> None:
    expected = {
        1: (),
        2: ((2, 1),),
        6: ((2, 1), (3, 1)),
        24: ((2, 3), (3, 1)),
        60: ((2, 2), (3, 1), (5, 1)),
        256: ((2, 8),),
    }
    for value, signature in expected.items():
        assert prime_signature(value) == signature
