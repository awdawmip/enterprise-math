from enterprise_math.p022_barlow_franel_stationary_terminal_joint import (
    bounded_joint_odd_part_divides_five,
    odd_part,
    stationary_terminal_joint_gcd,
)


def test_joint_gcd_is_much_smaller_than_the_separate_fixed_obstructions() -> None:
    assert stationary_terminal_joint_gcd(3) == 1
    assert stationary_terminal_joint_gcd(12) == 5
    assert stationary_terminal_joint_gcd(30) == 4
    assert stationary_terminal_joint_gcd(60) == 2


def test_power_of_two_part_is_not_artificially_bounded_by_four() -> None:
    # This regression corrects the tempting but false stronger guess J_r|20.
    assert stationary_terminal_joint_gcd(252) == 8
    assert odd_part(stationary_terminal_joint_gcd(252)) == 1


def test_bounded_joint_odd_part_is_five_smooth() -> None:
    # Finite evidence only; the uniform theorem remains open.
    assert bounded_joint_odd_part_divides_five(80)
