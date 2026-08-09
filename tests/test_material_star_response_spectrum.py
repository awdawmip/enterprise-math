import itertools
import unittest

from enterprise_math.material_star_response_spectrum import (
    star_minimum_relation_cardinality,
    star_minimum_relation_parameters,
    star_minimum_symmetric_integer_total,
    star_minimum_symmetric_refinement,
    star_minimum_total_has_symmetric_integer_selector,
    star_minimum_total_impulse,
    star_minimum_total_integer_relation,
    star_response_spectrum_report,
    star_score_vector,
)


class MaterialStarResponseSpectrumTests(unittest.TestCase):
    def test_closed_form_minimum_matches_bounded_integer_oracle(self):
        for leaf_count in range(2, 7):
            for closing_score in range(1, 9):
                expected = star_minimum_total_impulse(leaf_count, closing_score)
                best = None
                minimizers = []
                # Minimum total is small; enumerate by total rather than a full box.
                for total in range(expected + 1):
                    candidates = (
                        candidate
                        for candidate in itertools.product(
                            range(total + 1), repeat=leaf_count
                        )
                        if sum(candidate) == total
                    )
                    feasible = [
                        candidate
                        for candidate in candidates
                        if all(
                            score >= 0
                            for score in star_score_vector(candidate, closing_score)
                        )
                    ]
                    if feasible:
                        best = total
                        minimizers = feasible
                        break
                self.assertEqual(best, expected)
                self.assertEqual(
                    set(minimizers),
                    set(
                        star_minimum_total_integer_relation(
                            leaf_count, closing_score
                        )
                    ),
                )

    def test_minimum_relation_is_baseline_plus_weak_composition(self):
        for leaf_count in range(2, 9):
            for closing_score in range(1, 15):
                total, baseline, excess = star_minimum_relation_parameters(
                    leaf_count, closing_score
                )
                relation = star_minimum_total_integer_relation(
                    leaf_count, closing_score
                )
                self.assertTrue(relation)
                self.assertTrue(all(sum(vector) == total for vector in relation))
                self.assertTrue(
                    all(
                        all(value >= baseline for value in vector)
                        for vector in relation
                    )
                )
                self.assertTrue(
                    all(
                        sum(value - baseline for value in vector) == excess
                        for vector in relation
                    )
                )
                self.assertEqual(
                    len(relation),
                    star_minimum_relation_cardinality(leaf_count, closing_score),
                )

    def test_coarse_symmetric_minimum_exists_exactly_when_minimum_total_is_divisible_by_leaf_count(self):
        for leaf_count in range(2, 12):
            for closing_score in range(1, 30):
                minimum = star_minimum_total_impulse(leaf_count, closing_score)
                self.assertEqual(
                    star_minimum_total_has_symmetric_integer_selector(
                        leaf_count, closing_score
                    ),
                    minimum % leaf_count == 0,
                )
                symmetric_total = star_minimum_symmetric_integer_total(
                    leaf_count, closing_score
                )
                self.assertGreaterEqual(symmetric_total, minimum)
                if minimum % leaf_count == 0:
                    self.assertEqual(symmetric_total, minimum)

    def test_refined_symmetric_denominator_is_reduced_minimum_over_leaf_count(self):
        for leaf_count in range(2, 15):
            for closing_score in range(1, 30):
                minimum = star_minimum_total_impulse(leaf_count, closing_score)
                denominator, numerator = star_minimum_symmetric_refinement(
                    leaf_count, closing_score
                )
                self.assertEqual(
                    leaf_count * numerator,
                    denominator * minimum,
                )
                self.assertEqual(
                    __import__("math").gcd(denominator, numerator),
                    1,
                )
                score_numerator = (
                    -closing_score * denominator
                    + (leaf_count + 1) * numerator
                )
                self.assertGreaterEqual(score_numerator, 0)

    def test_q_one_specialization_recovers_leaf_count_denominator_and_unit_orbit(self):
        for leaf_count in range(2, 10):
            self.assertEqual(star_minimum_total_impulse(leaf_count, 1), 1)
            self.assertEqual(
                star_minimum_total_integer_relation(leaf_count, 1),
                tuple(
                    tuple(1 if index == selected else 0 for index in range(leaf_count))
                    for selected in range(leaf_count)
                ),
            )
            self.assertEqual(
                star_minimum_symmetric_refinement(leaf_count, 1),
                (leaf_count, 1),
            )

    def test_symmetry_obstruction_can_appear_and_disappear_with_closing_magnitude(self):
        # Three leaves: q=1,2 need refined symmetry; q=3,4 already admit a
        # symmetric minimum-total coarse response; q=5 needs refinement again.
        expected = {
            1: False,
            2: False,
            3: True,
            4: True,
            5: False,
        }
        for closing_score, coarse_exists in expected.items():
            self.assertEqual(
                star_minimum_total_has_symmetric_integer_selector(3, closing_score),
                coarse_exists,
            )

    def test_report_matches_relation_and_exact_final_score_numerator(self):
        for leaf_count in range(2, 9):
            for closing_score in range(1, 12):
                report = star_response_spectrum_report(leaf_count, closing_score)
                self.assertEqual(
                    report.minimum_relation_cardinality,
                    len(
                        star_minimum_total_integer_relation(
                            leaf_count, closing_score
                        )
                    ),
                )
                self.assertGreaterEqual(report.coarse_symmetry_overresponse, 0)
                self.assertGreaterEqual(report.refined_final_score_numerator, 0)
                self.assertEqual(
                    report.coarse_symmetric_minimum_exists,
                    report.coarse_symmetry_overresponse == 0,
                )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            star_minimum_total_impulse(1, 1)
        with self.assertRaises(ValueError):
            star_minimum_total_impulse(3, 0)
        with self.assertRaises(ValueError):
            star_score_vector((1,), 1)
        with self.assertRaises(ValueError):
            star_score_vector((1, -1), 2)
        with self.assertRaises(ValueError):
            star_minimum_symmetric_refinement(True, 2)


if __name__ == "__main__":
    unittest.main()
