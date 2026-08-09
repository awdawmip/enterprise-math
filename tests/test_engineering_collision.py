import unittest

from enterprise_math.engineering_collision import (
    COLLIDES,
    SEPARATE,
    UNRESOLVED,
    Body2D,
    adaptive_collision,
    broad_phase_candidates,
    collision_certificate_at_scale,
    exact_collision,
    exact_collision_pairs,
    run_collision_engine,
    validate_refinement_schedule,
)


class EngineeringCollisionTests(unittest.TestCase):
    def test_terminal_certificate_equals_exact_collision(self):
        body_id = 0
        bodies = []
        for x in range(-3, 4):
            for y in range(-3, 4):
                for radius in range(2):
                    bodies.append(Body2D(body_id, x, y, radius))
                    body_id += 1
        for left in bodies:
            for right in bodies:
                if left.body_id >= right.body_id:
                    continue
                certificate = collision_certificate_at_scale(left, right, 1)
                self.assertNotEqual(certificate.status, UNRESOLVED)
                self.assertEqual(certificate.status == COLLIDES, exact_collision(left, right))
                self.assertEqual(certificate.lower_distance, certificate.upper_distance)

    def test_coarse_certificates_are_sound(self):
        body_id = 0
        bodies = []
        for x in range(-4, 5, 2):
            for y in range(-4, 5, 2):
                for radius in range(2):
                    bodies.append(Body2D(body_id, x, y, radius))
                    body_id += 1
        for cell_size in (8, 4, 2):
            for left in bodies:
                for right in bodies:
                    if left.body_id >= right.body_id:
                        continue
                    certificate = collision_certificate_at_scale(left, right, cell_size)
                    if certificate.status == COLLIDES:
                        self.assertTrue(exact_collision(left, right))
                    elif certificate.status == SEPARATE:
                        self.assertFalse(exact_collision(left, right))

    def test_adaptive_collision_matches_exact_on_negative_and_positive_coordinates(self):
        bodies = [
            Body2D(0, -17, -1, 1),
            Body2D(1, -16, 1, 1),
            Body2D(2, -9, 5, 2),
            Body2D(3, 0, 0, 0),
            Body2D(4, 3, 3, 3),
            Body2D(5, 19, -7, 1),
        ]
        schedule = (16, 8, 4, 2, 1)
        for left in bodies:
            for right in bodies:
                if left.body_id >= right.body_id:
                    continue
                decision = adaptive_collision(left, right, schedule)
                self.assertEqual(decision.collides, exact_collision(left, right))
                statuses = [step.status for step in decision.trace]
                self.assertNotEqual(statuses[-1], UNRESOLVED)
                self.assertTrue(all(status == UNRESOLVED for status in statuses[:-1]))

    def test_broad_phase_has_no_false_negative(self):
        bodies = [
            Body2D(i, (i % 7) * 5 - 13, (i // 7) * 4 - 9, i % 3)
            for i in range(35)
        ]
        candidates = set(broad_phase_candidates(bodies, 8))
        exact = set(exact_collision_pairs(bodies))
        self.assertTrue(exact.issubset(candidates))

    def test_engine_is_deterministic_and_avoids_most_terminal_checks(self):
        bodies = []
        body_id = 0
        # Regular sparse field: the broad phase creates local candidates but most
        # pairs can be rejected before terminal precision.
        for y in range(24):
            for x in range(24):
                bodies.append(Body2D(body_id, 9 * x + (y % 3), 9 * y + (x % 2), 1))
                body_id += 1
        # Add a few deliberate collisions so the report is not a no-hit toy case.
        for x, y in ((30, 30), (31, 31), (90, 45), (91, 46), (-8, -8), (-7, -7)):
            bodies.append(Body2D(body_id, x, y, 1))
            body_id += 1

        schedule = (32, 16, 8, 4, 2, 1)
        first = run_collision_engine(bodies, schedule)
        second = run_collision_engine(list(reversed(bodies)), schedule)
        self.assertEqual(first, second)
        self.assertEqual(first.collision_pairs, exact_collision_pairs(bodies))
        self.assertLess(first.candidate_pairs, first.possible_pairs // 10)
        self.assertGreater(first.candidate_pairs, 0)
        self.assertLess(first.terminal_checks, first.candidate_pairs // 2)

    def test_schedule_requires_aligned_finite_terminal_precision(self):
        self.assertEqual(validate_refinement_schedule((16, 4, 2, 1)), (16, 4, 2, 1))
        for invalid in ((), (8, 3, 1), (8, 4, 2), (1, 2, 1), (8, 8, 1)):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    validate_refinement_schedule(invalid)


if __name__ == "__main__":
    unittest.main()
