import itertools
import unittest

from enterprise_math.causal_future_module import (
    agreement_depth_ge,
    causal_future_closure,
    first_distinguishing_depth,
    future_indistinguishable,
)


class CausalFutureModuleTests(unittest.TestCase):
    def test_shift_dynamics_reveals_three_integer_directions_in_three_depths(self):
        shift = (
            (0, 1, 0),
            (0, 0, 1),
            (0, 0, 0),
        )
        closure = causal_future_closure((shift,), ((1, 0, 0),))
        self.assertEqual(closure.ranks, (1, 2, 3))
        self.assertEqual(closure.stable_depth, 2)
        self.assertEqual(closure.causal_visible_rank, 3)
        self.assertEqual(closure.causal_invisible_rank, 0)

        self.assertEqual(first_distinguishing_depth((0, 0, 0), (1, 0, 0), closure), 0)
        self.assertEqual(first_distinguishing_depth((0, 0, 0), (0, 1, 0), closure), 1)
        self.assertEqual(first_distinguishing_depth((0, 0, 0), (0, 0, 1), closure), 2)

    def test_identity_future_keeps_only_current_observation_rank(self):
        identity = (
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
        )
        closure = causal_future_closure((identity,), ((1, 1, 1),))
        self.assertEqual(closure.ranks, (1,))
        self.assertEqual(closure.stable_depth, 0)
        self.assertEqual(closure.causal_visible_rank, 1)
        self.assertEqual(closure.causal_invisible_rank, 2)
        self.assertTrue(future_indistinguishable((1, 0, 0), (0, 1, 0), closure))
        self.assertFalse(future_indistinguishable((1, 0, 0), (0, 0, 0), closure))

    def test_multiple_operations_can_jointly_reveal_more_than_each_route(self):
        reveal_second = (
            (0, 1, 0),
            (0, 0, 0),
            (0, 0, 0),
        )
        reveal_third = (
            (0, 0, 1),
            (0, 0, 0),
            (0, 0, 0),
        )
        observation = ((1, 0, 0),)
        first = causal_future_closure((reveal_second,), observation)
        second = causal_future_closure((reveal_third,), observation)
        joint = causal_future_closure((reveal_second, reveal_third), observation)
        self.assertEqual(first.causal_visible_rank, 2)
        self.assertEqual(second.causal_visible_rank, 2)
        self.assertEqual(joint.causal_visible_rank, 3)

    def test_closure_stabilizes_with_at_most_state_dimension_strict_rank_gains(self):
        matrices = (
            (
                (0, 1, 0, 0),
                (0, 0, 1, 0),
                (0, 0, 0, 1),
                (0, 0, 0, 0),
            ),
        )
        closure = causal_future_closure(matrices, ((1, 0, 0, 0),))
        self.assertLessEqual(len(closure.ranks) - 1, 4)
        self.assertEqual(closure.ranks, (1, 2, 3, 4))

    def test_depth_equivalence_is_transitive_at_every_level(self):
        shift = (
            (0, 1, 0),
            (0, 0, 1),
            (0, 0, 0),
        )
        closure = causal_future_closure((shift,), ((1, 0, 0),))
        states = tuple(itertools.product(range(-1, 2), repeat=3))
        for depth in range(0, closure.stable_depth + 1):
            for left in states:
                for middle in states:
                    if not agreement_depth_ge(left, middle, closure, depth):
                        continue
                    for right in states:
                        if agreement_depth_ge(middle, right, closure, depth):
                            self.assertTrue(
                                agreement_depth_ge(left, right, closure, depth),
                                msg=(depth, left, middle, right),
                            )

    def test_first_distinguishing_depth_obeys_strong_similarity_law(self):
        shift = (
            (0, 1, 0),
            (0, 0, 1),
            (0, 0, 0),
        )
        closure = causal_future_closure((shift,), ((1, 0, 0),))
        states = tuple(itertools.product((0, 1), repeat=3))

        def depth_value(left, right):
            value = first_distinguishing_depth(left, right, closure)
            return closure.stable_depth + 1 if value is None else value

        # If two pairs remain equivalent through every depth below m, then the
        # third pair must do so as well.  Numerically this is the strong
        # similarity inequality s(x,z) >= min(s(x,y),s(y,z)).
        for left in states:
            for middle in states:
                for right in states:
                    self.assertGreaterEqual(
                        depth_value(left, right),
                        min(depth_value(left, middle), depth_value(middle, right)),
                    )


if __name__ == "__main__":
    unittest.main()
