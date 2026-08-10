from enterprise_math.p022_barlow_franel_integer_companion import (
    companion_casoratian,
    companion_transfer_determinant,
    forced_zero_offsets_from_integer_companion,
    integer_companion_matches_rational,
    integer_companion_reconstructs_zero_digits,
    integer_companion_scale,
    midpoint_integer_companion,
    zero_digits_from_integer_companion,
)


def test_integer_companion_first_values_and_rational_normalization() -> None:
    expected = (
        0,
        1,
        -29,
        3925,
        -1_138_025,
        586_364_625,
        -470_774_258_325,
        543_690_942_446_925,
        -854_053_932_715_790_625,
    )
    assert tuple(midpoint_integer_companion(d) for d in range(len(expected))) == expected
    for d in range(18):
        assert integer_companion_matches_rational(d)


def test_integer_scale_is_exact_and_positive() -> None:
    assert integer_companion_scale(0) == 1
    assert integer_companion_scale(1) == 1
    assert integer_companion_scale(2) == 72
    assert integer_companion_scale(3) == 14_400
    for d in range(1, 12):
        assert integer_companion_scale(d) > 0


def test_integer_companion_reconstructs_forced_zero_alphabets() -> None:
    for prime in (5, 7, 13, 23, 29, 47, 53, 71, 101, 157, 167, 173, 191):
        assert integer_companion_reconstructs_zero_digits(prime)

    assert forced_zero_offsets_from_integer_companion(29) == (2,)
    assert zero_digits_from_integer_companion(29) == (12, 14, 16)
    assert forced_zero_offsets_from_integer_companion(157) == (3, 62)
    assert zero_digits_from_integer_companion(157) == (16, 75, 78, 81, 140)
    assert forced_zero_offsets_from_integer_companion(173) == (82,)
    assert zero_digits_from_integer_companion(173) == (4, 86, 168)


def test_transfer_determinant_and_casoratian_product() -> None:
    product = 1
    assert companion_casoratian(0) == 1
    for step in range(1, 12):
        product *= companion_transfer_determinant(step)
        assert companion_casoratian(step) == product


def test_casoratian_matches_two_independent_integer_solutions() -> None:
    # H has initial data (0,1).  K has initial data (1,0) under the same recurrence.
    h = [0, 1]
    k = [1, 0]
    for d in range(1, 11):
        h.append(-(28 * d * d + 1) * h[d] + 8 * (2 * d - 1) ** 4 * h[d - 1])
        k.append(-(28 * d * d + 1) * k[d] + 8 * (2 * d - 1) ** 4 * k[d - 1])
        casoratian = h[d + 1] * k[d] - h[d] * k[d + 1]
        assert casoratian == companion_casoratian(d)
