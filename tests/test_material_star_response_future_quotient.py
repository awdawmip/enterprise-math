import itertools
import unittest

from enterprise_math.material_star_response_future_quotient import (
    star_minimum_response_symmetry_orbits,
    star_permutation_invariant_residual_observables,
    star_residual_partition_signature,
    star_response_quotient_report,
)
from enterprise_math.material_star_response_precision_phase import (
    star_minimum_response_relation_at_precision,
    star_response_refinement_phase,
    star_symmetric_minimum_numerators,
)


def integer_partitions(value, maximum=None):
    if value == 0:
        yield ()
        return
    if maximum is None or maximum > value:
        maximum = value
    for first in range(maximum, 0, -1):
        for tail in integer_partitions(value - first, first):
            yield (first,) + tail


class MaterialStarResponseFutureQuotientTests(unittest.TestCase):
    def test_orbit_signatures_are_exact_integer_partitions_of_residue(self):
        checked = 0
        for k in range(2, 9):
            for q in range(1, 7):
                for s in range(1, 9):
                    phase = star_response_refinement_phase(k, q, s)
                    orbits = set(
                        star_minimum_response_symmetry_orbits(k, q, s)
                    )
                    expected = set(integer_partitions(phase.residue))
                    self.assertEqual(orbits, expected)
                    checked += 1
        self.assertGreater(checked, 250)

    def test_signature_is_exactly_permutation_invariant(self):
        vector = (5, 3, 4, 3)
        baseline = 3
        expected = (2, 1)
        signatures = {
            star_residual_partition_signature(permutation, baseline)
            for permutation in itertools.permutations(vector)
        }
        self.assertEqual(signatures, {expected})

    def test_residue_determines_three_determinism_layers(self):
        seen = set()
        for k in range(2, 9):
            for q in range(1, 7):
                for s in range(1, 10):
                    report = star_response_quotient_report(k, q, s)
                    if report.residue == 0:
                        self.assertEqual(report.determinism_class, "LABELED_UNIQUE")
                        self.assertTrue(report.labeled_unique)
                        self.assertTrue(report.permutation_quotient_unique)
                    elif report.residue == 1:
                        self.assertEqual(
                            report.determinism_class,
                            "PERMUTATION_QUOTIENT_UNIQUE",
                        )
                        self.assertFalse(report.labeled_unique)
                        self.assertTrue(report.permutation_quotient_unique)
                        self.assertEqual(report.labeled_minimum_count, k)
                    else:
                        self.assertEqual(
                            report.determinism_class,
                            "RELATION_VALUED_AFTER_QUOTIENT",
                        )
                        self.assertFalse(report.permutation_quotient_unique)
                    seen.add(report.determinism_class)
        self.assertEqual(
            seen,
            {
                "LABELED_UNIQUE",
                "PERMUTATION_QUOTIENT_UNIQUE",
                "RELATION_VALUED_AFTER_QUOTIENT",
            },
        )

    def test_r_equals_k_has_symmetric_minimum_but_still_multiple_orbits(self):
        for k in range(2, 9):
            # q=1,s=k gives residue exactly k.
            report = star_response_quotient_report(k, 1, k)
            self.assertEqual(report.residue, k)
            self.assertTrue(report.symmetric_minimum_exists)
            self.assertEqual(report.symmetric_minimum_orbit, (1,) * k)
            self.assertIn((1,) * k, report.orbit_signatures)
            self.assertIn((k,), report.orbit_signatures)
            self.assertGreater(report.permutation_orbit_count, 1)
            self.assertEqual(
                report.determinism_class,
                "RELATION_VALUED_AFTER_QUOTIENT",
            )

    def test_total_residue_is_not_future_complete_for_r_at_least_two(self):
        for k in range(2, 9):
            for residue in range(2, k + 1):
                # Choose q=1,s=residue while residue<k+1.
                phase = star_response_refinement_phase(k, 1, residue)
                self.assertEqual(phase.residue, residue)
                relation = star_minimum_response_relation_at_precision(k, 1, residue)
                observations = {
                    star_permutation_invariant_residual_observables(
                        vector, phase.quotient_level
                    )
                    for vector in relation
                }
                totals = {observable[0] for observable in observations}
                maxima = {observable[1] for observable in observations}
                self.assertEqual(totals, {residue})
                self.assertGreater(len(maxima), 1)
                self.assertIn(residue, maxima)
                self.assertIn(residue - 1, maxima)

    def test_reference_k3_q1_precision_sequence(self):
        expected = {
            1: (1, 3, 1, "PERMUTATION_QUOTIENT_UNIQUE"),
            2: (2, 6, 2, "RELATION_VALUED_AFTER_QUOTIENT"),
            3: (3, 10, 3, "RELATION_VALUED_AFTER_QUOTIENT"),
            4: (0, 1, 1, "LABELED_UNIQUE"),
        }
        for denominator, (residue, labeled, orbits, kind) in expected.items():
            report = star_response_quotient_report(3, 1, denominator)
            self.assertEqual(report.residue, residue)
            self.assertEqual(report.labeled_minimum_count, labeled)
            self.assertEqual(report.permutation_orbit_count, orbits)
            self.assertEqual(report.determinism_class, kind)

        self.assertIsNone(star_symmetric_minimum_numerators(3, 1, 1))
        self.assertEqual(
            star_symmetric_minimum_numerators(3, 1, 3),
            (1, 1, 1),
        )
        # Symmetric representative at s=3 does not collapse the relation itself.
        self.assertEqual(
            set(star_minimum_response_symmetry_orbits(3, 1, 3)),
            {(3,), (2, 1), (1, 1, 1)},
        )

    def test_partition_signature_is_complete_for_labeled_permutation_orbit(self):
        vectors = (
            (4, 2, 2, 1),
            (1, 4, 2, 2),
            (3, 3, 2, 1),
            (5, 1, 2, 1),
        )
        baseline = 1
        signatures = [
            star_residual_partition_signature(vector, baseline)
            for vector in vectors
        ]
        self.assertEqual(signatures[0], signatures[1])
        self.assertNotEqual(signatures[0], signatures[2])
        self.assertNotEqual(signatures[0], signatures[3])

    def test_validation(self):
        with self.assertRaises(ValueError):
            star_residual_partition_signature((1,), 0)
        with self.assertRaises(ValueError):
            star_residual_partition_signature((0, 1), 1)
        with self.assertRaises(ValueError):
            star_residual_partition_signature((1, 1), -1)


if __name__ == "__main__":
    unittest.main()
