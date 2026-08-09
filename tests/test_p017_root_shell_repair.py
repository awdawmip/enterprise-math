import unittest

from enterprise_math.p017_root_shell_repair import (
    minimal_repair_symbol,
    minimal_root_shell_repair_alphabet_size,
    minimally_repaired_root_images,
    minimally_repaired_root_overlaps,
    p2_bit_matches_shell,
    p2_shell_bit,
    root_shell_split_multiplicities,
    uniform_repaired_root_images,
    uniform_repaired_root_overlaps,
)


class RootShellRepairTests(unittest.TestCase):
    def test_complete_small_actual_collision_classification_is_pinned(self) -> None:
        expected = {
            5: {3: 2},
            8: {5: 2},
        }
        actual = {}
        for k in range(4, 12):
            splits = {
                root: multiplicity
                for root, multiplicity in root_shell_split_multiplicities(k).items()
                if multiplicity > 1
            }
            if splits:
                actual[k] = splits
        self.assertEqual(actual, expected)

    def test_k6_has_no_realized_root_shell_split(self) -> None:
        self.assertTrue(
            all(value == 1 for value in root_shell_split_multiplicities(6).values())
        )
        self.assertEqual(minimal_root_shell_repair_alphabet_size(6), 1)

    def test_p2_bit_is_exact_shell_indicator(self) -> None:
        for k in range(4, 500):
            self.assertTrue(p2_bit_matches_shell(k), k)

    def test_uniform_p2_feature_repairs_all_realized_shells(self) -> None:
        for k in range(4, 1000):
            self.assertEqual(
                uniform_repaired_root_overlaps(k),
                (),
                (k, uniform_repaired_root_overlaps(k)),
            )

    def test_minimal_repair_repairs_all_realized_shells(self) -> None:
        for k in range(4, 1000):
            self.assertEqual(
                minimally_repaired_root_overlaps(k),
                (),
                (k, minimally_repaired_root_overlaps(k)),
            )

    def test_exact_minimum_repair_alphabet_profile(self) -> None:
        for k in range(4, 500):
            expected = 2 if k in {5, 8} else 1
            self.assertEqual(minimal_root_shell_repair_alphabet_size(k), expected, k)

    def test_minimal_repair_symbol_activates_only_at_actual_collisions(self) -> None:
        for k in range(4, 20):
            images = minimally_repaired_root_images(k)
            used_symbols = {symbol for shell in images.values() for _, symbol in shell}
            if k in {5, 8}:
                self.assertEqual(used_symbols, {0, 1}, k)
            else:
                self.assertEqual(used_symbols, {0}, k)

    def test_uniform_feature_can_be_informative_when_repair_is_unnecessary(self) -> None:
        uniform_symbols = {
            symbol for shell in uniform_repaired_root_images(6).values() for _, symbol in shell
        }
        minimal_symbols = {
            symbol for shell in minimally_repaired_root_images(6).values() for _, symbol in shell
        }
        self.assertEqual(uniform_symbols, {0, 1})
        self.assertEqual(minimal_symbols, {0})

    def test_collision_repairs_at_k5_and_k8(self) -> None:
        self.assertIn((3, 1), uniform_repaired_root_images(5)[2])
        self.assertIn((3, 0), uniform_repaired_root_images(5)[3])

        self.assertIn((5, 1), uniform_repaired_root_images(8)[2])
        self.assertIn((5, 0), uniform_repaired_root_images(8)[3])

        self.assertEqual(minimal_repair_symbol(5, 13), p2_shell_bit(5, 13))
        self.assertEqual(minimal_repair_symbol(8, 33), p2_shell_bit(8, 33))
        self.assertEqual(minimal_repair_symbol(6, 19), 0)


if __name__ == "__main__":
    unittest.main()
