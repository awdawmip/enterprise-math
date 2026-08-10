import itertools
import unittest

from enterprise_math.contact_cycle_capacity_topology import (
    active_edges_after_removal,
    contact_component_count,
    contact_cycle_rank,
    contact_removal_topology_report,
    first_exhaustion_topology_spectrum,
    first_witness_exhaustion,
)


TRIANGLE = ((0, 1), (1, 2), (2, 0))
PATH3 = ((0, 1), (1, 2))
FIGURE_EIGHT = (
    (0, 1),
    (1, 2),
    (2, 0),
    (0, 3),
    (3, 4),
    (4, 0),
)


class ContactCycleCapacityTopologyTests(unittest.TestCase):
    def test_first_exhaustion_reports_safe_cycles_and_all_bottlenecks(self):
        event = first_witness_exhaustion(
            (0, 0, 0),
            (2, 5, 5),
            (1, 1, 1),
        )
        self.assertEqual(event.safe_completed_repetitions, 2)
        self.assertEqual(event.first_exhaustion_attempt, 3)
        self.assertEqual(event.bottleneck_contacts, (0,))

        tied = first_witness_exhaustion(
            (0, 0, 0),
            (2, 2, 2),
            (1, 1, 1),
        )
        self.assertEqual(tied.safe_completed_repetitions, 2)
        self.assertEqual(tied.bottleneck_contacts, (0, 1, 2))

        uneven = first_witness_exhaustion(
            (1, 0, 3),
            (8, 7, 9),
            (3, 2, 0),
        )
        self.assertEqual(uneven.safe_completed_repetitions, 2)
        self.assertEqual(uneven.first_exhaustion_attempt, 3)
        self.assertEqual(uneven.bottleneck_contacts, (0,))

    def test_zero_memory_increment_never_exhausts(self):
        event = first_witness_exhaustion(
            (0, 5),
            (0, 5),
            (0, 0),
        )
        self.assertTrue(event.never_exhausts)
        self.assertIsNone(event.first_exhaustion_attempt)
        self.assertEqual(event.bottleneck_contacts, ())

    def test_unique_triangle_failure_turns_cycle_into_tree(self):
        spectrum = first_exhaustion_topology_spectrum(
            3,
            TRIANGLE,
            (0, 0, 0),
            (2, 5, 5),
            (1, 1, 1),
        )
        self.assertFalse(spectrum.topology_selector_is_required)
        self.assertEqual(spectrum.exhaustion.bottleneck_contacts, (0,))
        report = spectrum.simultaneous_bottleneck_removal
        assert report is not None
        self.assertEqual(report.before_cycle_rank, 1)
        self.assertEqual(report.after_cycle_rank, 0)
        self.assertEqual(report.component_increase, 0)
        self.assertEqual(report.cycle_rank_drop, 1)
        self.assertEqual(
            active_edges_after_removal(TRIANGLE, (0,)),
            ((1, 2), (2, 0)),
        )

    def test_equal_triangle_exhaustion_exposes_selector_boundary(self):
        spectrum = first_exhaustion_topology_spectrum(
            3,
            TRIANGLE,
            (0, 0, 0),
            (2, 2, 2),
            (1, 1, 1),
        )
        self.assertTrue(spectrum.topology_selector_is_required)
        self.assertEqual(len(spectrum.single_bottleneck_removals), 3)
        for report in spectrum.single_bottleneck_removals:
            self.assertEqual(report.after_cycle_rank, 0)
            self.assertEqual(report.after_component_count, 1)
            self.assertEqual(report.cycle_rank_drop, 1)

        simultaneous = spectrum.simultaneous_bottleneck_removal
        assert simultaneous is not None
        self.assertEqual(simultaneous.after_cycle_rank, 0)
        self.assertEqual(simultaneous.after_component_count, 3)
        self.assertEqual(simultaneous.component_increase, 2)
        self.assertEqual(simultaneous.cycle_rank_drop, 1)

    def test_bridge_removal_disconnects_without_changing_cycle_rank(self):
        report = contact_removal_topology_report(
            3,
            PATH3,
            (0,),
        )
        self.assertEqual(report.before_cycle_rank, 0)
        self.assertEqual(report.after_cycle_rank, 0)
        self.assertEqual(report.component_increase, 1)
        self.assertEqual(report.cycle_rank_drop, 0)
        self.assertTrue(report.disconnects_graph_further)

    def test_one_cycle_failure_in_figure_eight_removes_exactly_one_hidden_degree(self):
        report = contact_removal_topology_report(
            5,
            FIGURE_EIGHT,
            (0,),
        )
        self.assertEqual(report.before_cycle_rank, 2)
        self.assertEqual(report.after_cycle_rank, 1)
        self.assertEqual(report.component_increase, 0)
        self.assertEqual(report.cycle_rank_drop, 1)

        both = contact_removal_topology_report(
            5,
            FIGURE_EIGHT,
            (0, 3),
        )
        self.assertEqual(both.after_cycle_rank, 0)
        self.assertEqual(both.cycle_rank_drop, 2)

    def test_cycle_rank_removal_identity_exhaustively_on_small_graphs(self):
        for num_vertices in range(1, 5):
            possible_edges = tuple(
                (left, right)
                for left in range(num_vertices)
                for right in range(left + 1, num_vertices)
            )
            for mask in range(1 << len(possible_edges)):
                edges = tuple(
                    edge
                    for index, edge in enumerate(possible_edges)
                    if mask & (1 << index)
                )
                edge_count = len(edges)
                for removed_mask in range(1 << edge_count):
                    removed = tuple(
                        index
                        for index in range(edge_count)
                        if removed_mask & (1 << index)
                    )
                    report = contact_removal_topology_report(
                        num_vertices,
                        edges,
                        removed,
                    )
                    self.assertEqual(
                        report.cycle_rank_drop,
                        len(removed) - report.component_increase,
                    )
                    self.assertEqual(
                        report.before_cycle_rank,
                        contact_cycle_rank(num_vertices, edges),
                    )
                    self.assertEqual(
                        report.after_cycle_rank,
                        contact_cycle_rank(
                            num_vertices,
                            edges,
                            removed,
                        ),
                    )
                    self.assertEqual(
                        report.after_component_count,
                        contact_component_count(
                            num_vertices,
                            edges,
                            removed,
                        ),
                    )

    def test_selector_not_required_when_no_exhaustion_exists(self):
        spectrum = first_exhaustion_topology_spectrum(
            3,
            TRIANGLE,
            (0, 0, 0),
            (3, 3, 3),
            (0, 0, 0),
        )
        self.assertFalse(spectrum.topology_selector_is_required)
        self.assertIsNone(spectrum.simultaneous_bottleneck_removal)
        self.assertEqual(spectrum.single_bottleneck_removals, ())

    def test_validation(self):
        with self.assertRaises(ValueError):
            contact_removal_topology_report(
                2,
                ((0, 0),),
                (),
            )
        with self.assertRaises(ValueError):
            contact_removal_topology_report(
                2,
                ((0, 1),),
                (1,),
            )
        with self.assertRaises(ValueError):
            first_exhaustion_topology_spectrum(
                3,
                TRIANGLE,
                (0, 0),
                (1, 1),
                (1, 1),
            )


if __name__ == "__main__":
    unittest.main()
