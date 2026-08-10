import itertools
import unittest

from enterprise_math.contact_forest_reachability import (
    apply_integer_matrix,
)
from enterprise_math.contact_weighted_forest_reachability import (
    common_weight_tree_cokernel_invariant_factors,
    solve_weighted_forest_contact_target,
    weighted_forest_component_reachability,
    weighted_forest_contact_gram,
    weighted_forest_contact_gram_determinant,
    weighted_forest_reachability_report,
    weighted_forest_target_is_reachable,
    weighted_tree_determinant,
)


PATH3 = ((0, 1), (1, 2))
PATH4 = ((0, 1), (1, 2), (2, 3))
STAR4 = ((0, 1), (0, 2), (0, 3))
SPLIT22 = ((0, 1), (2, 3))


def bounded_oracle(gram, target, bound=10):
    dimension = len(gram)
    if dimension == 0:
        return target == ()
    for impulse in itertools.product(
        range(-bound, bound + 1),
        repeat=dimension,
    ):
        if apply_integer_matrix(gram, impulse) == target:
            return True
    return False


class ContactWeightedForestReachabilityTests(unittest.TestCase):
    def test_weighted_tree_determinant_closed_form(self):
        self.assertEqual(weighted_tree_determinant((2, 3)), 5)
        self.assertEqual(weighted_tree_determinant((2, 3, 5)), 31)
        self.assertEqual(
            weighted_tree_determinant((2, 3, 5, 7)),
            3 * 5 * 7 + 2 * 5 * 7 + 2 * 3 * 7 + 2 * 3 * 5,
        )

    def test_tree_shape_does_not_change_weighted_determinant(self):
        weights = (2, 3, 5, 7)
        expected = weighted_tree_determinant(weights)
        self.assertEqual(
            weighted_forest_contact_gram_determinant(
                4,
                PATH4,
                weights,
            ),
            expected,
        )
        self.assertEqual(
            weighted_forest_contact_gram_determinant(
                4,
                STAR4,
                weights,
            ),
            expected,
        )

    def test_common_weight_snf_family(self):
        for bodies in range(2, 9):
            for weight in range(1, 6):
                factors = common_weight_tree_cokernel_invariant_factors(
                    bodies,
                    weight,
                )
                self.assertEqual(
                    factors,
                    (weight,) * (bodies - 2) + (bodies * weight,),
                )
                order = 1
                for factor in factors:
                    order *= factor
                self.assertEqual(
                    order,
                    weighted_tree_determinant((weight,) * bodies),
                )

    def test_forced_shift_can_fail_before_coordinate_divisibility(self):
        report = weighted_forest_component_reachability(
            3,
            PATH3,
            (2, 3, 5),
            (-2, -2),
        )[0]
        self.assertIsNone(report.forced_shift)
        self.assertFalse(report.reachable)

    def test_integer_forced_shift_can_still_fail_weight_divisibility(self):
        report = weighted_forest_component_reachability(
            3,
            PATH3,
            (1, 2, 2),
            (-5, 2),
        )[0]
        self.assertEqual(report.forced_shift, 2)
        self.assertFalse(report.divisible_coordinates)
        self.assertFalse(report.reachable)

    def test_weighted_reachability_matches_bounded_oracle(self):
        trees = (
            (3, PATH3, (2, 3, 5)),
            (3, PATH3, (1, 2, 2)),
            (4, PATH4, (1, 2, 3, 4)),
            (4, STAR4, (2, 1, 3, 2)),
        )
        checked = 0
        for num_vertices, edges, weights in trees:
            gram = weighted_forest_contact_gram(
                num_vertices,
                edges,
                weights,
            )
            for target in itertools.product(
                range(-2, 3),
                repeat=len(edges),
            ):
                predicted = weighted_forest_target_is_reachable(
                    num_vertices,
                    edges,
                    weights,
                    target,
                )
                impulse = solve_weighted_forest_contact_target(
                    num_vertices,
                    edges,
                    weights,
                    target,
                )
                self.assertEqual(predicted, impulse is not None)
                self.assertEqual(
                    predicted,
                    bounded_oracle(gram, target, bound=12),
                )
                if impulse is not None:
                    self.assertEqual(
                        apply_integer_matrix(gram, impulse),
                        target,
                    )
                checked += 1
        self.assertGreater(checked, 1000)

    def test_equal_weight_reduces_to_mod_n_but_scaled(self):
        # With common weight d, K=d*K_unit.  Every reachable target must first
        # be divisible by d; after division the unit-weight mod-n condition is recovered.
        for bodies in range(2, 7):
            edges = tuple((i, i + 1) for i in range(bodies - 1))
            for common_weight in (2, 3):
                for target in itertools.product(
                    range(-3, 4),
                    repeat=bodies - 1,
                ):
                    if any(value % common_weight for value in target):
                        expected = False
                    else:
                        reduced = tuple(
                            value // common_weight for value in target
                        )
                        weighted_sum = sum(
                            (bodies - 1 - edge) * value
                            for edge, value in enumerate(reduced)
                        )
                        expected = weighted_sum % bodies == 0
                    self.assertEqual(
                        weighted_forest_target_is_reachable(
                            bodies,
                            edges,
                            (common_weight,) * bodies,
                            target,
                        ),
                        expected,
                    )

    def test_weighted_forest_determinant_multiplies_component_indices(self):
        weights = (2, 3, 5, 7)
        expected = (2 + 3) * (5 + 7)
        self.assertEqual(
            weighted_forest_contact_gram_determinant(
                4,
                SPLIT22,
                weights,
            ),
            expected,
        )

    def test_report_returns_unique_integer_impulse(self):
        gram = weighted_forest_contact_gram(
            3,
            PATH3,
            (2, 3, 5),
        )
        # Generate a target from a known integer impulse so reachability is certain.
        target = apply_integer_matrix(gram, (2, -1))
        report = weighted_forest_reachability_report(
            3,
            PATH3,
            (2, 3, 5),
            target,
        )
        self.assertTrue(report.reachable)
        self.assertEqual(report.unique_integer_impulse, (2, -1))
        self.assertEqual(report.determinant, 31)

    def test_validation(self):
        with self.assertRaises(ValueError):
            weighted_forest_contact_gram(
                3,
                PATH3,
                (1, 0, 2),
            )
        with self.assertRaises(ValueError):
            weighted_forest_contact_gram(
                3,
                ((0, 1), (1, 2), (2, 0)),
                (1, 1, 1),
            )
        with self.assertRaises(ValueError):
            common_weight_tree_cokernel_invariant_factors(1, 2)


if __name__ == "__main__":
    unittest.main()
