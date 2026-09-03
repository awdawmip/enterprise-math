from __future__ import annotations

import unittest

from enterprise_math.euler_fcc_chiral_transport import (
    OPPOSITE_EDGE_PAIRS,
    all_edge_bits,
    all_faces_frustrated,
    chiral_quarter_turn_globalizes,
    connection_certificate,
    correction,
    edge_coboundary,
    edge_weight,
    exhaustive_audit,
    face_holonomy,
    face_phase_monodromy,
    face_weight,
    flat_part,
    gauge_transform,
    half_turn_endpoint_globalizes,
    is_even_face_pattern,
    is_flat,
    one_edge_mask,
    potential_for_flat,
    repair_candidates,
    repair_distance,
    root_defect,
    root_gauge_normal_form,
    signed_winding_globalizes,
    tree_flat_connection,
    two_edge_mask,
)


class EulerFccChiralTransportTests(unittest.TestCase):
    def test_complete_exhaustive_audit(self) -> None:
        report = exhaustive_audit()
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["connections"], 64)
        self.assertEqual(report["flat_connections"], 8)
        self.assertEqual(report["curvature_patterns"], 8)
        self.assertEqual(report["curvature_fiber_size"], 8)
        self.assertEqual(report["repair_distance_histogram"], {0: 8, 1: 48, 2: 8})

    def test_face_parity_and_root_normal_form(self) -> None:
        for connection in all_edge_bits():
            holonomy = face_holonomy(connection)
            self.assertTrue(is_even_face_pattern(holonomy))
            self.assertEqual(
                root_gauge_normal_form(connection),
                (0, 0, 0, holonomy[0], holonomy[1], holonomy[2]),
            )
            self.assertEqual(root_defect(connection), holonomy[:3])

    def test_flat_spanning_tree_extension(self) -> None:
        for a in (0, 1):
            for b in (0, 1):
                for c in (0, 1):
                    connection = tree_flat_connection(a, b, c)
                    self.assertTrue(is_flat(connection))
                    self.assertEqual(flat_part(connection), connection)
                    self.assertEqual(edge_coboundary(potential_for_flat(connection)), connection)

    def test_gauge_invariance_and_complete_classification(self) -> None:
        gauges = [
            (0, 0, 0, 0),
            (1, 0, 0, 0),
            (0, 1, 1, 0),
            (1, 1, 1, 1),
        ]
        for connection in all_edge_bits():
            for gauge in gauges:
                moved = gauge_transform(connection, gauge)
                self.assertEqual(face_holonomy(moved), face_holonomy(connection))
                self.assertEqual(root_defect(moved), root_defect(connection))

    def test_two_face_defect_has_unique_one_edge_repair(self) -> None:
        for connection in all_edge_bits():
            if face_weight(face_holonomy(connection)) == 2:
                repairs = repair_candidates(connection)
                self.assertEqual(len(repairs), 1)
                self.assertEqual(edge_weight(repairs[0]), 1)
                self.assertTrue(is_flat(correction(connection, repairs[0])))

    def test_fully_frustrated_requires_opposite_edge_pair(self) -> None:
        expected = {two_edge_mask(*pair) for pair in OPPOSITE_EDGE_PAIRS}
        for connection in all_edge_bits():
            if all_faces_frustrated(connection):
                repairs = repair_candidates(connection)
                self.assertEqual(repair_distance(connection), 2)
                self.assertEqual(set(repairs), expected)
                for edge in range(6):
                    self.assertFalse(is_flat(correction(connection, one_edge_mask(edge))))

    def test_half_turn_is_blind_but_quarter_turn_detects_obstruction(self) -> None:
        for connection in all_edge_bits():
            self.assertTrue(half_turn_endpoint_globalizes(connection))
            self.assertEqual(chiral_quarter_turn_globalizes(connection), is_flat(connection))
            self.assertEqual(signed_winding_globalizes(connection), is_flat(connection))
            for face in range(4):
                self.assertEqual(
                    face_phase_monodromy(connection, face, (-1, 0)),
                    (-1, 0),
                )
                quarter = face_phase_monodromy(connection, face, (0, 1))
                expected = (0, -1) if face_holonomy(connection)[face] else (0, 1)
                self.assertEqual(quarter, expected)

    def test_certificate_exposes_only_three_independent_defect_bits(self) -> None:
        connection = (1, 0, 1, 1, 0, 1)
        certificate = connection_certificate(connection)
        h = certificate.holonomy
        self.assertEqual(h[3], h[0] ^ h[1] ^ h[2])
        self.assertEqual(certificate.root_normal_form, (0, 0, 0, *certificate.root_defect))


if __name__ == "__main__":
    unittest.main()
