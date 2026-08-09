import unittest

from enterprise_math.causal_operation_language import class_count, partition_refines
from enterprise_math.causal_semantic_saturation import (
    five_state_nonmonotone_example,
    safe_envelopes_incomparable_on_small_system,
    saturation_is_extensive,
    saturation_is_idempotent_on_small_system,
)


class CausalSemanticSaturationTests(unittest.TestCase):
    def test_saturation_is_extensive_and_idempotent_on_small_systems(self):
        states = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        generators = {
            "g": {0: 0, 1: 0, 2: 1, 3: 0},
            "h": {0: 0, 1: 3, 2: 0, 3: 0},
        }
        self.assertTrue(saturation_is_extensive(states, observation, generators))
        self.assertTrue(
            saturation_is_idempotent_on_small_system(
                states, observation, generators
            )
        )

    def test_more_required_operations_refine_state_but_safe_envelopes_can_be_incomparable(self):
        (
            states,
            observation,
            base,
            extended,
            base_partition,
            extended_partition,
        ) = five_state_nonmonotone_example()

        self.assertTrue(partition_refines(extended_partition, base_partition))
        self.assertEqual(class_count(base_partition), 2)
        self.assertEqual(class_count(extended_partition), 3)
        self.assertEqual(base_partition[0], base_partition[2])
        self.assertNotEqual(extended_partition[0], extended_partition[2])

        incomparable, base_only, extended_only = safe_envelopes_incomparable_on_small_system(
            states,
            base_partition,
            extended_partition,
        )
        self.assertTrue(incomparable)
        self.assertIsNotNone(base_only)
        self.assertIsNotNone(extended_only)

    def test_nonmonotonicity_is_not_failure_of_minimum_state_monotonicity(self):
        (
            states,
            observation,
            base,
            extended,
            base_partition,
            extended_partition,
        ) = five_state_nonmonotone_example()
        # Required languages are nested: empty subset {h}.  Minimum state behaves
        # monotonically as expected even though their maximal zero-cost envelopes do not.
        self.assertEqual(base, {})
        self.assertEqual(set(extended), {"h"})
        self.assertTrue(partition_refines(extended_partition, base_partition))


if __name__ == "__main__":
    unittest.main()
