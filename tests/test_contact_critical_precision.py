import unittest

from enterprise_math.contact_critical_precision import (
    contact_critical_precision_report,
)


def incidence(body_count, edges):
    rows = [[0] * len(edges) for _ in range(body_count)]
    for edge, (source, target) in enumerate(edges):
        rows[source][edge] = -1
        rows[target][edge] = 1
    return tuple(tuple(row) for row in rows)


def cycle_incidence(size):
    return incidence(
        size,
        tuple((index, (index + 1) % size) for index in range(size)),
    )


class ContactCriticalPrecisionTests(unittest.TestCase):
    def test_tree_has_trivial_critical_precision_for_every_unit_edge(self):
        for body_count in range(2, 8):
            graph = incidence(
                body_count,
                tuple((index, index + 1) for index in range(body_count - 1)),
            )
            for edge in range(body_count - 1):
                history = tuple(
                    1 if index == edge else 0
                    for index in range(body_count - 1)
                )
                report = contact_critical_precision_report(
                    graph,
                    history,
                )
                self.assertEqual(report.spanning_tree_count, 1)
                self.assertEqual(report.critical_class_order, 1)
                self.assertTrue(report.integer_potential_representative_exists)
                self.assertFalse(report.requires_precision_refinement)
                self.assertEqual(
                    report.cycle_numerators,
                    (0,) * (body_count - 1),
                )

    def test_cycle_unit_edge_requires_denominator_equal_cycle_length(self):
        for size in range(3, 10):
            graph = cycle_incidence(size)
            history = (1,) + (0,) * (size - 1)
            report = contact_critical_precision_report(
                graph,
                history,
            )
            self.assertEqual(report.spanning_tree_count, size)
            self.assertEqual(report.critical_class_order, size)
            self.assertEqual(report.potential_denominator, size)
            self.assertEqual(
                report.cut_numerators,
                (size - 1,) + (-1,) * (size - 1),
            )
            self.assertEqual(
                report.cycle_numerators,
                (1,) * size,
            )
            self.assertTrue(report.requires_precision_refinement)

    def test_triangle_unit_edge_has_exact_third_resolution_decomposition(self):
        graph = cycle_incidence(3)
        report = contact_critical_precision_report(
            graph,
            (1, 0, 0),
        )
        self.assertEqual(report.body_delta, (-1, 1, 0))
        self.assertEqual(report.potential_numerators, (-1, 1, 0))
        self.assertEqual(report.potential_denominator, 3)
        self.assertEqual(report.cut_numerators, (2, -1, -1))
        self.assertEqual(report.cycle_numerators, (1, 1, 1))

    def test_pure_cycle_history_has_no_critical_torsion_but_keeps_cycle_memory(self):
        graph = cycle_incidence(3)
        report = contact_critical_precision_report(
            graph,
            (1, 1, 1),
        )
        self.assertEqual(report.body_delta, (0, 0, 0))
        self.assertEqual(report.critical_class_order, 1)
        self.assertEqual(report.potential_numerators, (0, 0, 0))
        self.assertEqual(report.cut_numerators, (0, 0, 0))
        self.assertEqual(report.cycle_numerators, (1, 1, 1))

    def test_critical_class_depends_only_on_body_delta_not_cycle_representative(self):
        graph = cycle_incidence(3)
        first = contact_critical_precision_report(
            graph,
            (1, 0, 0),
        )
        second = contact_critical_precision_report(
            graph,
            (2, 1, 1),
        )
        self.assertEqual(first.body_delta, second.body_delta)
        self.assertEqual(
            first.critical_class_order,
            second.critical_class_order,
        )
        self.assertEqual(
            first.potential_numerators,
            second.potential_numerators,
        )
        self.assertEqual(
            first.cut_numerators,
            second.cut_numerators,
        )
        self.assertNotEqual(
            first.cycle_numerators,
            second.cycle_numerators,
        )
        self.assertEqual(
            tuple(
                right - left
                for left, right in zip(
                    first.cycle_numerators,
                    second.cycle_numerators,
                    strict=True,
                )
            ),
            (3, 3, 3),
        )

    def test_root_choice_does_not_change_critical_order(self):
        graphs = (
            cycle_incidence(5),
            incidence(
                4,
                (
                    (0, 1),
                    (1, 2),
                    (2, 3),
                    (3, 0),
                    (0, 2),
                ),
            ),
        )
        histories = (
            (1, -1, 2, 0, 1),
            (1, 0, -1, 2, 1),
        )
        for graph, history in zip(graphs, histories, strict=True):
            orders = {
                contact_critical_precision_report(
                    graph,
                    history,
                    root=root,
                ).critical_class_order
                for root in range(len(graph))
            }
            self.assertEqual(len(orders), 1)

    def test_class_order_divides_spanning_tree_count_on_dense_graph(self):
        graph = incidence(
            4,
            (
                (0, 1),
                (0, 2),
                (0, 3),
                (1, 2),
                (1, 3),
                (2, 3),
            ),
        )
        for edge in range(6):
            history = tuple(
                1 if index == edge else 0
                for index in range(6)
            )
            report = contact_critical_precision_report(
                graph,
                history,
            )
            self.assertEqual(report.spanning_tree_count, 16)
            self.assertEqual(report.critical_class_order, 4)
            self.assertEqual(
                report.spanning_tree_count
                % report.critical_class_order,
                0,
            )

    def test_validation(self):
        disconnected = incidence(
            4,
            ((0, 1), (2, 3)),
        )
        with self.assertRaises(ValueError):
            contact_critical_precision_report(
                disconnected,
                (1, 0),
            )
        with self.assertRaises(ValueError):
            contact_critical_precision_report(
                cycle_incidence(3),
                (1, 0),
            )
        with self.assertRaises(ValueError):
            contact_critical_precision_report(
                cycle_incidence(3),
                (1, 0, 0),
                root=3,
            )
        with self.assertRaises(TypeError):
            contact_critical_precision_report(
                cycle_incidence(3),
                (1, True, 0),
            )


if __name__ == "__main__":
    unittest.main()
