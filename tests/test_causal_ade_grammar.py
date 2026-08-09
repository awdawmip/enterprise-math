import unittest

from enterprise_math.causal_ade_grammar import (
    a_grammar,
    d_grammar,
    e6_grammar,
    e7_grammar,
    e8_binary_grammar,
    e8_factorizations_share_geometry_shadow,
    e8_ternary_grammar,
)


class CausalADEGrammarTests(unittest.TestCase):
    def test_a_rank_is_slots_minus_one_due_to_exact_total_constraint(self):
        factor, shadow = a_grammar(3)
        self.assertEqual(factor.local_cell_rank, 1)
        self.assertEqual(factor.cell_count, 4)
        self.assertEqual(factor.independent_constraint_rank_loss, 1)
        self.assertEqual(factor.global_relation_rank, 3)
        self.assertEqual(shadow.rank, 3)
        self.assertEqual(shadow.primitive_event_count, 12)
        self.assertEqual(shadow.coxeter_root_count_shadow, 4)

    def test_d_and_exceptional_code_glue_keep_product_rank(self):
        profiles = [d_grammar(4), e6_grammar(), e7_grammar(), e8_binary_grammar(), e8_ternary_grammar()]
        for factor, shadow in profiles:
            self.assertEqual(factor.independent_constraint_rank_loss, 0)
            self.assertEqual(factor.global_relation_rank, shadow.rank)

    def test_e6_e7_e8_are_primitive_grade_resonance_profiles(self):
        for grammar in (e6_grammar, e7_grammar, e8_binary_grammar, e8_ternary_grammar):
            factor, _ = grammar()
            self.assertEqual(factor.primitive_grade_regime, "resonant")

    def test_geometry_shadows_recover_ade_root_counts_and_coxeter_coordinates(self):
        expected = {
            "A3": (3, 12, 4),
            "D4": (4, 24, 6),
            "E6": (6, 72, 12),
            "E7": (7, 126, 18),
            "E8": (8, 240, 30),
        }
        profiles = [a_grammar(3)[1], d_grammar(4)[1], e6_grammar()[1], e7_grammar()[1], e8_binary_grammar()[1]]
        for profile in profiles:
            self.assertEqual(
                (profile.rank, profile.primitive_event_count, profile.coxeter_root_count_shadow),
                expected[profile.name],
            )

    def test_e8_has_two_different_causal_factorizations_with_same_geometry_shadow(self):
        binary_factor, binary_shadow = e8_binary_grammar()
        ternary_factor, ternary_shadow = e8_ternary_grammar()
        self.assertEqual(binary_shadow, ternary_shadow)
        self.assertNotEqual(binary_factor, ternary_factor)
        self.assertEqual((binary_factor.local_cell_rank, binary_factor.cell_count), (1, 8))
        self.assertEqual((ternary_factor.local_cell_rank, ternary_factor.cell_count), (2, 4))
        self.assertTrue(e8_factorizations_share_geometry_shadow())


if __name__ == "__main__":
    unittest.main()
