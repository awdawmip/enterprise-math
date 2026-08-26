import unittest

from enterprise_math.equivariant_section import (
    enumerate_equivariant_sections,
    equivariant_section_count,
    equivariant_section_obstructions,
    stabilizer_fixed_lifts,
    validate_equivariant_projection,
)


class EquivariantSectionTests(unittest.TestCase):
    def test_stabilizer_without_fixed_lift_obstructs_section(self):
        base = ("b",)
        total = ("0", "1")
        base_actions = {
            "id": {"b": "b"},
            "swap": {"b": "b"},
        }
        total_actions = {
            "id": {"0": "0", "1": "1"},
            "swap": {"0": "1", "1": "0"},
        }
        projection = {"0": "b", "1": "b"}

        validate_equivariant_projection(
            total, base, total_actions, base_actions, projection
        )
        self.assertEqual(equivariant_section_count(
            total, base, total_actions, base_actions, projection
        ), 0)
        obstructions = equivariant_section_obstructions(
            total, base, total_actions, base_actions, projection
        )
        self.assertEqual(len(obstructions), 1)
        self.assertEqual(obstructions[0][0], "b")
        self.assertEqual(set(obstructions[0][1]), {"id", "swap"})
        self.assertEqual(set(obstructions[0][2]), {"0", "1"})

    def test_fixed_lift_gives_unique_section(self):
        base = ("b",)
        total = ("fixed", "0", "1")
        base_actions = {
            "id": {"b": "b"},
            "swap": {"b": "b"},
        }
        total_actions = {
            "id": {"fixed": "fixed", "0": "0", "1": "1"},
            "swap": {"fixed": "fixed", "0": "1", "1": "0"},
        }
        projection = {"fixed": "b", "0": "b", "1": "b"}

        data = stabilizer_fixed_lifts(
            total, base, total_actions, base_actions, projection
        )
        self.assertEqual(data[0][3], ("fixed",))
        self.assertEqual(equivariant_section_count(
            total, base, total_actions, base_actions, projection
        ), 1)
        self.assertEqual(
            enumerate_equivariant_sections(
                total, base, total_actions, base_actions, projection
            ),
            ({"b": "fixed"},),
        )

    def test_two_sections_propagate_across_base_orbit(self):
        base = (0, 1)
        total = ("a0", "a1", "b0", "b1")
        base_actions = {
            "id": {0: 0, 1: 1},
            "swap": {0: 1, 1: 0},
        }
        total_actions = {
            "id": {"a0": "a0", "a1": "a1", "b0": "b0", "b1": "b1"},
            "swap": {"a0": "a1", "a1": "a0", "b0": "b1", "b1": "b0"},
        }
        projection = {"a0": 0, "a1": 1, "b0": 0, "b1": 1}

        self.assertEqual(equivariant_section_count(
            total, base, total_actions, base_actions, projection
        ), 2)
        sections = enumerate_equivariant_sections(
            total, base, total_actions, base_actions, projection
        )
        self.assertEqual(
            {tuple(section[item] for item in base) for section in sections},
            {("a0", "a1"), ("b0", "b1")},
        )

    def test_projection_must_be_equivariant(self):
        base = (0, 1)
        total = ("x0", "x1")
        base_actions = {
            "id": {0: 0, 1: 1},
            "swap": {0: 1, 1: 0},
        }
        total_actions = {
            "id": {"x0": "x0", "x1": "x1"},
            "swap": {"x0": "x1", "x1": "x0"},
        }
        bad_projection = {"x0": 0, "x1": 0}
        with self.assertRaises(ValueError):
            validate_equivariant_projection(
                total, base, total_actions, base_actions, bad_projection
            )


if __name__ == "__main__":
    unittest.main()
