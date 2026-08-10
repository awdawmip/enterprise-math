import unittest

from enterprise_math.integer_action_capability_basis import (
    INTEGER_MODULE,
    STATE_KERNEL,
)
from enterprise_math.integer_action_redundancy_context import (
    action_redundancy_contexts,
    action_redundant_over_context,
    first_redundancy_context_switch,
)


class IntegerActionRedundancyContextTests(unittest.TestCase):
    def setUp(self):
        # A is invisible on the initial e1 row but maps an e2 row to e3 once a
        # different action has created that intermediate direction.
        self.action_a = (
            (1, 0, 0),
            (0, 0, 1),
            (0, 0, 0),
        )
        # B and C are duplicate e1->e2 capabilities.  B is useful alone but
        # becomes redundant once C is already present.
        self.action_b = (
            (0, 1, 0),
            (0, 0, 0),
            (0, 0, 0),
        )
        self.action_c = self.action_b
        self.actions = (self.action_a, self.action_b, self.action_c)
        self.observation = ((1, 0, 0),)

    def test_hidden_activation_redundancy_switches_off_as_context_grows(self):
        for mode in (STATE_KERNEL, INTEGER_MODULE):
            self.assertTrue(
                action_redundant_over_context(
                    self.actions,
                    self.observation,
                    (),
                    0,
                    mode=mode,
                )
            )
            self.assertFalse(
                action_redundant_over_context(
                    self.actions,
                    self.observation,
                    (1,),
                    0,
                    mode=mode,
                )
            )

            switch = first_redundancy_context_switch(
                self.actions,
                self.observation,
                0,
                mode=mode,
            )
            self.assertIsNotNone(switch)
            assert switch is not None
            self.assertTrue(switch.activation)
            self.assertFalse(switch.suppression)
            self.assertTrue(set(switch.smaller_context).issubset(switch.larger_context))

    def test_substitution_suppresses_action_value_in_larger_context(self):
        for mode in (STATE_KERNEL, INTEGER_MODULE):
            self.assertFalse(
                action_redundant_over_context(
                    self.actions,
                    self.observation,
                    (),
                    1,
                    mode=mode,
                )
            )
            self.assertTrue(
                action_redundant_over_context(
                    self.actions,
                    self.observation,
                    (2,),
                    1,
                    mode=mode,
                )
            )

            switch = first_redundancy_context_switch(
                self.actions,
                self.observation,
                1,
                mode=mode,
            )
            self.assertIsNotNone(switch)
            assert switch is not None
            self.assertFalse(switch.activation)
            self.assertTrue(switch.suppression)

    def test_redundancy_context_family_is_not_upward_or_downward_closed(self):
        for mode in (STATE_KERNEL, INTEGER_MODULE):
            contexts_a = set(
                action_redundancy_contexts(
                    self.actions,
                    self.observation,
                    0,
                    mode=mode,
                )
            )
            self.assertIn((), contexts_a)
            self.assertNotIn((1,), contexts_a)

            contexts_b = set(
                action_redundancy_contexts(
                    self.actions,
                    self.observation,
                    1,
                    mode=mode,
                )
            )
            self.assertNotIn((), contexts_b)
            self.assertIn((2,), contexts_b)

    def test_duplicate_actions_are_mutually_redundant_when_the_other_is_present(self):
        for mode in (STATE_KERNEL, INTEGER_MODULE):
            self.assertTrue(
                action_redundant_over_context(
                    self.actions,
                    self.observation,
                    (2,),
                    1,
                    mode=mode,
                )
            )
            self.assertTrue(
                action_redundant_over_context(
                    self.actions,
                    self.observation,
                    (1,),
                    2,
                    mode=mode,
                )
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            action_redundant_over_context(
                (),
                self.observation,
                (),
                0,
            )
        with self.assertRaises(ValueError):
            action_redundant_over_context(
                self.actions,
                self.observation,
                (0,),
                0,
            )
        with self.assertRaises(ValueError):
            action_redundant_over_context(
                self.actions,
                self.observation,
                (1, 1),
                0,
            )
        with self.assertRaises(ValueError):
            action_redundancy_contexts(
                self.actions,
                self.observation,
                0,
                mode="UNKNOWN",
            )


if __name__ == "__main__":
    unittest.main()
