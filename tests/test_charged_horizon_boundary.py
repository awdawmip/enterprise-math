import unittest

from enterprise_math.charged_black_hole import (
    charged_discriminant,
    discriminant_is_square_fixed_point,
    horizon_boundary_complex,
    rescale_coefficients,
)


class ChargedHorizonBoundaryTests(unittest.TestCase):
    def test_subextremal_positive_charge_has_two_boundary_components(self):
        for a in range(1, 40):
            for b in range(1, 200):
                delta = charged_discriminant(a, b)
                if delta <= 0:
                    continue
                boundary = horizon_boundary_complex(a, b)
                components = len(boundary["vertices"]) + len(boundary["edges"])
                self.assertEqual(components, 2)
                if discriminant_is_square_fixed_point(a, b):
                    self.assertEqual(len(boundary["vertices"]), 2)
                    self.assertEqual(boundary["edges"], ())
                else:
                    self.assertEqual(boundary["vertices"], ())
                    self.assertEqual(len(boundary["edges"]), 2)

    def test_extremal_positive_charge_is_one_zero_vertex(self):
        for h in range(1, 40):
            a = 2 * h
            b = h * h
            boundary = horizon_boundary_complex(a, b)
            self.assertEqual(boundary["vertices"], (h,))
            self.assertEqual(boundary["edges"], ())

    def test_superextremal_has_no_boundary(self):
        for a in range(1, 30):
            for b in range(1, 150):
                if charged_discriminant(a, b) < 0:
                    self.assertEqual(
                        horizon_boundary_complex(a, b),
                        {"vertices": (), "edges": ()},
                    )

    def test_nonsquare_example_places_horizons_on_edges(self):
        self.assertEqual(charged_discriminant(5, 5), 5)
        self.assertEqual(
            horizon_boundary_complex(5, 5),
            {"vertices": (), "edges": ((1, 2), (3, 4))},
        )

    def test_uniform_scale_preserves_vertex_vs_edge_type(self):
        for a in range(1, 25):
            for b in range(1, 100):
                if charged_discriminant(a, b) <= 0:
                    continue
                original = horizon_boundary_complex(a, b)
                original_vertex_type = bool(original["vertices"])
                for scale in range(1, 6):
                    scaled_a, scaled_b = rescale_coefficients(scale, a, b)
                    scaled = horizon_boundary_complex(scaled_a, scaled_b)
                    self.assertEqual(bool(scaled["vertices"]), original_vertex_type)
                    self.assertEqual(
                        len(scaled["vertices"]) + len(scaled["edges"]),
                        2,
                    )


if __name__ == "__main__":
    unittest.main()
