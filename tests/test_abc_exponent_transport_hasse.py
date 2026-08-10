import unittest

from enterprise_math.abc_exponent_transport_hasse import (
    exponent_transport_cover_path,
    exponent_transport_diamond_holds,
    primitive_same_sign_exponent,
    same_sign_cover_predecessors,
)


class ExponentTransportHasseTests(unittest.TestCase):
    def test_difference_primitive_roots_are_exactly_primes(self) -> None:
        expected = {2, 3, 5, 7, 11, 13, 17, 19}
        actual = {
            n for n in range(2, 21)
            if primitive_same_sign_exponent(n, "difference")
        }
        self.assertEqual(actual, expected)

    def test_sum_primitive_roots_are_odd_primes_and_powers_of_two(self) -> None:
        expected = {2, 3, 4, 5, 7, 8, 11, 13, 16, 17, 19}
        actual = {
            n for n in range(2, 21)
            if primitive_same_sign_exponent(n, "sum")
        }
        self.assertEqual(actual, expected)

    def test_same_exponent_can_be_primitive_for_sum_but_not_difference(self) -> None:
        self.assertFalse(primitive_same_sign_exponent(4, "difference"))
        self.assertTrue(primitive_same_sign_exponent(4, "sum"))
        diff_covers = same_sign_cover_predecessors(4, "difference")
        self.assertEqual(
            [(edge.lower_exponent, edge.prime_ratio) for edge in diff_covers],
            [(2, 2)],
        )
        self.assertEqual(same_sign_cover_predecessors(4, "sum"), ())

    def test_cover_predecessors_record_only_prime_ratio_edges(self) -> None:
        diff = same_sign_cover_predecessors(12, "difference")
        self.assertEqual(
            {(edge.lower_exponent, edge.prime_ratio) for edge in diff},
            {(6, 2), (4, 3)},
        )
        summ = same_sign_cover_predecessors(12, "sum")
        self.assertEqual(
            [(edge.lower_exponent, edge.prime_ratio) for edge in summ],
            [(4, 3)],
        )

    def test_resonant_cube_to_ninth_sum_is_one_cover_edge(self) -> None:
        path = exponent_transport_cover_path(11, 13, 3, 9, "sum")
        self.assertEqual(len(path.covers), 1)
        self.assertEqual(path.covers[0].prime_ratio, 3)
        self.assertEqual(path.path_multiplier, 1)
        self.assertEqual(path.path_multiplier, path.direct_multiplier)

    def test_difference_cover_products_are_path_independent(self) -> None:
        path_one = exponent_transport_cover_path(
            3, 5, 2, 12, "difference", (2, 3)
        )
        path_two = exponent_transport_cover_path(
            3, 5, 2, 12, "difference", (3, 2)
        )
        self.assertEqual(path_one.path_multiplier, path_two.path_multiplier)
        self.assertEqual(path_one.direct_multiplier, path_two.direct_multiplier)
        self.assertTrue(exponent_transport_diamond_holds(3, 5, 2, 2, 3, "difference"))

    def test_sum_rejects_even_cover_ratio(self) -> None:
        with self.assertRaises(ValueError):
            exponent_transport_cover_path(3, 5, 2, 4, "sum")


if __name__ == "__main__":
    unittest.main()
