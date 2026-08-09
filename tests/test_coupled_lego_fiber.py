import unittest

from enterprise_math.coupled_lego_fiber import (
    coupled_fiber_count,
    coupling_split_excess,
    coupling_support,
    free_coupling,
)


class CoupledLegoFiberTests(unittest.TestCase):
    def test_free_coupling_counts_all_lower_dimensional_pairs(self):
        left_totals = {"l0": 0, "l1a": 1, "l1b": 1, "l2": 2}
        right_totals = {"r0": 0, "r1": 1, "r2a": 2, "r2b": 2}
        coupling = free_coupling(tuple(left_totals), tuple(right_totals))
        # total=2 pairs: l0 with two r2 states, two l1 states with r1,
        # and l2 with r0 -> 2+2+1=5.
        self.assertEqual(coupled_fiber_count(left_totals, right_totals, 2, coupling), 5)

    def test_zero_coupling_encodes_support_constraint(self):
        left_totals = {"l0": 0, "l1": 1}
        right_totals = {"r0": 0, "r1": 1}
        coupling = {
            ("l0", "r0"): 1,
            ("l0", "r1"): 1,
            ("l1", "r0"): 1,
            ("l1", "r1"): 0,
        }
        self.assertNotIn(("l1", "r1"), coupling_support(coupling))
        self.assertEqual(coupled_fiber_count(left_totals, right_totals, 2, coupling), 0)

    def test_multiplicity_above_one_encodes_extra_joint_relation_states(self):
        left_totals = {"l": 1}
        right_totals = {"r": 1}
        coupling = {("l", "r"): 3}
        self.assertEqual(coupled_fiber_count(left_totals, right_totals, 2, coupling), 3)
        self.assertEqual(coupling_split_excess(coupling), 2)

    def test_same_lower_dimensional_fibers_can_generate_different_joint_worlds(self):
        left_totals = {"l0": 0, "l1": 1}
        right_totals = {"r0": 0, "r1": 1}
        free = free_coupling(tuple(left_totals), tuple(right_totals))
        constrained = dict(free)
        constrained[("l1", "r1")] = 0
        split = dict(free)
        split[("l1", "r1")] = 2
        self.assertEqual(coupled_fiber_count(left_totals, right_totals, 2, free), 1)
        self.assertEqual(coupled_fiber_count(left_totals, right_totals, 2, constrained), 0)
        self.assertEqual(coupled_fiber_count(left_totals, right_totals, 2, split), 2)


if __name__ == "__main__":
    unittest.main()
