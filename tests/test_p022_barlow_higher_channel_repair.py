from collections import Counter
from itertools import permutations, product

from enterprise_math.p022_barlow_higher_channel_repair import (
    canonical_bd_chamber,
    first_rank_three_nonbinary_transition,
    path_is_binary_repair,
    path_lift_count,
    path_lift_factors,
    transition_multiplicity,
    transition_spectrum,
)
from enterprise_math.p022_barlow_two_sided_repair import (
    two_sided_microscopic_fiber_size,
    unordered_absolute_pair_history,
)


def _orbit_representatives(chamber):
    values = set()
    for permuted in set(permutations(chamber)):
        for signs in product((-1, 1), repeat=len(chamber)):
            values.add(tuple(sign * value for sign, value in zip(signs, permuted, strict=True)))
    return tuple(sorted(values))


def _direct_transition_counts(labelled_state):
    counts = Counter()
    for step in product((-1, 1), repeat=len(labelled_state)):
        target = tuple(
            value + increment
            for value, increment in zip(labelled_state, step, strict=True)
        )
        counts[canonical_bd_chamber(target)] += 1
    return counts


def test_transition_spectrum_partitions_all_microscopic_sign_steps() -> None:
    samples = (
        (0, 0),
        (0, 1),
        (1, 1),
        (0, 1, 2),
        (1, 1, 1),
        (0, 1, 1, 2),
    )
    for chamber in samples:
        spectrum = dict(transition_spectrum(chamber))
        assert sum(spectrum.values()) == 2 ** len(chamber)
        assert spectrum == _direct_transition_counts(chamber)


def test_transition_multiplicity_is_independent_of_labelled_orbit_representative() -> None:
    chambers = (
        (0, 2),
        (1, 1),
        (0, 1, 2),
        (1, 1, 2),
    )
    for chamber in chambers:
        expected = dict(transition_spectrum(chamber))
        for labelled in _orbit_representatives(chamber):
            assert _direct_transition_counts(labelled) == expected


def test_rank_two_general_formula_recovers_existing_binary_repair_exactly() -> None:
    for length in range(0, 7):
        words = tuple(product((-1, 1), repeat=length))
        for left in words:
            for right in words:
                history = unordered_absolute_pair_history(left, right)
                assert path_lift_count(history) == two_sided_microscopic_fiber_size(
                    history
                )
                assert path_is_binary_repair(history)


def test_rank_three_path_product_matches_direct_microscopic_grouping() -> None:
    dimension = 3
    for horizon in range(0, 4):
        grouped = Counter()
        for flattened_steps in product((-1, 1), repeat=dimension * horizon):
            state = [0] * dimension
            path = []
            for time in range(horizon):
                step = flattened_steps[time * dimension : (time + 1) * dimension]
                state = [
                    value + increment
                    for value, increment in zip(state, step, strict=True)
                ]
                path.append(canonical_bd_chamber(tuple(state)))
            grouped[tuple(path)] += 1

        assert sum(grouped.values()) == 2 ** (dimension * horizon)
        for path, microscopic_count in grouped.items():
            assert path_lift_count(path) == microscopic_count


def test_rank_three_has_a_genuinely_nonbinary_repair_factor() -> None:
    previous, current, multiplicity = first_rank_three_nonbinary_transition()
    assert (previous, current, multiplicity) == ((1, 1, 1), (0, 0, 2), 3)
    assert transition_multiplicity(previous, current) == 3

    path = ((1, 1, 1), (0, 0, 2))
    assert path_lift_factors(path) == (8, 3)
    assert path_lift_count(path) == 24
    assert not path_is_binary_repair(path)


def test_rank_four_already_contains_factor_six() -> None:
    previous = (0, 1, 1, 1)
    current = (0, 0, 1, 2)
    assert transition_multiplicity(previous, current) == 6
