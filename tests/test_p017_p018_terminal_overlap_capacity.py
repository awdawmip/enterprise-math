import unittest

from enterprise_math.p017_p018_terminal_core_compression import (
    terminal_core_signed_profile,
)
from enterprise_math.p017_p018_terminal_overlap_capacity import (
    terminal_overlap_capacity,
)


class P017P018TerminalOverlapCapacityTests(unittest.TestCase):
    def test_exact_overlap_capacity_parameters(self):
        expected = {
            8_191: (4, 2, 0, 1, 8_191),
            20_000: (4, 1, 2, 77, 260),
            524_287: (6, 2, 2, 15, 34_953),
        }
        for k, row in expected.items():
            data = terminal_overlap_capacity(k)
            self.assertEqual(
                (
                    data["transverse_primorial_depth"],
                    data["replacement_depth"],
                    data["forced_common_base_prime_count"],
                    data["forced_common_product_floor"],
                    data["terminal_residual_row_capacity"],
                ),
                row,
            )

    def test_observed_terminal_residual_never_exceeds_overlap_capacity(self):
        for k in (8_191, 20_000, 524_287):
            bound = terminal_overlap_capacity(k)
            actual = terminal_core_signed_profile(k)
            self.assertLessEqual(
                actual["residual_core_excess"],
                bound["terminal_residual_row_capacity"],
            )


if __name__ == "__main__":
    unittest.main()
