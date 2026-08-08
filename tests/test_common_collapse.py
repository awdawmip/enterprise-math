import unittest

from enterprise_math.common_collapse import (
    common_collapse_collision,
    common_collapse_multiplicity,
    common_collapse_pairs,
    common_collapse_witness,
    iter_terminal_collapse_targets,
)
from enterprise_math.engineering_collision import Body2D, exact_collision, exact_collision_pairs


class CommonCollapseTests(unittest.TestCase):
    def test_common_collapse_is_exact_collision_on_small_domain(self):
        body_id = 0
        bodies = []
        for x in range(-3, 4):
            for y in range(-3, 4):
                for radius in range(3):
                    bodies.append(Body2D(body_id, x, y, radius))
                    body_id += 1
        for left_index, left in enumerate(bodies):
            for right in bodies[left_index + 1 :]:
                self.assertEqual(
                    common_collapse_collision(left, right),
                    exact_collision(left, right),
                )

    def test_multiplicity_equals_explicit_shared_target_count(self):
        left = Body2D(0, -2, 1, 3)
        right = Body2D(1, 1, 3, 2)
        left_targets = set(iter_terminal_collapse_targets(left))
        right_targets = set(iter_terminal_collapse_targets(right))
        shared = left_targets & right_targets
        self.assertEqual(common_collapse_multiplicity(left, right), len(shared))
        self.assertGreater(len(shared), 0)

    def test_witness_is_shared_and_deterministic(self):
        left = Body2D(0, -1, 0, 2)
        right = Body2D(1, 2, 1, 2)
        witness = common_collapse_witness(left, right)
        self.assertIsNotNone(witness)
        self.assertIn(witness, set(iter_terminal_collapse_targets(left)))
        self.assertIn(witness, set(iter_terminal_collapse_targets(right)))
        self.assertEqual(witness, common_collapse_witness(right, left))

    def test_no_shared_target_means_separate(self):
        left = Body2D(0, 0, 0, 1)
        right = Body2D(1, 4, 0, 1)
        self.assertEqual(common_collapse_multiplicity(left, right), 0)
        self.assertIsNone(common_collapse_witness(left, right))
        self.assertFalse(common_collapse_collision(left, right))

    def test_inverted_target_index_finds_exact_pairs(self):
        bodies = [
            Body2D(0, -8, -8, 1),
            Body2D(1, -7, -7, 1),
            Body2D(2, 0, 0, 0),
            Body2D(3, 8, 0, 2),
            Body2D(4, 11, 0, 1),
            Body2D(5, 30, 30, 3),
        ]
        self.assertEqual(common_collapse_pairs(bodies), exact_collision_pairs(bodies))
        self.assertEqual(
            common_collapse_pairs(list(reversed(bodies))),
            common_collapse_pairs(bodies),
        )

    def test_inverted_target_index_requires_unique_ids(self):
        with self.assertRaises(ValueError):
            common_collapse_pairs([Body2D(0, 0, 0, 1), Body2D(0, 1, 1, 1)])


if __name__ == "__main__":
    unittest.main()
