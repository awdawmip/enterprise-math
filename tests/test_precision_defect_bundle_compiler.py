import unittest

from enterprise_math.precision_defect_bundle_compiler import (
    common_coset_subgroup_mod,
    compose_relations,
    fiber_supports,
    support_relation,
    target_descends,
    translation_defect_hom_mod,
)


class DefectBundleCompilerTests(unittest.TestCase):
    def test_cubic_mod8_has_state_dependent_defect_bundle(self):
        states = range(8)
        coarse = lambda x: x % 4
        target = lambda x: (x ** 3) % 8
        supports = fiber_supports(states, coarse, target)
        self.assertEqual(supports[0], frozenset({0}))
        self.assertEqual(supports[1], frozenset({1, 5}))
        self.assertIsNone(common_coset_subgroup_mod(supports, 8))
        self.assertFalse(target_descends(states, coarse, target))

    def test_common_support_coset_does_not_imply_action_homogeneity(self):
        target = lambda x: ((x // 2) if x % 2 == 0 else -(x // 2)) % 3
        supports = fiber_supports(range(6), lambda x: x % 2, target)
        self.assertEqual(supports[0], frozenset({0, 1, 2}))
        self.assertEqual(supports[1], frozenset({0, 1, 2}))
        self.assertEqual(common_coset_subgroup_mod(supports, 3), frozenset({0, 1, 2}))
        self.assertIsNone(translation_defect_hom_mod(6, (0, 2, 4), target, 3))

    def test_linear_target_has_translation_defect_homomorphism(self):
        target = lambda x: (3 * x) % 8
        phi = translation_defect_hom_mod(8, (0, 4), target, 8)
        self.assertEqual(phi, {0: 0, 4: 4})

    def test_support_relation_composes_exactly(self):
        states = range(4)
        coarse = lambda x: x % 2
        target = lambda x: x
        R = support_relation(states, coarse, target)
        S = frozenset({(0, "a"), (1, "b"), (2, "a"), (3, "c")})
        composed = compose_relations(R, S)
        direct = frozenset((coarse(x), z) for x in states for y, z in S if y == target(x))
        self.assertEqual(composed, direct)

    def test_singletons_are_exact_function_descent(self):
        states = range(8)
        coarse = lambda x: x % 4
        target = lambda x: x % 4
        self.assertTrue(target_descends(states, coarse, target))


if __name__ == "__main__":
    unittest.main()
