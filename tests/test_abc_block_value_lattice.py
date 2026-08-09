import math
import unittest

from enterprise_math.abc_block_value_lattice import (
    block_value_absorption_floor,
    block_value_lattice_invariants,
    block_value_wronskian_image_generator,
)


class AbcBlockValueLatticeTests(unittest.TestCase):
    def test_prime_triple_has_full_z2_value_lattice(self) -> None:
        data = block_value_lattice_invariants(2, 3, 5)
        self.assertEqual(data.block_image_generators, (1, 1, 1))
        self.assertEqual(data.relation_content, 1)
        self.assertEqual(data.wronskian_minor_generators, (5, 3, 2))
        self.assertEqual(data.wronskian_image_generator, 1)
        self.assertEqual(data.absorption_floor, 1)
        self.assertEqual(data.lattice_index_in_z2, 1)

    def test_279_compressed_lattice_recovers_floor(self) -> None:
        data = block_value_lattice_invariants(2, 7, 9)
        self.assertEqual(data.block_image_generators, (1, 1, 6))
        self.assertEqual(data.wronskian_minor_generators, (9, 42, 12))
        self.assertEqual(data.wronskian_image_generator, 3)
        self.assertEqual(data.residual_product, 3)
        self.assertEqual(data.absorption_floor, 1)
        self.assertEqual(data.lattice_index_in_z2, 6)

    def test_irreducible_absorption_overhead_is_visible_in_block_lattice(self) -> None:
        data = block_value_lattice_invariants(5, 7, 12)
        self.assertEqual(data.block_image_generators, (1, 1, 4))
        self.assertEqual(data.wronskian_minor_generators, (12, 28, 20))
        self.assertEqual(data.wronskian_image_generator, 4)
        self.assertEqual(data.residual_product, 2)
        self.assertEqual(data.absorption_floor, 2)
        self.assertEqual(data.lattice_index_in_z2, 4)

    def test_unit_relation_reduces_to_lcm_intersection(self) -> None:
        first = block_value_lattice_invariants(1, 8, 9)
        self.assertEqual(first.block_image_generators, (0, 12, 6))
        self.assertEqual(first.relation_content, 6)
        self.assertEqual(first.wronskian_minor_generators, (0, 0, 12))
        self.assertEqual(first.wronskian_image_generator, 12)
        self.assertEqual(first.absorption_floor, 1)
        self.assertIsNone(first.lattice_index_in_z2)

        second = block_value_lattice_invariants(1, 242, 243)
        self.assertEqual(second.block_image_generators, (0, 11, 405))
        self.assertEqual(second.wronskian_image_generator, 4455)
        self.assertEqual(second.residual_product, 891)
        self.assertEqual(second.absorption_floor, 5)

    def test_helpers_match_full_invariant(self) -> None:
        self.assertEqual(block_value_wronskian_image_generator(1, 512, 513), 6912)
        self.assertEqual(block_value_absorption_floor(1, 512, 513), 3)

    def test_bounded_primitive_triples_match_previous_block_formula(self) -> None:
        checked = 0
        for c in range(3, 80):
            for a in range(1, c):
                b = c - a
                if math.gcd(a, b) != 1:
                    continue
                data = block_value_lattice_invariants(a, b, c)
                self.assertGreater(data.wronskian_image_generator, 0)
                self.assertGreater(data.absorption_floor, 0)
                checked += 1
        self.assertGreater(checked, 1000)


if __name__ == "__main__":
    unittest.main()
