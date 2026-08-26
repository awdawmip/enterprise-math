import unittest

from enterprise_math.p017_tail_staircase import (
    exact_quotient_window,
    global_tail_staircase,
    odd_core_window_separation,
    small_core_tail_incidences,
)


class P017TailStaircaseTests(unittest.TestCase):
    def test_odd_core_windows_are_strictly_reverse_ordered(self) -> None:
        for k in range(5, 120):
            cores = list(range(3, k, 2))
            for index, smaller in enumerate(cores):
                for larger in cores[index + 1 : index + 9]:
                    data = odd_core_window_separation(k, smaller, larger)
                    self.assertLess(data["larger_window_max"], data["smaller_window_min"])

    def test_direct_window_endpoints_match_divisible_basin_quotients(self) -> None:
        for k in range(3, 70):
            for divisor in range(1, k + 1):
                quotients = [
                    n // divisor
                    for n in range(k * k + 1, (k + 1) * (k + 1))
                    if n % divisor == 0
                ]
                lower, upper = exact_quotient_window(k, divisor)
                expected = list(range(lower, upper + 1))
                self.assertEqual(quotients, expected)

    def test_small_core_tail_resources_are_globally_unique(self) -> None:
        saw_many = False
        for k in range(3, 180):
            rows = small_core_tail_incidences(k)
            tails = [int(row["tail_prime"]) for row in rows]
            self.assertEqual(len(tails), len(set(tails)))
            if len(rows) >= 20:
                saw_many = True
        self.assertTrue(saw_many)

    def test_tail_values_strictly_decrease_across_core_values(self) -> None:
        for k in range(5, 150):
            data = global_tail_staircase(k)
            cores = list(data["cores"])
            tails_by_core = data["tails_by_core"]
            for index, smaller in enumerate(cores):
                for larger in cores[index + 1 :]:
                    self.assertGreater(
                        min(tails_by_core[smaller]),
                        max(tails_by_core[larger]),
                    )

    def test_residual_hard_core_sides_consume_distinct_tails(self) -> None:
        # Any residual pair has both exact cores in (1,k), so its two sides are
        # included in TS02.  This regression locks a nontrivial basin example.
        data = global_tail_staircase(88)
        tails = [int(row["tail_prime"]) for row in data["incidences"]]
        self.assertEqual(len(tails), len(set(tails)))
        self.assertIn(2609, tails)
        self.assertIn(461, tails)


if __name__ == "__main__":
    unittest.main()
