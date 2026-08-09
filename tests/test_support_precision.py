import unittest

from enterprise_math.precision_system import FALSE, TRUE, UNRESOLVED
from enterprise_math.support_precision import (
    EMPTY,
    FULL,
    PARTIAL,
    support_abstraction,
    support_block_statuses,
    support_overlap_certificate,
    support_overlap_certificate_profile,
    support_refinement_consistency,
)


def cell_observation(cell_size):
    return lambda point: (point[0] // cell_size, point[1] // cell_size)


class SupportPrecisionTests(unittest.TestCase):
    def setUp(self):
        self.states = [
            (x, y)
            for x in range(-6, 7)
            for y in range(-6, 7)
        ]
        self.identity = lambda point: point

    def square_support(self, center_x, center_y, radius):
        return frozenset(
            point
            for point in self.states
            if max(abs(point[0] - center_x), abs(point[1] - center_y)) <= radius
        )

    def test_block_statuses_have_three_exact_states(self):
        support = self.square_support(0, 0, 4)
        observation = cell_observation(4)
        statuses = support_block_statuses(self.states, observation, support)
        abstraction = support_abstraction(self.states, observation, support)
        self.assertIn(EMPTY, statuses.values())
        self.assertIn(FULL, statuses.values())
        self.assertIn(PARTIAL, statuses.values())
        self.assertEqual(
            abstraction.may_blocks,
            frozenset(key for key, status in statuses.items() if status != EMPTY),
        )
        self.assertEqual(
            abstraction.must_blocks,
            frozenset(key for key, status in statuses.items() if status == FULL),
        )
        self.assertTrue(abstraction.must_blocks.issubset(abstraction.may_blocks))

    def test_terminal_identity_decides_exact_support_intersection(self):
        supports = [
            self.square_support(-3, 0, 2),
            self.square_support(0, 0, 2),
            self.square_support(5, 0, 1),
        ]
        for left_index, left in enumerate(supports):
            for right in supports[left_index + 1 :]:
                certificate = support_overlap_certificate(
                    self.states, self.identity, left, right
                )
                expected = TRUE if left.intersection(right) else FALSE
                self.assertEqual(certificate, expected)

    def test_coarse_partial_overlap_refines_to_exact_answer(self):
        left = self.square_support(1, 0, 1)
        right = self.square_support(4, 0, 1)
        observations = [
            cell_observation(8),
            cell_observation(4),
            cell_observation(2),
            self.identity,
        ]
        profile = support_overlap_certificate_profile(
            self.states, observations, left, right
        )
        self.assertEqual(profile[-1], FALSE)
        self.assertIn(UNRESOLVED, profile[:-1])

    def test_true_certificate_persists_under_refinement(self):
        left = self.square_support(-1, 0, 2)
        right = self.square_support(1, 0, 2)
        observations = [cell_observation(4), cell_observation(2), self.identity]
        profile = support_overlap_certificate_profile(
            self.states, observations, left, right
        )
        first_decided = next(
            index for index, status in enumerate(profile) if status != UNRESOLVED
        )
        self.assertEqual(profile[first_decided], TRUE)
        self.assertTrue(all(status == TRUE for status in profile[first_decided:]))

    def test_refinement_preserves_exact_may_coverage_and_must_evidence(self):
        support = self.square_support(0, 0, 4)
        coarse = cell_observation(4)
        fine = cell_observation(2)
        data = support_refinement_consistency(self.states, coarse, fine, support)
        self.assertEqual(
            data["projected_fine_may"], data["coarse"].may_blocks
        )
        self.assertTrue(
            data["coarse"].must_blocks.issubset(data["projected_fine_must"])
        )

    def test_identity_abstraction_is_exact_support(self):
        support = self.square_support(-1, 2, 2)
        abstraction = support_abstraction(self.states, self.identity, support)
        self.assertEqual(abstraction.may_blocks, support)
        self.assertEqual(abstraction.must_blocks, support)

    def test_support_must_lie_inside_terminal_state_set(self):
        with self.assertRaises(ValueError):
            support_block_statuses(
                self.states,
                self.identity,
                frozenset({(999, 999)}),
            )


if __name__ == "__main__":
    unittest.main()
