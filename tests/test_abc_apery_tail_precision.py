# Validation trigger only: no mathematical or executable semantics changed.
import unittest

from enterprise_math.abc_apery_tail_precision import (
    certified_tail_signature,
    exact_access_from_signature,
    exact_access_signature,
    same_apery_different_tail_onset_counterexample,
    same_tail_signature_different_raw_factorization_profile,
    tail_access_query,
)
from enterprise_math.abc_block_access_apery import exact_block_access_radius


class AbcAperyTailPrecisionTests(unittest.TestCase):
    def test_apery_values_alone_do_not_determine_tail_onset(self) -> None:
        data = same_apery_different_tail_onset_counterexample()
        self.assertEqual(data["period"], 22)
        self.assertEqual(data["target"], 16)
        self.assertEqual(data["access_radii"], (1, 2))

        first = data["first_tail_signature"]
        second = data["second_tail_signature"]
        q1 = tail_access_query(first, 16)
        q2 = tail_access_query(second, 16)
        self.assertTrue(q1["stable"])
        self.assertEqual(q1["radius"], 1)
        self.assertFalse(q2["stable"])
        self.assertEqual(q2["first_stable_target"], 38)

    def test_ceiling_half_factorization_cap_is_tail_complete(self) -> None:
        data = same_tail_signature_different_raw_factorization_profile()
        self.assertEqual(data["period"], 22)
        first_l, second_l = data["raw_linf_profiles"]
        self.assertNotEqual(first_l, second_l)

        first = certified_tail_signature((2, 4, 5, 11))
        second = certified_tail_signature((2, 5, 6, 9))
        for target in range(0, 120):
            q1 = tail_access_query(first, target)
            q2 = tail_access_query(second, target)
            self.assertEqual(q1, q2)

    def test_finite_signature_reconstructs_entire_access_function(self) -> None:
        for row in ((5, 2), (2, 5, 7, 8), (15, 10, 6), (11, 4)):
            signature = exact_access_signature(row)
            for target in range(0, 100):
                self.assertEqual(
                    exact_access_from_signature(signature, target),
                    exact_block_access_radius(row, target, max_radius=100),
                )

    def test_exception_table_is_small_in_working_examples(self) -> None:
        first = exact_access_signature((5, 2))
        self.assertEqual(first.exceptional_responses, ((1, 2),))

        second = exact_access_signature((2, 5, 7, 8))
        self.assertEqual(second.exceptional_responses, ((16, 2),))

        third = exact_access_signature((2, 4, 5, 11))
        self.assertEqual(third.exceptional_responses, ())

    def test_stable_formula_without_exception_table_is_partial_by_design(self) -> None:
        tail = certified_tail_signature((5, 2))
        query = tail_access_query(tail, 1)
        self.assertFalse(query["stable"])
        self.assertNotIn("radius", query)


if __name__ == "__main__":
    unittest.main()
