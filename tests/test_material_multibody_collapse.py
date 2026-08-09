import unittest
from itertools import combinations

from enterprise_math.engineering_collision import Body2D
from enterprise_math.material_multibody_collapse import (
    box_helly_equivalence,
    multibody_common_collapse_profile,
    multibody_extremal_certificate,
    pairwise_common_collapse_clique,
    pairwise_common_multiplicity_signature,
    reconstruct_common_bounds_from_certificate,
)


class MaterialMultiBodyCollapseTests(unittest.TestCase):
    def test_pairwise_clique_implies_one_shared_target_for_square_supports(self):
        bodies = (
            Body2D(0, 0, 0, 1),
            Body2D(1, 1, 0, 1),
            Body2D(2, 2, 0, 1),
        )
        self.assertTrue(pairwise_common_collapse_clique(bodies))
        self.assertTrue(box_helly_equivalence(bodies))
        profile = multibody_common_collapse_profile(bodies)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.bounds, (1, 1, -1, 1))
        self.assertEqual(profile.target_count, 3)
        self.assertEqual(profile.witness, (1, -1))

    def test_same_complete_pair_graph_does_not_determine_common_target_multiplicity(self):
        narrow = (
            Body2D(0, 0, 0, 1),
            Body2D(1, 1, 0, 1),
            Body2D(2, 2, 0, 1),
        )
        wide = (
            Body2D(0, 0, 0, 2),
            Body2D(1, 1, 0, 2),
            Body2D(2, 2, 0, 2),
        )
        self.assertTrue(pairwise_common_collapse_clique(narrow))
        self.assertTrue(pairwise_common_collapse_clique(wide))
        narrow_profile = multibody_common_collapse_profile(narrow)
        wide_profile = multibody_common_collapse_profile(wide)
        self.assertEqual(narrow_profile.target_count, 3)
        self.assertEqual(wide_profile.target_count, 15)
        self.assertNotEqual(narrow_profile.bounds, wide_profile.bounds)

    def test_even_complete_pairwise_multiplicities_do_not_determine_triple_multiplicity(self):
        first = (
            Body2D(0, -2, -2, 1),
            Body2D(1, -2, -1, 1),
            Body2D(2, -1, 0, 2),
        )
        second = (
            Body2D(0, -2, -2, 1),
            Body2D(1, -2, 0, 2),
            Body2D(2, 0, -2, 2),
        )
        first_pair = pairwise_common_multiplicity_signature(first)
        second_pair = pairwise_common_multiplicity_signature(second)
        self.assertEqual(
            tuple(value for _left, _right, value in first_pair),
            (6, 6, 9),
        )
        self.assertEqual(
            tuple(value for _left, _right, value in second_pair),
            (6, 6, 9),
        )
        first_profile = multibody_common_collapse_profile(first)
        second_profile = multibody_common_collapse_profile(second)
        self.assertEqual(first_profile.target_count, 6)
        self.assertEqual(second_profile.target_count, 4)

    def test_extremal_facets_reconstruct_whole_common_box_with_at_most_four_witness_bodies(self):
        bodies = (
            Body2D(9, -4, 0, 5),
            Body2D(2, 1, 2, 4),
            Body2D(7, 0, -3, 6),
            Body2D(5, 2, 0, 5),
            Body2D(1, -1, 1, 7),
            Body2D(12, 0, 3, 6),
        )
        profile = multibody_common_collapse_profile(bodies)
        self.assertIsNotNone(profile)
        certificate = multibody_extremal_certificate(bodies)
        self.assertIsNotNone(certificate)
        self.assertEqual(
            reconstruct_common_bounds_from_certificate(certificate),
            profile.bounds,
        )
        self.assertEqual(certificate.bounds, profile.bounds)
        self.assertEqual(len(certificate.facets), 4)
        self.assertLessEqual(len(certificate.unique_witness_body_ids), 4)
        self.assertTrue(
            set(certificate.unique_witness_body_ids).issubset(profile.body_ids)
        )

    def test_extremal_certificate_is_deterministic_under_tied_facets(self):
        bodies = (
            Body2D(8, 0, 0, 2),
            Body2D(3, 0, 0, 2),
            Body2D(5, 1, 0, 3),
        )
        certificate = multibody_extremal_certificate(bodies)
        reverse = multibody_extremal_certificate(tuple(reversed(bodies)))
        self.assertEqual(certificate, reverse)
        # Tied extreme facets select the smallest body id deterministically.
        for facet in certificate.facets:
            tied_ids = [
                body.body_id
                for body in bodies
                if facet.value
                in (
                    body.x - body.radius,
                    body.x + body.radius,
                    body.y - body.radius,
                    body.y + body.radius,
                )
            ]
            self.assertIn(facet.body_id, tied_ids)

    def test_nonclique_has_no_whole_family_common_target(self):
        bodies = (
            Body2D(0, 0, 0, 1),
            Body2D(1, 1, 0, 1),
            Body2D(2, 6, 0, 1),
        )
        self.assertFalse(pairwise_common_collapse_clique(bodies))
        self.assertTrue(box_helly_equivalence(bodies))
        self.assertIsNone(multibody_common_collapse_profile(bodies))
        self.assertIsNone(multibody_extremal_certificate(bodies))

    def test_bounded_three_body_family_never_breaks_box_helly_equivalence(self):
        library = []
        body_id = 0
        for x in range(-2, 3):
            for y in range(-1, 2):
                for radius in range(2):
                    library.append(Body2D(body_id, x, y, radius))
                    body_id += 1
        # Use a deterministic sparse subset of triples while preserving a mix
        # of radii/positions.  The theorem itself is coordinatewise interval
        # Helly; this regression is a counterexample search, not its proof.
        for indices in list(combinations(range(len(library)), 3))[::29]:
            bodies = tuple(library[index] for index in indices)
            self.assertTrue(box_helly_equivalence(bodies), bodies)
            profile = multibody_common_collapse_profile(bodies)
            self.assertEqual(profile is not None, pairwise_common_collapse_clique(bodies))
            certificate = multibody_extremal_certificate(bodies)
            self.assertEqual(certificate is not None, profile is not None)
            if profile is not None:
                self.assertEqual(certificate.bounds, profile.bounds)

    def test_common_profile_is_input_order_invariant(self):
        bodies = (
            Body2D(10, -1, 2, 2),
            Body2D(3, 0, 1, 2),
            Body2D(7, 1, 2, 2),
        )
        forward = multibody_common_collapse_profile(bodies)
        reverse = multibody_common_collapse_profile(tuple(reversed(bodies)))
        self.assertEqual(forward, reverse)
        self.assertEqual(forward.body_ids, (3, 7, 10))

    def test_duplicate_ids_or_singleton_are_rejected(self):
        with self.assertRaises(ValueError):
            multibody_common_collapse_profile((Body2D(0, 0, 0, 1),))
        with self.assertRaises(ValueError):
            multibody_common_collapse_profile(
                (Body2D(0, 0, 0, 1), Body2D(0, 1, 0, 1))
            )


if __name__ == "__main__":
    unittest.main()
