from enterprise_math.p022_barlow_coordination_fibers import (
    admissible_absolute_imbalances,
    deficit_from_absolute_imbalances,
    deficit_representation_pairs,
    maximum_shell_cardinality,
    odd_deficit_sum_of_odd_squares,
    possible_shell_cardinality_deficits,
    possible_shell_drift_energies,
    shell_cardinality_deficit,
    shell_cardinality_from_energy,
)


def test_deficit_formula_relabels_every_represented_shell_state() -> None:
    for radius in range(0, 30):
        values = admissible_absolute_imbalances(radius)
        direct = set()
        for left in values:
            for right in values:
                energy = left * left + right * right
                shell = shell_cardinality_from_energy(radius, energy)
                deficit = shell_cardinality_deficit(radius, shell)
                assert deficit == deficit_from_absolute_imbalances(
                    radius, left, right
                )
                direct.add(deficit)
        assert possible_shell_cardinality_deficits(radius) == tuple(sorted(direct))


def test_even_radius_deficits_are_bounded_sums_of_two_squares() -> None:
    for radius in range(0, 30, 2):
        bound = radius // 2
        expected = {
            left * left + right * right
            for left in range(bound + 1)
            for right in range(bound + 1)
        }
        assert set(possible_shell_cardinality_deficits(radius)) == expected
        for deficit in expected:
            pairs = deficit_representation_pairs(radius, deficit)
            assert pairs
            assert all(left * left + right * right == deficit for left, right in pairs)


def test_odd_radius_deficits_are_bounded_sums_of_two_pronic_numbers() -> None:
    for radius in range(1, 30, 2):
        bound = radius // 2
        expected = {
            left * (left + 1) + right * (right + 1)
            for left in range(bound + 1)
            for right in range(bound + 1)
        }
        assert set(possible_shell_cardinality_deficits(radius)) == expected
        for deficit in expected:
            pairs = deficit_representation_pairs(radius, deficit)
            assert pairs
            odd_square_energy = odd_deficit_sum_of_odd_squares(radius, deficit)
            assert all(
                (2 * left + 1) ** 2 + (2 * right + 1) ** 2
                == odd_square_energy
                for left, right in pairs
            )


def test_arithmetic_holes_appear_in_shell_cardinality_image() -> None:
    # Even radius four already has missing deficits inside the numerical
    # interval: represented deficits are 0,1,2,4,5,8.
    assert possible_shell_cardinality_deficits(4) == (0, 1, 2, 4, 5, 8)
    assert 3 not in possible_shell_cardinality_deficits(4)

    # Odd radius five has only even pronic-sum deficits and also additional
    # holes inside that even range.  Here 8 is represented (2+6); 10 is not.
    deficits = possible_shell_cardinality_deficits(5)
    assert all(deficit % 2 == 0 for deficit in deficits)
    assert 8 in deficits
    assert 10 not in deficits


def test_multiple_arithmetic_representations_can_merge_drift_allocations() -> None:
    # First odd-radius nontrivial collision of unordered magnitude pairs:
    # 50=1^2+7^2=5^2+5^2 at radius seven. In deficit coordinates the same
    # shell state is represented by (u,v)=(0,3),(3,0),(2,2).
    radius = 7
    energy = 50
    shell = shell_cardinality_from_energy(radius, energy)
    deficit = shell_cardinality_deficit(radius, shell)
    assert deficit == (maximum_shell_cardinality(radius) - shell)
    pairs = set(deficit_representation_pairs(radius, deficit))
    assert {(0, 3), (3, 0), (2, 2)}.issubset(pairs)


def test_energy_and_deficit_images_have_equal_cardinality() -> None:
    for radius in range(0, 30):
        assert len(possible_shell_drift_energies(radius)) == len(
            possible_shell_cardinality_deficits(radius)
        )
