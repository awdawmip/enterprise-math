import itertools
import unittest
from fractions import Fraction

from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    contact_coupling_gram,
    contact_incidence_matrix,
)
from enterprise_math.material_contact_network_rank_duality import (
    contact_rank_duality_report,
)


def exact_rank(matrix):
    rows = [list(map(Fraction, row)) for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    col_count = len(rows[0])
    pivot_row = 0
    for col in range(col_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if rows[row][col] != 0),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][col]
        rows[pivot_row] = [value / pivot_value for value in rows[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or rows[row][col] == 0:
                continue
            factor = rows[row][col]
            rows[row] = [
                value - factor * basis
                for value, basis in zip(rows[row], rows[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def score_map_matrix(state):
    incidence = contact_incidence_matrix(state)
    weights = state.body_scale_weights
    return tuple(
        tuple(
            incidence[body][edge] * weights[body]
            for body in range(len(state.masses))
        )
        for edge in range(len(state.contacts))
    )


class MaterialContactNetworkRankDualityTests(unittest.TestCase):
    def test_connected_tree_has_a3_n_minus_one_relative_rank_and_one_total_coordinate(self):
        state = ContactNetworkMomentum1D(
            masses=(2, 3, 5, 7),
            momenta=(4, -1, 2, 3),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, -1),
                ContactChannel1D(2, 3, 1),
            ),
        )
        report = contact_rank_duality_report(state)
        self.assertEqual(report.body_count, 4)
        self.assertEqual(report.component_count, 1)
        self.assertEqual(report.independent_relative_state_rank, 3)
        self.assertEqual(report.spanning_forest_edge_count, 3)
        self.assertEqual(report.component_total_coordinates_needed, 1)
        self.assertEqual(report.body_coordinate_balance, 4)
        self.assertEqual(report.contact_score_redundancy, 0)
        self.assertEqual(report.impulse_kernel_dimension, 0)

    def test_triangle_cycle_has_one_redundant_score_and_one_invisible_impulse_direction(self):
        state = ContactNetworkMomentum1D(
            masses=(2, 3, 5),
            momenta=(4, -1, 2),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
                ContactChannel1D(2, 0, 1),
            ),
        )
        report = contact_rank_duality_report(state)
        self.assertEqual(report.independent_relative_state_rank, 2)
        self.assertEqual(report.contact_score_redundancy, 1)
        self.assertEqual(report.impulse_kernel_dimension, 1)
        self.assertEqual(report.contact_coordinate_balance, 3)
        self.assertEqual(report.body_coordinate_balance, 3)

    def test_disconnected_forest_needs_one_total_per_component_for_full_body_state(self):
        state = ContactNetworkMomentum1D(
            masses=(2, 3, 5, 7),
            momenta=(4, -1, 2, 3),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(2, 3, -1),
            ),
        )
        report = contact_rank_duality_report(state)
        self.assertEqual(report.component_count, 2)
        self.assertEqual(report.independent_relative_state_rank, 2)
        self.assertEqual(report.component_total_coordinates_needed, 2)
        self.assertEqual(report.unresolved_component_offsets_with_global_total_only, 1)
        self.assertEqual(report.body_coordinate_balance, 4)
        self.assertEqual(report.contact_score_redundancy, 0)

    def test_rank_formulas_match_exact_rational_matrix_rank_on_all_four_body_simple_graphs(self):
        body_count = 4
        possible = tuple(itertools.combinations(range(body_count), 2))
        masses = (2, 3, 5, 7)
        for mask in range(1 << len(possible)):
            contacts = tuple(
                ContactChannel1D(
                    left,
                    right,
                    1 if edge_index % 2 == 0 else -1,
                )
                for edge_index, (left, right) in enumerate(possible)
                if mask & (1 << edge_index)
            )
            state = ContactNetworkMomentum1D(
                masses=masses,
                momenta=(1, -2, 3, -4),
                contacts=contacts,
            )
            report = contact_rank_duality_report(state)
            incidence_rank = exact_rank(contact_incidence_matrix(state))
            score_rank = exact_rank(score_map_matrix(state))
            gram_rank = exact_rank(contact_coupling_gram(state))
            self.assertEqual(incidence_rank, report.independent_relative_state_rank)
            self.assertEqual(score_rank, report.independent_relative_state_rank)
            self.assertEqual(gram_rank, report.independent_relative_state_rank)
            self.assertEqual(
                len(contacts) - gram_rank,
                report.impulse_kernel_dimension,
            )
            self.assertEqual(
                len(contacts) - score_rank,
                report.contact_score_redundancy,
            )

    def test_cycle_rank_is_simultaneously_score_redundancy_and_witness_nullity(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 1, 1, 1, 1),
            momenta=(0, 0, 0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
                ContactChannel1D(2, 0, 1),
                ContactChannel1D(2, 3, 1),
                ContactChannel1D(3, 4, 1),
                ContactChannel1D(4, 2, 1),
            ),
        )
        report = contact_rank_duality_report(state)
        self.assertEqual(report.component_count, 1)
        self.assertEqual(report.independent_relative_state_rank, 4)
        self.assertEqual(report.contact_score_redundancy, 2)
        self.assertEqual(report.impulse_kernel_dimension, 2)
        self.assertEqual(report.contact_coordinate_balance, 6)
        self.assertEqual(report.body_coordinate_balance, 5)

    def test_isolated_bodies_are_counted_as_components(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 2, 3),
            momenta=(0, 0, 0),
            contacts=(),
        )
        report = contact_rank_duality_report(state)
        self.assertEqual(report.component_count, 3)
        self.assertEqual(report.independent_relative_state_rank, 0)
        self.assertEqual(report.component_total_coordinates_needed, 3)
        self.assertEqual(report.unresolved_component_offsets_with_global_total_only, 2)
        self.assertEqual(report.contact_score_redundancy, 0)
        self.assertEqual(report.impulse_kernel_dimension, 0)
        self.assertEqual(report.body_coordinate_balance, 3)


if __name__ == "__main__":
    unittest.main()
