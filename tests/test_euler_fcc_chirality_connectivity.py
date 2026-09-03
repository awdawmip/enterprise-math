from __future__ import annotations

import unittest

from enterprise_math.euler_fcc_chirality import (
    ALL_ODD_FACES,
    ANTIBALANCED_EDGES,
    ZERO_EDGES,
    edge_assignments,
    face_holonomy,
    gauge_action,
    gauges,
    globalizable,
    is_s4_fixed,
    signed_slice_states,
    transition_cover_adjacent,
)
from enterprise_math.euler_fcc_chirality_connectivity import (
    cover_components,
    cover_connected,
    cover_diameter,
    cover_neighbors,
    gauge_cover_relabel,
    verify_connectivity_classification,
)


class EulerFccChiralityConnectivityTests(unittest.TestCase):
    def test_each_signed_state_has_three_neighbors(self) -> None:
        for edges in edge_assignments():
            for state in signed_slice_states():
                self.assertEqual(len(cover_neighbors(edges, state)), 3)

    def test_cover_is_connected_exactly_when_holonomy_is_nonflat(self) -> None:
        for edges in edge_assignments():
            self.assertEqual(cover_connected(edges), not globalizable(edges))
            component_sizes = tuple(
                sorted(len(component) for component in cover_components(edges))
            )
            self.assertEqual(
                component_sizes,
                (4, 4) if globalizable(edges) else (8,),
            )

    def test_gauge_action_is_sheet_relabeling_upstairs(self) -> None:
        states = tuple(signed_slice_states())
        for edges in edge_assignments():
            for gauge in gauges():
                transformed = gauge_action(edges, gauge)
                for left in states:
                    for right in states:
                        self.assertEqual(
                            transition_cover_adjacent(edges, left, right),
                            transition_cover_adjacent(
                                transformed,
                                gauge_cover_relabel(left, gauge),
                                gauge_cover_relabel(right, gauge),
                            ),
                        )

    def test_flat_cover_is_two_tetrahedra(self) -> None:
        components = cover_components(ZERO_EDGES)
        self.assertEqual(tuple(sorted(map(len, components))), (4, 4))
        for component in components:
            for left in component:
                for right in component:
                    if left != right:
                        self.assertTrue(
                            transition_cover_adjacent(ZERO_EDGES, left, right)
                        )

    def test_antibalanced_cover_is_connected_cube(self) -> None:
        self.assertTrue(cover_connected(ANTIBALANCED_EDGES))
        self.assertEqual(cover_diameter(ANTIBALANCED_EDGES), 3)
        self.assertEqual(
            tuple(sorted(map(len, cover_components(ANTIBALANCED_EDGES)))),
            (8,),
        )

    def test_full_symmetry_plus_connectivity_selects_all_odd(self) -> None:
        for edges in edge_assignments():
            if is_s4_fixed(face_holonomy(edges)) and cover_connected(edges):
                self.assertEqual(face_holonomy(edges), ALL_ODD_FACES)

    def test_connectivity_certificate(self) -> None:
        certificate = verify_connectivity_classification()
        self.assertEqual(certificate["edge_assignments_checked"], 64)
        self.assertEqual(certificate["flat_disconnected_assignments"], 8)
        self.assertEqual(certificate["nonflat_connected_assignments"], 56)
        self.assertEqual(certificate["fully_symmetric_assignments"], 16)
        self.assertEqual(certificate["connected_fully_symmetric_assignments"], 8)
        self.assertEqual(certificate["antibalanced_diameter"], 3)


if __name__ == "__main__":
    unittest.main()
