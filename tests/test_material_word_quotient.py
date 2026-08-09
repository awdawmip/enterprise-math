import unittest

from enterprise_math.material_program import (
    HARDEN,
    RETAIN,
    SOFTEN,
    MaterialOperator,
)
from enterprise_math.material_word_quotient import (
    compose_material_words,
    material_word_signature,
    material_words_equivalent,
    verify_equivalence_congruence,
)


class MaterialWordQuotientTests(unittest.TestCase):
    def test_distinct_hardening_powers_can_collapse_to_same_function_at_low_precision(self):
        h2 = (MaterialOperator(HARDEN, 2),)
        h3 = (MaterialOperator(HARDEN, 3),)
        self.assertEqual(material_word_signature(2, h2), (0, 0, 2))
        self.assertEqual(material_word_signature(2, h3), (0, 0, 2))
        self.assertTrue(material_words_equivalent(2, h2, h3))

    def test_refinement_can_split_previously_equivalent_material_words(self):
        h2 = (MaterialOperator(HARDEN, 2),)
        h3 = (MaterialOperator(HARDEN, 3),)
        self.assertTrue(material_words_equivalent(2, h2, h3))
        self.assertFalse(material_words_equivalent(3, h2, h3))
        self.assertEqual(material_word_signature(3, h2), (0, 0, 1, 3))
        self.assertEqual(material_word_signature(3, h3), (0, 0, 0, 3))

    def test_extensional_equivalence_survives_pre_and_post_composition(self):
        h2 = (MaterialOperator(HARDEN, 2),)
        h3 = (MaterialOperator(HARDEN, 3),)
        before = (MaterialOperator(SOFTEN, 2),)
        after = (MaterialOperator(RETAIN, 1),)
        self.assertTrue(
            verify_equivalence_congruence(
                2,
                h2,
                h3,
                context_before=before,
                context_after=after,
            )
        )

    def test_word_concatenation_matches_apply_first_then_second_order(self):
        first = (MaterialOperator(HARDEN, 2),)
        second = (MaterialOperator(SOFTEN, 2),)
        self.assertEqual(compose_material_words(first, second), first + second)

    def test_noncommuting_words_have_distinct_signatures_when_precision_resolves_them(self):
        left = (
            MaterialOperator(HARDEN, 3),
            MaterialOperator(HARDEN, 2),
        )
        right = (
            MaterialOperator(HARDEN, 2),
            MaterialOperator(HARDEN, 3),
        )
        self.assertFalse(material_words_equivalent(5, left, right))

    def test_congruence_checker_rejects_nonequivalent_starting_words(self):
        h2 = (MaterialOperator(HARDEN, 2),)
        h3 = (MaterialOperator(HARDEN, 3),)
        with self.assertRaises(ValueError):
            verify_equivalence_congruence(5, h2, h3)


if __name__ == "__main__":
    unittest.main()
