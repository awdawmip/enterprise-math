import unittest
from fractions import Fraction

from enterprise_math.stage131_horn_hyperedge_presentation import (
    balanced_binary_and_tree,
)
from enterprise_math.stage131_rooted_circuit_table_explosion import (
    availability_premise_polynomial,
    circuit_to_basis_rule_ratio,
    enumerate_rooted_circuit_premises,
    enumerated_width_histogram,
    local_horn_basis_rule_count,
    rooted_circuit_average_premise_width,
    rooted_circuit_count,
    rooted_circuit_count_lower_bound,
    rooted_circuit_count_recurrence,
    rooted_circuit_count_upper_bound,
    rooted_circuit_explosion_report,
    rooted_circuit_max_width,
    rooted_circuit_min_width,
    rooted_circuit_total_premise_literals,
    rooted_circuit_width_polynomial,
    total_internal_rooted_circuit_rule_count,
    verify_enumerated_rooted_circuits,
)


class Stage131RootedCircuitTableExplosionTests(unittest.TestCase):
    def test_exact_root_circuit_count_recurrence(self):
        expected = {
            1: 1,
            2: 4,
            3: 25,
            4: 676,
            5: 458329,
            6: 210066388900,
        }
        for height, count in expected.items():
            self.assertEqual(rooted_circuit_count(height), count)
            self.assertEqual(rooted_circuit_count_recurrence(height), count)

    def test_exact_small_width_polynomials(self):
        self.assertEqual(rooted_circuit_width_polynomial(1), {2: 1})
        self.assertEqual(
            rooted_circuit_width_polynomial(2),
            {2: 1, 3: 2, 4: 1},
        )
        self.assertEqual(
            rooted_circuit_width_polynomial(3),
            {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 4},
        )

    def test_availability_polynomial_is_direct_seed_plus_rooted_circuits(self):
        for height in range(1, 8):
            availability = availability_premise_polynomial(height)
            circuits = rooted_circuit_width_polynomial(height)
            self.assertEqual(availability.get(1), 1)
            for width, count in circuits.items():
                self.assertEqual(availability.get(width), count)
            self.assertEqual(sum(availability.values()), 1 + rooted_circuit_count(height))

    def test_explicit_small_tree_enumeration_matches_generating_polynomial(self):
        for height in range(1, 5):
            tree = balanced_binary_and_tree(height)
            circuits = enumerate_rooted_circuit_premises(tree, tree.root)
            self.assertEqual(len(circuits), rooted_circuit_count(height))
            self.assertEqual(
                enumerated_width_histogram(tree, tree.root),
                rooted_circuit_width_polynomial(height),
            )
            self.assertTrue(verify_enumerated_rooted_circuits(tree, tree.root))

    def test_min_and_max_widths(self):
        for height in range(1, 10):
            self.assertEqual(rooted_circuit_min_width(height), 2)
            self.assertEqual(rooted_circuit_max_width(height), 1 << height)

    def test_total_premise_literals_and_average_width(self):
        expected_literals = {
            1: 2,
            2: 12,
            3: 156,
            4: 6792,
            5: 7048360,
        }
        for height, literals in expected_literals.items():
            self.assertEqual(rooted_circuit_total_premise_literals(height), literals)
            self.assertEqual(
                rooted_circuit_average_premise_width(height),
                Fraction(literals, rooted_circuit_count(height)),
            )

    def test_exponential_in_leaf_count_bounds(self):
        for height in range(2, 12):
            count = rooted_circuit_count(height)
            self.assertGreaterEqual(count, rooted_circuit_count_lower_bound(height))
            self.assertLess(count, rooted_circuit_count_upper_bound(height))

    def test_all_internal_circuit_table_dwarfs_local_basis(self):
        expected = {
            1: (1, 1),
            2: (6, 3),
            3: (37, 7),
            4: (750, 15),
            5: (459829, 31),
            6: (210067308558, 63),
        }
        for height, (all_circuits, basis) in expected.items():
            self.assertEqual(total_internal_rooted_circuit_rule_count(height), all_circuits)
            self.assertEqual(local_horn_basis_rule_count(height), basis)
            self.assertEqual(circuit_to_basis_rule_ratio(height), Fraction(all_circuits, basis))

    def test_height_five_report(self):
        report = rooted_circuit_explosion_report(5)
        self.assertEqual(report.leaf_count, 32)
        self.assertEqual(report.local_basis_rules, 31)
        self.assertEqual(report.root_circuit_count, 458329)
        self.assertEqual(report.all_internal_circuit_rules, 459829)
        self.assertEqual(report.root_min_premise_width, 2)
        self.assertEqual(report.root_max_premise_width, 32)
        self.assertEqual(report.root_total_premise_literals, 7048360)

    def test_validation(self):
        with self.assertRaises(ValueError):
            rooted_circuit_count(0)
        with self.assertRaises(ValueError):
            rooted_circuit_count_lower_bound(1)
        tree = balanced_binary_and_tree(5)
        with self.assertRaises(ValueError):
            enumerate_rooted_circuit_premises(tree, tree.root)


if __name__ == "__main__":
    unittest.main()
