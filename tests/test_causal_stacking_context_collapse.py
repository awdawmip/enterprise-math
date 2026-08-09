import unittest
from itertools import product

from enterprise_math.causal_stacking_context_collapse import (
    context_fiber,
    context_observation_forgets_only_global_sign,
    context_word,
    every_context_fiber_has_size_two,
    reconstruct_signs,
    stacking_context_collision_spectrum,
)


class CausalStackingContextCollapseTests(unittest.TestCase):
    def test_context_plus_one_initial_sign_reconstructs_entire_trajectory(self):
        signs = (1, 1, -1, -1, 1, -1)
        context = context_word(signs)
        self.assertEqual(context, (0, 1, 0, 1, 1))
        self.assertEqual(reconstruct_signs(context, 1), signs)
        self.assertEqual(reconstruct_signs(context, -1), tuple(-value for value in signs))

    def test_every_context_fiber_is_exactly_global_sign_pair(self):
        for length in range(1, 9):
            self.assertTrue(every_context_fiber_has_size_two(length))
            for signs in product((-1, 1), repeat=length):
                self.assertTrue(context_observation_forgets_only_global_sign(tuple(signs)))

    def test_collision_spectrum_is_uniform_two_state_fibers(self):
        for length in range(1, 9):
            spectrum = stacking_context_collision_spectrum(length, 5)
            self.assertEqual(spectrum[0], 1 << length)
            self.assertEqual(spectrum[1], 1 << (length - 1))
            self.assertEqual(spectrum[2:], (0, 0, 0))

    def test_context_fiber_contains_two_and_only_two_orientation_choices(self):
        context = (1, 0, 1, 1)
        positive, negative = context_fiber(context)
        self.assertEqual(positive, tuple(-value for value in negative))
        self.assertEqual(context_word(positive), context)
        self.assertEqual(context_word(negative), context)


if __name__ == "__main__":
    unittest.main()
