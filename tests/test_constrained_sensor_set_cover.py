import itertools
import unittest

from enterprise_math.constrained_sensor_set_cover import (
    element_reflected_by_sensor,
    encode_set_cover_as_modular_sensors,
    first_primes,
    minimum_sensor_cardinality_equals_set_cover,
    minimum_sensor_cover_exact,
    minimum_set_cover_exact,
    minimum_weight_sensor_cover_exact,
    minimum_weight_set_cover_exact,
    reduction_equivalence_holds,
    selected_sensors_reflect_all_codebooks,
    selected_sets_cover,
    weighted_reduction_equivalence_holds,
)


class ConstrainedSensorSetCoverTests(unittest.TestCase):
    def test_first_primes(self):
        self.assertEqual(first_primes(0), ())
        self.assertEqual(first_primes(5), (2, 3, 5, 7, 11))

    def test_named_three_set_cover_encoding(self):
        universe = ("a", "b", "c")
        sets = {
            "S1": {"a", "b"},
            "S2": {"b", "c"},
            "S3": {"c"},
        }
        encoding = encode_set_cover_as_modular_sensors(universe, sets)
        self.assertEqual(encoding.sensor_primes, {"S1": 2, "S2": 3, "S3": 5})

        # a is not covered by S2/S3, so d_a=3*5=15.
        self.assertEqual(encoding.contextual_codebooks["a"], frozenset({0, 15}))
        # b is not covered only by S3, so d_b=5.
        self.assertEqual(encoding.contextual_codebooks["b"], frozenset({0, 5}))
        # c is not covered only by S1, so d_c=2.
        self.assertEqual(encoding.contextual_codebooks["c"], frozenset({0, 2}))

        for element in universe:
            for sensor in sets:
                self.assertEqual(
                    element_reflected_by_sensor(encoding, element, sensor),
                    element in sets[sensor],
                )

        for size in range(4):
            for selected in itertools.combinations(tuple(sets), size):
                self.assertEqual(
                    selected_sets_cover(encoding, selected),
                    selected_sensors_reflect_all_codebooks(encoding, selected),
                )
                self.assertEqual(
                    reduction_equivalence_holds(encoding, selected),
                    selected_sets_cover(encoding, selected),
                )

        sensor_min = minimum_sensor_cover_exact(encoding)
        cover_min = minimum_set_cover_exact(encoding)
        self.assertEqual(len(sensor_min), 2)
        self.assertEqual(len(cover_min), 2)
        self.assertTrue(minimum_sensor_cardinality_equals_set_cover(encoding))

    def test_exhaustive_three_by_three_incidence_instances(self):
        universe = (0, 1, 2)
        sensor_names = ("A", "B", "C")
        checked_instances = 0
        checked_subsets = 0

        # 3 candidate sets x 3 universe elements -> 9 incidence bits.
        for bits in itertools.product((0, 1), repeat=9):
            sets = {}
            cursor = 0
            for sensor in sensor_names:
                values = set()
                for element in universe:
                    if bits[cursor]:
                        values.add(element)
                    cursor += 1
                sets[sensor] = values

            encoding = encode_set_cover_as_modular_sensors(universe, sets)
            for size in range(4):
                for selected in itertools.combinations(sensor_names, size):
                    self.assertEqual(
                        selected_sets_cover(encoding, selected),
                        selected_sensors_reflect_all_codebooks(encoding, selected),
                    )
                    checked_subsets += 1

            self.assertTrue(minimum_sensor_cardinality_equals_set_cover(encoding))
            checked_instances += 1

        self.assertEqual(checked_instances, 2 ** 9)
        self.assertEqual(checked_subsets, (2 ** 9) * (2 ** 3))

    def test_infeasible_element_is_unreflectable_by_every_allowed_sensor_family(self):
        encoding = encode_set_cover_as_modular_sensors(
            ("covered", "missing"),
            {
                "A": {"covered"},
                "B": {"covered"},
            },
        )
        self.assertIsNone(minimum_set_cover_exact(encoding))
        self.assertIsNone(minimum_sensor_cover_exact(encoding))
        self.assertTrue(minimum_sensor_cardinality_equals_set_cover(encoding))

        # missing belongs to no set, so its difference is product of all sensor
        # primes and every allowed prime sensor divides it.
        difference = next(
            value
            for value in encoding.contextual_codebooks["missing"]
            if value != 0
        )
        self.assertEqual(difference, 2 * 3)
        for selected in (("A",), ("B",), ("A", "B")):
            self.assertFalse(selected_sensors_reflect_all_codebooks(encoding, selected))

    def test_weighted_reduction_preserves_optimal_cost(self):
        encoding = encode_set_cover_as_modular_sensors(
            (0, 1, 2, 3),
            {
                "cheap-left": {0, 1},
                "cheap-right": {2, 3},
                "expensive-all": {0, 1, 2, 3},
            },
        )
        costs = {
            "cheap-left": 2,
            "cheap-right": 2,
            "expensive-all": 7,
        }
        sensor = minimum_weight_sensor_cover_exact(encoding, costs)
        cover = minimum_weight_set_cover_exact(encoding, costs)
        self.assertEqual(sensor[1], 4.0)
        self.assertEqual(cover[1], 4.0)
        self.assertTrue(weighted_reduction_equivalence_holds(encoding, costs))

        # Reverse costs: the one-set solution becomes optimum on both sides.
        costs2 = {
            "cheap-left": 4,
            "cheap-right": 4,
            "expensive-all": 5,
        }
        sensor2 = minimum_weight_sensor_cover_exact(encoding, costs2)
        cover2 = minimum_weight_set_cover_exact(encoding, costs2)
        self.assertEqual(sensor2[1], 5.0)
        self.assertEqual(cover2[1], 5.0)
        self.assertTrue(weighted_reduction_equivalence_holds(encoding, costs2))

    def test_empty_universe_needs_no_sensor(self):
        encoding = encode_set_cover_as_modular_sensors((), {})
        self.assertEqual(minimum_sensor_cover_exact(encoding), ())
        self.assertEqual(minimum_set_cover_exact(encoding), ())
        self.assertTrue(selected_sensors_reflect_all_codebooks(encoding, ()))
        self.assertTrue(selected_sets_cover(encoding, ()))

    def test_validation(self):
        with self.assertRaises(ValueError):
            encode_set_cover_as_modular_sensors((0, 0), {"A": {0}})
        with self.assertRaises(ValueError):
            encode_set_cover_as_modular_sensors((0,), {"A": {1}})
        with self.assertRaises(ValueError):
            encode_set_cover_as_modular_sensors((0,), {})


if __name__ == "__main__":
    unittest.main()
