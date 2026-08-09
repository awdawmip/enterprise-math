import unittest

from enterprise_math.coupled_lego_fiber import (
    coupled_fiber_count,
    coupling_split_excess,
    coupling_support,
    fiber_coupling_defect,
    free_coupling,
)


class CoupledLegoFiberTests(unittest.TestCase):
    def test_free_coupling_counts_all_lower_dimensional_pairs(self):
        left_totals = {"l0": 0, "l1a": 1, "l1b": 1, "l2": 2}
        right_totals = {"r0": 0, "r1": 1, "r2a": 2, "r2b": 2}
        coupling = free_coupling(tuple(left_totals), tuple(right_totals))
        self.assertEqual(coupled_fiber_count(left_totals, right_totals, 2, coupling), 5)
        defect = fiber_coupling_defect(left_totals, right_totals, 2, coupling)
        self.assertEqual((defect.free_pairings, defect.coupled_states), (5, 5))
        self.assertEqual((defect.missing_support, defect.split_excess), (0, 0))

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
        defect = fiber_coupling_defect(left_totals, right_totals, 2, coupling)
        self.assertEqual((defect.free_pairings, defect.coupled_states), (1, 0))
        self.assertEqual((defect.missing_support, defect.split_excess), (1, 0))

    def test_multiplicity_above_one_encodes_extra_joint_relation_states(self):
        left_totals = {"l": 1}
        right_totals = {"r": 1}
        coupling = {("l", "r"): 3}
        self.assertEqual(coupled_fiber_count(left_totals, right_totals, 2, coupling), 3)
        self.assertEqual(coupling_split_excess(coupling), 2)
        defect = fiber_coupling_defect(left_totals, right_totals, 2, coupling)
        self.assertEqual((defect.missing_support, defect.split_excess), (0, 2))
        self.assertEqual(defect.signed_count_defect, 2)

    def test_missing_and_split_can_cancel_in_signed_count_but_not_typed_defect(self):
        left_totals = {"l0": 0, "l1": 0}
        right_totals = {"r0": 0, "r1": 0}
        # Four free pairings. One is forbidden and another has multiplicity two.
        coupling = {
            ("l0", "r0"): 0,
            ("l0", "r1"): 2,
            ("l1", "r0"): 1,
            ("l1", "r1"): 1,
        }
        defect = fiber_coupling_defect(left_totals, right_totals, 0, coupling)
        self.assertEqual(defect.free_pairings, 4)
        self.assertEqual(defect.coupled_states, 4)
        self.assertEqual(defect.signed_count_defect, 0)
        self.assertEqual((defect.missing_support, defect.split_excess), (1, 1))
        self.assertTrue(defect.identity_holds)

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
