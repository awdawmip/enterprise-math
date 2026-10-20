import unittest

from enterprise_math.p018_p023_quotient_word_storage import (
    minimum_storage_alphabets,
)
from enterprise_math.p018_p023_quotient_word_storage_union import (
    minimum_storage_alphabets_via_witness_union,
    minimum_storage_size_via_witness_union,
    witness_union_oracle_matches_subset_oracle,
)


class P018P023QuotientWordStorageUnionTests(unittest.TestCase):
    def test_union_oracle_matches_subset_oracle_small_domains(self):
        for root_exp in range(2, 5):
            for max_state in range(1, 13):
                for horizon in range(0, 4):
                    self.assertTrue(
                        witness_union_oracle_matches_subset_oracle(
                            max_state, root_exp, horizon
                        )
                    )

    def test_intermediate_multiple_optima_match_exactly(self):
        expected = {
            (2, 3, 4, 5, 7, 11),
            (2, 3, 5, 6, 7, 11),
            (2, 3, 5, 7, 11, 12),
        }
        self.assertEqual(
            set(minimum_storage_alphabets_via_witness_union(12, 3, 2)),
            expected,
        )
        self.assertEqual(
            set(minimum_storage_alphabets(12, 3, 2)),
            expected,
        )
        self.assertEqual(minimum_storage_size_via_witness_union(12, 3, 2), 6)

    def test_binary_like_storage_is_strictly_smaller_than_complete_capacity_dictionary(self):
        # N=24 in a high-root-order regime has all 2..24 as semantic actions.
        # At horizon 2, exact minimum storage is 11 primitive types; the full
        # Omega<=2 dictionary contains 17 types.  This is a regression boundary
        # separating capacity/latency optimality from storage optimality.
        solutions = minimum_storage_alphabets_via_witness_union(24, 10, 2)
        self.assertEqual(
            solutions,
            ((2, 3, 4, 5, 6, 7, 11, 13, 17, 19, 23),),
        )
        self.assertEqual(minimum_storage_size_via_witness_union(24, 10, 2), 11)

    def test_storage_curve_can_plateau_inside_intermediate_phase(self):
        # L_10(32)=5.  The exact storage profile is 31,15,12,12,11 for
        # horizons 1..5, so h=3->4 is an intermediate plateau rather than a
        # unit-step resource law.
        profile = tuple(
            minimum_storage_size_via_witness_union(32, 10, horizon)
            for horizon in range(1, 6)
        )
        self.assertEqual(profile, (31, 15, 12, 12, 11))


if __name__ == "__main__":
    unittest.main()
