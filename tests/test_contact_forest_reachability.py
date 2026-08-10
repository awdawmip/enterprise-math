import itertools
import unittest

from enterprise_math.contact_forest_reachability import (
    apply_integer_matrix,
    equal_weight_forest_contact_gram,
    forest_cokernel_component_factors,
    forest_contact_gram_determinant,
    forest_reachability_report,
    forest_target_is_reachable,
    forest_target_residues,
    integrated_vertex_potential,
    solve_forest_contact_target,
)


PATH3 = ((0, 1), (1, 2))
PATH4 = ((0, 1), (1, 2), (2, 3))
STAR4 = ((0, 1), (0, 2), (0, 3))
SPLIT22 = ((0, 1), (2, 3))


def direct_integer_solution_exists(gram, target, bound=8):
    if not gram:
        return target == ()
    dimension = len(gram)
    for impulse in itertools.product(range(-bound, bound + 1), repeat=dimension):
        if apply_integer_matrix(gram, impulse) == target:
            return True
    return False


class ContactForestReachabilityTests(unittest.TestCase):
    def test_any_connected_tree_has_cokernel_z_mod_n_and_determinant_n(self):
        trees = (
            (3, PATH3),
            (4, PATH4),
            (4, STAR4),
            (5, ((0, 1), (1, 2), (1, 3), (3, 4))),
        )
        for num_vertices, edges in trees:
            self.assertEqual(
                forest_cokernel_component_factors(num_vertices, edges),
                (num_vertices,),
            )
            self.assertEqual(
                forest_contact_gram_determinant(num_vertices, edges),
                num_vertices,
            )

    def test_forest_cokernel_is_direct_sum_of_component_size_factors(self):
        self.assertEqual(
            forest_cokernel_component_factors(4, SPLIT22),
            (2, 2),
        )
        self.assertEqual(
            forest_contact_gram_determinant(4, SPLIT22),
            4,
        )
        forest = ((0, 1), (1, 2), (3, 4))
        self.assertEqual(
            forest_cokernel_component_factors(6, forest),
            (3, 2),
        )
        self.assertEqual(
            forest_contact_gram_determinant(6, forest),
            6,
        )

    def test_tree_residue_is_root_independent_mod_component_size(self):
        target = (3, -2, 5)
        potential = integrated_vertex_potential(4, PATH4, target)
        self.assertEqual(potential, (0, 3, 1, 6))
        residue = sum(potential) % 4
        self.assertEqual(
            forest_target_residues(4, PATH4, target),
            (residue,),
        )
        for constant in range(-5, 6):
            shifted = tuple(value + constant for value in potential)
            self.assertEqual(sum(shifted) % 4, residue)

    def test_path_three_reachability_and_unique_impulse(self):
        gram = equal_weight_forest_contact_gram(3, PATH3)
        self.assertEqual(gram, ((2, -1), (-1, 2)))

        reachable = (1, 1)
        self.assertEqual(
            forest_target_residues(3, PATH3, reachable),
            (0,),
        )
        impulse = solve_forest_contact_target(3, PATH3, reachable)
        self.assertEqual(impulse, (1, 1))
        self.assertEqual(apply_integer_matrix(gram, impulse), reachable)

        blocked = (1, 0)
        self.assertNotEqual(
            forest_target_residues(3, PATH3, blocked),
            (0,),
        )
        self.assertIsNone(solve_forest_contact_target(3, PATH3, blocked))

    def test_arbitrary_tree_reachability_condition_matches_bounded_oracle(self):
        trees = (
            (3, PATH3),
            (4, PATH4),
            (4, STAR4),
            (5, ((0, 1), (1, 2), (1, 3), (3, 4))),
        )
        checked = 0
        for num_vertices, edges in trees:
            gram = equal_weight_forest_contact_gram(num_vertices, edges)
            for target in itertools.product(range(-2, 3), repeat=len(edges)):
                predicted = forest_target_is_reachable(
                    num_vertices,
                    edges,
                    target,
                )
                impulse = solve_forest_contact_target(
                    num_vertices,
                    edges,
                    target,
                )
                self.assertEqual(predicted, impulse is not None)
                # A reachable target in this bounded target box has a small
                # enough unique impulse for this independent finite oracle.
                self.assertEqual(
                    predicted,
                    direct_integer_solution_exists(gram, target, bound=12),
                )
                if impulse is not None:
                    self.assertEqual(
                        apply_integer_matrix(gram, impulse),
                        target,
                    )
                checked += 1
        self.assertGreater(checked, 1000)

    def test_forest_component_residues_are_independent_obstructions(self):
        target = (1, 1)
        report = forest_reachability_report(
            4,
            SPLIT22,
            target,
        )
        self.assertEqual(report.component_sizes, (2, 2))
        self.assertEqual(report.cokernel_component_factors, (2, 2))
        self.assertEqual(report.residues, (1, 1))
        self.assertFalse(report.reachable)

        reachable = forest_reachability_report(
            4,
            SPLIT22,
            (2, 2),
        )
        self.assertEqual(reachable.residues, (0, 0))
        self.assertTrue(reachable.reachable)
        self.assertEqual(reachable.unique_integer_impulse, (1, 1))

    def test_chain_mod_n_formula_is_recovered(self):
        # For path 0->1->...->n-1, integrated potential has
        # s_v=sum_{e<v} c_e, hence sum_v s_v = sum_e (n-1-e)c_e.
        for n in range(2, 8):
            edges = tuple((i, i + 1) for i in range(n - 1))
            for target in itertools.product(range(-2, 3), repeat=n - 1):
                weighted = sum(
                    (n - 1 - edge) * value
                    for edge, value in enumerate(target)
                )
                self.assertEqual(
                    forest_target_is_reachable(n, edges, target),
                    weighted % n == 0,
                )

    def test_topology_split_changes_torsion_signature(self):
        # Connected four-body tree: Z/4.  Removing the middle bridge produces
        # two 2-body components and changes the contact-target cokernel to
        # Z/2 direct-sum Z/2.
        self.assertEqual(
            forest_cokernel_component_factors(4, PATH4),
            (4,),
        )
        self.assertEqual(
            forest_cokernel_component_factors(4, SPLIT22),
            (2, 2),
        )
        self.assertEqual(
            forest_contact_gram_determinant(4, PATH4),
            4,
        )
        self.assertEqual(
            forest_contact_gram_determinant(4, SPLIT22),
            4,
        )

    def test_isolated_vertices_add_no_nontrivial_cokernel_factor(self):
        self.assertEqual(
            forest_cokernel_component_factors(3, ((0, 1),)),
            (2,),
        )
        self.assertEqual(
            forest_contact_gram_determinant(3, ((0, 1),)),
            2,
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            equal_weight_forest_contact_gram(
                3,
                ((0, 1), (1, 2), (2, 0)),
            )
        with self.assertRaises(ValueError):
            forest_target_residues(3, PATH3, (1,))
        with self.assertRaises(ValueError):
            equal_weight_forest_contact_gram(2, ((0, 0),))


if __name__ == "__main__":
    unittest.main()
