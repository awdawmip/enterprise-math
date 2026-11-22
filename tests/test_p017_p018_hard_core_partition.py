import ast
import inspect
import unittest

from enterprise_math import p017_p018_hard_core_partition as partition_module
from enterprise_math.p017_p018_hard_core_partition import (
    residual_affine_cell,
    residual_hard_core_partition,
    residual_hard_core_record,
)


class P017P018HardCorePartitionTests(unittest.TestCase):
    def test_k64_sharp_bridge_row_has_one_exact_ordered_cell(self):
        data = residual_hard_core_record(64, 47)
        self.assertEqual((data["lower_core"], data["upper_core"]), (9, 7))
        self.assertEqual((data["lower_tail"], data["upper_tail"]), (457, 601))
        self.assertEqual(data["core_product"], 63)

        cell = residual_affine_cell(64, 47)
        self.assertEqual(cell["cell_key"], (9, 7))
        self.assertEqual(cell["parity_modulus"], 126)
        self.assertEqual(cell["residual_lifts"], (47,))
        self.assertEqual(cell["simultaneous_prime_count"], 1)

    def test_k631_repeated_cell_recovers_exact_two_prime_lifts(self):
        cell = residual_affine_cell(631, 93)
        self.assertEqual(cell["cell_key"], (7, 5))
        self.assertEqual(cell["parity_modulus"], 70)
        self.assertEqual(cell["residual_lifts"], (93, 513))
        self.assertEqual(cell["simultaneous_prime_count"], 2)
        for row in cell["orbit"]:
            if row["radius"] in (93, 513):
                self.assertTrue(row["simultaneous_prime"])
                self.assertTrue(row["exact_same_cell"])
                self.assertTrue(row["anchor_survives"])

    def test_k118_is_a_small_repeated_exact_cell(self):
        cell = residual_affine_cell(118, 5)
        self.assertEqual(cell["cell_key"], (3, 11))
        self.assertEqual(cell["residual_lifts"], (5, 71))
        self.assertEqual(cell["simultaneous_prime_count"], 2)

    def test_partition_is_exact_and_disjoint_on_bounded_range(self):
        saw_nonempty = False
        saw_repeated = False
        for k in range(4, 181):
            data = residual_hard_core_partition(k)
            self.assertEqual(data["residual_count"], data["cell_prime_lift_mass"])
            radii = tuple(data["residual_radii"])
            self.assertEqual(len(radii), len(set(radii)))
            saw_nonempty |= bool(radii)
            for key, cell in data["cells"].items():
                self.assertEqual(tuple(cell["cell_key"]), key)
                actual = tuple(
                    radius
                    for radius in radii
                    if (
                        residual_hard_core_record(k, radius)["lower_core"],
                        residual_hard_core_record(k, radius)["upper_core"],
                    )
                    == key
                )
                self.assertEqual(tuple(sorted(cell["residual_lifts"])), actual)
                saw_repeated |= cell["simultaneous_prime_count"] > 1
        self.assertTrue(saw_nonempty)
        self.assertTrue(saw_repeated)

    def test_nonresidual_radius_is_rejected(self):
        with self.assertRaises(ValueError):
            residual_hard_core_record(64, 1)
        with self.assertRaises(ValueError):
            residual_hard_core_record(64, 2)
        with self.assertRaises(ValueError):
            residual_hard_core_record(64, 64)

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(partition_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
