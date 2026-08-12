import unittest

from enterprise_math.p017_p018_terminal_exponent_repair import (
    terminal_exponent_repair_profile,
)
from enterprise_math.p017_p018_terminal_full_core_identity import (
    terminal_complete_core_candidates,
)


class P017P018TerminalExponentRepairTests(unittest.TestCase):
    def test_global_exponent_repair_depth_checkpoints(self):
        expected = {
            8_191: (4, 2, 1, False, 56, 80, 65),
            20_000: (4, 1, 0, True, 2, 2, 2),
            524_287: (6, 2, 0, True, 9, 9, 9),
        }
        for k, row in expected.items():
            data = terminal_exponent_repair_profile(k)
            actual_cores = terminal_complete_core_candidates(k)
            self.assertEqual(
                (
                    data["transverse_primorial_depth"],
                    data["support_replacement_depth"],
                    data["global_exponent_repair_depth"],
                    data["globally_prime_power_rigid"],
                    data["candidate_radical_count"],
                    data["complete_core_candidate_count_upper_bound"],
                    actual_cores["complete_core_candidate_count"],
                ),
                row,
            )
            self.assertLessEqual(
                actual_cores["complete_core_candidate_count"],
                data["complete_core_candidate_count_upper_bound"],
            )

    def test_prime_power_rigidity_collapses_complete_cores_to_radicals(self):
        for k in (20_000, 524_287):
            repair = terminal_exponent_repair_profile(k)
            cores = terminal_complete_core_candidates(k)
            self.assertTrue(repair["globally_prime_power_rigid"])
            self.assertEqual(
                tuple(repair_row["radical"] for repair_row in repair["radical_rows"]),
                cores["complete_core_candidates"],
            )

    def test_k8191_needs_only_one_extra_exponent_unit(self):
        data = terminal_exponent_repair_profile(8_191)
        self.assertEqual(data["global_exponent_repair_depth"], 1)
        self.assertTrue(
            all(
                row["local_exponent_repair_depth"] <= 1
                for row in data["radical_rows"]
            )
        )
        self.assertTrue(
            any(
                row["local_exponent_repair_depth"] == 1
                for row in data["radical_rows"]
            )
        )


if __name__ == "__main__":
    unittest.main()
