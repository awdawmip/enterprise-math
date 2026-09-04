from fractions import Fraction
import unittest

from enterprise_math.euler_cube_cover_ramanujan import (
    all_cube_codes,
    all_frame_states,
    bcc_return_count,
    bcc_return_count_dynamic,
    bcc_return_probability,
    central_parity_holonomy_code,
    cube_code,
    deck_partner,
    exhaustive_certificate,
    frame_cover_edges,
    half_pochhammer_ratio,
    iter_slice_paths,
    lift_slice_path,
    ramanujan_signature_half_coefficient,
    s4_fixed_holonomy_classes,
    standard_cube_edges,
    verify_path_transport,
)


class EulerCubeCoverRamanujanTests(unittest.TestCase):
    def test_frame_cover_is_the_cube(self) -> None:
        self.assertEqual(len(all_frame_states()), 8)
        self.assertEqual(len(all_cube_codes()), 8)
        self.assertEqual(frame_cover_edges(), standard_cube_edges())
        self.assertEqual(len(frame_cover_edges()), 12)
        for state in all_frame_states():
            code = cube_code(*state)
            partner = cube_code(*deck_partner(state))
            self.assertEqual(partner, tuple(-coordinate for coordinate in code))

    def test_triangles_lift_to_antipodes(self) -> None:
        from itertools import permutations

        for start, middle, end in permutations(range(4), 3):
            lifted = lift_slice_path((start, middle, end, start))
            self.assertEqual(lifted[-1], deck_partner(lifted[0]))
            self.assertEqual(
                cube_code(*lifted[-1]),
                tuple(-coordinate for coordinate in cube_code(*lifted[0])),
            )

    def test_all_paths_through_eight_edges_obey_endpoint_parity(self) -> None:
        checked = 0
        for edge_count in range(9):
            for path in iter_slice_paths(edge_count):
                verify_path_transport(path)
                checked += 1
        self.assertEqual(checked, 4 * sum(3**edge_count for edge_count in range(9)))

    def test_unique_nonzero_s4_fixed_curvature_class(self) -> None:
        self.assertEqual(
            s4_fixed_holonomy_classes(),
            frozenset(((0, 0, 0), (1, 1, 1))),
        )
        self.assertEqual(central_parity_holonomy_code(), (1, 1, 1))

    def test_bcc_return_count_and_hypergeometric_coefficient(self) -> None:
        for n in range(7):
            self.assertEqual(bcc_return_count_dynamic(n), bcc_return_count(n))
            self.assertEqual(
                bcc_return_probability(n),
                ramanujan_signature_half_coefficient(n),
            )
            from math import comb

            self.assertEqual(
                half_pochhammer_ratio(n),
                Fraction(comb(2 * n, n), 4**n),
            )

    def test_full_certificate(self) -> None:
        certificate = exhaustive_certificate(max_path_edges=8, max_return_n=5)
        self.assertEqual(certificate["frame_states"], 8)
        self.assertEqual(certificate["cube_edges"], 12)
        self.assertEqual(
            certificate["closed_path_rule"],
            "even -> identity; odd -> tangent half-turn",
        )
        self.assertEqual(certificate["unique_nonzero_s4_fixed_class"], (1, 1, 1))
        self.assertEqual(certificate["ramanujan_kernel"], "((1/2)_n/n!)^3")


if __name__ == "__main__":
    unittest.main()
