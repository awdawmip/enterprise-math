import itertools
import unittest

from enterprise_math.contact_cycle_witness_repair import (
    contact_cycle_witness_repair_report,
)
from enterprise_math.contact_guarded_witness_normal_form import (
    apply_contact_guarded_witness_profile,
    compose_contact_guarded_witness_profiles,
    contact_guarded_witness_profile,
    contact_guarded_witness_profile_power,
    witnessed_profile_separating_state,
    zero_shift_witness_product,
)
from enterprise_math.contact_guarded_word_normal_form import (
    apply_contact_guarded_word,
    contact_word_action_counts,
)


CYCLE_K = (
    (2, -1, -1),
    (-1, 2, -1),
    (-1, -1, 2),
)
CYCLE_B = (
    (-1, 0, 1),
    (1, -1, 0),
    (0, 1, -1),
)


class ContactGuardedWitnessNormalFormTests(unittest.TestCase):
    def test_compiled_witnessed_profile_matches_literal_execution(self):
        witness_matrix = (
            (1, 0, 0),
            (0, 1, 1),
        )
        words = [()]
        for length in range(1, 5):
            words.extend(itertools.product(range(3), repeat=length))

        for word in words:
            profile = contact_guarded_witness_profile(
                CYCLE_K,
                witness_matrix,
                word,
            )
            counts = contact_word_action_counts(word, 3)
            expected_witness_shift = (
                counts[0],
                counts[1] + counts[2],
            )
            self.assertEqual(
                profile.witness_shift,
                expected_witness_shift,
            )
            for score in itertools.product(range(-3, 2), repeat=3):
                direct = apply_contact_guarded_word(
                    CYCLE_K,
                    score,
                    word,
                )
                compiled = apply_contact_guarded_witness_profile(
                    score,
                    (7, -2),
                    profile,
                )
                self.assertEqual(compiled.defined, direct.defined)
                if direct.defined:
                    self.assertEqual(compiled.score_state, direct.state)
                    self.assertEqual(
                        compiled.witness_state,
                        (
                            7 + expected_witness_shift[0],
                            -2 + expected_witness_shift[1],
                        ),
                    )

    def test_profile_product_matches_literal_concatenation(self):
        witness_matrix = ((1, 2, -1),)
        sample = (
            (),
            (0,),
            (1,),
            (2,),
            (0, 1),
            (2, 1, 0),
        )
        for first_word in sample:
            first = contact_guarded_witness_profile(
                CYCLE_K,
                witness_matrix,
                first_word,
            )
            for second_word in sample:
                second = contact_guarded_witness_profile(
                    CYCLE_K,
                    witness_matrix,
                    second_word,
                )
                self.assertEqual(
                    compose_contact_guarded_witness_profiles(
                        first,
                        second,
                    ),
                    contact_guarded_witness_profile(
                        CYCLE_K,
                        witness_matrix,
                        first_word + second_word,
                    ),
                )

    def test_triangle_full_witness_breaks_coarse_cycle_idempotence(self):
        profile = contact_guarded_witness_profile(
            CYCLE_K,
            (
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 1),
            ),
            (0, 1, 2),
        )
        self.assertTrue(profile.coarse_profile.is_partial_identity)
        self.assertEqual(profile.witness_shift, (1, 1, 1))
        self.assertFalse(profile.is_idempotent)

        for exponent in range(1, 8):
            power = contact_guarded_witness_profile_power(
                profile,
                exponent,
            )
            self.assertEqual(
                power.coarse_profile,
                profile.coarse_profile,
            )
            self.assertEqual(
                power.witness_shift,
                (exponent, exponent, exponent),
            )

    def test_triangle_difference_witness_kills_cycle_and_restores_idempotence(self):
        profile = contact_guarded_witness_profile(
            CYCLE_K,
            ((1, -1, 0),),
            (0, 1, 2),
        )
        self.assertEqual(profile.witness_shift, (0,))
        self.assertTrue(profile.is_idempotent)
        self.assertEqual(
            contact_guarded_witness_profile_power(profile, 9),
            profile,
        )

        report = contact_cycle_witness_repair_report(
            CYCLE_B,
            ((1, -1, 0),),
        )
        self.assertTrue(report.witness_descends_through_body_state)

    def test_triangle_total_witness_has_hidden_grain_three_and_infinite_powers(self):
        profile = contact_guarded_witness_profile(
            CYCLE_K,
            ((1, 1, 1),),
            (0, 1, 2),
        )
        self.assertEqual(profile.witness_shift, (3,))
        report = contact_cycle_witness_repair_report(
            CYCLE_B,
            ((1, 1, 1),),
        )
        self.assertFalse(report.witness_descends_through_body_state)
        self.assertEqual(report.scalar_hidden_grain, 3)

        powers = {
            contact_guarded_witness_profile_power(
                profile,
                exponent,
            ).witness_shift
            for exponent in range(1, 20)
        }
        self.assertEqual(len(powers), 19)

    def test_zero_shift_kernel_is_domain_semilattice_times_witness_addition(self):
        first = contact_guarded_witness_profile(
            CYCLE_K,
            ((1, 1, 1),),
            (0, 1, 2),
        )
        second = contact_guarded_witness_profile(
            CYCLE_K,
            ((1, 1, 1),),
            (1, 2, 0),
        )
        left = zero_shift_witness_product(first, second)
        right = zero_shift_witness_product(second, first)
        self.assertEqual(left, right)
        self.assertEqual(left.witness_shift, (6,))
        self.assertTrue(left.coarse_profile.is_partial_identity)
        self.assertFalse(left.is_idempotent)

    def test_distinct_witnessed_profiles_have_constructive_separator(self):
        full = contact_guarded_witness_profile(
            CYCLE_K,
            ((1, 1, 1),),
            (0, 1, 2),
        )
        killed = contact_guarded_witness_profile(
            CYCLE_K,
            ((0, 0, 0),),
            (0, 1, 2),
        )
        score, witness = witnessed_profile_separating_state(
            full,
            killed,
        )
        left = apply_contact_guarded_witness_profile(
            score,
            witness,
            full,
        )
        right = apply_contact_guarded_witness_profile(
            score,
            witness,
            killed,
        )
        self.assertTrue(left.defined and right.defined)
        self.assertEqual(left.score_state, right.score_state)
        self.assertNotEqual(left.witness_state, right.witness_state)

        reordered = contact_guarded_witness_profile(
            CYCLE_K,
            ((1, 1, 1),),
            (2, 1, 0),
        )
        score, witness = witnessed_profile_separating_state(
            full,
            reordered,
        )
        self.assertNotEqual(
            apply_contact_guarded_witness_profile(
                score,
                witness,
                full,
            ),
            apply_contact_guarded_witness_profile(
                score,
                witness,
                reordered,
            ),
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            contact_guarded_witness_profile(
                CYCLE_K,
                (),
                (0,),
            )
        with self.assertRaises(ValueError):
            contact_guarded_witness_profile(
                CYCLE_K,
                ((1, 0),),
                (0,),
            )
        with self.assertRaises(ValueError):
            contact_guarded_witness_profile_power(
                contact_guarded_witness_profile(
                    CYCLE_K,
                    ((1, 1, 1),),
                    (0,),
                ),
                -1,
            )


if __name__ == "__main__":
    unittest.main()
