import unittest

from enterprise_math.predictive_contact import (
    collapse_contact,
    contact_exit_time,
    contact_future_signature,
    contact_horizon_class_count,
    contact_horizon_rank,
    stable_contact_class_count,
    stable_contact_state_savings,
)
from enterprise_math.predictive_quotient import (
    finite_horizon_partition,
    restricted_block_count,
    stable_predictive_partition,
)


class PredictiveContactTests(unittest.TestCase):
    def test_exit_time_and_rank_match_direct_signatures(self) -> None:
        for precision in range(1, 20):
            for step in range(1, 10):
                for horizon in range(0, 12):
                    by_rank = {}
                    by_signature = {}
                    for gap in range(precision):
                        signature = contact_future_signature(gap, precision, step, horizon)
                        rank = contact_horizon_rank(gap, precision, step, horizon)
                        previous = by_rank.setdefault(rank, signature)
                        self.assertEqual(previous, signature)
                        previous_rank = by_signature.setdefault(signature, rank)
                        self.assertEqual(previous_rank, rank)
                    self.assertEqual(
                        len(by_rank),
                        contact_horizon_class_count(precision, step, horizon),
                    )

    def test_closed_form(self) -> None:
        for precision in range(1, 40):
            for step in range(1, 15):
                stable = (precision + step - 1) // step
                self.assertEqual(stable_contact_class_count(precision, step), stable)
                self.assertEqual(stable_contact_state_savings(precision, step), precision - stable)
                for horizon in range(0, 20):
                    self.assertEqual(
                        contact_horizon_class_count(precision, step, horizon),
                        min(horizon + 1, stable),
                    )

    def test_contact_bit_is_not_one_step_future_sufficient_when_boundary_can_exit(self) -> None:
        precision = 3
        step = 1
        self.assertTrue(collapse_contact(0, precision))
        self.assertTrue(collapse_contact(2, precision))
        self.assertTrue(collapse_contact(0 + step, precision))
        self.assertFalse(collapse_contact(2 + step, precision))
        self.assertEqual(contact_horizon_class_count(precision, step, 1), 2)

    def test_generic_compiler_reconstructs_contact_formula(self) -> None:
        for precision in range(1, 10):
            for step in range(1, 7):
                for horizon in range(0, 8):
                    max_gap = precision + (horizon + 3) * step
                    states = tuple(range(max_gap + 1))
                    actions = {"separate": lambda gap, s=step, cap=max_gap: min(cap, gap + s)}
                    observe = lambda gap, d=precision: gap < d
                    partition = finite_horizon_partition(states, actions, observe, horizon)
                    initial_contact = tuple(range(precision))
                    self.assertEqual(
                        restricted_block_count(states, partition, initial_contact),
                        contact_horizon_class_count(precision, step, horizon),
                    )

    def test_stable_compiler_matches_arbitrary_future_contact_count(self) -> None:
        for precision in range(1, 9):
            for step in range(1, 6):
                cap = precision + 8 * step
                states = tuple(range(cap + 1))
                actions = {"separate": lambda gap, s=step, c=cap: min(c, gap + s)}
                observe = lambda gap, d=precision: gap < d
                stable = stable_predictive_partition(states, actions, observe)
                initial_contact = tuple(range(precision))
                self.assertEqual(
                    restricted_block_count(states, stable.partition, initial_contact),
                    stable_contact_class_count(precision, step),
                )

    def test_exit_time_formula(self) -> None:
        for precision in range(1, 30):
            for step in range(1, 12):
                for gap in range(precision):
                    t = contact_exit_time(gap, precision, step)
                    self.assertTrue(collapse_contact(gap + (t - 1) * step, precision))
                    self.assertFalse(collapse_contact(gap + t * step, precision))


if __name__ == "__main__":
    unittest.main()
