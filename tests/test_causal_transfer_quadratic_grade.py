import unittest

from enterprise_math.causal_transfer_quadratic_grade import (
    closed_transfer_loop_has_zero_grade,
    path_grade_telescopes,
    path_quadratic_grade,
    primitive_transfer_quadratic_grade,
    quadratic_relation_potential,
    transfer_grade_identity,
)
from enterprise_math.causal_unit_transfer_geometry import (
    canonical_transfer_decomposition,
)
from enterprise_math.lattice_geometry import a_quadratic_separation


class CausalTransferQuadraticGradeTests(unittest.TestCase):
    def test_local_transfer_grade_is_exact_q_increment(self):
        states = (
            (0, 0, 0, 0),
            (2, -1, 0, -1),
            (3, -2, -1, 0),
        )
        transfers = ((0, 1), (2, 0), (3, 2), (1, 3))
        for state in states:
            for transfer in transfers:
                self.assertTrue(transfer_grade_identity(state, transfer))

    def test_quadratic_potential_is_same_integer_q_used_by_a_p_geometry(self):
        origin = (0, 0, 0, 0)
        states = (
            origin,
            (1, -1, 0, 0),
            (2, -1, -1, 0),
            (3, -2, 0, -1),
        )
        for state in states:
            self.assertEqual(
                quadratic_relation_potential(state),
                a_quadratic_separation(state, origin),
            )

    def test_any_minimum_transfer_path_telescopes_to_same_q_difference(self):
        left = (3, -2, -1, 0)
        right = (0, 1, -3, 2)
        transfers = canonical_transfer_decomposition(left, right)
        self.assertTrue(path_grade_telescopes(left, transfers))
        final, grade = path_quadratic_grade(left, transfers)
        self.assertEqual(final, right)
        self.assertEqual(
            grade,
            quadratic_relation_potential(right) - quadratic_relation_potential(left),
        )

    def test_closed_transfer_cycles_have_zero_total_quadratic_grade(self):
        origin = (0, 0, 0, 0)
        loop = (
            (0, 1),  # 1 -> 0
            (2, 0),  # 0 -> 2
            (1, 2),  # 2 -> 1, returns to origin
        )
        self.assertTrue(closed_transfer_loop_has_zero_grade(origin, loop))

    def test_local_grade_can_be_negative_while_global_potential_remains_integer(self):
        state = (3, -1, -1, -1)
        # Moving one unit from the highly occupied receiver slot 0 to slot 1 is
        # represented as receiver=1, donor=0 and reduces q.
        grade = primitive_transfer_quadratic_grade(state, (1, 0))
        self.assertLess(grade, 0)
        self.assertTrue(transfer_grade_identity(state, (1, 0)))


if __name__ == "__main__":
    unittest.main()
