import itertools
import unittest

from enterprise_math.integer_affine_future_equivalence import (
    affine_word_observation_difference,
    one_dimensional_guard_after_affine_step,
)


class IntegerAffineFutureEquivalenceTests(unittest.TestCase):
    def test_total_affine_offsets_cancel_for_all_small_words_and_states(self):
        matrices = (
            ((1, 1), (0, 1)),
            ((0, 1), (-1, 0)),
        )
        offsets = (
            (3, -2),
            (-4, 5),
        )
        observation_row = (2, -3)
        for length in range(5):
            for word in itertools.product(range(2), repeat=length):
                for left in itertools.product(range(-2, 3), repeat=2):
                    for right in itertools.product(range(-2, 3), repeat=2):
                        report = affine_word_observation_difference(
                            matrices,
                            offsets,
                            observation_row,
                            7,
                            word,
                            left,
                            right,
                        )
                        self.assertTrue(report.offsets_cancel_exactly)

    def test_changing_all_offsets_changes_absolute_world_but_not_pairwise_future_difference(self):
        matrices = (
            ((2, 1), (0, 1)),
            ((1, 0), (1, 1)),
        )
        left = (3, -1)
        right = (-2, 4)
        word = (0, 1, 0, 1)
        first = affine_word_observation_difference(
            matrices,
            ((1, 2), (3, 4)),
            (5, -2),
            9,
            word,
            left,
            right,
        )
        second = affine_word_observation_difference(
            matrices,
            ((100, -70), (-33, 41)),
            (5, -2),
            -123,
            word,
            left,
            right,
        )
        self.assertEqual(
            first.affine_output_difference,
            second.affine_output_difference,
        )

    def test_guarded_affine_offset_can_change_later_definedness(self):
        # Same linear part x->x, same initial x=-1, but the affine shift changes
        # whether the second guarded action remains legal.
        zero_shift = one_dimensional_guard_after_affine_step(-1, 0)
        unit_shift = one_dimensional_guard_after_affine_step(-1, 1)
        self.assertEqual(zero_shift, (True, -1, True))
        self.assertEqual(unit_shift, (True, 0, False))

    def test_first_guard_can_already_be_undefined(self):
        self.assertEqual(
            one_dimensional_guard_after_affine_step(0, 5),
            (False, None, None),
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            affine_word_observation_difference(
                (((1,),),),
                (),
                (1,),
                0,
                (),
                (0,),
                (0,),
            )
        with self.assertRaises(ValueError):
            affine_word_observation_difference(
                (((1,),),),
                ((0,),),
                (1,),
                0,
                (1,),
                (0,),
                (0,),
            )
        with self.assertRaises(TypeError):
            one_dimensional_guard_after_affine_step(False, 1)


if __name__ == "__main__":
    unittest.main()
