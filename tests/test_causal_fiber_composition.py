import unittest

from enterprise_math.causal_fiber_composition import (
    alternative_minimum,
    count_distributive_identity,
    count_observation,
    existence_observation,
    joint_additive_minimum,
    joint_product,
    minimum_cost,
    tagged_alternative,
)


class CausalFiberCompositionTests(unittest.TestCase):
    def test_counting_reads_alternative_as_addition(self):
        left = frozenset({"x", "y"})
        right = frozenset({"y", "z", "w"})
        alternative = tagged_alternative(left, right)
        self.assertEqual(count_observation(alternative), 5)
        self.assertEqual(
            count_observation(alternative),
            count_observation(left) + count_observation(right),
        )

    def test_counting_reads_joint_product_as_multiplication(self):
        left = frozenset({0, 1, 2})
        right = frozenset({"a", "b"})
        self.assertEqual(count_observation(joint_product(left, right)), 6)
        self.assertEqual(6, count_observation(left) * count_observation(right))

    def test_count_shadow_inherits_distributivity_from_fine_composition(self):
        self.assertTrue(
            count_distributive_identity(
                frozenset({0, 1}),
                frozenset({"a"}),
                frozenset({"b", "c"}),
            )
        )

    def test_existence_reads_alternative_and_product_as_boolean_operations(self):
        empty = frozenset()
        one = frozenset({"u"})
        two = frozenset({"v", "w"})
        self.assertEqual(
            existence_observation(tagged_alternative(empty, one)),
            existence_observation(empty) or existence_observation(one),
        )
        self.assertEqual(
            existence_observation(joint_product(one, two)),
            existence_observation(one) and existence_observation(two),
        )
        self.assertFalse(existence_observation(joint_product(empty, two)))

    def test_minimum_cost_reads_alternative_as_min_and_joint_as_plus(self):
        left = minimum_cost({"a": 7, "b": 3})
        right = minimum_cost({"c": 5, "d": 9})
        impossible = minimum_cost({})
        self.assertEqual(alternative_minimum(left, right), 3)
        self.assertEqual(joint_additive_minimum(left, right), 8)
        self.assertEqual(alternative_minimum(impossible, right), right)
        self.assertIsNone(joint_additive_minimum(impossible, right))

    def test_underlying_singleton_is_not_the_same_numeric_identity_in_every_shadow(self):
        singleton = frozenset({"unit"})
        self.assertEqual(count_observation(singleton), 1)
        # A zero-cost singleton is the neutral product object for additive cost,
        # but its minimum-cost shadow is numerically 0 rather than count-shadow 1.
        self.assertEqual(minimum_cost({"unit": 0}), 0)


if __name__ == "__main__":
    unittest.main()
