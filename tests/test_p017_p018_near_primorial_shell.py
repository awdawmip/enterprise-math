import unittest

from enterprise_math.p017_p018_near_primorial_shell import (
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

    def test_k524287_candidate_radicals(self):
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
        for radical in candidates:
            data = terminal_radical_replacement_count(524287, radical)
            self.assertTrue(data["within_replacement_depth"])
            self.assertLessEqual(data["outsider_count"], 2)

    def test_odd_depth_has_no_even_shell(self):
        with self.assertRaises(ValueError):
            near_primorial_replacement_profile(65536)


if __name__ == "__main__":
    unittest.main()
