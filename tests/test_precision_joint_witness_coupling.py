import unittest

from enterprise_math.precision_joint_witness_coupling import (
    coupled_predicate_count,
    coupling_obstruction,
    marginal_count_table,
    marginal_supports,
    marginal_supports_uniquely_determine_joint,
    pushforward_functorial,
    rectangular_hull,
)


class JointWitnessCouplingTests(unittest.TestCase):
    def test_diagonal_and_antidiagonal_have_same_marginals(self):
        diagonal = {(0, 0): 1, (1, 1): 1}
        anti = {(0, 1): 1, (1, 0): 1}
        for coordinate in (0, 1):
            self.assertEqual(marginal_count_table(diagonal, coordinate), marginal_count_table(anti, coordinate))
        self.assertEqual(coupled_predicate_count(diagonal, lambda y: y[0] == y[1]), 2)
        self.assertEqual(coupled_predicate_count(anti, lambda y: y[0] == y[1]), 0)

    def test_boolean_marginal_uniqueness_gate(self):
        chain = {(0, 0), (0, 1)}
        square = {(0, 0), (0, 1), (1, 0), (1, 1)}
        self.assertTrue(marginal_supports_uniquely_determine_joint(chain))
        self.assertFalse(marginal_supports_uniquely_determine_joint(square))

    def test_coupling_obstruction_is_missing_rectangular_tuples(self):
        diagonal = {(0, 0), (1, 1)}
        self.assertEqual(rectangular_hull(diagonal), frozenset({(0,0),(0,1),(1,0),(1,1)}))
        self.assertEqual(coupling_obstruction(diagonal), frozenset({(0,1),(1,0)}))

    def test_pushforward_is_functorial(self):
        table = {(0,0):2, (0,1):1, (1,0):3}
        self.assertTrue(pushforward_functorial(table, lambda y: y[0]+y[1], lambda z: z % 2))

    def test_marginal_supports(self):
        J = {(0,"a"),(1,"a"),(1,"b")}
        self.assertEqual(marginal_supports(J), (frozenset({0,1}), frozenset({"a","b"})))


if __name__ == "__main__":
    unittest.main()
