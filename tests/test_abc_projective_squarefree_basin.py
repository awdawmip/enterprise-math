import unittest

from enterprise_math.abc_projective_squarefree_basin import (
    squarefree_basin_state,
    squarefree_pair_derivative_dominates_sum,
)


class ProjectiveSquarefreeBasinTests(unittest.TestCase):
    def test_all_squarefree_nonunit_triple_is_subunit(self) -> None:
        state = squarefree_basin_state(2, 3, 5)
        self.assertEqual(state.squarefree, (True, True, True))
        self.assertTrue(state.forced_subunit_by_structure)
        self.assertFalse(state.actually_activated)

    def test_squarefree_c_forces_subunit_even_with_repeated_side(self) -> None:
        state = squarefree_basin_state(9, 2, 11)
        self.assertEqual(state.squarefree, (False, True, True))
        self.assertTrue(state.forced_subunit_by_structure)
        self.assertFalse(state.actually_activated)

    def test_squarefree_sides_force_subunit_with_repeated_c(self) -> None:
        state = squarefree_basin_state(3, 5, 8)
        self.assertEqual(state.squarefree, (True, True, False))
        self.assertTrue(state.forced_subunit_by_structure)
        self.assertFalse(state.actually_activated)

    def test_activated_nonunit_examples_have_c_and_a_side_nonsquarefree(self) -> None:
        for triple in ((2, 25, 27), (3, 125, 128), (7, 162, 169), (49, 576, 625)):
            state = squarefree_basin_state(*triple)
            self.assertTrue(state.actually_activated)
            self.assertFalse(state.squarefree[2])
            self.assertGreaterEqual(state.nonsquarefree_count, 2)
            self.assertFalse(state.squarefree[0] and state.squarefree[1])

    def test_squarefree_product_derivative_lower_bound(self) -> None:
        for a, b in ((2, 3), (3, 5), (6, 35), (10, 21), (30, 77)):
            self.assertTrue(squarefree_pair_derivative_dominates_sum(a, b))


if __name__ == "__main__":
    unittest.main()
