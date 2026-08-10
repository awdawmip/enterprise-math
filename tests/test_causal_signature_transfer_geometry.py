import unittest

from enterprise_math.causal_signature_transfer_geometry import (
    future_language_refinement_shrinks_neutral_geometry,
    maximal_neutral_transfer_edges,
    partition_blocks,
    signature_direction_count,
    signature_transfer_rank,
    slot_future_partition,
    slot_signature_geometry_profile,
)


class CausalSignatureTransferGeometryTests(unittest.TestCase):
    def test_no_future_operations_use_current_slot_observation_classes(self):
        slots = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        partition = slot_future_partition(slots, observation, {})
        blocks = partition_blocks(slots, partition)
        self.assertEqual(tuple(map(len, blocks)), (3, 1))
        self.assertEqual(signature_transfer_rank(slots, partition), 2)
        self.assertEqual(signature_direction_count(slots, partition), 6)
        self.assertEqual(
            set(maximal_neutral_transfer_edges(slots, partition)),
            {(0, 1), (0, 2), (1, 2)},
        )

    def test_richer_future_language_splits_slot_types_and_removes_neutral_transfers(self):
        slots = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        coarse = {}
        rich = {
            "reveal2": {0: 0, 1: 1, 2: 3, 3: 3},
        }
        self.assertTrue(
            future_language_refinement_shrinks_neutral_geometry(
                slots, observation, coarse, rich
            )
        )
        coarse_profile = slot_signature_geometry_profile(slots, observation, coarse)
        rich_profile = slot_signature_geometry_profile(slots, observation, rich)
        self.assertEqual(coarse_profile, ((3, 1), 2, 6))
        self.assertEqual(rich_profile, ((2, 1, 1), 1, 2))

    def test_full_anonymity_gives_complete_transfer_and_all_distinct_types_give_rank_zero(self):
        slots = (0, 1, 2, 3, 4)
        anonymous = {slot: 0 for slot in slots}
        all_distinct = {slot: slot for slot in slots}
        anonymous_partition = slot_future_partition(slots, anonymous, {})
        distinct_partition = slot_future_partition(slots, all_distinct, {})
        self.assertEqual(signature_transfer_rank(slots, anonymous_partition), 4)
        self.assertEqual(signature_direction_count(slots, anonymous_partition), 20)
        self.assertEqual(signature_transfer_rank(slots, distinct_partition), 0)
        self.assertEqual(signature_direction_count(slots, distinct_partition), 0)

    def test_mixed_type_classes_give_direct_sum_of_complete_components(self):
        slots = (0, 1, 2, 3, 4, 5)
        observation = {0: "a", 1: "a", 2: "b", 3: "a", 4: "b", 5: "c"}
        partition = slot_future_partition(slots, observation, {})
        self.assertEqual(slot_signature_geometry_profile(slots, observation, {}), ((3, 2, 1), 3, 8))
        self.assertEqual(signature_transfer_rank(slots, partition), (3 - 1) + (2 - 1) + (1 - 1))


if __name__ == "__main__":
    unittest.main()
