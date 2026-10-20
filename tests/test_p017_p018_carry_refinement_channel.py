from enterprise_math.p017_p018_carry_refinement_channel import (
    divisor_refinement_channel,
    signed_fiber_channel_state,
    verify_refinement_monoid,
)


def test_parent_child_fiber_is_one_quotient_index_channel():
    for K in range(0, 30):
        for parent in (1, 3, 5, 7, 9):
            for refinement in (3, 5, 7):
                data = divisor_refinement_channel(K, parent, refinement)
                assert data["child_carry_from_parent_transport"] is True
                assert data["refined_parent_state"]["child_fiber_size"] == data["direct_child"]["fiber_size"]


def test_odd_refinement_is_an_exact_multiplicative_monoid_action():
    probes = (
        (20, 3, 5, 7),
        (46, 5, 3, 9),
        (81, 7, 5, 11),
        (118, 11, 3, 5),
    )
    for K, parent, d1, d2 in probes:
        data = verify_refinement_monoid(K, parent, d1, d2)
        assert data["refinement_monoid_identity"] is True
        assert data["staged_second"]["child_fiber_size"] == data["direct_product"]["child_fiber_size"]
        assert data["staged_second"]["child_first_quotient"] == data["direct_product"]["child_first_quotient"]


def test_high_product_child_carry_cannot_exist_below_empty_parent():
    for K in (10, 20, 46):
        for parent in (K + 2, K + 4, K + 6):
            if parent % 2 == 0:
                parent += 1
            pstate = signed_fiber_channel_state(K, parent)
            for refinement in (3, 5, 7):
                data = divisor_refinement_channel(K, parent, refinement)
                assert data["high_product_carry_monotone"] is True
                assert data["child_centered_carry"] <= pstate["centered_carry"]
