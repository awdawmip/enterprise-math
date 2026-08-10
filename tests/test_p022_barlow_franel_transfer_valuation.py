from enterprise_math.p022_barlow_franel_transfer_valuation import (
    defect_valuation_from_transfer,
    forced_midpoint_transfer_formula,
    prime_halving_transfer_identity,
    transfer_imbalance,
    transfer_is_additive,
    transfer_pairing,
)


def test_transfer_pairing_is_completely_additive() -> None:
    weights = {2: 3, 4: -1, 8: 2, 16: 5}
    for left, right in ((2, 3), (5, 17), (31, 43), (78, 155), (125, 337)):
        assert transfer_is_additive(left, right, weights)
        assert transfer_pairing(left * right, weights) == (
            transfer_pairing(left, weights) + transfer_pairing(right, weights)
        )


def test_prime_halving_recursion_is_exact_for_sparse_weights() -> None:
    weights = {1: 0, 8: 1, 9: 0, 16: 1, 17: 0}
    for prime in (3, 5, 17, 31, 43, 1087):
        left, right = prime_halving_transfer_identity(prime, weights)
        assert left == right


def test_p157_exact_cancellation_is_transfer_imbalance_minus_one() -> None:
    # Relevant p=157 Franel weights on the canonical ancestry: midpoint 78 and earlier zero 16.
    weights = {16: 1, 78: 1}
    left, right, difference = transfer_imbalance(78, weights)
    assert (left, right, difference) == (0, 1, -1)
    assert forced_midpoint_transfer_formula(78, weights) == 0
    assert defect_valuation_from_transfer(78, weights) == 0


def test_p369581_sign_reversal_is_transfer_imbalance_minus_two() -> None:
    # The only relevant earlier zero is F_8, while the midpoint has valuation one.
    weights = {8: 1, 184790: 1}
    left, right, difference = transfer_imbalance(184790, weights)
    assert (left, right, difference) == (0, 2, -2)
    assert forced_midpoint_transfer_formula(184790, weights) == -1
    assert defect_valuation_from_transfer(184790, weights) == -1


def test_target_p_five_mod_twenty_four_factor_reduction() -> None:
    # For odd p>5, Franel weights have w_1=w_2=0, so tau(2)=tau(3)=0.
    weights = {8: 1}
    p = 369581
    m = (p - 1) // 2
    a = (p - 1) // 4
    b = (p - 2) // 3
    assert transfer_pairing(2, weights) == 0
    assert transfer_pairing(3, weights) == 0
    assert transfer_pairing(m, weights) == transfer_pairing(a, weights)
    assert transfer_pairing(p - 2, weights) == transfer_pairing(b, weights)
    assert transfer_pairing(a, weights) - transfer_pairing(b, weights) == -2
