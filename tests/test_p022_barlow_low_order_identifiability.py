from itertools import combinations
from math import isqrt

from enterprise_math.p022_barlow_collision_geometry import (
    collision_coefficients_from_selected_layers,
)
from enterprise_math.p022_barlow_low_order_identifiability import (
    CERTIFICATE_DETERMINANT_RESIDUE,
    CERTIFICATE_MODULUS,
    MAX_CERTIFIED_SEGMENT,
    certificate_determinant_residue,
    first_three_collision_coefficients_from_moments,
    identifiability_certificate_matrix,
    moment_pair_from_first_three_collisions,
    pair_moment_factor,
    p_adic_valuation,
    selected_moment_pair,
    triple_moment_factor,
    verify_bounded_identifiability_certificate,
)


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def _layers_from_segments(segments: tuple[int, ...]) -> tuple[int, ...]:
    running = 0
    layers = []
    for segment in segments:
        running += segment
        layers.append(running)
    return tuple(layers)


def _compositions(total: int, parts: int):
    for cuts in combinations(range(1, total), parts - 1):
        previous = 0
        result = []
        for cut in cuts + (total,):
            result.append(cut - previous)
            previous = cut
        yield tuple(result)


def test_certificate_modulus_is_prime_and_residue_is_nonzero() -> None:
    assert _is_prime(CERTIFICATE_MODULUS)
    assert CERTIFICATE_DETERMINANT_RESIDUE == 22
    assert certificate_determinant_residue() == 22
    assert verify_bounded_identifiability_certificate()


def test_certificate_matrix_is_exact_51_by_51() -> None:
    matrix = identifiability_certificate_matrix()
    assert len(matrix) == MAX_CERTIFIED_SEGMENT + 1 == 51
    assert all(len(row) == 51 for row in matrix)


def test_segment_moment_factors_match_direct_definitions() -> None:
    from math import comb

    for segment in range(1, MAX_CERTIFIED_SEGMENT + 1):
        assert pair_moment_factor(segment) == comb(2 * segment, segment)
        assert triple_moment_factor(segment) == sum(
            comb(segment, index) ** 3
            for index in range(segment + 1)
        )


def test_p_adic_valuation_is_exact_on_known_values() -> None:
    assert p_adic_valuation(1, 2) == 0
    assert p_adic_valuation(2**7 * 3**2, 2) == 7
    assert p_adic_valuation(2**7 * 3**2, 3) == 2
    assert p_adic_valuation(2**7 * 3**2, 5) == 0


def test_first_three_collision_transform_matches_complete_collision_polynomial() -> None:
    examples = (
        ((1,), 0),
        ((2, 2), 0),
        ((1, 3), 0),
        ((1, 2, 4), 2),
        ((3, 3, 5), 1),
    )
    for segments, tail in examples:
        pair, triple = selected_moment_pair(segments, tail)
        total_length = sum(segments) + tail
        domain = 2**total_length
        first_three = first_three_collision_coefficients_from_moments(
            domain, pair, triple
        )
        selected_layers = _layers_from_segments(segments)
        complete = collision_coefficients_from_selected_layers(
            total_length, selected_layers
        )
        expected = complete[:3] + (0,) * max(0, 3 - len(complete))
        assert first_three == expected[:3]
        assert moment_pair_from_first_three_collisions(first_three) == (
            pair,
            triple,
        )


def test_bounded_small_schedule_search_has_no_J1_J2_J3_geometry_alias() -> None:
    # The determinant certificate proves the much stronger statement through
    # segment length 50. This enumeration is only a readable regression shadow.
    for total in range(1, 13):
        seen = {}
        for parts in range(1, min(total, 6) + 1):
            for segments in _compositions(total, parts):
                multiset = tuple(sorted(segments))
                layers = _layers_from_segments(segments)
                complete = collision_coefficients_from_selected_layers(
                    total, layers
                )
                first_three = complete[:3] + (0,) * max(0, 3 - len(complete))
                signature = first_three[:3]
                if signature in seen:
                    assert seen[signature] == multiset
                else:
                    seen[signature] = multiset
