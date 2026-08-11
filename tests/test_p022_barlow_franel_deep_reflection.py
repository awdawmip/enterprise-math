from enterprise_math.p022_barlow_franel_deep_reflection import (
    deep_reflected_pair_iff_multiple_root,
    deep_zero_reflection_split,
    digit_root_is_multiple,
)
from enterprise_math.p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    triple_moment_factor,
)


def test_q67_deep_digit_is_transverse_and_reflects_to_a_simple_zero() -> None:
    # F_23 has q-adic depth two at q=67, while its Jarvis--Verrill mirror 43
    # has depth one.  This is the smallest known regression separating
    # "deep" from the genuinely harder multiple-root/deep-mirror locus.
    assert p_adic_valuation(triple_moment_factor(23), 67) == 2
    assert p_adic_valuation(triple_moment_factor(43), 67) == 1
    branch, mirror, derivative, mirror_depth = deep_zero_reflection_split(67, 23)
    assert branch == "simple-mirror"
    assert mirror == 43
    assert derivative != 0
    assert mirror_depth == 1
    assert not digit_root_is_multiple(67, 23)
    assert not deep_reflected_pair_iff_multiple_root(67, 23)


def test_small_digit_roots_are_transverse_in_distinguishing_examples() -> None:
    # These examples include primitive, reflected and midpoint zeros.  This is
    # bounded evidence only; the universal multiple-root exclusion remains a
    # separate arithmetic frontier.
    examples = {
        13: (6,),
        29: (12, 16),
        59: (20, 38),
        67: (23, 43),
        73: (6, 66),
        149: (50, 74, 98),
    }
    for prime, digits in examples.items():
        for digit in digits:
            assert triple_moment_factor(digit) % prime == 0
            assert not digit_root_is_multiple(prime, digit)
