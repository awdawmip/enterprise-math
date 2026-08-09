import unittest

from enterprise_math.witness_precision_layers import (
    exact_degeneracy_barrier_examples,
    minimal_additive_radius,
    witness_precision_layer_profile,
)


class WitnessPrecisionLayerTests(unittest.TestCase):
    def test_minimal_additive_radius(self) -> None:
        self.assertEqual(minimal_additive_radius(1, 36, 37), 3)
        self.assertEqual(minimal_additive_radius(1, 53, 54), 2)

    def test_one_plus_36_has_independent_nondegeneracy_cost(self) -> None:
        profile = witness_precision_layer_profile(1, 36, 37, max_bound=24)
        self.assertEqual(profile["lambda_abc"], 6)
        self.assertEqual(profile["rho"], 3)
        self.assertEqual(profile["combined_floor"], 6)
        self.assertEqual(profile["mu"], 12)
        self.assertEqual(profile["nondegeneracy_overhead"], 6)
        self.assertEqual(profile["U2"], 24)

    def test_one_plus_53_has_large_exact_degeneracy_barrier(self) -> None:
        profile = witness_precision_layer_profile(1, 53, 54, max_bound=27)
        self.assertEqual(profile["lambda_abc"], 9)
        self.assertEqual(profile["rho"], 2)
        self.assertEqual(profile["combined_floor"], 9)
        self.assertEqual(profile["mu"], 27)
        self.assertEqual(profile["nondegeneracy_overhead"], 18)
        self.assertEqual(profile["U2"], 27)
        self.assertEqual(profile["upper_gap"], 0)

    def test_flag_layer_can_be_redundant_on_easy_state(self) -> None:
        profile = witness_precision_layer_profile(1, 2, 3)
        self.assertEqual(profile["lambda_abc"], 1)
        self.assertEqual(profile["rho"], 1)
        self.assertEqual(profile["mu"], 1)
        self.assertEqual(profile["nondegeneracy_overhead"], 0)

    def test_fixed_barrier_examples(self) -> None:
        examples = exact_degeneracy_barrier_examples()
        self.assertEqual(len(examples), 2)
        self.assertTrue(all(example["nondegeneracy_overhead"] > 0 for example in examples))


if __name__ == "__main__":
    unittest.main()
