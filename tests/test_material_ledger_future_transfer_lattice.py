import unittest
from itertools import product

from enterprise_math.material_ledger_future_transfer_lattice import (
    difference_hidden_from_all_future_component_totals,
    difference_is_redistribution_in_every_future_graph,
    future_component_observation_saturation_index,
    future_transfer_lattice_report,
    independent_joint_future_rows,
    joint_future_component_sum_matrix,
    joint_future_component_sum_rank,
    joint_future_component_sum_signature,
    maximal_minor_gcd,
    minimal_linear_future_signature,
    pairwise_connectivity_meet_blocks,
)


class MaterialLedgerFutureTransferLatticeTests(unittest.TestCase):
    def test_crossing_two_partitions_refute_connectivity_meet_minimality(self):
        compartments = (0, 1, 2, 3)
        future = (
            ((0, 1), (2, 3)),
            ((0, 2), (1, 3)),
        )
        meet = pairwise_connectivity_meet_blocks(compartments, future)
        self.assertEqual(
            set(meet),
            {
                frozenset({0}),
                frozenset({1}),
                frozenset({2}),
                frozenset({3}),
            },
        )
        self.assertEqual(joint_future_component_sum_rank(compartments, future), 3)
        report = future_transfer_lattice_report(compartments, future)
        self.assertEqual(report.connectivity_meet_block_count, 4)
        self.assertEqual(report.joint_observation_rank, 3)
        self.assertEqual(report.hidden_difference_rank, 1)

        hidden = (1, -1, -1, 1)
        self.assertTrue(
            difference_hidden_from_all_future_component_totals(
                compartments,
                future,
                hidden,
            )
        )
        self.assertTrue(
            difference_is_redistribution_in_every_future_graph(
                compartments,
                future,
                hidden,
            )
        )

        left = {0: 1, 1: 0, 2: 0, 3: 1}
        right = {0: 0, 1: 1, 2: 1, 3: 0}
        self.assertNotEqual(left, right)
        self.assertEqual(
            joint_future_component_sum_signature(compartments, future, left),
            joint_future_component_sum_signature(compartments, future, right),
        )
        self.assertEqual(
            minimal_linear_future_signature(compartments, future, left),
            minimal_linear_future_signature(compartments, future, right),
        )

    def test_three_pair_partitions_are_injective_but_nonunimodular(self):
        compartments = (0, 1, 2, 3)
        future = (
            ((0, 1), (2, 3)),
            ((0, 2), (1, 3)),
            ((0, 3), (1, 2)),
        )
        report = future_transfer_lattice_report(compartments, future)
        self.assertEqual(report.joint_observation_rank, 4)
        self.assertEqual(report.hidden_difference_rank, 0)
        self.assertTrue(report.joint_observation_injective)
        self.assertEqual(report.row_lattice_saturation_index, 2)
        self.assertTrue(report.injective_but_nonunimodular)
        self.assertEqual(
            future_component_observation_saturation_index(compartments, future),
            2,
        )

        # Bounded direct check: the complete future signature is injective.
        seen = {}
        for values in product(range(3), repeat=4):
            ledger = dict(zip(compartments, values, strict=True))
            signature = joint_future_component_sum_signature(
                compartments,
                future,
                ledger,
            )
            self.assertNotIn(signature, seen, (values, seen.get(signature)))
            seen[signature] = values

    def test_single_graph_reduces_to_one_total_per_connected_component(self):
        compartments = (0, 1, 2, 3, 4)
        future = (((0, 1), (1, 2), (3, 4)),)
        report = future_transfer_lattice_report(compartments, future)
        self.assertEqual(report.joint_observation_rank, 2)
        self.assertEqual(report.hidden_difference_rank, 3)
        self.assertEqual(report.connectivity_meet_block_count, 2)
        self.assertEqual(report.row_lattice_saturation_index, 1)
        rows = independent_joint_future_rows(compartments, future)
        self.assertEqual(len(rows), 2)

    def test_joint_signature_and_rank_handle_future_merging_and_splitting(self):
        compartments = (0, 1, 2)
        connected = ((0, 1), (1, 2))
        split = ((0, 1),)

        connected_only = future_transfer_lattice_report(
            compartments,
            (connected,),
        )
        self.assertEqual(connected_only.joint_observation_rank, 1)

        connected_and_split = future_transfer_lattice_report(
            compartments,
            (connected, split),
        )
        self.assertEqual(connected_and_split.joint_observation_rank, 2)
        self.assertEqual(connected_and_split.hidden_difference_rank, 1)

        with_discrete = future_transfer_lattice_report(
            compartments,
            (connected, ()),
        )
        self.assertEqual(with_discrete.joint_observation_rank, 3)
        self.assertEqual(with_discrete.hidden_difference_rank, 0)

    def test_joint_kernel_equals_component_zero_sum_condition_exhaustively(self):
        compartments = (0, 1, 2)
        graph_families = (
            (((0, 1),),),
            (((0, 1),), ((1, 2),)),
            (((0, 1), (1, 2)), ((0, 2),)),
            ((), ((0, 1), (1, 2))),
        )
        for future in graph_families:
            for difference in product(range(-2, 3), repeat=3):
                self.assertEqual(
                    difference_hidden_from_all_future_component_totals(
                        compartments,
                        future,
                        difference,
                    ),
                    difference_is_redistribution_in_every_future_graph(
                        compartments,
                        future,
                        difference,
                    ),
                    (future, difference),
                )

    def test_independent_rows_have_same_equality_kernel_as_full_signature(self):
        compartments = (0, 1, 2, 3)
        future = (
            ((0, 1), (2, 3)),
            ((0, 2), (1, 3)),
        )
        rows = independent_joint_future_rows(compartments, future)
        self.assertEqual(len(rows), 3)
        seen_full = {}
        seen_minimal = {}
        for values in product(range(3), repeat=4):
            ledger = dict(zip(compartments, values, strict=True))
            full = joint_future_component_sum_signature(compartments, future, ledger)
            minimal = minimal_linear_future_signature(compartments, future, ledger)
            seen_full.setdefault(full, set()).add(values)
            seen_minimal.setdefault(minimal, set()).add(values)
        self.assertEqual(
            {frozenset(group) for group in seen_full.values()},
            {frozenset(group) for group in seen_minimal.values()},
        )

    def test_maximal_minor_gcd_basic_cases(self):
        self.assertEqual(maximal_minor_gcd(((1, 0), (0, 1))), 1)
        self.assertEqual(maximal_minor_gcd(((2, 0), (0, 2))), 4)
        self.assertEqual(maximal_minor_gcd(((1, 1), (1, -1))), 2)
        self.assertEqual(maximal_minor_gcd(((1, 1, 0), (0, 1, 1))), 1)

    def test_validation(self):
        with self.assertRaises(ValueError):
            joint_future_component_sum_matrix((), ((),))
        with self.assertRaises(ValueError):
            joint_future_component_sum_matrix((0, 1), ())
        with self.assertRaises(ValueError):
            joint_future_component_sum_signature(
                (0, 1),
                ((),),
                {0: 1},
            )
        with self.assertRaises(ValueError):
            difference_hidden_from_all_future_component_totals(
                (0, 1),
                ((),),
                (1,),
            )


if __name__ == "__main__":
    unittest.main()
