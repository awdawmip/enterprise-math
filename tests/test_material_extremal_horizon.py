import unittest
from itertools import combinations

from enterprise_math.engineering_collision import Body2D
from enterprise_math.material_extremal_horizon import (
    direct_remaining_bounds,
    reconstruct_bounds_after_removals,
    removal_safe_extremal_certificate,
)


class MaterialExtremalHorizonTests(unittest.TestCase):
    def test_h_plus_one_candidates_reconstruct_every_allowed_removal(self):
        bodies = (
            Body2D(0, -4, 1, 5),
            Body2D(1, -1, 2, 4),
            Body2D(2, 3, -2, 6),
            Body2D(3, 1, 0, 3),
            Body2D(4, 5, 1, 5),
            Body2D(5, 0, -4, 7),
        )
        for horizon in range(0, 4):
            certificate = removal_safe_extremal_certificate(bodies, horizon)
            self.assertEqual(len(certificate.candidates), 4 * (horizon + 1))
            for removed_count in range(horizon + 1):
                for removed in combinations(
                    [body.body_id for body in bodies], removed_count
                ):
                    self.assertEqual(
                        reconstruct_bounds_after_removals(certificate, removed),
                        direct_remaining_bounds(bodies, removed),
                    )

    def test_current_four_facet_state_is_not_one_deletion_future_sufficient(self):
        # Both families have the same current intersection [3,4] x [-2,2]
        # and the same current x-low witness body 0.  After deleting body 0,
        # the next x-low differs because the second order statistic differs.
        first = (
            Body2D(0, 5, 0, 2),   # x=[3,7], y=[-2,2]
            Body2D(1, 4, 0, 2),   # x=[2,6]
            Body2D(2, -1, 0, 5),  # x=[-6,4]
        )
        second = (
            Body2D(0, 5, 0, 2),   # same current max lower = 3
            Body2D(1, 3, 0, 2),   # x=[1,5], different second lower
            Body2D(2, -1, 0, 5),  # same current min upper = 4
        )
        self.assertEqual(direct_remaining_bounds(first, ()), (3, 4, -2, 2))
        self.assertEqual(direct_remaining_bounds(second, ()), (3, 4, -2, 2))
        self.assertEqual(direct_remaining_bounds(first, (0,)), (2, 4, -2, 2))
        self.assertEqual(direct_remaining_bounds(second, (0,)), (1, 4, -2, 2))

        first_h1 = removal_safe_extremal_certificate(first, 1)
        second_h1 = removal_safe_extremal_certificate(second, 1)
        self.assertNotEqual(first_h1, second_h1)
        self.assertEqual(
            reconstruct_bounds_after_removals(first_h1, (0,)),
            (2, 4, -2, 2),
        )
        self.assertEqual(
            reconstruct_bounds_after_removals(second_h1, (0,)),
            (1, 4, -2, 2),
        )

    def test_strictly_ordered_facets_expose_h_plus_one_worst_case_need(self):
        # x-low values are 0,1,2,3,4 while a large common upper/y body range
        # prevents other facets from obscuring the order-statistic point.
        bodies = tuple(
            Body2D(body_id, 10 + body_id, 0, 10)
            for body_id in range(5)
        )
        certificate = removal_safe_extremal_certificate(bodies, 2)
        x_low = sorted(
            (
                candidate
                for candidate in certificate.candidates
                if candidate.axis == "x" and candidate.side == "lo"
            ),
            key=lambda candidate: candidate.rank,
        )
        self.assertEqual([candidate.rank for candidate in x_low], [1, 2, 3])
        # Remove the first two x-low witnesses; the third retained record must
        # become the exact new maximum lower bound.
        removed = (x_low[0].body_id, x_low[1].body_id)
        reconstructed = reconstruct_bounds_after_removals(certificate, removed)
        direct = direct_remaining_bounds(bodies, removed)
        self.assertEqual(reconstructed, direct)
        self.assertEqual(reconstructed[0], x_low[2].value)

    def test_bounded_randomlike_family_matches_direct_oracle(self):
        bodies = []
        body_id = 0
        for x in (-3, 0, 4):
            for y in (-2, 1):
                for radius in (1, 3):
                    bodies.append(Body2D(body_id, x, y, radius))
                    body_id += 1
        horizon = 2
        certificate = removal_safe_extremal_certificate(bodies, horizon)
        ids = [body.body_id for body in bodies]
        for removed_count in range(horizon + 1):
            for removed in list(combinations(ids, removed_count))[::7]:
                self.assertEqual(
                    reconstruct_bounds_after_removals(certificate, removed),
                    direct_remaining_bounds(bodies, removed),
                )

    def test_invalid_horizon_or_removal_is_rejected(self):
        bodies = (Body2D(0, 0, 0, 1), Body2D(1, 1, 0, 1))
        with self.assertRaises(ValueError):
            removal_safe_extremal_certificate(bodies, -1)
        with self.assertRaises(ValueError):
            removal_safe_extremal_certificate(bodies, 2)
        certificate = removal_safe_extremal_certificate(bodies, 0)
        with self.assertRaises(ValueError):
            reconstruct_bounds_after_removals(certificate, (1,))
        with self.assertRaises(ValueError):
            reconstruct_bounds_after_removals(certificate, (99,))


if __name__ == "__main__":
    unittest.main()
