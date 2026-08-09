import unittest

from enterprise_math.engineering_collision import Body2D, exact_collision_pairs
from enterprise_math.multiscale_collapse import (
    EMPTY,
    FULL,
    PARTIAL,
    collapse_cell_relation,
    multiscale_common_collapse,
)


class MultiscaleCollapseTests(unittest.TestCase):
    def test_terminal_cells_are_never_partial(self):
        body = Body2D(0, -2, 3, 2)
        for x in range(-6, 3):
            for y in range(-1, 8):
                relation = collapse_cell_relation(body, x, y, 1)
                self.assertIn(relation, (EMPTY, FULL))

    def test_coarse_cell_distinguishes_full_partial_and_empty(self):
        body = Body2D(0, 4, 4, 4)  # target square [0,8] x [0,8]
        self.assertEqual(collapse_cell_relation(body, 0, 0, 4), FULL)
        self.assertEqual(collapse_cell_relation(body, 2, 2, 4), PARTIAL)
        self.assertEqual(collapse_cell_relation(body, 4, 4, 4), EMPTY)

    def test_multiscale_matches_exact_pairs_with_negative_coordinates(self):
        bodies = [
            Body2D(0, -17, -1, 1),
            Body2D(1, -16, 1, 1),
            Body2D(2, -9, 5, 2),
            Body2D(3, 0, 0, 0),
            Body2D(4, 3, 3, 3),
            Body2D(5, 19, -7, 1),
            Body2D(6, 20, -8, 2),
        ]
        report = multiscale_common_collapse(bodies, (32, 16, 8, 4, 2, 1))
        self.assertEqual(report.collision_pairs, exact_collision_pairs(bodies))
        self.assertEqual(
            report,
            multiscale_common_collapse(list(reversed(bodies)), (32, 16, 8, 4, 2, 1)),
        )

    def test_multiscale_exact_on_dense_small_integer_field(self):
        bodies = []
        body_id = 0
        for x in range(-6, 7, 3):
            for y in range(-6, 7, 3):
                bodies.append(Body2D(body_id, x, y, (body_id % 3)))
                body_id += 1
        report = multiscale_common_collapse(bodies, (16, 8, 4, 2, 1))
        self.assertEqual(report.collision_pairs, exact_collision_pairs(bodies))

    def test_large_target_domains_are_compressed_before_terminal_emission(self):
        bodies = []
        body_id = 0
        for y in range(5):
            for x in range(5):
                bodies.append(Body2D(body_id, 80 * x, 80 * y, 32))
                body_id += 1
        # Add one deliberate deep overlap.
        bodies.append(Body2D(body_id, 12, 12, 32))
        terminal_memberships = sum((2 * body.radius + 1) ** 2 for body in bodies)
        report = multiscale_common_collapse(
            bodies, (256, 128, 64, 32, 16, 8, 4, 2, 1)
        )
        self.assertEqual(report.collision_pairs, exact_collision_pairs(bodies))
        self.assertLess(report.emitted_memberships * 10, terminal_memberships)
        self.assertGreater(len(report.collision_pairs), 0)

    def test_unique_ids_are_required(self):
        bodies = [Body2D(0, 0, 0, 1), Body2D(0, 1, 1, 1)]
        with self.assertRaises(ValueError):
            multiscale_common_collapse(bodies, (4, 2, 1))


if __name__ == "__main__":
    unittest.main()
