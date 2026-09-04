from __future__ import annotations

import unittest

from enterprise_math.euler_fcc_chirality import (
    ALL_ODD_FACES,
    ANTIBALANCED_EDGES,
    GLOBAL_FLIP,
    ZERO_EDGES,
    ZERO_FACES,
    ZERO_GAUGE,
    classify,
    cube_adjacent,
    cube_complement,
    cube_label,
    cube_vertices,
    deck_flip,
    edge_assignments,
    face_holonomy,
    face_parity,
    face_patterns,
    face_weight,
    gauge_action,
    gauge_equivalent,
    gauge_lift_state,
    gauge_orbit,
    gauges,
    globalizable,
    is_even_face_pattern,
    is_s4_fixed,
    representative_from_even_faces,
    s4_orbit,
    signed_slice_states,
    transition_cover_adjacent,
    trivializing_gauges,
    verify_accepted_antibalanced_signature,
    verify_antibalanced_cube_cover,
)


class EulerFccChiralityTests(unittest.TestCase):
    def test_face_holonomy_is_gauge_invariant_and_even(self) -> None:
        for edges in edge_assignments():
            holonomy = face_holonomy(edges)
            self.assertEqual(face_parity(holonomy), 0)
            for gauge in gauges():
                self.assertEqual(face_holonomy(gauge_action(edges, gauge)), holonomy)

    def test_gauge_kernel_is_exactly_global_flip(self) -> None:
        kernel = [
            gauge
            for gauge in gauges()
            if all(
                gauge_action(edges, gauge) == edges
                for edges in edge_assignments()
            )
        ]
        self.assertEqual(set(kernel), {ZERO_GAUGE, GLOBAL_FLIP})

    def test_eight_gauge_orbits_of_size_eight(self) -> None:
        unseen = set(edge_assignments())
        orbits = []
        while unseen:
            orbit = gauge_orbit(min(unseen))
            orbits.append(orbit)
            unseen.difference_update(orbit)
        self.assertEqual(len(orbits), 8)
        self.assertEqual({len(orbit) for orbit in orbits}, {8})
        self.assertEqual(
            {face_holonomy(next(iter(orbit))) for orbit in orbits},
            {
                pattern
                for pattern in face_patterns()
                if is_even_face_pattern(pattern)
            },
        )

    def test_face_holonomy_is_complete_gauge_invariant(self) -> None:
        all_edges = tuple(edge_assignments())
        for left in all_edges:
            for right in all_edges:
                self.assertEqual(
                    face_holonomy(left) == face_holonomy(right),
                    gauge_equivalent(left, right),
                )

    def test_every_even_pattern_has_canonical_star_representative(self) -> None:
        for pattern in face_patterns():
            if is_even_face_pattern(pattern):
                representative = representative_from_even_faces(pattern)
                self.assertEqual(face_holonomy(representative), pattern)
            else:
                with self.assertRaises(ValueError):
                    representative_from_even_faces(pattern)

    def test_global_signed_J_exists_exactly_for_flat_class(self) -> None:
        for edges in edge_assignments():
            self.assertEqual(
                globalizable(edges), face_holonomy(edges) == ZERO_FACES
            )
            gauges_to_zero = trivializing_gauges(edges)
            if globalizable(edges):
                self.assertEqual(len(gauges_to_zero), 2)
                self.assertEqual(
                    {
                        tuple(1 ^ bit for bit in gauge)
                        for gauge in gauges_to_zero
                    },
                    set(gauges_to_zero),
                )
            else:
                self.assertEqual(gauges_to_zero, ())

    def test_full_S4_orbit_classification(self) -> None:
        even_patterns = {
            pattern
            for pattern in face_patterns()
            if is_even_face_pattern(pattern)
        }
        remaining = set(even_patterns)
        orbits = []
        while remaining:
            orbit = s4_orbit(min(remaining))
            orbits.append(orbit)
            remaining.difference_update(orbit)
        self.assertEqual(sorted(len(orbit) for orbit in orbits), [1, 1, 6])
        self.assertEqual(
            sorted(
                {face_weight(pattern) for pattern in orbit}
                for orbit in orbits
            ),
            [{0}, {2}, {4}],
        )

    def test_only_flat_and_all_odd_are_fully_symmetric(self) -> None:
        fixed = {
            pattern
            for pattern in face_patterns()
            if is_even_face_pattern(pattern) and is_s4_fixed(pattern)
        }
        self.assertEqual(fixed, {ZERO_FACES, ALL_ODD_FACES})

    def test_accepted_all_negative_signature_is_unique_symmetric_obstruction(
        self,
    ) -> None:
        certificate = verify_accepted_antibalanced_signature()
        self.assertEqual(face_holonomy(ANTIBALANCED_EDGES), ALL_ODD_FACES)
        self.assertTrue(certificate["s4_fixed"])
        self.assertFalse(certificate["global_signed_J_exists"])
        self.assertFalse(gauge_equivalent(ANTIBALANCED_EDGES, ZERO_EDGES))

    def test_gauge_related_transition_covers_are_isomorphic(self) -> None:
        states = tuple(signed_slice_states())
        for edges in edge_assignments():
            for gauge in gauges():
                transformed_edges = gauge_action(edges, gauge)
                for left in states:
                    for right in states:
                        self.assertEqual(
                            transition_cover_adjacent(edges, left, right),
                            transition_cover_adjacent(
                                transformed_edges,
                                gauge_lift_state(left, gauge),
                                gauge_lift_state(right, gauge),
                            ),
                        )

    def test_antibalanced_orientation_cover_is_cube(self) -> None:
        states = tuple(signed_slice_states())
        labels = {state: cube_label(state) for state in states}
        self.assertEqual(set(labels.values()), set(cube_vertices()))
        for left in states:
            self.assertEqual(
                cube_label(deck_flip(left)), cube_complement(cube_label(left))
            )
            for right in states:
                self.assertEqual(
                    transition_cover_adjacent(ANTIBALANCED_EDGES, left, right),
                    cube_adjacent(cube_label(left), cube_label(right)),
                )

        certificate = verify_antibalanced_cube_cover()
        self.assertEqual(certificate["signed_slice_states"], 8)
        self.assertEqual(certificate["cover_edges"], 12)
        self.assertEqual(certificate["cube_vertices"], 8)
        self.assertEqual(certificate["cube_edges"], 12)
        self.assertEqual(certificate["body_diagonals"], 4)
        self.assertTrue(certificate["adjacency_isomorphism"])

    def test_exact_assignment_counts(self) -> None:
        report = classify()
        self.assertEqual(report.edge_assignments, 64)
        self.assertEqual(report.gauge_group_size, 16)
        self.assertEqual(report.gauge_kernel_size, 2)
        self.assertEqual(report.gauge_orbit_count, 8)
        self.assertEqual(report.gauge_orbit_sizes, (8,) * 8)
        self.assertEqual(
            dict(report.face_weight_class_counts), {0: 1, 2: 6, 4: 1}
        )
        self.assertEqual(report.s4_face_orbit_sizes, (1, 1, 6))
        self.assertEqual(
            report.s4_fixed_patterns, (ZERO_FACES, ALL_ODD_FACES)
        )
        self.assertEqual(report.flat_edge_assignments, 8)
        self.assertEqual(report.weight_two_edge_assignments, 48)
        self.assertEqual(report.all_odd_edge_assignments, 8)


if __name__ == "__main__":
    unittest.main()
