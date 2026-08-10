from enterprise_math.p022_barlow_low_order_defect_reduction import composite_indices
from enterprise_math.p022_barlow_twin_defect_difference import (
    primitive_twin_defect_difference,
    primitive_twin_first_defect_incidence,
    primitive_twin_reflection_safe_target,
    primitive_twin_terminal_depths,
    twin_blackout_high_support,
    twin_blackout_target,
    twin_zero_local_visibility,
)


def test_twin_blackout_high_support_is_one_dimensional() -> None:
    for rank in (3, 6, 21, 30):
        target = twin_blackout_target(rank)
        for segment in composite_indices(target):
            if segment < rank + 2:
                continue
            expected = (
                ((segment - 1, 1),)
                if segment < target
                else ((rank, -1), (target - 1, 1))
            )
            assert twin_blackout_high_support(rank, segment) == expected


def test_small_twin_primitive_rows_obey_depth_difference() -> None:
    # q=13 is primitive at F_6, while 11 and 13 are twin odd boundaries.
    assert primitive_twin_defect_difference(6, 13, 8) == 0
    assert primitive_twin_defect_difference(6, 13, 11) == 1
    assert primitive_twin_terminal_depths(6, 13) == (1, 0, 0, 1)

    # q=73 is another primitive divisor of F_6.  It is outside the short
    # reflection-safe prime window but still re-enters cleanly at D_11.
    assert primitive_twin_first_defect_incidence(6, 73) == (11, 1)


def test_reflection_safe_window_recovers_the_primitive_depth() -> None:
    # These are exact simple primitive twin markers with q<3r-1.
    assert primitive_twin_reflection_safe_target(3, 7) == (5, 1)
    assert primitive_twin_reflection_safe_target(6, 13) == (11, 1)
    assert primitive_twin_reflection_safe_target(15, 31) == (29, 1)

    assert primitive_twin_first_defect_incidence(3, 7) == (5, 1)
    assert primitive_twin_first_defect_incidence(6, 13) == (11, 1)
    assert primitive_twin_first_defect_incidence(15, 31) == (29, 1)


def test_zero_visibility_has_exact_direct_successor_hidden_cases() -> None:
    # 1301 and 1303 are twin primes: a zero at rank 651 is locally hidden.
    assert twin_zero_local_visibility(651) == (False, False)

    # Both odd boundaries around 657 are composite: a zero has + and - atoms.
    assert twin_zero_local_visibility(657) == (True, True)

    # 5711 is prime but 5713 is composite: successor-only visibility.
    assert twin_zero_local_visibility(2856) == (False, True)

    # 4589 is composite and 4591 is prime: direct-only visibility.
    assert twin_zero_local_visibility(2295) == (True, False)
