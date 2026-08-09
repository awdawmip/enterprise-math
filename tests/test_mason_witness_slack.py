import itertools
import unittest

from enterprise_math.mason_witness_slack import (
    infinity_contact_depth,
    mason_margin_profile,
    mason_polynomial_slack_profile,
    polynomial_degree,
    wronskian,
    wronskian_capacity_slack,
    wronskian_contact_profile,
)


class MasonWitnessSlackTests(unittest.TestCase):
    def test_unequal_degrees_have_zero_capacity_slack(self) -> None:
        p = (0, 0, 1)  # x^2
        q = (1, 1)  # x+1
        profile = wronskian_contact_profile(p, q)
        self.assertEqual(profile["wronskian_degree"], 2)
        self.assertEqual(profile["capacity_slack"], 0)
        self.assertEqual(profile["infinity_contact_depth"], 0)

    def test_equal_degree_depth_two_example(self) -> None:
        p = (0, 0, 1)  # x^2
        q = (1, 0, 1)  # x^2+1
        profile = wronskian_contact_profile(p, q)
        self.assertEqual(profile["wronskian"], (0, 2))
        self.assertEqual(profile["capacity_slack"], 2)
        self.assertEqual(profile["infinity_contact_depth"], 2)

    def test_equal_degree_depth_one_example(self) -> None:
        p = (0, 0, 1)  # x^2
        q = (1, 1, 1)  # x^2+x+1
        profile = wronskian_contact_profile(p, q)
        self.assertEqual(profile["wronskian"], (0, 2, 1))
        self.assertEqual(profile["capacity_slack"], 1)
        self.assertEqual(profile["infinity_contact_depth"], 1)

    def test_capacity_equals_infinity_contact_exhaustively(self) -> None:
        candidates = []
        for degree in range(1, 4):
            for low in itertools.product(range(-2, 3), repeat=degree):
                for leading in (-2, -1, 1, 2):
                    candidates.append(tuple(low) + (leading,))

        checked = 0
        for left in candidates:
            for right in candidates:
                if wronskian(left, right) == (0,):
                    continue
                self.assertEqual(
                    wronskian_capacity_slack(left, right),
                    infinity_contact_depth(left, right),
                )
                checked += 1
        self.assertGreater(checked, 100000)

    def test_margin_decomposition_integer_identity(self) -> None:
        profile = mason_margin_profile((2, 2, 2), 5, 1, 2)
        self.assertEqual(profile["residual_degree"], 1)
        self.assertEqual(profile["absorption_slack"], 0)
        self.assertEqual(profile["capacity_slack"], 2)
        self.assertEqual(profile["theorem_margin"], 2)

    def test_same_coarse_margin_different_internal_slack(self) -> None:
        a = (0, 0, 1)  # x^2

        first = mason_polynomial_slack_profile(
            (a, (1, 0, 1), (-1, 0, -2)),
            radical_degree=5,
            target_index=2,
        )
        second = mason_polynomial_slack_profile(
            (a, (1, 1, 1), (-1, -1, -2)),
            radical_degree=5,
            target_index=2,
        )

        self.assertEqual(first["degrees"], second["degrees"])
        self.assertEqual(first["radical_degree"], second["radical_degree"])
        self.assertEqual(first["theorem_margin"], second["theorem_margin"])
        self.assertEqual(first["theorem_margin"], 2)
        self.assertEqual(
            (first["absorption_slack"], first["capacity_slack"]),
            (0, 2),
        )
        self.assertEqual(
            (second["absorption_slack"], second["capacity_slack"]),
            (1, 1),
        )

    def test_unequal_degree_mason_sample(self) -> None:
        profile = mason_polynomial_slack_profile(
            ((0, 0, 1), (1, 1), (-1, -1, -1)),
            radical_degree=4,
            target_index=2,
        )
        self.assertEqual(profile["degrees"], (2, 1, 2))
        self.assertEqual(profile["absorption_slack"], 1)
        self.assertEqual(profile["capacity_slack"], 0)
        self.assertEqual(profile["infinity_contact_depth"], 0)
        self.assertEqual(profile["theorem_margin"], 1)

    def test_invalid_mason_bounds_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            mason_margin_profile((2, 2, 2), 5, 0, 2)
        with self.assertRaises(ValueError):
            mason_margin_profile((2, 2, 2), 5, 4, 2)

    def test_proportional_pair_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            wronskian_contact_profile((1, 2), (2, 4))

    def test_polynomial_degree_rejects_zero(self) -> None:
        with self.assertRaises(ValueError):
            polynomial_degree((0, 0))


if __name__ == "__main__":
    unittest.main()
