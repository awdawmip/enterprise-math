import itertools
import unittest
from fractions import Fraction

from enterprise_math.material_contact_network_cycle_kernel import (
    contact_cycle_rank,
    contact_graph_component_count,
    contact_graph_is_forest,
    contact_impulse_vectors_same_body_update,
    contact_impulse_vectors_same_score_update,
    contact_kernel_report,
    coupling_image,
    declared_cycle_circulation,
    incidence_image,
    verify_impulse_identifiability_equivalence,
    verify_incidence_coupling_kernel_equivalence,
)
from enterprise_math.material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    contact_coupling_gram,
    contact_incidence_matrix,
)


def exact_rank(matrix):
    rows = [list(map(Fraction, row)) for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    col_count = len(rows[0]) if rows else 0
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
                value - factor * pivot_value
                for value, pivot_value in zip(rows[row], rows[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


class MaterialContactNetworkCycleKernelTests(unittest.TestCase):
    def test_path_is_forest_and_triangle_has_one_cycle_dimension(self):
        path = ContactNetworkMomentum1D(
            masses=(1, 2, 3, 4),
            momenta=(0, 0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, -1),
                ContactChannel1D(2, 3, 1),
            ),
        )
        self.assertEqual(contact_graph_component_count(path), 1)
        self.assertEqual(contact_cycle_rank(path), 0)
        self.assertTrue(contact_graph_is_forest(path))
        self.assertTrue(verify_impulse_identifiability_equivalence(path))

        triangle_plus_isolate = ContactNetworkMomentum1D(
            masses=(2, 3, 5, 7),
            momenta=(0, 0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
                ContactChannel1D(2, 0, 1),
            ),
        )
        report = contact_kernel_report(triangle_plus_isolate)
        self.assertEqual(report.component_count, 2)
        self.assertEqual(report.cycle_rank, 1)
        self.assertFalse(report.contact_graph_is_forest)
        self.assertFalse(report.impulse_update_is_injective)

    def test_cycle_rank_equals_exact_incidence_and_gram_nullity_on_all_four_body_graphs(self):
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
                momenta=(0, 0, 0, 0),
                contacts=contacts,
            )
            incidence = contact_incidence_matrix(state)
            gram = contact_coupling_gram(state)
            edge_count = len(contacts)
            cycle_rank = contact_cycle_rank(state)
            self.assertEqual(edge_count - exact_rank(incidence), cycle_rank)
            self.assertEqual(edge_count - exact_rank(gram), cycle_rank)
            self.assertEqual(contact_graph_is_forest(state), cycle_rank == 0)

    def test_declared_triangle_circulation_is_exact_body_and_score_kernel_witness(self):
        state = ContactNetworkMomentum1D(
            masses=(2, 3, 5),
            momenta=(4, -1, 2),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
                ContactChannel1D(2, 0, 1),
            ),
        )
        circulation = declared_cycle_circulation(state, (0, 1, 2))
        self.assertEqual(circulation, (1, 1, 1))
        self.assertEqual(incidence_image(state, circulation), (0, 0, 0))
        self.assertEqual(coupling_image(state, circulation), (0, 0, 0))
        self.assertTrue(
            verify_incidence_coupling_kernel_equivalence(state, circulation)
        )
        self.assertTrue(
            contact_impulse_vectors_same_body_update(state, (0, 0, 0), circulation)
        )
        self.assertTrue(
            contact_impulse_vectors_same_score_update(state, (0, 0, 0), circulation)
        )

    def test_cycle_circulation_respects_arbitrary_contact_orientation_signs(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 2, 4, 8),
            momenta=(0, 0, 0, 0),
            contacts=(
                ContactChannel1D(1, 0, 1),
                ContactChannel1D(1, 2, -1),
                ContactChannel1D(3, 2, 1),
                ContactChannel1D(0, 3, -1),
            ),
        )
        circulation = declared_cycle_circulation(state, (0, 1, 2, 3))
        self.assertTrue(any(value != 0 for value in circulation))
        self.assertEqual(incidence_image(state, circulation), (0, 0, 0, 0))
        self.assertEqual(coupling_image(state, circulation), (0, 0, 0, 0))

    def test_forest_has_no_nonzero_small_integer_contact_kernel_vector(self):
        state = ContactNetworkMomentum1D(
            masses=(2, 3, 5, 7),
            momenta=(0, 0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, -1),
                ContactChannel1D(2, 3, 1),
            ),
        )
        self.assertTrue(contact_graph_is_forest(state))
        for vector in itertools.product(range(-2, 3), repeat=3):
            if not any(vector):
                continue
            self.assertFalse(
                verify_incidence_coupling_kernel_equivalence(state, vector)
            )

    def test_any_incidence_kernel_vector_is_also_exact_gram_kernel_vector(self):
        state = ContactNetworkMomentum1D(
            masses=(2, 3, 5, 7),
            momenta=(0, 0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
                ContactChannel1D(2, 0, 1),
                ContactChannel1D(2, 3, -1),
            ),
        )
        for vector in itertools.product(range(-2, 3), repeat=4):
            body_zero = all(value == 0 for value in incidence_image(state, vector))
            score_zero = all(value == 0 for value in coupling_image(state, vector))
            self.assertEqual(body_zero, score_zero)

    def test_invalid_cycle_and_edge_vectors_are_rejected(self):
        state = ContactNetworkMomentum1D(
            masses=(1, 1, 1),
            momenta=(0, 0, 0),
            contacts=(
                ContactChannel1D(0, 1, 1),
                ContactChannel1D(1, 2, 1),
            ),
        )
        with self.assertRaises(ValueError):
            declared_cycle_circulation(state, (0, 1))
        with self.assertRaises(ValueError):
            declared_cycle_circulation(state, (0, 1, 1))
        with self.assertRaises(ValueError):
            declared_cycle_circulation(state, (0, 1, 2))
        with self.assertRaises(ValueError):
            incidence_image(state, (1,))
        with self.assertRaises(ValueError):
            coupling_image(state, (True, 0))


if __name__ == "__main__":
    unittest.main()
