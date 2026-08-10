import unittest
from itertools import product

from enterprise_math.operation_quotient_duality import (
    elementary_family_descends,
    elementary_translations,
    finitary_family_descends,
    interval_lattice_identity_holds,
    stable_finitary_observation_congruence,
)


def _table(states, function):
    return {
        inputs: function(*inputs)
        for inputs in product(states, repeat=2)
    }


def _restricted_growth_partitions(n):
    result = []

    def visit(index, labels, maximum):
        if index == n:
            result.append(tuple(labels))
            return
        for label in range(maximum + 2):
            labels.append(label)
            visit(index + 1, labels, max(maximum, label))
            labels.pop()

    visit(1, [0], 0)
    return tuple(result)


class OperationQuotientDualityTests(unittest.TestCase):
    def test_elementary_translation_compiler_matches_direct_congruence_test(self):
        states = (0, 1, 2)
        operation_families = (
            {"min": _table(states, min)},
            {"max": _table(states, max)},
            {"min": _table(states, min), "max": _table(states, max)},
            {"cyclic_add": _table(states, lambda x, y: (x + y) % 3)},
            {"left": _table(states, lambda x, _y: x)},
        )
        for labels in _restricted_growth_partitions(len(states)):
            partition = dict(zip(states, labels))
            for operations in operation_families:
                self.assertEqual(
                    finitary_family_descends(states, operations, partition),
                    elementary_family_descends(states, operations, partition),
                )

    def test_binary_operation_compiles_all_coordinate_contexts(self):
        states = (0, 1, 2)
        translations = elementary_translations(
            states, {"min": _table(states, min)}
        )
        # Two coordinates times three choices for the fixed parameter.
        self.assertEqual(len(translations), 6)
        self.assertEqual(
            translations[("min", 0, (1,))],
            {0: 0, 1: 1, 2: 1},
        )
        self.assertEqual(
            translations[("min", 1, (1,))],
            {0: 0, 1: 1, 2: 1},
        )

    def test_min_max_leave_convex_interval_observation_unchanged(self):
        states = tuple(range(7))
        operations = {
            "min": _table(states, min),
            "max": _table(states, max),
        }
        observation = {
            0: 0,
            1: 0,
            2: 1,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
        }
        stable = stable_finitary_observation_congruence(
            states, operations, observation
        )
        self.assertEqual(stable, observation)

    def test_min_detects_nonconvex_observation_and_refines_it(self):
        states = (0, 1, 2)
        observation = {0: 0, 1: 1, 2: 0}
        stable = stable_finitary_observation_congruence(
            states,
            {"min": _table(states, min)},
            observation,
        )
        self.assertEqual(len(set(stable.values())), 3)

    def test_total_operation_language_always_admits_equality_and_universal(self):
        states = (0, 1, 2)
        operations = {
            "cyclic_add": _table(states, lambda x, y: (x + y) % 3),
            "min": _table(states, min),
        }
        equality = {state: state for state in states}
        universal = {state: 0 for state in states}
        self.assertTrue(finitary_family_descends(states, operations, equality))
        self.assertTrue(finitary_family_descends(states, operations, universal))

    def test_p008_interval_min_max_identities_for_irregular_and_polynomial_growth(self):
        samples = (
            (0, 1, 3, 6, 10, 15),
            tuple(k * k for k in range(8)),
            tuple(k**3 for k in range(6)),
        )
        for boundaries in samples:
            for x in range(boundaries[-1]):
                for y in range(boundaries[-1]):
                    self.assertTrue(
                        interval_lattice_identity_holds(boundaries, x, y)
                    )


if __name__ == "__main__":
    unittest.main()
