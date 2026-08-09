import itertools
import unittest

from enterprise_math.relational_spectrum import (
    function_collision_spectrum,
    function_graph_relation,
    relation_overlap_spectrum,
)


class RelationalSpectrumTests(unittest.TestCase):
    def test_every_small_function_specializes_exactly(self):
        size = 4
        sources = tuple(range(size))
        for values in itertools.product(range(size), repeat=size):
            mapping = dict(zip(sources, values, strict=True))
            relation = function_graph_relation(mapping)
            self.assertEqual(
                relation_overlap_spectrum(relation, max_order=size),
                function_collision_spectrum(mapping, max_order=size),
            )

    def test_functional_order_one_is_domain_size(self):
        mapping = {0: "a", 1: "a", 2: "b", 3: "c", 4: "c"}
        spectrum = dict(
            relation_overlap_spectrum(function_graph_relation(mapping), max_order=5)
        )
        self.assertEqual(spectrum[1], len(mapping))
        self.assertEqual(spectrum[2], 2)

    def test_multivalued_relation_can_create_nontransitive_pair_support(self):
        # Sources a,b,c have supports {x}, {x,y}, {y}.  Pairwise common-target
        # support is a-b and b-c but not a-c, impossible for equality fibers of
        # one single-valued function.
        relation = frozenset(
            {
                ("a", "x"),
                ("b", "x"),
                ("b", "y"),
                ("c", "y"),
            }
        )
        spectrum = dict(relation_overlap_spectrum(relation, max_order=3))
        self.assertEqual(spectrum, {1: 4, 2: 2, 3: 0})

    def test_one_source_can_contribute_multiple_order_one_memberships(self):
        relation = frozenset({("a", 1), ("a", 2), ("b", 2)})
        spectrum = dict(relation_overlap_spectrum(relation, max_order=2))
        self.assertEqual(spectrum[1], 3)
        self.assertEqual(spectrum[2], 1)

    def test_zero_max_order_is_empty(self):
        self.assertEqual(relation_overlap_spectrum(frozenset(), max_order=0), ())


if __name__ == "__main__":
    unittest.main()
