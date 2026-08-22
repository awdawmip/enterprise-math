import itertools
import unittest

from enterprise_math.finite_symmetry import (
    canonical_choice_obstruction,
    enumerate_equivariant_maps,
    equivariant_map_count,
    global_fixed_points,
    orbit_partition,
    stabilizer,
    validate_finite_group_action,
)


class FiniteSymmetryTests(unittest.TestCase):
    @staticmethod
    def s3_action():
        elements = (0, 1, 2)
        actions = {}
        for permutation in itertools.permutations(elements):
            actions[permutation] = {element: permutation[element] for element in elements}
        return elements, actions

    def test_s3_orbit_stabilizer_and_choice_obstruction(self):
        elements, actions = self.s3_action()
        validate_finite_group_action(elements, actions)
        self.assertEqual(orbit_partition(elements, actions), (frozenset(elements),))
        self.assertEqual(len(stabilizer(elements, actions, 0)), 2)
        self.assertEqual(global_fixed_points(elements, actions), frozenset())
        self.assertTrue(canonical_choice_obstruction(elements, actions))

    def test_r064_component_carrier_has_exactly_three_equivariant_binary_maps(self):
        elements, actions = self.s3_action()
        domain = tuple(itertools.product(elements, repeat=2))
        domain_actions = {
            name: {pair: (action[pair[0]], action[pair[1]]) for pair in domain}
            for name, action in actions.items()
        }
        count = equivariant_map_count(domain, elements, domain_actions, actions)
        self.assertEqual(count, 3)
        maps = enumerate_equivariant_maps(domain, elements, domain_actions, actions)
        self.assertEqual(len(maps), 3)
        signatures = {
            tuple(mapping[pair] for pair in domain)
            for mapping in maps
        }
        self.assertEqual(len(signatures), 3)

    def test_identity_action_has_no_choice_obstruction(self):
        elements = ("a", "b")
        actions = {"id": {"a": "a", "b": "b"}}
        self.assertEqual(global_fixed_points(elements, actions), frozenset(elements))
        self.assertFalse(canonical_choice_obstruction(elements, actions))


if __name__ == "__main__":
    unittest.main()
