import itertools
import unittest

from enterprise_math.material_star_response_precision import (
    star_final_score_numerators,
    star_impulse_numerators_are_feasible,
    star_minimum_symmetric_integer_response,
    star_minimum_symmetric_refinement_denominator,
    star_minimum_total_integer_response_relation,
    star_refined_symmetric_minimum_response,
    star_response_precision_report,
)


class MaterialStarResponsePrecisionTests(unittest.TestCase):
    def test_minimum_total_integer_relation_is_exact_unit_orbit(self):
        for leaf_count in range(2, 9):
            relation = star_minimum_total_integer_response_relation(leaf_count)
            self.assertEqual(len(relation), leaf_count)
            self.assertEqual(len(set(relation)), leaf_count)
            self.assertTrue(all(sum(vector) == 1 for vector in relation))
            self.assertTrue(
                all(star_impulse_numerators_are_feasible(vector) for vector in relation)
            )
            self.assertFalse(
                star_impulse_numerators_are_feasible((0,) * leaf_count)
            )

    def test_bounded_integer_oracle_finds_no_other_total_one_minimizers(self):
        for leaf_count in range(2, 7):
            feasible_total_one = {
                candidate
                for candidate in itertools.product(range(2), repeat=leaf_count)
                if sum(candidate) == 1
                and star_impulse_numerators_are_feasible(candidate)
            }
            self.assertEqual(
                feasible_total_one,
                set(star_minimum_total_integer_response_relation(leaf_count)),
            )

    def test_minimum_response_relation_is_closed_under_leaf_permutations(self):
        for leaf_count in range(2, 7):
            relation = set(star_minimum_total_integer_response_relation(leaf_count))
            for vector in tuple(relation):
                for permutation in itertools.permutations(range(leaf_count)):
                    permuted = tuple(vector[index] for index in permutation)
                    self.assertIn(permuted, relation)

    def test_deterministic_permutation_fixed_integer_response_overresponds_by_leaf_count(self):
        for leaf_count in range(2, 10):
            symmetric = star_minimum_symmetric_integer_response(leaf_count)
            self.assertEqual(symmetric, (1,) * leaf_count)
            self.assertTrue(star_impulse_numerators_are_feasible(symmetric))
            self.assertEqual(sum(symmetric), leaf_count)
            report = star_response_precision_report(leaf_count)
            self.assertEqual(report.minimum_total_impulse, 1)
            self.assertEqual(report.coarse_symmetry_overresponse_factor, leaf_count)

    def test_refinement_denominator_leaf_count_is_exact_first_symmetric_total_one_scale(self):
        for leaf_count in range(2, 12):
            denominator = star_minimum_symmetric_refinement_denominator(leaf_count)
            self.assertEqual(denominator, leaf_count)
            returned_denominator, numerators = star_refined_symmetric_minimum_response(
                leaf_count
            )
            self.assertEqual(returned_denominator, leaf_count)
            self.assertEqual(numerators, (1,) * leaf_count)
            self.assertEqual(sum(numerators), returned_denominator)
            self.assertTrue(
                star_impulse_numerators_are_feasible(numerators, returned_denominator)
            )

            # A symmetric total-one rational vector c/s requires s=k*c, so no
            # smaller positive denominator can represent it at all.
            for smaller in range(1, leaf_count):
                representable = any(
                    leaf_count * numerator == smaller
                    for numerator in range(smaller + 1)
                )
                self.assertFalse(representable)

    def test_refined_symmetric_score_numerator_is_exactly_one_on_every_contact(self):
        for leaf_count in range(2, 10):
            denominator, numerators = star_refined_symmetric_minimum_response(
                leaf_count
            )
            self.assertEqual(
                star_final_score_numerators(numerators, denominator),
                (1,) * leaf_count,
            )

    def test_report_recovers_exact_star_gram_and_relation(self):
        for leaf_count in range(2, 8):
            report = star_response_precision_report(leaf_count)
            self.assertEqual(report.initial_scores, (-1,) * leaf_count)
            self.assertEqual(
                report.coupling_gram,
                tuple(
                    tuple(2 if row == col else 1 for col in range(leaf_count))
                    for row in range(leaf_count)
                ),
            )
            self.assertEqual(
                set(report.minimum_relation),
                set(star_minimum_total_integer_response_relation(leaf_count)),
            )

    def test_invalid_precision_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            star_minimum_total_integer_response_relation(1)
        with self.assertRaises(ValueError):
            star_minimum_symmetric_refinement_denominator(True)
        with self.assertRaises(ValueError):
            star_final_score_numerators((1,), 1)
        with self.assertRaises(ValueError):
            star_final_score_numerators((1, 1), 0)
        with self.assertRaises(ValueError):
            star_final_score_numerators((1, -1), 2)


if __name__ == "__main__":
    unittest.main()
