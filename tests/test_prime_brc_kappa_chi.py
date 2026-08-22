from enterprise_math.prime_brc_kappa_chi import (
    carry_state,
    silent_binary_carry_repair,
    strict_directional_hit_counts,
)


def test_four_carry_states_are_sum_detail_complete():
    seen = set()
    for k in range(3, 80):
        for d in range(2, k + 8):
            state = carry_state(k, d)
            seen.add((state["lower_carry_bit"], state["upper_carry_bit"]))
            assert state["kappa"] == state["lower_carry_bit"] + state["upper_carry_bit"]
            assert state["chi"] == state["lower_carry_bit"] - state["upper_carry_bit"]
    assert seen == {(0, 0), (1, 0), (0, 1), (1, 1)}


def test_directional_hit_counts_reconstruct_from_kappa_chi():
    for k, d in [(13, 11), (21, 13), (31, 17), (40, 23), (73, 43)]:
        data = strict_directional_hit_counts(k, d)
        assert data["lower_hits"] - data["upper_hits"] == data["chi"]


def test_silent_semiprime_is_repaired_by_binary_carry_amount():
    examples = [(13, 5, 1), (17, 7, -1), (21, 19, 1), (23, 19, -1)]
    for k, radius, side in examples:
        data = silent_binary_carry_repair(k, radius, side)
        assert data["q_carry"]["kappa"] == 2
        assert data["q_carry"]["chi"] == 0
        assert data["two_q_carry"]["kappa"] == 1
        assert data["binary_carry_delta"] == 1
