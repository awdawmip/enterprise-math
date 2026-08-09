import unittest

from enterprise_math.action_language_precision import reachable_boundary_cuts
from enterprise_math.adjoint_boundary_precision import (
    AdjointChainAction,
    action_words,
    apply_action_word,
    audit_adjunction_box,
    boundary_orbit,
    direct_future_threshold_signature,
    dilation_action,
    floor_division_action,
    future_boundary_rank,
    naive_boundary_cut_bound,
    natural_collapse_action,
    natural_quotient_action,
    natural_root_action,
    pullback_boundary_word,
    pullback_word_signature,
    stabilize_boundary_orbit,
    translation_action,
)


class AdjointBoundaryPrecisionTests(unittest.TestCase):
    def test_translation_boundary_orbit_recovers_stage_one(self) -> None:
        boundaries = (-3, 2, 7)
        increments = (-2, 3, 5)
        actions = tuple(translation_action(value) for value in increments)
        for horizon in range(5):
            self.assertEqual(
                boundary_orbit(boundaries, actions, horizon),
                reachable_boundary_cuts(boundaries, increments, horizon),
            )

    def test_direct_future_signature_equals_cut_rank_equivalence(self) -> None:
        piecewise = AdjointChainAction(
            "piecewise_step",
            lambda x: x + 1 if x < 0 else x + 2,
            lambda b: b - 1 if b <= 0 else (0 if b <= 2 else b - 2),
        )
        actions = (
            translation_action(2),
            dilation_action(2),
            floor_division_action(2),
            piecewise,
        )
        boundaries = (-4, 0, 3, 7)
        horizon = 3
        states = tuple(range(-24, 25))
        signatures = {
            state: direct_future_threshold_signature(state, boundaries, actions, horizon)
            for state in states
        }
        ranks = {
            state: future_boundary_rank(state, boundaries, actions, horizon)
            for state in states
        }
        for left in states:
            for right in states:
                self.assertEqual(
                    signatures[left] == signatures[right],
                    ranks[left] == ranks[right],
                    msg=(left, right),
                )

    def test_pullback_word_is_contravariant_to_forward_composition(self) -> None:
        actions = (
            translation_action(3),
            dilation_action(2),
            floor_division_action(3),
        )
        word = (0, 1, 2)
        for boundary in range(-9, 10):
            pulled = pullback_boundary_word(boundary, actions, word)
            for state in range(-25, 26):
                self.assertEqual(
                    pulled <= state,
                    boundary <= apply_action_word(state, actions, word),
                    msg=(boundary, state),
                )

    def test_foundational_root_quotient_and_collapse_adjunctions(self) -> None:
        root = natural_root_action(2)
        quotient = natural_quotient_action(3)
        collapse = natural_collapse_action(2)
        self.assertTrue(audit_adjunction_box(root, range(0, 12), range(0, 130)))
        self.assertTrue(audit_adjunction_box(quotient, range(0, 20), range(0, 130)))
        self.assertTrue(audit_adjunction_box(collapse, range(0, 40), range(0, 130)))

        self.assertEqual(root.pullback_cut(7), 49)
        self.assertEqual(quotient.pullback_cut(7), 21)
        self.assertEqual(collapse.pullback_cut(7), 9)
        self.assertEqual(collapse.pullback_cut(9), 9)

    def test_floor_division_creates_unbounded_boundary_hierarchy(self) -> None:
        action = floor_division_action(2)
        self.assertEqual(boundary_orbit((1,), (action,), 5), (1, 2, 4, 8, 16, 32))
        result = stabilize_boundary_orbit((1,), (action,), 8)
        self.assertFalse(result.stabilized)
        self.assertEqual(result.cuts, tuple(2**power for power in range(9)))

    def test_dilation_boundary_orbit_stabilizes(self) -> None:
        action = dilation_action(2)
        result = stabilize_boundary_orbit((17, -9, 0), (action,), 10)
        self.assertTrue(result.stabilized)
        self.assertEqual(result.horizon, 6)
        self.assertEqual(
            result.cuts,
            (-9, -4, -2, -1, 0, 1, 2, 3, 5, 9, 17),
        )

    def test_action_words_can_collapse_to_one_boundary_transformation(self) -> None:
        actions = (translation_action(2), translation_action(5))
        boundaries = (-3, 0, 8)
        left_word = (0, 1)
        right_word = (1, 0)
        self.assertEqual(
            pullback_word_signature(left_word, boundaries, actions),
            pullback_word_signature(right_word, boundaries, actions),
        )
        for state in range(-20, 21):
            left = tuple(boundary <= apply_action_word(state, actions, left_word) for boundary in boundaries)
            right = tuple(boundary <= apply_action_word(state, actions, right_word) for boundary in boundaries)
            self.assertEqual(left, right)

    def test_task_specific_boundary_closure_is_weaker_than_global_adjunction(self) -> None:
        def nonmonotone(value: int) -> int:
            if value == -2:
                return -1
            if value == -1:
                return -2
            return value

        # The declared threshold 0 is perfectly preserved.
        for state in range(-12, 13):
            self.assertEqual(state >= 0, nonmonotone(state) >= 0)

        # But threshold -1 has a non-upper preimage: -2 is accepted while -1 is not.
        self.assertTrue(nonmonotone(-2) >= -1)
        self.assertFalse(nonmonotone(-1) >= -1)
        self.assertTrue(nonmonotone(0) >= -1)

    def test_nonmonotone_absolute_value_breaks_single_cut_pullback(self) -> None:
        self.assertTrue(abs(-1) >= 1)
        self.assertFalse(abs(0) >= 1)
        self.assertTrue(abs(1) >= 1)

    def test_naive_cut_bound_dominates_exact_orbit(self) -> None:
        actions = (translation_action(1), dilation_action(2), floor_division_action(2))
        boundaries = (-5, 0, 7)
        for horizon in range(5):
            exact = len(boundary_orbit(boundaries, actions, horizon))
            bound = naive_boundary_cut_bound(len(boundaries), len(actions), horizon)
            self.assertLessEqual(exact, bound)
            self.assertEqual(len(action_words(len(actions), horizon)), (3 ** (horizon + 1) - 1) // 2)


if __name__ == "__main__":
    unittest.main()
