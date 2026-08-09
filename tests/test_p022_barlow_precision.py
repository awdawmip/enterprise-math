from itertools import product

from enterprise_math.p022_barlow_precision import (
    barlow_prefix_normal_form,
    counts_from_length_and_imbalance,
    recover_imbalance_from_vertical_polynomial,
    recover_upward_sign_word_from_full_trajectory,
    selected_layer_imbalance_state,
    target_layer_polynomial_matches_scalar_state,
    vertical_polynomial_from_imbalance,
    vertical_polynomial_moments,
)
from enterprise_math.p022_barlow_stacking import (
    stacking_prefix_counts,
    stacking_prefix_imbalance,
    vertical_witness_polynomial,
)


def test_counts_and_normal_form_are_exact_integer_coordinates() -> None:
    assert counts_from_length_and_imbalance(4, 0) == (2, 2)
    assert counts_from_length_and_imbalance(5, -3) == (4, 1)
    assert counts_from_length_and_imbalance(5, 3) == (1, 4)

    assert barlow_prefix_normal_form((-1, 1), 4) == (2, 0, 0)
    assert barlow_prefix_normal_form((-1,), 4) == (0, -1, 4)
    assert barlow_prefix_normal_form((-1, -1, 1), 6) == (2, -1, 2)


def test_vertical_polynomial_reconstructs_from_imbalance_for_many_patterns() -> None:
    for length in range(1, 6):
        for pattern in product((-1, 1), repeat=length):
            for target_layer in range(-7, 8):
                assert target_layer_polynomial_matches_scalar_state(
                    tuple(pattern), target_layer
                )


def test_first_moment_recovers_imbalance_exactly() -> None:
    for length in range(1, 6):
        for pattern in product((-1, 1), repeat=length):
            pattern = tuple(pattern)
            for target_layer in range(-6, 7):
                polynomial = vertical_witness_polynomial(pattern, target_layer)
                expected = stacking_prefix_imbalance(pattern, target_layer)
                recovered = recover_imbalance_from_vertical_polynomial(
                    polynomial, abs(target_layer)
                )
                assert recovered == expected

                mass, q_moment, r_moment = vertical_polynomial_moments(polynomial)
                assert mass == 3 ** abs(target_layer)
                assert q_moment == r_moment


def test_different_order_same_selected_layer_state_has_same_polynomial() -> None:
    first = (-1, -1, 1, 1)
    second = (-1, 1, -1, 1)
    target_layer = 4
    assert selected_layer_imbalance_state(first, (target_layer,)) == (0,)
    assert selected_layer_imbalance_state(second, (target_layer,)) == (0,)
    assert vertical_witness_polynomial(
        first, target_layer
    ) == vertical_witness_polynomial(second, target_layer)


def test_selected_layer_vector_distinguishes_only_queried_prefixes() -> None:
    first = (-1, -1, 1, 1)
    second = (-1, 1, -1, 1)

    assert selected_layer_imbalance_state(first, (4,)) == selected_layer_imbalance_state(
        second, (4,)
    )
    assert selected_layer_imbalance_state(first, (2, 4)) != selected_layer_imbalance_state(
        second, (2, 4)
    )

    # At the selected layer four, the entire vertical coefficient state agrees.
    assert vertical_polynomial_from_imbalance(4, 0) == vertical_witness_polynomial(
        first, 4
    )


def test_full_prefix_imbalance_trajectory_is_equivalent_to_stacking_word() -> None:
    for word_length in range(1, 8):
        for word in product((-1, 1), repeat=word_length):
            word = tuple(word)
            trajectory = tuple(
                stacking_prefix_imbalance(word, layer)
                for layer in range(1, word_length + 1)
            )
            assert recover_upward_sign_word_from_full_trajectory(trajectory) == word


def test_fixed_layer_polynomial_determines_imbalance_so_scalar_state_is_minimal() -> None:
    # Exhaustively group all length-six stacking words by their layer-six
    # vertical witness polynomial.  Every polynomial fiber has one and only one
    # imbalance.  Conversely, all words with the same imbalance share the same
    # polynomial.  This is the finite executable shadow of the first-moment
    # minimality proof.
    fibers = {}
    for word in product((-1, 1), repeat=6):
        word = tuple(word)
        polynomial = tuple(sorted(vertical_witness_polynomial(word, 6).items()))
        imbalance = stacking_prefix_imbalance(word, 6)
        fibers.setdefault(polynomial, set()).add(imbalance)
    assert all(len(values) == 1 for values in fibers.values())

    by_imbalance = {}
    for word in product((-1, 1), repeat=6):
        word = tuple(word)
        imbalance = stacking_prefix_imbalance(word, 6)
        polynomial = tuple(sorted(vertical_witness_polynomial(word, 6).items()))
        by_imbalance.setdefault(imbalance, set()).add(polynomial)
    assert all(len(values) == 1 for values in by_imbalance.values())


def test_length_and_imbalance_recover_prefix_counts() -> None:
    for word_length in range(1, 8):
        for word in product((-1, 1), repeat=word_length):
            word = tuple(word)
            minus_count, plus_count = stacking_prefix_counts(word, word_length)
            imbalance = stacking_prefix_imbalance(word, word_length)
            assert counts_from_length_and_imbalance(
                word_length, imbalance
            ) == (minus_count, plus_count)
