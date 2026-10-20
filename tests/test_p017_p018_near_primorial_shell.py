import unittest

from enterprise_math.p017_p018_near_primorial_shell import (
    near_primorial_radical_candidates,
    near_primorial_replacement_profile,
    terminal_radical_replacement_count,
)


class NearPrimorialShellTests(unittest.TestCase):
    def test_profiles(self):
        cases = {
            8191: (4, 1155, 2),
            20000: (4, 17017, 1),
            524287: (6, 255255, 2),
        }
        for k, expected in cases.items():
            data = near_primorial_replacement_profile(k)
            self.assertEqual(
                (
                    data["transverse_primorial_depth"],
                    data["base_primorial_product"],
                    data["replacement_depth"],
                ),
                expected,
            )

    def test_exact_replacement_formula_counts(self):
        expected = {
            8191: (56, ((0, 1), (1, 35), (2, 20))),
            20000: (2, ((0, 1), (1, 1))),
            524287: (9, ((0, 1), (1, 7), (2, 1))),
        }
        for k, (count, by_depth) in expected.items():
            data = near_primorial_radical_candidates(k)
            self.assertEqual(data["candidate_count"], count)
            self.assertEqual(data["candidate_count_by_replacement_depth"], by_depth)
            self.assertTrue(all(radical < k for radical in data["candidate_radicals"]))

    def test_k524287_candidate_radicals_are_exact(self):
        candidates = (
            255255,
            285285,
            345345,
            373065,
            435435,
            440895,
            451605,
            465465,
            504735,
        )
        data = near_primorial_radical_candidates(524287)
        self.assertEqual(data["candidate_radicals"], candidates)
        for radical in candidates:
            row = terminal_radical_replacement_count(524287, radical)
            self.assertTrue(row["within_replacement_depth"])
            self.assertLessEqual(row["outsider_count"], 2)

    def test_odd_depth_has_no_even_shell(self):
        with self.assertRaises(ValueError):
            near_primorial_replacement_profile(65536)


if __name__ == "__main__":
    unittest.main()
