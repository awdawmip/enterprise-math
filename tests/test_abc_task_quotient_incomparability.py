import unittest
from fractions import Fraction

from enterprise_math.abc_task_quotient_incomparability import (
    future_query_separation_examples,
    same_pair_selector_different_projective_counterexample,
    same_projective_different_pair_selector_counterexample,
)


class AbcTaskQuotientIncomparabilityTests(unittest.TestCase):
    def test_pair_selector_does_not_determine_projective_state(self) -> None:
        data = same_pair_selector_different_projective_counterexample()
        self.assertEqual(data["shared_pair_selector"], 2)
        self.assertEqual(data["projective_values"], (Fraction(1, 1), Fraction(2, 1)))

    def test_projective_state_does_not_determine_pair_selector(self) -> None:
        data = same_projective_different_pair_selector_counterexample()
        self.assertEqual(data["shared_projective"], Fraction(1, 1))
        self.assertEqual(data["pair_selectors"], (2, 5))

    def test_declared_future_queries_separate_the_collisions(self) -> None:
        data = future_query_separation_examples()
        self.assertEqual(
            data,
            {
                "pcc_half_123": True,
                "pcc_half_134": False,
                "pair_le_3_123": True,
                "pair_le_3_156": False,
            },
        )


if __name__ == "__main__":
    unittest.main()
