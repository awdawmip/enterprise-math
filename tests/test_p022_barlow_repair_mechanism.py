from collections import Counter
from itertools import product

from enterprise_math.p022_barlow_repair_mechanism import (
    diagonal_repair_coefficients,
    evaluate_mechanism_polynomial,
    first_mechanism_alias,
    mechanism_aliases_at_total_repair,
    mechanism_load_identities,
    mechanism_polynomial_terms,
)
from enterprise_math.p022_barlow_repair_polynomial import (
    coordination_history_image_size,
    repair_polynomial_coefficients,
)
from enterprise_math.p022_barlow_two_sided_repair import (
    diagonal_split_count,
    total_zero_departure_events,
    unordered_absolute_pair_history,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def _direct_mechanism_distribution(length: int):
    histories = {}
    words = _words(length)
    for left in words:
        for right in words:
            history = unordered_absolute_pair_history(left, right)
            histories.setdefault(history, None)
    counts = Counter()
    for history in histories:
        counts[(total_zero_departure_events(history), diagonal_split_count(history))] += 1
    return counts


def test_bivariate_terms_match_direct_distinct_history_grouping() -> None:
    for length in range(0, 7):
        direct = _direct_mechanism_distribution(length)
        closed = Counter(
            {
                (orientation, split): count
                for orientation, split, count in mechanism_polynomial_terms(length)
            }
        )
        assert closed == direct


def test_diagonal_specialization_is_exact_original_repair_polynomial() -> None:
    for length in range(0, 25):
        assert diagonal_repair_coefficients(
            length
        ) == repair_polynomial_coefficients(length)


def test_basic_evaluations_recover_image_and_microscopic_domain() -> None:
    for length in range(0, 20):
        terms = mechanism_polynomial_terms(length)
        assert evaluate_mechanism_polynomial(terms, 1, 1) == (
            coordination_history_image_size(length)
        )
        assert evaluate_mechanism_polynomial(terms, 2, 2) == 4**length


def test_partial_mechanism_loads_match_independent_event_totals() -> None:
    for length in range(0, 18):
        orientation, split = mechanism_load_identities(length)
        assert orientation[0] == orientation[1]
        assert split[0] == split[1]


def test_first_mechanism_alias_is_length_three_repair_four() -> None:
    length, repair, values = first_mechanism_alias()
    assert length == 3
    assert repair == 4
    assert set(values) == {(4, 0, 1), (3, 1, 2)}

    assert mechanism_aliases_at_total_repair(1) == ()
    assert mechanism_aliases_at_total_repair(2) == ()
    assert dict(mechanism_aliases_at_total_repair(3))[4] == values


def test_same_total_repair_can_hide_multiple_mechanism_types() -> None:
    for length in range(3, 10):
        aliases = mechanism_aliases_at_total_repair(length)
        assert aliases
        for repair, values in aliases:
            assert len(values) >= 2
            assert all(orientation + split == repair for orientation, split, _ in values)


def test_univariate_coefficient_is_sum_of_bivariate_alias_counts() -> None:
    for length in range(0, 20):
        coefficients = repair_polynomial_coefficients(length)
        grouped = Counter()
        for orientation, split, count in mechanism_polynomial_terms(length):
            grouped[orientation + split] += count
        assert tuple(
            grouped.get(repair, 0) for repair in range(len(coefficients))
        ) == coefficients
