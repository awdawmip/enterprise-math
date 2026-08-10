import unittest
from itertools import product
from math import comb

from enterprise_math.material_contact_queue_age_precision import (
    ContactWholeQueueAgeState,
    age_key_matches_total_trace,
    age_queue_step,
    age_total_future_key,
    consume_then_age_queue,
    fifo_lifo_future_total_diverges,
    fixed_total_age_class_count,
    linear_age_readout_descends_to_total,
    pure_aging_total_trace,
)


def weak_compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in weak_compositions(total - first, parts - 1):
            yield (first, *rest)


class MaterialContactQueueAgePrecisionTests(unittest.TestCase):
    def test_ttl_aging_total_ledger_and_oldest_expiry(self):
        state = ContactWholeQueueAgeState((2, 3, 5, 7))
        step = age_queue_step(state, 11)
        self.assertEqual(step.expired_quanta, 7)
        self.assertEqual(step.after.buckets, (11, 2, 3, 5))
        self.assertEqual(step.after.total, 21)
        self.assertEqual(step.after.total, state.total + 11 - 7)

    def test_same_current_total_can_split_next_total_under_ttl(self):
        left = ContactWholeQueueAgeState((2, 1, 0))
        right = ContactWholeQueueAgeState((1, 0, 2))
        self.assertEqual(left.total, right.total)
        self.assertNotEqual(left.oldest, right.oldest)
        left_next = age_queue_step(left, 0).after
        right_next = age_queue_step(right, 0).after
        self.assertNotEqual(left_next.total, right_next.total)
        self.assertEqual((left_next.total, right_next.total), (3, 1))

    def test_future_key_is_exactly_equivalent_to_total_trace_exhaustively(self):
        for depth in range(1, 6):
            states = tuple(
                ContactWholeQueueAgeState(buckets)
                for buckets in product(range(3), repeat=depth)
            )
            for horizon in range(depth + 3):
                by_key = {}
                by_trace = {}
                for state in states:
                    key = age_total_future_key(state, horizon)
                    trace = pure_aging_total_trace(state, horizon)
                    by_key.setdefault(key, set()).add(state.buckets)
                    by_trace.setdefault(trace, set()).add(state.buckets)
                self.assertEqual(
                    {frozenset(group) for group in by_key.values()},
                    {frozenset(group) for group in by_trace.values()},
                )
                for left in states[: min(20, len(states))]:
                    for right in states[-min(20, len(states)) :]:
                        self.assertEqual(
                            age_key_matches_total_trace(left, right, horizon),
                            pure_aging_total_trace(left, horizon)
                            == pure_aging_total_trace(right, horizon),
                        )

    def test_key_peels_one_old_bucket_per_future_horizon(self):
        state = ContactWholeQueueAgeState((1, 2, 3, 4, 5))
        self.assertEqual(age_total_future_key(state, 0), (15,))
        self.assertEqual(age_total_future_key(state, 1), (10, 5))
        self.assertEqual(age_total_future_key(state, 2), (6, 4, 5))
        self.assertEqual(age_total_future_key(state, 3), (3, 3, 4, 5))
        self.assertEqual(age_total_future_key(state, 4), (1, 2, 3, 4, 5))
        self.assertEqual(age_total_future_key(state, 20), (1, 2, 3, 4, 5))

    def test_fixed_total_class_count_matches_weak_compositions(self):
        for depth in range(1, 7):
            for total in range(0, 8):
                states = tuple(
                    ContactWholeQueueAgeState(buckets)
                    for buckets in weak_compositions(total, depth)
                )
                self.assertEqual(len(states), comb(total + depth - 1, depth - 1))
                for horizon in range(depth + 3):
                    keys = {
                        age_total_future_key(state, horizon)
                        for state in states
                    }
                    expected = fixed_total_age_class_count(
                        total,
                        depth,
                        horizon,
                    )
                    self.assertEqual(len(keys), expected)
                    effective = min(horizon, depth - 1)
                    self.assertEqual(expected, comb(total + effective, effective))

    def test_full_age_precision_is_reached_at_depth_minus_one(self):
        depth = 5
        total = 6
        states = tuple(
            ContactWholeQueueAgeState(buckets)
            for buckets in weak_compositions(total, depth)
        )
        horizon = depth - 1
        self.assertEqual(
            fixed_total_age_class_count(total, depth, horizon),
            len(states),
        )
        self.assertEqual(
            len({age_total_future_key(state, horizon) for state in states}),
            len(states),
        )
        self.assertEqual(
            fixed_total_age_class_count(total, depth, horizon + 20),
            len(states),
        )

    def test_linear_age_readout_descends_to_total_iff_weights_are_constant(self):
        for depth in range(1, 6):
            for weights in product(range(-1, 2), repeat=depth):
                expected = len(set(weights)) == 1
                self.assertEqual(
                    linear_age_readout_descends_to_total(weights),
                    expected,
                )

    def test_fifo_lifo_same_applied_count_can_have_different_future_total(self):
        state = ContactWholeQueueAgeState((1, 0, 1))
        fifo = consume_then_age_queue(
            state,
            new_quanta=0,
            applied_quanta=1,
            policy="FIFO",
        )
        lifo = consume_then_age_queue(
            state,
            new_quanta=0,
            applied_quanta=1,
            policy="LIFO",
        )
        self.assertEqual(fifo.applied_quanta, lifo.applied_quanta)
        self.assertEqual(fifo.pre_age_survivors.total, 1)
        self.assertEqual(lifo.pre_age_survivors.total, 1)
        self.assertEqual(fifo.expired_quanta, 0)
        self.assertEqual(lifo.expired_quanta, 1)
        self.assertEqual(fifo.after.total, 1)
        self.assertEqual(lifo.after.total, 0)
        self.assertTrue(fifo_lifo_future_total_diverges(state, 0, 1))

    def test_fifo_lifo_can_differ_in_age_distribution_before_total_diverges(self):
        state = ContactWholeQueueAgeState((2, 1, 0, 0))
        fifo = consume_then_age_queue(
            state,
            new_quanta=1,
            applied_quanta=1,
            policy="FIFO",
        )
        lifo = consume_then_age_queue(
            state,
            new_quanta=1,
            applied_quanta=1,
            policy="LIFO",
        )
        self.assertEqual(fifo.after.total, lifo.after.total)
        self.assertNotEqual(fifo.after.buckets, lifo.after.buckets)
        # Even when the immediate total aliases, future TTL totals can split.
        self.assertNotEqual(
            pure_aging_total_trace(fifo.after, 3),
            pure_aging_total_trace(lifo.after, 3),
        )

    def test_consumption_with_new_quanta_is_exact_count_ledger(self):
        state = ContactWholeQueueAgeState((2, 3, 1))
        for policy in ("FIFO", "LIFO"):
            for new in range(3):
                for applied in range(state.total + new + 1):
                    step = consume_then_age_queue(
                        state,
                        new,
                        applied,
                        policy=policy,
                    )
                    self.assertEqual(
                        step.after.total,
                        state.total + new - applied - step.expired_quanta,
                    )

    def test_validation(self):
        with self.assertRaises(ValueError):
            ContactWholeQueueAgeState(())
        with self.assertRaises(ValueError):
            ContactWholeQueueAgeState((0, -1))
        state = ContactWholeQueueAgeState((1, 2))
        with self.assertRaises(ValueError):
            age_queue_step(state, -1)
        with self.assertRaises(ValueError):
            fixed_total_age_class_count(1, 0, 0)
        with self.assertRaises(ValueError):
            fixed_total_age_class_count(1, 2, -1)
        with self.assertRaises(ValueError):
            linear_age_readout_descends_to_total(())
        with self.assertRaises(ValueError):
            consume_then_age_queue(state, 0, 4, policy="FIFO")
        with self.assertRaises(ValueError):
            consume_then_age_queue(state, 0, 1, policy="RANDOM")
        with self.assertRaises(TypeError):
            age_queue_step(object(), 0)


if __name__ == "__main__":
    unittest.main()
