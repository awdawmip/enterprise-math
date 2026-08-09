import unittest

from enterprise_math.lego_pair_interaction import (
    pair_interaction_from_unit_effects,
    unit_pair_effects_determine_same_response,
)


class LegoPairInteractionTests(unittest.TestCase):
    def test_one_pair_effect_table_reconstructs_integer_cross_response(self):
        # Two left unit types, two right unit types, scalar output stored as 1-vector.
        effects = (
            ((2,), (3,)),
            ((5,), (7,)),
        )
        left = (2, 1)
        right = (3, 4)
        expected = (
            2 * 3 * 2
            + 2 * 4 * 3
            + 1 * 3 * 5
            + 1 * 4 * 7,
        )
        self.assertEqual(pair_interaction_from_unit_effects(left, right, effects), expected)

    def test_separate_lego_additivity_is_exact(self):
        effects = (
            ((1, 2), (0, 1)),
            ((3, 0), (2, -1)),
        )
        self.assertTrue(
            unit_pair_effects_determine_same_response(
                (2, 1),
                (3, -2),
                (4, 5),
                effects,
            )
        )

    def test_one_unit_each_reads_the_primitive_pair_effect(self):
        effects = (
            ((11,), (13,)),
            ((17,), (19,)),
        )
        self.assertEqual(pair_interaction_from_unit_effects((0, 1), (1, 0), effects), (17,))

    def test_zero_multiplicity_removes_cross_effect_without_special_case(self):
        effects = (((9,),),)
        self.assertEqual(pair_interaction_from_unit_effects((0,), (7,), effects), (0,))
        self.assertEqual(pair_interaction_from_unit_effects((5,), (0,), effects), (0,))


if __name__ == "__main__":
    unittest.main()
