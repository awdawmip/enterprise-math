import unittest

from enterprise_math.precision_integer_cone import (
    cone_separation_certificate_holds,
    functional_nonpositive_on_cone,
    generator_combination,
    integer_dot,
    r004_bell_integer_certificate_defect,
    r004_bell_separating_functional,
    r004_bell_target_word,
    r004_local_bell_generators,
)


class PrecisionIntegerConeTests(unittest.TestCase):
    def test_local_bell_atoms_obey_one_integer_dual_halfspace(self):
        generators = r004_local_bell_generators()
        functional = r004_bell_separating_functional()
        self.assertEqual(len(generators), 16)
        values = tuple(integer_dot(functional, generator) for generator in generators)
        self.assertEqual(set(values), {-4, 0})
        self.assertTrue(all(value <= 0 for value in values))

    def test_target_is_separated_by_integer_defect_sixteen(self):
        target = r004_bell_target_word()
        functional = r004_bell_separating_functional()
        self.assertEqual(target, (-12, -12, -16, 16, 20))
        self.assertEqual(integer_dot(functional, target), 16)
        self.assertEqual(r004_bell_integer_certificate_defect(), 16)
        self.assertTrue(
            cone_separation_certificate_holds(
                r004_local_bell_generators(), target, functional
            )
        )

    def test_nonnegative_integer_mixtures_preserve_generatorwise_inequality(self):
        generators = r004_local_bell_generators()
        functional = r004_bell_separating_functional()
        weight_families = (
            (1,) * 16,
            tuple(range(16)),
            tuple((index * index + 1) % 5 for index in range(16)),
        )
        for weights in weight_families:
            self.assertTrue(
                functional_nonpositive_on_cone(generators, weights, functional)
            )
            combined = generator_combination(generators, weights)
            self.assertLessEqual(integer_dot(functional, combined), 0)

    def test_invalid_words_fail_closed(self):
        with self.assertRaises(ValueError):
            integer_dot((1, 2), (1,))
        with self.assertRaises(ValueError):
            generator_combination(((1, 2),), (-1,))
        with self.assertRaises(ValueError):
            cone_separation_certificate_holds((), (1,), (1,))


if __name__ == "__main__":
    unittest.main()
