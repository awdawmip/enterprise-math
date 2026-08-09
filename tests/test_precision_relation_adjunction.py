import unittest
from itertools import product

from enterprise_math.precision_relation_adjunction import (
    existential_image,
    powerset_adjunction_holds,
    universal_residual,
)


def subsets(values):
    values = tuple(values)
    for mask in range(1 << len(values)):
        yield frozenset(
            value for index, value in enumerate(values) if mask & (1 << index)
        )


class PrecisionRelationAdjunctionTests(unittest.TestCase):
    def test_existential_image_and_universal_residual(self):
        relation = frozenset({(0, "a"), (0, "b"), (1, "b")})
        self.assertEqual(existential_image(relation, {0}), frozenset({"a", "b"}))
        self.assertEqual(
            universal_residual(relation, {0, 1, 2}, {"b"}), frozenset({1, 2})
        )

    def test_adjunction_holds_for_every_two_by_two_relation(self):
        sources = (0, 1)
        targets = ("a", "b")
        pairs = tuple(product(sources, targets))
        checked = 0
        for mask in range(1 << len(pairs)):
            relation = frozenset(
                pairs[index]
                for index in range(len(pairs))
                if mask & (1 << index)
            )
            for source_subset in subsets(sources):
                for target_subset in subsets(targets):
                    self.assertTrue(
                        powerset_adjunction_holds(
                            relation, sources, source_subset, target_subset
                        )
                    )
                    checked += 1
        self.assertEqual(checked, 256)

    def test_generic_adjunction_does_not_require_seriality_or_functionality(self):
        relation = frozenset({(0, "a"), (0, "b")})
        self.assertTrue(powerset_adjunction_holds(relation, {0, 1}, {1}, set()))
        self.assertTrue(
            powerset_adjunction_holds(relation, {0, 1}, {0}, {"a", "b"})
        )


if __name__ == "__main__":
    unittest.main()
