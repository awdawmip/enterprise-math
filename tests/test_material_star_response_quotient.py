import itertools
import unittest

from enterprise_math.material_star_response_quotient import (
    integer_partition_number,
    star_coarse_symmetric_minimum_exists_from_residue,
    star_identity_quotient_is_single_valued,
    star_minimum_unlabeled_orbit_count,
    star_minimum_unlabeled_response_shapes,
    star_residue_symmetric_refinement,
    star_response_quotient_report,
    star_response_residue,
)
from enterprise_math.material_star_response_spectrum import (
    star_minimum_symmetric_refinement,
    star_minimum_total_integer_relation,
    star_response_spectrum_report,
)


class MaterialStarResponseQuotientTests(unittest.TestCase):
    def test_parent_star_parameters_reduce_to_q_mod_k_plus_one(self):
        for leaf_count in range(2, 13):
            for closing_score in range(1, 60):
                baseline, residue = star_response_residue(
                    leaf_count, closing_score
                )
                self.assertEqual(
                    closing_score,
                    (leaf_count + 1) * baseline + residue,
                )
                parent = star_response_spectrum_report(
                    leaf_count, closing_score
                )
                self.assertEqual(parent.baseline_impulse, baseline)
                self.assertEqual(parent.composition_excess, residue)
                self.assertEqual(
                    parent.minimum_total_impulse,
                    leaf_count * baseline + residue,
                )

    def test_unlabeled_shapes_are_exact_permutation_orbits_of_labeled_relation(self):
        for leaf_count in range(2, 7):
            for closing_score in range(1, 12):
                relation = star_minimum_total_integer_relation(
                    leaf_count, closing_score
                )
                canonicalized = {
                    tuple(sorted(vector, reverse=True))
                    for vector in relation
                }
                self.assertEqual(
                    canonicalized,
                    set(
                        star_minimum_unlabeled_response_shapes(
                            leaf_count, closing_score
                        )
                    ),
                )

    def test_unlabeled_orbit_count_is_partition_number_of_residue(self):
        known_partition_numbers = (1, 1, 2, 3, 5, 7, 11, 15, 22)
        for total, expected in enumerate(known_partition_numbers):
            self.assertEqual(integer_partition_number(total), expected)
        for leaf_count in range(2, 9):
            for closing_score in range(1, 30):
                _, residue = star_response_residue(
                    leaf_count, closing_score
                )
                self.assertEqual(
                    star_minimum_unlabeled_orbit_count(
                        leaf_count, closing_score
                    ),
                    integer_partition_number(residue),
                )

    def test_identity_coarsening_is_single_valued_exactly_for_residue_zero_or_one(self):
        for leaf_count in range(2, 12):
            for closing_score in range(1, 50):
                _, residue = star_response_residue(
                    leaf_count, closing_score
                )
                self.assertEqual(
                    star_identity_quotient_is_single_valued(
                        leaf_count, closing_score
                    ),
                    residue <= 1,
                )

    def test_q_one_has_one_unlabeled_shape_but_q_two_can_have_more(self):
        for leaf_count in range(2, 10):
            self.assertEqual(
                star_minimum_unlabeled_orbit_count(leaf_count, 1),
                1,
            )
        self.assertEqual(star_response_residue(3, 2), (0, 2))
        self.assertEqual(
            set(star_minimum_unlabeled_response_shapes(3, 2)),
            {(2, 0, 0), (1, 1, 0)},
        )
        self.assertFalse(star_identity_quotient_is_single_valued(3, 2))

    def test_existence_of_symmetric_minimizer_does_not_make_whole_relation_single_valued(self):
        # k=3,q=3 has residue R=3: (1,1,1) is a symmetric minimum, but the
        # minimum relation has the three unlabeled shapes 3, 2+1, 1+1+1.
        report = star_response_quotient_report(3, 3)
        self.assertTrue(report.coarse_symmetric_minimum_exists)
        self.assertFalse(report.identity_quotient_single_valued)
        self.assertEqual(report.unlabeled_orbit_count, 3)
        self.assertEqual(
            set(report.unlabeled_shapes),
            {(3, 0, 0), (2, 1, 0), (1, 1, 1)},
        )

    def test_coarse_symmetric_minimum_residue_criterion_matches_parent_owner(self):
        for leaf_count in range(2, 12):
            for closing_score in range(1, 60):
                _, residue = star_response_residue(
                    leaf_count, closing_score
                )
                expected = residue in (0, leaf_count)
                self.assertEqual(
                    star_coarse_symmetric_minimum_exists_from_residue(
                        leaf_count, closing_score
                    ),
                    expected,
                )
                self.assertEqual(
                    star_response_spectrum_report(
                        leaf_count, closing_score
                    ).coarse_symmetric_minimum_exists,
                    expected,
                )

    def test_symmetric_refinement_denominator_and_surplus_depend_only_on_residue(self):
        for leaf_count in range(2, 15):
            by_residue = {}
            for closing_score in range(1, 80):
                _, residue = star_response_residue(
                    leaf_count, closing_score
                )
                denominator, surplus = star_residue_symmetric_refinement(
                    leaf_count, closing_score
                )
                parent_denominator, _ = star_minimum_symmetric_refinement(
                    leaf_count, closing_score
                )
                self.assertEqual(denominator, parent_denominator)
                current = (denominator, surplus)
                if residue in by_residue:
                    self.assertEqual(by_residue[residue], current)
                else:
                    by_residue[residue] = current

    def test_relation_and_precision_pattern_is_periodic_after_uniform_baseline_shift(self):
        for leaf_count in range(2, 9):
            period = leaf_count + 1
            for closing_score in range(1, 20):
                left = star_response_quotient_report(
                    leaf_count, closing_score
                )
                right = star_response_quotient_report(
                    leaf_count, closing_score + period
                )
                self.assertEqual(left.residue, right.residue)
                self.assertEqual(
                    right.uniform_baseline,
                    left.uniform_baseline + 1,
                )
                self.assertEqual(
                    left.unlabeled_orbit_count,
                    right.unlabeled_orbit_count,
                )
                self.assertEqual(
                    left.identity_quotient_single_valued,
                    right.identity_quotient_single_valued,
                )
                self.assertEqual(
                    left.symmetric_refinement_denominator,
                    right.symmetric_refinement_denominator,
                )
                self.assertEqual(
                    tuple(tuple(value + 1 for value in shape) for shape in left.unlabeled_shapes),
                    right.unlabeled_shapes,
                )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            integer_partition_number(-1)
        with self.assertRaises(ValueError):
            star_response_residue(1, 1)
        with self.assertRaises(ValueError):
            star_response_residue(3, 0)
        with self.assertRaises(ValueError):
            star_response_residue(True, 2)


if __name__ == "__main__":
    unittest.main()
