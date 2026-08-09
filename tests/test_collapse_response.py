import unittest

from enterprise_math.collapse_response import (
    anchored_pair_responses,
    apply_pair_response,
    balanced_pair_responses,
    l1_steps,
    minimal_pair_responses,
)
from enterprise_math.common_collapse import common_collapse_collision
from enterprise_math.engineering_collision import Body2D


def rotate_vector_90(vector):
    return (-vector[1], vector[0])


def rotate_body_90(body):
    return Body2D(body.body_id, -body.y, body.x, body.radius)


class CollapseResponseTests(unittest.TestCase):
    def test_every_minimum_work_response_separates_and_hits_lower_bound(self):
        examples = (
            (Body2D(0, 0, 0, 1), Body2D(1, 2, 0, 1)),
            (Body2D(0, 0, 0, 2), Body2D(1, 2, 1, 2)),
            (Body2D(0, 0, 0, 5), Body2D(1, 0, 0, 1)),
        )
        for left, right in examples:
            responses = minimal_pair_responses(left, right)
            self.assertTrue(responses)
            lower_bound = responses[0].total_steps
            for response in responses:
                self.assertEqual(response.total_steps, lower_bound)
                self.assertEqual(
                    (
                        response.right_delta[0] - response.left_delta[0],
                        response.right_delta[1] - response.left_delta[1],
                    ),
                    response.relative_delta,
                )
                self.assertEqual(
                    response.total_steps,
                    l1_steps(response.left_delta) + l1_steps(response.right_delta),
                )
                updated_left, updated_right = apply_pair_response(left, right, response)
                self.assertFalse(common_collapse_collision(updated_left, updated_right))

    def test_one_step_relative_correction_cannot_be_split_evenly(self):
        left = Body2D(0, -1, 0, 1)
        right = Body2D(1, 1, 0, 1)
        responses = balanced_pair_responses(left, right)
        self.assertEqual(len(responses), 2)
        allocations = {(response.left_delta, response.right_delta) for response in responses}
        self.assertEqual(
            allocations,
            {((0, 0), (1, 0)), ((-1, 0), (0, 0))},
        )
        self.assertTrue(all(response.max_body_steps == 1 for response in responses))

    def test_even_relative_correction_has_unique_balanced_allocation_when_direction_is_unique(self):
        left = Body2D(0, 0, 0, 1)
        right = Body2D(1, 1, 0, 1)
        responses = balanced_pair_responses(left, right)
        self.assertEqual(len(responses), 1)
        response = responses[0]
        self.assertEqual(response.relative_delta, (2, 0))
        self.assertEqual(response.left_delta, (-1, 0))
        self.assertEqual(response.right_delta, (1, 0))
        self.assertEqual(response.total_steps, 2)
        self.assertEqual(response.max_body_steps, 1)

    def test_exact_coincidence_exposes_geometry_only_symmetry_ambiguity(self):
        left = Body2D(0, 0, 0, 1)
        right = Body2D(1, 0, 0, 1)
        responses = balanced_pair_responses(left, right)
        self.assertEqual(len(responses), 8)
        self.assertTrue(all(response.relative_delta != (0, 0) for response in responses))
        self.assertEqual(
            {response.relative_delta for response in responses},
            {(-3, 0), (3, 0), (0, -3), (0, 3)},
        )

    def test_balanced_response_set_is_rotation_equivariant(self):
        left = Body2D(0, -2, 1, 3)
        right = Body2D(1, 0, 1, 1)
        original = balanced_pair_responses(left, right)
        rotated = balanced_pair_responses(rotate_body_90(left), rotate_body_90(right))
        expected = {
            (
                rotate_vector_90(response.left_delta),
                rotate_vector_90(response.right_delta),
                rotate_vector_90(response.relative_delta),
            )
            for response in original
        }
        actual = {
            (response.left_delta, response.right_delta, response.relative_delta)
            for response in rotated
        }
        self.assertEqual(actual, expected)

    def test_response_set_is_swap_equivariant_without_body_id_priority(self):
        left = Body2D(10, -2, 3, 4)
        right = Body2D(4, 1, 2, 1)
        forward = balanced_pair_responses(left, right)
        reverse = balanced_pair_responses(right, left)
        expected = {
            (
                response.right_delta,
                response.left_delta,
                (-response.relative_delta[0], -response.relative_delta[1]),
            )
            for response in forward
        }
        actual = {
            (response.left_delta, response.right_delta, response.relative_delta)
            for response in reverse
        }
        self.assertEqual(actual, expected)

    def test_explicit_anchor_reduces_allocation_freedom(self):
        left = Body2D(0, 0, 0, 1)
        right = Body2D(1, 1, 0, 1)
        left_fixed = anchored_pair_responses(left, right, fixed_body_id=0)
        right_fixed = anchored_pair_responses(left, right, fixed_body_id=1)
        self.assertEqual(len(left_fixed), 1)
        self.assertEqual(left_fixed[0].left_delta, (0, 0))
        self.assertEqual(left_fixed[0].right_delta, (2, 0))
        self.assertEqual(len(right_fixed), 1)
        self.assertEqual(right_fixed[0].left_delta, (-2, 0))
        self.assertEqual(right_fixed[0].right_delta, (0, 0))

    def test_separate_bodies_need_no_response(self):
        left = Body2D(0, 0, 0, 1)
        right = Body2D(1, 9, 0, 1)
        self.assertEqual(minimal_pair_responses(left, right), ())
        self.assertEqual(balanced_pair_responses(left, right), ())

    def test_response_orientation_is_explicit(self):
        left = Body2D(0, 0, 0, 1)
        right = Body2D(1, 1, 0, 1)
        response = balanced_pair_responses(left, right)[0]
        with self.assertRaises(ValueError):
            apply_pair_response(right, left, response)


if __name__ == "__main__":
    unittest.main()
