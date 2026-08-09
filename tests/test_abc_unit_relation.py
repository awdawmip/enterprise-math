import unittest

from enterprise_math.abc_unit_relation import (
    mersenne_prime_unit_relation_access,
    minimum_block_derivative_access_radius,
    raw_block_derivative_coefficients,
    raw_block_derivative_image_generator,
    unit_relation_absorption_access,
    unit_relation_absorption_floor,
)


class AbcUnitRelationTests(unittest.TestCase):
    def test_block_derivative_images(self) -> None:
        self.assertEqual(raw_block_derivative_coefficients(242), ((2, 121), (11, 44)))
        self.assertEqual(raw_block_derivative_image_generator(242), 11)
        self.assertEqual(raw_block_derivative_coefficients(243), ((3, 405),))
        self.assertEqual(raw_block_derivative_image_generator(243), 405)

    def test_unit_floor_is_lcm_of_block_images(self) -> None:
        data = unit_relation_absorption_floor(242, 243)
        self.assertEqual(data["block_generator_b"], 11)
        self.assertEqual(data["block_generator_c"], 405)
        self.assertEqual(data["wronskian_image_generator"], 4455)
        self.assertEqual(data["multiplicity_residual_product"], 891)
        self.assertEqual(data["eta_min"], 5)
        self.assertEqual(data["target_multiple_b"], 405)
        self.assertEqual(data["target_multiple_c"], 11)

    def test_unit_access_decomposes_into_independent_blocks(self) -> None:
        data = unit_relation_absorption_access(242, 243)
        self.assertEqual(data["block_witness_b"]["coordinates"], (27, 27))
        self.assertEqual(data["block_witness_b"]["radius"], 27)
        self.assertEqual(data["block_witness_c"]["coordinates"], (11,))
        self.assertEqual(data["block_witness_c"]["radius"], 11)
        self.assertEqual(data["nu"], 27)

        high_quality = unit_relation_absorption_access(512, 513)
        self.assertEqual(high_quality["eta_min"], 3)
        self.assertEqual(high_quality["nu"], 13)

    def test_squarefree_sophie_examples_are_block_bezout_access(self) -> None:
        first = unit_relation_absorption_access(10, 11)
        self.assertEqual(first["eta_min"], 1)
        self.assertEqual(first["nu"], 2)

        second = unit_relation_absorption_access(22, 23)
        self.assertEqual(second["eta_min"], 1)
        self.assertEqual(second["nu"], 5)

    def test_mersenne_prime_family(self) -> None:
        m5 = mersenne_prime_unit_relation_access(5)
        self.assertEqual(m5["mersenne_prime"], 31)
        self.assertEqual(m5["eta_min"], 5)
        self.assertEqual(m5["mu"], 80)
        self.assertEqual(m5["nu"], 80)
        self.assertEqual(m5["floor_witness_q_2"], (80, 1))

        m7 = mersenne_prime_unit_relation_access(7)
        self.assertEqual(m7["mersenne_prime"], 127)
        self.assertEqual(m7["eta_min"], 7)
        self.assertEqual(m7["nu"], 448)

    def test_block_helper_rejects_higher_support_without_hidden_bruteforce(self) -> None:
        # 30 has three prime coordinates; the generic higher-rank problem must
        # remain explicit rather than silently invoking an expensive search.
        with self.assertRaises(ValueError):
            minimum_block_derivative_access_radius(30, 1)


if __name__ == "__main__":
    unittest.main()
