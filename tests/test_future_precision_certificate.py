import unittest

from enterprise_math.future_precision_certificate import (
    a3_precision_certificate,
    a3_precision_refinement,
)


class FuturePrecisionCertificateTests(unittest.TestCase):
    def test_rank_one_residue_refinement_adds_torsion_without_hidden_rank_drop(self):
        fine_capacities = (1, 1, 1)
        guards = (
            (0, 1, 2),
            (0, -1, -2),
        )
        parent = ((0, 1, 2),)
        child = ((0, 2), (1,))

        parent_certificate = a3_precision_certificate(
            fine_capacities, guards, parent
        )
        child_certificate = a3_precision_certificate(
            fine_capacities, guards, child
        )
        self.assertEqual(parent_certificate.hidden_guard_rank, 1)
        self.assertEqual(child_certificate.hidden_guard_rank, 1)
        self.assertEqual(parent_certificate.guard_free_rank, 1)
        self.assertEqual(child_certificate.guard_free_rank, 1)
        self.assertEqual(parent_certificate.guard_torsion_factors, ())
        self.assertEqual(child_certificate.guard_torsion_factors, (2,))

        refinement = a3_precision_refinement(
            fine_capacities, guards, parent, child
        )
        self.assertEqual(refinement.relation_rank_gain, 1)
        self.assertEqual(refinement.hidden_guard_rank_drop, 0)
        self.assertEqual(refinement.guard_free_rank_gain, 0)
        self.assertEqual(refinement.relation_quantum_factor, 3)

    def test_full_guard_visibility_converts_hidden_rank_to_free_rank(self):
        fine_capacities = (1, 1, 1)
        guards = (
            (0, 1, 2),
            (0, -1, -2),
        )
        parent = ((0, 1, 2),)
        singleton = ((0,), (1,), (2,))
        refinement = a3_precision_refinement(
            fine_capacities, guards, parent, singleton
        )
        self.assertEqual(refinement.relation_rank_gain, 2)
        self.assertEqual(refinement.hidden_guard_rank_drop, 1)
        self.assertEqual(refinement.guard_free_rank_gain, 1)
        self.assertLessEqual(
            refinement.hidden_guard_rank_drop,
            refinement.relation_rank_gain,
        )
        self.assertEqual(refinement.child.hidden_guard_rank, 0)
        self.assertEqual(refinement.child.guard_free_rank, 2)

    def test_hidden_guard_rank_is_bounded_by_hidden_relation_rank(self):
        fine_capacities = (1, 1, 1, 1, 1)
        guards = (
            (0, 1, 2, 3, 4),
            (0, 1, 0, 1, 0),
            (2, -1, 3, 0, 4),
        )
        partitions = (
            ((0, 1, 2, 3, 4),),
            ((0, 1), (2, 3, 4)),
            ((0, 1), (2,), (3, 4)),
            ((0,), (1,), (2,), (3,), (4,)),
        )
        fine_relation_rank = len(fine_capacities) - 1
        for partition in partitions:
            certificate = a3_precision_certificate(
                fine_capacities, guards, partition
            )
            hidden_relation_rank = fine_relation_rank - certificate.relation_rank
            self.assertLessEqual(
                certificate.hidden_guard_rank,
                hidden_relation_rank,
            )

    def test_guard_free_and_hidden_ranks_sum_to_guard_count(self):
        fine_capacities = (2, 1, 3, 1)
        guards = (
            (0, 2, 4, 7),
            (1, 0, -1, 3),
            (2, 2, 2, 2),
        )
        for partition in (
            ((0, 1, 2, 3),),
            ((0, 2), (1, 3)),
            ((0,), (1,), (2, 3)),
        ):
            certificate = a3_precision_certificate(
                fine_capacities, guards, partition
            )
            self.assertEqual(
                certificate.hidden_guard_rank + certificate.guard_free_rank,
                certificate.guard_count,
            )


if __name__ == "__main__":
    unittest.main()
