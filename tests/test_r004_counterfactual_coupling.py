import unittest
from fractions import Fraction

from enterprise_math.r004_counterfactual_coupling import (
    common_quantile_coupling,
    coupling_certificate_holds,
    coupling_marginals,
    coupling_support_bounds,
    exact_two_binary_action_coupling_rank,
    identical_marginal_diagonal_rank,
)


class R004CounterfactualCouplingTests(unittest.TestCase):
    def test_two_rational_action_marginals_get_exact_small_coupling(self):
        marginals = {
            "a": {0: Fraction(1, 3), 1: Fraction(2, 3)},
            "b": {0: Fraction(1, 2), 1: Fraction(1, 2)},
        }
        coupling = common_quantile_coupling(marginals)
        self.assertTrue(coupling_certificate_holds(marginals, coupling))
        self.assertEqual(coupling_marginals(coupling), marginals)
        lower, upper = coupling_support_bounds(marginals)
        self.assertEqual((lower, upper), (2, 3))
        self.assertLessEqual(len(coupling), 3)
        self.assertEqual(exact_two_binary_action_coupling_rank(marginals), 3)

    def test_two_binary_actions_have_rank_two_exactly_when_mass_multisets_match(self):
        aligned = {
            "a": {"x": Fraction(1, 3), "y": Fraction(2, 3)},
            "b": {"u": Fraction(1, 3), "v": Fraction(2, 3)},
        }
        swapped = {
            "a": {"x": Fraction(1, 3), "y": Fraction(2, 3)},
            "b": {"u": Fraction(2, 3), "v": Fraction(1, 3)},
        }
        mismatched = {
            "a": {"x": Fraction(1, 2), "y": Fraction(1, 2)},
            "b": {"u": Fraction(1, 3), "v": Fraction(2, 3)},
        }
        self.assertEqual(exact_two_binary_action_coupling_rank(aligned), 2)
        self.assertEqual(exact_two_binary_action_coupling_rank(swapped), 2)
        self.assertEqual(exact_two_binary_action_coupling_rank(mismatched), 3)
        self.assertEqual(len(common_quantile_coupling(mismatched)), 3)

    def test_many_identical_actions_need_only_common_support_many_atoms(self):
        row = {
            "w": Fraction(1, 4),
            "x": Fraction(1, 4),
            "y": Fraction(1, 4),
            "z": Fraction(1, 4),
        }
        marginals = {f"a{index}": row for index in range(12)}
        coupling = common_quantile_coupling(marginals)
        self.assertEqual(len(coupling), 4)
        self.assertEqual(identical_marginal_diagonal_rank(marginals), 4)
        self.assertTrue(coupling_certificate_holds(marginals, coupling))
        for table in coupling:
            outcomes = {outcome for _, outcome in table}
            self.assertEqual(len(outcomes), 1)

    def test_deterministic_action_family_has_one_static_atom(self):
        marginals = {
            "left": {"L": Fraction(1)},
            "right": {"R": Fraction(1)},
            "stay": {"S": Fraction(1)},
        }
        coupling = common_quantile_coupling(marginals)
        self.assertEqual(len(coupling), 1)
        self.assertEqual(coupling_support_bounds(marginals), (1, 1))

    def test_three_different_support_sizes_obey_linear_not_product_upper_bound(self):
        marginals = {
            "a": {0: Fraction(1, 2), 1: Fraction(1, 2)},
            "b": {0: Fraction(1, 3), 1: Fraction(1, 3), 2: Fraction(1, 3)},
            "c": {
                0: Fraction(1, 4),
                1: Fraction(1, 4),
                2: Fraction(1, 4),
                3: Fraction(1, 4),
            },
        }
        lower, upper = coupling_support_bounds(marginals)
        self.assertEqual((lower, upper), (4, 7))
        coupling = common_quantile_coupling(marginals)
        self.assertLessEqual(len(coupling), 7)
        self.assertLess(len(coupling), 2 * 3 * 4)
        self.assertTrue(coupling_certificate_holds(marginals, coupling))

    def test_identical_rank_only_claimed_for_literal_identical_marginals(self):
        self.assertIsNone(
            identical_marginal_diagonal_rank(
                {
                    "a": {0: Fraction(1, 2), 1: Fraction(1, 2)},
                    "b": {0: Fraction(1, 3), 1: Fraction(2, 3)},
                }
            )
        )

    def test_zero_weight_coordinates_are_removed_before_support_bounds(self):
        marginals = {
            "a": {0: Fraction(1), 1: Fraction(0)},
            "b": {0: Fraction(1, 2), 1: Fraction(1, 2), 2: Fraction(0)},
        }
        self.assertEqual(coupling_support_bounds(marginals), (2, 2))
        coupling = common_quantile_coupling(marginals)
        self.assertEqual(len(coupling), 2)

    def test_invalid_marginals_and_couplings_fail_closed(self):
        with self.assertRaises(ValueError):
            common_quantile_coupling({})
        with self.assertRaisesRegex(ValueError, "sum exactly to one"):
            common_quantile_coupling({"a": {0: Fraction(1, 2)}})
        with self.assertRaises(ValueError):
            common_quantile_coupling({"a": {0: 0.5, 1: 0.5}})
        with self.assertRaisesRegex(ValueError, "sum exactly to one"):
            coupling_marginals({(("a", 0),): Fraction(1, 2)})
        with self.assertRaisesRegex(ValueError, "common ordered action family"):
            coupling_marginals(
                {
                    (("a", 0), ("b", 0)): Fraction(1, 2),
                    (("b", 1), ("a", 1)): Fraction(1, 2),
                }
            )
        with self.assertRaises(ValueError):
            exact_two_binary_action_coupling_rank({"a": {0: Fraction(1)}})
        with self.assertRaises(ValueError):
            exact_two_binary_action_coupling_rank(
                {
                    "a": {0: Fraction(1)},
                    "b": {0: Fraction(1, 2), 1: Fraction(1, 2)},
                }
            )


if __name__ == "__main__":
    unittest.main()
