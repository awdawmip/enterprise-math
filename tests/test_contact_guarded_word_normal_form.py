import itertools
import unittest

from enterprise_math.contact_guarded_word_normal_form import (
    ContactGuardedWordProfile,
    apply_contact_guarded_profile,
    apply_contact_guarded_word,
    compose_contact_guarded_profiles,
    contact_guarded_profile_power,
    contact_guarded_word_profile,
    contact_profile_separating_state,
    contact_word_action_counts,
    empty_contact_guarded_profile,
    zero_shift_domain_product,
)


PATH_K = (
    (2, -1),
    (-1, 2),
)

POSITIVE_V_K = (
    (2, 1),
    (1, 2),
)

CYCLE_K = (
    (2, -1, -1),
    (-1, 2, -1),
    (-1, -1, 2),
)


def words(dimension, maximum_length):
    result = [()]
    for length in range(1, maximum_length + 1):
        result.extend(itertools.product(range(dimension), repeat=length))
    return tuple(result)


class ContactGuardedWordNormalFormTests(unittest.TestCase):
    def test_compiled_profile_matches_literal_word_exhaustively(self):
        matrices = (PATH_K, POSITIVE_V_K, CYCLE_K)
        for coupling in matrices:
            dimension = len(coupling)
            for word in words(dimension, 4):
                profile = contact_guarded_word_profile(coupling, word)
                for state in itertools.product(range(-3, 3), repeat=dimension):
                    self.assertEqual(
                        apply_contact_guarded_profile(state, profile),
                        apply_contact_guarded_word(coupling, state, word),
                    )

    def test_profile_product_is_exact_literal_concatenation(self):
        for coupling in (PATH_K, POSITIVE_V_K, CYCLE_K):
            dimension = len(coupling)
            sample = words(dimension, 3)
            for first_word in sample:
                first = contact_guarded_word_profile(coupling, first_word)
                for second_word in sample:
                    second = contact_guarded_word_profile(
                        coupling,
                        second_word,
                    )
                    self.assertEqual(
                        compose_contact_guarded_profiles(first, second),
                        contact_guarded_word_profile(
                            coupling,
                            first_word + second_word,
                        ),
                    )

    def test_distinct_profiles_have_constructive_separating_state(self):
        for coupling in (PATH_K, POSITIVE_V_K, CYCLE_K):
            dimension = len(coupling)
            profiles = tuple(
                {
                    contact_guarded_word_profile(coupling, word)
                    for word in words(dimension, 3)
                }
            )
            for index, left in enumerate(profiles):
                for right in profiles[index + 1 :]:
                    state = contact_profile_separating_state(left, right)
                    self.assertNotEqual(
                        apply_contact_guarded_profile(state, left),
                        apply_contact_guarded_profile(state, right),
                    )

    def test_path_same_counts_can_still_have_different_causal_domains(self):
        left = contact_guarded_word_profile(PATH_K, (0, 1))
        right = contact_guarded_word_profile(PATH_K, (1, 0))

        self.assertEqual(left.score_shift, right.score_shift)
        self.assertEqual(left.score_shift, (1, 1))
        self.assertEqual(left.requirements, (0, -1))
        self.assertEqual(right.requirements, (-1, 0))

        state = (-1, 0)
        self.assertTrue(
            apply_contact_guarded_profile(state, left).defined
        )
        self.assertFalse(
            apply_contact_guarded_profile(state, right).defined
        )

        all_closing = (-1, -1)
        self.assertEqual(
            apply_contact_guarded_profile(all_closing, left),
            apply_contact_guarded_profile(all_closing, right),
        )

    def test_triangle_cycle_word_is_zero_shift_partial_identity(self):
        cycle = contact_guarded_word_profile(CYCLE_K, (0, 1, 2))
        self.assertTrue(cycle.is_partial_identity)
        self.assertEqual(cycle.score_shift, (0, 0, 0))
        self.assertEqual(cycle.requirements, (0, -1, -2))

        state = (-1, 0, 1)
        outcome = apply_contact_guarded_profile(state, cycle)
        self.assertTrue(outcome.defined)
        self.assertEqual(outcome.state, state)

    def test_zero_shift_word_is_idempotent_and_all_positive_powers_collapse(self):
        cycle = contact_guarded_word_profile(CYCLE_K, (0, 1, 2))
        identity = empty_contact_guarded_profile(3)

        self.assertEqual(contact_guarded_profile_power(cycle, 0), identity)
        for exponent in range(1, 8):
            self.assertEqual(
                contact_guarded_profile_power(cycle, exponent),
                cycle,
            )

        self.assertEqual(
            contact_guarded_word_profile(
                CYCLE_K,
                (0, 1, 2) * 6,
            ),
            cycle,
        )
        self.assertNotEqual(
            contact_word_action_counts((0, 1, 2), 3),
            contact_word_action_counts((0, 1, 2) * 6, 3),
        )

    def test_cycle_orderings_have_same_zero_shift_but_different_domain_projectors(self):
        forward = contact_guarded_word_profile(CYCLE_K, (0, 1, 2))
        reverse = contact_guarded_word_profile(CYCLE_K, (2, 1, 0))

        self.assertEqual(forward.score_shift, reverse.score_shift)
        self.assertEqual(forward.score_shift, (0, 0, 0))
        self.assertNotEqual(forward.requirements, reverse.requirements)
        self.assertEqual(forward.requirements, (0, -1, -2))
        self.assertEqual(reverse.requirements, (-2, -1, 0))

        witness = (0, 0, -1)
        self.assertFalse(
            apply_contact_guarded_profile(witness, forward).defined
        )
        reverse_outcome = apply_contact_guarded_profile(
            witness,
            reverse,
        )
        self.assertTrue(reverse_outcome.defined)
        self.assertEqual(reverse_outcome.state, witness)

    def test_zero_shift_profiles_form_commutative_domain_semilattice(self):
        first = contact_guarded_word_profile(CYCLE_K, (0, 1, 2))
        second = contact_guarded_word_profile(CYCLE_K, (2, 1, 0))

        product = zero_shift_domain_product(first, second)
        reverse_product = zero_shift_domain_product(second, first)

        self.assertEqual(product, reverse_product)
        self.assertTrue(product.is_partial_identity)
        self.assertEqual(
            product.requirements,
            tuple(
                max(left, right)
                for left, right in zip(
                    first.requirements,
                    second.requirements,
                    strict=True,
                )
            ),
        )
        self.assertEqual(
            zero_shift_domain_product(first, first),
            first,
        )

    def test_six_triangle_cycle_orders_generate_sixteen_domain_idempotents(self):
        primitive = {
            contact_guarded_word_profile(CYCLE_K, ordering)
            for ordering in itertools.permutations(range(3))
        }
        self.assertEqual(len(primitive), 6)
        self.assertEqual(
            {profile.score_shift for profile in primitive},
            {(0, 0, 0)},
        )

        closure = set(primitive)
        changed = True
        while changed:
            changed = False
            current = tuple(closure)
            for left in current:
                for right in current:
                    product = zero_shift_domain_product(left, right)
                    if product not in closure:
                        closure.add(product)
                        changed = True

        self.assertEqual(len(closure), 16)
        self.assertTrue(all(profile.is_partial_identity for profile in closure))

    def test_validation(self):
        with self.assertRaises(ValueError):
            contact_guarded_word_profile((), ())
        with self.assertRaises(ValueError):
            contact_guarded_word_profile(((1, 2),), ())
        with self.assertRaises(ValueError):
            contact_guarded_word_profile(PATH_K, (2,))
        with self.assertRaises(TypeError):
            contact_guarded_word_profile(((True,),), ())
        with self.assertRaises(ValueError):
            empty_contact_guarded_profile(0)

        profile = ContactGuardedWordProfile((0, 0), (None, None))
        with self.assertRaises(ValueError):
            apply_contact_guarded_profile((0,), profile)
        with self.assertRaises(ValueError):
            contact_guarded_profile_power(profile, -1)
        with self.assertRaises(ValueError):
            contact_profile_separating_state(profile, profile)
        with self.assertRaises(ValueError):
            zero_shift_domain_product(
                contact_guarded_word_profile(PATH_K, (0,)),
                profile,
            )


if __name__ == "__main__":
    unittest.main()
