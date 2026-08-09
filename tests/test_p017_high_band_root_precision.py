import unittest

from enterprise_math.p017_high_band_root_precision import (
    diagonal_goldbach_slices,
    diagonal_raw_root_data,
    diagonal_realized_root_data,
    raw_root_prime_labels,
    realized_root_shell_labels,
)


class P017HighBandRootPrecisionTests(unittest.TestCase):
    def test_diagonal_dual_window_is_previous_square_interval_up_to_two_offsets(self) -> None:
        for t in (6, 10, 20, 50, 100):
            data = diagonal_raw_root_data(t)
            self.assertEqual(data["factor_window"].lo, (t - 1) ** 2 + 3)
            self.assertEqual(data["factor_window"].hi, t * t)
            self.assertIn(data["count_difference"], (0, 1))

    def test_realized_shell_labels_are_a_subset_of_raw_window_labels(self) -> None:
        for k, root in ((56, 8), (317, 20), (1737, 45)):
            raw = set(raw_root_prime_labels(k, root))
            realized = set(realized_root_shell_labels(k, root))
            self.assertTrue(realized.issubset(raw))

    def test_high_band_one_bit_generalization_is_false(self) -> None:
        labels = realized_root_shell_labels(1737, 45)
        self.assertEqual(
            labels,
            (1429, 1439, 1447, 1451, 1459, 1471, 1481, 1489),
        )
        self.assertEqual(len(labels), 8)

    def test_diagonal_raw_burden_can_be_much_larger_than_realized_burden(self) -> None:
        data = diagonal_realized_root_data(100)
        self.assertEqual(data["raw_multiplicity"], 20)
        self.assertEqual(data["consecutive_square_prime_count"], 21)
        self.assertEqual(data["realized_multiplicity"], 3)

    def test_diagonal_realized_burden_already_exceeds_one_bit(self) -> None:
        data = diagonal_realized_root_data(200)
        self.assertEqual(data["raw_multiplicity"], 39)
        self.assertEqual(data["realized_multiplicity"], 6)

    def test_two_goldbach_slices_exactly_reconstruct_diagonal_realizability(self) -> None:
        for t in range(6, 101):
            data = diagonal_goldbach_slices(t)
            direct = diagonal_realized_root_data(t)
            self.assertEqual(
                tuple(data["goldbach_label_union"]),
                tuple(direct["realized_prime_labels"]),
            )

    def test_same_shell_label_can_have_both_goldbach_witness_types(self) -> None:
        data = diagonal_goldbach_slices(11)
        self.assertIn(107, data["sum_2k_plus_2"])
        self.assertIn(107, data["sum_2k_plus_4"])
        self.assertEqual(data["sum_2k_plus_2"][107], 137)
        self.assertEqual(data["sum_2k_plus_4"][107], 139)


if __name__ == "__main__":
    unittest.main()
