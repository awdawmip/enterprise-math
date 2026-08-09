import unittest

from enterprise_math.quotient_basin import (
    iterated_quotient_flatness,
    open_divisible_cofactor_window,
    square_basin_iterated_quotient_transport,
    square_basin_quotient_transport,
    square_basin_quotient_window,
    strict_square_root_descent,
)


class QuotientBasinTests(unittest.TestCase):
    def test_statewise_two_basin_transport(self):
        saw_upper = False
        for k in range(1, 80):
            upper = (k + 1) * (k + 1)
            for divisor in range(2, min(2 * upper, 80) + 1):
                window = square_basin_quotient_window(k, divisor)
                for n in range(k * k, upper):
                    data = square_basin_quotient_transport(k, divisor, n)
                    self.assertLess(data["base_root"], k)
                    self.assertIn(
                        data["quotient_root"],
                        (data["base_root"], data["base_root"] + 1),
                    )
                    saw_upper |= data["quotient_root"] == data["base_root"] + 1
                self.assertEqual(window["q_min"], (k * k) // divisor)
                self.assertEqual(window["q_max"], (upper - 1) // divisor)
        self.assertTrue(saw_upper)

    def test_open_cofactor_window_lies_between_two_square_boundaries(self):
        saw_nonempty = False
        for k in range(1, 160):
            upper = (k + 1) * (k + 1) - 1
            for divisor in range(2, min(k + 20, 80) + 1):
                data = open_divisible_cofactor_window(k, divisor)
                if not data["nonempty"]:
                    continue
                saw_nonempty = True
                j = data["base_root"]
                self.assertLess(j * j, data["q_min_open"])
                self.assertLessEqual(data["q_min_open"], data["q_max"])
                self.assertLess(data["q_max"], (j + 2) * (j + 2))
                for q in range(data["q_min_open"], data["q_max"] + 1):
                    n = divisor * q
                    if k * k < n <= upper:
                        transported = square_basin_quotient_transport(k, divisor, n)
                        self.assertEqual(transported["quotient"], q)
        self.assertTrue(saw_nonempty)

    def test_iterated_floor_quotients_depend_only_on_total_divisor(self):
        paths = ([2], [2, 2], [2, 3], [3, 2], [2, 2, 3], [3, 5, 2])
        for n in range(0, 500):
            for divisors in paths:
                data = iterated_quotient_flatness(n, list(divisors))
                product = 1
                for divisor in divisors:
                    product *= divisor
                self.assertEqual(data["divisor_product"], product)
                self.assertEqual(data["iterated_quotient"], n // product)
                self.assertEqual(data["direct_quotient"], n // product)

    def test_iterated_paths_do_not_multiply_final_root_choices(self):
        paths = ([2, 2], [2, 3], [3, 2], [2, 5, 3])
        for k in range(1, 45):
            upper = (k + 1) * (k + 1)
            for n in range(k * k, upper):
                for divisors in paths:
                    data = square_basin_iterated_quotient_transport(
                        k, list(divisors), n
                    )
                    self.assertIn(
                        data["quotient_root"],
                        (data["base_root"], data["base_root"] + 1),
                    )
                    self.assertEqual(
                        data["iterated_quotient"], data["direct_quotient"]
                    )

    def test_actual_quotient_root_strictly_descends_from_k_three(self):
        for k in range(3, 100):
            upper = (k + 1) * (k + 1)
            for divisor in range(2, min(k + 20, 50) + 1):
                for n in range(k * k, upper):
                    data = strict_square_root_descent(k, divisor, n)
                    self.assertLess(data["quotient"], k * k)
                    self.assertLess(data["quotient_root"], k)

    def test_input_validation(self):
        with self.assertRaises(ValueError):
            square_basin_quotient_window(0, 2)
        with self.assertRaises(ValueError):
            square_basin_quotient_window(3, 1)
        with self.assertRaises(ValueError):
            square_basin_quotient_transport(3, 2, 8)
        with self.assertRaises(ValueError):
            square_basin_quotient_transport(3, 2, 16)
        with self.assertRaises(ValueError):
            iterated_quotient_flatness(10, [])
        with self.assertRaises(ValueError):
            iterated_quotient_flatness(10, [2, 1])
        with self.assertRaises(ValueError):
            strict_square_root_descent(2, 2, 4)


if __name__ == "__main__":
    unittest.main()
