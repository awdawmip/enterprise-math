import unittest

from enterprise_math.precision_coupling_liveness import (
    additive_potential,
    boolean_predicate_is_single_coordinate,
    count_query_from_marginals,
    full_joint_count_coupling_dimension,
    full_joint_count_padic_profile,
    may_query_from_marginals,
)


class CouplingLivenessTests(unittest.TestCase):
    def test_may_cylinder_forcing(self):
        marginals = (frozenset({0, 1}), frozenset({0, 1}))
        row0 = frozenset({(0,0),(0,1)})
        diagonal = frozenset({(0,0),(1,1)})
        self.assertTrue(may_query_from_marginals(marginals, row0))
        self.assertIsNone(may_query_from_marginals(marginals, diagonal))
        self.assertFalse(may_query_from_marginals(marginals, frozenset()))

    def test_count_additive_potential(self):
        shape = (2, 2)
        row_query = {(i,j): int(i == 0) for i in range(2) for j in range(2)}
        equality = {(i,j): int(i == j) for i in range(2) for j in range(2)}
        self.assertIsNotNone(additive_potential(row_query, shape))
        self.assertIsNone(additive_potential(equality, shape))
        marginals = ((3, 4), (2, 5))
        self.assertEqual(count_query_from_marginals(row_query, marginals), 3)
        self.assertIsNone(count_query_from_marginals(equality, marginals))

    def test_boolean_count_query_depends_on_at_most_one_coordinate(self):
        row_query = frozenset({(0,0),(0,1)})
        equality = frozenset({(0,0),(1,1)})
        self.assertTrue(boolean_predicate_is_single_coordinate(row_query, (2,2)))
        self.assertFalse(boolean_predicate_is_single_coordinate(equality, (2,2)))

    def test_full_joint_count_dimension(self):
        self.assertEqual(full_joint_count_coupling_dimension((2,2)), 1)
        self.assertEqual(full_joint_count_coupling_dimension((2,3)), 2)
        self.assertEqual(full_joint_count_coupling_dimension((2,2,2)), 4)
        self.assertEqual(full_joint_count_padic_profile((2,2), 3), (3,))

    def test_may_and_count_have_different_liveness(self):
        marginals = (frozenset({0,1}), frozenset({0,1}))
        predicate = frozenset({(0,0),(0,1),(1,1)})
        # MAY is forced true because the whole row y0=0 is included.
        self.assertTrue(may_query_from_marginals(marginals, predicate))
        # Exact count is coupling-sensitive because the predicate is not single-coordinate.
        self.assertFalse(boolean_predicate_is_single_coordinate(predicate, (2,2)))


if __name__ == "__main__":
    unittest.main()
