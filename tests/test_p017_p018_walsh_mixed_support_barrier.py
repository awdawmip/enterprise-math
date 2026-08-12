from enterprise_math.p017_p018_walsh_mixed_support_barrier import (
    four_support_sharpness_witness,
    positive_mixed_square_root_trigger,
    support_three_nonpositive,
)


def test_every_budget_is_nonpositive_through_support_depth_three():
    for primes in ((), (3,), (3, 5), (3, 5, 11)):
        radical = 1
        for p in primes:
            radical *= p
        for budget in range(0, radical + 1):
            data = support_three_nonpositive(primes, budget)
            assert data["truncated_mixed_inner"] <= 0
            assert data["positive_mixed_inner_impossible"] is True


def test_four_support_threshold_is_sharp():
    data = four_support_sharpness_witness()
    assert data["truncated_mixed_inner"] == 2
    assert data["four_support_threshold_sharp"] is True


def test_positive_mixed_basin_state_forces_square_root_least_prime():
    # 3*5*7*11=1155 lies in the open 33rd square basin (1089,1156).
    data = positive_mixed_square_root_trigger(33, 1155, (3, 5, 7, 11), 77)
    assert data["positive_mixed_inner"] is True
    assert data["support_size"] == 4
    assert data["least_support_prime"] <= data["least_prime_square_root_ceiling"]
