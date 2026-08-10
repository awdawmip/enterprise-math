import unittest

from enterprise_math.causal_quadratic_interaction import (
    cross_pair_interaction,
    merge_quadratic_identity,
    pythagorean_shadow_holds,
    quadratic_interaction_response,
)


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def add_word(word):
    return tuple(sum(vector[i] for vector in word) for i in range(len(word[0])))


class CausalQuadraticInteractionTests(unittest.TestCase):
    def test_a3_root_word_quadratic_response_matches_coordinate_square_audit(self):
        roots = (
            (1, -1, 0, 0),
            (0, 1, -1, 0),
            (0, 0, 1, -1),
            (1, 0, -1, 0),
        )
        for word in (roots[:1], roots[:2], roots[:3], roots):
            net = add_word(word)
            response = quadratic_interaction_response(word, 2, dot)
            self.assertEqual(response, sum(value * value for value in net))

    def test_pythagorean_shadow_is_zero_cross_interaction_not_hidden_angle_axiom(self):
        left = ((1, -1, 0, 0),)
        right = ((0, 0, 1, -1),)
        self.assertEqual(cross_pair_interaction(left, right, dot), 0)
        self.assertTrue(pythagorean_shadow_holds(left, right, 2, dot))

    def test_nonzero_cross_relation_produces_exact_quadratic_defect(self):
        left = ((1, -1, 0, 0),)
        right = ((1, 0, -1, 0),)
        self.assertEqual(cross_pair_interaction(left, right, dot), 1)
        self.assertTrue(merge_quadratic_identity(left, right, 2, dot))
        self.assertFalse(pythagorean_shadow_holds(left, right, 2, dot))
        self.assertEqual(
            quadratic_interaction_response(left + right, 2, dot)
            - quadratic_interaction_response(left, 2, dot)
            - quadratic_interaction_response(right, 2, dot),
            2,
        )


if __name__ == "__main__":
    unittest.main()
