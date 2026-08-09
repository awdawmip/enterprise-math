import unittest

from enterprise_math.causal_coupling_complex import (
    coupling_order,
    is_downward_closed,
    minimal_coupling_groups,
)


class CausalCouplingComplexTests(unittest.TestCase):
    def test_pairwise_independent_but_irreducibly_triple_coupled(self):
        universe = ("A", "B", "C")
        independent = frozenset(
            {
                frozenset({"A"}),
                frozenset({"B"}),
                frozenset({"C"}),
                frozenset({"A", "B"}),
                frozenset({"A", "C"}),
                frozenset({"B", "C"}),
            }
        )
        self.assertTrue(is_downward_closed(universe, independent))
        self.assertEqual(
            minimal_coupling_groups(universe, independent),
            (frozenset({"A", "B", "C"}),),
        )
        self.assertEqual(coupling_order(universe, independent), 3)

    def test_pair_coupling_is_a_minimal_nonface(self):
        universe = ("A", "B", "C")
        independent = frozenset(
            {
                frozenset({"A"}),
                frozenset({"B"}),
                frozenset({"C"}),
                frozenset({"A", "C"}),
                frozenset({"B", "C"}),
            }
        )
        self.assertEqual(
            minimal_coupling_groups(universe, independent),
            (frozenset({"A", "B"}),),
        )
        self.assertEqual(coupling_order(universe, independent), 2)

    def test_fully_independent_family_has_no_coupling_order(self):
        universe = ("A", "B", "C")
        independent = frozenset(
            {
                frozenset({"A"}),
                frozenset({"B"}),
                frozenset({"C"}),
                frozenset({"A", "B"}),
                frozenset({"A", "C"}),
                frozenset({"B", "C"}),
                frozenset({"A", "B", "C"}),
            }
        )
        self.assertEqual(minimal_coupling_groups(universe, independent), ())
        self.assertIsNone(coupling_order(universe, independent))

    def test_non_downward_family_is_rejected(self):
        universe = ("A", "B", "C")
        invalid = frozenset({frozenset({"A", "B"}), frozenset({"A"})})
        self.assertFalse(is_downward_closed(universe, invalid))
        with self.assertRaises(ValueError):
            minimal_coupling_groups(universe, invalid)


if __name__ == "__main__":
    unittest.main()
