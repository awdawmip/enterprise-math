import unittest

from enterprise_math.infinite_branch_escape import (
    finite_prefix_common_survivor,
    fixed_label_blocker,
    infinite_branch_locally_solvable,
    least_local_branch_label,
)


class InfiniteBranchEscapeTests(unittest.TestCase):
    def test_every_modulus_has_a_local_branch(self):
        for modulus in range(1, 101):
            label = least_local_branch_label(modulus)
            self.assertEqual(label, modulus)
            self.assertTrue(infinite_branch_locally_solvable(label, modulus))

    def test_support_descends_under_divisibility(self):
        labels = range(1, 301)
        for coarse, fine in ((2, 4), (3, 6), (5, 15), (6, 30), (7, 77)):
            coarse_support = {
                label for label in labels
                if infinite_branch_locally_solvable(label, coarse)
            }
            fine_support = {
                label for label in labels
                if infinite_branch_locally_solvable(label, fine)
            }
            self.assertTrue(fine_support.issubset(coarse_support))

    def test_every_fixed_label_is_eventually_blocked(self):
        for label in range(1, 101):
            blocker = fixed_label_blocker(label)
            self.assertFalse(infinite_branch_locally_solvable(label, blocker))

    def test_finite_precision_prefix_has_common_label_but_label_escapes(self):
        previous = 1
        for maximum in range(1, 13):
            label = finite_prefix_common_survivor(maximum)
            self.assertGreaterEqual(label, previous)
            self.assertTrue(all(
                infinite_branch_locally_solvable(label, modulus)
                for modulus in range(1, maximum + 1)
            ))
            # The chosen common label is always killed by some later modulus.
            self.assertFalse(
                infinite_branch_locally_solvable(
                    label,
                    fixed_label_blocker(label),
                )
            )
            previous = label

    def test_no_bounded_label_can_survive_all_checked_depths_forever(self):
        for bound in (1, 2, 5, 10, 25):
            blocker_family = tuple(fixed_label_blocker(label) for label in range(1, bound + 1))
            for label in range(1, bound + 1):
                self.assertTrue(any(
                    not infinite_branch_locally_solvable(label, modulus)
                    for modulus in blocker_family
                ))

    def test_validation(self):
        with self.assertRaises(ValueError):
            least_local_branch_label(0)
        with self.assertRaises(ValueError):
            infinite_branch_locally_solvable(0, 2)
        with self.assertRaises(TypeError):
            infinite_branch_locally_solvable(True, 2)
        with self.assertRaises(ValueError):
            finite_prefix_common_survivor(0)


if __name__ == "__main__":
    unittest.main()
