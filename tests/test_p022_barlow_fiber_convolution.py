from collections import Counter
from itertools import combinations, product
from math import comb

from enterprise_math.p022_barlow_fiber_convolution import (
    multiplicative_profile_convolution,
    profile_character_product_identity,
    profile_collision_count,
    profile_domain_size,
    profile_from_segments,
    profile_from_selected_layers,
    profile_power_moment,
    recover_segment_multiset_from_profile,
    recover_selected_geometry_from_profile,
    segment_binomial_fiber_profile,
    segment_minimal_nontrivial_multiplicity,
)
from enterprise_math.p022_barlow_higher_collision_precision import (
    ordered_equal_observation_tuple_count,
    selected_collision_count,
)
from enterprise_math.p022_barlow_precision_fibers import (
    selected_layer_observation,
    selected_segment_lengths,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def _direct_profile(length: int, selected_layers: tuple[int, ...]):
    fibers: dict[tuple[int, ...], int] = {}
    for word in _words(length):
        observed = selected_layer_observation(word, selected_layers)
        fibers[observed] = fibers.get(observed, 0) + 1
    return tuple(sorted(Counter(fibers.values()).items()))


def _compositions(length: int, parts: int):
    for cuts in combinations(range(1, length), parts - 1):
        previous = 0
        result = []
        for cut in cuts + (length,):
            result.append(cut - previous)
            previous = cut
        yield tuple(result)


def _selected_layer_sets(length: int):
    yield ()
    for count in range(1, min(length, 5) + 1):
        for layers in combinations(range(1, length + 1), count):
            yield tuple(layers)


def test_one_segment_profile_is_binomial_row_size_distribution() -> None:
    for length in range(1, 12):
        direct = Counter(comb(length, index) for index in range(length + 1))
        profile = segment_binomial_fiber_profile(length)
        assert profile == tuple(sorted(direct.items()))
        assert dict(profile)[1] == 2
        if length >= 2:
            assert min(size for size, _ in profile if size > 1) == length
            assert dict(profile)[length] == segment_minimal_nontrivial_multiplicity(
                length
            )


def test_multiplicative_convolution_matches_direct_segment_products() -> None:
    for left_length in range(1, 7):
        for right_length in range(1, 7):
            left = segment_binomial_fiber_profile(left_length)
            right = segment_binomial_fiber_profile(right_length)
            convolved = multiplicative_profile_convolution(left, right)
            direct = Counter(
                comb(left_length, i) * comb(right_length, j)
                for i in range(left_length + 1)
                for j in range(right_length + 1)
            )
            assert convolved == tuple(sorted(direct.items()))


def test_selected_layer_profile_matches_direct_microscopic_enumeration() -> None:
    for length in range(0, 8):
        schedules = [()]
        if length:
            schedules.extend(
                [
                    (length,),
                    tuple(range(1, length + 1)),
                    tuple(range(2, length + 1, 2)),
                ]
            )
        for selected_layers in schedules:
            profile = profile_from_selected_layers(length, selected_layers)
            assert profile == _direct_profile(length, selected_layers)
            assert profile_domain_size(profile) == 2 ** length


def test_power_moments_are_exact_multiplicative_characters() -> None:
    for left_length in range(1, 6):
        for right_length in range(1, 6):
            left = segment_binomial_fiber_profile(left_length)
            right = segment_binomial_fiber_profile(right_length)
            for order in range(1, 8):
                lhs, rhs = profile_character_product_identity(left, right, order)
                assert lhs == rhs


def test_profile_moments_and_collisions_match_higher_collision_layer() -> None:
    for length in range(0, 9):
        schedules = [()]
        if length:
            schedules.extend(
                [
                    (length,),
                    tuple(range(1, length + 1)),
                    tuple(range(2, length + 1, 2)),
                ]
            )
        for selected_layers in schedules:
            profile = profile_from_selected_layers(length, selected_layers)
            for order in range(1, 8):
                assert profile_power_moment(
                    profile, order
                ) == ordered_equal_observation_tuple_count(
                    length, selected_layers, order
                )
                assert profile_collision_count(
                    profile, order
                ) == selected_collision_count(length, selected_layers, order)


def test_segment_order_is_the_only_lost_geometry_in_complete_final_profile() -> None:
    assert profile_from_segments((1, 2, 3, 4)) == profile_from_segments((4, 2, 1, 3))
    assert recover_segment_multiset_from_profile(
        profile_from_segments((4, 2, 1, 3))
    ) == (1, 2, 3, 4)


def test_complete_profile_recovers_segment_multiset_for_all_small_compositions() -> None:
    for length in range(1, 16):
        for parts in range(1, min(length, 7) + 1):
            for segments in _compositions(length, parts):
                profile = profile_from_segments(segments)
                assert recover_segment_multiset_from_profile(
                    profile
                ) == tuple(sorted(segments))


def test_complete_profile_recovers_selected_segment_multiset_and_hidden_tail() -> None:
    for length in range(0, 11):
        for selected_layers in _selected_layer_sets(length):
            profile = profile_from_selected_layers(length, selected_layers)
            segments, tail = selected_segment_lengths(length, selected_layers)
            recovered_segments, recovered_tail = recover_selected_geometry_from_profile(
                profile
            )
            assert recovered_segments == tuple(sorted(segments))
            assert recovered_tail == tail
            assert sum(recovered_segments) + recovered_tail == length


def test_no_checkpoint_profile_is_identified_as_pure_hidden_tail() -> None:
    for length in range(0, 12):
        profile = profile_from_selected_layers(length, ())
        assert recover_selected_geometry_from_profile(profile) == ((), length)
