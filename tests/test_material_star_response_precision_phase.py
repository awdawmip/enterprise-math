import itertools
import math
import unittest

from enterprise_math.material_star_response_precision_phase import (
    star_first_symmetric_minimum_denominator,
    star_general_final_score_numerators,
    star_least_symmetric_feasible_numerators,
    star_minimum_response_relation_at_precision,
    star_minimum_total_numerator_at_precision,
    star_refinement_phase_period,
    star_response_refinement_phase,
    star_scaled_closing_phase,
    star_symmetric_minimum_numerators,
    star_true_refinement_cost_drop_cross_numerator,
)


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, length - 1):
            yield (first,) + tail


def feasible(vector, q, s):
    return all(
        score >= 0
        for score in star_general_final_score_numerators(vector, q, s)
    )


def brute_minimum_relation(k, q, s):
    claimed = star_minimum_total_numerator_at_precision(k, q, s)
    for total in range(claimed + 1):
        candidates = tuple(
            vector
            for vector in compositions(total, k)
            if feasible(vector, q, s)
        )
        if candidates:
            return total, candidates
    raise AssertionError("bounded star oracle found no feasible response")


class MaterialStarResponsePrecisionPhaseTests(unittest.TestCase):
    def test_closed_form_matches_independent_minimum_relation_oracle(self):
        checked = 0
        for k in range(2, 5):
            for q in range(1, 4):
                for s in range(1, 6):
                    t, residue = star_scaled_closing_phase(k, q, s)
                    expected_total = k * t + residue
                    formula = star_minimum_total_numerator_at_precision(k, q, s)
                    self.assertEqual(formula, expected_total)

                    brute_total, brute_relation = brute_minimum_relation(k, q, s)
                    relation = star_minimum_response_relation_at_precision(k, q, s)
                    self.assertEqual(brute_total, formula)
                    self.assertEqual(set(brute_relation), set(relation))
                    checked += 1
        self.assertGreater(checked, 40)

    def test_residue_is_exact_unavoidable_outward_score_witness(self):
        for k in range(2, 7):
            for q in range(1, 5):
                for s in range(1, 8):
                    t, residue = star_scaled_closing_phase(k, q, s)
                    relation = star_minimum_response_relation_at_precision(k, q, s)
                    self.assertEqual(
                        len(relation),
                        math.comb(residue + k - 1, k - 1),
                    )
                    for vector in relation:
                        residual_distribution = tuple(value - t for value in vector)
                        self.assertEqual(sum(residual_distribution), residue)
                        self.assertTrue(all(value >= 0 for value in residual_distribution))
                        self.assertEqual(
                            star_general_final_score_numerators(vector, q, s),
                            residual_distribution,
                        )

    def test_symmetry_minimum_gate_is_exact_modular_condition(self):
        for k in range(2, 9):
            modulus = k + 1
            for q in range(1, 9):
                for s in range(1, 13):
                    phase = star_response_refinement_phase(k, q, s)
                    scaled = q * s
                    modular_gate = scaled % modulus == 0 or (scaled + 1) % modulus == 0
                    self.assertEqual(phase.symmetry_minimum_compatible, modular_gate)
                    self.assertEqual(
                        star_symmetric_minimum_numerators(k, q, s) is not None,
                        modular_gate,
                    )
                    if phase.residue == 0:
                        self.assertEqual(phase.symmetric_overresponse_numerator, 0)
                        self.assertTrue(phase.zero_excess_gate)
                    else:
                        self.assertEqual(
                            phase.symmetric_overresponse_numerator,
                            k - phase.residue,
                        )
                    if phase.residue == k:
                        self.assertTrue(phase.one_excess_gate)
                        self.assertEqual(
                            star_general_final_score_numerators(
                                phase.symmetric_minimum_numerators, q, s
                            ),
                            (1,) * k,
                        )

    def test_q_one_recovers_and_extends_previous_star_precision_result(self):
        for k in range(2, 9):
            self.assertEqual(star_first_symmetric_minimum_denominator(k, 1), k)

            first = star_response_refinement_phase(k, 1, k)
            self.assertEqual(first.residue, k)
            self.assertEqual(first.minimum_total_numerator, k)
            self.assertEqual(first.symmetric_minimum_numerators, (1,) * k)
            self.assertEqual(
                star_general_final_score_numerators((1,) * k, 1, k),
                (1,) * k,
            )

            zero_gate = star_response_refinement_phase(k, 1, k + 1)
            self.assertEqual(zero_gate.residue, 0)
            self.assertEqual(zero_gate.minimum_total_numerator, k)
            self.assertEqual(zero_gate.symmetric_minimum_numerators, (1,) * k)
            self.assertEqual(
                star_general_final_score_numerators((1,) * k, 1, k + 1),
                (0,) * k,
            )
            # k/(k+1) is strictly below the coarse integer minimum 1.
            self.assertLess(zero_gate.minimum_total_numerator, zero_gate.denominator)

    def test_residue_phase_has_exact_gcd_period(self):
        for k in range(2, 10):
            for q in range(1, 10):
                period = star_refinement_phase_period(k, q)
                residues = [
                    star_response_refinement_phase(k, q, s).residue
                    for s in range(1, period + 1)
                ]
                self.assertEqual(
                    residues,
                    [
                        star_response_refinement_phase(k, q, s + period).residue
                        for s in range(1, period + 1)
                    ],
                )
                for smaller in range(1, period):
                    if all(
                        star_response_refinement_phase(k, q, s).residue
                        == star_response_refinement_phase(k, q, s + smaller).residue
                        for s in range(1, period + 1)
                    ):
                        self.fail("reported residue period was not minimal")

    def test_first_symmetric_denominator_matches_bounded_modular_oracle(self):
        for k in range(2, 12):
            for q in range(1, 12):
                expected = next(
                    s
                    for s in range(1, k + 2)
                    if (q * s) % (k + 1) in (0, k)
                )
                self.assertEqual(
                    star_first_symmetric_minimum_denominator(k, q),
                    expected,
                )

    def test_true_divisibility_refinement_never_increases_minimum_physical_cost(self):
        checked = 0
        for k in range(2, 8):
            for q in range(1, 6):
                for coarse in range(1, 7):
                    coarse_relation = star_minimum_response_relation_at_precision(k, q, coarse)
                    for multiplier in range(1, 6):
                        fine = coarse * multiplier
                        drop = star_true_refinement_cost_drop_cross_numerator(
                            k, q, coarse, fine
                        )
                        self.assertGreaterEqual(drop, 0)
                        coarse_total = star_minimum_total_numerator_at_precision(k, q, coarse)
                        fine_total = star_minimum_total_numerator_at_precision(k, q, fine)
                        self.assertLessEqual(
                            fine_total * coarse,
                            coarse_total * fine,
                        )
                        scaled_old = tuple(
                            multiplier * value for value in coarse_relation[0]
                        )
                        self.assertTrue(feasible(scaled_old, q, fine))
                        checked += 1
        self.assertGreater(checked, 500)

    def test_larger_denominator_is_not_itself_a_refinement_order(self):
        # k=3,q=1: s=4 has exact minimum 3/4; s=5 has minimum 4/5.
        left_total = star_minimum_total_numerator_at_precision(3, 1, 4)
        right_total = star_minimum_total_numerator_at_precision(3, 1, 5)
        self.assertEqual((left_total, right_total), (3, 4))
        self.assertGreater(right_total * 4, left_total * 5)
        with self.assertRaises(ValueError):
            star_true_refinement_cost_drop_cross_numerator(3, 1, 4, 5)

    def test_least_symmetric_feasible_vector_has_exact_overresponse(self):
        for k in range(2, 8):
            for q in range(1, 6):
                for s in range(1, 9):
                    phase = star_response_refinement_phase(k, q, s)
                    vector = star_least_symmetric_feasible_numerators(k, q, s)
                    self.assertTrue(feasible(vector, q, s))
                    self.assertEqual(
                        sum(vector) - phase.minimum_total_numerator,
                        phase.symmetric_overresponse_numerator,
                    )

    def test_validation(self):
        with self.assertRaises(ValueError):
            star_response_refinement_phase(1, 1, 1)
        with self.assertRaises(ValueError):
            star_response_refinement_phase(3, 0, 1)
        with self.assertRaises(ValueError):
            star_response_refinement_phase(3, 1, 0)
        with self.assertRaises(ValueError):
            star_general_final_score_numerators((0, -1, 0), 1, 1)
        with self.assertRaises(ValueError):
            star_true_refinement_cost_drop_cross_numerator(3, 1, 4, 6)


if __name__ == "__main__":
    unittest.main()
