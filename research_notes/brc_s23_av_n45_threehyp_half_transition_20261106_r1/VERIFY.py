#!/usr/bin/env python3
"""Exact finite S23 AV three-hypothesis ML certificate; standard library only.
This is an author-side finite computation, not an independent project review.
"""
from fractions import Fraction
from math import comb

D = 56
Z = 14  # common stop3 probability: 1/4
A = (40, 35, 28)  # stop1 integer weights
B = (2, 7, 14)    # stop4 integer weights


def certificate(n):
    """Sum all labeled word-type masses, by exact three-way maximum likelihood."""
    maximum_mass_num = 0
    endpoint_l1_num = 0
    class_type_counts = [0, 0, 0]
    for u in range(n + 1):  # count of stop4
        for s in range(n + 1 - u):  # count of stop3
            v = n - u - s  # count of stop1
            multiplicity = comb(n, u) * comb(n - u, s) * Z ** s
            unscaled = tuple(B[j] ** u * A[j] ** v for j in range(3))
            winner = max(range(3), key=lambda j: unscaled[j])
            class_type_counts[winner] += 1
            maximum_mass_num += multiplicity * unscaled[winner]
            endpoint_l1_num += multiplicity * abs(unscaled[0] - unscaled[2])
    denominator = D ** n
    assert sum(class_type_counts) == (n + 1) * (n + 2) // 2
    assert denominator < maximum_mass_num < 3 * denominator
    return maximum_mass_num, endpoint_l1_num, denominator, class_type_counts


def main():
    for aj, bj in zip(A, B):
        a = Fraction(aj, D)
        c = Fraction(Z, Z + bj)
        assert Fraction(1, 2) <= a <= Fraction(7, 8)
        assert Fraction(1, 2) <= c <= Fraction(7, 8)
        assert (1 - a) * c == Fraction(1, 4)
        assert a + Fraction(Z + bj, D) == 1
    first_over_pair = None
    first_over_half = None
    checked = 0
    for n in range(1, 46):
        m, distance, den, counts = certificate(n)
        over_pair = 4 * (m - den) > 3 * distance
        over_half = 2 * m > 5 * den
        if over_pair and first_over_pair is None:
            first_over_pair = n
        if over_half and first_over_half is None:
            first_over_half = n
        if n in (41, 42, 44, 45):
            r3 = Fraction(m - den, 3 * den)
            pair = Fraction(distance, 4 * den)
            print(f'n={n} types={(n+1)*(n+2)//2} R3={float(r3):.15f} endpoint_half_tv={float(pair):.15f} over_pair={over_pair} over_half={over_half}')
            print(f'n={n} exact_M={m} exact_den={den} exact_pair_L1_num={distance} class_types={counts}')
        checked += (n + 1) * (n + 2) // 2
    assert first_over_pair == 42, first_over_pair
    assert first_over_half == 45, first_over_half
    m, distance, den, counts = certificate(45)
    assert 2 * m - 5 * den > 0
    assert 1000 * (m - den) > 1503 * den  # R45 > 501/1000
    assert 4 * (m - den) - 3 * distance > 0
    print('PASS_S23_THREE_RATIONAL_STATES_FINITE_PHASE_20261106')
    print(f'exact_parameter_weights: D={D}, Z={Z}, A={A}, B={B}')
    print(f'first_R3_above_endpoint_half_TV={first_over_pair}')
    print(f'first_R3_above_universal_pair_witness_cap_half={first_over_half}')
    print(f'n45_R3_decimal={float(Fraction(m-den,3*den)):.15f}')
    print('for_all_n_ge_45: delta_n > 501/1000 (project output to 45 coordinates)')
    print(f'certified_n_range=1..45 total_tested_types={checked}')
    print('claim=exact-finite-three-state lower bound; not an exact global minimax delta_n')


if __name__ == '__main__':
    main()
