import itertools
import unittest

from enterprise_math.integer_dynamic_model_separation import (
    finite_horizon_dynamic_difference_content,
)
from enterprise_math.integer_dynamic_model_separation_horizon import (
    dynamic_model_separation_horizon_report,
)


class IntegerDynamicModelSeparationHorizonTests(unittest.TestCase):
    def test_delayed_difference_first_appears_at_horizon_two_with_content_six(self):
        left_action = (
            (0, 1, 0),
            (0, 0, 6),
            (0, 0, 0),
        )
        right_action = (
            (0, 1, 0),
            (0, 0, 0),
            (0, 0, 0),
        )
        observation = ((1, 0, 0),)
        report = dynamic_model_separation_horizon_report(
            (left_action,),
            observation,
            (right_action,),
            observation,
        )
        by_horizon = {step.horizon: step for step in report.steps}
        self.assertEqual(by_horizon[0].difference_content, 0)
        self.assertEqual(by_horizon[1].difference_content, 0)
        self.assertEqual(by_horizon[2].difference_content, 6)
        self.assertEqual(report.final_difference_content, 6)

        for modulus in (2, 3, 6):
            self.assertIsNone(report.first_distinguishing_horizon(modulus))
        for modulus in (4, 5, 7):
            self.assertEqual(report.first_distinguishing_horizon(modulus), 2)

    def test_horizon_compiler_matches_literal_difference_content_at_every_recorded_step(self):
        model_pairs = (
            (
                (((1, 0), (0, 1)),),
                (((1, 6), (0, 1)),),
            ),
            (
                (
                    ((0, 1), (0, 0)),
                    ((1, 0), (0, 1)),
                ),
                (
                    ((0, 0), (0, 0)),
                    ((1, 1), (0, 1)),
                ),
            ),
        )
        observation = ((1, 0),)
        for left_actions, right_actions in model_pairs:
            report = dynamic_model_separation_horizon_report(
                left_actions,
                observation,
                right_actions,
                observation,
            )
            for step in report.steps:
                literal = finite_horizon_dynamic_difference_content(
                    left_actions,
                    observation,
                    right_actions,
                    observation,
                    step.horizon,
                )
                self.assertEqual(step.difference_content, literal)

    def test_indistinguishable_modulus_set_only_shrinks_with_future_depth(self):
        left_action = (
            (0, 1, 0),
            (0, 0, 6),
            (0, 0, 0),
        )
        right_action = (
            (0, 1, 0),
            (0, 0, 0),
            (0, 0, 0),
        )
        report = dynamic_model_separation_horizon_report(
            (left_action,),
            ((1, 0, 0),),
            (right_action,),
            ((1, 0, 0),),
        )
        candidates = tuple(range(1, 13))
        previous = set(candidates)
        for horizon in range(report.steps[-1].horizon + 1):
            current = set(
                report.indistinguishable_moduli_through_horizon(
                    horizon,
                    candidates,
                )
            )
            self.assertTrue(current.issubset(previous))
            previous = current
        self.assertEqual(previous, {1, 2, 3, 6})

    def test_exactly_future_equivalent_internal_models_never_separate_at_any_modulus(self):
        left_action = ((1, 0), (0, 1))
        right_action = ((1, 0), (1, 0))
        report = dynamic_model_separation_horizon_report(
            (left_action,),
            ((1, 0),),
            (right_action,),
            ((1, 0),),
        )
        self.assertTrue(all(step.difference_content == 0 for step in report.steps))
        for modulus in range(1, 10):
            self.assertIsNone(report.first_distinguishing_horizon(modulus))

    def test_small_binary_single_action_pairs_match_literal_content_chain(self):
        actions = tuple(
            (
                (entries[0], entries[1]),
                (entries[2], entries[3]),
            )
            for entries in itertools.product((0, 1), repeat=4)
        )
        observation = ((1, 0),)
        for left in actions:
            for right in actions:
                report = dynamic_model_separation_horizon_report(
                    (left,),
                    observation,
                    (right,),
                    observation,
                )
                contents = []
                for step in report.steps:
                    literal = finite_horizon_dynamic_difference_content(
                        (left,),
                        observation,
                        (right,),
                        observation,
                        step.horizon,
                    )
                    self.assertEqual(step.difference_content, literal)
                    contents.append(literal)
                for earlier, later in zip(contents, contents[1:]):
                    self.assertTrue(earlier == 0 or later != 0 and earlier % later == 0)

    def test_validation(self):
        report = dynamic_model_separation_horizon_report(
            (((1,),),),
            ((1,),),
            (((1,),),),
            ((1,),),
        )
        with self.assertRaises(ValueError):
            report.first_distinguishing_horizon(0)
        with self.assertRaises(ValueError):
            report.indistinguishable_moduli_through_horizon(-1, (1, 2))


if __name__ == "__main__":
    unittest.main()
