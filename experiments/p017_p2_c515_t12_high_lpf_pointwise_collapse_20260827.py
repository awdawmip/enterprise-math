#!/usr/bin/env python3
"""Exact-rational checker for the c=103/20 T1-T2 high-LPF collapse."""

from fractions import Fraction as Q


def main() -> None:
    a = Q(6)
    b = Q(93, 20)
    c = Q(103, 20)
    delta = 2 * c - b - 1
    U = (b + 1) / (2 * a)
    tau0 = U - 1 / a

    assert delta == Q(93, 20)
    assert U == Q(113, 240)
    assert tau0 == Q(73, 240)

    # T2 vanishing: U-tau <=1/a at and above tau0.
    assert U - tau0 == Q(1, 6)

    # Six distinct primes at tau0 already overshoot the full basin D^(9/5).
    assert 6 * tau0 == Q(73, 40) > Q(9, 5)

    # Base-minus-T3 numerator at the transition frontier.
    base_t3_num = 12 * tau0 - 1
    assert base_t3_num == Q(53, 20)

    # At most five T1 primes, each charged 1/2.
    t1_max = Q(5, 2)
    assert (base_t3_num - t1_max) / delta == Q(1, 31)

    # Above U, at most three distinct prime factors.
    assert 4 * U == Q(113, 60) > Q(9, 5)
    assert 1 - Q(3, 2) / delta == Q(21, 31)

    # W-coordinate endpoint: D=W^(10/9).
    assert Q(10, 9) * tau0 == Q(73, 216)

    print("P017 c515 T1-T2 high-LPF pointwise collapse checker: PASS")
    print("dangerous least-prime sector: z <= p_min < D^(73/240)=W^(73/216)")
    print("transition-band margin >= 1/31 before T4")
    print("above T3 endpoint margin >= 21/31 before T4")


if __name__ == "__main__":
    main()
