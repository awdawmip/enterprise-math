import unittest
from fractions import Fraction

from enterprise_math.precision_locality_obstruction import (
    SETTINGS,
    chsh_value,
    correlation_from_joint_counts,
    deterministic_chsh,
    local_chsh_bound_holds,
    local_joint_counts_for_setting,
    local_response_tables,
    maximum_setting_total_variation,
    max_l1_setting_distance,
    rational_singlet_correlations,
    rational_singlet_joint_counts,
    rational_target_measurement_dependence_minimum,
    rational_target_sharp_measurement_dependent_weights,
    relaxed_measurement_dependence_bound_holds,
    setting_dependent_chsh_numerator,
    setting_dependent_local_correlations,
    weighted_local_chsh,
    weighted_local_correlations,
)


class PrecisionLocalityObstructionTests(unittest.TestCase):
    def test_all_sixteen_local_deterministic_tables_saturate_chsh_at_two(self):
        values = tuple(deterministic_chsh(table) for table in local_response_tables())
        self.assertEqual(len(values), 16)
        self.assertEqual(set(values), {-2, 2})
        self.assertEqual(values.count(-2), 8)
        self.assertEqual(values.count(2), 8)

    def test_integer_weighted_local_mixtures_obey_cross_multiplied_bound(self):
        weight_families = (
            (1,) * 16,
            tuple(range(16)),
            tuple((index * index + 3 * index + 1) % 7 for index in range(16)),
            tuple(1 if index in (0, 3, 5, 11) else 0 for index in range(16)),
        )
        for weights in weight_families:
            numerator, total = weighted_local_chsh(weights)
            self.assertLessEqual(abs(numerator), 2 * total)
            self.assertTrue(local_chsh_bound_holds(weights))
            self.assertLessEqual(abs(chsh_value(weighted_local_correlations(weights))), 2)

    def test_rational_singlet_target_violates_local_bound_exactly(self):
        correlations = rational_singlet_correlations()
        self.assertEqual(
            correlations,
            {
                (0, 0): Fraction(-3, 5),
                (0, 1): Fraction(-3, 5),
                (1, 0): Fraction(-4, 5),
                (1, 1): Fraction(4, 5),
            },
        )
        self.assertEqual(chsh_value(correlations), Fraction(-14, 5))
        self.assertGreater(abs(chsh_value(correlations)), 2)

    def test_twenty_atom_joint_counts_are_exact_balanced_and_no_signalling(self):
        counts = rational_singlet_joint_counts()
        correlations = rational_singlet_correlations()
        for setting, table in counts.items():
            self.assertEqual(sum(table.values()), 20)
            self.assertEqual(correlation_from_joint_counts(table), correlations[setting])
            self.assertEqual(table[(-1, -1)] + table[(-1, 1)], 10)
            self.assertEqual(table[(1, -1)] + table[(1, 1)], 10)
            self.assertEqual(table[(-1, -1)] + table[(1, -1)], 10)
            self.assertEqual(table[(-1, 1)] + table[(1, 1)], 10)

        # Alice's marginal for a fixed x is the same for y=0 and y=1;
        # Bob's marginal for fixed y is the same for x=0 and x=1.
        for x in (0, 1):
            for a in (-1, 1):
                left = sum(counts[(x, 0)][(a, b)] for b in (-1, 1))
                right = sum(counts[(x, 1)][(a, b)] for b in (-1, 1))
                self.assertEqual(left, right)
        for y in (0, 1):
            for b in (-1, 1):
                left = sum(counts[(0, y)][(a, b)] for a in (-1, 1))
                right = sum(counts[(1, y)][(a, b)] for a in (-1, 1))
                self.assertEqual(left, right)

        self.assertEqual(counts[(0, 0)], {(-1, -1): 2, (-1, 1): 8, (1, -1): 8, (1, 1): 2})
        self.assertEqual(counts[(0, 1)], counts[(0, 0)])
        self.assertEqual(counts[(1, 0)], {(-1, -1): 1, (-1, 1): 9, (1, -1): 9, (1, 1): 1})
        self.assertEqual(counts[(1, 1)], {(-1, -1): 9, (-1, 1): 1, (1, -1): 1, (1, 1): 9})

    def test_relaxed_measurement_dependence_bound_is_exact_integer_inequality(self):
        witness = rational_target_sharp_measurement_dependent_weights()
        numerator, total = setting_dependent_chsh_numerator(witness)
        distance = max_l1_setting_distance(witness)
        self.assertEqual(total, 60)
        self.assertEqual(abs(numerator), 168)
        self.assertEqual(distance, 16)
        self.assertEqual(2 * total + 3 * distance, 168)
        self.assertTrue(relaxed_measurement_dependence_bound_holds(witness))
        self.assertEqual(maximum_setting_total_variation(witness), Fraction(2, 15))

    def test_measurement_dependence_lower_bound_is_sharp_for_rational_target(self):
        witness = rational_target_sharp_measurement_dependent_weights()
        self.assertEqual(
            setting_dependent_local_correlations(witness),
            rational_singlet_correlations(),
        )
        target = rational_singlet_joint_counts()
        for setting in SETTINGS:
            self.assertEqual(
                local_joint_counts_for_setting(witness[setting], setting),
                {outcome: 3 * count for outcome, count in target[setting].items()},
            )
        self.assertEqual(rational_target_measurement_dependence_minimum(), Fraction(2, 15))

    def test_invalid_weights_fail_closed(self):
        with self.assertRaises(ValueError):
            weighted_local_chsh((1,) * 15)
        with self.assertRaises(ValueError):
            weighted_local_chsh((0,) * 16)
        with self.assertRaises(ValueError):
            weighted_local_chsh((-1,) + (1,) * 15)
        with self.assertRaises(ValueError):
            setting_dependent_local_correlations({setting: (1,) * 16 for setting in SETTINGS[:-1]})


if __name__ == "__main__":
    unittest.main()
