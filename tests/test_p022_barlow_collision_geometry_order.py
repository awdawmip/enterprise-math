from itertools import permutations

from enterprise_math.p022_barlow_collision_geometry import (
    balanced_order_repair_count,
    collision_coefficients_from_selected_layers,
    ordered_checkpoint_geometry_fiber_size_from_collision_coefficients,
    ordered_segment_realization_count,
)


def _layers(segments):
    running = 0
    output = []
    for segment in segments:
        running += segment
        output.append(running)
    return tuple(output)


def test_multiset_permutation_formula_matches_direct_distinct_orders() -> None:
    samples = (
        (),
        (1,),
        (1, 1, 1),
        (1, 2, 3),
        (2, 2, 3, 3, 3),
        (1, 2, 2, 4, 4, 5),
    )
    for segments in samples:
        expected = len(set(permutations(segments))) if segments else 1
        assert ordered_segment_realization_count(segments) == expected


def test_complete_collision_polynomial_fiber_is_exactly_segment_order() -> None:
    segment_multisets = (
        (1, 2, 3),
        (1, 1, 2, 3),
        (2, 2, 3, 3),
        (1, 2, 2, 4),
    )
    for multiset in segment_multisets:
        length = sum(multiset)
        polynomials = {}
        for ordered in set(permutations(multiset)):
            layers = _layers(ordered)
            coefficients = collision_coefficients_from_selected_layers(length, layers)
            polynomials.setdefault(coefficients, 0)
            polynomials[coefficients] += 1
        assert len(polynomials) == 1
        coefficients, observed_count = next(iter(polynomials.items()))
        assert observed_count == ordered_segment_realization_count(multiset)
        assert ordered_checkpoint_geometry_fiber_size_from_collision_coefficients(
            coefficients
        ) == observed_count


def test_balanced_schedule_order_repair_is_binomial() -> None:
    for length in range(1, 30):
        for checkpoints in range(1, length + 1):
            q, r = divmod(length, checkpoints)
            multiset = (q,) * (checkpoints - r) + (q + 1,) * r
            assert ordered_segment_realization_count(multiset) == balanced_order_repair_count(
                length, checkpoints
            )


def test_all_equal_segments_have_no_residual_order_ambiguity() -> None:
    for checkpoints in range(1, 10):
        for segment_length in range(1, 8):
            multiset = (segment_length,) * checkpoints
            assert ordered_segment_realization_count(multiset) == 1


def test_all_distinct_segments_have_factorial_order_ambiguity() -> None:
    from math import factorial

    for count in range(1, 9):
        multiset = tuple(range(1, count + 1))
        assert ordered_segment_realization_count(multiset) == factorial(count)
