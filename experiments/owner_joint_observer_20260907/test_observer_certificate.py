"""Focused regression for the experimental adapter's source-state integrity."""
import unittest

from observer_certificate import Branch, raw_marginal_table


class BranchProvenanceTests(unittest.TestCase):
    def test_mutating_input_coordinate_cannot_change_frozen_branch(self):
        coordinate = [0, 0, 0, 0, 0, 0]
        branch = Branch("anchor", coordinate)
        before = raw_marginal_table((branch,), (0, 1, 2))
        coordinate[0] = 99
        self.assertEqual(branch.coordinate, (0, 0, 0, 0, 0, 0))
        self.assertIsInstance(branch.coordinate, tuple)
        self.assertEqual(raw_marginal_table((branch,), (0, 1, 2)), before)


if __name__ == "__main__":
    unittest.main()
