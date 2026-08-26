import unittest

from enterprise_math.p017_p018_complete_core_tail import (
    complete_core_tail_profile,
    complete_core_tail_row,
)


class P017P018CompleteCoreTailTests(unittest.TestCase):
    def test_k22_representatives_of_all_three_classes(self):
        prime = complete_core_tail_row(22, 503, ())
        self.assertEqual(prime["kind"], "PRIME")
        self.assertEqual(prime["complete_transverse_core"], 1)
        self.assertEqual(prime["quotient"], 503)

        smooth = complete_core_tail_row(22, 525, (3, 5, 7))
        self.assertEqual(smooth["kind"], "FULLY_K_SMOOTH")
        self.assertEqual(smooth["complete_transverse_core"], 525)
        self.assertEqual(smooth["quotient"], 1)

        tail = complete_core_tail_row(22, 493, (17,))
        self.assertEqual(tail["kind"], "ONE_LARGE_PRIME_TAIL")
        self.assertEqual(tail["complete_transverse_core"], 17)
        self.assertEqual(tail["quotient"], 29)
        self.assertEqual(tail["large_prime_tail"], 29)

    def test_k22_profile_is_an_exact_partition(self):
        data = complete_core_tail_profile(22)

        self.assertEqual(data["signed_state_count"], 20)
        self.assertEqual(data["prime_state_count"], 7)
        self.assertEqual(data["fully_k_smooth_count"], 3)
        self.assertEqual(data["one_large_prime_tail_count"], 10)
        self.assertTrue(data["large_prime_tails_globally_distinct"])
        self.assertEqual(
            data["prime_state_count"]
            + data["fully_k_smooth_count"]
            + data["one_large_prime_tail_count"],
            data["signed_state_count"],
        )


if __name__ == "__main__":
    unittest.main()
