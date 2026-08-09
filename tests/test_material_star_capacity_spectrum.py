import itertools
import unittest

from enterprise_math.material_star_capacity_spectrum import (
    STAR_CAPACITY_INSUFFICIENT,
    STAR_CAPACITY_RESOLVED,
    star_capacity_minimum_relation,
    star_capacity_minimum_total,
    star_capacity_spectrum_report,
    star_capacity_vector_is_feasible,
)
from enterprise_math.material_star_response_spectrum import (
    star_minimum_total_impulse,
)


class MaterialStarCapacitySpectrumTests(unittest.TestCase):
    def test_closed_form_minimum_matches_direct_capacity_box_enumeration(self):
        checked = 0
        for leaf_count in range(2, 6):
            for closing_score in range(1, 8):
                for capacities in itertools.product(range(4), repeat=leaf_count):
                    predicted = star_capacity_minimum_total(
                        leaf_count, closing_score, capacities
                    )
                    direct = None
                    for vector in itertools.product(
                        *(range(limit + 1) for limit in capacities)
                    ):
                        if not star_capacity_vector_is_feasible(
                            vector, closing_score, capacities
                        ):
                            continue
                        total = sum(vector)
                        direct = total if direct is None else min(direct, total)
                    self.assertEqual(predicted, direct)
                    if direct is not None:
                        relation = star_capacity_minimum_relation(
                            leaf_count, closing_score, capacities
                        )
                        direct_relation = {
                            vector
                            for vector in itertools.product(
                                *(range(limit + 1) for limit in capacities)
                            )
                            if sum(vector) == direct
                            and star_capacity_vector_is_feasible(
                                vector, closing_score, capacities
                            )
                        }
                        self.assertEqual(set(relation), direct_relation)
                    checked += 1
        self.assertGreater(checked, 5000)

    def test_asymmetric_capacity_can_raise_minimum_total_then_refinement_lowers_it(self):
        low = star_capacity_spectrum_report(3, 5, (5, 0, 0))
        high = star_capacity_spectrum_report(3, 5, (5, 1, 1))
        self.assertEqual(low.unconstrained_minimum_total, 4)
        self.assertEqual(low.constrained_minimum_total, 5)
        self.assertEqual(low.capacity_penalty, 1)
        self.assertEqual(low.response_relation, ((5, 0, 0),))
        self.assertEqual(high.constrained_minimum_total, 4)
        self.assertEqual(high.capacity_penalty, 0)
        self.assertEqual(high.response_relation, ((2, 1, 1),))
        self.assertTrue(
            star_capacity_vector_is_feasible((5, 0, 0), 5, (5, 1, 1))
        )
        self.assertNotIn((5, 0, 0), high.response_relation)

    def test_equal_capacity_threshold_is_ceil_q_over_k_plus_one(self):
        for leaf_count in range(2, 12):
            for closing_score in range(1, 30):
                threshold = (
                    closing_score + leaf_count
                ) // (leaf_count + 1)
                for capacity in range(threshold):
                    self.assertIsNone(
                        star_capacity_minimum_total(
                            leaf_count,
                            closing_score,
                            (capacity,) * leaf_count,
                        )
                    )
                resolved = star_capacity_spectrum_report(
                    leaf_count,
                    closing_score,
                    (threshold,) * leaf_count,
                )
                self.assertTrue(resolved.resolved)
                self.assertEqual(
                    resolved.constrained_minimum_total,
                    star_minimum_total_impulse(leaf_count, closing_score),
                )

    def test_capacity_refinement_makes_minimum_total_weakly_decrease(self):
        for leaf_count in range(2, 6):
            for closing_score in range(1, 10):
                for low in itertools.product(range(3), repeat=leaf_count):
                    high = tuple(value + 1 for value in low)
                    low_total = star_capacity_minimum_total(
                        leaf_count, closing_score, low
                    )
                    high_total = star_capacity_minimum_total(
                        leaf_count, closing_score, high
                    )
                    if low_total is not None:
                        self.assertIsNotNone(high_total)
                        self.assertLessEqual(high_total, low_total)

    def test_minimum_relation_itself_is_not_inclusion_monotone_under_capacity_refinement(self):
        low = star_capacity_minimum_relation(3, 5, (5, 0, 0))
        high = star_capacity_minimum_relation(3, 5, (5, 1, 1))
        self.assertEqual(low, ((5, 0, 0),))
        self.assertEqual(high, ((2, 1, 1),))
        self.assertFalse(set(low).issubset(set(high)))
        self.assertTrue(star_capacity_vector_is_feasible(low[0], 5, (5, 1, 1)))

    def test_q_two_unit_capacity_keeps_only_split_shape_orbit(self):
        report = star_capacity_spectrum_report(3, 2, (1, 1, 1))
        self.assertEqual(report.status, STAR_CAPACITY_RESOLVED)
        self.assertEqual(report.constrained_minimum_total, 2)
        self.assertEqual(
            set(report.response_relation),
            {(1, 1, 0), (1, 0, 1), (0, 1, 1)},
        )

    def test_insufficient_capacity_is_exact_formula_not_search_failure(self):
        report = star_capacity_spectrum_report(3, 1, (0, 0, 0))
        self.assertEqual(report.status, STAR_CAPACITY_INSUFFICIENT)
        self.assertFalse(report.resolved)
        self.assertIsNone(report.constrained_minimum_total)
        self.assertIsNone(report.capacity_penalty)
        self.assertEqual(report.response_relation, ())

    def test_capacity_floor_formula_matches_report(self):
        for leaf_count in range(2, 8):
            for closing_score in range(1, 15):
                for capacities in (
                    (0,) * leaf_count,
                    (1,) * leaf_count,
                    tuple(range(leaf_count)),
                    tuple(reversed(range(leaf_count))),
                ):
                    report = star_capacity_spectrum_report(
                        leaf_count, closing_score, capacities
                    )
                    predicted = max(
                        report.unconstrained_minimum_total,
                        closing_score - report.minimum_capacity,
                    )
                    if predicted <= report.total_capacity:
                        self.assertEqual(report.constrained_minimum_total, predicted)
                        self.assertEqual(
                            report.lower_impulse_floor,
                            max(0, closing_score - predicted),
                        )
                    else:
                        self.assertIsNone(report.constrained_minimum_total)

    def test_validation(self):
        with self.assertRaises(ValueError):
            star_capacity_minimum_total(1, 1, (1,))
        with self.assertRaises(ValueError):
            star_capacity_minimum_total(3, 0, (1, 1, 1))
        with self.assertRaises(ValueError):
            star_capacity_minimum_total(3, 1, (1, 1))
        with self.assertRaises(ValueError):
            star_capacity_minimum_total(3, 1, (1, -1, 1))
        with self.assertRaises(ValueError):
            star_capacity_vector_is_feasible((1,), 1, (1,))
        with self.assertRaises(ValueError):
            star_capacity_vector_is_feasible((1, -1), 1, (1, 1))


if __name__ == "__main__":
    unittest.main()
