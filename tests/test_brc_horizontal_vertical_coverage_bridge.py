from __future__ import annotations

import unittest
from math import isqrt

from enterprise_math.brc_multiplier_factor_scan import (
    AdmissibleMultiplierRootState,
    multiplier_priority_score,
    nontrivial_same_parity_factor_pairs,
)
from enterprise_math.brc_multiplier_vertical_wheel import (
    vertical_gap_at,
    vertical_state_from_multiplier_state,
)


class BRCHorizontalVerticalCoverageBridgeTests(unittest.TestCase):
    def test_factor_pair_witness_lands_on_vertical_gap(self) -> None:
        prime_pairs = ((101, 103), (101, 149), (109, 251), (127, 499))
        for p, q in prime_pairs:
            n = p * q
            for multiplier in range(1, 101):
                target = multiplier * n
                root = isqrt(target)
                remainder = target - root * root
                state = AdmissibleMultiplierRootState(
                    n=n,
                    multiplier=multiplier,
                    root=root,
                    remainder=remainder,
                    correction_steps=0,
                )
                vertical = vertical_state_from_multiplier_state(state)

                for u, v in nontrivial_same_parity_factor_pairs(multiplier):
                    x_numerator = u * p + v * q
                    b_numerator = v * q - u * p
                    self.assertEqual(x_numerator % 2, 0)
                    self.assertEqual(b_numerator % 2, 0)
                    x = x_numerator // 2
                    b = b_numerator // 2
                    self.assertEqual(x * x - multiplier * n, b * b)

                    t = x - vertical.base_x
                    self.assertGreaterEqual(t, 0)
                    self.assertEqual(vertical_gap_at(vertical, t), b * b)

    def test_existing_score_is_fourth_power_normalization(self) -> None:
        # C_m = nu(m)*m^(-1/4) is the leading log-ratio coverage
        # coefficient after removing the universal 4*sqrt(2*theta) factor.
        # Hence C_m^4 = nu(m)^4/m, exactly the existing rational score.
        for multiplier in range(1, 101):
            nu = len(nontrivial_same_parity_factor_pairs(multiplier))
            score = multiplier_priority_score(multiplier)
            self.assertEqual(score.numerator * multiplier, nu**4 * score.denominator)


if __name__ == "__main__":
    unittest.main()
