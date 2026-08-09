import unittest

from enterprise_math.material_program import (
    HARDEN,
    OFFSET,
    RETAIN,
    SOFTEN,
    MaterialOperator,
    apply_material_word,
    material_program_profile,
    material_word_branch,
)


class MaterialProgramTests(unittest.TestCase):
    def test_empty_word_is_identity(self):
        trace = apply_material_word(37, 100, ())
        self.assertEqual(trace.result, 37)
        self.assertEqual(trace.steps, ())

    def test_operator_word_retains_noncommutative_order(self):
        h2 = MaterialOperator(HARDEN, 2)
        h3 = MaterialOperator(HARDEN, 3)
        forward = apply_material_word(4, 5, (h3, h2))
        reverse = apply_material_word(4, 5, (h2, h3))
        self.assertEqual(forward.result, 0)
        self.assertEqual(reverse.result, 1)
        self.assertNotEqual(forward.word, reverse.word)
        self.assertNotEqual(forward.result, reverse.result)

    def test_word_trace_exposes_every_intermediate_state(self):
        word = (
            MaterialOperator(HARDEN, 2),
            MaterialOperator(RETAIN, 500),
            MaterialOperator(OFFSET, 50),
        )
        trace = apply_material_word(800, 1000, word)
        self.assertEqual(
            tuple((step.before, step.after) for step in trace.steps),
            ((800, 640), (640, 320), (320, 370)),
        )
        self.assertEqual(trace.result, 370)

    def test_loading_and_returning_can_use_different_words(self):
        base = (0, 250, 500, 750, 1000)
        profile = material_program_profile(
            base,
            amplitude=1000,
            loading_word=(MaterialOperator(HARDEN, 2),),
            return_word=(
                MaterialOperator(SOFTEN, 1),
                MaterialOperator(RETAIN, 500),
            ),
        )
        self.assertEqual(profile.loading, (0, 62, 250, 562, 1000))
        self.assertEqual(profile.returning, (0, 125, 250, 375, 500))
        self.assertEqual(profile.branch_gap, 687)
        self.assertEqual(profile.signed_area, 624)

    def test_word_branch_matches_individual_word_application(self):
        base = (0, 10, 20, 30, 40, 50)
        word = (MaterialOperator(SOFTEN, 2), MaterialOperator(RETAIN, 25))
        branch = material_word_branch(base, 50, word)
        expected = tuple(
            apply_material_word(sample, 50, word).result for sample in base
        )
        self.assertEqual(branch, expected)

    def test_invalid_operator_parameters_are_rejected(self):
        with self.assertRaises(ValueError):
            apply_material_word(1, 10, (MaterialOperator(HARDEN, 0),))
        with self.assertRaises(ValueError):
            apply_material_word(1, 10, (MaterialOperator(RETAIN, 11),))
        with self.assertRaises(ValueError):
            apply_material_word(1, 10, (MaterialOperator("UNKNOWN", 1),))


if __name__ == "__main__":
    unittest.main()
