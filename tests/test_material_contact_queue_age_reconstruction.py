import unittest
from itertools import product

from enterprise_math.material_contact_queue_age_precision import (
    ContactWholeQueueAgeState,
    age_total_future_key,
    pure_aging_total_trace,
)
from enterprise_math.material_contact_queue_age_reconstruction import (
    age_future_key_from_total_trace,
    age_histogram_from_full_total_trace,
    verify_age_trace_key_inversion,
)


class MaterialContactQueueAgeReconstructionTests(unittest.TestCase):
    def test_closed_difference_reconstruction_example(self):
        state = ContactWholeQueueAgeState((2, 3, 5, 7))
        trace = pure_aging_total_trace(state, 3)
        self.assertEqual(trace, (17, 10, 5, 2))
        self.assertEqual(
            age_future_key_from_total_trace(trace),
            (2, 3, 5, 7),
        )
        self.assertEqual(
            age_histogram_from_full_total_trace(trace, 4),
            state,
        )

    def test_partial_trace_inverts_exact_future_key(self):
        state = ContactWholeQueueAgeState((1, 2, 3, 4, 5))
        for horizon in range(5):
            trace = pure_aging_total_trace(state, horizon)
            self.assertEqual(
                age_future_key_from_total_trace(trace),
                age_total_future_key(state, horizon),
            )
            self.assertTrue(verify_age_trace_key_inversion(state, horizon))

    def test_exhaustive_small_histograms_reconstruct_without_division(self):
        for depth in range(1, 6):
            for buckets in product(range(4), repeat=depth):
                state = ContactWholeQueueAgeState(buckets)
                trace = pure_aging_total_trace(state, depth - 1)
                recovered = age_histogram_from_full_total_trace(
                    trace,
                    depth,
                )
                self.assertEqual(recovered, state)
                self.assertTrue(
                    verify_age_trace_key_inversion(state, depth - 1)
                )

    def test_future_differences_reveal_oldest_buckets_one_by_one(self):
        state = ContactWholeQueueAgeState((4, 1, 3, 2))
        trace = pure_aging_total_trace(state, 3)
        self.assertEqual(trace, (10, 8, 5, 4))
        self.assertEqual(trace[0] - trace[1], 2)
        self.assertEqual(trace[1] - trace[2], 3)
        self.assertEqual(trace[2] - trace[3], 1)
        self.assertEqual(trace[3], 4)

    def test_horizon_beyond_full_depth_adds_no_new_age_information(self):
        state = ContactWholeQueueAgeState((2, 0, 1))
        full_key = age_total_future_key(state, 2)
        self.assertEqual(full_key, state.buckets)
        for horizon in range(2, 8):
            self.assertTrue(verify_age_trace_key_inversion(state, horizon))
            self.assertEqual(age_total_future_key(state, horizon), full_key)

    def test_invalid_nonmonotone_trace_is_rejected(self):
        with self.assertRaises(ValueError):
            age_future_key_from_total_trace((3, 4))
        with self.assertRaises(ValueError):
            age_future_key_from_total_trace(())
        with self.assertRaises(ValueError):
            age_future_key_from_total_trace((3, -1))
        with self.assertRaises(TypeError):
            age_future_key_from_total_trace((3, False))

    def test_full_reconstruction_requires_exact_trace_length(self):
        with self.assertRaises(ValueError):
            age_histogram_from_full_total_trace((3, 2), 3)
        with self.assertRaises(ValueError):
            age_histogram_from_full_total_trace((3, 2, 1), 0)
        with self.assertRaises(TypeError):
            age_histogram_from_full_total_trace((3,), False)


if __name__ == "__main__":
    unittest.main()
